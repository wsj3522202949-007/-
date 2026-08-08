#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
检索基准.py — 工具卡检索效果基准（Baseline）

为 tools/cards/ 的 3572 张工具卡建立检索效果基准：
对每一类"检索任务"（按 category 语义分组），用关键词在
title/summary/tags/category 上做检索，计算召回率。

产出：
  - 每类任务的召回率（检索命中该类卡片数 / 该类卡片总数）
  - 总体平均召回率 = 基准分数（Baseline）
  - 报告写入 tools/reports/检索基准.md

用法：
  python tools/scripts/quality/检索基准.py             # 生成/更新基准报告
  python tools/scripts/quality/检索基准.py --json      # 输出 JSON
  python tools/scripts/quality/检索基准.py --check     # 只校验不写报告（CI 用）

注意：本基准衡量的是"关键词检索的召回覆盖"，是检索能力的下限基线，
不衡量排序质量（Top-K 相关性）。后续引入向量检索后可对比提升。
"""
import os
import re
import sys
import json
import argparse
from datetime import datetime

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
CARDS_DIR = os.path.join(ROOT, "tools", "cards")
REPORT_DIR = os.path.join(ROOT, "tools", "reports")
REPORT_FILE = os.path.join(REPORT_DIR, "检索基准.md")

# ---------------------------------------------------------------------------
# 检索任务定义：类别语义 → 检索关键词
# 每类任务的"黄金集" = category 字段命中语义的卡片
# ---------------------------------------------------------------------------
TASKS = [
    {
        "name": "去AI味/Humanizer",
        "cat_keywords": ["去 AI 味", "去AI味"],
        "search_keywords": ["humanizer", "去AI味", "去 AI 味", "降 AI", "去味"],
    },
    {
        "name": "网文/长篇AI写作系统",
        "cat_keywords": ["网文 / 长篇"],
        "search_keywords": ["writing", "写作系统", "novel", "小说", "story"],
    },
    {
        "name": "长篇一致性/RAG/故事圣经",
        "cat_keywords": ["长篇一致性"],
        "search_keywords": ["RAG", "一致性", "故事圣经", "记忆", "memory"],
    },
    {
        "name": "写作IDE/本地工作台",
        "cat_keywords": ["写作 IDE"],
        "search_keywords": ["IDE", "工作台", "workbench", "editor", "本地优先"],
    },
    {
        "name": "多Agent小说生产",
        "cat_keywords": ["多 Agent"],
        "search_keywords": ["multi-agent", "多Agent", "多代理", "agent", "叙事引擎"],
    },
    {
        "name": "大纲/规划/结构软件",
        "cat_keywords": ["大纲"],
        "search_keywords": ["outline", "大纲", "规划", "结构", "plot"],
    },
    {
        "name": "语法/风格检查/校对",
        "cat_keywords": ["语法"],
        "search_keywords": ["grammar", "语法", "风格检查", "校对", "润色", "proofread"],
    },
    {
        "name": "TTS/有声书",
        "cat_keywords": ["有声书"],
        "search_keywords": ["TTS", "有声书", "语音", "tts", "audio"],
    },
    {
        "name": "互动叙事/AI Dungeon",
        "cat_keywords": ["互动叙事"],
        "search_keywords": ["互动叙事", "dungeon", "interactive", "chat bot", "聊天"],
    },
    {
        "name": "短剧/剧本/影视化",
        "cat_keywords": ["短剧"],
        "search_keywords": ["短剧", "剧本", "影视化", "screenplay", "film"],
    },
]


def load_cards():
    """加载所有卡片：返回 list[dict{file, title, summary, tags, category}]。"""
    cards = []
    for f in sorted(os.listdir(CARDS_DIR)):
        if not f.endswith(".md") or f == "README.md":
            continue
        head = open(os.path.join(CARDS_DIR, f), encoding="utf-8", errors="replace").read(4000)
        def get_field(key):
            m = re.search(rf"^{key}:\s*(.+)$", head, re.MULTILINE)
            return m.group(1).strip().strip('"').strip("'") if m else ""
        title = get_field("title") or f
        summary = get_field("summary")
        category = get_field("category")
        tags = get_field("tags")
        cards.append({
            "file": f,
            "title": title,
            "summary": summary,
            "category": category,
            "tags": tags,
            # 可检索文本：只用 title/summary/tags，不含 category。
            # 若含 category 则检索与黄金集同源，形成自证循环（曾导致 100% 假基线）。
            # 真实用户搜索时只看到工具名/简介/标签，看不到分类字段。
            "haystack": f"{title} {summary} {tags}".lower(),
        })
    return cards


def in_category(card, cat_keywords):
    """卡片是否属于该任务语义类别（黄金集判定）。"""
    cat = card["category"].lower()
    return any(k.lower() in cat for k in cat_keywords)


def search(card, keywords):
    """关键词检索：任一关键词命中即可（title/summary/tags/category 全文）。"""
    h = card["haystack"]
    return any(k.lower() in h for k in keywords)


def run_baseline(cards):
    """计算每类任务召回率。"""
    results = []
    total_hits = total_gold = 0
    for task in TASKS:
        gold = [c for c in cards if in_category(c, task["cat_keywords"])]
        if not gold:
            results.append({**task, "gold": 0, "hits": 0, "recall": None, "missed": []})
            continue
        hits = [c for c in gold if search(c, task["search_keywords"])]
        missed = [c["file"] for c in gold if c not in hits]
        recall = len(hits) / len(gold)
        total_hits += len(hits)
        total_gold += len(gold)
        results.append({
            **task,
            "gold": len(gold),
            "hits": len(hits),
            "recall": round(recall, 3),
            "missed_files": missed[:10],  # 只列前 10 个漏检样本
            "missed_total": len(missed),
        })
    overall = round(total_hits / total_gold, 3) if total_gold else None
    return results, overall


def render_md(results, overall, total_cards, run_date):
    lines = [
        "---",
        "id: tools-retrieval-baseline",
        "type: report",
        "area: 库",
        "status: active",
        "tags: [工具, 检索, 基准, 评测]",
        f"title: 工具卡检索效果基准 - {run_date}",
        "summary: 关键词检索召回率基线，衡量检索层能否覆盖各类工具卡。",
        "source: 自动生成",
        f"created: {run_date}",
        f"updated: {run_date}",
        "---",
        "",
        f"# 工具卡检索效果基准（{run_date}）",
        "",
        f"> 基准卡片总数：**{total_cards}** 张。",
        f"> 总体平均召回率：**{overall:.1%}**（{overall if overall else 'N/A'}）",
        "",
        "## 什么是本基准",
        "",
        "本基准衡量**关键词检索的召回覆盖**（检索层能否找到该类工具卡），",
        "是检索能力的下限基线，不衡量排序质量。每次新增卡片或改进检索后重跑，",
        "对比本基准即可判断检索是否退化/提升。",
        "",
        "## 各类任务召回率",
        "",
        "| 任务 | 黄金集 | 检索命中 | 召回率 | 漏检数 |",
        "|---|---|---|---|---|",
    ]
    for r in results:
        rec = f"{r['recall']:.1%}" if r["recall"] is not None else "N/A(无卡片)"
        lines.append(
            f"| {r['name']} | {r['gold']} | {r['hits']} | {rec} | {r.get('missed_total', 0)} |"
        )
    lines.append(f"| **总体** | **{sum(r['gold'] for r in results)}** | "
                 f"**{sum(r['hits'] for r in results)}** | **{overall:.1%}** | — |")
    lines += [
        "",
        "## 漏检样本（每类前 10）",
        "",
    ]
    for r in results:
        if r.get("missed_total"):
            lines.append(f"### {r['name']}（漏检 {r['missed_total']}）")
            for mf in r.get("missed_files", []):
                lines.append(f"- `{mf}`")
            lines.append("")
    lines += [
        "---",
        "> 本报告由 tools/scripts/quality/检索基准.py 自动生成，",
        "> 重跑命令：`python tools/scripts/quality/检索基准.py`",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="工具卡检索效果基准")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--check", action="store_true", help="只校验不写报告")
    args = ap.parse_args()

    cards = load_cards()
    results, overall = run_baseline(cards)
    run_date = datetime.now().strftime("%Y-%m-%d")

    if args.json:
        print(json.dumps({
            "total_cards": len(cards),
            "overall_recall": overall,
            "tasks": results,
        }, ensure_ascii=False, indent=2))
        return 0

    if not args.check:
        os.makedirs(REPORT_DIR, exist_ok=True)
        md = render_md(results, overall, len(cards), run_date)
        with open(REPORT_FILE, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"✅ 检索基准报告已写入: {REPORT_FILE}")
        print(f"   总体召回率: {overall:.1%}（{len(cards)} 张卡片，{len(TASKS)} 类任务）")
        for r in results:
            rec = f"{r['recall']:.1%}" if r["recall"] is not None else "N/A"
            print(f"   {r['name']:<18} 召回 {rec}（{r['hits']}/{r['gold']}）")
        # 低召回任务预警
        weak = [r for r in results if r["recall"] is not None and r["recall"] < 0.5]
        if weak:
            print(f"\n⚠️ 召回率 < 50% 的任务：{', '.join(r['name'] for r in weak)}")
            print("   建议补充该类工具的检索关键词或检查卡片字段完整性")
    else:
        print(f"检索基准检查：总体召回率 {overall:.1%}，任务数 {len(TASKS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
