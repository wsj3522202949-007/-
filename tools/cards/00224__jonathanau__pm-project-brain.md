---
id: tool-00224
type: tool
area: 库
status: active
tags: [TTS, Claude插件, 协议宽松, 本地优先, 英文文档, 本地写作]
title: pm-project-brain
summary: 小说转语音/有声书
source: https://github.com/jonathanau/pm-project-brain
created: 2026-07-18
updated: 2026-07-18
no: 224
category: 二、网文 / 长篇 AI 写作系统 库
repo: jonathanau/pm-project-brain
stars: 4
url: https://github.com/jonathanau/pm-project-brain
tier: "B"
use_case: "小说转语音/有声书"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8b49691827404007
  - methods/最强写作方法论_全球最强综合版.md
---

# jonathanau/pm-project-brain

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jonathanau/pm-project-brain
- **Stars**：4
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A reusable prompt that helps product managers set up persistent AI context ("project brain") for any AI coding assistant. Run it once, answer the interview questions, and your product knowledge, terminology, writing standards, and key decisions load automatically in every future conversation.
- **本地描述**：A reusable prompt that helps product managers set up persistent AI context ("project brain") for any AI coding assistant. Run it once, answer the interview questions, and your product knowledge, terminology, writing standards, and key decisions load automatically in every future conversation.
- **拉取时间**：2026-07-23 22:45:36

---

# PM Project Brain

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A reusable prompt that helps product managers set up persistent AI context ("project brain") for any AI coding assistant. Run it once, answer the interview questions, and your product knowledge, terminology, writing standards, and key decisions load automatically in every future conversation.

## What it does

The prompt walks you through four sections:

1. **Product Context**: vision, codenames, business models, customer segments, metrics, infrastructure, geographic footprint, features, active/paused initiatives
2. **Terminology & Acronyms**: product, technical, business, infrastructure, platform, and organizational terms, kept consistent everywhere
3. **Writing Standards**: document formats like PRFAQs (press release/FAQs), PRDs (product requirements documents), and one-pagers; writing voice; metric conventions; frequently asked questions (FAQ) style; PRD templates; and formatting rules
4. **Key Decisions & Constraints**: settled strategic/product/technical/pricing decisions, things you don't do, canceled initiatives, and open questions

After the interview, the AI generates context files in the correct format for your tool.

## Compatible tools and where files go

| Tool | Context file location | Global location | Format |
|---|---|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Claude Code | `CLAUDE.md` (project root) | `~/.claude/CLAUDE.md` | Single markdown file |
| Codex CLI | `AGENTS.md` (project root) | `~/.codex/AGENTS.md` | Single markdown file |
| Antigravity | `.gemini/GEMINI.md` (project root) | `~/.gemini/GEMINI.md` | Single markdown file (same as Gemini CLI) |
| Gemini CLI | `GEMINI.md` (project root) | `~/.gemini/GEMINI.md` | Single markdown file |
| Cursor | `.cursor/rules/*.mdc` | User-level rules in Settings | Markdown with YAML front matter |
| GitHub Copilot | `.github/copilot-instructions.md` | Settings > Copilot > Custom Instructions | Single markdown file |
| OpenCode | `AGENTS.md` (project root) | `~/.config/opencode/AGENTS.md` | Single markdown file |
| Qwen Code | `QWEN.md` (project root or `.qwen/QWEN.md`) | `~/.qwen/QWEN.md` | Single markdown file |
| Windsurf | `.windsurf/rules/*.md` | `global_rules.md` via Settings | Markdown (12K char limit per file) |
| Kiro IDE / CLI | `.kiro/steering/*.md` | `~/.kiro/steering/*.md` | Markdown with YAML front matter |

For single-file tools (Claude Code, Codex CLI, Gemini CLI, Antigravity, GitHub Copilot, OpenCode, Qwen Code), the AI will combine all sections into one file using H1 headers as separators. For multi-file tools (Kiro, Cursor, Windsurf), it will create one file per section.

## How to use

1. Copy the entire contents of [PM-Project-Brain-Prompt.md](https://github.com/jonathanau/pm-project-brain/blob/main/PM-Project-Brain-Prompt.md?plain=1)
2. Paste it into your AI assistant and follow the interactive interview
3. Review the generated files and commit them to your project repo

The AI will ask which tool you're using and create files in the right format and location.

## Tips for providing input

- You can answer the questions conversationally, or you can share documents (drag and drop, paste, or reference files) and the AI will extract the relevant information.
- The more specific you are with numbers, dates, and names, the more useful the project brain will be.
- You do not need to answer every question. Skip what is not relevant and you can always add more later.
- Review your project brain quarterly to keep it current.

## License

This project is licensed under the [MIT License](https://github.com/jonathanau/pm-project-brain/blob/main/LICENSE).
