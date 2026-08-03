---
id: tool-04967
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: humanize
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/bojanstef/humanize
created: 2026-07-18
updated: 2026-07-18
no: 4967
category: 一、去 AI 味 / Humanizer 库
repo: bojanstef/humanize
stars: 0
url: https://github.com/bojanstef/humanize
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# bojanstef/humanize

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/bojanstef/humanize
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Rewrite text so it reads as human-written and stops tripping AI-writing detectors (Claude Code skill).
- **本地描述**：Rewrite text so it reads as human-written and stops tripping AI-writing detectors (Claude Code skill).
- **拉取时间**：2026-07-25 18:01:16

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# humanize

A Claude Code skill that rewrites text so it reads as human-written and stops tripping AI-writing detectors.

It strips the tells catalogued in Wikipedia's "Signs of AI writing" (puffery, AI vocab, em dashes, the rule of three, negative parallelisms) and puts ordinary human texture back where they were.

## Usage

Drop this directory into `~/.claude/skills/` (or symlink it there), then ask Claude to "humanize" some text. Trigger phrases include "make it sound human", "remove AI tells", "de-AI this", and "pass AI detection".

## What's here

- `SKILL.md`: the skill definition and rewrite guidance
- `detect.py`: a regex scanner that flags those tells and scores any text
