---
id: tool-00196
type: tool
area: 库
status: active
tags: [TypeScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ai-text-editor
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/darrylschaefer/ai-text-editor
created: 2026-07-18
updated: 2026-07-18
no: 196
category: 二、网文 / 长篇 AI 写作系统 库
repo: darrylschaefer/ai-text-editor
stars: 42
url: https://github.com/darrylschaefer/ai-text-editor
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 3193151769a1170c
  - methods/最强写作方法论_全球最强综合版.md
---

# darrylschaefer/ai-text-editor

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/darrylschaefer/ai-text-editor
- **Stars**：42
- **语言**：TypeScript
- **License**：MIT
- **Topics**：ai, artificial-intelligence, chatgpt, openai, productivity, text, text-editor, word-processor, writing
- **GitHub 描述**：AI-powered word processor for writers—semantic search, version diffs, and tool-using agents with reusable prompt macros.
- **本地描述**：AI-powered word processor for writers—semantic search, version diffs, and tool-using agents with reusable prompt macros.
- **拉取时间**：2026-07-23 22:44:44

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ai-text-editor

Local-first AI text editor for writers. Manage documents, run powerful macros, and collaborate with AI agents (with tools) using your own API key.

[Visit Website](https://fthr.vercel.app/) · [Report Bugs](https://github.com/darrylschaefer/ai-text-editor/issues/new/choose) · [Request Feature](https://github.com/darrylschaefer/ai-text-editor/issues/new/choose)

## Core features
- **Document management**: create, edit, organize, export/import
- **AI agents with tool access**: multi-step workflows that can call tools to help complete tasks
- **Reusable macros & prompts**: quick actions, templates, and selection sending
- **Semantic / hybrid search (embeddings)**: faster "find by meaning," not just keywords
- **Revision history & diffs**: inspect changes over time
- **Mobile + desktop friendly**

## Privacy / Data
Your documents and API key are stored locally on your device. When you use AI features (including agents, tools, and embeddings), the app sends relevant text/context and request payloads to the OpenAI API for processing; we don't store your content on our servers.

## Prerequisites
- **Node.js**
- **OpenAI API key**

## Getting started (dev)
```bash
git clone https://github.com/darrylschaefer/ai-text-editor
cd ai-text-editor
npm install
npm run dev
```

Open: `http://localhost:5173`

## Backup
Use **Export** in the sidebar to save your data and **Import** to restore it.

## Contributing
Issues and PRs welcome.

## License / Credits
Inspired by and adapted from BetterChatGPT (CC0). This project is released under the MIT license.
