---
id: tool-01443
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: FlowForge-AI
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/yatindrarai002/flowforge-ai
created: 2026-07-18
updated: 2026-07-18
no: 1443
category: 二、网文 / 长篇 AI 写作系统 库
repo: YatindraRai002/FlowForge-AI
stars: 0
url: https://github.com/yatindrarai002/flowforge-ai
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# YatindraRai002/FlowForge-AI

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/yatindrarai002/flowforge-ai
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Intelligent marketing automation platform with collaborative AI agents. Delivers professional-grade content through autonomous planning, research, writing, and review workflows. Built on FastAPI and Groq LLM for enterprise scalability.
- **本地描述**：Intelligent marketing automation platform with collaborative AI agents. Delivers professional-grade content through autonomous planning, research, writing, and review workflows. Built on FastAPI and Groq LLM for enterprise scalability.
- **拉取时间**：2026-07-23 23:21:10

---

# 🚀 FlowForge AI

FlowForge AI is a **multi-agent marketing automation system** that generates complete marketing campaigns in seconds using AI.

Built with **FastAPI + React + Groq LLM**, it automates planning, research, content creation, review, and final assembly.

## ✨ Features

- Multi-agent AI workflow
- Real-time progress streaming (SSE)
- Smart caching for faster responses
- Groq-powered LLM inference
- Modern React frontend
- FastAPI backend
- Exportable marketing briefs

---

## 🏗 Architecture

```mermaid
graph LR
    U[User] --> F[React Frontend]
    F --> B[FastAPI Backend]
    B --> O[Workflow Orchestrator]

    O --> A1[Planner]
    O --> A2[Researcher]
    O --> A3[Writer]
    O --> A4[Reviewer]
    O --> A5[Assembler]

    A1 --> G[Groq LLM]
    A2 --> G
    A3 --> G
    A4 --> G
    A5 --> G

    O --> C[Cache]
```

### Workflow

```text
User Input
   ↓
Planner
   ↓
Researcher
   ↓
Writer
   ↓
Reviewer
   ↓
Assembler
   ↓
Final Marketing Brief
```

---

## 🛠 Tech Stack

### Frontend
- React
- TailwindCSS
- Framer Motion

### Backend
- FastAPI
- Pydantic
- Async Python

### AI
- Groq LLM
- Multi-Agent Orchestration

---

## 🚀 Quick Start

```bash
# Clone repo
git clone https://github.com/YatindraRai002/FlowForge-AI.git

# Backend
cd backend
pip install -r requirements.txt

# Add API key
GROQ_API_KEY=your_api_key

# Run backend
python main.py

# Frontend
cd ..
npm install
npm run dev
```

---

## 📂 Project Structure

```bash
FlowForge-AI/
├── backend/
│   ├── agents/
│   ├── orchestrator.py
│   ├── main.py
│
├── frontend/
│   ├── src/
│   ├── components/
│
└── README.md
```

---

## ⚡ API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/workflow/start` | Start workflow |
| `/api/workflow/stream` | Stream progress |
| `/api/workflow/result` | Get final result |

---

## 📜 License

MIT License

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---
⭐ Star this repo if you find it useful.
