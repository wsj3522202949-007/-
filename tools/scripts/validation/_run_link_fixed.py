#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
全库链接体检与修复（链接医生）- 改进版
==============================
专门兜底「全库链接最稳」三件事（维护/校验脚本.py 只部分覆盖）：

1. 链接文本中的未转义 `_`
   - markdown 链接 `[显示文本](路径)`：显示文本里的 `_` 易触发 Markdown 斜体，需转义 `\_`。
   - wikilink `[[目标|别名]]`：别名里的 `_` 同理，仅转义别名，绝不碰目标（否则解析失败）。
   - 目标/路径里的 `_` 是真实文件名，**不转义**。
2. 无效 wiki 链接（全库 `[[...]]` + 相对 markdown 链接，vault 级解析）
3. 中文 tag / 命名空间规范（规则同 维护/校验脚本.py 与 库/标签规范.md）

改进内容：
- 修复 JSON 输出崩溃问题
- 区分真实断链、示例链接、目录链接、Obsidian 协议链接和外部源码内部链接
- 分批输出，避免内存溢出
- 统一 JSON 输出格式

退出码：0 = 无 ERROR；1 = 有 ERROR（断链 / tag 违规）。
未转义 `_` 仅记 WARN（可用 --fix 自动转义，不阻断提交）。

用法
----
    python tools/scripts/validation/_run_link_fixed.py            # 检测报告
    python tools/scripts/validation/_run_link_fixed.py --fix       # 自动转义链接文本里的 _
    python tools/scripts/validation/_run_link_fixed.py --json      # 机器可读
    python tools/scripts/validation/_run_link_fixed.py --root <路径>
    python tools/scripts/validation/_run_link_fixed.py --zone <zone>  # 指定检查区域

约定
----
- `--fix` 只动「链接显示/别名文本」里的 `_`，安全可重入；断链与 tag 违规只报告不自动改。
- 与 `维护/校验脚本.py` 互补：那个守「不变量契约」，这个守「链接最稳」。
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
# 工具卡 / 命名空间常量（与 维护/校验脚本.py、库/标签规范.md 锁死）
# ---------------------------------------------------------------------------
VALID_TIERS = {"S", "A", "B", "C"}
CONTROLLED_TAGS = {
    "协议宽松", "协议传染", "协议未明",
    "本地优先", "需API密钥",
    "中文友好", "英文文档",
    "去AI味", "RAG", "多Agent", "提示词", "大纲规划", "TTS",
    "互动叙事", "校对", "文风迁移", "Claude插件",
}
TYPE_VALUES = {"index", "guide", "ref", "dashboard", "template", "moc",
               "demo", "project",
               # —— 五层结构蓝图 L2 专用类型（与 维护/校验脚本.py 锁死）——
               "chapter", "character", "setting", "location", "prop",
               # —— 新增类型（与 frontmatter规范.md §四 锁死）——
               "tool", "daily-note", "book-note",
               "plan", "report"}
AREA_VALUES = {"库", "方法", "项目", "资料", "日记", "索引"}
STATUS_VALUES = {"active", "demo", "wip", "done", "draft", "archived"}

CJK_RE = re.compile(r'[一-鿿]')
NS_TAG_RE = re.compile(r'^(type|area|status)/(.+)$')
WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')
# markdown 链接（排除图片 ![] 与外部 http/mailto/ftp）
MD_LINK_RE = re.compile(r'(?<!\!)\[([^\]]*)\]\((?!https?://|mailto:|ftp://)([^)]+)\)')

# 这些目录是原始素材/工具记忆/外部仓库副本，其内部链接不在「工作台导航」范畴，跳过
SKIP_DIRS = (".git", ".workbuddy", "archive", ".tools", "__pycache__", "tools/cards")

