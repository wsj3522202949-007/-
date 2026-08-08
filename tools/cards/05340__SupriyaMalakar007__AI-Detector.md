---
id: tool-05340
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/supriyamalakar007/ai-detector
created: 2026-07-18
updated: 2026-07-18
no: 5340
category: 一、去 AI 味 / Humanizer 库
repo: SupriyaMalakar007/AI-Detector
stars: 1
url: https://github.com/supriyamalakar007/ai-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 0c164c54ad56a3b9
  - methods/改稿润色指令库.md
---

# SupriyaMalakar007/AI-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/supriyamalakar007/ai-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：An AI-powered text detection system that analyzes and classifies content as human-written or AI-generated using Machine Learning and NLP techniques.
- **本地描述**：An AI-powered text detection system that analyzes and classifies content as human-written or AI-generated using Machine Learning and NLP techniques.
- **拉取时间**：2026-07-25 18:14:57

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI-Detector

# Description

AI-Detector is a Machine Learning and NLP-based project that detects whether a text is AI-generated or human-written. The system uses TF-IDF vectorization and Logistic Regression to analyze writing patterns and classify the content with confidence scores.

# The project also supports:

Manual text input
PDF file analysis
Image text extraction using OCR
# 🚀 Features
Detect AI-generated content
Human vs AI text classification
PDF text detection
Image text extraction using Tesseract OCR
Confidence score prediction
Command-line interactive interface
# 🛠 Technologies Used
Python
Scikit-learn
Pandas
NumPy
Joblib
PDFPlumber
PyTesseract
Pillow (PIL)
# ⚙️ Machine Learning Model

This project uses:

TF-IDF Vectorizer for feature extraction
Logistic Regression for text classification
# 📂 Dataset

The dataset contains:

Human-written text samples
AI-generated text samples

The model is trained to classify the input text into:

Human Written 👨
AI Generated 🤖
# 📊 Workflow
Load Dataset
Preprocess Text
Train ML Model
Predict Input Text
Display Result with Confidence Score
