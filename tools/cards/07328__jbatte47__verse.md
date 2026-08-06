---
id: tool-07328
type: tool
area: 库
status: active
tags: [TypeScript, 协议传染, 本地优先, 英文文档, 人物设定, RAG, 本地写作]
title: verse
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/jbatte47/verse
created: 2026-07-18
updated: 2026-07-18
no: 7328
category: 画龙补充 / 扩容入库 — 补充源
repo: jbatte47/verse
stars: 1
url: https://github.com/jbatte47/verse
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/QUICK_START.md
---

# jbatte47/verse

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/jbatte47/verse
- **Stars**：1
- **语言**：TypeScript
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：an open source content management tool for world builders and storytellers
- **本地描述**：verse
- **拉取时间**：2026-07-25 19:18:00

related:
  - methods/QUICK_START.md
---

# Verse

An open source content management platform for world builders and storytellers.

**Build lore wikis, curate art galleries, publish prose, and bring your worlds to life.**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Deploy to Cloudflare](https://github.com/jbatte47/verse/actions/workflows/deploy.yml/badge.svg)](https://github.com/jbatte47/verse/actions/workflows/deploy.yml)

## Features

- **Lore Wiki** — Interconnected knowledge bases for characters, locations, factions, and timelines
- **Art Gallery** — Showcase concept art, maps, and visual assets with metadata and tagging
- **Text Reader** — Beautiful Markdown-rendered prose with rich typography
- **Secure Auth** — Pluggable authentication via Cloudflare Access
- **Edge-First** — Deployed on Cloudflare Workers for global performance
- **WCAG Compliant** — Accessible by design, mobile-first responsive layouts

## Tech Stack

- [Next.js 15](https://nextjs.org/) — React framework with App Router
- [Cloudflare Workers](https://workers.cloudflare.com/) — Edge runtime via [OpenNext](https://opennext.js.org/cloudflare)
- [Cloudflare D1](https://developers.cloudflare.com/d1/) — Serverless SQL for structured content
- [Cloudflare R2](https://developers.cloudflare.com/r2/) — Object storage for media assets
- [Cloudflare KV](https://developers.cloudflare.com/kv/) — Key-value store for config and flags

## Getting Started

### Prerequisites

- Node.js 22+
- npm

### Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Preview with Cloudflare runtime
npm run preview
```

### Deployment

Deployments are fully automated via GitHub Actions. Push to `main` and the site deploys to Cloudflare Workers within minutes.

To deploy manually:

```bash
npm run deploy
```

## Architecture

```
  GitHub (push to main)
    │
    ▼
  GitHub Actions (build + deploy)
    │
    ▼
  Cloudflare Workers (edge runtime)
    │
    ├──▶  KV    config, feature flags
    ├──▶  D1    lore entries, metadata
    └──▶  R2    images, media, prose files

  Content persists across deployments ✓
```

## License

This project is licensed under the [GNU General Public License v3.0](https://github.com/jbatte47/verse/blob/main/LICENSE).
