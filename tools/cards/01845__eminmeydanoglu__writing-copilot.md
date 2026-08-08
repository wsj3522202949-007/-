---
id: tool-01845
type: tool
area: 库
status: active
tags: [Claude插件, TypeScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: writing-copilot
summary: Claude Code 插件式写作流
source: https://github.com/eminmeydanoglu/writing-copilot
created: 2026-07-18
updated: 2026-07-18
no: 1845
category: 二、网文 / 长篇 AI 写作系统 库
repo: eminmeydanoglu/writing-copilot
stars: 0
url: https://github.com/eminmeydanoglu/writing-copilot
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: f86835e8904cc426
  - methods/最强写作方法论_全球最强综合版.md
---

# eminmeydanoglu/writing-copilot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/eminmeydanoglu/writing-copilot
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A collobarative and powerful way to write good stuff with AI | Works with any agent that can use Skills
- **本地描述**：A collobarative and powerful way to write good stuff with AI （ Works with any agent that can use Skills
- **拉取时间**：2026-07-23 23:32:48

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# writing-copilot

`writing-copilot` is an Obsidian plugin for reviewing a sibling shadow file next to a Markdown note.

## How It Works

- canonical note: `x.md`
- agent working copy: `x.shadow`
- review command: `Toggle Diff Review Mode`

Open `x.md` in Obsidian, keep `x.shadow` in the same folder, then run the command. The plugin opens a split diff review surface, keeps both sides editable, highlights pending changes, and lets you approve or reject the selected change.

## Repo Layout

- `src/`: plugin runtime and review logic
- `tests/`: unit tests
- `skills/`: local writing-copilot skill material
- `writings/styles/`: shared style references for writing projects
- `archive/app/`: archived web prototype kept only as reference

## Install

1. Run `npm install`
2. Run `npm run build`
3. Create `<vault>/.obsidian/plugins/writing-copilot/`
4. Copy `manifest.json` and `styles.css` into that folder
5. Copy the built `main.js` into that folder
6. Enable `Writing Copilot` in Obsidian community plugins

## Develop

- `npm run dev`: watch and rebuild `main.js`
- `npm run typecheck`
- `npm test`
