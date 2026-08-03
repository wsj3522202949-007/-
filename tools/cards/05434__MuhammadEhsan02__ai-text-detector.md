---
id: tool-05434
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/muhammadehsan02/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5434
category: 一、去 AI 味 / Humanizer 库
repo: MuhammadEhsan02/ai-text-detector
stars: 0
url: https://github.com/muhammadehsan02/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# MuhammadEhsan02/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/muhammadehsan02/ai-text-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：MuhammadEhsan02/ai-text-detector
- **拉取时间**：2026-07-25 18:18:30

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detector

Flask web app for detecting whether text is Human-Written or AI-Generated.

The project compares:
- Classical NLP model: TF-IDF with Linear SVM
- Transformer model: RoBERTa

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## API

```text
POST /predict
```

Input:

```json
{"text": "sample text here"}
```

## Main Files

- `app.py`
- `templates/`
- `static/`
- `artifacts/`
- `notebook/`
- `requirements.txt`
