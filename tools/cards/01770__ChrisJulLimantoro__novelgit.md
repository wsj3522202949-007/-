---
id: tool-01770
type: tool
area: 库
status: active
tags: [RAG, TypeScript, 协议宽松, 需API密钥, 英文文档, 人物设定]
title: novelgit
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/chrisjullimantoro/novelgit
created: 2026-07-18
updated: 2026-07-18
no: 1770
category: 二、网文 / 长篇 AI 写作系统 库
repo: ChrisJulLimantoro/novelgit
stars: 1
url: https://github.com/chrisjullimantoro/novelgit
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ChrisJulLimantoro/novelgit

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/chrisjullimantoro/novelgit
- **Stars**：1
- **语言**：TypeScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI-powered novel management system — GitHub-backed Markdown manuscripts, TipTap editor, lore world-bible, Global Bible, dual RAG AI chat (lore + manuscript), chapter distillation, analytics, and PDF/DOCX export. Self-hosted, open source.
- **本地描述**：AI-powered novel management system — GitHub-backed Markdown manuscripts, TipTap editor, lore world-bible, Global Bible, dual RAG AI chat (lore + manuscript), chapter distillation, analytics, and PDF/DOCX export. Self-hosted, open source.
- **拉取时间**：2026-07-23 23:30:37

---

# NovelGit — AI-powered novel management

> Write freely. Your manuscripts live as plain Markdown in your own GitHub repository, version-controlled and readable in any editor. NovelGit layers a full **novel management** experience on top: library, rich editing, analytics, export, structured lore, **Global Bible** (story-wide AI summary), and **dual RAG** AI chat that pulls lore, manuscript text, and the Global Bible together. AI is optional and degrades gracefully when keys are missing.

## What it is

NovelGit is a self-hosted web app for long-form fiction. It gives you a **library**, a **TipTap** editor with GitHub sync, **analytics**, **PDF/DOCX export**, a per-novel **lore / world-bible** (`content/{novelId}/lore/`), a **Global Bible** (`content/{novelId}/global-summary.md`) maintained from chapter-level AI distillation, and an **AI chat** that can use lore entries, manuscript chunks, and the Global Bible at once.

Everything can be run on free tiers where noted:

- **GitHub** (free tier) stores content as plain `.md` and JSON
- **Groq** (free tier) powers the chat LLM and HyDE-style query expansion for manuscript search
- **OpenRouter** (free model) embeds manuscript chunks for semantic search (default embedding stack)
- **Voyage** (optional, paid) embeds lore entries (default stack); without it, lore retrieval falls back to keyword-style matching
- **Google Gemini** (optional; free tier limits apply) powers **chapter distillation**, **Global Bible** generation/patching, optional **Gemini Embedding** mode for reindexing, and configurable model IDs via **Admin → AI Settings**

---

## Features

- **Library** — list and manage novels; scaffold `content/<id>/…` in the content repo
- **Editor** — TipTap (Markdown), debounced drafts, GitHub sync, drag-and-drop chapter order, read/edit modes, floating prev/next chapter navigation
- **Lore / world-bible** — per-novel entries under `content/<novelId>/lore/*.md` with AI scaffold and semantic search (when embeddings exist)
- **Global Bible** — AI-built running overview (plot, characters, threads) stored as `content/<novelId>/global-summary.md`, updated on reindex from per-chapter summaries; editable at `/edit/<novelId>/bible`
- **AI chat** — retrieves lore and manuscript excerpts together; **injects the Global Bible** when present; combines sources for answers
- **Admin — AI Settings** (`/admin`) — edit models and **embedding provider**; settings persist as `ai-config.json` in the **content** repository
- **Analytics** — calendar heatmap of daily word counts
- **Export** — combined manuscript as PDF or DOCX in chapter order
- **Auth** — single-user passphrase; opaque session cookie; writing, admin, and export routes protected

---

## AI & RAG

The assistant uses **retrieval-augmented generation**: relevant lore, manuscript excerpts, and (when available) the Global Bible are injected into the system prompt before the LLM runs.

