---
id: tool-01506
type: tool
area: 库
status: active
tags: [互动叙事, TypeScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: ai-behavior-designer
summary: 互动叙事/聊天写故事
source: https://github.com/webartzy/ai-behavior-designer
created: 2026-07-18
updated: 2026-07-18
no: 1506
category: 二、网文 / 长篇 AI 写作系统 库
repo: webartzy/ai-behavior-designer
stars: 0
url: https://github.com/webartzy/ai-behavior-designer
tier: "C"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# webartzy/ai-behavior-designer

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/webartzy/ai-behavior-designer
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Design AI behavior before writing prompts. Open-source playground for AI builders.
- **本地描述**：Design AI behavior before writing prompts. Open-source playground for AI builders.
- **拉取时间**：2026-07-23 23:23:00

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Behavior Designer

**Design the behavior first. Generate the prompt second.**

An open-source playground that helps AI builders and vibe coders design a production-ready behavior spec and system prompt for an AI support agent — before they touch a single line of prompt copy.

> 📸 _Screenshot placeholder — replace with a screenshot of the builder once deployed._

## Why this exists

Most AI chatbots fail because of bad prompts. But that's rarely the real cause — the deeper problem is that nobody designed the AI's behavior before writing the prompt.

**Prompts are implementation. Behavior is architecture.**

This project started from one idea: most AI chatbots fail because the behavior was never designed. AI Behavior Designer breaks that decision-making into nine layers — identity, goal, audience, tone, scope, boundaries, fallback, output style, and examples — and turns your answers into a behavior spec, a production-ready system prompt, and an AI Readiness Score that tells you what's still missing.

This is **not** a chatbot builder and **not** a SaaS product. There's no login, no database, no server, and no paid API required. Everything runs client-side, and your work is saved to your browser's local storage.

## Features

- **Nine-layer behavior form** — identity, goal, audience, tone, scope, boundaries, fallback, output style, and few-shot examples.
- **Live-generated Behavior Spec** — a clean markdown document you can hand to a teammate or drop in a repo.
- **Live-generated System Prompt** — a production-ready, XML-tagged system prompt built from your answers.
- **AI Readiness Score (0–100)** — a weighted score across all nine layers with a status label (risky / decent but fragile / production-minded / strong) and a list of missing layers.
- **Copy & download** — copy either output to your clipboard, or download the behavior spec as `.md` / the system prompt as `.txt`.
- **Sample templates** — three fully worked examples (SaaS support agent, crypto community assistant, AI product onboarding agent) you can load straight into the builder.
- **LocalStorage persistence** — refresh the page without losing your work.
- **Dark mode, responsive, no backend** — deploy-ready for Vercel out of the box.

## Tech stack

- [Next.js](https://nextjs.org) (App Router, latest stable)
- TypeScript (strict mode)
- Tailwind CSS v4
- 100% client-side logic — no database, no auth, no server-side API calls

## Local setup

```bash
git clone https://github.com/your-username/ai-behavior-designer.git
cd ai-behavior-designer
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

Other useful commands:

```bash
npm run lint   # ESLint
npm run build  # production build
npm run start  # serve the production build locally
```

## Deploy to Vercel

1. Push this repo to your own GitHub account.
2. Go to [vercel.com/new](https://vercel.com/new) and import the repo.
3. Leave the defaults (Next.js is auto-detected) and click **Deploy**.

No environment variables, database, or API keys are required.

## How to customize

- **Behavior layers & scoring** — `lib/types.ts` (layer definitions) and `lib/calculateScore.ts` (scoring weights and status thresholds).
- **Behavior Spec / System Prompt generation** — `lib/generatePrompt.ts`. Edit the templates here to change the markdown structure or the XML tags used in the system prompt.
- **Sample templates** — `lib/examples.ts`. Add, remove, or edit the example behavior specs shown on `/examples`.
- **Copy & positioning** — `components/Hero.tsx`, `app/about/page.tsx`.
- **Theme** — CSS variables in `app/globals.css` (`--background`, `--surface`, `--accent`, etc).
- **GitHub link** — update `GITHUB_URL` in `lib/constants.ts` to point at your fork.

## Project structure

```
app/                # routes: / (landing + builder), /about, /examples
components/          # Hero, BehaviorForm, LivePreview, ScoreCard, OutputTabs, LayerProgress, ExampleCard, Builder, Nav, Footer
lib/
  types.ts           # BehaviorSpec, layer definitions
  generatePrompt.ts  # behavior spec + system prompt generators
  calculateScore.ts  # AI Readiness Score logic
  examples.ts         # sample behavior spec templates
```

## License

MIT — fork it, remix it, ship your own version.

## Build in public

This project started from one idea: most AI chatbots fail because the behavior was never designed. If you build something with it, tag it — this is meant to be forked, remixed, and shared.

## Creator

Built by Artzy.
