---
id: tool-05746
type: tool
area: 库
status: active
tags: [去AI味, TTS, TypeScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: Anti-AI-Writer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/re3con/anti-ai-writer
created: 2026-07-18
updated: 2026-07-18
no: 5746
category: 一、去 AI 味 / Humanizer 库
repo: RE3CON/Anti-AI-Writer
stars: 0
url: https://github.com/re3con/anti-ai-writer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 37b12f6c9dc63de6
  - methods/改稿润色指令库.md
---

# RE3CON/Anti-AI-Writer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/re3con/anti-ai-writer
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：ai-humanizer, ai-tools, aiwriting
- **GitHub 描述**：AI Footprint Scrub, an advanced, production-grade text humanizer, bypasser, and editor suite. This application is engineered to completely purge the predictable markers, robotic vocabulary, and uniform pacing typical of LLM-generated text (such as ChatGPT, Claude, and Gemini), restoring an authentic, high-impact human voice to your content.
- **本地描述**：AI Footprint Scrub, an advanced, production-grade text humanizer, bypasser, and editor suite. This application is engineered to completely purge the predictable markers, robotic vocabulary, and uniform pacing typical of LLM-generated text (such as ChatGPT, Claude, and Gemini), restoring an authentic, high-impact human voice to your content.
- **拉取时间**：2026-07-25 18:30:06

---

# AI Footprint Scrub & Text Humanizer 🧼✨

Welcome to the **AI Footprint Scrub**, an advanced, production-grade text humanizer, bypasser, and editor suite. This application is engineered to completely purge the predictable markers, robotic vocabulary, and uniform pacing typical of LLM-generated text (such as ChatGPT, Claude, and Gemini), restoring an authentic, high-impact human voice to your content.

---

## 🎨 Core Visual & Functional Features

### 1. 37 Deep-Dive Humanizer Personas
We have curated a library of **37 distinct professional, creative, and academic writing personas**, categorized cleanly into four main hubs:
- 💥 **Marketing & Copywriting**: Startups, sales landings, B2B SaaS pragmatists, direct response (Hook & Slide).
- 🎓 **Academic & Professional**: Surgical editors, technical documentation specialists, realist biographers, legal translators, and scientific skeptics.
- 🗣️ **Conversational & Social**: Ghostwriters, Reddit/forum natives, Quora experts, and LinkedIn thought leaders (no cringe!).
- 🎙️ **Creative & Scriptwriting**: Raw storytellers, late-night radio hosts, TED Keynote speakers, Wong Fu-style vloggers, and culinary writers.

### 2. 5 Micro-Scrub Modifiers (Overlays)
Apply individual overlay constraints on top of any persona:
- **The Vocabulary Scrub**: Instantly block the biggest AI giveaways (`delve`, `leverage`, `tapestry`, `foster`, `testament`, `pivot`, `utilize`, `holistic`, etc.).
- **The Burstiness Rhythm**: Mix extremely short, punchy sentences with longer flowing clauses to break uniform robotic cadence.
- **No Throat-Clearing**: Completely trim redundant, generic warm-ups or introductory sentences and start with the core value point.
- **The Coffee Shop Style**: Transform stuffy corporate language into a casual, authoritative voice-note tone.
- **The De-Hyping Filter**: Strip all hyperbole, cliché metaphors, and unearned motivational filler.

### 3. Real-Time Footprint Contrast Panel & Thesaurus
- **Footprint Highlights**: Displays input and output side-by-side with color-coded markers, highlighting detected AI slop words in red and showing their clean human equivalents in green.
- **Contrast Dictionary**: An interactive live table displaying the exact slop words found, their custom human synonyms, and their purge status (✨ *Cleaned!*).

### 4. Cadence & Authenticity Analytics
- **Human Authenticity Score**: A 0-100% metric calculated from the frequency of robotic giveaway words, uniform sentence loops, and active pacing.
- **Sentence Burstiness Meter**: Calculates the mathematical standard deviation of sentence lengths in real-time, showing whether the rhythm is naturally human or uniformly robotic.
- **Average Sentence Stats**: Compares structural length and sentence counts between your original draft and humanized output.

---

## ⚙️ Secure Full-Stack Architecture

- **Secure API Proxy**: Gemini API requests are streamed securely via Server-Sent Events (SSE) server-side in `server.ts` to fully shield system API keys.
- **Direct Client-Side Key Bypassing**: Includes a dedicated bottom setup drawer for adding your own local Gemini API Key (`AIzaSy...`). When active, all requests bypass the server quota entirely, fetching stream completions directly client-side for unlimited, fast execution!

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🚀 Commands & Development

- `npm run dev`: Boots up the server-side compiler and frontend livereload in TypeScript environment mode.
- `npm run build`: Bundles the React application and compiles `server.ts` into a fast-loading production-ready file.
- `npm run start`: Runs the pre-compiled server in production container mode.
