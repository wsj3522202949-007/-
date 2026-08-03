---
id: tool-01582
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI-assisted-Essay-Writing
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/hanchen9127/ai-assisted-essay-writing
created: 2026-07-18
updated: 2026-07-18
no: 1582
category: 二、网文 / 长篇 AI 写作系统 库
repo: hanchen9127/AI-assisted-Essay-Writing
stars: 0
url: https://github.com/hanchen9127/ai-assisted-essay-writing
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

# hanchen9127/AI-assisted-Essay-Writing

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/hanchen9127/ai-assisted-essay-writing
- **Stars**：0
- **语言**：JavaScript
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：A local essay practice app, shows essay prompts, lets you write responses, reveals model answers, includes a phrase-learning page with flashcards, and can optionally use AI to rate essays.
- **本地描述**：A local essay practice app, shows essay prompts, lets you write responses, reveals model answers, includes a phrase-learning page with flashcards, and can optionally use AI to rate essays.
- **拉取时间**：2026-07-23 23:25:12

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Essay Writing Practice

A local essay practice app. It shows essay prompts, lets you write responses,
reveals model answers, includes a phrase-learning page with flashcards, and can
optionally use AI to rate essays.

## Data Files

The app reads data directly from JSON files:

```text
src/data/essays.json
src/data/phrases.json
```

There is no text-source conversion step anymore. Edit these JSON files manually
when you want to change essay questions, model answers, phrases, explanations,
or translations.

## Quick Start

1. Install Node.js 20 or newer.

2. Make sure these files exist:

```text
src/data/essays.json
src/data/phrases.json
```

3. Install dependencies:

```bash
npm install
```

4. Start the local app:

```bash
npm run dev
```

5. Open:

```text
http://127.0.0.1:5173/
```

## Editing Essays

Each essay record should follow this shape:

```json
{
  "id": "essay-01",
  "number": 1,
  "title": "Work-Life Balance",
  "prompt": "Full essay question here.",
  "answer": {
    "introduction": "Model introduction here.",
    "body": ["Body paragraph one.", "Body paragraph two."],
    "conclusion": "Model conclusion here."
  }
}
```

After editing `src/data/essays.json`, refresh the browser or restart the dev
server.

## Learn Phrases

Use the `Learn Phrases` button on the main page to open the phrase-learning
page. Phrase data comes directly from:

```text
src/data/phrases.json
```

Each phrase record should follow this shape:

```json
{
  "id": "phrase-01",
  "number": 1,
  "phrase": "draw the line",
  "explanation": "To set a clear limit on what is acceptable.",
  "translation": "划清界限；设定底线"
}
```

Click a phrase card to see its English explanation and Chinese translation.
Use `Flashcards` to start a random practice queue containing half of all
phrases. Click the flashcard to flip it, then use the next button to continue.

## AI Rating

AI rating is optional. The app works without it, but the `Rate Essay` button
needs an OpenAI API key.

Create a private `.env` file:

```bash
cp .env.example .env
```

Then edit `.env`:

```text
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_MODEL=gpt-5.4-mini
PORT=5173
```

Restart the app after changing `.env`.

AI rating sends your essay, the selected prompt, and the local model answer to
the configured API provider. Only use it with content you are allowed to submit
to that provider.

## Commands

```bash
npm run dev
```

Runs the local app and API server.

```bash
npm run build
```

Builds the app for production.

```bash
npm run preview
```

Runs the production build locally.

## Notes

The code is licensed under the MIT License. 

See `CONTENT-NOTICE.md` for the full content rights notice.
