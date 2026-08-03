---
id: tool-04852
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 需API密钥, 英文文档, 去AI味]
title: ai-news-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/adarsh123-coder/ai-news-detector
created: 2026-07-18
updated: 2026-07-18
no: 4852
category: 一、去 AI 味 / Humanizer 库
repo: adarsh123-coder/ai-news-detector
stars: 0
url: https://github.com/adarsh123-coder/ai-news-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# adarsh123-coder/ai-news-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/adarsh123-coder/ai-news-detector
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：A full-stack web application that uses the Google Gemini API to analyze news stories from text and images for authenticity.
- **本地描述**：A full-stack web application that uses the Google Gemini API to analyze news stories from text and images for authenticity.
- **拉取时间**：2026-07-25 17:56:50

---

# 📰 AI News Detector

An AI-powered web application that analyzes news articles and images to determine whether they are likely to be **Real** or **Fake** using the **Google Gemini API**. The application provides an analysis of the news, explains the reasoning, and offers counterarguments to help users evaluate the credibility of information.

---

## 🚀 Features

- 🔍 Analyze news articles using AI
- 🖼️ Support for text and image-based news
- 🤖 Powered by Google Gemini API
- 📊 Provides authenticity analysis
- 💡 Generates reasoning behind the prediction
- ⚖️ Shows possible counterarguments and alternative viewpoints
- 🌐 Simple and responsive web interface

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Node.js
- Express.js

### AI
- Google Gemini API

---

## 📂 Project Structure

```
ai-news-detector/
│
├── backend/
│   ├── server.js
│   ├── package.json
│   ├── package-lock.json
│   └── .env
│
├── public/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/adarsh123-coder/ai-news-detector.git
```

### 2. Navigate to the project

```bash
cd ai-news-detector/backend
```

### 3. Install dependencies

```bash
npm install
```

### 4. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
PORT=5001
```

### 5. Start the server

```bash
node server.js
```

Open your browser and visit:

```
http://localhost:5001
```

---

## 📸 Application Workflow

1. Enter or upload a news article.
2. Click **Analyze News**.
3. The application sends the request to the backend.
4. Google Gemini analyzes the content.
5. The result displays:
   - Authenticity assessment
   - AI explanation
   - Counterarguments
   - Additional insights

---

## 📌 Future Improvements

- ✅ Real-time fact-checking using trusted news APIs
- 🌍 Multilingual news support
- 📈 Confidence score for predictions
- 📰 News summarization
- 👤 User authentication
- 📜 Analysis history
- ☁️ Cloud deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

## 👨‍💻 Author

**Adarsh Bind**

GitHub: https://github.com/adarsh123-coder

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub!
