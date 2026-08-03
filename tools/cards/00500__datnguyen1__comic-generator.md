---
id: tool-00500
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: comic-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/datnguyen1/comic-generator
created: 2026-07-18
updated: 2026-07-18
no: 500
category: 二、网文 / 长篇 AI 写作系统 库
repo: datnguyen1/comic-generator
stars: 1
url: https://github.com/datnguyen1/comic-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# datnguyen1/comic-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/datnguyen1/comic-generator
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Build an AI-powered comic creator that turns any written story, script, or simple paragraph into a full sequence of manga-style illustrated panels with consistent characters, dynamic scenes, speech bubbles, and sound effects.
- **本地描述**：Build an AI-powered comic creator that turns any written story, script, or simple paragraph into a full sequence of manga-style illustrated panels with consistent characters, dynamic scenes, speech bubbles, and sound effects.
- **拉取时间**：2026-07-23 22:53:38

---

# Comic Generator

AI-powered comic creation app. Enter a story and generate manga-style comic panels using Hugging Face.

## Prerequisites

- Node.js >= 18.0.0
- npm >= 9.0.0
- MongoDB (local or cloud)
- [Hugging Face](https://huggingface.co) account (for AI generation)

## Quick Start

### 1. Clone and Install

```bash
npm install
npm run install:all
```

### 2. Environment Setup

**Backend** (`backend/.env`):
```bash
cd backend
cp .env.example .env
```

Required: `DATABASE_URL`, `HUGGINGFACE_TOKEN`. See [backend/README.md](backend/README.md) for Hugging Face setup.

**Frontend** (`frontend/.env`):
```env
VITE_API_URL=http://localhost:3000
```

### 3. Run the Application

```bash
npm run dev
```

- **Frontend:** http://localhost:5173
- **Backend:** http://localhost:3000

### 4. Verify

Visit http://localhost:3000/health to check the backend.

## Features

- **Create comics** – Story → AI-generated panel descriptions → AI-generated panel images
- **Manga styles** – shounen, shoujo, seinen, chibi, isekai
- **Manga AI page** – `/manga-ai` (UI demo)

## Tech Stack

| Layer   | Tech |
|---------|---related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Frontend | React 18, Vite, React Router, Axios, TailwindCSS |
| Backend  | Node.js, Express, Mongoose |
| Database | MongoDB |
| AI       | Hugging Face Inference (chat + FLUX.1-schnell) |

## Project Structure

```
comic-generator/
├── frontend/     # React app
├── backend/      # Express API + AI service
└── package.json
```

## Troubleshooting

### Port Already in Use
If ports 3000 or 5173 are already in use, update the port numbers in:
- Backend: `backend/.env` (PORT)
- Frontend: `frontend/vite.config.js` (server.port)

### Module Not Found
```bash
rm -rf node_modules frontend/node_modules backend/node_modules
npm run install:all
```

## License

MIT
