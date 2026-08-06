#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
gate_scope.py —— 门禁范围的唯一权威定义
=======================================

背景（为什么有这个文件）
------------------------
在此之前，`run_all.py`、`quality/链接检查器-修复版.py`、
`maintenance/提交前校验.py` 各自维护了一份 `CORE_DIRS`，且三份互不相同：

    run_all.py            CORE_DIRS = schema / knowledge / projects / methods
    链接检查器-修复版.py    CORE_DIRS = schema / knowledge / projects / methods
    提交前校验.py          CORE_DIRS = projects / methods / schema / maintenance

结果是统一门禁只覆盖了四个目录，把 README / CLAUDE / ai/ / goals/ /
maintenance/ / tools 导航层全部漏在外面，于是它们的错误被降级成
"external_warnings"，门禁照样报「总体通过」——**假绿灯**。

本模块把范围划分收敛成一处，任何门禁脚本都必须 import 它，不得自己再定义。


三分区模型
----------
    STRICT   严格区：ERROR 即 FAIL，阻断提交
    EXTERNAL 外部区：只产生 warning，供参考，不阻断
    EXCLUDED 排除区：完全不扫描，也不进任何报告

严格区（strict）
    README.md、CLAUDE.md          —— 根入口
    ai/                           —— AI 读写层
    schema/                       —— 规范契约
    methods/                      —— 方法论（模板/示范子目录豁免，见下）
    knowledge/                    —— 知识层
    projects/                     —— 项目层
    goals/                        —— 目标层
    maintenance/                  —— 维护层（reports/history 已在排除区）
    tools/*.md                    —— 工具区导航层（tools 根目录直属文档）
    tools/分类导航/                —— 分类导航层
    tools/推荐层/
    tools/检索层/

严格区内部豁免（属于严格区路径，但允许占位符/未填示例，按外部区处理）
    methods/templates/            —— 模板与「已填示范」
    methods/项目骨架模板/          —— 骨架占位符

排除区（excluded，完全不扫描）
    archive/
    references/原始来源包/
    tools/cards/
    maintenance/reports/history/
    drafts/
    以及基础设施目录：.git .workbuddy .obsidian node_modules __pycache__ .tools

外部区（external）
    以上都不匹配的其余内容，典型如：
    references/（除原始来源包）、tools/scripts/、tools/reports/、
    根目录其余散文档（如 Git仓库清理清单.md）


路径约定
--------
本模块所有函数接收的 `rel` 均为**相对库根的路径**。Windows 上
`os.path.relpath` 返回反斜杠，函数内部统一规范化为 `/`，调用方无需自己处理。
"""

import os

__all__ = [
    "STRICT_ROOT_FILES",
    "STRICT_DIR_PREFIXES",
    "STRICT_EXEMPT_PREFIXES",
    "EXCLUDE_PREFIXES",
    "SKIP_COMPONENTS",
    "norm",
    "is_excluded",
    "is_strict",
    "zone_of",
    "should_skip_dir",
    "iter_md_files",
    "scope_summary",
    "describe",
]

# —— 严格区：根目录入口文件 ——
STRICT_ROOT_FILES = ("README.md", "CLAUDE.md")

# —— 严格区：目录前缀 ——
STRICT_DIR_PREFIXES = (
    "ai/",
    "schema/",
    "methods/",
    "knowledge/",
    "projects/",
    "goals/",
    "maintenance/",
    "tools/分类导航/",
    "tools/推荐层/",
    "tools/检索层/",
)

# —— 严格区内部豁免（降级为外部区）——
STRICT_EXEMPT_PREFIXES = (
    "methods/templates/",
    "methods/项目骨架模板/",
)

# —— 排除区：完全不扫描（前缀匹配，仅限顶层指定路径）——
# 用前缀而非路径组件匹配，避免误伤 projects/<书名>/drafts/ 这类同名子目录。
EXCLUDE_PREFIXES = (
    "archive/",
    "references/原始来源包/",
    "tools/cards/",
    "maintenance/reports/history/",
    "drafts/",
)

# —— 基础设施目录：按路径组件匹配，任意层级都跳过 ——
SKIP_COMPONENTS = frozenset({
    ".git", ".workbuddy", ".obsidian", "node_modules", "__pycache__", ".tools",
})


def norm(rel):
    """把相对路径统一为正斜杠形式，并去掉开头的 './'。"""
    rel = (rel or "").replace(os.sep, "/").replace("\\", "/")
    while rel.startswith("./"):
        rel = rel[2:]
    return rel.strip("/")


def _has_skip_component(rel):
    return any(part in SKIP_COMPONENTS for part in norm(rel).split("/"))


def is_excluded(rel):
    """是否属于排除区（完全不扫描、不进报告）。"""
    r = norm(rel)
    if not r:
        return False
    if _has_skip_component(r):
        return True
    for p in EXCLUDE_PREFIXES:
        if r == p.rstrip("/") or r.startswith(p):
            return True
    return False


def is_strict(rel):
    """是否属于严格区（ERROR 即 FAIL）。排除区一律返回 False。"""
    r = norm(rel)
    if not r or is_excluded(r):
        return False

    # 严格区内部豁免优先于命中判定
    for p in STRICT_EXEMPT_PREFIXES:
        if r.startswith(p):
            return False

    # 根目录入口文件
    if r in STRICT_ROOT_FILES:
        return True

    # 目录前缀
    for p in STRICT_DIR_PREFIXES:
        if r == p.rstrip("/") or r.startswith(p):
            return True

    # tools 导航层：tools/ 根目录直属 .md
    if r.startswith("tools/") and r.count("/") == 1 and r.endswith(".md"):
        return True

    return False


def zone_of(rel):
    """返回 'excluded' / 'strict' / 'external' 三者之一。"""
    if is_excluded(rel):
        return "excluded"
    if is_strict(rel):
        return "strict"
    return "external"


def should_skip_dir(dir_path, root):
    """os.walk 剪枝：该目录整棵子树是否可以直接跳过。"""
    try:
        rel = os.path.relpath(dir_path, root)
    except ValueError:
        return False
    if rel in (".", ""):
        return False
    return is_excluded(rel)


def iter_md_files(root, include_external=True):
    """遍历库内 .md 文件，产出 (abs_path, rel_posix, zone)。

    自动跳过排除区。include_external=False 时只产出严格区文件。
    """
    for dp, dn, fn in os.walk(root):
        # 原地剪枝，避免走进排除区子树
        dn[:] = [d for d in dn
                 if not should_skip_dir(os.path.join(dp, d), root)]
        if should_skip_dir(dp, root):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            ap = os.path.join(dp, f)
            rel = norm(os.path.relpath(ap, root))
            z = zone_of(rel)
            if z == "excluded":
                continue
            if not include_external and z != "strict":
                continue
            yield ap, rel, z


def scope_summary(root):
    """统计各区文件数，用于门禁报告的范围透明度。"""
    counts = {"strict": 0, "external": 0}
    for _ap, _rel, z in iter_md_files(root):
        counts[z] = counts.get(z, 0) + 1
    return counts


def describe():
    """返回范围定义的结构化描述，便于写进 JSON 报告。"""
    return {
        "strict": {
            "root_files": list(STRICT_ROOT_FILES),
            "dirs": list(STRICT_DIR_PREFIXES),
            "tools_nav_root_md": "tools/*.md",
            "exempt": list(STRICT_EXEMPT_PREFIXES),
        },
        "excluded": list(EXCLUDE_PREFIXES),
        "skip_components": sorted(SKIP_COMPONENTS),
        "external": "其余未匹配内容（references/、tools/scripts/、tools/reports/ 等）",
    }


if __name__ == "__main__":
    import sys
    import json

    r = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    print(json.dumps({
        "root": r,
        "scope": describe(),
        "counts": scope_summary(r),
    }, ensure_ascii=False, indent=2))