### Lore RAG

Structured lore files (character, location, faction, event, item) are embedded and stored in `content/{novelId}/lore-index.json`.

- **Default (`embeddingProvider: "current"` in `ai-config.json`)** — **Voyage** `voyage-3` (1024-d) via HTTPS REST. Requires `VOYAGE_API_KEY`. Without it, lore side degrades to keyword / heuristic matching.
- **Optional** — **Gemini Embedding** when `embeddingProvider` is set to `"gemini"` in Admin; reindex uses [`lib/ai/embeddings-gemini.ts`](lib/ai/embeddings-gemini.ts) and `GEMINI_API_KEY`. A **full reindex** is required after switching providers.

### Manuscript RAG

Chapters are split into overlapping **400-character** chunks (one-paragraph overlap). Per-chapter embedding shards live at `content/{novelId}/manuscript-rag-emb/{chapterSlug}.json`; metadata (and optional sharded index) in `manuscript-rag-index.json` (and `manuscript-rag-index-*.json` when sharded).

- **Default** — **OpenRouter** `nvidia/llama-nemotron-embed-vl-1b-v2:free` (2048-d). Requires `OPENROUTER_API_KEY`.
- **Optional** — same `embeddingProvider: "gemini"` path as lore, using Gemini Embedding for shard builds.

At chat time for manuscript retrieval:

1. **HyDE** — Groq generates a short hypothetical prose passage that matches the user’s intent
2. That text is embedded (default: OpenRouter) and scored against chunks with cosine similarity plus keyword and entity-style boosts
3. Top chunks are returned (see [`lib/ai/manuscript-chat-retrieval.ts`](lib/ai/manuscript-chat-retrieval.ts))

Keep **`embeddingProvider` on `current`** unless you intentionally standardize on Gemini embeddings for your indexes and understand the implications for query-time embedding alignment.

### Global Bible & chapter distillation

On **reindex**, each chapter can be **distilled** (summary, entities, tags) via **Gemini** ([`lib/ai/chapter-distillation.ts`](lib/ai/chapter-distillation.ts)). Summaries feed **Global Bible** generation or incremental patching ([`lib/ai/global-bible.ts`](lib/ai/global-bible.ts)). Model IDs come from `ai-config.json` (`distillationModel`, `bibleRebuildModel`, `biblePatchModel`). If `GEMINI_API_KEY` is unset, distillation and Global Bible generation are skipped.

### How retrieval works in chat

[`app/api/ai/[novelId]/chat/route.ts`](app/api/ai/[novelId]/chat/route.ts) loads the Global Bible (if present), then lore context, then manuscript context. The model sees all sections together.

### Citation behaviour

- **Character / world-building** questions — answers draw on context; chapter names are not emphasized unless asked.
- **Scene / “which chapter”** questions — the model is instructed to cite **chapter titles** when referring to specific manuscript moments.

### Reindex

Use **Reindex RAG** from the editor AI sidebar or the reindex API. Modes include full rebuild (lore embed, manuscript embed, distillation, Global Bible) and lighter paths. After changing **embedding provider** in Admin, run a **full** reindex so indexes match configuration.

---

## AI configuration

- **Environment** — API keys in `.env.local` (see below).
- **Runtime settings** — `/admin` reads and writes **`ai-config.json`** at the root of the **GitHub content repo** (not this app repo). Schema: [`types/ai-config.ts`](types/ai-config.ts) (`distillationModel`, `bibleRebuildModel`, `biblePatchModel`, `embeddingProvider`, `geminiEmbeddingModel`).

---

## Stack

