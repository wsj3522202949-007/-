---
id: tool-00188
type: tool
area: 库
status: active
tags: [多Agent, 大纲规划, TTS, TypeScript, 协议未明, 需API密钥, 英文文档]
title: ai-writer-room
summary: 多 Agent 协作自动产文
source: https://github.com/igorverevkin1992/ai-writer-room
created: 2026-07-18
updated: 2026-07-18
no: 188
category: 二、网文 / 长篇 AI 写作系统 库
repo: igorverevkin1992/ai-writer-room
stars: 0
url: https://github.com/igorverevkin1992/ai-writer-room
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: c28bbd289ab156f0
  - methods/最强写作方法论_全球最强综合版.md
---

# igorverevkin1992/ai-writer-room

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/igorverevkin1992/ai-writer-room
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A professional-grade desktop tool for fiction writers, powered by Google Gemini AI. This application features a multi-agent system to help you plan, write, and maintain continuity in your stories.
- **本地描述**：A professional-grade desktop tool for fiction writers, powered by Google Gemini AI. This application features a multi-agent system to help you plan, write, and maintain continuity in your stories.
- **拉取时间**：2026-07-23 22:44:30

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---


# ✍️ Virtual Writers Room v2.0

A professional-grade desktop tool for fiction writers, powered by Google Gemini AI. This application features a multi-agent system to help you plan, write, and maintain continuity in your stories.

## 🚀 Features

- **Project Bible**: Manage story summaries, characters, and locations in one place.
- **AI Agents**:
  - **Planner**: Generates detailed beat sheets from rough ideas.
  - **Writer**: Drafts vivid prose based on your plans.
  - **Continuity**: Checks your scenes against the Project Bible for inconsistencies.
  - **Editor**: Refines style and dialogue based on your instructions.
  - **Visualizer**: Creates concept art using Gemini 2.5 Flash Image.
- **Read Aloud**: Integrated TTS to hear your prose as it's written.
- **Docker Ready**: Easy setup with containerization.

## 🛠 Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/virtual-writers-room.git
   cd virtual-writers-room
   ```

2. **Configure API Key**:
   Create a `.env` file in the root directory:
   ```env
   VITE_GEMINI_API_KEY=your_api_key_here
   ```

3. **Run with Docker**:
   ```bash
   docker-compose up --build
   ```
   Open [http://localhost:5173](http://localhost:5173) in your browser.

## 📦 Tech Stack

- **Frontend**: React 19, TypeScript, Tailwind CSS
- **AI**: @google/genai (Gemini 3 Flash & 2.5 Flash Image)
- **Environment**: Vite + Docker
