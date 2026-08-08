---
id: tool-01171
type: tool
area: 库
status: active
tags: [提示词, JavaScript, 协议未明, 本地优先, 英文文档, 多Agent, 本地写作]
title: prompt-library
summary: 提示词/写作工作流
source: https://github.com/glittercowboy/prompt-library
created: 2026-07-18
updated: 2026-07-18
no: 1171
category: 二、网文 / 长篇 AI 写作系统 库
repo: glittercowboy/prompt-library
stars: 23
url: https://github.com/glittercowboy/prompt-library
tier: "B"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: e2157bb347b463e8
  - methods/最强写作方法论_全球最强综合版.md
---

# glittercowboy/prompt-library

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/glittercowboy/prompt-library
- **Stars**：23
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Prompt Library - Save, organize, and share prompts for music, marketing, writing, images & code
- **本地描述**：AI Prompt Library - Save, organize, and share prompts for music, marketing, writing, images & code
- **拉取时间**：2026-07-23 23:13:11

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Prompt Library

A clean, notion-like AI prompt library for creators. Save, organize, and share your prompts for music production, marketing, writing, images, and code.

![Prompt Library](https://img.shields.io/badge/React-18-blue) ![Tailwind](https://img.shields.io/badge/Tailwind-4-cyan) ![Vite](https://img.shields.io/badge/Vite-7-purple)

## Features

- **Save Prompts** - Store prompts with title, category, text, and tags
- **Categories** - Music Production, Marketing, Writing, Images, Code
- **Search & Filter** - Find prompts by text, tags, or category
- **One-Click Copy** - Copy prompts instantly to clipboard
- **Variable Placeholders** - Use `{{genre}}`, `{{mood}}` etc. and fill them in when copying
- **Favorites** - Star your most-used prompts
- **Import/Export** - Backup and restore as JSON
- **Share via URL** - Share individual prompts with a unique link
- **Dark Mode** - Easy on the eyes
- **Local Storage** - Your data stays on your device

## Quick Start

```bash
npm install
npm run dev
```

## Variable Placeholders

Use double curly braces for variables that you fill in when copying:

```
Create a {{duration}} minute {{genre}} track with a {{mood}} atmosphere.
```

When you copy, a modal appears to fill in each variable.

## Tech Stack

- **Vite** + **React 18**
- **Tailwind CSS 4**
- **Lucide Icons**
- **Local Storage** for persistence

## Deployment

### Vercel (Recommended)

1. Push to GitHub
2. Import in Vercel
3. Deploy automatically

### Manual Build

```bash
npm run build
# Output in dist/
```

## License

MIT
