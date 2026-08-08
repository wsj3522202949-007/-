---
id: tool-05412
type: tool
area: 库
status: active
tags: [RAG, TypeScript, 协议未明, 本地优先, 英文文档, 人物设定, 本地写作]
title: cf_ai_plot-armor-ai
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/shalinidhar/cf_ai_plot-armor-ai
created: 2026-07-18
updated: 2026-07-18
no: 5412
category: 一、去 AI 味 / Humanizer 库
repo: shalinidhar/cf_ai_plot-armor-ai
stars: 0
url: https://github.com/shalinidhar/cf_ai_plot-armor-ai
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4a9a217fc60957b1
  - methods/改稿润色指令库.md
---

# shalinidhar/cf_ai_plot-armor-ai

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/shalinidhar/cf_ai_plot-armor-ai
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：An AI-powered writing tool that detects plot holes in a story. 
- **本地描述**：An AI-powered writing tool that detects plot holes in a story.
- **拉取时间**：2026-07-25 18:17:37

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# -- Plot Armor AI -- 
A full-stack story continuity assistant. Use AI to scan your drafts against your "Story Bible" to find plot holes and character contradictions before they reach your readers.

# Link to Project 
https://6f3e028b.plot-armor-ai.pages.dev/

# Project Structure
This is a monorepo containing both the frontend and backend services:

/client: React frontend powered by Vite and styled with Tailwind CSS v4.

/server: Backend API powered by Hono running on Cloudflare Workers.

# Tech Stack
Frontend: React, Vite, Tailwind CSS v4, Lucide React (Icons)

Backend: Hono, Cloudflare Workers, Cloudflare Workflows

AI: Llama 3.1 8B (via Cloudflare Workers AI)

Database: Cloudflare D1 (SQLite)

# Getting Started
1. Prerequisites
Node.js (v18 or higher)

Cloudflare Wrangler (for backend development)

2. Installation
Install dependencies for both the frontend and backend:

Bash
# Install frontend dependencies
cd client && npm install

# Install backend dependencies
cd ../server && npm install
3. Local Development
You will need two terminal windows open to run the full stack:

Terminal 1: Frontend (Vite)

Bash
cd client
npm run dev
Runs at: http://localhost:5173

Terminal 2: Backend (Hono/Wrangler)

Bash
cd server
npx wrangler dev
Runs at: http://localhost:8787

# Configuration
Frontend Proxy
The Vite dev server is configured in client/vite.config.ts to proxy all /api requests to the Hono server at 127.0.0.1:8787 to avoid CORS issues during development.

Database (Cloudflare D1)
The backend uses a D1 database for logging. To initialize your local database:

Bash
cd server
npx wrangler d1 execute plot_armor_db --local --command="CREATE TABLE IF NOT EXISTS plot_hole_logs (id INTEGER PRIMARY KEY AUTOINCREMENT, analysis TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
# Deployment
Backend (Workers)
Login to Cloudflare: npx wrangler login

Deploy the worker: cd server && npx wrangler deploy

Frontend (Pages)
Build the project: cd client && npm run build

Deploy to Cloudflare Pages:

Bash
npx wrangler pages deploy dist --project-name plot-armor-ai

