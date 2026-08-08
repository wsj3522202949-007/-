---
id: tool-04947
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Ai-Emotion-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/yashil2007/ai-emotion-detector
created: 2026-07-18
updated: 2026-07-18
no: 4947
category: 一、去 AI 味 / Humanizer 库
repo: Yashil2007/Ai-Emotion-Detector
stars: 0
url: https://github.com/yashil2007/ai-emotion-detector
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
content_hash: 139dca2875e351ec
  - methods/改稿润色指令库.md
---

# Yashil2007/Ai-Emotion-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/yashil2007/ai-emotion-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Developed a responsive Flask-based AI Emotion Detector that dynamically processes text inputs and scores emotional tone out of 20 using local keyword-parsing algorithms
- **本地描述**：Developed a responsive Flask-based AI Emotion Detector that dynamically processes text inputs and scores emotional tone out of 20 using local keyword-parsing algorithms
- **拉取时间**：2026-07-25 18:00:29

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Final Project: AI Emotion Detector

## Features

- Detects emotions from text input
- Identifies the dominant emotion
- Supports:
  - Joy
  - Anger
  - Sadness
  - Fear
  - Disgust
- Real-time web interface using Flask
- Error handling for empty input
- Unit testing support
- Clean project structure

## Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- Git
- GitHub

## Emotion Detection Logic

The application uses a keyword-based scoring mechanism.

Each emotion category contains a predefined set of keywords:

- Joy
- Anger
- Sadness
- Fear
- Disgust

When a keyword is found in the user input, the corresponding emotion score increases.

The emotion with the highest score is selected as the dominant emotion.

## Example

### Input

```text
I am very happy and excited today
```

### Output

python
    "joy": 14.0,
    "anger": 2.0,
    "sadness": 2.0,
    "fear": 2.0,
    "disgust": 2.0,
    "dominant_emotion": "joy"

## Installation

### Clone Repository

```bash
git clone https://github.com/Yashil2007/Ai-Emotion-Detector.git
```
### Move Into Project Directory

```bash
cd Ai-Emotion-Detector
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

## Running Tests

```bash
python -m unittest discover tests
```

## Author

Yashil Pandya
