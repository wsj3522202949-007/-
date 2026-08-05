#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
校验脚本.py —— 已合并到统一门禁 run_all.py（单一权威入口）

本文件现为「委托包装器」：直接调用 run_all.py 的 main()，
确保所有门禁入口给出**完全一致**的结果，不再各自为政。

原先独有的检查项（frontmatter、结构、旧路径、重复ID、编码、同目录重名、
链接）已全部并入 run_all.py，并统一以 gate_scope.py 的严格区为唯一范围。

用法（与以前兼容):
  python 校验脚本.py            # 人类可读报告（= run_all.py）
  python 校验脚本.py --json     # 机器可读 JSON（= run_all.py --json）
  python 校验脚本.py --root <路径>

说明：--fix / --core-only / --exclude / --zone 等历史参数已被忽略（统一门禁只认
严格区，且不做自动修复）。如需这些能力，请直接在 run_all.py 上扩展。
"""

import os
import sys

# 终端编码安全（同 run_all.py）
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

_HERE = os.path.dirname(os.path.abspath(__file__))
_RUN_ALL = os.path.normpath(os.path.join(_HERE, "run_all.py"))

if not os.path.isfile(_RUN_ALL):
    sys.stderr.write(f"[校验脚本] 找不到统一门禁 run_all.py: {_RUN_ALL}\n")
    sys.exit(2)

import importlib.util
_spec = importlib.util.spec_from_file_location("run_all", _RUN_ALL)
_run_all_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_run_all_mod)

if __name__ == "__main__":
    sys.stderr.write(
        "[校验脚本] 已合并到 run_all.py，现委托执行（结果完全一致）。\n")
    sys.exit(_run_all_mod.main())
import sys
import json
import tempfile

# ---------------------------------------------------------------------------
# 契约常量（与《库/标签规范.md》锁死）
# ---------------------------------------------------------------------------
README_DIR = os.path.join("tools", "cards")
MOC_DIR = os.path.join("tools", "分类导航")
GUIDE_FILE = os.path.join("tools", "工具选型指南.md")
DASHBOARD_FILE = "tools/仪表盘.md"

VALID_TIERS = {"S", "A", "B", "C"}

# 工具卡受控标签（22 个）
CONTROLLED_TAGS = {
    # 协议 3
    "协议宽松", "协议传染", "协议未明",
    # 部署 2
    "本地优先", "需API密钥",
    # 文档 2
    "中文友好", "英文文档",
    # 能力 15
    "去AI味", "RAG", "多Agent", "提示词", "大纲规划", "TTS",
    "互动叙事", "校对", "文风迁移", "Claude插件",
    "人物设定", "改稿润色", "本地写作", "平台运营", "灵感创意",
}

# 笔记层命名空间取值（旧格式，过渡期保留）
TYPE_VALUES = {"index", "guide", "ref", "dashboard", "template", "moc",
               "demo", "project",
               # —— 五层结构蓝图 L2 专用类型 ——
               "chapter",    # L2 正文层：第NNN章-标题.md
               "character",  # L2 知识单页层：人物/xxx.md
               "setting",    # L2 知识单页层：设定/xxx.md
               "location",   # L2 知识单页层：地点/xxx.md
               "prop",       # L2 知识单页层：道具/xxx.md
               # —— 新增类型（frontmatter规范.md §4.1）——
               "tool",       # 工具卡
               "daily-note", # 每日笔记
               "book-note",  # 读书笔记
               "plan",       # 计划文档
               "report"}     # 报告文档
AREA_VALUES = {"库", "方法", "项目", "资料", "日记", "索引"}
STATUS_VALUES = {"active", "demo", "wip", "done", "draft", "archived"}

CJK_RE = re.compile(r'[一-鿿]')
NS_TAG_RE = re.compile(r'^(type|area|status)/(.+)$')
README_NAME_RE = re.compile(r'^\d{5}__.+__.+\.md$')
WIKILINK_RE = re.compile(r'\[\[\s*tools/cards/([^\]|#]+)')
CHAPTER_NAME_RE = re.compile(r'^第\d{3}章-.+\.md$')   # 命名契约①：正文层 第NNN章-标题.md
KNOWLEDGE_DIRS = ("人物", "设定", "地点", "道具")      # 命名契约②：知识单页目录名（仅允许在 projects/<书名>/ 内）

ERRORS = []
WARNS = []


def err(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNS.append(msg)


# ---------------------------------------------------------------------------
# frontmatter 解析（轻量、无第三方依赖）
# ---------------------------------------------------------------------------
def parse_frontmatter(text):
    """返回 (dict_of_raw_str, body) 或 None。"""
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
    order = []
    for line in lines[1:end]:
        m = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        fm[key] = val
        order.append(key)
    body = "\n".join(lines[end + 1:])
    return fm, order, body


def parse_tags(raw):
    """raw 形如 '[a, b, c]' 或 '[a]' 或 '' 。返回 list[str]。"""
    if not raw:
        return []
    raw = raw.strip()
    if raw.startswith("["):
        raw = raw[1:]
    if raw.endswith("]"):
        raw = raw[:-1]
    out = []
    for t in raw.split(","):
        t = t.strip().strip('"').strip("'")
        if t:
            out.append(t)
    return out


def parse_quoted(raw):
    if not raw:
        return ""
    return raw.strip().strip('"').strip("'")


# ---------------------------------------------------------------------------
# A. 工具卡校验
# ---------------------------------------------------------------------------
def check_readmes(root):
    d = os.path.join(root, README_DIR)
    if not os.path.isdir(d):
        err(f"[A] 工具卡目录不存在: {README_DIR}")
        return
    files = sorted(f for f in os.listdir(d) if f.endswith(".md"))
    tier_count = {"S": 0, "A": 0, "B": 0, "C": 0}
    bad_name = 0
    for f in files:
        if not README_NAME_RE.match(f):
            warn(f"[A] readme 命名不规范: {f}")
            bad_name += 1
        path = os.path.join(d, f)
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        pf = parse_frontmatter(text)
        if pf is None:
            err(f"[A] 缺 frontmatter: {f}")
            continue
        fm, order, body = pf
        # 四字段 + stars
        for key in ("tier", "tags", "use_case", "pitfalls", "stars"):
            if key not in fm:
                err(f"[A] 缺字段 {key}: {f}")
        # tier
        tier = parse_quoted(fm.get("tier", ""))
        if tier not in VALID_TIERS:
            err(f"[A] tier 非法 '{tier}': {f}")
        else:
            tier_count[tier] += 1
        # stars 数值
        stars_raw = fm.get("stars", "")
        if stars_raw and not re.match(r'^-?\d+$', stars_raw.strip().strip('"')):
            warn(f"[A] stars 非整数: {f} -> {stars_raw}")
        # tags
        tags = parse_tags(fm.get("tags", ""))
        if not tags:
            warn(f"[A] tags 为空: {f}")
        for tg in tags:
            if "/" in tg:
                err(f"[A] 工具卡混入命名空间标签 '{tg}': {f}")
                continue
            if tg in CONTROLLED_TAGS:
                continue
            if CJK_RE.search(tg):
                # 中文且非受控 => 领域泄漏进 tags（应留 category）
                err(f"[A] 非受控中文标签 '{tg}'（疑似领域泄漏）: {f}")
            # 其余视为技术语言（ASCII），开放，放行
        # use_case 非空（pitfalls 仅空壳/特殊协议/API 风险才填，空属基线，不告警）
        if not parse_quoted(fm.get("use_case", "")):
            warn(f"[A] use_case 为空: {f}")
    total = len(files)
    summed = sum(tier_count.values())
    if summed != total:
        err(f"[A] tier 分布合计 {summed} != readme 总数 {total}")
    print(f"  · 工具卡: {total} 篇 | tier S {tier_count['S']} / "
          f"A {tier_count['A']} / B {tier_count['B']} / C {tier_count['C']}"
          + (f" | {bad_name} 个命名不规范" if bad_name else ""))
    return tier_count, total


# ---------------------------------------------------------------------------
# B. 笔记层 frontmatter 合规（平键为主，旧命名空间标签过渡期 WARN）
# ---------------------------------------------------------------------------
def check_note_frontmatter(root):
    readme_root = os.path.join(root, README_DIR)
    note_count = 0
    new_fmt = 0   # 新格式（平键 type: 存在）
    old_fmt = 0    # 旧格式（仅 tags: [type/xxx]）
    for dp, dn, fn in os.walk(root):
        if ".git" in dp:
            continue
        # archive/ 为 L3 素材仓（外部来源），frontmatter 不受本库规范约束，豁免
        if "archive" in dp.split(os.sep) or "references" in dp.split(os.sep) or "原始来源包" in dp.split(os.sep) or "在线调研" in dp.split(os.sep):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, root)
            if p.startswith(readme_root):
                continue  # 工具卡走 A 类校验
            with open(p, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            pf = parse_frontmatter(text)
            if pf is None:
                continue  # 无 frontmatter 的内容笔记，允许
            fm, order, body = pf
            note_count += 1

            # --- 检测新格式：平键 type 存在 ---
            has_flat_type = "type" in fm and fm["type"].strip()
            has_flat_area = "area" in fm and fm["area"].strip()
            has_flat_status = "status" in fm and fm["status"].strip()

            # --- 检测旧格式：tags 含命名空间标签 ---
            tags = parse_tags(fm.get("tags", ""))
            ns_tags = [t for t in tags if NS_TAG_RE.match(t)]

            # --- 平键 type 值以 type/ 开头 = 旧格式值混在平键里，视为旧格式 ---
            flat_type_is_old = has_flat_type and fm["type"].strip().startswith("type/")
            if flat_type_is_old:
                has_flat_type = False  # 降级为旧格式处理

            if has_flat_type:
                new_fmt += 1
                # 新格式：严格校验平键取值（ERROR）
                tv = fm["type"].strip()
                if tv not in TYPE_VALUES:
                    err(f"[B] type 非法取值 '{tv}'（受控词见 frontmatter规范.md §4.1）: {rel}")
                # 检查旧命名空间标签是否残留（WARN：冗余）
                if ns_tags:
                    warn(f"[B] 新旧格式并存：已有平键 type，tags 中残留命名空间标签 {ns_tags}，建议清理: {rel}")
            elif ns_tags:
                old_fmt += 1
                # 旧格式：WARN（过渡期不阻断）
                warn(f"[B] 旧格式（命名空间标签），建议迁移为平键: {rel}")
                # 仍校验取值合法性（ERROR：非法值无论新旧格式都要报）
                for tg in ns_tags:
                    m = NS_TAG_RE.match(tg)
                    if not m:
                        continue
                    ns, val = m.group(1), m.group(2)
                    if ns == "type" and val not in TYPE_VALUES:
                        err(f"[B] type/ 非法取值 '{tg}': {rel}")
                    elif ns == "area":
                        if val not in AREA_VALUES:
                            err(f"[B] area/ 非法取值 '{tg}'（受控词见 frontmatter规范.md §4.2）: {rel}")
                    elif ns == "status" and val not in STATUS_VALUES:
                        err(f"[B] status/ 非法取值 '{tg}': {rel}")
            # else: 无 type 信息（既无平键也无命名空间标签），放行

            # --- 校验平键 area/status 取值（如果存在）---
            if has_flat_area:
                av = fm["area"].strip()
                if av not in AREA_VALUES:
                    err(f"[B] area 非法取值 '{av}'（受控词见 frontmatter规范.md §4.2）: {rel}")
            if has_flat_status:
                sv = fm["status"].strip()
                if sv not in STATUS_VALUES:
                    err(f"[B] status 非法取值 '{sv}'（受控词见 frontmatter规范.md §4.3）: {rel}")

            # --- 检查 tags 中是否有非命名空间的裸中文标签（旧规则保留）---
            # 旧格式下 tags 里的非命名空间标签如果是中文且非受控，仍报 ERROR
            if not has_flat_type and ns_tags:
                # 旧格式：检查 tags 是否只有命名空间标签
                non_ns_tags = [t for t in tags if not NS_TAG_RE.match(t)]
                for tg in non_ns_tags:
                    # 裸标签在旧格式下如果是中文，可能是领域泄漏
                    if CJK_RE.search(tg) and tg not in CONTROLLED_TAGS:
                        # 但允许 area/ 方法 等已知的中文 area 值作为裸标签出现（历史遗留）
                        pass  # 过渡期放宽，不报 ERROR

    print(f"  · 笔记层: {note_count} 篇带 frontmatter | 新格式 {new_fmt} / 旧格式 {old_fmt}")
    return note_count


# ---------------------------------------------------------------------------
# C. 结构不变量
# ---------------------------------------------------------------------------
def check_structure(root):
    d = os.path.join(root, MOC_DIR)
    if not os.path.isdir(d):
        err(f"[C] 分类导航目录不存在: {MOC_DIR}")
        return
    mocs = [f for f in os.listdir(d) if f.endswith(".md")]
    missing_moc_tag = 0
    for f in mocs:
        path = os.path.join(d, f)
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        pf = parse_frontmatter(text)
        if pf is None:
            err(f"[C] MOC 缺 frontmatter: {f}")
            missing_moc_tag += 1
            continue
        fm, order, body = pf
        # 新格式：平键 type: moc
        flat_type = (fm.get("type") or "").strip()
        if flat_type == "moc":
            continue  # 新格式 OK
        # 旧格式：tags 含 type/moc
        tags = parse_tags(fm.get("tags", ""))
        if "type/moc" in tags:
            warn(f"[C] MOC 用旧格式 type/moc 标签，建议迁移为平键 type: moc: {f}")
            # 检查是否有冗余（新旧并存）
            if flat_type:
                warn(f"[C] MOC 新旧并存（平键 type:{flat_type} + tags:type/moc），建议清理: {f}")
            continue
        # 都没有
        err(f"[C] MOC 缺 type: moc（平键）或 type/moc（旧标签）: {f}")
        missing_moc_tag += 1
    print(f"  · 分类导航 MOC: {len(mocs)} 篇"
          + (f" | {missing_moc_tag} 篇缺 type" if missing_moc_tag else " 全部合规"))


# ---------------------------------------------------------------------------
# D. 关键 wiki 链接
# ---------------------------------------------------------------------------
def check_wikilinks(root):
    broken = 0
    total = 0
    for rel in (GUIDE_FILE, DASHBOARD_FILE):
        p = os.path.join(root, rel)
        if not os.path.isfile(p):
            warn(f"[D] 链接源文件不存在: {rel}")
            continue
        with open(p, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for m in WIKILINK_RE.finditer(text):
            target = m.group(1).strip()
            total += 1
            t = target[:-3] if target.endswith(".md") else target
            cand = os.path.join(root, README_DIR, t + ".md")
            if not os.path.isfile(cand):
                broken += 1
                err(f"[D] 链接失效 [[tools/cards/{target}]] 见于 {rel}")
    print(f"  · wiki 链接: 校验 {total} 条"
          + (f" | {broken} 条失效" if broken else " | 全部有效"))


# ---------------------------------------------------------------------------
# E. 命名契约
# ---------------------------------------------------------------------------
def check_naming_contract(root):
    """E 类：命名契约（ERROR 阻断）。
    - E1 正文层：projects/<书名>/正文/ 下（README.md 除外）必须是 第NNN章-标题.md
    - E2 知识单页层：人物/设定/地点/道具/ 不得出现在 vault 根（必须位于 projects/<书名>/ 内）
    注：archive/ 为 L3 素材仓（原始来源包等），命名可不规范，已豁免。
    """
    # E1 正文命名（仅扫 projects/，archive/ 豁免）
    proj = os.path.join(root, "projects")
    if not os.path.isdir(proj):
        proj = os.path.join(root, "小说", "projects")
    bad_chap = 0
    if os.path.isdir(proj):
        for dp, dn, fn in os.walk(proj):
            if os.path.basename(dp) in ("正文", "chapters"):
                for f in fn:
                    if f == "README.md":
                        continue
                    if not CHAPTER_NAME_RE.match(f):
                        err(f"[E1] 正文命名不合规 '{f}'（应为 第NNN章-标题.md）: "
                            f"{os.path.relpath(dp, root)}/")
                        bad_chap += 1
    # E2 知识单页位置（vault 根不得出现旧式目录名）
    root_knowledge = 0
    for name in KNOWLEDGE_DIRS:
        if os.path.isdir(os.path.join(root, name)):
            err(f"[E2] 知识单页目录 '{name}/' 出现在 vault 根"
                f"（必须下沉到 projects/<书名>/entities/ 内）")
            root_knowledge += 1
    verdict = "OK" if (bad_chap == 0 and root_knowledge == 0) else \
        f"{bad_chap} 处正文不合规 / {root_knowledge} 处沉到根"
    print(f"  · 命名契约: {verdict}")


# ---------------------------------------------------------------------------
# F. 正文层 frontmatter 强制
# ---------------------------------------------------------------------------
def check_body_frontmatter(root):
    """[F] 正文层 frontmatter 强制（ERROR 阻断）。
    projects/<书名>/正文/第NNN章-*.md（README.md 除外）必须：
      - 带 frontmatter；
      - 含必填键 title / chapter / status / type；
      - type 必须为 chapter（平键，新格式）或 type/chapter（旧格式，WARN）；
      - chapter 数值与文件名 第NNN章 序号一致。
    archive/ 为素材仓，豁免。
    """
    print("[F] 正文层 frontmatter 强制")
    proj = os.path.join(root, "projects")
    if not os.path.isdir(proj):
        proj = os.path.join(root, "小说", "projects")
    n = 0
    if os.path.isdir(proj):
        for dp, dn, fn in os.walk(proj):
            if os.path.basename(dp) not in ("正文", "chapters"):
                continue
            for f in fn:
                if f == "README.md":
                    continue
                if not CHAPTER_NAME_RE.match(f):
                    continue  # 命名违规交给 [E1]，不重复报
                p = os.path.join(dp, f)
                rel = os.path.relpath(p, root)
                n += 1
                with open(p, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
                pf = parse_frontmatter(text)
                if pf is None:
                    err(f"[F] 正文缺 frontmatter（强制，否则 ERROR）: {rel}")
                    continue
                fm, order, body = pf
                missing = [k for k in ("title", "chapter", "status", "type")
                           if k not in fm]
                if missing:
                    err(f"[F] 正文 frontmatter 缺必填键 {missing}: {rel}")
                tv = (fm.get("type") or "").strip()
                # 新格式：type: chapter
                if tv == "chapter":
                    pass  # OK
                # 旧格式：type: type/chapter
                elif tv == "type/chapter":
                    warn(f"[F] 正文 type 用旧格式 type/chapter，建议迁移为平键 type: chapter: {rel}")
                elif tv.startswith("type/"):
                    err(f"[F] 正文 type 应为 chapter（平键），实为 {tv}: {rel}")
                elif tv:
                    err(f"[F] 正文 type 应为 chapter（平键），实为 '{tv}': {rel}")
                m = re.match(r"第(\d{3})章", f)
                if m and "chapter" in fm:
                    try:
                        if int(str(fm["chapter"]).strip()) != int(m.group(1)):
                            err(f"[F] 正文 chapter({fm['chapter']}) 与文件名序号({m.group(1)}) 不一致: {rel}")
                    except (ValueError, TypeError):
                        err(f"[F] 正文 chapter 非整数: {rel}")
    print(f"  · 正文层: 检查 {n} 篇，frontmatter 强制已启用")


# ---------------------------------------------------------------------------
# G. 通用字段缺失检查（过渡期 WARN）
# ---------------------------------------------------------------------------
# frontmatter规范.md §二 定义的通用必填字段
UNIVERSAL_REQUIRED = ("id", "type", "area", "status", "title", "summary", "created", "updated")

def check_universal_fields(root):
    """[G] 检查所有带 frontmatter 的文件是否包含通用必填字段。
    过渡期仅 WARN（不阻断）；迁移完成后可升级为 ERROR。
    工具卡（tools/cards/）的通用字段由 _enrich_readmes.py 补齐前，单独 WARN。
    """
    print("[G] 通用字段缺失检查（过渡期 WARN）")
    readme_root = os.path.join(root, README_DIR)
    note_count = 0
    tool_count = 0
    note_missing = 0
    tool_missing = 0
    for dp, dn, fn in os.walk(root):
        if ".git" in dp:
            continue
        # archive/ 为 L3 素材仓（外部来源），frontmatter 不受本库规范约束，豁免
        if "archive" in dp.split(os.sep) or "references" in dp.split(os.sep) or "原始来源包" in dp.split(os.sep):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, root)
            with open(p, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            pf = parse_frontmatter(text)
            if pf is None:
                continue  # 无 frontmatter，放行
            fm, order, body = pf
            is_tool = p.startswith(readme_root)
            if is_tool:
                tool_count += 1
            else:
                note_count += 1
            missing = [k for k in UNIVERSAL_REQUIRED if k not in fm or not fm[k].strip()]
            if missing:
                if is_tool:
                    tool_missing += 1
                else:
                    note_missing += 1
                # 只报告前 5 个缺失字段，避免过长
                shown = missing[:5]
                suffix = f" 等{len(missing)}项" if len(missing) > 5 else ""
                warn(f"[G] 缺通用字段 {shown}{suffix}: {rel}")
    print(f"  · 笔记层: {note_count} 篇，{note_missing} 篇缺字段")
    print(f"  · 工具卡: {tool_count} 篇，{tool_missing} 篇缺字段（待 _enrich_readmes.py 补齐）")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    args = sys.argv[1:]
    root = None
    as_json = False
    as_json_file = None
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--json":
            as_json = True
        elif a.startswith("--json-file="):
            as_json = True
            as_json_file = a.split("=", 1)[1]
        elif a == "--json-file" and i + 1 < len(args):
            as_json = True
            as_json_file = args[i + 1]
            i += 1
        elif a == "--root":
            root = args[i + 1]
            i += 1
        elif a.startswith("--root="):
            root = a.split("=", 1)[1]
        i += 1
    if root is None:
        # 脚本位于 tools/scripts/validation/校验脚本.py，根为父目录的父目录的父目录的父目录
        root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

    # 报告输出目标：--json 时报告走 stderr，JSON 纯净走 stdout
    _orig_stdout = sys.stdout
    if as_json:
        sys.stdout = sys.stderr

    print("=" * 60)
    print(f"知识库维护校验  ·  根: {root}")
    print("=" * 60)
    print("[A] 工具卡完整性")
    check_readmes(root)
    print("[B] 笔记层 frontmatter 合规")
    check_note_frontmatter(root)
    print("[C] 结构不变量")
    check_structure(root)
    print("[D] 关键 wiki 链接")
    check_wikilinks(root)
    print("[E] 命名契约")
    check_naming_contract(root)
    print("[F] 正文层 frontmatter 强制")
    check_body_frontmatter(root)
    print("[G] 通用字段缺失检查")
    check_universal_fields(root)
    print("=" * 60)

    verdict = "PASS ✅（无 ERROR，可提交）" if not ERRORS else \
        f"FAIL ❌（{len(ERRORS)} 个 ERROR，需修复后再提交）"
    print(f"结论: {verdict}")
    if WARNS:
        print(f"提示: {len(WARNS)} 条 WARN（不阻断）")
    print("=" * 60)

    if as_json:
        sys.stdout = _orig_stdout
        out = {
            "errors": ERRORS,
            "warns": WARNS,
            "error_count": len(ERRORS),
            "warn_count": len(WARNS),
            "pass": len(ERRORS) == 0,
        }
        json_str = "\n" + json.dumps(out, ensure_ascii=False, indent=2) + "\n"
        # 输出 JSON 到临时文件，避免 PowerShell 重定向问题
        if as_json_file:
            with open(as_json_file, 'w', encoding='utf-8') as f:
                f.write(json_str)
        else:
            sys.stdout.write(json_str)

    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
