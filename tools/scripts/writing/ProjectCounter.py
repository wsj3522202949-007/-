#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
ProjectCounter.py —— 项目统计单一真源
=======================================

原子生成 STATUS.md 的统计区块，并回写每章 frontmatter 的 word_count。

背景
----
update_progress() 用 12 条正则分别在 STATUS.md 里零散替换统计数字——
正则匹配失败/格式漂移/多次部分更新 → STATUS.md 同时存在互相矛盾的数字
（38,333 vs 36,111 vs 37,445；43% vs 13%；13% vs 12%），另有 10 章
frontmatter word_count 漂移合计 579 字。

设计
----
- 扫描 chapters/ 全部正式章节，统一 extract_body+count_chars 实算
- 原子替换 STATUS.md 中两块统计区域内的**全部内容**（不零散拼凑）：
  1) ## 📊 当前进度 到 ## ✅ 已完成内容 之间（含表头行）
  2) ## 📊 创作统计 到 ## ⚠️ 注意事项 之间
- 回写每章 frontmatter 的 word_count（只在实算值与记录值不同时修改）
- 更新 STATUS.md frontmatter 的 updated

用法
----
  python ProjectCounter.py （已删除项目）
  python ProjectCounter.py （已删除项目） --dry-run
  python ProjectCounter.py （已删除项目）
  python ProjectCounter.py --all
