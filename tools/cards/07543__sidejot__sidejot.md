---
id: tool-07543
type: tool
area: 库
status: active
tags: [TypeScript, 协议宽松, 本地优先, 英文文档, 本地写作]
title: sidejot
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/sidejot/sidejot
created: 2026-07-18
updated: 2026-07-18
no: 7543
category: 画龙补充 / 扩容入库 — 补充源
repo: sidejot/sidejot
stars: 96
url: https://github.com/sidejot/sidejot
tier: "A"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 9b43a85b904ef994
  - methods/QUICK_START.md
---

# sidejot/sidejot

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/sidejot/sidejot
- **Stars**：96
- **语言**：TypeScript
- **License**：MIT
- **Topics**：adhd, pomodoro, task-scheduler, todo
- **GitHub 描述**：AI Task Planner & Pomodoro Assistant
- **本地描述**：sidejot
- **拉取时间**：2026-07-25 19:25:09

related:
  - methods/QUICK_START.md
---

# Sidejot

Sidejot is an AI-powered Pomodoro Planner designed to be privacy-focused, ADHD-friendly, and accessible. It helps you break down your tasks into manageable 25-minute chunks, ensuring you stay focused and productive.

## Features

- **AI-Powered Planning**: Uses Google Gemini 2.5 Flash (via OpenRouter) to break down vague goals into specific, actionable Pomodoro tasks.
- **Local-First & Private**: All data is stored locally in your browser using IndexedDB (Dexie.js).
- **Cross-Device Sync**: Supports syncing your plan across tabs and devices.
- **ADHD-Friendly UI**: Clean, distraction-free interface designed to reduce cognitive load.
- **Pomodoro Timer**: Integrated timer to keep you on track.
- **Dark/Light Mode**: Fully themeable UI using Tailwind CSS and shadcn/ui.

## Tech Stack

- **Framework**: Next.js 15 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS v4, shadcn/ui
- **State Management**: Zustand
- **Database**: Dexie.js (IndexedDB)
- **AI**: Vercel AI SDK 5.0, OpenRouter
- **Package Manager**: Bun

## Getting Started

### Prerequisites

- [Bun](https://bun.sh/) installed
- An [OpenRouter](https://openrouter.ai/) API Key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sidejot.git
   cd sidejot
   ```

2. Install dependencies:
   ```bash
   bun install
   ```

3. Enter your OpenRouter API key in the app's Settings UI. Keys are stored locally in your browser — there is no shared server-side key.

4. Run the development server:
   ```bash
   bun dev
   ```

5. Open [http://localhost:3000](http://localhost:3000) with your browser.

## License

MIT
