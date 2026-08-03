---
id: tool-00452
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ai-storyboard-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/shubh-vedi/ai-storyboard-generator
created: 2026-07-18
updated: 2026-07-18
no: 452
category: 二、网文 / 长篇 AI 写作系统 库
repo: shubh-vedi/ai-storyboard-generator
stars: 7
url: https://github.com/shubh-vedi/ai-storyboard-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# shubh-vedi/ai-storyboard-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/shubh-vedi/ai-storyboard-generator
- **Stars**：7
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：shubh-vedi/ai-storyboard-generator
- **拉取时间**：2026-07-23 22:52:17

---

# 🎬 AI Storyboard Generator

> Turn any script or scene description into a sequential cinematic storyboard — powered by **Gemini 3.1 Flash Image Preview** via **OpenRouter**, with a draggable React timeline.

---

## Features

- 📝 **Script-to-storyboard** — paste any script or scene description, choose 1–8 frames
- 🖼️ **Gemini image gen** — each scene rendered as a pencil-sketch cinematic storyboard frame
- 🎞️ **Filmstrip timeline** — horizontal drag-and-drop reordering with `@dnd-kit`
- 🗑️ **Delete frames** — remove unwanted frames from the board
- 📥 **Export** — download the storyboard metadata as JSON
- 🌑 **Dark cinematic theme** — IMDb-style gold + charcoal design

---

## Project Structure

```
ai-storyboard-generator/
├── backend/
│   ├── agent.py         # Scene splitting + Gemini image gen via OpenRouter
│   ├── main.py          # FastAPI app (POST /generate-storyboard)
│   ├── requirements.txt
│   └── .env.example
└── frontend/            # Vite + React
    └── src/
        ├── App.jsx
        ├── App.css
        └── components/
            ├── ScriptInput.jsx
            ├── StoryboardTimeline.jsx
            └── FrameCard.jsx
```

---

## Setup

### 1. Backend

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Add your OpenRouter API key
cp .env.example .env
# Edit .env → OPENROUTER_API_KEY=your_key

# Start the server
uvicorn main:app --reload --port 8000
```

> API docs available at http://localhost:8000/docs

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

> Open http://localhost:5173

---

## Usage

1. Enter a script or scene description in the left panel
2. Choose how many frames to generate (1–8)
3. Click **🎬 Generate Storyboard**
4. Watch frames appear in the filmstrip timeline
5. **Drag** frames to reorder • **Hover** to see full scene detail • **✕** to delete

---

## Environment Variables

| Variable | Description |
|---|---|
| `OPENROUTER_API_KEY` | Your OpenRouter API key (get one at [openrouter.ai](https://openrouter.ai)) |

---

## Models Used

| Task | Model |
|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Image generation | `google/gemini-3.1-flash-image-preview` |
| Scene splitting | `google/gemini-3.0-flash` |
