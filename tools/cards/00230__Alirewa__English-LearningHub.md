---
id: tool-00230
type: tool
area: 库
status: active
tags: [校对, TypeScript, 协议未明, 需API密钥, 英文文档, 改稿润色]
title: English-LearningHub
summary: 错别字/语法/风格校对
source: https://github.com/alirewa/english-learninghub
created: 2026-07-18
updated: 2026-07-18
no: 230
category: 二、网文 / 长篇 AI 写作系统 库
repo: Alirewa/English-LearningHub
stars: 0
url: https://github.com/alirewa/english-learninghub
tier: "C"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 77e37e7c5e42c66b
  - methods/最强写作方法论_全球最强综合版.md
---

# Alirewa/English-LearningHub

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/alirewa/english-learninghub
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：english-learning, flashcards, framer-motion, grammar, indexeddb, language-learning, nextjs, offline-first, pwa, spaced-repetition, tailwindcss, typescript, vocabulary, zustand
- **GitHub 描述**：Premium offline-first English learning dashboard with flashcards (SM-2), vocabulary, grammar, speaking, writing, analytics, AI tools, and gamification. Built with Next.js, TypeScript, and Tailwind CSS.
- **本地描述**：Premium offline-first English learning dashboard with flashcards (SM-2), vocabulary, grammar, speaking, writing, analytics, AI tools, and gamification. Built with Next.js, TypeScript, and Tailwind CSS.
- **拉取时间**：2026-07-23 22:45:46

---

# English Learning Hub

A premium, offline-first English learning dashboard built with Next.js, TypeScript, and Tailwind CSS. Designed for serious learners who want a distraction-free, all-in-one study environment.

[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)](https://nextjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://typescriptlang.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-v4-38bdf8?logo=tailwindcss)](https://tailwindcss.com)

## Features

### Core Learning Tools
- **Vocabulary Manager** — Add, categorize, and track words with difficulty levels; auto-creates flashcards
- **Flashcard System** — SM-2 spaced repetition algorithm for optimal review scheduling
- **Common Sentences** — Persian/English sentence pairs organized by category (business, travel, daily life, etc.)
- **Grammar Academy** — 8 grammar topics with explanations, examples, and completion tracking
- **Reading Practice** — Save articles, enter reading mode, track comprehension
- **Writing Practice** — Full-screen editor with word count and grammar notes
- **Speaking Practice** — 20 prompts with star-rating sessions and history

### Planning & Analytics
- **Study Planner** — Weekly schedule by day with task types (vocabulary, grammar, reading, speaking, writing)
- **Analytics Dashboard** — 30-day XP trend chart, category distribution, streaks and milestones
- **Achievements** — 17 unlockable achievements with progress tracking

### Gamification
- **XP & Levels** — Earn XP for every learning action (words added, flashcards reviewed, sessions completed)
- **Daily Streaks** — Persistent streak tracking with longest-streak records
- **Progress Bars** — Visual XP progress toward next level in the sidebar

### AI Tools (requires Anthropic API key)
- **Sentence Explainer** — Break down grammar, vocabulary, and usage of any English sentence
- **Grammar Checker** — Identify and explain grammatical errors with corrections
- **Vocabulary Generator** — Get context-rich word lists for any topic
- **Daily Challenge** — AI-generated personalized learning challenges
- **AI Conversation** — Free-form English practice with an AI tutor

### UX
- **Offline-First** — All data stored locally via IndexedDB (Dexie) — no account needed
- **Mobile Responsive** — Collapsible sidebar on desktop; hamburger drawer on mobile
- **Dark Mode** — Polished dark-first design with light mode toggle
- **Command Palette** — `Ctrl+K` / `⌘K` to jump anywhere instantly
- **Smooth Animations** — Framer Motion transitions throughout

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Next.js (App Router, Turbopack) |
| Language | TypeScript 5 |
| Styling | Tailwind CSS v4 + shadcn/ui (base-nova) |
| Animations | Framer Motion v12 |
| State | Zustand v5 (persisted) |
| Storage | Dexie v4 (IndexedDB, fully offline) |
| Charts | Recharts v3 |
| AI | Anthropic SDK (claude-haiku-4-5) |
| Toasts | Sonner |
| Icons | Lucide React |

## Getting Started

### Prerequisites
- Node.js 18+
- npm or pnpm

### Installation

```bash
git clone https://github.com/Alirewa/English-LearningHub.git
cd English-LearningHub
npm install
```

### Environment Variables

Create a `.env.local` file in the root:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

> AI features (AI Tools page) require an Anthropic API key. All other features work fully offline without any API key.

### Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
app/
├── (app)/              # Main app shell (requires layout with sidebar)
│   ├── layout.tsx      # Shell layout: sidebar, mobile drawer, toasts
│   ├── dashboard/      # Home dashboard with stats & quick actions
│   ├── vocabulary/     # Word management CRUD
│   ├── flashcards/     # Spaced repetition review sessions
│   ├── grammar/        # Grammar topics with examples
│   ├── sentences/      # Persian/English sentence library
│   ├── reading/        # Article saving and reading mode
│   ├── writing/        # Writing journal with editor
│   ├── speaking/       # Speaking practice with prompts
│   ├── planner/        # Weekly study planner
│   ├── analytics/      # Learning analytics & charts
│   ├── achievements/   # Gamification achievement board
│   └── ai-tools/       # AI-powered learning tools
├── api/ai/             # Anthropic API proxy route
└── page.tsx            # Root redirect to /dashboard

components/
├── layout/             # Header, Sidebar (desktop+mobile), CommandPalette
└── ui/                 # shadcn/ui base components

lib/
├── db.ts               # Dexie schema, seed data, SM-2 algorithm, XP system
└── store.ts            # Zustand global state
```

## Spaced Repetition (SM-2)

Flashcards use the SM-2 algorithm:
- **Easy** → longer interval, increased ease factor
- **Medium** → same interval
- **Hard** → reset to 1-day interval, decreased ease factor

The next review date is stored in IndexedDB and cards are surfaced when due.

## XP Rewards

| Action | XP |
|--------|-related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Word added | +5 |
| Flashcard reviewed | +2 |
| Grammar topic completed | +20 |
| Reading completed | +15 |
| Writing entry | +10 |
| Speaking session | +10 |
| Daily streak maintained | +5 |

## License

MIT
