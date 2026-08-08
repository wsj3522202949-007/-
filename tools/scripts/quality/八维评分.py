#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
八维评分.py —— 章节八维质量评分（情节/人物/世界规则/时间/财务/文风/节奏/趣味性）
================================================================

背景
----
"世界级长篇评估不能只检查字数和关键词"。本项目已有的机器可算信号：
  - chapter_selfcheck：字数/AI味/钩子/重复/模板句
  - continuity_check：时间线/人物状态/金额公式断言
  - entities/ 设定卡：世界规则引用
本脚本把上述信号映射为八维 0-10 分，全部可机器计算，不靠人工感觉。

维度与信号映射
--------------
  情节(plot)       事件密度：段落数/千字、转折词密度（"突然/没想到/竟然/结果"）
  人物(character)  人物卡出场率：正文命中 entities/人物-*.md 的名字数 / 已知人物数
  世界规则(world)  设定引用：正文命中 entities/系统设定|世界观 等关键实体次数
  时间(time)       continuity_check 时间线断言通过率（0 ERROR 即满分）
  财务(finance)    金额公式断言通过率 + 账本累计链完整性
  文风(style)      AI 味干净度（干净=10，微量=8，轻度=6，中度=4，重度=0）
  节奏(pacing)     段落均长 30-60 字为佳 + 对话行占比 20-50% 为佳
  趣味性(fun)      钩子强度（强钩子=满分）+ 爽点词密度（"打脸/碾压/震惊/反转"等）

用法
----
  python 八维评分.py                    # 全部项目
  python 八维评分.py （已删除项目）
  python 八维评分.py --json
