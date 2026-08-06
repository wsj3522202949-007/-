---
id: tool-05602
type: tool
area: 库
status: active
tags: [TTS, Claude插件, 协议宽松, 本地优先, 英文文档, 本地写作]
title: ai-pattern-detector
summary: 小说转语音/有声书
source: https://github.com/ananas-agency/ai-pattern-detector
created: 2026-07-18
updated: 2026-07-18
no: 5602
category: 一、去 AI 味 / Humanizer 库
repo: ananas-agency/ai-pattern-detector
stars: 4
url: https://github.com/ananas-agency/ai-pattern-detector
tier: "B"
use_case: "小说转语音/有声书"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ananas-agency/ai-pattern-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ananas-agency/ai-pattern-detector
- **Stars**：4
- **语言**：None
- **License**：MIT
- **Topics**：ai-detection, ai-detector, ai-writing, antropic, claude, llm, skill, text-analysis, writing-tool
- **GitHub 描述**：Claude Code plugin that flags AI-writing tells across 11 categories, scores text on a 0–100 "AI-feel" scale, and proposes before → after rewrites to make it sound human.
- **本地描述**：Claude Code plugin that flags AI-writing tells across 11 categories, scores text on a 0–100 "AI-feel" scale, and proposes before → after rewrites to make it sound human.
- **拉取时间**：2026-07-25 18:24:47

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Pattern Detector

A [Claude Code](https://docs.claude.com/en/docs/claude-code) plugin that scans text for
telltale AI-writing patterns and proposes specific rewrites to make it sound human.

It checks eleven categories of tells — telltale vocabulary, stock openers, signature
constructions, hedges, meta-commentary, closers, GPT artifacts, punctuation and formatting,
voice, structure, and engagement bait — scores the text on a 0–100 "AI-feel" scale, and
gives you concrete before → after rewrites for every finding.

It first identifies the text's register — social post, landing page, product description, blog,
scientific, business, or general — and calibrates what counts as a tell to match, so a product
description's feature list or a scientific paper's methods-passive isn't mistaken for AI.

## Install

Clone the repo and load it into Claude Code:

```
git clone https://github.com/ananas-agency/ai-pattern-detector
claude --plugin-dir ./ai-pattern-detector
```

Then ask Claude to "de-AI this draft." To keep it loaded across sessions, copy
`skills/ai-pattern-detector` into your `~/.claude/skills/` directory.

## Usage

Ask Claude to scan whatever you want checked. The skill triggers on requests like "make this
sound less like AI," "de-AI this," or "check this for AI patterns." It works on:

- text you paste directly,
- a file (`scan draft.md`),
- a URL (`check this post: …`),
- or a draft already in the conversation (`review what you just wrote`).

It scans prose written for humans — when a source mixes prose with code, config, or markup,
it scans the prose and leaves the rest alone.

**Language:** the plugin is built on English phrases and patterns, so it's designed for
scanning English text.

```
Scan this for AI patterns:

"In today's fast-paced world, leveraging cutting-edge solutions is no longer just an
option — it's a necessity. Let's delve into how businesses can unlock their full potential."
```

### Example output

```markdown
# AI Pattern Scan

**Verdict:** Heavy AI fingerprint: 5 strong tells across openers, vocabulary, and constructions.
**AI-feel score:** 71/100 — strong AI signature
**Counts:** Strong: 4 · Medium: 1 · Weak: 1 · Total: 6

## Findings

### 1. "In today's fast-paced world"
- **Pattern:** Stock opener
- **Severity:** Strong
- **Rewrite:** Cut it. Open on the actual claim: "Most teams already have the tools they need —"

### 2. "leveraging cutting-edge solutions"
- **Pattern:** Telltale vocabulary (`leverage`, `cutting-edge`)
- **Severity:** Strong
- **Rewrite:** "using the tools they already pay for"

### 3. "it's not just an option — it's a necessity"
- **Pattern:** Antithesis construction with pivot em-dash
- **Severity:** Strong
- **Rewrite:** Cut, or state the stake plainly: "Skip it and competitors close the gap."
```

Claude finishes by offering to apply every rewrite and hand back the clean full text.

## What it won't flag

Domain jargon you chose on purpose, parenthetical em-dashes in technical writing, bullets in
step-by-step instructions, passive voice in scientific or legal registers, and words like
"robust" used in their literal technical sense. The score is a density-of-evidence measure,
not a verdict on authorship — detectors are unreliable, and the skill says so. It also adapts to
register: it won't flag a product description's feature-adjective stack or a scientific paper's
methods-passive, which are native there.

## Structure

```
.claude-plugin/
  plugin.json                   # plugin manifest
skills/
  ai-pattern-detector/
    SKILL.md                    # workflow: register, metrics, scoring, output format
    references/
      patterns.md               # the eleven-category pattern catalog
      examples.md               # worked before → after rewrites, by pattern
    CHANGELOG.md
```

## License

[MIT](https://github.com/ananas-agency/ai-pattern-detector/blob/main/LICENSE) © Ananas Agency
