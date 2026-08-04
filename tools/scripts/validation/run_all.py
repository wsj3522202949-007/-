#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
统一门禁入口 run_all.py
=======================
一次命令跑完全部质量检查，输出统一 JSON。

子检查
------
  1. frontmatter 校验  —— 必填字段(id/type/area/status) + 取值合法性
  2. 项目结构校验      —— MOC、章节命名、知识单页位置
  3. 核心断链校验      —— 复用 链接检查器-修复版.run_link_check（core_errors 必须为 0）
  4. 旧路径检查        —— 绝对路径 / 旧系统路径残留
  5. 重复 ID 检查      —— 全库 id 唯一性
  6. 健康报告生成      —— 汇总为统一 JSON

验收标准
--------
  · 基础校验 0 ERROR   （frontmatter / 结构 / 旧路径 / 重复ID）
  · 核心断链 0 ERROR   （core_errors 必须为 0）
  · JSON 输出正常      （异常安全，任何时候都输出合法 JSON）
  · 外部资料不会污染核心报告（external_warnings 为独立字段，绝不并入 basic / core）

范围约定
--------
  核心区（basic + core 必查，错误即 FAIL）：
      schema / methods（模板子目录除外）/ knowledge / projects
  排除目录（完全不扫描，也不污染报告）：
      .git .workbuddy .obsidian node_modules __pycache__
      .tools / archive / references/原始来源包
  外部资料（仅产生 external_warnings，参考用，不计入核心）：
      references / tools/cards / 根目录文档 / ai / drafts 等

用法
----
  python tools/scripts/validation/run_all.py
  python tools/scripts/validation/run_all.py --json
  python tools/scripts/validation/run_all.py --json-file=gate_report.json
  python tools/scripts/validation/run_all.py --root <路径>
