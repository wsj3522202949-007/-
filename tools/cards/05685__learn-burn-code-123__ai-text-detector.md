---
id: tool-05685
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/learn-burn-code-123/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5685
category: 一、去 AI 味 / Humanizer 库
repo: learn-burn-code-123/ai-text-detector
stars: 0
url: https://github.com/learn-burn-code-123/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# learn-burn-code-123/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/learn-burn-code-123/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI text detector app
- **本地描述**：AI text detector app
- **拉取时间**：2026-07-25 18:27:50

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detector

A web application that helps users identify AI-generated content in their text and provides suggestions to make the text appear more human-written. This application is designed to be globally accessible, including from regions with internet restrictions such as China and Hong Kong.

**Live Demo:** [https://ai-text-detector.onrender.com](https://ai-text-detector.onrender.com)

## Features

- Analyze text input (up to 800 words)
- Highlight AI-written passages in yellow
- Provide suggestions to make text appear more human-written
- Simple and intuitive user interface
- Globally accessible with no external API dependencies
- Fast startup with background model loading

## Technologies

- Python/Flask backend
- HTML/CSS/JavaScript frontend
- Custom TF-IDF and Random Forest model for AI text detection
- Scikit-learn for machine learning capabilities
- NLTK for natural language processing

## Setup

### Local Development

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Open your browser and navigate to `http://localhost:5001`

### Deployment to Render

1. Fork or clone this repository to your GitHub account
2. Log in to [Render](https://render.com)
3. Click on "New Web Service"
4. Connect your GitHub repository
5. Use the following settings:
   - Name: ai-text-detector (or your preferred name)
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Click "Create Web Service"
7. Your application will be deployed and available at the URL provided by Render

## Global Accessibility

This application is designed to work worldwide without relying on external APIs that might be restricted in certain regions. Instead of using pre-trained models that require downloading from external sources, it uses a custom-built TF-IDF and Random Forest model that trains locally using scikit-learn.

## How It Works

1. When first analyzing text, the application uses a simulated detection method while training a custom model in the background
2. The custom model uses TF-IDF vectorization and a Random Forest classifier to identify patterns common in AI-written text
3. Once the model is trained, it's saved locally for future use
4. The application provides real-time feedback on whether text appears to be AI-generated
5. For each flagged passage, it offers specific suggestions to make the text appear more human-written
