---
id: tool-01457
type: tool
area: 库
status: active
tags: [TypeScript, 协议宽松, 需API密钥, 中文友好, 大纲规划, 多Agent, 灵感创意]
title: ParaWrite
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/a5677746shdh/parawrite
created: 2026-07-18
updated: 2026-07-18
no: 1457
category: 二、网文 / 长篇 AI 写作系统 库
repo: a5677746shdh/ParaWrite
stars: 0
url: https://github.com/a5677746shdh/parawrite
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# a5677746shdh/ParaWrite

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/a5677746shdh/parawrite
- **Stars**：0
- **语言**：TypeScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：ParaWrite is an open‑source writing assistant inspired by DeepL’s “Alternatives” feature. It helps you polish translations and text by suggesting context‑aware synonyms, rephrasing, and style refinements—all powered by configurable large language model (LLM) APIs. Bring your own API key to tailor the model and pricing to your needs. 
- **本地描述**：ParaWrite is an open‑source writing assistant inspired by DeepL’s “Alternatives” feature. It helps you polish translations and text by suggesting context‑aware synonyms, rephrasing, and style refinements—all powered by configurable large language model (LLM) APIs. Bring your own API key to tailor the model and pricing to your needs.
- **拉取时间**：2026-07-23 23:21:33

---

# ParaWrite

[English](README.md) | [中文](README.zh-CN.md)

ParaWrite is an open-source writing assistant inspired by DeepL's "Alternatives" feature. Translate text with streaming LLM output, then refine the result with context-aware synonyms, dictionary lookups, and sentence rephrasing.

**Version 1.1.2** — see [CHANGELOG.md](CHANGELOG.md) · [中文更新日志](CHANGELOG.zh-CN.md).

## Screenshots

| Desktop (three-column) | Tablet (two-column) |
|:---:|:---:|
| ![Desktop layout](docs/snapshots/desktop-layout.jpg) | ![Tablet layout](docs/snapshots/tablet-layout.jpg) |

| Mobile (stacked) | Synonyms & alternatives |
|:---:|:---:|
| ![Mobile layout](docs/snapshots/mobile-layout.jpg) | ![Synonyms panel](docs/snapshots/synonyms-panel.jpg) |

| Main interface | Login dialog |
|:---:|:---:|
| ![Main interface](docs/snapshots/main-interface.jpg) | ![Login dialog](docs/snapshots/login-dialog.jpg) |

More UI details: [docs/UI-DESIGN.md](docs/UI-DESIGN.md).

## Features

- **Streaming translation** with DeepL-style source/target panes and responsive layouts
- **Word panel** — synonyms, bilingual dictionary, and alternative phrasings on word click
- **Glossary** — YAML domain terms in prompts; `other` fallback; optional pane marking (`app.point_out_glossary`)
- **Translation history** — auto-save when signed in; favorites, pagination, bulk select/delete
- **Configurable LLM backends** — OpenAI-compatible APIs, Claude, and Ollama via YAML
- **Per-user preferences** — optional `app` / `theme` / glossary YAML per account
- **PWA** — installable app with offline shell

## Prerequisites

- Node.js **≥ 22**
- pnpm **9.15** (see `packageManager` in `package.json`)

## Quick Start

```bash
pnpm install
cp config/config.example.yaml config/config.yaml
export OPENAI_API_KEY=your-key-here   # or set keys in config.yaml
pnpm dev
```

- Frontend: http://localhost:5173 (proxies `/api` to the backend)
- Backend: http://localhost:8787

Production:

```bash
pnpm build
pnpm start    # serves API + built frontend on :8787
```

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for Docker and beta packaging.

## Architecture

```
parawrite/
├── apps/web/       # Vite + React frontend (PWA)
├── apps/server/    # Hono API + static file server
├── packages/core/  # Shared engines, dictionary, config, types
├── config/         # YAML templates (secrets gitignored)
├── data/           # SQLite user data (gitignored)
├── docker/         # Production Docker
└── docs/           # Technical documentation
```

## Documentation

| Document | Description |
|----------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| [docs/README.md](docs/README.md) | Documentation index |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | System design and request flow |
| [docs/CONFIGURATION.md](docs/CONFIGURATION.md) | YAML configuration reference |
| [docs/API.md](docs/API.md) | HTTP API and SSE protocol |
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Docker, beta package, environment variables |
| [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) | Local development and build scripts |
| [docs/UI-DESIGN.md](docs/UI-DESIGN.md) | UI tokens, layout, and screenshots |

## License

MIT — see [LICENSE](LICENSE).
