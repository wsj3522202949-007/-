---
id: tool-04362
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 人物设定, RAG, 本地写作]
title: loregen
summary: 长篇人物/设定/伏笔一致性（RAG 记忆库）
source: https://github.com/shaderx/loregen
created: 2026-07-18
updated: 2026-07-18
no: 4362
category: 四、长篇一致性 / RAG / 故事圣经 库
repo: Shaderx/loregen
stars: 1
url: https://github.com/shaderx/loregen
tier: "B"
use_case: "长篇人物/设定/伏笔一致性（RAG 记忆库）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---

# Shaderx/loregen

- **分类**：四、长篇一致性 / RAG / 故事圣经 库
- **链接**：https://github.com/shaderx/loregen
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：An automatic lorebook generator for Sillytarvern.
- **本地描述**：An automatic lorebook generator for Sillytarvern.
- **拉取时间**：2026-07-25 17:44:23

---

# LoreGen

A lightweight lorebook entry generator for [SillyTavern](https://github.com/SillyTavern/SillyTavern). Scans chat messages for a keyword and uses an LLM to build a **permanent entity profile** — appearance, personality, skills, relationships — and saves it as a lorebook entry.

Designed to complement [OpenVault](https://github.com/AkaiRitsu/SillyTavern-OpenVault), which handles event memory. LoreGen handles **who and what things are**, not what happened.

## What It Does

You enter a keyword (a character name, location, object, etc.) and LoreGen:

1. Scans the chat for messages containing that keyword (whole-word, case-insensitive).
2. Sends the relevant messages to an LLM with a profiling prompt.
3. Creates or updates a lorebook entry with structured data fields (identity, appearance, personality, skills, relationships, rank) and a short prose blurb.

The entry focuses on **permanent attributes only** — no event summaries, no temporary state, no inventory. Things like scars or rank changes are recorded as attributes; the events that caused them are not.

## Features

- **Keyword-based scanning** — Whole-word matching, case-insensitive. Scans both user and character messages.
- **Smart updates** — If an entry for that keyword already exists, the LLM receives it as context and refines the profile with new information.
- **Batched processing** — If matched messages exceed the context limit, they are split into batches. Each batch is saved to the lorebook immediately, so progress is preserved if the LLM fails mid-way.
- **Resumable** — Processed message indices are stored in chat metadata. Re-running a keyword only processes new messages. If a batch fails at 3/7, batches 1-2 are already saved and the next run picks up from batch 3.
- **Connection profiles** — Select primary and backup LLM profiles via Connection Manager. Automatic failover if the primary fails.
- **Multi-entry resolution** — If a keyword matches multiple existing lorebook entries, a popup lets you choose which to update or create a new one.
- **Streaming console** — Real-time LLM output displayed in the settings panel.
- **Keyword history** — Shows which keywords have been processed for the current chat, with re-run and reset buttons.
- **Slash commands** — `/loregen keyword` and `/loregen-reset keyword` for automation.

## Installation

### Via SillyTavern's Extension Installer

Use the install URL:
```
https://github.com/Shaderx/loregen
```

### Manual Installation

Clone this repo into your SillyTavern third-party extensions folder:

```bash
cd SillyTavern/public/scripts/extensions/third-party
git clone https://github.com/Shaderx/loregen.git
```

Restart SillyTavern.

## Configuration

Open the **LoreGen** panel in the extensions sidebar. Settings:

| Setting | Default | Description |
|---------|---------|----------related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---|
| Target Lorebook | Chat Lorebook (auto) | Which lorebook to write entries to. Defaults to the chat-bound lorebook. |
| Extraction Profile | Current connection | Connection Manager profile for LLM calls. |
| Backup Profile | None | Fallback profile if the primary fails. |
| Max Entry Size | 500 chars | Maximum character length for the generated entry content. |
| Max Context / Batch | 16000 chars | Max characters of chat messages per LLM batch. |
| Context Window | 1 | Number of messages before/after each keyword match to include as context. |

## Usage

1. Open a chat that has some history.
2. In the LoreGen panel, type a keyword (e.g. a character name) and click **Generate**.
3. A confirmation popup shows the number of matches, target lorebook, and batch count. Confirm to proceed.
4. Watch the streaming console for LLM progress. Each batch is saved as it completes.
5. The lorebook entry appears in your selected lorebook.

To re-scan with new messages later, just run the same keyword again — only unprocessed messages are sent.

To start fresh for a keyword (e.g. after a bad generation), use the reset button in the keyword history or run `/loregen-reset keyword`.

## Entry Format

LoreGen produces human-readable entries with structured data fields and a short prose blurb:

```
[name: Marcus Vale
aliases: The Iron Wolf
titles: Knight-Commander
species: Human
age: 34
gender: Male
appearance: Tall, broad-shouldered, short dark hair, grey eyes, jagged scar across left cheek, missing right ear
personality: Stoic, Loyal, Short-tempered, Protective, Blunt
skills: Swordsmanship, Shield combat, Military tactics, Horseback riding
rank: Knight-Commander of the Western Order
relationships: Elena(Wife), Gareth(Squire), Lord Ashford(Liege lord), Sable(Rival)]
A battle-hardened knight known for his direct manner and unwavering loyalty. Commands respect through decades of frontline service, bearing the scars to prove it.
```

The profile adapts to entity type — characters get appearance/personality/skills, locations get architecture/occupants/reputation, objects get materials/properties/origin.

## File Structure

```
loregen/
├── manifest.json        # Extension metadata
├── index.js             # Entry point, UI init, slash commands
├── settings.html        # Settings panel template
├── style.css            # Extension styles
└── src/
    ├── constants.js     # Extension name, default settings
    ├── scanner.js       # Chat message scanning and batching
    ├── prompts.js       # LLM prompt construction
    ├── generator.js     # LLM orchestration, batch loop, parsing
    ├── lorebook.js      # World Info API integration
    └── ui.js            # Settings bindings, console, keyword history
```

## Requirements

- SillyTavern with Connection Manager support
- An LLM connection profile configured in SillyTavern

## License

MIT
