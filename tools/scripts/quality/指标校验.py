#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
指标校验.py —— platform_metrics 的 machine 字段解析与一致性检查
================================================================

把 platform_metrics.yaml 里新增的 machine 块变成机器可执行：
  - 结构校验：kind 合法、condition/formula/nodes 按 kind 齐备
  - 条件求值：用样例数据 eval condition，验证表达式可运行
  - 输出报告：统计各 kind 分布 + 异常清单

用法
----
  python 指标校验.py                          # 全部项目
  python 指标校验.py （已删除项目）      # 单项目
  python 指标校验.py --json
"""

import os
import re
import sys
import json
import argparse

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

VALID_KINDS = {"threshold", "formula", "workflow", "flag"}
SAMPLE = {"shelf_ratio": 0.40, "follow_ratio": 0.30, "stored_words": 120000,
          "words": 80000, "apply_count": 2, "x": 1}


def find_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "projects")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def check_metrics(path):
    """解析 platform_metrics.yaml 的 metrics 列表，检查 machine 块。"""
    import yaml as _yaml
    errors, warnings, stats = [], [], {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = _yaml.safe_load(f)
    except Exception as e:
        return [f"[{path}] YAML 解析失败: {e}"], [], {}
    metrics = data.get("metrics", []) if isinstance(data, dict) else []
    kinds = {}
    for m in metrics:
        mid = m.get("id", "?")
        machine = m.get("machine")
        if machine is None:
            warnings.append(f"[{mid}] 无 machine 字段（非机器可计算）")
            continue
        kind = machine.get("kind")
        if kind not in VALID_KINDS:
            errors.append(f"[{mid}] machine.kind 非法: {kind!r}")
            continue
        kinds[kind] = kinds.get(kind, 0) + 1
        # 按 kind 校验必备字段
        if kind == "threshold":
            if "condition" not in machine:
                errors.append(f"[{mid}] threshold 缺少 condition")
            else:
                # 尝试求值（样例数据），验证表达式可运行
                try:
                    eval(machine["condition"], {"__builtins__": {}}, dict(SAMPLE))
                except Exception as e:
                    errors.append(f"[{mid}] condition 求值失败: {e}")
        elif kind == "formula":
            if "formula" not in machine:
                errors.append(f"[{mid}] formula 缺少 formula 字段")
        elif kind == "workflow":
            if "nodes" not in machine or not isinstance(machine["nodes"], list):
                errors.append(f"[{mid}] workflow 缺少 nodes 列表")
    stats["total"] = len(metrics)
    stats["with_machine"] = sum(1 for m in metrics if m.get("machine"))
    stats["kinds"] = kinds
    return errors, warnings, stats


def main():
    ap = argparse.ArgumentParser(description="平台指标 machine 字段校验")
    ap.add_argument("project", nargs="?", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--root", default=None)
    args = ap.parse_args()

    root = os.path.abspath(args.root) if args.root else find_root()
    proj_dir = os.path.join(root, "projects")
    targets = [args.project] if args.project else sorted(os.listdir(proj_dir))
    all_errors, all_warnings, all_stats = [], [], []
    for name in targets:
        path = os.path.join(proj_dir, name, "platform_metrics.yaml")
        if not os.path.isfile(path):
            continue
        errs, warns, stats = check_metrics(path)
        if errs or warns or stats.get("with_machine"):
            all_errors += errs
            all_warnings += warns
            all_stats.append({"project": name, **stats})

    if args.json:
        print(json.dumps({"errors": all_errors, "warnings": all_warnings,
                          "stats": all_stats}, ensure_ascii=False, indent=2))
    else:
        print("=" * 60)
        print("平台指标 machine 字段校验")
        print("=" * 60)
        for s in all_stats:
            print(f"  {s['project']}: 指标 {s['total']} | machine {s['with_machine']} | "
                  f"kind {s['kinds']}")
        if all_warnings:
            print(f"\n⚠️ {len(all_warnings)} 个警告（无 machine 字段）:")
            for w in all_warnings[:10]:
                print(f"  {w}")
        if all_errors:
            print(f"\n❌ {len(all_errors)} 个错误:")
            for e in all_errors[:10]:
                print(f"  {e}")
        else:
            print("\n✅ machine 字段全部合法")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
