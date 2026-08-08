#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
test_gate_scope.py —— 门禁范围的防回归测试
==========================================

为什么需要这个测试
------------------
统一门禁曾长期报「总体通过」，但那是**假绿灯**：
`run_all.py` 的 CORE_DIRS 只有 schema/knowledge/projects/methods，
于是 README、CLAUDE、ai/、goals/、maintenance/、tools 导航层的错误
全被降级成「外部资料警告」，永远不阻断。

范围一旦被悄悄缩小，门禁就会重新变成摆设，而且**表面还是绿的**——
这类回归不会自己暴露出来。所以必须有测试把范围钉死。

运行
----
    python tools/scripts/validation/test_gate_scope.py
退出码 0 = 全部通过。
"""

import os
import sys
import importlib.util

# Windows GBK 终端安全：避免 emoji/中文输出 UnicodeEncodeError
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass



def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


HERE = os.path.dirname(os.path.abspath(__file__))
SCOPE_PATH = os.path.normpath(os.path.join(HERE, "..", "gate_scope.py"))
scope = _load(SCOPE_PATH, "gate_scope")


# (相对路径, 期望分区)
CASES = [
    # —— 严格区：这些正是当年被漏掉的地方，一条都不许再掉出去 ——
    ("README.md", "strict"),
    ("CLAUDE.md", "strict"),
    ("ai/入口.md", "strict"),
    ("ai/constraints/格式要求.md", "strict"),
    ("schema/frontmatter规范.md", "strict"),
    ("knowledge/任意.md", "strict"),
    ("projects/某书/chapters/第001章-开局.md", "strict"),
    ("goals/yearly/2026.md", "strict"),
    ("maintenance/入口.md", "strict"),
    ("maintenance/reports/weekly-health-2026-08-04.md", "strict"),
    ("methods/网文写作最强SOP.md", "strict"),
    ("tools/最终索引.md", "strict"),                 # tools 导航层
    ("tools/分类导航.md", "strict"),
    ("tools/分类导航/01_二_网文.md", "strict"),
    ("tools/推荐层/README.md", "strict"),
    ("tools/推荐层/分类/写作辅助.md", "strict"),
    ("tools/检索层/README.md", "strict"),
    ("tools/检索层/按评级/B级.md", "strict"),

    # —— 严格区内部豁免（模板 / 示范，允许占位符）——
    ("methods/templates/01_单章作战卡.md", "external"),
    ("methods/templates/已填示范/【示范】神瞳鉴宝/前5章总评.md", "external"),
    ("methods/项目骨架模板/framework.md", "external"),

    # —— 排除区：完全不扫描 ——
    ("archive/任意素材.md", "excluded"),
    ("references/原始来源包/nuwa-skill-main/README.md", "excluded"),
    ("tools/cards/00002__forsonny__X.md", "excluded"),
    ("maintenance/reports/history/Batch-01清理记录.md", "excluded"),
    ("drafts/scratch/收件箱.md", "excluded"),
    (".git/config", "excluded"),
    ("tools/scripts/__pycache__/x.md", "excluded"),

    # —— 外部区：参考性质，不阻断 ——
    ("references/README.md", "external"),
    ("references/在线调研/某报告.md", "external"),
    ("tools/scripts/说明.md", "external"),
    ("tools/reports/weekly-health-2026-08-04.md", "external"),
    ("Git仓库清理清单.md", "external"),

    # —— 边界：同名子目录不得被误伤 ——
    # projects/<书名>/drafts/ 是项目内草稿，不是顶层 drafts/，必须留在严格区
    ("projects/（已删除项目）/drafts/第011章-作战卡.md", "strict"),
]


def main():
    failures = []
    for rel, expect in CASES:
        got = scope.zone_of(rel)
        if got != expect:
            failures.append((rel, expect, got))

    # 反向断言：严格区目录一个都不能少（防止有人删条目）
    must_have = ("ai/", "schema/", "methods/", "knowledge/", "projects/",
                 "goals/", "maintenance/", "tools/分类导航/",
                 "tools/推荐层/", "tools/检索层/")
    missing = [d for d in must_have if d not in scope.STRICT_DIR_PREFIXES]
    for d in missing:
        failures.append((d, "在 STRICT_DIR_PREFIXES 中", "缺失"))
    for f in ("README.md", "CLAUDE.md"):
        if f not in scope.STRICT_ROOT_FILES:
            failures.append((f, "在 STRICT_ROOT_FILES 中", "缺失"))

    # 反向断言：排除区不得超出约定的五项（防止有人偷偷加排除项来「变绿」）
    allowed_excludes = {
        "archive/", "references/原始来源包/", "tools/cards/",
        "maintenance/reports/history/", "drafts/",
    }
    extra = set(scope.EXCLUDE_PREFIXES) - allowed_excludes
    for e in sorted(extra):
        failures.append((e, "不应出现在排除区", "被排除"))

    print("=" * 60)
    print("门禁范围防回归测试")
    print("=" * 60)
    if failures:
        for rel, expect, got in failures:
            print(f"  ❌ {rel}\n     期望: {expect}   实际: {got}")
        print("-" * 60)
        print(f"FAIL ❌ {len(failures)} 项不符（范围被改动，可能重新引入假绿灯）")
        return 1

    print(f"  ✅ {len(CASES)} 条分区断言全部通过")
    print("  ✅ 严格区目录清单完整")
    print("  ✅ 排除区未被擅自扩大")
    print("-" * 60)
    print("PASS ✅")
    return 0


if __name__ == "__main__":
    sys.exit(main())