"""

import os
import re
import sys
import json
import traceback
import importlib.util
from datetime import datetime

# ---------------------------------------------------------------------------
# 常量（与 校验脚本.py / frontmatter规范.md / 链接检查器-修复版.py 锁死）
# ---------------------------------------------------------------------------
TYPE_VALUES = {"index", "guide", "ref", "dashboard", "template", "moc",
               "demo", "project", "chapter", "character", "setting",
               "location", "prop", "tool", "daily-note", "book-note"}
AREA_VALUES = {"库", "方法", "项目", "资料", "日记", "索引", "管理"}
STATUS_VALUES = {"active", "demo", "wip", "done", "draft", "archived"}
# 关键必填字段（缺失/非法 = ERROR）
CRITICAL_FIELDS = ("id", "type", "area", "status")
# 过渡期字段（缺失仅 WARN）
WARN_FIELDS = ("title", "summary", "created", "updated")

NS_TAG_RE = re.compile(r'^(type|area|status)/(.+)$')
# 旧路径：Windows 绝对路径（盘符:\ 或 盘符:/）+ /Users / /Program Files
# 负向后顾 (?<![A-Za-z]) 避免误伤 http(s)://、ftp:// 等 URL（其中的 s:/ 是协议一部分）
OLD_PATH_RE = re.compile(r'(?<![A-Za-z])[A-Za-z]:[\\/]|/(?:Users|Program\s*Files)')
# 章节命名契约：第NNN章-标题.md
CHAPTER_NAME_RE = re.compile(r'^第\d{3}章-.+\.md$')
# 知识单页目录（仅允许在 projects/<书名>/ 内，禁止出现在 vault 根）
KNOWLEDGE_DIRS = ("人物", "设定", "地点", "道具")
MOC_DIR = os.path.join("tools", "分类导航")

# 核心区（basic + core 必查）
CORE_DIRS = ("schema", "knowledge", "projects", "methods")
# 排除目录（路径组件匹配）
SKIP_COMPONENTS = {
    ".git", ".workbuddy", ".obsidian", "node_modules", "__pycache__",
    ".tools", "archive", "原始来源包",
}

WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')


# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------
def find_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "schema")) or \
           os.path.isdir(os.path.join(d, "tools")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def should_skip_dir(dir_path, root):
    rel = os.path.relpath(dir_path, root)
    parts = rel.split(os.sep)
    return any(c in parts for c in SKIP_COMPONENTS)


def is_core(rel):
    """判断文件是否属于核心区（basic + core 必查）。

    注意：os.path.relpath 在 Windows 返回反斜杠路径，而 CORE_DIRS /
    模板排除前缀用正斜杠书写。先统一规范为 '/'，避免 Windows 下
    模板子目录（methods/templates、methods/项目骨架模板）排除失效、
    被错划为核心区。
    """
    rel = rel.replace(os.sep, "/")
    for d in CORE_DIRS:
        if rel == d or rel.startswith(d + "/"):
            if d == "methods":
                if rel.startswith("methods/templates/") or \
                   rel.startswith("methods/项目骨架模板/"):
                    return False
            return True
    return False


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return None
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None
    fm = {}
    for line in lines[1:end]:
        m = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def strip_code(text):
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`\n]*`', '', text)
    return text


def safe_json(data):
    try:
        return json.dumps(data, ensure_ascii=False, indent=2)
    except Exception as e:  # noqa: BLE001
        return json.dumps({
            "success": False,
            "error": f"JSON 序列化失败: {e}",
        }, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# 1. frontmatter 校验（核心区）
# ---------------------------------------------------------------------------
def check_frontmatter(root):
    errors, warns = [], []
    for dp, dn, fn in os.walk(root):
        if should_skip_dir(dp, root):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dp, f), root)
            if not is_core(rel):
                continue
            try:
                with open(os.path.join(dp, f), encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
            except OSError:
                continue
            fm = parse_frontmatter(text)
            if fm is None:
                continue
            # 关键必填字段
            for k in CRITICAL_FIELDS:
                if k not in fm or not fm[k].strip():
                    errors.append(f"[frontmatter] 缺关键字段 '{k}': {rel}")
            # 取值合法性（平键）
            tv = (fm.get("type") or "").strip()
            av = (fm.get("area") or "").strip()
            sv = (fm.get("status") or "").strip()
            # 旧格式平键（type/...）降级
            if tv.startswith("type/"):
                tv = ""
            if tv and tv not in TYPE_VALUES:
                errors.append(f"[frontmatter] type 非法取值 '{tv}': {rel}")
            if av and av not in AREA_VALUES:
                errors.append(f"[frontmatter] area 非法取值 '{av}': {rel}")
            if sv and sv not in STATUS_VALUES:
                errors.append(f"[frontmatter] status 非法取值 '{sv}': {rel}")
            # 过渡期字段 / 旧命名空间标签
            for k in WARN_FIELDS:
                if k not in fm or not fm[k].strip():
                    warns.append(f"[frontmatter] 缺推荐字段 '{k}': {rel}")
            tags_raw = fm.get("tags", "")
            if tags_raw:
                for tg in re.findall(r'[\w/一-鿿]+', tags_raw):
                    if NS_TAG_RE.match(tg):
                        warns.append(f"[frontmatter] 残留旧命名空间标签 '{tg}': {rel}")
    return errors, warns


# ---------------------------------------------------------------------------
# 2. 项目结构校验（核心区 + 针对性目录）
# ---------------------------------------------------------------------------
def check_structure(root):
    errors, warns = [], []

    # MOC：tools/分类导航 下每篇需 type: moc
    moc_dir = os.path.join(root, MOC_DIR)
    if os.path.isdir(moc_dir):
        for f in sorted(os.listdir(moc_dir)):
            if not f.endswith(".md"):
                continue
            p = os.path.join(moc_dir, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                fm = parse_frontmatter(fh.read())
            if fm is None:
                errors.append(f"[structure] MOC 缺 frontmatter: {MOC_DIR}/{f}")
                continue
            ft = (fm.get("type") or "").strip()
            tags = fm.get("tags", "")
            if ft == "moc":
                continue
            if "type/moc" in tags:
                warns.append(f"[structure] MOC 旧格式 type/moc，建议迁移平键: {f}")
                continue
            errors.append(f"[structure] MOC 缺 type: moc: {MOC_DIR}/{f}")
    else:
        errors.append(f"[structure] 分类导航目录不存在: {MOC_DIR}")

    # E1 章节命名：projects/<书名>/正文|chapters 下必须为 第NNN章-标题.md
    proj = os.path.join(root, "projects")
    if os.path.isdir(proj):
        for dp, dn, fn in os.walk(proj):
            if os.path.basename(dp) in ("正文", "chapters"):
                for f in fn:
                    if f == "README.md":
                        continue
                    if not CHAPTER_NAME_RE.match(f):
                        errors.append(
                            f"[structure] 章节命名不合规 '{f}'"
                            f"（应为 第NNN章-标题.md）: {os.path.relpath(dp, root)}/")

    # E2 知识单页目录不得出现在 vault 根
    for name in KNOWLEDGE_DIRS:
        if os.path.isdir(os.path.join(root, name)):
            errors.append(
                f"[structure] 知识单页目录 '{name}/' 出现在 vault 根"
                f"（必须下沉到 projects/<书名>/entities/ 内）")
    return errors, warns


# ---------------------------------------------------------------------------
# 4. 旧路径检查（核心区内容中的绝对/旧系统路径残留）
# ---------------------------------------------------------------------------
def check_old_paths(root):
    errors, warns = [], []
    for dp, dn, fn in os.walk(root):
        if should_skip_dir(dp, root):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dp, f), root)
            if not is_core(rel):
                continue
            try:
                with open(os.path.join(dp, f), encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
            except OSError:
                continue
            body = strip_code(text)
            for m in OLD_PATH_RE.finditer(body):
                seg = m.group(0)
                errors.append(
                    f"[old_path] 发现旧/绝对路径残留 '{seg}': {rel}")
    return errors, warns


# ---------------------------------------------------------------------------
# 5. 重复 ID 检查（核心区）
# ---------------------------------------------------------------------------
def check_duplicate_ids(root):
    errors, warns = [], []
    seen = {}
    for dp, dn, fn in os.walk(root):
        if should_skip_dir(dp, root):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dp, f), root)
            if not is_core(rel):
                continue
            try:
                with open(os.path.join(dp, f), encoding="utf-8", errors="replace") as fh:
                    fm = parse_frontmatter(fh.read())
            except OSError:
                continue
            if fm is None:
                continue
            vid = (fm.get("id") or "").strip()
            if not vid:
                continue
            seen.setdefault(vid, []).append(rel)
    for vid, locs in seen.items():
        if len(locs) > 1:
            errors.append(
                f"[duplicate_id] id 重复 '{vid}'（{len(locs)} 处）: "
                + "; ".join(locs))
    return errors, warns


# ---------------------------------------------------------------------------
# 3/6. 核心断链校验（复用链接检查器） + 健康报告生成
# ---------------------------------------------------------------------------
def load_link_checker():
    quality_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "..", "quality")
    path = os.path.join(quality_dir, "链接检查器-修复版.py")
    spec = importlib.util.spec_from_file_location("link_checker_fixed", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.run_link_check


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    json_file = None
    root = None
    for a in args:
        if a.startswith("--json-file="):
            json_file = a.split("=", 1)[1]
            as_json = True
        elif a.startswith("--root="):
            root = a.split("=", 1)[1]
    if root is None:
        root = find_root()

    try:
        # —— 基础校验（核心区）——
        fm_err, fm_warn = check_frontmatter(root)
        st_err, st_warn = check_structure(root)
        op_err, op_warn = check_old_paths(root)
        di_err, di_warn = check_duplicate_ids(root)

        basic = {
            "frontmatter":  {"errors": fm_err, "warns": fm_warn},
            "structure":    {"errors": st_err, "warns": st_warn},
            "old_paths":    {"errors": op_err, "warns": op_warn},
            "duplicate_ids": {"errors": di_err, "warns": di_warn},
        }
        basic_error_count = len(fm_err) + len(st_err) + len(op_err) + len(di_err)
        basic_warn_count = len(fm_warn) + len(st_warn) + len(op_warn) + len(di_warn)
        basic_pass = basic_error_count == 0

        # —— 核心断链校验（复用链接检查器）——
        run_link_check = load_link_checker()
        lc = run_link_check(root)
        core_broken_links = lc["core_errors"]
        external_warnings = lc["external_warnings"]
        recognized = lc.get("recognized", {})
        core_pass = len(core_broken_links) == 0

        overall_pass = basic_pass and core_pass

        result = {
            "timestamp": datetime.now().isoformat(),
            "root": root,
            "summary": {
                "basic": {
                    "errors": basic_error_count,
                    "warns": basic_warn_count,
                    "pass": basic_pass,
                },
                "core_broken_links": {
                    "errors": len(core_broken_links),
                    "pass": core_pass,
                },
                "external_warnings": {
                    "count": len(external_warnings),
                },
                "overall_pass": overall_pass,
            },
            "basic_checks": basic,
            "core_broken_links": core_broken_links,
            "external_warnings": external_warnings,
        }

        if as_json:
            js = safe_json(result)
            if json_file:
                try:
                    with open(json_file, "w", encoding="utf-8") as fh:
                        json.dump(result, fh, ensure_ascii=False, indent=2)
                        fh.write("\n")
                except Exception as e:  # noqa: BLE001
                    sys.stderr.write(f"[门禁] 写入 JSON 文件失败: {e}\n")
                    sys.stdout.write(js + "\n")
            else:
                sys.stdout.write(js + "\n")
        else:
            print("=" * 64)
            print(f"统一门禁 · 根: {root}")
            print("=" * 64)
            print(f"[1] frontmatter 校验 : ERROR {len(fm_err)} | WARN {len(fm_warn)}")
            print(f"[2] 项目结构校验    : ERROR {len(st_err)} | WARN {len(st_warn)}")
            print(f"[3] 核心断链校验    : ERROR {len(core_broken_links)}（必须为 0）")
            print(f"[4] 旧路径检查      : ERROR {len(op_err)} | WARN {len(op_warn)}")
            print(f"[5] 重复 ID 检查    : ERROR {len(di_err)} | WARN {len(di_warn)}")
            print("-" * 64)
            print(f"基础校验: {'PASS ✅' if basic_pass else f'FAIL ❌ ({basic_error_count} ERROR)'}")
            print(f"核心断链: {'PASS ✅' if core_pass else f'FAIL ❌ ({len(core_broken_links)} ERROR)'}")
            print(f"外部警告: {len(external_warnings)} 条（仅供参考，不计入核心）")
            print(f"单独识别: {recognized}")
            if not basic_pass:
                for cat in basic:
                    for e in basic[cat]["errors"][:50]:
                        print(f"  ❌ {e}")
            if not core_pass:
                for e in core_broken_links[:50]:
                    print(f"  ❌ {e}")
            print("=" * 64)
            print(f"结论: {'PASS ✅ 全部通过' if overall_pass else 'FAIL ❌ 存在 ERROR'}")

        return 0 if overall_pass else 1

    except Exception as e:  # noqa: BLE001
        sys.stderr.write(f"[门禁] 运行异常: {e}\n")
        traceback.print_exc()
        err_result = {
            "success": False,
            "timestamp": datetime.now().isoformat(),
            "error": str(e),
        }
        if as_json:
            sys.stdout.write(safe_json(err_result) + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
