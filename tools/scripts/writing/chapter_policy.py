# -*- coding: utf-8 -*-
"""
chapter_policy.py — 单章篇幅与质量政策的单一来源（Single Source of Truth）

为什么存在
----------
之前两套脚本各自硬编码字数标准，导致口径分裂：
  - chapter_selfcheck.py        : 2600–3400（宽松 ≤4000）
  - 创作闭环助手.py --self-check : 2300–2700
而 STATUS.md / shared_wordcount.py 采用「正文去空白字符(含标点)」作为字数口径。

本模块把「篇幅标准」抽成项目配置 chapter_policy.{yaml,json}，所有脚本统一读取，
禁止再在各自脚本里写 2300 / 2600 / 3400 之类魔数。

配置字段
--------
  platform       : 目标平台（仅用于报告展示，如「番茄」）
  min_chars      : 达标下限，低于即「不足」
  target_chars   : 推荐目标字数（仅展示/建议，不参与判级）
  max_chars      : 严格达标上限，高于进入「宽松超标」
  hard_max_chars : 硬上限，高于即「严重超标」

配置查找顺序
------------
  load_policy(base) 从 base（文件或目录）向上逐级查找：
    chapter_policy.yaml / chapter_policy.yml / chapter_policy.json
  找不到则用 DEFAULT_POLICY（与番茄标准一致），保证脚本不崩溃。
"""
from __future__ import annotations

import os
import re

DEFAULT_POLICY = {
    "platform": "番茄",
    "min_chars": 2600,
    "target_chars": 3000,
    "max_chars": 3400,
    "hard_max_chars": 4000,
}

_POLICY_KEYS = ("platform", "min_chars", "target_chars", "max_chars", "hard_max_chars")
_CONFIG_NAMES = ("chapter_policy.yaml", "chapter_policy.yml", "chapter_policy.json")


def _coerce(v: str):
    """把 YAML/JSON 文本标量转成 Python 值（字符串/int/float/bool）。"""
    v = v.strip()
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if re.fullmatch(r"-?\d+\.\d+", v):
        return float(v)
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False
    return v


def _parse_yaml(path: str) -> dict:
    """极简 YAML 解析：支持任意深度的 `key: value` 与缩进嵌套，无外部依赖。

    足以读取 chapter_policy 这类小型配置文件；不追求完整 YAML 规范。
    """
    data: dict = {}
    stack = [(-1, data)]
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.rstrip("\n")
            if not stripped.strip() or stripped.lstrip().startswith("#"):
                continue
            indent = len(line) - len(line.lstrip(" "))
            key, _, val = stripped.strip().partition(":")
            key = key.strip()
            # 去掉行内注释（" #" 之后，且不在引号内）
            if ' #' in val:
                val = val.split(' #', 1)[0].strip()
            val = val.strip()
            if not key:
                continue
            # 回退栈到正确的父节点
            while stack and stack[-1][0] >= indent:
                stack.pop()
            parent = stack[-1][1]
            if val == "":
                node: dict = {}
                parent[key] = node
                stack.append((indent, node))
            else:
                parent[key] = _coerce(val)
    return data


def _parse_json(path: str) -> dict:
    import json
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def find_policy_file(start_dir: str) -> str | None:
    """从 start_dir（文件或目录）向上逐级查找配置文件。"""
    cur = os.path.abspath(start_dir)
    if not os.path.isdir(cur):
        cur = os.path.dirname(cur)
    for _ in range(10):
        for name in _CONFIG_NAMES:
            cand = os.path.join(cur, name)
            if os.path.exists(cand):
                return cand
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent
    return None


def load_policy(start_dir: str | None = None, explicit_path: str | None = None) -> dict:
    """返回合并后的政策 dict（DEFAULT_POLICY 打底，配置文件覆盖）。"""
    policy = dict(DEFAULT_POLICY)
    path = explicit_path or (find_policy_file(start_dir) if start_dir else None)
    if path and os.path.exists(path):
        try:
            data = _parse_yaml(path) if path.endswith((".yaml", ".yml")) else _parse_json(path)
            node = data.get("chapter_policy", data) if isinstance(data, dict) else data
            for k in _POLICY_KEYS:
                if k in node and node[k] is not None:
                    policy[k] = node[k]
        except Exception:
            pass  # 解析失败则回退默认，保证脚本不崩溃
    return policy


def char_verdict(n: int, policy: dict | None = None) -> str:
    """统一字数裁决，返回如「达标(3000)」「不足(1500<2600)」「超标(3500>3400)」「严重超标(4500>4000)」。"""
    p = policy or DEFAULT_POLICY
    lo, hi, hard = p["min_chars"], p["max_chars"], p["hard_max_chars"]
    if n < lo:
        return f"不足({n}<{lo})"
    if n > hard:
        return f"严重超标({n}>{hard})"
    if n > hi:
        return f"超标({n}>{hi})"
    return f"达标({n})"


def char_status(n: int, policy: dict | None = None) -> str:
    """返回判级状态：short / ok / loose / over_hard。"""
    p = policy or DEFAULT_POLICY
    if n < p["min_chars"]:
        return "short"
    if n > p["hard_max_chars"]:
        return "over_hard"
    if n > p["max_chars"]:
        return "loose"
    return "ok"
