---
id: tool-05452
type: tool
area: 库
status: active
tags: [CSS, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/apoorwa46/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5452
category: 一、去 AI 味 / Humanizer 库
repo: apoorwa46/AI-Text-Detector
stars: 0
url: https://github.com/apoorwa46/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# apoorwa46/AI-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/apoorwa46/ai-text-detector
- **Stars**：0
- **语言**：CSS
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：apoorwa46/AI-Text-Detector
- **拉取时间**：2026-07-25 18:19:12

---

# ⚡ AI Text Detector — Detect AI vs Human-Written Text

A full-stack machine learning web application that analyzes writing patterns to determine whether a piece of text is **AI-generated** or **human-written**, along with a probability score.

## 🚀 Live Demo
🔗 https://ai-text-detector.vercel.app/ 

---

## 🧠 Features
- Classifies text as **AI-generated** or **Human-written**
- Shows **probability score** for clarity
- Fast and lightweight **Logistic Regression** model
- Beautiful **futuristic neon hacker UI**
- Real-time inference using **FastAPI**
- Deployed with **Vercel (frontend)** and **Render (backend)**

---

## 🛠️ Tech Stack

### **Machine Learning**
- Python  
- Scikit-learn  
- Logistic Regression  
- Joblib  

### **Backend**
- FastAPI  
- Uvicorn  
- Render deployment  

### **Frontend**
- HTML  
- CSS (Neon Hacker Theme)  
- JavaScript (fetch API)  
- Vercel deployment  

---

## 📂 Project Structure

ai-text-detector/
├── data/ # Training data (ignored in production)
├── models/
│ └── ai_detector.joblib # Trained model
├── src/
│ ├── app.py # FastAPI backend
│ ├── combine_data.py # Dataset merging script
│ └── train_model.py # Model training script
├── frontend/
│ ├── index.html
│ └── styles.css
├── requirements.txt
└── README.md

---

## 🔧 How It Works

1. User enters text in the UI  
2. Frontend sends a POST request to `/detect`  
3. Backend loads the ML model and predicts AI vs Human  
4. Result + probability is returned to the frontend  
5. UI displays a glowing classification panel + animations  

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🏁 Local Development

### Clone repository:
```bash
git clone https://github.com/apoorwa46/AI-Text-Detector.git
cd ai-text-detector
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run backend:
bash
Copy code
uvicorn src.app:app --reload
Open frontend:
Open frontend/index.html with Live Server or browser.

🌐 Deployment
Backend (Render)
Use:

nginx
Copy code
uvicorn src.app:app --host 0.0.0.0 --port $PORT
Frontend (Vercel)
Deploy frontend/ as root folder
Update API URL in index.html:

js
Copy code
fetch("https://your-backend.onrender.com/detect")
🤝 Contributing
Pull requests are welcome.

📬 Contact
Portfolio: https://my-portfolio-website-seven-lemon.vercel.app/
Made by Apoorwa Kumar
