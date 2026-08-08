---
id: tool-04854
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: oaqjp-final-project-emb-ai
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/zaihaha-tp/oaqjp-final-project-emb-ai
created: 2026-07-18
updated: 2026-07-18
no: 4854
category: 一、去 AI 味 / Humanizer 库
repo: Zaihaha-tp/oaqjp-final-project-emb-ai
stars: 0
url: https://github.com/zaihaha-tp/oaqjp-final-project-emb-ai
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
content_hash: 0c6a689fbe4745a4
  - methods/改稿润色指令库.md
---

# Zaihaha-tp/oaqjp-final-project-emb-ai

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/zaihaha-tp/oaqjp-final-project-emb-ai
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Emotion Detector web app using Watson NLP and Flask — detects anger, disgust, fear, joy, and sadness in text.
- **本地描述**：Emotion Detector web app using Watson NLP and Flask — detects anger, disgust, fear, joy, and sadness in text.
- **拉取时间**：2026-07-25 17:56:55

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Emotion Detector using Watson NLP and Flask

A Flask-based web application that uses the Watson NLP Library to detect emotions in text.

## Features

- Detects five emotions: **anger**, **disgust**, **fear**, **joy**, and **sadness**
- Identifies the **dominant emotion** in the given text
- RESTful API endpoint for emotion analysis
- Error handling for invalid or blank input

## Project Structure

```
emotion_detector_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Installation

```bash
pip install flask requests
```

## Usage

### Running the Server

```bash
python server.py
```

The application will be available at `http://localhost:5000`.

### API Endpoint

**GET** `/emotionDetector?textToAnalyze=<your text>`

### Running Unit Tests

```bash
python -m unittest test_emotion_detection.py
```

### Running PyLint

```bash
pylint server.py
```

## Technologies Used

- **Python 3**
- **Flask** — Web framework
- **Watson NLP Library** — Emotion analysis API
- **unittest** — Test framework