"""

import os
import re
import sys
import json
import argparse
import importlib.util
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

_HERE = os.path.dirname(os.path.abspath(__file__))
_SC_PATH = os.path.join(_HERE, "chapter_selfcheck.py")
_spec = importlib.util.spec_from_file_location("chapter_selfcheck", _SC_PATH)
_chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_chk)


def find_root():
    d = _HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "projects")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(_HERE)


def find_projects(root):
    """projects/*/ 有 chapters/ 目录的项目名列表。"""
    out = []
    proj = os.path.join(root, "projects")
    if os.path.isdir(proj):
        for name in sorted(os.listdir(proj)):
            if os.path.isdir(os.path.join(proj, name, "chapters")):
                out.append(name)
    return out


def count_project(project_dir):
    """扫描 chapters/ 返回 (chapter_num, total_words, per_chapter, policy)。

    per_chapter: dict[filename] -> word_count
    header: project_dir 下的主标题
    """
    ch_dir = os.path.join(project_dir, "chapters")
    policy = _chk.load_policy(ch_dir)
    total = 0
    per = {}
    header = ""
    if not os.path.isdir(ch_dir):
        return 0, 0, {}, policy, ""

    # 取项目名（用于表格标题）
    header = os.path.basename(project_dir)

    for fname in sorted(os.listdir(ch_dir)):
        if not fname.startswith("第") or not fname.endswith(".md"):
            continue
        if fname == "README.md":
            continue
        r = _chk.check_chapter(os.path.join(ch_dir, fname), policy=policy)
        per[fname] = r["chars"]
        total += r["chars"]
    return len(per), total, per, policy, header


def parse_frontmatter(text):
    """极简 frontmatter 解析（纯文本操作，避免导入其他模块）。"""
    if not text.startswith("---"):
        return None, 0
    lines = text.split("\n")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, 0
    fm = {}
    for line in lines[1:end]:
        m = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm, end


def sync_frontmatter_wordcount(chapter_path, actual):
    """回写章节文件的 frontmatter word_count 字段。

    只在实算值与记录值不同时修改；首次写入（之前不存在该字段）也触发。
    返回 (old_int_or_None, actual, changed)。
    """
    with open(chapter_path, "r", encoding="utf-8") as f:
        raw = f.read()
    fm, fm_end = parse_frontmatter(raw)
    if fm is None:
        return None, actual, False
    old = fm.get("word_count", None)
    if old is None:
        old_int = None
    else:
        try:
            old_int = int(str(old).strip())
        except (ValueError, TypeError):
            old_int = None
    if old_int == actual:
        return old_int, actual, False

    lines = raw.split("\n")
    new_lines = []
    found = False
    for i, line in enumerate(lines):
        m = re.match(r'^word_count:\s*(\d+)', line)
        if m and i < fm_end:
            # 替换已有 word_count 行
            new_lines.append(f"word_count: {actual}")
            found = True
        else:
            new_lines.append(line)
    if not found:
        # 新增 word_count 字段（插在 fm 末尾行 --- 之前）
        insert_at = fm_end
        # 找 frontmatter 结束前的最后一行
        for i in range(fm_end - 1, 0, -1):
            if lines[i].strip() and not lines[i].strip().startswith("---"):
                insert_at = i + 1
                break
        new_lines = lines[:insert_at] + [f"word_count: {actual}"] + lines[insert_at:]

    new_text = "\n".join(new_lines)
    with open(chapter_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    return old_int, actual, True


# ---------------------------------------------------------------------------
# 原子块生成：用 section header 精确界定替换范围
# ---------------------------------------------------------------------------
_TOP_HEADER = "## 📊 当前进度"
_TOP_NEXT = "## ✅ 已完成内容"
_BOTTOM_HEADER = "## 📊 创作统计"
_BOTTOM_NEXT = "## ⚠️ 注意事项"


def _build_top_block(chapter_num, total_words, header, policy):
    """生成顶部进度表的全部内容（替代 ## 📊 当前进度 到 ## ✅ 已完成内容 之间）。"""
    avg = total_words // chapter_num if chapter_num else 0
    completion_pct = chapter_num / 30  # 第一卷 30 章
    word_pct = total_words / 300000   # 目标 30 万字
    return f"""## 📊 当前进度

| 维度 | 进度 | 口径说明 |
|---|---|---|
| 章节进度 | **{completion_pct:.0%}** | {chapter_num}/30 章（第一卷）|
| 字数进度 | **~{word_pct:.0%}** | {total_words:,} / 300,000 字（正文去空白口径）|
| 当前阶段 | — | — |
| 当前章节 | 第{chapter_num}章 | — |
| 下一章节 | 第{chapter_num + 1}章 | 待创作 |
| 存稿正文 | ~{total_words:,}字 | {chapter_num}章合计，均~{avg}字/章 |
| 目标字数 | 300,000 字 | 第一卷目标 |

### 篇幅策略（v2 两级判级，全章统一适用）

| 区间 | 范围 | 级别 | 说明 |
|---|---|---|---|
| 目标区间 | {policy['soft_min']}–{policy['soft_max']} | 警告 | 低于或高于仅警告，不阻断流程 |
| 硬性区间 | {policy['hard_min']}–{policy['hard_max']} | 阻断 | 超出才阻断，阻止入库 |

> 此区块由 ProjectCounter 原子生成，禁止手工编辑。
"""


def _build_bottom_block(chapter_num, total_words):
    """生成底部创作统计表的全部内容。"""
    avg = total_words // chapter_num if chapter_num else 0
    days = max(1, chapter_num // 3)  # 保守估计
    return f"""## 📊 创作统计

| 指标 | 数值 | 备注 |
|---|---|---|
| 总章节数 | {chapter_num} 章 | 第1-{chapter_num}章 |
| 章节完成率 | {chapter_num}/30 = {chapter_num/30:.0%} | 第一卷 30 章 |
| 正文总字数 | ~{total_words:,}字 | 均~{avg}字/章 |
| 字数完成率 | {total_words/300000:.1%} | {total_words:,} / 300,000 字 |
| 存稿天数 | {days} 天 | 按日更 6000 字计算 |
| 重写章节 | — | — |
| 新政策章节 | — | — |

> 此区块由 ProjectCounter 原子生成，禁止手工编辑。
"""


def replace_between(content, start_header, end_header, replacement):
    """在 content 中，把 start_header 那一行到 end_header 前一行的整块替换为 replacement。

    replacement 应包含 start_header 行自身。如果找不到 start_header 或 end_header，返回原内容。
    """
    # 定位两个 header 的起止行
    lines = content.split("\n")
    si = None
    ei = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if si is None and stripped == start_header:
            si = i
        if si is not None and ei is None and stripped == end_header:
            ei = i
            break
    if si is None or ei is None:
        return content
    return "\n".join(lines[:si] + [replacement.rstrip("\n")] + lines[ei:])


def apply_stats(project_dir, chapter_num, total_words, per_chapter, policy, header,
                dry_run=False):
    """核心：原子替换 STATUS.md 两个统计区块 + 回写 frontmatter。"""
    status_path = os.path.join(project_dir, "STATUS.md")
    ch_dir = os.path.join(project_dir, "chapters")
    changed = []

    # ---- 1) 回写每章 frontmatter word_count ----
    for fname, actual in per_chapter.items():
        path = os.path.join(ch_dir, fname)
        old, new, touched = sync_frontmatter_wordcount(path, actual)
        if touched:
            if dry_run:
                print(f"  [DRY-RUN] {fname}: word_count {old} → {new}")
            else:
                print(f"  {fname}: word_count {old} → {new}")
            changed.append(fname)

    # ---- 2) 原子替换 STATUS.md 统计块 ----
    if not os.path.exists(status_path):
        print(f"  ⚠️ STATUS.md 不存在: {status_path}")
        return changed

    with open(status_path, "r", encoding="utf-8") as f:
        content = f.read()

    top = _build_top_block(chapter_num, total_words, header, policy)
    content = replace_between(content, _TOP_HEADER, _TOP_NEXT, top)

    bottom = _build_bottom_block(chapter_num, total_words)
    content = replace_between(content, _BOTTOM_HEADER, _BOTTOM_NEXT, bottom)

    # 更新 STATUS.md 自己的 frontmatter updated 和首页日期
    today = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(r'updated:\s*\d{4}-\d{2}-\d{2}', f'updated: {today}',
                     content, count=1)
    content = re.sub(
        r'最后更新时间：\d{4}-\d{2}-\d{2}',
        f'最后更新时间：{today}', content, count=1)

    if dry_run:
        print(f"\n  [DRY-RUN] STATUS.md 统计块已生成（未写盘）:")
        # 打印 diff 摘要
        old_lines = open(status_path, "r", encoding="utf-8").read().split("\n")
        new_lines = content.split("\n")
        print(f"    章节: {chapter_num}章 | 正文: {total_words:,}字 | "
              f"均: {total_words//chapter_num}字 | "
              f"卷完成率: {chapter_num/30:.0%}")
    else:
        with open(status_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\n  STATUS.md 两个统计区块已原子替换")
        print(f"    章节: {chapter_num}章 | 正文: {total_words:,}字 | "
              f"均: {total_words//chapter_num}字 | "
              f"卷完成率: {chapter_num/30:.0%} | "
              f"frontmatter回写: {len(changed)}章")

    return changed


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="项目统计单一真源")
    ap.add_argument("project", nargs="?", default=None,
                    help="项目名（如 （已删除项目））或 --all")
    ap.add_argument("--all", action="store_true", help="全部项目")
    ap.add_argument("--dry-run", action="store_true", help="仅显示要改的内容，不写盘")
    ap.add_argument("--root", default=None)
    args = ap.parse_args()

    root = os.path.abspath(args.root) if args.root else find_root()
    targets = []
    if args.all or args.project is None:
        targets = find_projects(root)
    else:
        targets = [args.project]

    if not targets:
        print("未找到任何含 chapters/ 的项目。")
        return

    any_changed = False
    for proj_name in targets:
        proj_dir = os.path.join(root, "projects", proj_name)
        print(f"\n{'=' * 60}")
        print(f"项目: {proj_name}")
        cn, tw, pc, policy, hdr = count_project(proj_dir)
        if cn == 0:
            print("  (无章节文件)")
            continue
        print(f"  实算: {cn}章 | {tw:,}字 | 均{tw//cn}字 | 卷完成率{cn/30:.0%}")
        changed = apply_stats(proj_dir, cn, tw, pc, policy, hdr,
                              dry_run=args.dry_run)
        if changed:
            any_changed = True

    if args.dry_run:
        print("\n⚠️ --dry-run 模式：上述修改不会落盘。去掉 --dry-run 后正式执行。")


if __name__ == "__main__":
    main()
