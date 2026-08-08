---
id: tool-05250
type: tool
area: 库
status: active
tags: [大纲规划, TTS, 协议宽松, 本地优先, 英文文档, 本地写作]
title: book-writing-assistant
summary: 小说转语音/有声书
source: https://github.com/wakeband/book-writing-assistant
created: 2026-07-18
updated: 2026-07-18
no: 5250
category: 一、去 AI 味 / Humanizer 库
repo: wakeband/book-writing-assistant
stars: 0
url: https://github.com/wakeband/book-writing-assistant
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 5967ef544eadff95
  - methods/改稿润色指令库.md
---

# wakeband/book-writing-assistant

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/wakeband/book-writing-assistant
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Complete writing companion for book authors. Tracks characters, plot threads, chapters, world-building, and research with automatic contradiction detection. Brainstorms ideas, drafts passages, and helps with writer's block. Supports fiction and nonfiction.
- **本地描述**：Complete writing companion for book authors. Tracks characters, plot threads, chapters, world-building, and research with automatic contradiction detection. Brainstorms ideas, drafts passages, and helps with writer's block. Supports fiction and nonfiction.
- **拉取时间**：2026-07-25 18:11:37

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Book Writing Assistant

A conversational OpenClaw skill for book authors that combines project organization with creative writing support. Tracks characters, plot threads, chapter outlines, world-building, research, and continuity for both fiction and nonfiction projects. Also brainstorms, drafts passages, and helps push through writer's block.

## What It Does

### Organizer Mode
- **Character Bibles** -- full profiles with appearance, personality, backstory, motivation, arc, relationships, voice notes, and chapter appearances. Automatically flags contradictions across the manuscript.
- **Plot / Argument Threads** -- track throughlines with key beats, chapter references, and setup/payoff connections (fiction) or thesis, evidence, and counterarguments (nonfiction).
- **Chapter Outlines** -- status, summaries, POV, key events, word counts, and which threads advance in each chapter.
- **World-Building** -- locations, rules/systems, and in-story timelines (fiction).
- **Research Notes** -- topics, sources, key findings, and which chapters reference them.
- **Consistency Engine** -- cross-references new details against existing records and flags contradictions immediately.

### Writing Partner Mode
- **Brainstorming** -- generate ideas that fit the established characters, world, and plot.
- **Drafting** -- write passages that match the project's tone and voice.
- **Writer's Block** -- help find the next move by analyzing character dynamics and story structure.
- **Nonfiction Structure** -- outline arguments, build chapter frameworks, and draft sections.

## Example Usage

**Start a project:**
> "I'm starting a novel. Working title is 'The Hollow.' Literary fiction set in a small coastal town in Maine."

**Build a character:**
> "Elena is 33, dark hair, a journalist in Boston. She clicks her pen when she's thinking."

**Check consistency:**
> "Can you check if I've been consistent with Elena across chapters?"

**Brainstorm:**
> "I need a reason for Elena to stay in town longer than she planned."

**Draft a passage:**
> "Can you draft an opening paragraph for chapter 1? Elena is driving into town. It's foggy."

**Beat writer's block:**
> "I'm stuck on chapter 4. Elena just found out James knew her mother."

## Installation

Copy the `book-writing-assistant` folder into your OpenClaw skills directory and restart your agent.
