---
id: tool-04827
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: emotion-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sebes12345/emotion-detector
created: 2026-07-18
updated: 2026-07-18
no: 4827
category: 一、去 AI 味 / Humanizer 库
repo: Sebes12345/emotion-detector
stars: 0
url: https://github.com/sebes12345/emotion-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Sebes12345/emotion-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sebes12345/emotion-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：An AI-powered web app that detects emotions from text using HuggingFace Transformers and Streamlit.
- **本地描述**：An AI-powered web app that detects emotions from text using HuggingFace Transformers and Streamlit.
- **拉取时间**：2026-07-25 17:55:52

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# 🎭 Emotion Detector

A simple AI-powered web app that detects emotions from text using a pretrained NLP model.

## What it does
- User types any sentence
- App predicts the emotion (joy, sadness, anger, fear, surprise, disgust, neutral)
- Shows confidence score for each emotion

## Tech Stack
- Python
- Streamlit (UI)
- HuggingFace Transformers (NLP model)
- PyTorch

## Model Used
`j-hartmann/emotion-english-distilroberta-base` from HuggingFace

## How to Run

1. Clone the repo
```
git clone https://github.com/yourusername/emotion-detector.git
cd emotion-detector
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Run the app
```
streamlit run app.py
```

4. Open browser at http://localhost:8501
