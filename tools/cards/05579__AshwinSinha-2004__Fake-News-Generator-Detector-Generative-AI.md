---
id: tool-05579
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: Fake-News-Generator-Detector-Generative-AI
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ashwinsinha-2004/fake-news-generator-detector-generative-ai
created: 2026-07-18
updated: 2026-07-18
no: 5579
category: 一、去 AI 味 / Humanizer 库
repo: AshwinSinha-2004/Fake-News-Generator-Detector-Generative-AI
stars: 1
url: https://github.com/ashwinsinha-2004/fake-news-generator-detector-generative-ai
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: b87d62c754135b35
  - methods/改稿润色指令库.md
---

# AshwinSinha-2004/Fake-News-Generator-Detector-Generative-AI

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ashwinsinha-2004/fake-news-generator-detector-generative-ai
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：The project builds a Generative-AI system that generates fake news headlines using GPT-2 and detects them using a text classification model like BERT. It demonstrates both the power and ethical responsibility of generative AI in combating misinformation.
- **本地描述**：The project builds a Generative-AI system that generates fake news headlines using GPT-2 and detects them using a text classification model like BERT. It demonstrates both the power and ethical responsibility of generative AI in combating misinformation.
- **拉取时间**：2026-07-25 18:23:55

---

# 📰 Fake News Generator & Detector Generative AI

The project builds a Generative-AI system that generates fake news headlines using GPT-2 and detects them using a text classification model like BERT.
A demonstration system showcasing both the creative power and ethical responsibility of generative AI. 

This project:
- **Generates** plausible “fake” news headlines by fine‑tuning GPT‑2.
- **Detects** real versus fake headlines using a BERT‑based classifier.
- Provides a simple command‑line or Colab interface for experimentation.

---

## 🚀 Features

- **GPT‑2 Headline Generator**  
  • Fine‑tune on real news headlines  
  • Sample new, synthetic headlines  
- **BERT Detector**  
  • Binary classification (REAL vs. FAKE)  
  • Train on balanced True_News.csv and Fake_News.csv  
- **Easy Experimentation**  
  • Run locally or in Google Colab  
  • Script handles data loading, training, and inference  

---

## 📋 Requirements

- Python 3.8+  
- `transformers`  
- `torch`  
- `scikit-learn`  
- `pandas`  
- `numpy`  
- `nltk`  
- `gradio`  

---

## 🔧 Installation (Local)

1. **Clone the repository**  
   ```bash
   git clone https://github.com/https:/AshwinSinha-2004/Fake-News-AI.git
   cd Fake-News-AI

2. **Create and activate a virtual environment**
    python3 -m venv venv
    source venv/bin/activate

3. **Install dependencies**
    pip install -r requirements.txt

---

## ☁️ Running in Google Colab

1. Upload True_News.csv and Fake_News.csv to your Colab session.

2. **In a notebook cell, install packages:**
    !pip install -r requirements.txt

3. **Execute the main script:**
    !python Fake_News_Generator_&_Detector_Using_Generative_AI_&_NLP.py

4. Follow the on‑screen prompts or Gradio link.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🚀 Live Demo

Try the Fake News Detector in your browser:  
👉 [https://b609ba1d78fa3a310d.gradio.live](https://b609ba1d78fa3a310d.gradio.live)

⚠️ Note: This is a temporary link hosted via Gradio on Google Colab. It may expire after a few days.
⚠️ Note: Due to hardware constraints, the model was trained on a reduced dataset, which may affect accuracy. For better results, retrain using the full dataset on a GPU/TPU-enabled environment.

