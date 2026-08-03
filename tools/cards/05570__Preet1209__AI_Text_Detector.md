---
id: tool-05570
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI_Text_Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/preet1209/ai_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5570
category: 一、去 AI 味 / Humanizer 库
repo: Preet1209/AI_Text_Detector
stars: 0
url: https://github.com/preet1209/ai_text_detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Preet1209/AI_Text_Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/preet1209/ai_text_detector
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI powered text detector with a C and Python interface. Top 5 RVCE C Programming Hackathon.
- **本地描述**：AI powered text detector with a C and Python interface. Top 5 RVCE C Programming Hackathon.
- **拉取时间**：2026-07-25 18:23:35

---

# Logic2Impact - AI Content Detection System

## Overview
Logic2Impact is a lightweight AI content detection system built using C and Python integration. It analyzes text using multiple linguistic signals and calculates an AI probability score to classify text.

## Features
- AI vs Human text classification
- Multi-signal detection engine
- PDF report generation
- Web interface for file upload
- Weighted scoring model

## Detection Signals

### Signal 1: Sentence Length Variance
Low sentence variance may indicate AI-generated content.

### Signal 2: Type Token Ratio (TTR)
Measures vocabulary diversity.

```text
TTR = Unique Words / Total Words
```

### Signal 3: Filler Word Detection
Detects words like:
- furthermore
- moreover
- additionally

## Scoring Model

```text
Final Score =
(0.40 × S1) +
(0.30 × S2) +
(0.30 × S3)

AI Probability = Score × 100
```

## Classification

| Score | Result |
|------|---related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| >70% | Likely AI Generated |
| 40–70% | Uncertain |
| <40% | Likely Human Written |

## Tech Stack
- C
- Python
- Flask
- HTML/CSS/JavaScript

## Run Locally

```bash
pip install flask
python app.py
```

## Project Structure

```text
Logic2Impact/
├── app.py
├── main.c
├── detector.h
├── templates/
├── static/
└── uploads/
```

## Limitations
- Rule-based approach
- English text focused
- Not 100% accurate

## Contributors
Logic2Impact Project Team
