---
id: tool-01489
type: tool
area: 库
status: active
tags: [Claude插件, TypeScript, 协议宽松, 需API密钥, 英文文档]
title: pen
summary: Claude Code 插件式写作流
source: https://github.com/fauzaanu/pen
created: 2026-07-18
updated: 2026-07-18
no: 1489
category: 二、网文 / 长篇 AI 写作系统 库
repo: fauzaanu/pen
stars: 0
url: https://github.com/fauzaanu/pen
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1562bca4a3dc6b32
  - methods/最强写作方法论_全球最强综合版.md
---

# fauzaanu/pen

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/fauzaanu/pen
- **Stars**：0
- **语言**：TypeScript
- **License**：MIT
- **Topics**：ai, obsidian, writing
- **GitHub 描述**：Pen is an Obsidian plugin that brings AI-powered writing directly into your notes. Out of the box it works as a research assistant, but since you can fully customize the system prompt, custom rules, and profiles, it becomes whatever writing tool you need
- **本地描述**：Pen is an Obsidian plugin that brings AI-powered writing directly into your notes. Out of the box it works as a research assistant, but since you can fully customize the system prompt, custom rules, and profiles, it becomes whatever writing tool you need
- **拉取时间**：2026-07-23 23:22:31

---

# Pen

Pen is an Obsidian plugin that brings AI-powered writing directly into your notes. Out of the box it works as a research assistant, but since you can fully customize the system prompt, custom rules, and profiles, it becomes whatever writing tool you need — a translator, a copywriter, a summarizer, a brainstorming partner, or anything else you can describe in a prompt.

Powered by Google's Gemini API. Also supports image generation.

## Features

- **AI writing from any prompt** — Customize the system prompt and rules to make Pen do any writing task, not just research
- **Profiles** — Save multiple prompt configurations and switch between them (e.g. one for research, one for translation, one for creative writing)
- **Web search** — Optionally use Gemini's built-in web search for up-to-date information
- **Image generation** — Select text and generate an image from it, embedded directly in your note
- **Frontmatter fields** — Define custom fields (text or list) that get populated automatically alongside the generated content
- **Custom rules** — Append extra instructions per profile (e.g. "Always write in Spanish", "Use formal tone")

## Installation

1. Download the latest release from [GitHub Releases](https://github.com/fauzaanu/pen/releases)
2. Extract `main.js`, `manifest.json`, and `styles.css` into your vault's `.obsidian/plugins/pen/` folder
3. Reload Obsidian and enable the plugin in Settings → Community Plugins

## Setup

1. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Open Settings → Pen
3. Paste your API key in the "Gemini API key" field

## Usage

### Commands

All commands are available from the Command Palette (`Ctrl/Cmd + P`):

| Command | Description |
|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Pen: Research | Generates content based on the note title, existing content, and your active profile's prompt |
| Pen: Research with web search | Same as above, but with Gemini web search enabled |
| Pen: Generate image from selected text | Generates an image from selected text and embeds it in the note |

### Profiles

Profiles are the core of Pen's flexibility. Each profile has its own:

- System prompt — defines what Pen does (research, translate, rewrite, summarize, etc.)
- Image prompt — template for image generation, use `{{selection}}` as a placeholder
- Custom rules — additional instructions layered on top of the system prompt
- Frontmatter fields — auto-populated metadata fields

Create a "Translator" profile with a translation prompt, a "Blog Writer" profile for drafting posts, a "Study Notes" profile for academic summaries — then switch between them in one click.

You can create, rename, duplicate, and delete profiles from the settings tab.

### Frontmatter fields

Add custom frontmatter fields that Pen populates during generation. For example, a `tags` field with type `list` generates relevant tags automatically. A `summary` field with type `text` produces a short summary.

## Development

```bash
npm install
npm run dev       # watch mode — outputs to build/
npm run build     # production build — outputs to build/
npx vitest --run  # run tests
```

Build output goes to `build/` (includes `main.js`, `manifest.json`, and `styles.css`).

### Installing into your vaults

```bash
npm run install-plugin
```

This builds the plugin, then reads your Obsidian config to find all your vaults. It prompts you for each one — hit `y` to symlink `build/` into that vault's `.obsidian/plugins/pen/`, or `n` to skip. With the symlink in place, rebuilds are picked up automatically on reload.

## License

[MIT](https://github.com/fauzaanu/pen/blob/main/LICENSE)
