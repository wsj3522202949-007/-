---
id: tool-01010
type: tool
area: 库
status: active
tags: [TTS, 协议未明, 本地优先, 英文文档, 本地写作]
title: voice-ai-prompting-skill
summary: 小说转语音/有声书
source: https://github.com/dawood-akceleration/voice-ai-prompting-skill
created: 2026-07-18
updated: 2026-07-18
no: 1010
category: 二、网文 / 长篇 AI 写作系统 库
repo: dawood-akceleration/voice-ai-prompting-skill
stars: 0
url: https://github.com/dawood-akceleration/voice-ai-prompting-skill
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# dawood-akceleration/voice-ai-prompting-skill

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/dawood-akceleration/voice-ai-prompting-skill
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Claude Skill for writing perfect AI voice agent prompts — inbound or outbound, simple or complex. Interviews you through every building block: identity, personality, tools, call flow, and constraints. Drafts a production-ready system prompt for Vapi, Retell, Bland, and other voice AI platforms.
- **本地描述**：Claude Skill for writing perfect AI voice agent prompts — inbound or outbound, simple or complex. Interviews you through every building block: identity, personality, tools, call flow, and constraints. Drafts a production-ready system prompt for Vapi, Retell, Bland, and other voice AI platforms.
- **拉取时间**：2026-07-23 23:08:28

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# voice-ai-prompt-writer

A Claude Skill that interviews you through every building block of a good AI voice-agent prompt — Identity & Role, Voice & Personality, Tools, Call Flow, Constraints — then drafts a production-ready system prompt for platforms like Vapi, Retell, or Bland.

## What it does

1. Figures out the basics: new prompt vs. refining an existing one, inbound vs. outbound, which platform.
2. Runs a deep, one-question-at-a-time interview through all five building blocks.
3. Shares a bullet-point plan for you to confirm before writing anything.
4. Drafts the full prompt in raw markdown.
5. Saves it as a downloadable `.md` file and points you at the test-and-refine loop.

## Structure

```
voice-ai-prompt-writer/
├── SKILL.md                          # entry point: the workflow itself
├── references/
│   ├── interview-guide.md            # full question bank by building block
│   └── platform-notes.md             # Vapi & Retell templating conventions
└── assets/
    └── prompt-template.md            # blank skeleton used when drafting
```

## Install

Upload `SKILL.md` (with its folder) to Claude wherever skill installation is enabled — or upload the whole folder to a Claude conversation and ask it to write you a voice agent prompt.

## License

Internal use — adapt freely for your own workflow.
