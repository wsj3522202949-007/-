---
id: tool-05334
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/hasinur1997/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5334
category: 一、去 AI 味 / Humanizer 库
repo: hasinur1997/ai-text-detector
stars: 0
url: https://github.com/hasinur1997/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# hasinur1997/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/hasinur1997/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A lightweight machine learning API that classifies whether a given text is AI-generated (e.g., from ChatGPT, GPT-4, Claude, etc.) or Human-written.
- **本地描述**：A lightweight machine learning API that classifies whether a given text is AI-generated (e.g., from ChatGPT, GPT-4, Claude, etc.) or Human-written.
- **拉取时间**：2026-07-25 18:14:45

---

# 🤖 AI Text Detector

A lightweight machine learning API that classifies whether a given text is **AI-generated** (e.g., from ChatGPT, GPT-4, Claude, etc.) or **Human-written**.  

Built with Python, FastAPI, and scikit-learn, it serves predictions via a clean REST API with probabilities in percentage format (e.g., `"AI-generated: 92%"`).

---

## ✨ Features

- 🧠 **ML-based Text Classification**: Detects AI vs Human-written text
- 📊 **Probability Scoring**: Returns results like `"AI: 92%"`, `"Human: 8%"`
- ⚡ **FastAPI Backend**: Lightweight and blazing fast REST API
- 🧪 **Easy to Extend**: Swap in BERT or other models as needed
- 📁 **Modular Design**: Clean separation of training, API, and data

---

## 📁 Project Structure
ai-text-detector/
├── app/
│ └── main.py # FastAPI API definition
├── model/
│ ├── classifier.pkl # Trained ML model
│ └── train_model.py # Model training script
├── data/
│ ├── human_texts.txt # Human-written samples
│ └── ai_texts.txt # AI-generated samples
├── requirements.txt
└── README.md


related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-text-detector.git
cd ai-text-detector
```


###  Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Development Server

```commandline
uvicorn app.main:app --reload
```


### API Usage

http://127.0.0.1:8000/predict

➕ Endpoint: POST /predict

```json
{
  "text": "Sure! Here's how to create a REST API with Flask."
}
```


Response
```json
{
  "ai_generated_probability": "89%",
  "human_generated_probability": "11%"
}
```





