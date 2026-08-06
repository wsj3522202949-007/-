---
id: tool-04952
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: spam-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/roshnyjohnson/spam-detector
created: 2026-07-18
updated: 2026-07-18
no: 4952
category: 一、去 AI 味 / Humanizer 库
repo: roshnyjohnson/spam-detector
stars: 0
url: https://github.com/roshnyjohnson/spam-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# roshnyjohnson/spam-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/roshnyjohnson/spam-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered spam detection app that analyzes text content and predicts whether it is reliable or suspicious.
- **本地描述**：AI-powered spam detection app that analyzes text content and predicts whether it is reliable or suspicious.
- **拉取时间**：2026-07-25 18:00:41

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---



# MailPal — Spam Detector with Explainable AI
 
A web app that detects spam messages using machine learning, and
explains its decision by highlighting which words influenced the result.
 
## Live Demo
Frontend:https://spam-detector-red-five.vercel.app/

Backend:https://spam-detector-u6hc.onrender.com/
 
## Screenshots
![alt text](https://github.com/roshnyjohnson/spam-detector/blob/main/notebook/class_distribution.png)


![alt text](https://github.com/roshnyjohnson/spam-detector/blob/main/notebook/confusion_matrix.png)

![alt text](https://github.com/roshnyjohnson/spam-detector/blob/main/notebook/top_spam_words.png)


## Tech Stack
- Frontend: React (Vite)
- Backend: FastAPI
- ML: scikit-learn (TF-IDF + Logistic Regression)
- Dataset: SMS Spam Collection
 
## How It Works
1. Messages are vectorized using TF-IDF
2. A Logistic Regression model predicts spam/ham
3. Word-level coefficients are used to explain which words
   influenced each specific prediction
 
## Results
- Accuracy: 97.3%
- F1-score (spam class): ~93%
 
## Running Locally
### Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
 
### Frontend
cd spam-detector-app
npm install
npm run dev
