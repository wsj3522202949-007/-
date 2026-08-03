---
id: tool-07642
type: tool
area: 库
status: active
tags: [多Agent, JavaScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: comicgeneration
summary: 多 Agent 协作自动产文
source: https://github.com/yuvrajgupta1808/comicgeneration
created: 2026-07-18
updated: 2026-07-18
no: 7642
category: 画龙补充 / 扩容入库 — 补充源
repo: yuvrajgupta1808/comicgeneration
stars: 1
url: https://github.com/yuvrajgupta1808/comicgeneration
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# yuvrajgupta1808/comicgeneration

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/yuvrajgupta1808/comicgeneration
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Designed a LangGraph-based agentic pipeline to convert story prompts into multi-page comics with a human-in-the-loop workflow, coordinating prompt orchestration, panel layout, and scene continuity across pages
- **本地描述**：comicgeneration
- **拉取时间**：2026-07-25 19:28:38

related:
  - methods/QUICK_START.md
---

# 🎨 Comic Generation Platform

An AI-powered comic generation platform that combines Leonardo AI image generation with intelligent layout composition and dialogue management.

## 📁 Project Structure

This monorepo contains two main components:

- **comic-backend** - LangChain-based agent for comic generation with Leonardo AI
- **comic-frontend** - React-based web interface for comic creation

## 🚀 Quick Start

### Prerequisites

- Node.js 16+ 
- npm or yarn
- Leonardo AI API key
- Cloudinary account (for image storage)
- Google Gemini API key (for comic-backend)

### Installation

```bash
# Install all dependencies
npm install --prefix comic-backend
npm install --prefix comic-frontend
```

### Environment Setup

Each project requires its own `.env` file. See individual project READMEs for details.

### Running the Application

Open two terminal windows:

**Terminal 1 - Backend:**
```bash
cd comic-backend
npm run langchain
```
Wait for: `✓ Server running on http://localhost:8000`

**Terminal 2 - Frontend:**
```bash
cd comic-frontend
npm start
```
Opens automatically at `http://localhost:3000`

## 🎯 Features

- **AI-Powered Panel Generation** - Generate comic panels with Leonardo AI
- **Character Consistency** - Maintain character appearance across panels
- **Smart Layouts** - Automatic page composition with multiple layout options
- **Dialogue Management** - Add speech bubbles, narration, and sound effects
- **Interactive Agent** - Conversational interface for comic creation
- **Web Interface** - User-friendly frontend for comic generation
- **Cloudinary Integration** - Direct display of generated panels

## 🎨 Usage

Chat with the agent in the frontend:

```
You: "Create a sci-fi comic about a space explorer"

Agent: 
✅ Generated 8 panels successfully!
▸ Panel 1 (establishing-shot): [description]
▸ Panel 2 (medium-shot): [description]
...

You: "Generate characters"

Agent:
✅ Generated 2 characters successfully!
👤 Character 1 (char_1): [details]
👤 Character 2 (char_2): [details]

You: "Generate images"

Agent:
✅ Comic panels generated! Your comic grid is now displayed in the frontend.
```

The system automatically generates images with Leonardo AI, uploads to Cloudinary, and displays your comic grid. No manual steps needed!

## 📚 Documentation

- [comic-backend README](./comic-backend/README.md) - LangChain agent documentation
- [comic-frontend README](./comic-frontend/README.md) - Frontend documentation

## 🛠️ Tech Stack

- **Backend**: Node.js, LangChain, Leonardo AI, Cloudinary
- **Frontend**: React, TypeScript, Tailwind CSS, Framer Motion
- **AI Models**: Google Gemini, Leonardo Phoenix 1.0
- **Image Processing**: Sharp, Canvas

## 📝 License

ISC

## 🤝 Contributing

Contributions are welcome! Please check individual project READMEs for specific guidelines.
