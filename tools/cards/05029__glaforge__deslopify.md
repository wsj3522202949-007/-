---
id: tool-05029
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: deslopify
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/glaforge/deslopify
created: 2026-07-18
updated: 2026-07-18
no: 5029
category: 一、去 AI 味 / Humanizer 库
repo: glaforge/deslopify
stars: 29
url: https://github.com/glaforge/deslopify
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# glaforge/deslopify

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/glaforge/deslopify
- **Stars**：29
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：A Gemini CLI skill to make text more genuine, natural, and free of AI tropes.
- **本地描述**：A Gemini CLI skill to make text more genuine, natural, and free of AI tropes.
- **拉取时间**：2026-07-25 18:03:30

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Deslopify Skill

A specialized skill for Gemini CLI that makes text more genuine, natural, and free of "AI slop" by identifying and removing common LLM writing tropes.

## Goal

The goal of this skill is to transform AI-generated or overly formal text into clear, direct, human-like prose. It helps you move away from the repetitive, patronizing, and grandiose patterns that often signal a piece was written by a machine.

## How it Works

The skill is grounded in the comprehensive [AI Writing Tropes](https://tropes.fyi/) list. It scans your text for anti-patterns such as:

- **Magic Adverbs:** Overuse of words like "quietly," "deeply," or "arguably."
- **The "Delve" Family:** Overused vocabulary like "leverage," "streamline," or "harness."
- **Pompous Constructions:** Patterns like "It's not X -- it's Y" or "The result? Devastating."
- **Structural Tics:** Bold-first bullets, em-dash addiction, and tricolon abuse.
- **Tone Issues:** Patronizing analogies ("Think of it as...") and grandiose stakes inflation.

## Usage

Once installed and reloaded, you can use the skill by asking Gemini CLI to "deslopify" or "naturalize" a piece of text or a URL.

### Example Commands:

- "Deslopify this article: [URL]"
- "Naturalize this draft: [Text content]"
- "Remove the AI slop from my README file."

## Installation

If you have the `.skill` file, you can install it using:

```bash
gemini skills install deslopify.skill --scope workspace
```

Then, reload your skills in your interactive session:

```bash
/skills reload
```

## Reference

This skill's stylistic rules are strictly based on the observations and research found at **[tropes.fyi](https://tropes.fyi/)**.
