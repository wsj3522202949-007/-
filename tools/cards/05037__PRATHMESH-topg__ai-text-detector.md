---
id: tool-05037
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/prathmesh-topg/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5037
category: 一、去 AI 味 / Humanizer 库
repo: PRATHMESH-topg/ai-text-detector
stars: 0
url: https://github.com/prathmesh-topg/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# PRATHMESH-topg/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/prathmesh-topg/ai-text-detector
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：PRATHMESH-topg/ai-text-detector
- **拉取时间**：2026-07-25 18:03:47

---

# 🧠 AI-Generated Content Detection System

This project is an **end-to-end machine learning system** that detects whether a given text is **AI-generated** or **human-written**.  
It combines a **FastAPI backend** (for ML model inference) with a **React + Material UI frontend** (for user interaction).  

---

## 📌 Features
- 🔍 **AI vs Human Text Detection** using an ML model trained on labeled datasets.  
- ⚡ **FastAPI Backend** serving predictions via a REST API.  
- 🎨 **React Frontend** with a modern dark theme built using **Material UI**.  
- 🖼️ **Attractive UI** with text input box, real-time prediction, and result highlighting.  
- 📂 Modular project structure for backend and frontend.  

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---



## ⚙️ Tech Stack
- **Backend:** FastAPI, Scikit-learn, Pandas, Joblib, Uvicorn  
- **Frontend:** React, Material UI, JavaScript, HTML, CSS  
- **Version Control:** Git & GitHub

📊 Dataset

human_data.csv → contains human-written sentences/essays/articles.

ai_data.csv → contains AI-generated text (from models like ChatGPT).

Both datasets are combined into data.csv for training.

🖼️ Frontend Preview

Dark theme UI with header "CONTENT DETECTION"

Transparent text box for user input

"Send" button triggers backend API and displays result (AI or Human)

Result is color-coded:

🟥 Red → AI-Generated

🟩 Green → Human-Written
