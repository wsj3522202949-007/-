---
id: tool-05548
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/gulkapoor/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5548
category: 一、去 AI 味 / Humanizer 库
repo: gulkapoor/AI-Text-Detector
stars: 0
url: https://github.com/gulkapoor/ai-text-detector
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
content_hash: a4e4d25e1eea9f7d
  - methods/改稿润色指令库.md
---

# gulkapoor/AI-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/gulkapoor/ai-text-detector
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：gulkapoor/AI-Text-Detector
- **拉取时间**：2026-07-25 18:22:46

---

#  AI Text Detector

A web application built with **Flask** and **Hugging Face Transformers** that analyzes text and predicts whether it is **AI-generated** or **Human-written**.

---

##  Features

- Detects AI-generated vs Human-written text
- Confidence scores for each prediction
- Interactive and responsive web interface
- Real-time text analysis
- Clean and modern UI

---

##  Tech Stack

### Backend
- Python
- Flask
- Hugging Face Transformers

### Frontend
- HTML
- CSS
- JavaScript

### Machine Learning
- Zero-Shot Classification
- `facebook/bart-large-mnli`

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/gulkapoor/AI-Text-Detector.git
```

Move into the project folder:

```bash
cd AI-Text-Detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

##  Model Used

This project uses the Hugging Face **Zero-Shot Classification** pipeline with:

- `facebook/bart-large-mnli`

The model compares the input text against the labels **"AI-generated"** and **"Human-written"** to provide a confidence score for each category.


## 👩‍💻 Author

**Gul Kapoor**

- GitHub: https://github.com/gulkapoor
