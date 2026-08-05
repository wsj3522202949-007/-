#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
质量门禁系统.py —— 已合并到统一门禁 run_all.py（单一权威入口）

本文件现为「委托包装器」：直接调用 run_all.py 的 main()，
确保所有门禁入口给出**完全一致**的结果，不再各自为政。

原先的 zone 体系（core/all）已取消：现在只认 gate_scope.py 的严格区，
外部资料走 run_all.py 的 external_warnings，不再单独报 ERROR。

用法（与以前兼容）:
  python 质量门禁系统.py            # 全库（= run_all.py 严格区）
  python 质量门禁系统.py --zone core  # 严格区（同上，默认）
  python 质量门禁系统.py --json     # 机器可读 JSON
  python 质量门禁系统.py --root <路径>
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
    sys.stderr.write(f"[质量门禁系统] 找不到统一门禁 run_all.py: {_RUN_ALL}\n")
    sys.exit(2)

import importlib.util
_spec = importlib.util.spec_from_file_location("run_all", _RUN_ALL)
_run_all_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_run_all_mod)

if __name__ == "__main__":
    sys.stderr.write(
        "[质量门禁系统] 已合并到 run_all.py，现委托执行（结果完全一致）。\n")
    sys.exit(_run_all_mod.main())
