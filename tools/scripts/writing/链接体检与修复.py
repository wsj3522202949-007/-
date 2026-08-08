#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
全库链接体检与修复（链接医生）
==============================
专门兜底「全库链接最稳」三件事（维护/校验脚本.py 只部分覆盖）：

1. 链接文本中的未转义 `_`
   - markdown 链接 `[显示文本](路径)`：显示文本里的 `_` 易触发 Markdown 斜体，需转义 `\_`。
   - wikilink `[[目标|别名]]`：别名里的 `_` 同理，仅转义别名，绝不碰目标（否则解析失败）。
   - 目标/路径里的 `_` 是真实文件名，**不转义**。
2. 无效 wiki 链接（全库 `[[...]]` + 相对 markdown 链接，vault 级解析）
3. 中文 tag / 命名空间规范（规则同 维护/校验脚本.py 与 库/标签规范.md）

退出码：0 = 无 ERROR；1 = 有 ERROR（断链 / tag 违规）。
未转义 `_` 仅记 WARN（可用 --fix 自动转义，不阻断提交）。

用法
----
    python 通用小说创作流程/工具/链接体检与修复.py            # 检测报告
    python 通用小说创作流程/工具/链接体检与修复.py --fix       # 自动转义链接文本里的 _
    python 通用小说创作流程/工具/链接体检与修复.py --json      # 机器可读
    python 通用小说创作流程/工具/链接体检与修复.py --root <路径>

约定
----
- `--fix` 只动「链接显示/别名文本」里的 `_`，安全可重入；断链与 tag 违规只报告不自动改。
- 与 `维护/校验脚本.py` 互补：那个守「不变量契约」，这个守「链接最稳」。
"""

import os
import re
import sys
import json

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
SKIP_DIRS = (".git", ".workbuddy", "archive")

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
        if os.path.isdir(os.path.join(d, "库", "enriched", "readmes")) or \
           os.path.isdir(os.path.join(d, "维护")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.abspath(start or __file__))


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
    """去除 fenced / inline 代码块，避免把代码里的字面 [[...]]/(...) 当成链接。

    例：文档里写 `[[双向链接]]` 教 wiki 语法，是字面量不是真链接，应跳过。
    """
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`\n]*`', '', text)
    return text


# ---------------------------------------------------------------------------
# 1. 未转义 _ 在链接文本
# ---------------------------------------------------------------------------
def check_underscores(root, fix):
    changes = []  # (rel, n)
    readme_root = os.path.join(root, "库", "enriched", "readmes")
    for dp, dn, fn in os.walk(root):
        if any(m in dp.split(os.sep) for m in SKIP_DIRS):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            if p.startswith(readme_root):
                continue  # 爬取的外部 README 正文含非 vault 链接，跳过
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
                # 仅检测
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
        print(f"  · 链接文本未转义 _ 检测完成（见上方 WARN）")


# ---------------------------------------------------------------------------
# 2. 无效 wiki / markdown 链接（vault 级解析）
# ---------------------------------------------------------------------------
def resolve(root, filedir, target):
    target = target.split("#")[0].split("^")[0].strip()
    if not target:
        return False
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


def check_broken_links(root):
    count = 0
    readme_root = os.path.join(root, "库", "enriched", "readmes")
    for dp, dn, fn in os.walk(root):
        if any(m in dp.split(os.sep) for m in SKIP_DIRS):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            if p.startswith(readme_root):
                continue  # 爬取外部 README 正文含非 vault 链接，跳过
            rel = os.path.relpath(p, root)
            with open(p, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            text = strip_code(text)  # 跳过代码块里的字面 [[...]]/(...)
            # wikilinks
            for m in WIKILINK_RE.finditer(text):
                inner = m.group(1)
                tgt = inner.split("|", 1)[0].strip()
                if not resolve(root, dp, tgt):
                    err(f"[2] 断链(wiki): {rel}  →  [[{inner}]]")
                    count += 1
            # markdown 链接（相对路径，非外部）
            for m in MD_LINK_RE.finditer(text):
                url = m.group(2).strip()
                if url.startswith(("#", "http://", "https://", "mailto:", "ftp://")):
                    continue
                if re.fullmatch(r'[一-鿿]+', url):
                    continue  # 占位符如 (链接)/(参见)，非真实链接
                if not resolve(root, dp, url):
                    err(f"[2] 断链(md): {rel}  →  ({url})")
                    count += 1
    print(f"  · 全库链接解析：{count} 条失效"
          + ("（ERROR，需修复）" if count else "，全部有效 ✅"))


# ---------------------------------------------------------------------------
# 3. 中文 tag / 命名空间规范
# ---------------------------------------------------------------------------
def check_tags(root):
    readme_root = os.path.join(root, "库", "enriched", "readmes")
    for dp, dn, fn in os.walk(root):
        if any(m in dp.split(os.sep) for m in SKIP_DIRS):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, root)
            if p.startswith(readme_root):
                continue
            with open(p, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
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
    print(f"  · 笔记层 tag/命名空间校验完成（双轨：平键 ERROR / 旧格式 WARN）")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    args = sys.argv[1:]
    root = None
    fix = False
    as_json = False
    for a in args:
        if a == "--fix":
            fix = True
        elif a == "--json":
            as_json = True
        elif a.startswith("--root"):
            root = a.split("=", 1)[1] if "=" in a else None
    if root is None and "--root" in args:
        i = args.index("--root")
        root = args[i + 1] if i + 1 < len(args) else None
    if root is None:
        root = find_root(__file__)

    _orig = sys.stdout
    if as_json:
        sys.stdout = sys.stderr

    print("=" * 60)
    print(f"链接体检与修复  ·  根: {root}" + ("  [--fix 模式]" if fix else ""))
    print("=" * 60)
    print("[1] 链接文本未转义 _")
    check_underscores(root, fix)
    print("[2] 无效 wiki / markdown 链接")
    check_broken_links(root)
    print("[3] 中文 tag / 命名空间规范")
    check_tags(root)
    print("=" * 60)

    if ERRORS:
        print(f"--- ERROR 明细（{len(ERRORS)}）---")
        for e in ERRORS:
            print("  ❌", e)
    if WARNS:
        print(f"--- WARN 明细（{len(WARNS)}，未转义_等）---")
        for w in WARNS:
            print("  ⚠", w)

    verdict = "PASS ✅" if not ERRORS else f"FAIL ❌（{len(ERRORS)} ERROR）"
    print(f"结论: {verdict}  |  WARN(含未转义_): {len(WARNS)}")
    print("=" * 60)

    if as_json:
        sys.stdout = _orig
        json.dump({"errors": ERRORS, "warns": WARNS,
                   "error_count": len(ERRORS), "warn_count": len(WARNS),
                   "pass": not ERRORS}, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")

    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
