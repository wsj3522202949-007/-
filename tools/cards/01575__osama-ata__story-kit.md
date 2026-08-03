---
id: tool-01575
type: tool
area: 库
status: active
tags: [大纲规划, Python, 协议未明, 需API密钥, 英文文档]
title: story-kit
summary: 搭大纲/分卷/节拍
source: https://github.com/osama-ata/story-kit
created: 2026-07-18
updated: 2026-07-18
no: 1575
category: 二、网文 / 长篇 AI 写作系统 库
repo: osama-ata/story-kit
stars: 0
url: https://github.com/osama-ata/story-kit
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# osama-ata/story-kit

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/osama-ata/story-kit
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：StoryKit is an open-source, AI-powered CLI framework designed to bring Parametric Storytelling and Structured Drafting to creative writing.
- **本地描述**：StoryKit is an open-source, AI-powered CLI framework designed to bring Parametric Storytelling and Structured Drafting to creative writing.
- **拉取时间**：2026-07-23 23:25:00

---

# StoryKit

An AI-powered CLI framework for **Parametric Narrative Architecture** — separating story structure from prose generation so you act as the Showrunner while AI handles the Writers' Room.

## How it works

StoryKit enforces a five-phase pipeline. Each phase produces a Markdown artifact that the next phase consumes. Editing any file mid-project is supported — the framework adapts.

```text
Phase 1  storykit bible      →  bible.md
Phase 2  storykit treatment  →  treatment.md
Phase 3  storykit outline    →  beat_sheet.md
Phase 4  storykit scenes     →  scene_cards.md
Phase 5  storykit draft      →  manuscript/chapter_*.md
         storykit sync       ←  reconciles manual edits back to architecture
```

## Installation

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/osama-ata/story-kit
cd story-kit
uv sync
```

The `storykit` command is then available via `uv run storykit`.

## Quickstart

```bash
uv run storykit init mynovel
cd mynovel

uv run storykit bible       # define genre, tone, world rules
uv run storykit treatment   # premise, protagonist arc, themes
uv run storykit outline     # beat sheet (Save the Cat, Monomyth, etc.)
uv run storykit scenes      # granular scene cards as a checklist
uv run storykit draft       # AI drafts each scene, validates, retries
```

Every generation command shows a **rich diff** and asks `[Y/n]` before writing — you stay in control.

## LLM configuration

On `storykit init` you choose the model. StoryKit uses [LiteLLM](https://github.com/BerriAI/litellm), so any supported provider works:

| Provider | Model string example |
| --- | related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- |
| Anthropic | `anthropic/claude-3-5-sonnet-20241022` |
| OpenAI | `openai/gpt-4o` |
| Google | `gemini/gemini-1.5-pro` |
| Local (Ollama) | `ollama/llama3` |

Set the appropriate API key as an environment variable (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, etc.) before running any generation command.

To change the model after init, edit `.storykit/config.json`.

## Commands

### `storykit init <name>`

Creates the project directory:

```text
<name>/
├── .storykit/
│   ├── config.json   # model selection
│   └── state.json    # SHA-256 hashes for drift detection
├── manuscript/       # generated prose
├── quarantine/       # scenes that failed validation
├── bible.md
├── treatment.md
├── beat_sheet.md
└── scene_cards.md
```

### `storykit bible`

Prompts for genre, themes, and constraints. Generates `bible.md` — the absolute rule document for every subsequent step.

### `storykit treatment`

Reads `bible.md`. Prompts for premise and protagonist. Generates `treatment.md` with the emotional arc and thematic motifs.

### `storykit outline`

Reads `bible.md` + `treatment.md`. Applies a structural framework (Save the Cat, Freytag, Monomyth…) to produce `beat_sheet.md`.

### `storykit scenes`

Reads all prior files. Generates `scene_cards.md` — a markdown checklist where each line is one actionable scene card:

```text
- [ ] [Ch.1] Scene 1: Forest path. Kira enters alone. Strange sound triggers unease. Polarity: Curious→Fearful. Exposition: Establish recklessness.
```

### `storykit draft`

The main loop. For each unchecked `- [ ]` card:

1. Builds the **Context Sandwich** — `<story_bible>`, `<macro_structure>`, `<current_scene_task>`, `<previous_context>` — wrapped in XML tags
2. Forces a `<continuity_check>` before the LLM writes prose (anchors rules in active memory)
3. Extracts the `<manuscript>` block
4. Runs a **Validation Hook** — a second LLM call scores continuity, tone adherence, and show-don't-tell (all must be ≥ 7/10)
5. If validation fails, sends editorial feedback to a revision pass and retries (default: 3 attempts)
6. On final failure, saves to `quarantine/` and stops
7. Marks the card `- [x]` and appends prose to `manuscript/chapter_N.md`

The loop is **idempotent** — `storykit draft` always resumes from the first unchecked card.

Options:

```text
--max-retries INT     Validation retry limit (default: 3)
--no-validate         Skip the validation hook
--all                 Draft all remaining scenes without pausing
--scenes-per-chapter  Scenes per chapter file (default: 5)
```

### `storykit sync`

Run this after manually editing any `manuscript/chapter_*.md` file.

1. Compares SHA-256 hashes of manuscript files against `.storykit/state.json`
2. Extracts modified content
3. Runs a **Continuity Editor** LLM pass to detect narrative drift (new characters, changed rules, plot shifts)
4. Presents proposed patches to `bible.md` and `beat_sheet.md`
5. Applies them only on `[Y]` confirmation

This closes the loop: you can steer the story from the architecture (top-down) or from the prose (bottom-up), and the framework keeps everything coherent.

## Architecture

```text
storykit/
├── main.py          # Typer CLI — all commands
├── core/
│   ├── prompts.py   # system prompts for every phase
│   ├── context.py   # context compiler (Context Sandwich builder)
│   └── llm.py       # LiteLLM wrapper + JSON extraction
└── utils/
    ├── file_io.py   # read/write/hash/JSON helpers
    └── parser.py    # checkbox parser, XML block extractor
```
