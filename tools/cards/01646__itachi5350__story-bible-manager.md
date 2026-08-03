---
id: tool-01646
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: story-bible-manager
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/itachi5350/story-bible-manager
created: 2026-07-18
updated: 2026-07-18
no: 1646
category: 二、网文 / 长篇 AI 写作系统 库
repo: itachi5350/story-bible-manager
stars: 0
url: https://github.com/itachi5350/story-bible-manager
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# itachi5350/story-bible-manager

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/itachi5350/story-bible-manager
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：itachi5350/story-bible-manager
- **拉取时间**：2026-07-23 23:27:02

---

# 📖 Story Bible Manager

I built this because I love writing stories — and I kept forgetting details about my own characters. 
This app fixes that. Upload your story chapters, and ask the AI anything about your own story. It answers from *your* writing, not from guesswork.

## Live App
👉 **[story-bible-manager.vercel.app](https://story-bible-manager.vercel.app)**

---

## What it does

**Ask questions about your story**
> "What do we know about King Aldric?"
> "Who knows about the secret meeting?"

**Check for contradictions**
> Paste a new scene you just wrote — the AI tells you if it conflicts with anything you've already written.

**Extract characters automatically**
> One click pulls out every character with their description, traits and relationships.

---

## TechStack

- **React + Vite** for the frontend
- **FastAPI** for the backend
- **ChromaDB** to store and search story content
- **Cohere** for turning text into searchable vectors
- **Groq (Llama 3.3)** as the AI brain
- **Vercel + Render** for deployment

---

## Run it locally

You'll need a free API key from [Groq](https://console.groq.com) and [Cohere](https://dashboard.cohere.com).

**Backend**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

**`.env` file in `/backend`**
```
GROQ_API_KEY=your_key
COHERE_API_KEY=your_key
```

---

## How it works under the hood

When you upload a chapter, the app splits it into chunks and converts each chunk into a vector (a list of numbers that captures meaning). These vectors are stored in ChromaDB.

When you ask a question, your question gets converted to a vector too. ChromaDB finds the chunks that are closest in meaning, and passes them to the AI as context. The AI reads those chunks and answers from them — not from its own training data.

This is called RAG (Retrieval Augmented Generation).

---


related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*Built by Sarika — because writers deserve better tools.*
