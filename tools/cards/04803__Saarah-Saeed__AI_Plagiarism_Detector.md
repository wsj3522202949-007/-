---
id: tool-04803
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI_Plagiarism_Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/saarah-saeed/ai_plagiarism_detector
created: 2026-07-18
updated: 2026-07-18
no: 4803
category: 一、去 AI 味 / Humanizer 库
repo: Saarah-Saeed/AI_Plagiarism_Detector
stars: 0
url: https://github.com/saarah-saeed/ai_plagiarism_detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Saarah-Saeed/AI_Plagiarism_Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/saarah-saeed/ai_plagiarism_detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**： AI-powered plagiarism detection system to identify semantic similarities beyond exact text matching through stylometric analysis, and TF-IDF keyword matching, along with a Streamlit-based interactive web interface .
- **本地描述**：AI-powered plagiarism detection system to identify semantic similarities beyond exact text matching through stylometric analysis, and TF-IDF keyword matching, along with a Streamlit-based interactive web interface .
- **拉取时间**：2026-07-25 17:54:53

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# 🔬 PlagioScan AI

An AI-powered plagiarism detection system that goes beyond exact text matching by combining **Semantic Analysis**, **Stylometric Analysis**, and **TF-IDF Keyword Matching**.

## 🚀 Features

* Semantic similarity detection using Sentence Transformers
* Stylometric analysis to compare writing styles
* TF-IDF based keyword similarity scoring
* Single Text Analysis mode
* Compare Two Texts mode
* Multiple input methods:

  * Text Input
  * File Upload (.txt, .pdf, .docx)
  * URL-based text extraction
* Interactive Streamlit web interface
* Real-time plagiarism risk assessment

## 🛠️ Tech Stack

* Python
* Streamlit
* Sentence Transformers (all-MiniLM-L6-v2)
* Scikit-learn
* NLTK
* NumPy
* BeautifulSoup4
* PyPDF2
* python-docx

## 📊 Detection Pipeline

1. Input collection (Text, File, or URL)
2. Text preprocessing and sentence tokenization
3. Semantic embedding generation using Sentence Transformers
4. Cosine similarity calculation
5. Stylometric feature extraction
6. TF-IDF keyword similarity analysis
7. Risk classification (Safe, Moderate, High Risk)
8. Interactive result visualization

## 🎯 Plagiarism Risk Levels

* 🟢 Safe
* 🟡 Moderate
* 🔴 High Risk
