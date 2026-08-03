---
id: tool-05183
type: tool
area: 库
status: active
tags: [TTS, Python, 协议未明, 本地优先, 中文友好, 本地写作]
title: ai-text-detector
summary: 小说转语音/有声书
source: https://github.com/caryyang59/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5183
category: 一、去 AI 味 / Humanizer 库
repo: CaryYang59/ai-text-detector
stars: 0
url: https://github.com/caryyang59/ai-text-detector
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# CaryYang59/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/caryyang59/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：测试仓库 For AI产品经理面试（AI测试）
- **本地描述**：测试仓库 For AI产品经理面试（AI测试）
- **拉取时间**：2026-07-25 18:09:10

---

# AI Generated Text Detector

A lightweight, **fully offline** tool to detect AI-generated text using linguistic pattern analysis. No external API or language model required.

## Features

- **Text input**: Paste any text for analysis
- **Detection dimensions**: Vocabulary diversity, sentence rhythm, AI filler phrases, passive voice, punctuation uniformity, character-level entropy
- **Confidence output**: AI probability score (0–100%) with verdict and reasoning
- **Feature highlighting**: Flags specific AI-typical phrases in the text
- **Limitations disclosure**: Honest accuracy bounds

## Quick Start

```bash
# Run web interface
python3 app.py
# Open http://localhost:8080

# CLI usage
python3 detector.py --text "Your text here"
python3 detector.py --file myfile.txt
python3 detector.py --demo   # Run 10 test cases

# JSON output
python3 detector.py --text "..." --json
```

## How It Works

### Detection Pipeline

1. **Feature Extraction** — 7 linguistic features computed from raw text
2. **Weighted Scoring** — Each feature contributes a signal; high-risk features have higher weight
3. **Sigmoid Normalization** — Raw score mapped to [0,1] probability
4. **Verdict** — Thresholds: ≥75% = AI Generated, 50–74% = Likely AI, 30–49% = Likely Human, <30% = Human

### Feature Details

| Feature | AI Signal | Rationale |
|---|---|---|
| Type-Token Ratio (TTR) | Low → AI | AI text reuses vocabulary more uniformly |
| Avg Sentence Length | High → AI | AI tends to write longer, complete sentences |
| Sentence Length Variance | Low → AI | AI has more monotone rhythm |
| Character Trigram Entropy | Low → AI | AI text is more predictable at character level |
| AI Filler Phrase Density | High → AI | "Furthermore", "notably", "seamlessly", etc. |
| Passive Voice Ratio | High → AI | AI uses passive constructions more often |
| Punctuation Uniformity | High → AI | AI text uses periods more uniformly |

### AI-Typical Keywords Flagged

`furthermore`, `moreover`, `it is worth noting`, `notably`, `significantly`, `ultimately`, `in conclusion`, `in summary`, `overall`, `tailored`, `comprehensive`, `seamlessly`, `robust`, `leverage`, `facilitate`, `optimize`, `delve`

## Test Cases (10)

| # | Label | Type | Expected |
|---|---|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 1 | 产品介绍段落 | AI | AI生成 |
| 2 | 学术摘要风格 | AI | AI生成 |
| 3 | 旅游景点描述 | AI | AI生成 |
| 4 | 商业分析报告 | AI | AI生成 |
| 5 | 健康科普文章 | AI | AI生成 |
| 6 | 个人博客随笔 | Human | 人工写作 |
| 7 | 社交媒体帖子 | Human | 人工写作 |
| 8 | 读书笔记 | Human | 人工写作 |
| 9 | 工作邮件片段 | Human | 人工写作 |
| 10 | 技术论坛回帖 | Human | 人工写作 |

Run `python3 detector.py --demo` to see live results.

## Accuracy & Limitations

- **Estimated accuracy**: 70–80% on English general text
- **Short texts (<100 words)**: Accuracy drops significantly
- **AI text with human editing**: May be missed (false negative)
- **Formal human writing** (academic papers): May trigger false positives
- **Language dependency**: Tuned for English; Chinese text needs separate calibration
- **Not a definitive verdict**: Use as one signal among many, not sole evidence

## Tech Principle

This tool uses **interpretable heuristic rules** rather than a black-box neural classifier. The advantage: you can see exactly *why* a text was flagged, and the tool works without any internet connection or API key.

The core insight: AI language models optimize for fluency and coherence, which produces statistically observable patterns — lower vocabulary variance, more formulaic transitions, higher sentence length uniformity — that differ from natural human writing.

## Files

```
detector.py     # Core detection logic + CLI
test_cases.py   # 10 labeled test cases
app.py          # Simple web UI (no dependencies beyond stdlib)
README.md       # This file
```

## Requirements

- Python 3.7+
- No external packages required (stdlib only)
