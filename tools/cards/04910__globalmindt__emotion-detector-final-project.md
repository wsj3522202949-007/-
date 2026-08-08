---
id: tool-04910
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: emotion-detector-final-project
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/globalmindt/emotion-detector-final-project
created: 2026-07-18
updated: 2026-07-18
no: 4910
category: 一、去 AI 味 / Humanizer 库
repo: globalmindt/emotion-detector-final-project
stars: 0
url: https://github.com/globalmindt/emotion-detector-final-project
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
content_hash: 49eda9f8131cca47
  - methods/改稿润色指令库.md
---

# globalmindt/emotion-detector-final-project

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/globalmindt/emotion-detector-final-project
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered Emotion Detector web application built with Python, Flask, and Watson NLP. This project analyzes user-provided text and identifies emotions such as joy, sadness, anger, fear, and disgust.
- **本地描述**：AI-powered Emotion Detector web application built with Python, Flask, and Watson NLP. This project analyzes user-provided text and identifies emotions such as joy, sadness, anger, fear, and disgust.
- **拉取时间**：2026-07-25 17:59:01

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Emotion Detector Final Project

AI-powered web application built with Python, Flask, and Watson NLP. It
analyzes English text and reports scores for anger, disgust, fear, joy, and
sadness, along with the dominant emotion.

## Run the project

```bash
python3.11 -m pip install flask requests pylint
python3.11 test_emotion_detection.py
python3.11 server.py
```

Open `http://127.0.0.1:5000` in a browser.

## Rubric screenshots

1. For `6b_deployment_test.png`, start the server, open the home page, enter
   `I am glad this happened`, click **Analyze emotion**, and capture the page
   showing the formatted result.
2. For `7c_error_handling_interface.png`, erase the text (or enter spaces),
   click **Analyze emotion**, and capture the
   `Invalid input! Please enter some text to analyze.` message.

## Watson lab endpoint availability

The application uses the IBM Skills Network endpoint required by the rubric.
If that temporary lab endpoint is unavailable, the application returns the
specified invalid-text response instead of crashing. Unit tests simulate
valid Watson responses so they remain deterministic and do not depend on an
external lab service.
