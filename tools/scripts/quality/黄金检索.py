#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
黄金检索.py —— 固定语料 × 固定问题 × 固定相关性判断的检索评估
================================================================

对齐 NIST TREC 思想
-------------------
TREC 的核心：用**固定语料 + 固定问题集 + 相关性判断**评估检索系统，
而不是凭感觉说"好搜"。本脚本对 tools/cards/ 3572 张工具卡做同样的评测。

指标
----
  Recall@5      前 5 条命中相关卡片的比例
  MRR           首个相关卡片排名的倒数均值
  nDCG@10       前 10 条 DCG / 理想 DCG（相关性分级 0/1/2）
  引用正确率     返回结果中 source 字段可验证（存在且为合法 URL）的比例

用法
----
  python 黄金检索.py                # 全量 40 题评估
  python 黄金检索.py --topk 5       # 只看前 5
  python 黄金检索.py --json
"""

import os
import re
import sys
import json
import argparse
import math
from collections import Counter

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

TOP_K = 10


def find_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "tools", "cards")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ---------------------------------------------------------------------------
# 黄金问题集（固定 40 题，覆盖 10 类任务，每类 4 题）
# 相关性判断：命中卡片 category 含期望关键词 → rel=2；title/summary 含查询核心词 → rel=1
# ---------------------------------------------------------------------------
GOLD = [
    # 去 AI 味
    {"q": "怎么把 AI 写的网文段落改得更像人写的", "cat": ["去AI味"], "core": ["去AI味"]},
    {"q": "中文文本 AI 痕迹清洗工具", "cat": ["去AI味"], "core": ["去AI味", "清洗"]},
    {"q": "去除 AI 味的大纲与正文改写提示词", "cat": ["去AI味"], "core": ["去AI味"]},
    {"q": "帮我把小说对白改成口语化工具", "cat": ["去AI味"], "core": ["口语"]},
    # 网文 / 长篇 AI 写作系统
    {"q": "长篇网文自动生成系统", "cat": ["网文"], "core": ["网文", "长篇"]},
    {"q": "小说章节大纲到正文的自动扩展工具", "cat": ["网文", "大纲"], "core": ["大纲", "正文"]},
    {"q": "中文网络小说写作辅助工具", "cat": ["网文"], "core": ["网文", "写作"]},
    {"q": "多智能体协作写小说的框架", "cat": ["网文", "多Agent"], "core": ["多Agent"]},
    # RAG
    {"q": "知识库检索增强生成框架", "cat": ["RAG"], "core": ["RAG"]},
    {"q": "本地文档问答 RAG 工具", "cat": ["RAG"], "core": ["RAG", "问答"]},
    {"q": "向量数据库检索方案", "cat": ["RAG"], "core": ["向量"]},
    {"q": "把笔记库变成可检索知识库", "cat": ["RAG", "知识库"], "core": ["知识库"]},
    # IDE / 编程助手
    {"q": "IDE 里的 AI 代码补全插件", "cat": ["IDE"], "core": ["IDE", "补全"]},
    {"q": "代码审查 AI 工具", "cat": ["IDE", "代码"], "core": ["审查"]},
    {"q": "命令行里的 AI 助手", "cat": ["IDE"], "core": ["命令行"]},
    {"q": "自动写单元测试的 AI", "cat": ["IDE", "测试"], "core": ["测试"]},
    # 大纲
    {"q": "小说大纲生成器", "cat": ["大纲"], "core": ["大纲"]},
    {"q": "章节细纲拆解工具", "cat": ["大纲"], "core": ["细纲"]},
    {"q": "网文节奏大纲模板", "cat": ["大纲", "网文"], "core": ["节奏", "大纲"]},
    {"q": "从世界观设定生成故事大纲", "cat": ["大纲"], "core": ["世界观", "大纲"]},
    # 语法 / 文本检查
    {"q": "中文语法纠错工具", "cat": ["语法"], "core": ["语法", "纠错"]},
    {"q": "文本拼写检查 AI", "cat": ["语法"], "core": ["拼写"]},
    {"q": "校对助手", "cat": ["语法"], "core": ["校对"]},
    {"q": "中文病句检测", "cat": ["语法"], "core": ["病句"]},
    # 互动叙事
    {"q": "互动小说引擎", "cat": ["互动叙事"], "core": ["互动"]},
    {"q": "文字冒险游戏生成器", "cat": ["互动叙事"], "core": ["冒险"]},
    {"q": "分支剧情可视化工具", "cat": ["互动叙事"], "core": ["分支"]},
    {"q": "沉浸式叙事 AI", "cat": ["互动叙事"], "core": ["叙事"]},
    # 短剧 / 剧本
    {"q": "短剧脚本生成器", "cat": ["短剧"], "core": ["短剧"]},
    {"q": "剧本格式转换工具", "cat": ["短剧", "剧本"], "core": ["剧本"]},
    {"q": "分镜脚本 AI", "cat": ["短剧"], "core": ["分镜"]},
    {"q": "短视频文案助手", "cat": ["短剧"], "core": ["短视频"]},
    # TTS / 语音
    {"q": "中文语音合成工具", "cat": ["TTS"], "core": ["语音", "合成"]},
    {"q": "文字转语音朗读", "cat": ["TTS"], "core": ["TTS"]},
    {"q": "AI 配音工具", "cat": ["TTS"], "core": ["配音"]},
    {"q": "情感语音生成", "cat": ["TTS"], "core": ["情感", "语音"]},
    # 人设 / 世界观
    {"q": "小说人物卡生成器", "cat": ["人设"], "core": ["人物"]},
    {"q": "世界观设定工具", "cat": ["人设"], "core": ["世界观"]},
    {"q": "角色性格分析 AI", "cat": ["人设"], "core": ["角色"]},
    {"q": "人物关系图谱工具", "cat": ["人设"], "core": ["关系图"]},
]


def load_cards(root):
    cards = []
    card_dir = os.path.join(root, "tools", "cards")
    if not os.path.isdir(card_dir):
        return cards
    for fname in sorted(os.listdir(card_dir)):
        if not fname.endswith(".md"):
            continue
        try:
            with open(os.path.join(card_dir, fname), "r", encoding="utf-8") as f:
                text = f.read(2500)
        except OSError:
            continue
        fm = {}
        if text.startswith("---"):
            end = text.find("\n---", 4)
            if end > 0:
                for line in text[4:end].split("\n"):
                    m = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
                    if m:
                        fm[m.group(1)] = m.group(2).strip().strip('"')
        cards.append({
            "file": fname,
            "title": fm.get("title", ""),
            "summary": fm.get("summary", ""),
            "tags": fm.get("tags", ""),
            "category": fm.get("category", ""),
            "source": fm.get("source", ""),
            "use_case": fm.get("use_case", ""),
        })
    return cards


def tokenize(s):
    # 简单切词：中文按字/词（2-4字窗口）+ 英文单词
    toks = []
    for m in re.finditer(r'[A-Za-z0-9_\-]+|[\u4e00-\u9fff]{2,4}', s):
        toks.append(m.group(0).lower())
    return toks


def build_index(cards):
    """词 → [(card_idx, weight)] 倒排 + 文档长度。"""
    df = Counter()
    doc_len = []
    field_w = {"title": 3.0, "summary": 1.5, "tags": 1.2, "category": 1.0,
               "use_case": 1.0}
    doc_tokens = []
    for c in cards:
        toks = []
        for f, w in field_w.items():
            for t in tokenize(c.get(f, "")):
                toks.append((t, w))
        doc_tokens.append(toks)
        doc_len.append(sum(w for _, w in toks))
        for t, _ in set(toks):
            df[t] += 1
    N = len(cards)
    index = {}
    for i, toks in enumerate(doc_tokens):
        for t, w in set(toks):
            index.setdefault(t, []).append((i, w))
    return index, df, doc_len, N


def bm25(query, index, df, doc_len, N, k1=1.5, b=0.75):
    scores = Counter()
    q_toks = set(tokenize(query))
    avg_len = sum(doc_len) / max(N, 1)
    for t in q_toks:
        if t not in index:
            continue
        n = df[t]
        idf = math.log(1 + (N - n + 0.5) / (n + 0.5))
        for i, w in index[t]:
            dl = doc_len[i]
            scores[i] += idf * w * (1 + k1) / (1 + k1 * (1 - b + b * dl / max(avg_len, 1)))
    return scores


def relevance(card, gold):
    """相关性分级：category 命中=2；title/summary 含 core 词=1。"""
    cat = card.get("category", "")
    for kw in gold["cat"]:
        if kw in cat:
            return 2
    text = card.get("title", "") + card.get("summary", "")
    for kw in gold["core"]:
        if kw in text:
            return 1
    return 0


def dcg(rels):
    return sum(rel / math.log2(i + 2) for i, rel in enumerate(rels))


def eval_gold(cards, index, df, doc_len, N):
    per_q = []
    for g in GOLD:
        scores = bm25(g["q"], index, df, doc_len, N)
        ranked = [i for i, _ in scores.most_common(TOP_K)]
        rels = [relevance(cards[i], g) for i in ranked]
        rel_count = sum(1 for r in rels if r > 0)

        # Recall@5
        recall5 = min(rel_count, 5) / 5 if rel_count else 0.0
        # MRR
        mrr = 0.0
        for i, r in enumerate(rels):
            if r > 0:
                mrr = 1.0 / (i + 1)
                break
        # nDCG@10
        ideal = sorted(rels, reverse=True)
        ndcg = dcg(rels) / dcg(ideal) if any(rels) else 0.0
        # 引用正确率：ranked 结果中 source 可验证比例
        src_ok = sum(1 for i in ranked if re.match(r'^https?://', cards[i].get("source", "")))
        cite = src_ok / len(ranked) if ranked else 0.0

        per_q.append({
            "query": g["q"],
            "recall@5": round(recall5, 3),
            "mrr": round(mrr, 3),
            "ndcg@10": round(ndcg, 3),
            "cite_acc": round(cite, 3),
            "hit_count": rel_count,
        })
    return per_q


def main():
    ap = argparse.ArgumentParser(description="黄金检索评估（TREC 式）")
    ap.add_argument("--topk", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--root", default=None)
    args = ap.parse_args()
    global TOP_K
    TOP_K = args.topk

    root = os.path.abspath(args.root) if args.root else find_root()
    cards = load_cards(root)
    if not cards:
        print("未找到工具卡", file=sys.stderr)
        sys.exit(1)
    index, df, doc_len, N = build_index(cards)
    per_q = eval_gold(cards, index, df, doc_len, N)

    agg = {k: sum(q[k] for q in per_q) / len(per_q) for k in
           ("recall@5", "mrr", "ndcg@10", "cite_acc")}

    if args.json:
        print(json.dumps({"total_questions": len(per_q), "cards": len(cards),
                          "aggregate": {k: round(v, 4) for k, v in agg.items()},
                          "per_query": per_q}, ensure_ascii=False, indent=2))
    else:
        print("=" * 72)
        print(f"黄金检索评估 · 语料 {len(cards)} 张工具卡 · 问题 {len(per_q)} 题"
              f" · top-{TOP_K}")
        print("=" * 72)
        print(f"聚合指标:")
        for k, v in agg.items():
            print(f"  {k:<12} {v:.3f}")
        print("-" * 72)
        for q in per_q:
            print(f"  [{q['recall@5']:.2f}/{q['mrr']:.2f}/{q['ndcg@10']:.2f}/{q['cite_acc']:.2f}] "
                  f"{q['query'][:34]}")
        print("=" * 72)
        print("解读：recall@5 低 = 检索覆盖面不足；mrr 低 = 相关结果排太后；"
              "cite_acc 低 = 卡片 source 缺失")


if __name__ == "__main__":
    main()