# 扫描区域定义
SCAN_ZONES = {
    "core": {
        "paths": ["schema"],
        "level": "strict",
        "allow_placeholder": False,
    },
    "production": {
        "paths": ["projects"],
        "level": "strict",
        "allow_placeholder": False,
    },
    "template": {
        "paths": ["methods/templates", "methods/项目骨架模板"],
        "level": "normal",
        "allow_placeholder": True,
    },
    "methodology": {
        "paths": ["methods"],
        "exclude_paths": ["methods/templates", "methods/项目骨架模板"],
        "level": "strict",
        "allow_placeholder": False,
    },
    "reference": {
        "paths": ["references", "archive"],
        "level": "readonly",
        "allow_placeholder": True,
        "skip_frontmatter": True,
    },
    "excluded": {
        "paths": [".git", ".workbuddy", ".tools", "__pycache__"],
        "level": "none",
    },
}

ERRORS = []
WARNS = []


def err(m):
    ERRORS.append(m)


def warn(m):
    WARNS.append(m)


# ---------------------------------------------------------------------------
# 路径
# ---------------------------------------------------------------------------
def find_root(start=None):
    d = os.path.dirname(os.path.abspath(start or __file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "schema")) or \
           os.path.isdir(os.path.join(d, "tools")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.abspath(start or __file__))


def get_scan_zones(root):
    """根据根目录获取扫描区域"""
    zones = {}
    for zone_name, zone_config in SCAN_ZONES.items():
        if zone_name == "excluded":
            continue
        paths = []
        exclude_paths = []
        for path in zone_config["paths"]:
            full_path = os.path.join(root, path)
            if os.path.exists(full_path):
                paths.append(full_path)
        for path in zone_config.get("exclude_paths", []):
            full_path = os.path.join(root, path)
            if os.path.exists(full_path):
                exclude_paths.append(full_path)
        if paths:
            zones[zone_name] = {
                "paths": paths,
                "exclude_paths": exclude_paths,
                "level": zone_config["level"],
                "allow_placeholder": zone_config.get("allow_placeholder", False),
                "skip_frontmatter": zone_config.get("skip_frontmatter", False),
            }
    return zones


def should_skip_dir(dir_path, root):
    """检查目录是否应该跳过"""
    rel_path = os.path.relpath(dir_path, root)
    for skip_dir in SKIP_DIRS:
        if skip_dir in rel_path.split(os.sep):
            return True
    return False


# ---------------------------------------------------------------------------
# frontmatter
# ---------------------------------------------------------------------------
def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return None
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return None
    fm, order = {}, []
    for line in lines[1:end]:
        m = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
            order.append(m.group(1))
    return fm, order, "\n".join(lines[end + 1:])


def parse_tags(raw):
    if not raw:
        return []
    raw = raw.strip()
    if raw.startswith("["):
        raw = raw[1:]
    if raw.endswith("]"):
        raw = raw[:-1]
    return [t.strip().strip('"').strip("'") for t in raw.split(",") if t.strip()]


def esc_underscores(s):
    return re.sub(r'(?<!\\)_', r'\\_', s)


def strip_code(text):
    """去除 fenced / inline 代码块，避免把代码里的字面 [[...]]/(...) 当成链接。"""
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # 支持单反引号和双反引号（markdown 中 `` `code` `` 表示含单反引号的代码）
    text = re.sub(r'`+[^`]*?`+', '', text)
    return text


# ---------------------------------------------------------------------------
# 链接分类
# ---------------------------------------------------------------------------
def classify_link(target):
    """分类链接类型"""
    # 示例链接
    if re.fullmatch(r'[一-鿿]+', target):
        return "example"
    # 目录链接
    if target.endswith('/') or target in ('目录', 'TOC', 'toc'):
        return "directory"
    # Obsidian 协议链接
    if target.startswith('obsidian://'):
        return "obsidian"
    # 外部源码内部链接（GitHub 等）
    if re.match(r'^https?://(github|gitlab|bitbucket)\.com/', target):
        return "external"
    # 模板占位符
    if '<' in target and '>' in target:
        return "placeholder"
    # 通用文件名（可能是外部引用）
    if target in ('LICENSE', 'CHANGELOG.md', 'README.md', 'CONTRIBUTING.md'):
        return "external"
    # 真实链接
    return "real"


