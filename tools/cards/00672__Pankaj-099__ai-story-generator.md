---
id: tool-00672
type: tool
area: 库
status: active
tags: [互动叙事, Python, 协议未明, 需API密钥, 英文文档]
title: ai-story-generator
summary: 互动叙事/聊天写故事
source: https://github.com/pankaj-099/ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 672
category: 二、网文 / 长篇 AI 写作系统 库
repo: Pankaj-099/ai-story-generator
stars: 2
url: https://github.com/pankaj-099/ai-story-generator
tier: "B"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 26317b82689d0344
  - methods/最强写作方法论_全球最强综合版.md
---

# Pankaj-099/ai-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/pankaj-099/ai-story-generator
- **Stars**：2
- **语言**：Python
- **License**：None
- **Topics**：ai, fastapi, fullstack, openai, python, react
- **GitHub 描述**：AI-powered interactive story app using FastAPI + React
- **本地描述**：AI-powered interactive story app using FastAPI + React
- **拉取时间**：2026-07-23 22:58:37

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI-Powered Choose Your Own Adventure Story App

Full-stack interactive storytelling game where AI generates dynamic, branching stories based on user choices in real-time.

## Project Overview
This is an AI-integrated full-stack web application that lets users create and play "choose-your-own-adventure" style stories.  
- Enter a theme (e.g., "fantasy dragon quest" or "sci-fi space mission").  
- AI generates the starting story and multiple choices.  
- Select a choice → AI continues the story with new branches.  
- Stories are saved in the database for resuming later.

Built as a portfolio project to showcase full-stack skills with modern AI integration.

## Features
- Real-time AI story generation using LLM (OpenAI/Groq compatible)  
- Interactive choice-based gameplay with branching narratives  
- User story history and resume functionality  
- Responsive React frontend with loading states and UI feedback  
- Secure FastAPI backend APIs  
- Database integration for persistent data  

## Tech Stack
- **Backend**: FastAPI (Python), Pydantic for validation, SQLAlchemy/PostgreSQL  
- **Frontend**: React + Vite (fast development & HMR), JavaScript/TypeScript  
- **AI/LLM**: OpenAI API (or alternatives like Groq/Llama) for dynamic content generation  
- **Database**: PostgreSQL (or SQLite for local testing)  
- **Other**: Environment variables (.env), CORS handling, async APIs  

## Setup & Installation (For Reference)
1. Clone the repo  
2. Install dependencies:  
   - Backend: `pip install -r backend/requirements.txt`  
   - Frontend: `cd frontend && npm install`  
3. Set up `.env` with your OpenAI API key (OPENAI_API_KEY=sk-...)  
4. Run backend: `uvicorn main:app --reload` (from backend folder)  
5. Run frontend: `npm run dev` (from frontend folder)  

(Note: API key required for AI features; without it, UI loads but generation fails.)

## Why This Project?
As a fresher, this project helped me learn:  
- Full-stack integration (React frontend calling FastAPI backend)  
- API design with async endpoints  
- LLM prompting and integration  
- Database CRUD for user data  
- Modern tools like Vite for fast frontend dev  


Feel free to fork/contribute! 🚀
