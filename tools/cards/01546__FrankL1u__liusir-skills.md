---
id: tool-01546
type: tool
area: 库
status: active
tags: [Claude插件, TypeScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: liusir-skills
summary: Claude Code 插件式写作流
source: https://github.com/frankl1u/liusir-skills
created: 2026-07-18
updated: 2026-07-18
no: 1546
category: 二、网文 / 长篇 AI 写作系统 库
repo: FrankL1u/liusir-skills
stars: 2
url: https://github.com/frankl1u/liusir-skills
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# FrankL1u/liusir-skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/frankl1u/liusir-skills
- **Stars**：2
- **语言**：TypeScript
- **License**：None
- **Topics**：agent-skills, agent-workflow, ai-skills, claude-code, codex, content-automation, wechat, wechat-official-account
- **GitHub 描述**：AI agent skills for WeChat article writing, publishing, and workflow automation.
- **本地描述**：AI agent skills for WeChat article writing, publishing, and workflow automation.
- **拉取时间**：2026-07-23 23:24:11

---

# LIUSIR Skills

AI agent skills for source collection, content workflows, and publishing automation.

This repository currently includes three workflow skills:

- Local media and article collection workflow
- WeChat Official Account article workflow
- Xiaohongshu note workflow

## Available Skills

| Skill | Description |
|-------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| [ls-multi-collector](./skills/ls-multi-collector) | Collect Douyin, YouTube, WeChat, X, and generic web content into local bundles with video download, transcript, and article-fetch workflows |
| [ls-wechat-article](./skills/ls-wechat-article) | Write and publish WeChat Official Account articles end-to-end — topic intake, drafting, SEO polish, cover and inline images, theme preview, draft publish, stats backfill, and learning workflows |
| [ls-xhs-note](./skills/ls-xhs-note) | Create Xiaohongshu note assets end-to-end — topic intake, source article drafting, native note writing, visual planning, and image generation |

## Quick Install

### Install a specific skill

```bash
npx skills add FrankL1u/liusir-skills --skill ls-multi-collector
npx skills add FrankL1u/liusir-skills --skill ls-wechat-article
npx skills add FrankL1u/liusir-skills --skill ls-xhs-note
```

### See available skills

```bash
npx skills add FrankL1u/liusir-skills --list
```

### Install from a marketplace plugin

This repository also includes a plugin-style distribution path through `.claude-plugin/`.

## Prerequisites

Some skills may require additional local setup.

Common prerequisites across the workflow skills:

- Node.js >= 18
- Python >= 3.9
- `ls-multi-collector` also requires `uv`, `ffmpeg`, `yt-dlp`, `defuddle`, `xreach`, and `camoufox`
- Optional image provider keys for AI image generation

Skill-specific notes:

- `ls-multi-collector`: collects source material into local bundles; remote ASR and LLM are optional for transcript enhancement
- `ls-wechat-article`: requires WeChat Official Account API credentials for publishing, and can optionally use TrendRadar MCP for topic signals
- `ls-xhs-note`: does not publish directly; it can optionally use TrendRadar MCP for topic signals and image providers for Step 5 generation

See the setup guides in [skills/ls-multi-collector/README.md](./skills/ls-multi-collector/README.md), [skills/ls-wechat-article/README.md](./skills/ls-wechat-article/README.md), and [skills/ls-xhs-note/README.md](./skills/ls-xhs-note/README.md).

## Works With

These skills are designed for AI agents and coding tools that support skill-style packaging:

- OpenClaw
- Claude Code
- Cursor
- Codex
- Gemini CLI
- Windsurf
- Kilo
- OpenCode
- Goose
- Roo
- Any tool supporting `npx skills add`

## Repository Layout

```text
.
├── .claude-plugin/        # Plugin-style distribution metadata
├── .github/workflows/     # CI and release workflows
├── scripts/               # Repository-level maintenance scripts
├── shared/                # Shared templates and publishing docs
└── skills/                # Installable skills
```

## Contributing

### Add a new skill

1. Create `skills/<skill-name>/`
2. Add a `SKILL.md` with `name`, `version`, `description`, triggers, and usage rules
3. Add skill-specific references, scripts, and runtime files inside that skill directory
4. Update any plugin or marketplace metadata if needed
5. Open a pull request

### Update an existing skill

1. Make your changes
2. Bump the `version:` in `SKILL.md`
3. Update skill-specific docs if behavior changed
4. Open a pull request

## Publish

- CI can publish changed skills through the repository release flow
- Repository maintenance scripts live under `scripts/`

## Notes

- Each skill should keep its own agent-facing files inside its skill directory
- Runtime output, caches, secrets, and virtualenvs should stay out of `skills/`
- `shared/` is repository-level guidance and publishing support, not per-skill runtime output

## License

MIT