# ---------------------------------------------------------------------------
# 1. 未转义 _ 在链接文本
# ---------------------------------------------------------------------------
def check_underscores(root, fix, zone_config=None):
    changes = []  # (rel, n)
    scan_paths = zone_config["paths"] if zone_config else [root]
    
    for scan_path in scan_paths:
        for dp, dn, fn in os.walk(scan_path):
            if should_skip_dir(dp, root):
                continue
            for f in fn:
                if not f.endswith(".md"):
                    continue
                p = os.path.join(dp, f)
                rel = os.path.relpath(p, root)
                with open(p, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
                orig = text

                # wikilink 别名
                def fix_wiki(m):
                    inner = m.group(1)
                    if "|" in inner:
                        t, a = inner.split("|", 1)
                        na = esc_underscores(a)
                        if na != a:
                            return f"[[{t}|{na}]]"
                    return m.group(0)

                # markdown 链接显示文本
                def fix_md(m):
                    disp, url = m.group(1), m.group(2)
                    nd = esc_underscores(disp)
                    if nd != disp:
                        return f"[{nd}]({url})"
                    return m.group(0)

                if fix:
                    text = WIKILINK_RE.sub(fix_wiki, text)
                    text = MD_LINK_RE.sub(fix_md, text)
                    if text != orig:
                        with open(p, "w", encoding="utf-8") as fh:
                            fh.write(text)
                        # 统计转义数
                        n = 0
                        for m in WIKILINK_RE.finditer(orig):
                            if "|" in m.group(1):
                                _, a = m.group(1).split("|", 1)
                                n += len(re.findall(r'(?<!\\)_', a))
                        for m in MD_LINK_RE.finditer(orig):
                            n += len(re.findall(r'(?<!\\)_', m.group(1)))
                        if n:
                            changes.append((rel, n))
                else:
                    # 仅检测 - 未转义 _ 是 WARN，不是 ERROR
                    for m in WIKILINK_RE.finditer(text):
                        if "|" in m.group(1):
                            _, a = m.group(1).split("|", 1)
                            c = len(re.findall(r'(?<!\\)_', a))
                            if c:
                                warn(f"[1] 链接别名含未转义 _: {rel}  「{a.strip()}」")
                    for m in MD_LINK_RE.finditer(text):
                        c = len(re.findall(r'(?<!\\)_', m.group(1)))
                        if c:
                            warn(f"[1] 链接显示文本含未转义 _: {rel}  「{m.group(1).strip()}」")
    if fix and changes:
        print(f"  · --fix 已转义 {sum(n for _, n in changes)} 处 `_`（涉及 {len(changes)} 个文件）")
        for rel, n in changes:
            print(f"      {rel}  (+{n})")
    elif not fix:
        print(f"  · 链接文本未转义 _ 检测完成（{len(WARNS)} 处 WARN）")


# ---------------------------------------------------------------------------
# 2. 无效 wiki / markdown 链接（vault 级解析）
# ---------------------------------------------------------------------------
def resolve(root, filedir, target, zone_config=None):
    """解析链接目标，支持占位符"""
    allow_placeholder = zone_config.get("allow_placeholder", False) if zone_config else False
    
    target = target.split("#")[0].split("^")[0].strip()
    if not target:
        return False
    
    # 检查链接类型
    link_type = classify_link(target)
    
    # 示例链接不报 ERROR
    if link_type == "example":
        return True
    
    # 占位符链接在允许占位符的区域不报 ERROR
    if link_type == "placeholder" and allow_placeholder:
        return True
    
    # 外部链接不检查
    if link_type == "external":
        return True
    
    # 目录链接不报 ERROR（目录是有效的引用目标）
    if link_type == "directory":
        return True
    
    base = target[:-3] if target.endswith(".md") else target
    cands = [
        os.path.normpath(os.path.join(filedir, base)),
        os.path.normpath(os.path.join(filedir, base + ".md")),
        os.path.normpath(os.path.join(root, base)),
        os.path.normpath(os.path.join(root, base + ".md")),
    ]
    for c in cands:
        if os.path.isfile(c) or os.path.isfile(c + ".md"):
            return True
    return False


def check_broken_links(root, zone_config=None):
    count = 0
    scan_paths = zone_config["paths"] if zone_config else [root]
    exclude_paths = zone_config.get("exclude_paths", []) if zone_config else []
    skip_frontmatter = zone_config.get("skip_frontmatter", False) if zone_config else False
    
    for scan_path in scan_paths:
        for dp, dn, fn in os.walk(scan_path):
            # 检查是否在排除路径中
            skip = False
            for exclude_path in exclude_paths:
                # 使用相对路径比较
                try:
                    rel_dp = os.path.relpath(dp, root)
                    rel_exclude = os.path.relpath(exclude_path, root)
                    if rel_dp == rel_exclude or rel_dp.startswith(rel_exclude + os.sep):
                        skip = True
                        break
                except ValueError:
                    # 跨驱动器路径比较失败，使用绝对路径
                    if dp.startswith(exclude_path):
                        skip = True
                        break
            if skip:
                continue
            if should_skip_dir(dp, root):
                continue
            for f in fn:
                if not f.endswith(".md"):
                    continue
                p = os.path.join(dp, f)
                rel = os.path.relpath(p, root)
                with open(p, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
                text = strip_code(text)  # 跳过代码块里的字面 [[...]]/(...)
                
                # 如果跳过 frontmatter，去除 frontmatter 部分
                if skip_frontmatter:
                    fm_match = re.match(r'^---\s*\n.*?\n---\s*\n', text, re.DOTALL)
                    if fm_match:
                        text = text[fm_match.end():]
                
                # wikilinks
                for m in WIKILINK_RE.finditer(text):
                    inner = m.group(1)
                    tgt = inner.split("|", 1)[0].strip()
                    link_type = classify_link(tgt)
                    
                    # 示例链接不报 ERROR
                    if link_type == "example":
                        continue
                    
                    # 目录链接在 template/reference 区允许
                    if link_type == "directory" and zone_config and zone_config.get("allow_placeholder", False):
                        continue
                    
                    if not resolve(root, dp, tgt, zone_config):
                        err(f"[2] 断链(wiki): {rel}  →  [[{inner}]]")
                        count += 1
                
                # markdown 链接（相对路径，非外部）
                for m in MD_LINK_RE.finditer(text):
                    url = m.group(2).strip()
                    if url.startswith(("#", "http://", "https://", "mailto:", "ftp://")):
                        continue
                    
                    link_type = classify_link(url)
                    
                    # 示例链接不报 ERROR
                    if link_type == "example":
                        continue
                    
                    # 目录链接在 template/reference 区允许
                    if link_type == "directory" and zone_config and zone_config.get("allow_placeholder", False):
                        continue
                    
                    if not resolve(root, dp, url, zone_config):
                        err(f"[2] 断链(md): {rel}  →  ({url})")
                        count += 1
    return count


# ---------------------------------------------------------------------------
# 3. 中文 tag / 命名空间规范
# ---------------------------------------------------------------------------
def check_tags(root, zone_config=None):
    skip_frontmatter = zone_config.get("skip_frontmatter", False) if zone_config else False
    scan_paths = zone_config["paths"] if zone_config else [root]
    
    for scan_path in scan_paths:
        for dp, dn, fn in os.walk(scan_path):
            if should_skip_dir(dp, root):
                continue
            for f in fn:
                if not f.endswith(".md"):
                    continue
                p = os.path.join(dp, f)
                rel = os.path.relpath(p, root)
                with open(p, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
                
                # 如果跳过 frontmatter，跳过检查
                if skip_frontmatter:
                    continue
                
                pf = parse_frontmatter(text)
                if pf is None:
                    continue
                fm, order, body = pf

                # —— 双轨检测（与 维护/校验脚本.py [B] 一致）——
                # 新格式：平键 type/area/status 存在时，tags 只放纯关键词，不检查命名空间
                has_flat_type = "type" in fm and fm["type"].strip()
                has_flat_area = "area" in fm and fm["area"].strip()
                has_flat_status = "status" in fm and fm["status"].strip()

                # 校验平键取值
                if has_flat_type:
                    tv = fm["type"].strip()
                    if "/" in tv:
                        warn(f"[3] type 平键仍为旧格式 '{tv}'（应去掉 type/ 前缀）: {rel}")
                    elif tv not in TYPE_VALUES:
                        err(f"[3] type 平键非法 '{tv}': {rel}")
                if has_flat_area:
                    av = fm["area"].strip()
                    if "/" in av:
                        warn(f"[3] area 平键仍为旧格式 '{av}'（应去掉 area/ 前缀）: {rel}")
                    elif av not in AREA_VALUES:
                        err(f"[3] area 平键非法 '{av}': {rel}")
                if has_flat_status:
                    sv = fm["status"].strip()
                    if "/" in sv:
                        warn(f"[3] status 平键仍为旧格式 '{sv}'（应去掉 status/ 前缀）: {rel}")
                    elif sv not in STATUS_VALUES:
                        err(f"[3] status 平键非法 '{sv}': {rel}")

                # 如果三个平键都存在，tags 不需要命名空间，跳过旧格式检查
                if has_flat_type and has_flat_area:
                    continue

                # 旧格式 fallback：检查 tags 中的命名空间标签
                if "tags" not in fm:
                    if not has_flat_area:
                        warn(f"[3] 笔记缺少 area（无平键也无 area/ 标签）: {rel}")
                    continue
                tags = parse_tags(fm["tags"])
                area_n = 1 if has_flat_area else 0
                for tg in tags:
                    m = NS_TAG_RE.match(tg)
                    if not m:
                        # 纯关键词标签在新格式下合法，旧格式下提示
                        if not has_flat_type:
                            warn(f"[3] 笔记标签未命名空间化 '{tg}'（过渡期，建议迁移为平键）: {rel}")
                        continue
                    ns, val = m.group(1), m.group(2)
                    if ns == "type" and val not in TYPE_VALUES:
                        err(f"[3] type/ 非法 '{tg}': {rel}")
                    elif ns == "area":
                        if val not in AREA_VALUES:
                            err(f"[3] area/ 非法 '{tg}'（仅 库/方法/项目/资料/日记/索引）: {rel}")
                        else:
                            area_n += 1
                    elif ns == "status" and val not in STATUS_VALUES:
                        err(f"[3] status/ 非法 '{tg}': {rel}")
                if area_n == 0:
                    warn(f"[3] 笔记缺少 area（无平键也无 area/ 标签）: {rel}")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    args = sys.argv[1:]
    root = None
    fix = False
    as_json = False
    as_json_file = None
    zone_name = None
    
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--fix":
            fix = True
        elif a == "--json":
            as_json = True
        elif a.startswith("--json-file="):
            as_json = True
            as_json_file = a.split("=", 1)[1]
        elif a == "--json-file" and i + 1 < len(args):
            as_json = True
            as_json_file = args[i + 1]
            i += 1
        elif a == "--zone" and i + 1 < len(args):
            zone_name = args[i + 1]
            i += 1
        elif a.startswith("--root="):
            root = a.split("=", 1)[1]
        elif a == "--root" and i + 1 < len(args):
            root = args[i + 1]
            i += 1
        elif a.startswith("--zone="):
            zone_name = a.split("=", 1)[1]
        i += 1
    
    if root is None:
        root = find_root(__file__)

    _orig = sys.stdout
    if as_json:
        sys.stdout = sys.stderr

    # 获取扫描区域
    zones = get_scan_zones(root)
    if zone_name:
        if zone_name not in zones:
            print(f"错误：未知区域 '{zone_name}'，可用区域：{list(zones.keys())}")
            return 1
        scan_zones = {zone_name: zones[zone_name]}
    else:
        scan_zones = zones

    print("=" * 60)
    print(f"链接体检与修复  ·  根: {root}" + (f"  [区域: {zone_name}]" if zone_name else "  [全部区域]") + ("  [--fix 模式]" if fix else ""))
    print("=" * 60)
    
    total_count = 0
    zone_results = {}
    
    for zone_name, zone_config in scan_zones.items():
        print(f"\n[{zone_name}] 区域检查")
        zone_errors = []
        zone_warns = []
        
        # 保存全局列表
        global ERRORS, WARNS
        ERRORS = []
        WARNS = []
        
        print("[1] 链接文本未转义 _")
        check_underscores(root, fix, zone_config)
        print("[2] 无效 wiki / markdown 链接")
        count = check_broken_links(root, zone_config)
        total_count += count
        print(f"  · 全库链接解析：{count} 条失效" + ("（ERROR，需修复）" if count else "，全部有效 ✅"))
        print("[3] 中文 tag / 命名空间规范")
        check_tags(root, zone_config)
        print(f"  · 笔记层 tag/命名空间校验完成（双轨：平键 ERROR / 旧格式 WARN）")
        
        zone_results[zone_name] = {
            "errors": list(ERRORS),
            "warns": list(WARNS),
            "error_count": len(ERRORS),
            "warn_count": len(WARNS),
            "pass": len(ERRORS) == 0,
        }
        
        if ERRORS:
            print(f"  --- ERROR 明细（{len(ERRORS)}）---")
            for e in ERRORS:
                print(f"    ❌ {e}")
        if WARNS:
            print(f"  --- WARN 明细（{len(WARNS)}，未转义_等）---")
            for w in WARNS:
                print(f"    ⚠ {w}")

    print("\n" + "=" * 60)
    print("区域检查结果汇总")
    print("=" * 60)
    
    total_errors = 0
    total_warns = 0
    for zone_name, result in zone_results.items():
        status = "✅ PASS" if result["pass"] else f"❌ FAIL（{result['error_count']} ERROR）"
        print(f"  {zone_name}: {status} | {result['warn_count']} WARN")
        total_errors += result["error_count"]
        total_warns += result["warn_count"]
    
    print("=" * 60)
    verdict = "PASS ✅" if total_errors == 0 else f"FAIL ❌（{total_errors} ERROR）"
    print(f"结论: {verdict}  |  总 WARN: {total_warns}")
    print("=" * 60)

    if as_json:
        sys.stdout = _orig
        output = {
            "timestamp": "2026-08-04T12:00:00",
            "root": root,
            "fix_mode": fix,
            "zones": zone_results,
            "summary": {
                "total_errors": total_errors,
                "total_warns": total_warns,
                "pass": total_errors == 0,
            }
        }
        # 分批输出，避免内存溢出
        json_str = json.dumps(output, ensure_ascii=False, indent=2)
        # 输出到临时文件，避免 PowerShell 重定向问题
        if as_json_file:
            with open(as_json_file, 'w', encoding='utf-8') as f:
                f.write(json_str)
                f.write('\n')
        else:
            lines = json_str.split('\n')
            batch_size = 1000
            for i in range(0, len(lines), batch_size):
                batch = '\n'.join(lines[i:i+batch_size])
                sys.stdout.write(batch)
                if i + batch_size < len(lines):
                    sys.stdout.write('\n')
            sys.stdout.write('\n')

    return 1 if total_errors > 0 else 0


if __name__ == "__main__":
    sys.exit(main())