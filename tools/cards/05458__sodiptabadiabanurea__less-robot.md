---
id: tool-05458
type: tool
area: 库
status: active
tags: [去AI味, TTS, 协议宽松, 本地优先, 英文文档, 本地写作]
title: less-robot
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/sodiptabadiabanurea/less-robot
created: 2026-07-18
updated: 2026-07-18
no: 5458
category: 一、去 AI 味 / Humanizer 库
repo: sodiptabadiabanurea/less-robot
stars: 1
url: https://github.com/sodiptabadiabanurea/less-robot
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: c00c9e5398e6ca2f
  - methods/改稿润色指令库.md
---

# sodiptabadiabanurea/less-robot

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sodiptabadiabanurea/less-robot
- **Stars**：1
- **语言**：None
- **License**：MIT
- **Topics**：ai-writing, hermes, humanizer, llm, prompt-engineering, technical-writing, writing-tools
- **GitHub 描述**：Humanizer skill and prompt pack for making AI writing sound natural without losing meaning or technical precision.
- **本地描述**：Humanizer skill and prompt pack for making AI writing sound natural without losing meaning or technical precision.
- **拉取时间**：2026-07-25 18:19:27

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

<p align="center">
  <img src="./assets/less-robot-hero-v2.svg" alt="less-robot hero illustration" width="420" />
</p>

<p align="center">
  <a href="https://github.com/sodiptabadiabanurea/less-robot/releases/tag/v1.1.0">
    <img src="https://img.shields.io/badge/release-v1.1.0-EA580C?style=for-the-badge&labelColor=111827" alt="Release v1.1.0" />
  </a>
  <a href="https://x.com/sodiptabb23?s=21">
    <img src="https://img.shields.io/badge/follow%20on%20X-1D9BF0?style=for-the-badge&logo=x&logoColor=white&labelColor=111827" alt="Follow on X" />
  </a>
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-2563EB?style=for-the-badge&labelColor=111827" alt="MIT License" />
  </a>
</p>

<h1 align="center">less-robot</h1>

<p align="center">
  <strong>Make AI writing sound human without losing meaning or technical precision.</strong>
</p>

<p align="center">
  A small prompt pack and Hermes skill for cleaning up robotic prose, matching voice when it helps, and staying conservative with technical docs.
</p>

<p align="center">
  Repo social preview asset: <code>assets/less-robot-social-preview.png</code>
</p>

## What this repo includes

- `SKILL.md`
  - the Hermes-native humanizer skill
- `templates/generic-humanize-prompt.md`
  - a reusable prompt for Claude, Codex, OpenCode, or other LLMs
- `templates/technical-humanize-prompt.md`
  - a safer prompt for technical writing
- `references/pattern-cheatsheet.md`
  - a fast checklist of common AI-writing tells
- `references/technical-checklist.md`
  - a verification checklist for technical rewrites
- `references/source-notes.md`
  - adaptation notes and attribution

## When to use it

Good fit for:
- blog drafts
- product copy that feels too corporate
- emails and internal writeups that sound too polished or synthetic
- technical docs, API docs, runbooks, postmortems, changelogs, and setup guides that need cleanup without changing commands, flags, numbers, or requirements

## Quick start

### Option 1: Use it in Hermes

Copy the files into a Hermes skill directory:

```text
~/.hermes/skills/productivity/humanizer/
  SKILL.md
  templates/
  references/
```

Then invoke it when you want to humanize text, reduce robotic tone, or clean up technical writing without losing precision.

### Option 2: Use it with any AI tool

Start with one of these prompt templates:
- `templates/generic-humanize-prompt.md`
- `templates/technical-humanize-prompt.md`

If the text contains commands, paths, versions, thresholds, or RFC-style words like `must`, `should`, and `may`, use the technical template first.

## What makes this different

A lot of AI-cleanup prompts overcorrect. They make text shorter, but also flatter, vaguer, or less accurate.

This repo tries to do the opposite:
- reduce the obvious AI smell
- keep specificity
- preserve technical meaning
- avoid forced slang or fake personality
- use voice matching only when it actually helps

## Before / after

### Before

> AI-assisted documentation serves as a crucial foundation for modern engineering workflows, enabling teams to streamline collaboration, enhance clarity, and ensure alignment across stakeholders.

### After

> AI can help teams write docs faster, especially for repetitive stuff. The problem is that the output often sounds polished without saying much. You still need someone to cut the filler and make the meaning clear.

That is the point of this repo: less brochure language, less fake polish, more real signal.

## Technical-safe mode

The technical flow is conservative by default.

It is designed to preserve:
- commands and flags
- code, config keys, filenames, paths, and URLs
- versions, dates, units, thresholds, and numbers
- modality words such as `must`, `should`, `may`, `required`, and `optional`
- repeated technical terms that should stay consistent

It still removes fluff, hype, and generic corporate padding. The point is to make technical writing cleaner, not warmer at the cost of accuracy.

## Suggested workflow

1. Classify the text: technical, business, or casual
2. If available, use a writing sample for voice matching
3. Remove obvious AI patterns and filler
4. Rewrite with simpler, more concrete phrasing
5. Run a final anti-AI pass
6. For technical text, verify that meaning and requirements did not change

## Example use cases

### Humanize a generic draft
Use `templates/generic-humanize-prompt.md` when the text is too polished, repetitive, or obviously machine-written.

### Clean up technical docs safely
Use `templates/technical-humanize-prompt.md` when the text contains:
- shell commands
- config examples
- API requirements
- incident notes
- setup instructions
- postmortem findings

Then verify the result with `references/technical-checklist.md`.

## Attribution

This repo adapts ideas from:
- blader/humanizer: https://github.com/blader/humanizer
- Wikipedia: Signs of AI writing / WikiProject AI Cleanup

The source repo is MIT-licensed.
This adaptation is also distributed under MIT. See `LICENSE`.
