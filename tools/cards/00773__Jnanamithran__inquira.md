---
id: tool-00773
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: inquira
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/jnanamithran/inquira
created: 2026-07-18
updated: 2026-07-18
no: 773
category: 二、网文 / 长篇 AI 写作系统 库
repo: Jnanamithran/inquira
stars: 0
url: https://github.com/jnanamithran/inquira
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 3606de40104128df
  - methods/最强写作方法论_全球最强综合版.md
---

# Jnanamithran/inquira

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jnanamithran/inquira
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：ai, buiness-intelligence, fastapi, llama, natural-language-processing, nlp, nodejs, ollama, postgresql, react, saas, sql
- **GitHub 描述**：Inquira is an AI-powered Business Intelligence platform that enables organizations to interact with their data using natural language. Connect your existing databases, ask questions in plain English, and receive instant insights through AI-generated SQL, interactive dashboards, and visual analytics—all without writing a single SQL query.
- **本地描述**：Inquira is an AI-powered Business Intelligence platform that enables organizations to interact with their data using natural language. Connect your existing databases, ask questions in plain English, and receive instant insights through AI-generated SQL, interactive dashboards, and visual analytics—all without writing a single SQL query.
- **拉取时间**：2026-07-23 23:01:34

---

# Inquira

> Ask Better. Know Faster.

Inquira is a full-stack B2B SaaS platform that lets non-technical users query their business databases using plain English — no SQL knowledge required.

---

## What it does

Instead of writing SQL, users simply ask questions like:

- "What was our total revenue last month?"
- "Show the top 5 customers by order value."
- "Which product had the highest sales this quarter?"

Inquira translates these into safe, read-only SQL queries, executes them on the connected database, and returns results as tables with AI-generated summaries.

---

## Tech Stack

### Frontend
- React 19 + Vite
- Tailwind CSS
- Framer Motion
- React Router
- TanStack Query
- Axios

### Backend
- Node.js + Express
- Prisma ORM
- PostgreSQL
- JWT + bcrypt
- AES-256-CBC encryption

### AI Service
- Python + FastAPI
- Ollama (local LLM)
- Llama 3.2

---

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Frontend  │────▶│   Backend   │────▶│  AI Service │
│  React/Vite │     │ Express/Node│     │FastAPI/Python│
│  Port 5173  │     │  Port 5000  │     │  Port 8000  │
└─────────────┘     └─────────────┘     └─────────────┘
                           │                    │
                    ┌──────┴──────┐      ┌──────┴──────┐
                    │  Inquira DB │      │   Ollama    │
                    │ PostgreSQL  │      │ Llama 3.2   │
                    └─────────────┘      └─────────────┘
```

---

## Features

- **Natural Language Queries** — Ask questions in plain English
- **Read-Only & Secure** — Never writes to your database
- **Multi-Tenant Workspaces** — Full tenant isolation per organization
- **Schema Introspection** — Auto-discovers tables, columns and relationships
- **SQL Safety Validator** — Blocks all non-SELECT queries and injection patterns
- **AI Summaries** — Plain English explanation of every query result
- **Custom Roles & RBAC** — Owner, Admin, Analyst, Viewer + custom roles
- **Audit Logs** — Full activity trail for every user action
- **Local LLM** — Runs on Ollama locally, no external API costs
- **Multi-Database Support** — PostgreSQL, MySQL, MariaDB, SQL Server

---

## Project Structure

```
inquira/
├── frontend/          # React + Vite frontend
├── backend/           # Node.js + Express backend
├── ai-service/        # Python + FastAPI AI service
└── docs/              # Documentation
```

---

## Getting Started

### Prerequisites

- Node.js 20+
- Python 3.12+
- PostgreSQL 17+
- Ollama (https://ollama.com)

### 1. Clone the repo

```bash
git clone https://github.com/Jnanamithran/inquira.git
cd inquira
```

### 2. Set up the backend

```bash
cd backend
npm install
cp .env.example .env
# Edit .env with your PostgreSQL credentials
npx prisma migrate dev
npm run dev
```

### 3. Set up the frontend

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

### 4. Set up the AI service

```bash
cd ai-service
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python main.py
```

### 5. Pull the Llama model

```bash
ollama pull llama3.2
```

### 6. Open the app

```
http://localhost:5173
```

---

## Environment Variables

### Backend `.env`

```env
PORT=5000
CLIENT_URL=http://localhost:5173
DATABASE_URL="postgresql://postgres:yourpassword@localhost:5432/inquira_db"
JWT_SECRET=your_jwt_secret
JWT_EXPIRES_IN=7d
ENCRYPTION_KEY=your_32_char_encryption_key
AI_SERVICE_URL=http://localhost:8000
NODE_ENV=development
```

### Frontend `.env`

```env
VITE_API_URL=http://localhost:5000/api
```

---

## How the Query Flow Works

```
User asks a question
        ↓
Frontend sends question + connectionId to Backend
        ↓
Backend fetches schema from user's database
        ↓
Backend calls AI Service with question + schema
        ↓
AI Service builds prompt and sends to Ollama (Llama 3.2)
        ↓
Llama generates SQL query
        ↓
Backend validates SQL (SELECT only, no injections)
        ↓
Backend executes SQL on user's database
        ↓
Results returned as table + AI summary
```

---

## Security

- JWT authentication on all protected routes
- Passwords hashed with bcrypt (12 rounds)
- Database credentials encrypted with AES-256-CBC
- Read-only database connections enforced
- SQL validator blocks all non-SELECT statements
- Full audit logging of all user actions
- Multi-tenant isolation — organizations cannot access each other's data

---

## Built by

Jnanamithran — Final Year B.Tech Computer Science
St. Thomas Institute for Science & Technology, Trivandrum, Kerala

GitHub: [@Jnanamithran](https://github.com/Jnanamithran)
LinkedIn: [jnanamithran](https://linkedin.com/in/jnanamithran)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

© 2026 Inquira. All rights reserved.
