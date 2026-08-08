---
id: tool-00645
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI_Hub_Website
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/divijmodi/ai_hub_website
created: 2026-07-18
updated: 2026-07-18
no: 645
category: 二、网文 / 长篇 AI 写作系统 库
repo: divijmodi/AI_Hub_Website
stars: 1
url: https://github.com/divijmodi/ai_hub_website
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: f5931e5b5369f64b
  - methods/最强写作方法论_全球最强综合版.md
---

# divijmodi/AI_Hub_Website

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/divijmodi/ai_hub_website
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：ai, ai-interviewer, gemini-api, genrative-ai, llm, local-ai, nextjs, ocr, ollama, portfolio-project, react
- **GitHub 描述**：A local-first Personal AI Hub with tools like a Story Improver, Caption Generator, and an AI Mock Interviewer powered by Ollama and Gemini.
- **本地描述**：A local-first Personal AI Hub with tools like a Story Improver, Caption Generator, and an AI Mock Interviewer powered by Ollama and Gemini.
- **拉取时间**：2026-07-23 22:57:53

---

# 🌐 Personal AI Hub

Welcome to the **Personal AI Hub**, a powerful, local-first web application that integrates multiple AI-powered tools into a unified, user-friendly platform.  
This hub runs entirely on your local machine, ensuring your data remains private and secure.

---

## ✨ Features

This application combines several AI tools into one seamless experience:

- **✍️ Story Improver & Generator** → Paste your text to get suggestions on grammar, flow, and pacing, or let the AI continue your story.
- **🖼️ Caption Generator** → Upload an image to generate short, catchy captions suitable for social media.
- **🎙️ AI Mock Interviewer** → A flagship feature that provides a personalized interview experience based on your resume:
  - **Resume Processing**: Upload your resume (PDF/Image) to automatically extract your skills using OCR.
  - **Customized Interviews**: Select the skills and interview type (HR, Technical, System Design) you want to practice.
  - **Live Feedback**: Receive instant, AI-powered feedback on every answer you give.
  - **Performance Report**: Get a detailed scorecard at the end with your strengths, weaknesses, and areas for improvement.
- **📊 Productivity Dashboard** → Track your activity, including stories improved, captions generated, and interviews completed.

---

## 🖥️ Tech Stack

- **Frontend**: Next.js, React, TailwindCSS  
- **Local AI Engine**: Ollama  
- **Interview AI**: Google Gemini Flash API  
- **Resume Parsing (OCR)**: Tesseract.js  
- **Database**: MongoDB  

---

## 🚀 Getting Started

Follow these steps to get the project running on your local machine.

### 1. Prerequisites
Make sure you have the following software installed on your system:

- Node.js: Version 18.x or higher  
- Ollama: Installed and running (required for Story Improver & Caption Generator)  

### 2. Start the Ollama Server

Before pulling models or running the app, you need to start the Ollama service.

- **macOS & Windows** → Run the Ollama application (it runs in the background).  
- **Linux** → Open your terminal and run:  

```bash
ollama serve
```

> Leave this running in a separate terminal window.

### 3. Install Required Ollama Models

With the Ollama server running, pull the necessary models:

```bash
# For the Story Improver and text-based tasks
ollama pull tinyllama

# For the Image Caption Generator
ollama pull llava:latest
```

Verify installation:  

```bash
ollama list
```

### 4. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-project-directory>
```

### 5. Install Dependencies

```bash
npm install
```

### 6. Set Up Environment Variables

Create `.env.local` in your project root and configure your credentials:  

```env
# MongoDB Connection String
MONGO_URL="your_mongodb_connection_string_here"
DB_NAME="ai_hub"

# Google Gemini API Key (for the Interview feature)
GEMINI_API_KEY="your_google_gemini_api_key_here"
```

### 7. Run the Application

```bash
npm run dev
```

Open the app: **http://localhost:3000** 🎉

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 💡 Performance Note
When you use a feature for the first time in a session, the local AI model needs to be loaded into your computer's memory (RAM/VRAM). This initial request might take a bit longer. Subsequent requests for that feature will be much faster as the model will already be loaded and ready.

## 📄 License

MIT License © 2025  
