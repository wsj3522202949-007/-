#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Wikilink → Markdown 链接批量转换脚本
=====================================

将 Obsidian 专属的 [[target|alias]] / [[target]] 语法转换为标准 markdown 链接
[alias](relative-path.md)，使 AI/RAG 管道可稳定消费。

转换规则见《维护/链接规范.md》§五。

跳过的情况：
  - 代码块（``` 和 `）内的字面 [[...]]
  - Dataview 查询块（```dataview ... ```）内的 [[...]]
  - frontmatter（--- ... ---）内的 [[...]]
  - 无法解析的短名 wikilink（仅报告不转换）

用法
----
    python 维护/wikilink_to_md.py                    # dry-run，只报告会转换什么
    python 维护/wikilink_to_md.py --apply             # 实际执行转换
    python 维护/wikilink_to_md.py --dir 通用小说创作流程  # 只转换指定目录
    python 维护/wikilink_to_md.py --json              # 机器可读输出
"""

import os
import re
import sys
import json
from pathlib import Path

# Windows GBK 终端安全：避免 emoji/中文输出 UnicodeEncodeError
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass


# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------
SKIP_DIRS = {".git", ".workbuddy", "archive", "__pycache__"}
# 工具卡目录：外部 GitHub README 原文，其 wikilink 非本 vault 链接，跳过
README_DIR_PARTS = ("库", "enriched", "readmes")
WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')
FENCE_RE = re.compile(r'```[^\n]*\n.*?```', re.DOTALL)
INLINE_CODE_RE = re.compile(r'`[^`\n]*`')

# ---------------------------------------------------------------------------
# 路径解析
# ---------------------------------------------------------------------------
def find_root(start=None):
    d = os.path.dirname(os.path.abspath(start or __file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "库", "enriched", "readmes")) or \
           os.path.isdir(os.path.join(d, "维护")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.abspath(start or __file__))


def build_file_index(root):
    """构建 vault 根相对路径 → 绝对路径 的索引，用于解析短名 wikilink。"""
    index = {}
    for dp, dn, fn in os.walk(root):
        if any(s in dp.split(os.sep) for s in SKIP_DIRS):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, root).replace(os.sep, "/")
            index[rel] = p
            # 也按文件名索引（用于短名解析）
            basename = f
            if basename not in index:
                index[basename] = p
    return index


def resolve_target(root, file_index, file_dir, target):
    """解析 wikilink target 为 vault 根相对路径。
    返回 (vault_rel_path, display_name) 或 None（无法解析）。
    """
    target = target.split("#")[0].split("^")[0].strip()
    if not target:
        return None

    # 去掉 .md 后缀再统一加
    base = target[:-3] if target.endswith(".md") else target

    # 候选路径
    candidates = [
        base,                    # vault 根相对（如 库/工具选型指南）
        base + ".md",
        os.path.normpath(os.path.join(file_dir, base)).replace(os.sep, "/"),
        os.path.normpath(os.path.join(file_dir, base + ".md")).replace(os.sep, "/"),
    ]

    # 尝试匹配
    for cand in candidates:
        cand_norm = cand.replace("\\", "/")
        if cand_norm in file_index:
            abs_path = file_index[cand_norm]
            vault_rel = os.path.relpath(abs_path, root).replace(os.sep, "/")
            display = os.path.splitext(os.path.basename(vault_rel))[0]
            return vault_rel, display

    # 短名匹配：在 file_index 中找 basename 匹配
    basename = os.path.basename(base) + ".md"
    if basename in file_index:
        abs_path = file_index[basename]
        vault_rel = os.path.relpath(abs_path, root).replace(os.sep, "/")
        display = os.path.splitext(basename)[0]
        return vault_rel, display

    return None


def vault_rel_to_file_rel(current_vault_rel, target_vault_rel):
    """计算从当前文件到目标文件的相对路径（markdown 链接用）。"""
    current_dir = os.path.dirname(current_vault_rel)
    rel = os.path.relpath(target_vault_rel, current_dir).replace(os.sep, "/")
    return rel


# ---------------------------------------------------------------------------
# 代码块/ frontmatter 保护
# ---------------------------------------------------------------------------
def mask_protected_regions(text):
    """将代码块、inline code、frontmatter 中的内容替换为占位符，保护它们不被转换。
    返回 (masked_text, replacements) 其中 replacements 是 {placeholder: original}。
    """
    replacements = {}
    counter = [0]

    def make_placeholder(matched_text):
        key = f"\x00PROTECTED_{counter[0]}\x00"
        replacements[key] = matched_text
        counter[0] += 1
        return key

    # frontmatter
    if text.startswith("---"):
        lines = text.split("\n")
        end = None
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                end = i
                break
        if end is not None:
            fm = "\n".join(lines[:end + 1])
            masked_fm = make_placeholder(fm)
            text = masked_fm + "\n" + "\n".join(lines[end + 1:])

    # fenced code blocks
    def replace_fence(m):
        return make_placeholder(m.group(0))
    text = FENCE_RE.sub(replace_fence, text)

    # inline code
    text = INLINE_CODE_RE.sub(replace_fence, text)

    return text, replacements


def unmask(text, replacements):
    for key, original in replacements.items():
        text = text.replace(key, original)
    return text


# ---------------------------------------------------------------------------
# 转换
# ---------------------------------------------------------------------------
def convert_text(text, root, file_index, vault_rel_path):
    """转换单个文件的 wikilink。返回 (new_text, stats)。"""
    file_dir = os.path.dirname(os.path.join(root, vault_rel_path))
    masked, replacements = mask_protected_regions(text)

    stats = {"converted": 0, "skipped": 0, "errors": []}

    def replace_wikilink(m):
        inner = m.group(1)
        # 分离 target 和 alias（表格中 | 被转义为 \|，两种都要处理）
        if "\\|" in inner:
            target, alias = inner.split("\\|", 1)
            target = target.strip()
            alias = alias.strip()
        elif "|" in inner:
            target, alias = inner.split("|", 1)
            target = target.strip()
            alias = alias.strip()
        else:
            target = inner.strip()
            alias = None

        # 跳过 ... （占位符）
        if target == "...":
            stats["skipped"] += 1
            return m.group(0)

        resolved = resolve_target(root, file_index, file_dir, target)
        if resolved is None:
            stats["skipped"] += 1
            stats["errors"].append(f"无法解析: [[{inner}]]")
            return m.group(0)  # 保留原样

        target_vault_rel, default_display = resolved
        display = alias if alias else default_display

        # 计算文件相对路径
        file_rel = vault_rel_to_file_rel(vault_rel_path, target_vault_rel)

        stats["converted"] += 1
        return f"[{display}]({file_rel})"

    new_masked = WIKILINK_RE.sub(replace_wikilink, masked)
    new_text = unmask(new_masked, replacements)

    return new_text, stats


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    args = sys.argv[1:]
    apply = "--apply" in args
    as_json = "--json" in args
    target_dir = None
    for i, a in enumerate(args):
        if a == "--dir" and i + 1 < len(args):
            target_dir = args[i + 1]

    root = find_root(__file__)

    file_index = build_file_index(root)

    total_files = 0
    total_converted = 0
    total_skipped = 0
    file_results = []

    for dp, dn, fn in os.walk(root):
        if any(s in dp.split(os.sep) for s in SKIP_DIRS):
            continue
        # --dir 过滤
        if target_dir:
            rel_dir = os.path.relpath(dp, root).replace(os.sep, "/")
            if not rel_dir.startswith(target_dir) and dp != os.path.join(root, target_dir):
                continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            vault_rel = os.path.relpath(p, root).replace(os.sep, "/")

            with open(p, encoding="utf-8", errors="replace") as fh:
                text = fh.read()

            # 快速检查有无 wikilink
            if "[[" not in text:
                continue

            new_text, stats = convert_text(text, root, file_index, vault_rel)

            if stats["converted"] == 0 and stats["skipped"] == 0:
                continue

            total_files += 1
            total_converted += stats["converted"]
            total_skipped += stats["skipped"]

            file_results.append({
                "file": vault_rel,
                "converted": stats["converted"],
                "skipped": stats["skipped"],
                "errors": stats["errors"][:5],  # 只报前5个
            })

            if apply and stats["converted"] > 0:
                with open(p, "w", encoding="utf-8") as fh:
                    fh.write(new_text)

    # 输出
    if as_json:
        out = {
            "files_scanned": total_files,
            "total_converted": total_converted,
            "total_skipped": total_skipped,
            "applied": apply,
            "results": file_results,
        }
        sys.stdout.write(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    else:
        mode = "APPLIED" if apply else "DRY-RUN (use --apply to execute)"
        print(f"\n{'=' * 60}")
        print(f"Wikilink → Markdown 链接转换  ·  模式: {mode}")
        print(f"{'=' * 60}")
        print(f"涉及文件: {total_files}")
        print(f"转换链接: {total_converted}")
        print(f"跳过(无法解析): {total_skipped}")
        if file_results:
            print(f"\n按文件明细（前 30 个）:")
            for r in file_results[:30]:
                print(f"  {r['converted']:4d} 转换 / {r['skipped']:3d} 跳过  {r['file']}")
                for e in r["errors"][:2]:
                    print(f"         ⚠ {e}")
            if len(file_results) > 30:
                print(f"  ... 还有 {len(file_results) - 30} 个文件")
        print(f"{'=' * 60}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
