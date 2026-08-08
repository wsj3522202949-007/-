---
id: tool-04875
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: fake-news-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/khansawaheed7/fake-news-detector
created: 2026-07-18
updated: 2026-07-18
no: 4875
category: 一、去 AI 味 / Humanizer 库
repo: KhansaWaheed7/fake-news-detector
stars: 0
url: https://github.com/khansawaheed7/fake-news-detector
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
content_hash: f7965c4164ce10b7
  - methods/改稿润色指令库.md
---

# KhansaWaheed7/fake-news-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/khansawaheed7/fake-news-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Verify AI, Fake News Detector An AI-powered web application that classifies news articles as Real or Fake using Machine Learning and Natural Language Processing (NLP). The system analyzes article text, extracts features, and predicts credibility through an interactive web interface.
- **本地描述**：Verify AI, Fake News Detector An AI-powered web application that classifies news articles as Real or Fake using Machine Learning and Natural Language Processing (NLP). The system analyzes article text, extracts features, and predicts credibility through an interactive web interface.
- **拉取时间**：2026-07-25 17:57:43

---

# VerifyAI 

> *Don't share before you verify.*

**Team:** Khansa Waheed (230982) · Momna Nawaz (23081) · Areeba Jilani (230904)  
**Course:** Artificial Intelligence  
**Deadline:** June 01, 2026

---

## Quick Start (Run Locally)

**Step 1 — Backend**
```bash
cd backend
pip install -r requirements.txt
python app.py
# Backend runs at http://localhost:5000
```

**Step 2 — Frontend**
```bash
# Simply open frontend/index.html in your browser
# OR serve it:
cd frontend
python -m http.server 3000
# Open http://localhost:3000
```

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Project Structure
```
fakenews-detector/
├── frontend/
│   └── index.html          # Complete 5-page React-style SPA
├── backend/
│   ├── app.py              # Flask REST API
│   └── requirements.txt
├── notebooks/
│   └── model_training.ipynb  # EDA + Model training
├── report/                 # Project report (PDF)
├── demo/                   # Video demo link
└── README.md
```

## Features
- NLP text classifier 
- Highlighted suspicious phrases (clickbait / hedging / emotional)
- Credibility score dial (0–100)
- Fact-check cross-reference 
- Web presence timeline
- Dashboard with charts and history
- Model analytics page

