---
id: tool-05291
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI_Slop_Detection_Building
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/dhanikanki/ai_slop_detection_building
created: 2026-07-18
updated: 2026-07-18
no: 5291
category: 一、去 AI 味 / Humanizer 库
repo: DhaniKanki/AI_Slop_Detection_Building
stars: 0
url: https://github.com/dhanikanki/ai_slop_detection_building
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# DhaniKanki/AI_Slop_Detection_Building

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/dhanikanki/ai_slop_detection_building
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Slop Detector 🤖 — A Streamlit-based web app that detects AI-generated content using Hugging Face’s roberta-base-openai-detector model. Analyze text in real time, identify likely AI or human-written content, and view confidence scores through a clean, interactive UI.
- **本地描述**：AI Slop Detector 🤖 — A Streamlit-based web app that detects AI-generated content using Hugging Face’s roberta-base-openai-detector model. Analyze text in real time, identify likely AI or human-written content, and view confidence scores through a clean, interactive UI.
- **拉取时间**：2026-07-25 18:13:08

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Slop Detector

A simple web application to detect AI-generated content (AI Slop) using the `roberta-base-openai-detector` model.

## Features
- Detects if text is likely human-written or AI-generated.
- Built with Streamlit for a clean, interactive UI.
- Uses Hugging Face Transformers for state-of-the-art detection.

## Local Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the App**:
   ```bash
   streamlit run app.py
   ```

## Deployment Options

### 1. Streamlit Cloud (Recommended)
- Push this code to a GitHub repository.
- Connect your GitHub account to [Streamlit Cloud](https://share.streamlit.io/).
- Select your repository and `app.py` as the main file.
- Click "Deploy"!

### 2. Hugging Face Spaces
- Create a new Space on [Hugging Face](https://huggingface.co/spaces).
- Select **Streamlit** as the SDK.
- Upload `app.py` and `requirements.txt`.
- The space will automatically build and deploy your app.

### 3. Docker Deployment
A `Dockerfile` can be added for containerized deployment (e.g., to AWS, Google Cloud, or DigitalOcean).
