---
id: tool-00257
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI-Story-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/shagufta28/ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 257
category: 二、网文 / 长篇 AI 写作系统 库
repo: shagufta28/AI-Story-Generator
stars: 1
url: https://github.com/shagufta28/ai-story-generator
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
content_hash: bde0d232be5241da
  - methods/最强写作方法论_全球最强综合版.md
---

# shagufta28/AI-Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/shagufta28/ai-story-generator
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：shagufta28/AI-Story-Generator
- **拉取时间**：2026-07-23 22:46:35

---

# 🧠 AI Story Generator

An AI-powered storytelling web application built with the **MERN stack** (MongoDB, Express, React, Node.js), integrated with a **free GPT API** to generate creative stories based on user input.

---

## 🚀 Features

- ✍️ Generate short stories using AI based on user prompt and selected genre
- 🔐 Secure authentication using JWT
- 🗂 Save and retrieve stories by logged-in users
- ❌ Delete stories
- 🌍 Free and open-source AI integration (ChatAnywhere GPT API)

---

## 🛠 Tech Stack

**Frontend:** React  
**Backend:** Node.js, Express  
**Database:** MongoDB Atlas  
**Auth:** JWT (JSON Web Tokens)  
**AI Model:** Free GPT API ([ChatAnywhere GPT Proxy](https://github.com/chatanywhere/GPT_API_free))  

---

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## ⚙️ Installation & Setup

### 1. Clone the Repo
git clone https://github.com/yourusername/AI-Story-Generator.git
cd AI-Story-Generator

### 2. Setup Backend
cd backend
npm install

### Create a .env file inside backend/ and add:
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret_key
OPENAI_API_BASE=https://api.chatanywhere.com.cn/v1
OPENAI_API_KEY=your_dummy_api_key (anything, since it’s open)
### 3. Run Backend
nodemon server.js
Make sure MongoDB Atlas is connected.

📬 API Endpoints
Auth
POST /api/auth/signup
POST /api/auth/login

Story
POST /api/stories/generate → Requires JWT
GET /api/stories → Get all user stories
DELETE /api/stories/:id → Delete a story

🔐 Use Authorization: Bearer <token> in headers

### 🌟 Credits
1. ChatAnywhere GPT API Free
2. OpenAI
3. Chatgpt of course
4. And Me💐


