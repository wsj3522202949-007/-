---
id: tool-01227
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ai-writing-copilot
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/twangapples/ai-writing-copilot
created: 2026-07-18
updated: 2026-07-18
no: 1227
category: 二、网文 / 长篇 AI 写作系统 库
repo: twangapples/ai-writing-copilot
stars: 0
url: https://github.com/twangapples/ai-writing-copilot
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

# twangapples/ai-writing-copilot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/twangapples/ai-writing-copilot
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Web-based document editor with real-time AI-powered inline autocomplete — like GitHub Copilot for writing
- **本地描述**：Web-based document editor with real-time AI-powered inline autocomplete — like GitHub Copilot for writing
- **拉取时间**：2026-07-23 23:14:52

---

# AI Writing Copilot

A web-based document editor with real-time AI-powered inline autocomplete — like GitHub Copilot, but for natural language writing.

![Demo](https://placehold.co/800x400?text=AI+Writing+Copilot)

## Features

- **Ghost text autocomplete** — suggestions appear inline as you type; press `Tab` to accept, keep typing to dismiss
- **Prefix matching** — typing a character that matches the ghost text advances it instead of resetting
- **Word boundary triggering** — suggestions only fire after a complete word (space/punctuation), never mid-word
- **Document Plan** — describe your writing intent, structure, or goals; included in every AI prompt
- **Auto-summarization** — the AI periodically summarizes your document and uses it as context
- **Autocomplete level slider** — control suggestion length from a single word (level 1) up to multiple paragraphs (level 10)
- **Streaming responses** — suggestions stream in token by token; cancelled instantly when you type

## Tech Stack

- **[Next.js 16](https://nextjs.org/)** — App Router, full-stack (frontend + API routes in one)
- **[Lexical](https://lexical.dev/)** — extensible rich text editor by Meta
- **[OpenAI GPT-4o mini](https://platform.openai.com/docs/models/gpt-4o-mini)** — fast, cheap model for all autocomplete levels
- **[Tailwind CSS v4](https://tailwindcss.com/)** — styling
- **TypeScript** — throughout

## How It Works

```
User types → pauses at word boundary (420ms debounce)
           → extract context (plan + auto-summary + recent paragraphs + current sentence)
           → POST /api/autocomplete
           → GPT-4o mini streams tokens back
           → ghost text appears inline
           → Tab to accept / keep typing to dismiss
```

### Context Layers (sent with every request)

| Layer | Source | Purpose |
|-------|--------|---------|
| Document Plan | User-written | High-level intent and structure |
| Auto-summary | AI-generated (every 30s) | What's been written so far |
| Recent paragraphs | Last 2 paragraphs | Local writing context |
| Current sentence | Text up to cursor | Immediate completion target |

### Autocomplete Levels

| Level | Completion | Max Tokens |
|-------|-----------|--------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| 1–2 | Word / Word+ | 8–12 |
| 3–4 | Phrase / Half sentence | 20–35 |
| 5–6 | Sentence / Sentence+ | 50–75 |
| 7–8 | 2–3 sentences | 120–180 |
| 9–10 | Paragraph / Multi-paragraph | 250–400 |

## Getting Started

### Prerequisites

- Node.js 18+
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

```bash
git clone https://github.com/twangapples/ai-writing-copilot.git
cd ai-writing-copilot
npm install
```

### Configuration

Copy the example env file and add your OpenAI key:

```bash
cp .env.example .env.local
```

```env
OPENAI_API_KEY=sk-...
```

### Run

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Project Structure

```
├── app/
│   ├── page.tsx                    # Entry point
│   ├── layout.tsx
│   └── api/autocomplete/route.ts   # Streaming GPT-4o mini endpoint
│
├── components/
│   ├── WritingApp.tsx              # Top-level shell, holds plan + level state
│   ├── editor/
│   │   ├── Editor.tsx              # LexicalComposer + plugin assembly
│   │   ├── GhostTextNode.ts        # Custom DecoratorNode (inline, excluded from copy)
│   │   ├── GhostTextPlugin.tsx     # Tab accept, Escape dismiss
│   │   ├── AutocompletePlugin.tsx  # Debounce, streaming, prefix matching
│   │   └── DocumentSummaryPlugin.tsx
│   └── ui/
│       ├── DocumentPlan.tsx        # Collapsible plan textarea
│       ├── LevelSlider.tsx
│       └── StatusBar.tsx
│
├── lib/autocomplete/
│   ├── buildPrompt.ts              # Assembles OpenAI chat messages
│   └── levelConfig.ts              # Level → { maxTokens, stopSequences }
│
└── types/autocomplete.ts
```

## License

MIT
