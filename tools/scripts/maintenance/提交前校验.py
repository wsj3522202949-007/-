#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
提交前校验.py —— 已合并到统一门禁 run_all.py（单一权威入口）

本文件现为「委托包装器」：直接调用 run_all.py 的 main()，
确保所有门禁入口给出**完全一致**的结果，不再各自为政。

原先独有的检查项（编码、同目录重名、链接、frontmatter、结构、旧路径、
重复 ID）已全部并入 run_all.py，并统一以 gate_scope.py 的严格区为唯一范围。

用法（与以前兼容）:
  python 提交前校验.py            # 人类可读报告（= run_all.py）
  python 提交前校验.py --json     # 机器可读 JSON（= run_all.py --json）
  python 提交前校验.py --root <路径>

说明：--fix / --core-only / --exclude 等历史参数已被忽略（统一门禁只认
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
_RUN_ALL = os.path.normpath(os.path.join(_HERE, "..", "validation", "run_all.py"))

if not os.path.isfile(_RUN_ALL):
    sys.stderr.write(f"[提交前校验] 找不到统一门禁 run_all.py: {_RUN_ALL}\n")
    sys.exit(2)

import importlib.util
_spec = importlib.util.spec_from_file_location("run_all", _RUN_ALL)
_run_all_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_run_all_mod)

if __name__ == "__main__":
    sys.stderr.write(
        "[提交前校验] 已合并到 run_all.py，现委托执行（结果完全一致）。\n")
    sys.exit(_run_all_mod.main())
