---
id: tool-05177
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Toxic-Comment-Detector-Updated
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sarkar24/toxic-comment-detector-updated
created: 2026-07-18
updated: 2026-07-18
no: 5177
category: 一、去 AI 味 / Humanizer 库
repo: sarkar24/Toxic-Comment-Detector-Updated
stars: 4
url: https://github.com/sarkar24/toxic-comment-detector-updated
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# sarkar24/Toxic-Comment-Detector-Updated

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sarkar24/toxic-comment-detector-updated
- **Stars**：4
- **语言**：HTML
- **License**：None
- **Topics**：app, extension, toxic-comment-classification, toxicity, web, webapp, webapplication
- **GitHub 描述**：The Toxic Comment Detection System is an AI-powered web application that identifies toxic and hate speech in real-time. It uses a fine-tuned BERT model to predict the toxicity of user-input text and displays results instantly. The system also includes a Chrome Extension that blurs out toxic comments on social media platforms such as YouTube.
- **本地描述**：The Toxic Comment Detection System is an AI-powered web application that identifies toxic and hate speech in real-time. It uses a fine-tuned BERT model to predict the toxicity of user-input text and displays results instantly. The system also includes a Chrome Extension that blurs out toxic comments on social media platforms such as YouTube.
- **拉取时间**：2026-07-25 18:08:56

---

# 🧠 Toxic Comment Detection System

<a href="https://toxic-comment-detector-updated.onrender.com" target="_blank">
  <img src="https://img.shields.io/badge/Live%20Demo-Visit-green?style=for-the-badge&logo=google-chrome" />
</a>
<a href="https://www.python.org/" target="_blank">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
</a>
<a href="https://flask.palletsprojects.com/" target="_blank">
  <img src="https://img.shields.io/badge/Backend-Flask-orange?style=for-the-badge&logo=flask" />
</a>
<a href="https://huggingface.co/sarkararnab/toxic_bert_model" target="_blank">
  <img src="https://img.shields.io/badge/ML-BERT-yellow?style=for-the-badge&logo=huggingface" />
</a>

---

## 🔍 Overview
The **Toxic Comment Detection System** is an **AI-powered tool** that identifies **toxic and hate comments** in real time.  
It consists of:

- 🌐 **Web App** for checking individual comments  
- 🧩 **Chrome Extension** that **blurs toxic comments** on YouTube & Instagram  
- 🤖 **Custom BERT model** fine-tuned for English toxic comment detection

---

## 🚀 Live Demo & Downloads

### 🌐 **Try the Web App:**  
🔗 <a href="https://toxic-comment-detector-updated.onrender.com" target="_blank" rel="noopener noreferrer">Toxic Comment Detector Live</a>

### ▶️ **Complete Walkthrough (Youtube):**  
🔗 <a href="https://www.youtube.com/watch?v=wv8dsj2tdGo" target="_blank" rel="noopener noreferrer">Check out this video</a>

### 💻 **Download Chrome Extension ZIP:**  
🔗 <a href="https://drive.google.com/file/d/1tlcMZA7iFqsEo9a8n_oIAsJvzbtq2OAp/view?usp=drive_link" target="_blank" rel="noopener noreferrer">Download Extension</a>

🎥 **Chrome Extension Setup Tutorial (YouTube):**  
🔗 <a href="https://www.youtube.com/watch?v=MnTMe5dBzf8" target="_blank" rel="noopener noreferrer">How to Install & Use the Extension</a>

---

## 🧩 How to Use the Chrome Extension Locally

1. **Download** and **unzip** the extension file.  
2. Open **Chrome** → go to `chrome://extensions/`.  
3. Enable **Developer Mode** (top-right).  
4. Click **Load Unpacked** and select the **unzipped folder**.  
5. Visit **YouTube or Instagram** → Toxic comments will be **blurred automatically**.  
6. Click **Show** to reveal hidden comments if needed.

---

## 🌟 Key Highlights
- ✅ **Real-time** detection of toxic & hate comments  
- ⚡ **Fine-tuned BERT model** hosted via Flask backend  
- 🖥️ **Sleek and responsive UI** with probability scores  
- 🔒 **Chrome Extension** automatically blurs toxic comments on social media  
- 🌍 **Live & publicly accessible** via Render deployment  

---

## 🖼️ Screenshots

### 🌐 Web App
![Web App Screenshot](https://github.com/sarkar24/Toxic-Comment-Detector-Updated/blob/main/images/web-ui.jpg)

### 🧩 Chrome Extension in Action
![Web App Screenshot](https://github.com/sarkar24/Toxic-Comment-Detector-Updated/blob/main/images/extension-demo.jpg)

---

## 🛠️ Tech Stack

| Layer             | Technology                                 |
|-------------------|--------------------------------------------|
| **Frontend**      | React.js, TailwindCSS, HTML                |
| **Backend**       | Flask (Python)                             |
| **ML Model**      | fine-tunned BERT (`transformers`)          |
| **Browser Ext.**  | JavaScript, Manifest v3                    |
| **Deployment**    | Render (Flask app), Hugging Face (Model)   |

---

## 📖 Usage Guide

### 🌍 Web App
1. Enter any text or comment in the input box.
2. Click **"Check Toxicity"**.
3. Instantly see **prediction** (Toxic / Not Toxic) and **confidence score**.

### 🧩 Extension
- Visit YouTube or Instagram.
- Toxic comments will be blurred automatically.
- You can also unhide the blurred comment on your wish.

---

## 📚 Acknowledgments
- 🤗 **Hugging Face** for BERT model & transformers library  
- 🐍 **Flask** for serving ML model as API  
- ⚛️ **React.js & TailwindCSS** for the responsive frontend  
- 🌐 **Google Chrome** for extension support  

---

## ⭐ Pro Tip
> Blurring toxic comments while browsing makes the internet **a calmer place**.  
> Give it a try and enjoy **clean social media feeds**! ✨

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

### 🏆 Star this repo if you like it!  
It helps more people discover this project 🚀

