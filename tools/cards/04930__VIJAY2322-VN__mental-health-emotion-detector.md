---
id: tool-04930
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: mental-health-emotion-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/vijay2322-vn/mental-health-emotion-detector
created: 2026-07-18
updated: 2026-07-18
no: 4930
category: 一、去 AI 味 / Humanizer 库
repo: VIJAY2322-VN/mental-health-emotion-detector
stars: 0
url: https://github.com/vijay2322-vn/mental-health-emotion-detector
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
content_hash: 501be6402588dda8
  - methods/改稿润色指令库.md
---

# VIJAY2322-VN/mental-health-emotion-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/vijay2322-vn/mental-health-emotion-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Mental Health Emotion Detector is an AI-powered application that analyzes user text and predicts emotions such as happiness, sadness, anger, fear, love, or stress using Natural Language Processing (NLP) and deep learning techniques. The project is built using Python, Hugging Face Transformers, and the DistilBERT model
- **本地描述**：Mental Health Emotion Detector is an AI-powered application that analyzes user text and predicts emotions such as happiness, sadness, anger, fear, love, or stress using Natural Language Processing (NLP) and deep learning techniques. The project is built using Python, Hugging Face Transformers, and the DistilBERT model
- **拉取时间**：2026-07-25 17:59:49

---

# 🧠 Mental Health Emotion Detector

A deep learning-based application designed to detect emotions from text and provide supportive mental health context. Built with **DistilBERT**, **Hugging Face Transformers**, and **Gradio**.

## ✨ Features
- **Emotion Recognition**: Detects 6 core emotions: Sadness, Joy, Love, Anger, Fear, and Surprise.
- **Mental Health Insights**: Provides tailored advice and emotional context for each detected emotion.
- **Deep Learning Core**: Fine-tuned DistilBERT model for high accuracy and fast inference.
- **Interactive UI**: A modern, responsive Gradio interface for easy experimentation.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Virtual Environment (recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd mental-health-emotion-detector
   ```

2. Activate your virtual environment and install dependencies:
   ```bash
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

### 🏋️ Model Training
The model is fine-tuned on the `dair-ai/emotion` dataset. To re-train or fine-tune:
```bash
python src/train.py
```

### 💻 Running the App
Launch the interactive web interface:
```bash
python app.py
```

## 🛠️ Technology Stack
- **Model Architecture**: DistilBERT (`distilbert-base-uncased`)
- **Frameworks**: PyTorch, Hugging Face Transformers, Datasets
- **UI/UX**: Gradio (Soft Theme)
- **Data Analysis**: Pandas, Scikit-learn

## 📄 License
This project is open-source and intended for educational and supportive purposes.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---
*Disclaimer: This tool is not a substitute for professional medical advice, diagnosis, or treatment for the people.*