- **Next.js 16** (App Router), React 19, TypeScript
- **Tailwind CSS v4**, shadcn-style UI components
- **Octokit** — GitHub Contents API for reads/writes
- **TipTap** + `tiptap-markdown`, `@dnd-kit`, `@nivo/calendar`, `@react-pdf/renderer`, `docx`
- **Groq** — chat completions and HyDE expansion
- **Voyage** — lore embeddings (REST, no `voyageai` SDK)
- **OpenRouter** — manuscript embeddings (REST)
- **Gemini (Google AI)** — REST for distillation, Global Bible, and optional embeddings ([`lib/ai/gemini.ts`](lib/ai/gemini.ts), [`lib/ai/embeddings-gemini.ts`](lib/ai/embeddings-gemini.ts))
- **gray-matter** — lore frontmatter

---

## Installation

### Step 1: Prerequisites

- Node.js 20+
- A **GitHub** account (free)
- **Groq** — [console.groq.com](https://console.groq.com) (chat + HyDE)
- **OpenRouter** — [openrouter.ai/keys](https://openrouter.ai/keys) (default manuscript embeddings)
- *(Optional)* **Voyage** — [voyageai.com](https://www.voyageai.com) (default lore embeddings)
- *(Optional)* **Google AI Studio** — Gemini API key for distillation, Global Bible, and optional Gemini embeddings

### Step 2: Create the content repository

Create a **private** GitHub repository for manuscripts (not the app code). Seed:

**`config/novels.json`**

```json
{ "novels": [] }
```

**`content/.gitkeep`** — empty file

Create a **Personal Access Token** with **Contents: Read and Write** and **Metadata: Read** for this repository.

### Step 3: Clone and install

```bash
git clone https://github.com/your-username/novelgit.git
cd novelgit
npm install
```

### Step 4: Configure environment

```bash
cp .env.example .env.local
```

```env
# Required
GITHUB_TOKEN=ghp_...
GITHUB_REPO=owner/repo
AUTH_SECRET=your-passphrase

# AI — recommended for full experience
GROQ_API_KEY=gsk_...
OPENROUTER_API_KEY=sk-or-...
VOYAGE_API_KEY=pa-...

# Optional — distillation, Global Bible, optional Gemini embeddings
GEMINI_API_KEY=
```

### Step 5: Run

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000). Enter your passphrase after the hero to unlock the library, editor, and admin.

---

## Environment variables

| Variable | Required | Purpose |
|----------|----------|---------|
| `GITHUB_TOKEN` | Yes | PAT for the content repo (`contents: read/write`, `metadata: read`) |
| `GITHUB_REPO` | Yes | `owner/repo` of the content store |
| `AUTH_SECRET` | Yes | Passphrase used to mint session cookies |
| `GROQ_API_KEY` | Recommended | LLM for chat and HyDE expansion |
| `OPENROUTER_API_KEY` | Recommended | Default manuscript chunk embeddings |
| `VOYAGE_API_KEY` | Optional | Default lore embeddings; keyword fallback without |
| `GEMINI_API_KEY` | Optional | Chapter distillation, Global Bible, optional Gemini embedding reindex |

Core writing features work with only the three required variables. AI features degrade gracefully when optional keys are absent.

---

## Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Next.js dev server (raises Node old-space limit for the bundler) |
| `npm run build` | Production build |
| `npm run start` | Production server |
| `npm run lint` | ESLint |

---

## Deploying

Deploy on [Vercel](https://vercel.com/) or any Node host that supports Next.js. Set environment variables in project settings. The app commits via the GitHub API — allow for rate limits when syncing many chapters.

`GET /api/health` uses `octokit.rest.repos.get` — use it to verify token and repo after deployment.

---

## Documentation

| Doc | Contents |
|-----|----------|
| [docs/design-docs.md](docs/design-docs.md) | Architecture, content schema, data flow |
| [docs/spec/ai-rag-plan.md](docs/spec/ai-rag-plan.md) | Lore + RAG + AI routes (original spec) |
| [docs/nextjs-coding-guide.md](docs/nextjs-coding-guide.md) | Next.js 16 / React 19 conventions |
| [docs/ui-ux.md](docs/ui-ux.md) | UI stack and component patterns |

This project targets **Next.js 16** — see `node_modules/next/dist/docs/` for framework APIs.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## License

This project is licensed under the [MIT License](LICENSE).
