---
id: tool-00395
type: tool
area: 库
status: active
tags: [TTS, Claude插件, 协议未明, 本地优先, 英文文档, 本地写作]
title: realtime-voice-prompt
summary: 小说转语音/有声书
source: https://github.com/edubrigham/realtime-voice-prompt
created: 2026-07-18
updated: 2026-07-18
no: 395
category: 二、网文 / 长篇 AI 写作系统 库
repo: edubrigham/realtime-voice-prompt
stars: 0
url: https://github.com/edubrigham/realtime-voice-prompt
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# edubrigham/realtime-voice-prompt

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/edubrigham/realtime-voice-prompt
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI agent skill for writing voice prompts for OpenAI's Realtime API
- **本地描述**：AI agent skill for writing voice prompts for OpenAI's Realtime API
- **拉取时间**：2026-07-23 22:50:40

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Realtime Voice Prompt

AI agent skill for writing voice prompts for [OpenAI's Realtime API](https://platform.openai.com/docs/guides/realtime). Based on OpenAI's official Realtime Prompting Guide.

## Install

```bash
npx skills add edubrigham/realtime-voice-prompt
```

This installs the skill for your AI coding agent (Claude Code, Cursor, Windsurf, Copilot, etc.).

## What it does

Gives your AI coding agent expert knowledge on writing voice prompts:

- **Prompt structure** — sections, ordering, role/objective, personality/tone
- **Voice behavior** — speed, language constraints, variety, pronunciations, unclear audio handling
- **Tool design** — preambles, behavior types (proactive/confirmation/preambles), rephrase supervisor
- **Conversation flow** — static state machines, dynamic `session.update`, sample phrases
- **Safety & escalation** — when and how to hand off to a human

The skill triggers automatically when the agent is creating, editing, or reviewing voice prompts.

## Structure

```
SKILL.md                              # Core workflow + quick reference
references/
  prompt-sections.md                  # Detailed prompt section guidance
  tools-patterns.md                   # Tool design patterns
  conversation-flow.md                # Flow design patterns
```

## License

MIT
