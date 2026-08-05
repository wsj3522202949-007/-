---
id: tool-01619
type: tool
area: 库
status: active
tags: [校对, TypeScript, 协议未明, 本地优先, 中文友好, 改稿润色, 本地写作]
title: PromptDock
summary: 错别字/语法/风格校对
source: https://github.com/madamagy1-art/promptdock
created: 2026-07-18
updated: 2026-07-18
no: 1619
category: 二、网文 / 长篇 AI 写作系统 库
repo: madamagy1-art/PromptDock
stars: 4
url: https://github.com/madamagy1-art/promptdock
tier: "B"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# madamagy1-art/PromptDock

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/madamagy1-art/promptdock
- **Stars**：4
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：PromptDock is a lightweight desktop companion for writing better AI prompts. Summon it with a shortcut, keep it on top, organize and search past prompts, manage groups and templates with fillable variables, import or export your library, and connect any OpenAI-compatible API for one-click prompt optimization and smart completion while you write AI.
- **本地描述**：PromptDock is a lightweight desktop companion for writing better AI prompts. Summon it with a shortcut, keep it on top, organize and search past prompts, manage groups and templates with fillable variables, import or export your library, and connect any OpenAI-compatible API for one-click prompt optimization and smart completion while you write AI.
- **拉取时间**：2026-07-23 23:26:14

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# PromptDock

**Language:** English | `[中文](README.zh-CN.md)`

PromptDock is a lightweight Windows desktop companion for writing, organizing, and improving AI prompts. It stays out of the way until you summon it, then gives you a focused workspace for drafting prompts, reusing templates, searching prompt history, and improving prompts with any OpenAI-compatible API.

## Features

- **Global shortcut summon:** Use `Alt + Space` to show or hide PromptDock quickly.
- **Tray-first desktop workflow:** PromptDock can stay running in the system tray, and closing the window hides it instead of quitting.
- **Always on top:** Keep the prompt window above other applications when you are working across documents, browsers, and chat tools.
- **Draggable compact window:** The frameless window includes a drag handle and title area for easy repositioning.
- **Prompt editor:** Write prompts in a clean, spellcheck-free editor designed for mixed technical and natural-language drafting.
- **Prompt optimization:** Connect an OpenAI-compatible Chat Completions API and optimize the current prompt with one click.
- **Prompt completion:** Enable smart completion suggestions while writing, then accept suggestions with `Tab` or dismiss them with `Esc`.
- **Prompt history:** Save prompts when optimizing, copying, creating from templates, or manually saving.
- **Prompt management:** Name prompts, assign groups, mark favorites, edit saved prompts, and filter history by group or favorite status.
- **Full-text search:** Search past prompts through a local SQLite history database.
- **Prompt import/export:** Import or export your prompt library as JSON for backup or migration.
- **Template library:** Create, edit, delete, and search reusable prompt templates.
- **Fillable variables:** Use `{{variable}}` placeholders in templates and fill them through a generated form.
- **Bilingual UI:** Switch between English and Chinese in settings. English is the default language.
- **Secure API key storage:** API keys are stored through the operating system credential store via `keytar`; SQLite only stores non-secret settings.
- **Local-first data:** Prompts, templates, and settings stay on your machine.

## Model Configuration

PromptDock works with OpenAI-compatible Chat Completions endpoints. In Settings, configure:

- Base URL, for example `https://api.openai.com/v1`
- Model name
- API key
- Request timeout
- Prompt completion toggle
- Always-on-top behavior
- Interface language

PromptDock does not ship with any private API URL or API key.

## Development

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
npm run dist
```

The Windows portable executable is generated in `release/`.

## Tests

```bash
npm test
```

## Data And Privacy

- Local database: stored in the Electron user data directory as `promptdock.sqlite`.
- API key: stored in the system credential manager, not in SQLite.
- Build outputs, local databases, executables, and dependency folders are ignored by Git.

## Release

Current release: `v0.01`