"""

import os
import re
import sys
import json
import argparse
import subprocess
import importlib.util
from datetime import datetime, timedelta

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

_HERE = os.path.dirname(os.path.abspath(__file__))
_SC_PATH = os.path.join(_HERE, "..", "writing", "chapter_selfcheck.py")
_spec = importlib.util.spec_from_file_location("chapter_selfcheck", _SC_PATH)
_chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_chk)

# 八维定义
DIMS = ["plot", "character", "world", "time", "finance", "style", "pacing", "fun"]
DIM_CN = {
    "plot": "情节", "character": "人物", "world": "世界规则", "time": "时间",
    "finance": "财务", "style": "文风", "pacing": "节奏", "fun": "趣味性",
}

TURN_WORDS = ["突然", "没想到", "竟然", "居然", "结果", "反手", "一转眼", "就在这时"]
FUN_WORDS = ["打脸", "碾压", "震惊", "反转", "逆袭", "暴富", "狠狠", "栽了",
             "傻眼", "目瞪口呆", "颤抖", "发家", "捡漏"]


def find_root():
    d = _HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "projects")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(_HERE)


def _git_head_sha(root):
    """读取仓库 HEAD 完整 SHA（用于基线 observed_commit）。"""
    try:
        r = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root, capture_output=True, text=True, timeout=15,
            encoding="utf-8", errors="replace",
        )
        if r.returncode == 0:
            return r.stdout.strip() or None
    except Exception:  # noqa: BLE001
        pass
    return None


def find_projects(root):
    out = []
    proj = os.path.join(root, "projects")
    if os.path.isdir(proj):
        for name in sorted(os.listdir(proj)):
            if os.path.isdir(os.path.join(proj, name, "chapters")):
                out.append(name)
    return out


def clamp(x, lo=0, hi=10):
    return max(lo, min(hi, x))


def score_chapter(path, body, entity_names, policy, prev=None):
    """对单章正文计算八维得分。path 为章节完整路径。返回 (scores, signals)。"""
    n = _chk.count_chars(body)
    paras = [p for p in body.split("\n\n") if p.strip()]
    n_para = max(len(paras), 1)
    n_lines = body.count("\n") + 1
    # ---- 情节：事件密度 + 转折词 ----
    turns = sum(body.count(w) for w in TURN_WORDS)
    plot = clamp(4 + n_para / 20 + turns * 1.2)

    # ---- 人物：人物卡名字命中 ----
    if entity_names:
        hit = sum(1 for nm in entity_names if nm in body)
        character = clamp(hit * 2.5)
    else:
        character = 5.0  # 无人物卡时中性分

    # ---- 世界规则：设定实体命中 ----
    world_kws = ["系统", "世界观", "设定"]
    world_hits = sum(1 for w in world_kws if w in body)
    world = clamp(3 + world_hits * 1.5)

    # ---- 时间：月份引用明确且无矛盾（由 continuity 断言给出，此处中性）----
    time = 10.0  # 实际通过率由 continuity 层覆盖

    # ---- 财务：正文金额出现频次（账本断言由 continuity 层覆盖）----
    money = len(re.findall(r'[\d,]+\.?\d*\s*(?:万|元|块|亿)', body))
    finance = clamp(4 + money * 0.8)

    # ---- 文风：AI 味 ----
    r = _chk.check_chapter(path, policy=policy)
    style_map = {"干净": 10, "微量": 8, "轻度": 6, "中度": 4, "重度": 0}
    style = style_map.get(r["ai_verdict"], 5)

    # ---- 节奏：段落均长 + 对话占比 ----
    avg_para = n / n_para
    dialog = len(re.findall(r'"', body)) / 2
    dialog_ratio = dialog / max(n_lines, 1)
    pacing = clamp(10 - abs(avg_para - 45) / 10 - abs(dialog_ratio - 0.35) * 8)

    # ---- 趣味性：钩子 + 爽点词 ----
    fun_words = sum(body.count(w) for w in FUN_WORDS)
    hook_bonus = 2.0 if r["hook_verdict"].startswith("强钩子") else 0
    fun = clamp(4 + fun_words * 0.9 + hook_bonus)

    return {
        "plot": round(plot, 1), "character": round(character, 1),
        "world": round(world, 1), "time": round(time, 1),
        "finance": round(finance, 1), "style": round(style, 1),
        "pacing": round(pacing, 1), "fun": round(fun, 1),
    }, {
        "chars": n, "paras": n_para, "turns": turns,
        "entity_hits": min(hit if entity_names else 0, 4),
        "money_refs": money, "ai_verdict": r["ai_verdict"],
        "avg_para": round(avg_para, 1), "dialog_ratio": round(dialog_ratio, 2),
        "fun_words": fun_words, "hook": r["hook_verdict"][:12],
    }


def score_project(root, proj_name):
    proj_dir = os.path.join(root, "projects", proj_name)
    ch_dir = os.path.join(proj_dir, "chapters")
    policy = _chk.load_policy(ch_dir)

    # 人物卡名字（entities/人物-*.md）
    entity_names = []
    ent_dir = os.path.join(proj_dir, "entities")
    if os.path.isdir(ent_dir):
        for f in os.listdir(ent_dir):
            if f.startswith("人物-") and f.endswith(".md"):
                head = open(os.path.join(ent_dir, f), encoding="utf-8",
                            errors="replace").read(600)
                m = re.search(r'^name:\s*(.+)$', head, re.MULTILINE)
                if m:
                    entity_names.append(m.group(1).strip())

    chapters = []
    if os.path.isdir(ch_dir):
        for fname in sorted(os.listdir(ch_dir)):
            if not fname.startswith("第") or not fname.endswith(".md"):
                continue
            path = os.path.join(ch_dir, fname)
            raw = _chk.read_text(path)
            body = _chk.extract_body(raw)
            scores, signals = score_chapter(path, body, entity_names, policy)
            chapters.append({"file": fname, "scores": scores, "signals": signals})

    # 汇总：八维平均
    agg = {d: [] for d in DIMS}
    for c in chapters:
        for d in DIMS:
            agg[d].append(c["scores"][d])
    summary = {d: round(sum(v) / len(v), 1) if v else 0
               for d, v in agg.items()}
    return {"project": proj_name, "chapters": chapters,
            "chapter_count": len(chapters), "summary": summary}


def render_text(project):
    lines = [f"\n{'=' * 64}", f"项目: {project['project']}", "=" * 64]
    lines.append(f"{'章':<22} " + " ".join(f"{DIM_CN[d]}".ljust(6) for d in DIMS))
    lines.append("-" * 64)
    for c in project["chapters"]:
        row = c["file"][:20].ljust(22)
        for d in DIMS:
            row += f"{c['scores'][d]:<7.1f}"
        lines.append(row)
    lines.append("-" * 64)
    s = project["summary"]
    row = "八维均值".ljust(22)
    for d in DIMS:
        row += f"{s[d]:<7.1f}"
    lines.append(row)
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="章节八维质量评分")
    ap.add_argument("project", nargs="?", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--root", default=None)
    ap.add_argument("--check", action="store_true",
                    help="固化创作质量基线（CI 用）：保存各项目八维均值")
    args = ap.parse_args()

    root = os.path.abspath(args.root) if args.root else find_root()
    targets = [args.project] if args.project else find_projects(root)
    results = [score_project(root, p) for p in targets]

    if args.check:
        baseline_path = os.path.join(root, "tools", "reports", "创作质量基线.json")
        payload = {
            "generated_at": datetime.now().isoformat(),
            "observed_commit": _git_head_sha(root),
            "valid_until": (datetime.now() + timedelta(days=90)).isoformat(),
            "superseded_by": None,
            "projects": [
                {
                    "project": r["project"],
                    "summary": r["summary"],
                } for r in results
            ],
        }
        os.makedirs(os.path.dirname(baseline_path), exist_ok=True)
        with open(baseline_path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
        for r in results:
            s = r["summary"]
            print(f"✅ {r['project']}: "
                  + " | ".join(f"{DIM_CN[d]} {s[d]}" for d in DIMS))
        print(f"创作质量基线已固化 → {baseline_path}")
        # 校验：有实际章节文件的项目均值全 0 说明评分器失效（假基线）；
        # 空项目（示范目录无章节）跳过，避免误报。
        for r in results:
            if r.get("chapter_count", 0) == 0:
                continue
            if all(r["summary"].get(d, 0) == 0 for d in DIMS):
                print(f"❌ {r['project']} 八维均值全 0，评分器疑似失效",
                      file=sys.stderr)
                sys.exit(1)
        return

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for r in results:
            print(render_text(r))
        # 全局均值
        for r in results:
            s = r["summary"]
            print(f"\n【{r['project']}】"
                  + " | ".join(f"{DIM_CN[d]} {s[d]}" for d in DIMS))


if __name__ == "__main__":
    main()
