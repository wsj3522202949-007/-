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
  6. 编码检查          —— 严格区文件必须 UTF-8 可解码
  7. 同目录重名检查    —— 同目录同名且内容不同的真实重复文件
  8. 健康报告生成      —— 汇总为统一 JSON

验收标准
--------
  · 基础校验 0 ERROR   （frontmatter / 结构 / 旧路径 / 重复ID / 编码 / 同目录重名）
  · 核心断链 0 ERROR   （core_errors 必须为 0）
  · JSON 输出正常      （异常安全，任何时候都输出合法 JSON）
  · 外部资料不会污染核心报告（external_warnings 为独立字段，绝不并入 basic / core）

范围约定
--------
  范围划分统一由 tools/scripts/gate_scope.py 定义，本文件不再自行维护
  CORE_DIRS。历史教训：本文件与 链接检查器-修复版.py 各写一份
  CORE_DIRS（都只有 schema/knowledge/projects/methods），导致
  README / CLAUDE / ai/ / goals/ / maintenance/ / tools 导航层
  全部被降级成 external_warnings，门禁因此长期报「总体通过」——假绿灯。

  严格区（basic + 断链必查，ERROR 即 FAIL）：
      README.md · CLAUDE.md
      ai/ · schema/ · knowledge/ · projects/ · goals/
      methods/（templates 与 项目骨架模板 豁免）
      maintenance/（reports/history 已排除）
      tools/*.md（导航层）· tools/分类导航/ · tools/推荐层/ · tools/检索层/
  排除区（完全不扫描，也不进报告）：
      archive/ · references/原始来源包/ · tools/cards/
      maintenance/reports/history/ · drafts/
      以及 .git .workbuddy .obsidian node_modules __pycache__ .tools
  外部区（仅产生 external_warnings，参考用，不阻断）：
      其余内容，如 references/（除原始来源包）· tools/scripts/ · tools/reports/

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
# 终端编码安全：Windows GBK 控制台遇到 emoji/特殊字符会抛 UnicodeEncodeError。
# 统一把标准输出/错误重新配置为 UTF-8（errors=replace 保证永不崩溃）。
# ---------------------------------------------------------------------------
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

# ---------------------------------------------------------------------------
# 常量（与 校验脚本.py / frontmatter规范.md / 链接检查器-修复版.py 锁死）
# ---------------------------------------------------------------------------
TYPE_VALUES = {"index", "guide", "ref", "dashboard", "template", "moc",
               "demo", "project", "chapter", "character", "setting",
               "location", "prop", "tool", "daily-note", "book-note",
               "plan", "report"}
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

WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')


# ---------------------------------------------------------------------------
# 范围定义：唯一权威来源 tools/scripts/gate_scope.py
# ---------------------------------------------------------------------------
def _load_gate_scope():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.normpath(os.path.join(here, "..", "gate_scope.py"))
    if not os.path.isfile(path):
        raise RuntimeError(
            f"缺少范围定义模块 gate_scope.py（期望位置: {path}）。"
            "门禁范围必须由该模块统一定义，不提供局部回退，以免再次出现假绿灯。")
    spec = importlib.util.spec_from_file_location("gate_scope", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


scope = _load_gate_scope()
is_core = scope.is_strict            # 严格区判定（沿用旧函数名，语义已扩大）
should_skip_dir = scope.should_skip_dir


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
    """去除 fenced / inline 代码块，避免把代码里的字面 [[...]]/(...) 当成链接。"""
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # 支持单反引号和双反引号（markdown 中 `` `code` `` 表示含单反引号的代码）
    text = re.sub(r'`+[^`]*?`+', '', text)
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
    """严格区 frontmatter 校验。

    修复点：旧实现在 `fm is None`（整份文件根本没有 frontmatter）时直接
    `continue`，等于「越糟糕的文件越不被检查」——这是第二个假绿灯来源。
    现在严格区内缺 frontmatter 直接判 ERROR。
    """
    errors, warns = [], []
    for path, rel, _zone in scope.iter_md_files(root, include_external=False):
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"[frontmatter] 缺 frontmatter（严格区必须有）: {rel}")
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
# 允许出现的绝对路径白名单（避免误伤当前仓库路径与测试路径）
ALLOWED_OLD_PATHS = {
    "e:\\个人知识库\\",  # 当前仓库路径
    "C:\\",             # 演练/测试路径（Windows 系统盘）
}
def _is_allowed_old_path(seg: str) -> bool:
    for allowed in ALLOWED_OLD_PATHS:
        if seg.startswith(allowed):
            return True
    return False

def check_old_paths(root):
    errors, warns = [], []
    for path, rel, _zone in scope.iter_md_files(root, include_external=False):
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        body = strip_code(text)
        for m in OLD_PATH_RE.finditer(body):
            seg = m.group(0)
            if _is_allowed_old_path(seg):
                continue
            errors.append(
                f"[old_path] 发现旧/绝对路径残留 '{seg}': {rel}")
    return errors, warns


# ---------------------------------------------------------------------------
# 5. 重复 ID 检查（核心区）
# ---------------------------------------------------------------------------
def check_duplicate_ids(root):
    errors, warns = [], []
    seen = {}
    for path, rel, _zone in scope.iter_md_files(root, include_external=False):
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
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
# 6. 编码检查（严格区必须 UTF-8）
# ---------------------------------------------------------------------------
def check_encoding(root):
    errors, warns = [], []
    for path, rel, _zone in scope.iter_md_files(root, include_external=False):
        try:
            with open(path, "rb") as fb:
                fb.read().decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"[encoding] 非 UTF-8 编码（含乱码）: {rel}")
        except OSError:
            continue
    return errors, warns


# ---------------------------------------------------------------------------
# 7. 同目录重名文件检查（内容不同的真实重复 = ERROR；跨目录同名如 README 不报）
# ---------------------------------------------------------------------------
def check_duplicate_filenames(root):
    errors, warns = [], []
    by_dir = {}
    for path, rel, _zone in scope.iter_md_files(root, include_external=False):
        key = (os.path.dirname(rel), os.path.basename(rel))
        by_dir.setdefault(key, []).append(path)
    for (d, name), paths in by_dir.items():
        if len(paths) < 2:
            continue
        try:
            contents = {open(p, "rb").read() for p in paths}
        except OSError:
            continue
        if len(contents) > 1:
            rels = "; ".join(sorted(os.path.relpath(p, root) for p in paths))
            errors.append(
                f"[dup_file] 同目录同名文件内容不同 '{name}'（{len(paths)} 副本）: {rels}")
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
        en_err, en_warn = check_encoding(root)
        df_err, df_warn = check_duplicate_filenames(root)

        basic = {
            "frontmatter":  {"errors": fm_err, "warns": fm_warn},
            "structure":    {"errors": st_err, "warns": st_warn},
            "old_paths":    {"errors": op_err, "warns": op_warn},
            "duplicate_ids": {"errors": di_err, "warns": di_warn},
            "encoding":     {"errors": en_err, "warns": en_warn},
            "duplicate_files": {"errors": df_err, "warns": df_warn},
        }
        basic_error_count = (len(fm_err) + len(st_err) + len(op_err)
                             + len(di_err) + len(en_err) + len(df_err))
        basic_warn_count = (len(fm_warn) + len(st_warn) + len(op_warn)
                            + len(di_warn) + len(en_warn) + len(df_warn))
        basic_pass = basic_error_count == 0

        # —— 核心断链校验（复用链接检查器）——
        run_link_check = load_link_checker()
        lc = run_link_check(root)
        core_broken_links = lc["core_errors"]
        external_warnings = lc["external_warnings"]
        recognized = lc.get("recognized", {})
        core_pass = len(core_broken_links) == 0

        overall_pass = basic_pass and core_pass

        # 范围透明度：报告必须自证「到底查了哪些文件」，
        # 否则无法判断一个 PASS 是真通过还是范围太小造成的假绿灯。
        scope_counts = {
            "strict_files": lc.get("strict_files", 0),
            "external_files": lc.get("external_files", 0),
            "scanned_files": lc.get("scanned", 0),
        }

        result = {
            "timestamp": datetime.now().isoformat(),
            "root": root,
            "scope": scope.describe(),
            "scope_counts": scope_counts,
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
            print(f"严格区文件: {scope_counts['strict_files']} 篇"
                  f" | 外部区: {scope_counts['external_files']} 篇"
                  f" | 合计扫描: {scope_counts['scanned_files']} 篇")
            print("严格区 = README/CLAUDE · ai · schema · methods(除模板/示范)"
                  " · knowledge · projects · goals · maintenance · tools导航/推荐/检索层")
            print("排除区 = archive · references/原始来源包 · tools/cards"
                  " · maintenance/reports/history · drafts")
            print("-" * 64)
            print(f"[1] frontmatter 校验 : ERROR {len(fm_err)} | WARN {len(fm_warn)}")
            print(f"[2] 项目结构校验    : ERROR {len(st_err)} | WARN {len(st_warn)}")
            print(f"[3] 严格区断链校验  : ERROR {len(core_broken_links)}（必须为 0）")
            print(f"[4] 旧路径检查      : ERROR {len(op_err)} | WARN {len(op_warn)}")
            print(f"[5] 重复 ID 检查    : ERROR {len(di_err)} | WARN {len(di_warn)}")
            print(f"[6] 编码检查(UTF-8) : ERROR {len(en_err)} | WARN {len(en_warn)}")
            print(f"[7] 同目录重名文件  : ERROR {len(df_err)} | WARN {len(df_warn)}")
            print("-" * 64)
            print(f"基础校验: {'PASS ✅' if basic_pass else f'FAIL ❌ ({basic_error_count} ERROR)'}")
            print(f"严格断链: {'PASS ✅' if core_pass else f'FAIL ❌ ({len(core_broken_links)} ERROR)'}")
            print(f"外部警告: {len(external_warnings)} 条（仅供参考，不阻断）")
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
