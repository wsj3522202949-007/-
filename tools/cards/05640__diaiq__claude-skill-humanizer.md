---
id: tool-05640
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, 协议宽松, 本地优先, 英文文档, 本地写作]
title: claude-skill-humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/diaiq/claude-skill-humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5640
category: 一、去 AI 味 / Humanizer 库
repo: diaiq/claude-skill-humanizer
stars: 6
url: https://github.com/diaiq/claude-skill-humanizer
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 7612dfe1a73e395a
  - methods/改稿润色指令库.md
---

# diaiq/claude-skill-humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/diaiq/claude-skill-humanizer
- **Stars**：6
- **语言**：None
- **License**：MIT
- **Topics**：agent-skill, ai-humanizer, claude-code, claude-skill, gpt-zero, skills-sh
- **GitHub 描述**：Free Claude Code skill to humanize AI-generated text. Bypass GPTZero, Turnitin, and other AI detectors. Powered by DiaIQ.
- **本地描述**：Free Claude Code skill to humanize AI-generated text. Bypass GPTZero, Turnitin, and other AI detectors. Powered by DiaIQ.
- **拉取时间**：2026-07-25 18:26:13

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

![DiaIQ Humanizer](https://github.com/diaiq/claude-skill-humanizer/blob/main/banner-humanizer-high-res.png)

# Humanize AI Text — Claude Code Skill

Free Claude Code skill that humanizes AI-generated text so it passes GPTZero, ZeroGPT, Turnitin, Copyleaks, and other AI detectors.

Powered by [DiaIQ Humanizer](https://humanizer.diaiq.com) — no API key, no sign-up, no cost.

## Install

```bash
npx skills add diaiq/claude-skill-humanizer
```

## Usage

Once installed, just ask Claude to humanize text naturally:

```
humanize this text: Your AI-generated content here...
```

Or use the slash command:

```
/humanize Your AI-generated content here...
```

You can also point it at a file:

```
/humanize path/to/article.md
```

## What it does

- Rewrites ChatGPT, Claude, Gemini, Copilot, or any AI-generated text to sound human
- Passes GPTZero, ZeroGPT, Turnitin, Copyleaks, and other AI content detectors
- Preserves meaning, facts, and formatting (headings, lists, markdown)
- Supports 1-3 humanization passes for deeper rewriting

## How it works

The skill calls the free [DiaIQ Humanizer API](https://humanizer.diaiq.com/api/humanize). No authentication required. Your text is sent to the API, humanized using a fine-tuned local AI model, and returned directly in your terminal.

## About DiaIQ

[DiaIQ](https://diaiq.com) converts video recordings into blog posts, newsletters, social media posts, and more. The humanizer was originally built for our own content pipeline and is now available as a free public tool.
