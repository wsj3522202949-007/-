---
id: tool-00624
type: tool
area: 库
status: active
tags: [Claude插件, 协议未明, 本地优先, 英文文档, 本地写作]
title: ai-system-prompts
summary: Claude Code 插件式写作流
source: https://github.com/thomasvunguyen/ai-system-prompts
created: 2026-07-18
updated: 2026-07-18
no: 624
category: 二、网文 / 长篇 AI 写作系统 库
repo: ThomasVuNguyen/ai-system-prompts
stars: 0
url: https://github.com/thomasvunguyen/ai-system-prompts
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ThomasVuNguyen/ai-system-prompts

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/thomasvunguyen/ai-system-prompts
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：System prompts extracted from 9 top AI coding agents (Codex, Claude Code, Cursor, Windsurf, Aider, SWE-agent, Hermes, OpenClaw, OpenCode) + a practical guide on writing your own
- **本地描述**：System prompts extracted from 9 top AI coding agents (Codex, Claude Code, Cursor, Windsurf, Aider, SWE-agent, Hermes, OpenClaw, OpenCode) + a practical guide on writing your own
- **拉取时间**：2026-07-23 22:57:16

---

# 🧠 AI System Prompt Collection

> System prompts extracted from the source code of the 9 most popular AI coding agents — plus a practical guide on how to write your own.

## What's Inside

| # | File | Tool | Source | Size |
|---|------|------|--------|---related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| 📘 | `[00-how-to-write-system-prompts.md](00-how-to-write-system-prompts.md)` | **Writing Guide** | Original analysis | — |
| 1 | `[01-openai-codex-cli.md](01-openai-codex-cli.md)` | **OpenAI Codex CLI** | [Official repo](https://github.com/openai/codex) | 12KB |
| 2 | `[02-opencode.md](02-opencode.md)` | **OpenCode** | [Official repo](https://github.com/anomalyco/opencode) | 13KB |
| 3 | `[03-hermes-agent.md](03-hermes-agent.md)` | **Hermes Agent** | [Official repo](https://github.com/NousResearch/hermes-agent) | 23KB |
| 4 | `[04-openclaw.md](04-openclaw.md)` | **OpenClaw** | [Official repo](https://github.com/openclaw/openclaw) | 31KB |
| 5 | `[05-aider.md](05-aider.md)` | **Aider** | [Official repo](https://github.com/Aider-AI/aider) | 27KB |
| 6 | `[06-swe-agent.md](06-swe-agent.md)` | **SWE-agent** | [Official repo](https://github.com/SWE-agent/SWE-agent) | 43KB |
| 7 | `[07-claude-code.md](07-claude-code.md)` | **Claude Code** | [Community extracted](https://github.com/dontriskit/awesome-ai-system-prompts) | 23KB |
| 8 | `[08-cursor.md](08-cursor.md)` | **Cursor** | [Community extracted](https://github.com/dontriskit/awesome-ai-system-prompts) | 15KB |
| 9 | `[09-windsurf.md](09-windsurf.md)` | **Windsurf** | [Community extracted](https://github.com/dontriskit/awesome-ai-system-prompts) | 18KB |

**Total: ~205KB of real-world production prompts**

## Sourcing

- **01–06**: Extracted directly from **official open-source repositories** on GitHub
- **07–09**: Extracted from [awesome-ai-system-prompts](https://github.com/dontriskit/awesome-ai-system-prompts), a community collection of reverse-engineered/leaked prompts from commercial AI tools

## Key Patterns Across All Agents

1. **Identity anchoring** — Every prompt opens with a clear "You are X" statement
2. **Negative constraints** — "NEVER do X" is more effective than "try to be good"
3. **Brevity enforcement** — Concrete rules + few-shot examples, not just "be concise"
4. **Tool-first mentality** — "Act, don't describe" is universal
5. **Safety guardrails** — Git safety, secrets protection, anti-destructive commands
6. **Convention awareness** — "Learn the codebase style, don't impose your own"
7. **Provider-specific tuning** — Claude and GPT need different instructions
8. **Layered architecture** — Identity → Project context → Session memory

## Start Here

👉 Read **`[00-how-to-write-system-prompts.md](00-how-to-write-system-prompts.md)`** — a 12-principle guide distilled from analyzing all 9 prompts.

## License

This repository is for **educational purposes only**. All system prompts remain the intellectual property of their respective creators. Community-extracted prompts (Claude Code, Cursor, Windsurf) are included under fair use for research and education.
