---
id: tool-05704
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/kubrick-g/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5704
category: 一、去 AI 味 / Humanizer 库
repo: kubrick-G/ai-slop-detector
stars: 0
url: https://github.com/kubrick-g/ai-slop-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 2cc8767789b63a84
  - methods/改稿润色指令库.md
---

# kubrick-G/ai-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/kubrick-g/ai-slop-detector
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：An AI-generated content detection pipeline with Flask API and web UI.
- **本地描述**：An AI-generated content detection pipeline with Flask API and web UI.
- **拉取时间**：2026-07-25 18:28:31

---

# 🛡 Slop Shield — AI Content Detector

A machine learning pipeline that detects AI-generated text and filters it from training datasets to prevent model collapse.

## What it does
- Detects AI-generated "slop" with 99.5% F1 score
- Scores text from 0–100 (clean to flagged)
- Exposes a REST API for integration
- Includes a web UI for easy testing

## How it works
The classifier uses 6 signals:
- **Perplexity** — how predictable is the text?
- **Burstiness** — sentence rhythm variation
- **Filler phrases** — AI giveaway words
- **Vocab richness** — unique word ratio
- **Avg word length** — writing complexity
- **Sentence count** — structural patterns

## Tech stack
- Python, scikit-learn, HuggingFace Transformers
- Flask REST API
- Vanilla HTML/CSS/JS frontend
- Trained on: distilgpt2, Llama 3.1 8B, Llama 3.3 70B

## Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the API
python api.py

# Open slop_detector_ui.html in browser
```

## API Usage
```bash
# Check a single text
curl -X POST http://127.0.0.1:5000/check \
  -H "Content-Type: application/json" \
  -d '{"text": "Your text here"}'

# Response
{
  "slop_score": 99.5,
  "verdict": "FLAGGED - likely AI generated",
  "details": {
    "perplexity": 19.68,
    "burstiness": 0.233,
    "filler_count": 11,
    "vocab_richness": 0.742
  }
}
```

## Results
| Class | Precision | Recall | F1 |
|---|---|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| Human (0) | 0.99 | 0.99 | 0.99 |
| AI Slop (1) | 0.99 | 0.99 | 0.99 |

**Overall F1: 0.995**

## Built by
Gokul · 2026
