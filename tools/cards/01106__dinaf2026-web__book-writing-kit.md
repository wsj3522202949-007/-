---
id: tool-01106
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 英文文档, 大纲规划, 本地写作]
title: book-writing-kit
summary: 搭大纲/分卷/节拍
source: https://github.com/dinaf2026-web/book-writing-kit
created: 2026-07-18
updated: 2026-07-18
no: 1106
category: 二、网文 / 长篇 AI 写作系统 库
repo: dinaf2026-web/book-writing-kit
stars: 0
url: https://github.com/dinaf2026-web/book-writing-kit
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# dinaf2026-web/book-writing-kit

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/dinaf2026-web/book-writing-kit
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A fiction-first co-authorship framework for writing books with AI. Full pipeline: brainstorm → world-building → character bible → outline → draft → revision → publish. Genre-flexible. MIT licensed. Built around a three-round creative loop that pushes past the obvious answer. QUILL is your on-demand AI ghost writer. You direct. QUILL executes.
- **本地描述**：A fiction-first co-authorship framework for writing books with AI. Full pipeline: brainstorm → world-building → character bible → outline → draft → revision → publish. Genre-flexible. MIT licensed. Built around a three-round creative loop that pushes past the obvious answer. QUILL is your on-demand AI ghost writer. You direct. QUILL executes.
- **拉取时间**：2026-07-23 23:11:18

---

# book-writing-kit

A fiction-first co-authorship framework for writing books with AI — from seed idea to revised manuscript and publication prep.

Built by [BookWeaver Publishing](https://bookweaverpublishing.com). Powered by Claude.

---

## Philosophy

**You are the director. QUILL executes.**

This kit does not write your book for you. It gives you a structured workspace where you bring the ideas, the voice, and the creative decisions — and your AI writing partner (QUILL) drafts, refines, pushes harder, and goes further out of the box on demand.

The creative loop at the heart of this kit applies to high-leverage creative decisions: premise, character, structure, scene solutions, hooks, revision fixes, and moments where the obvious answer is not enough.

1. QUILL gives the unexpected answer — not the obvious one
2. You push harder → QUILL throws it out and goes further
3. QUILL automatically adds one rule-breaking idea — the version that might be too wild but opens a door

Round 3 is required for ideation and creative problem-solving. You reject it 9 times out of 10. The 10th time is where the best idea in the book comes from.

---

## How to Start a New Book

**Open `START-HERE.md` first.** It walks you through the first 10 minutes — what to copy, what to paste into Claude, and what to save afterward.

After that:

1. **Duplicate this repo** — rename it to your book title (e.g. `my-book-title`)
2. **Create a starter brain file** — copy `brain/_template-brain.md`, fill in what you know, save as `brain/[your-book].md`
3. **Open `TRACKER.md`** — it tells you exactly what stage you're in and what to do next
4. **Open the `PROMPT.md`** for that stage — paste it to Claude with your details
5. **Work through each stage** in order, saving outputs and updating `TRACKER.md` as you go

You do not need a complete brain file before Stage 00. Start sparse. Stage 00 helps you lock the premise and emotional core.

---

## How QUILL Uses Your Files

QUILL can only use files that are available in the chat or tool environment you are using.

- **Manual chat:** paste the relevant brain file, tracker notes, and stage prompt into the chat.
- **Claude Project or file-enabled chat:** attach this repo or the files for the current stage.
- **Local agent workflow:** point QUILL at the repo and let it read `TRACKER.md`, the brain file, and the current stage files directly.

If QUILL cannot access a file, it should ask for exactly one missing file or excerpt rather than pretending it has read it.

---

## Stages

| Folder | Stage | What happens | Done when |
|---|---|---|---|
| `00-brainstorm/` | Seed → Premise | You throw an idea. QUILL generates, you refine, you bounce back and forth | `premise.md` is locked and the brain file has an emotional core |
| `01-world-and-rules/` | World & Genre Rules | Setting, atmosphere, genre conventions you keep and break | `world.md` and `genre-rules.md` are updated |
| `02-character-bible/` | Character Bible | Full cast profiles, opposition / pressure source deep dive, relationship map, voice guide | Major characters have profiles and distinct voices |
| `03-outline/` | Outline | Beat sheet, plot structure, timeline, midpoint, reader promises | `chapter-beats.md`, `timeline.md`, and `reader-promises.md` are usable |
| `04-draft/` | Draft | Chapter by chapter — QUILL drafts, you direct, redirect, or push harder | All chapters exist and `continuity-tracker.md` is current |
| `05-revision/` | Revision | Plot audit, line edit, fresh eyes pass | Structural fixes, line edits, and fresh-eyes notes are resolved |
| `06-publish/` | Publication Prep *(optional — separate from the creative workflow)* | Back cover, query letter, KDP metadata, pre-publish checklist | Metadata, copy, formats, and checklist are complete |

---

## What Else Is In Here

- `START-HERE.md` — The first 10 minutes. Open this before anything else.
- `brain/` — Your series bible or book brain. QUILL loads this before every session.
- `craft/` — Reference sheets for key writing craft techniques: scene construction, subtext, misdirection, pacing, atmosphere, chapter endings, protagonist balance.
- `vault/` — Cut file, title vault, research tracker, decision log. Cuts hurt — do them anyway. Nothing disappears without a record.
- `genres/` — Genre packs with sharper prompts for specific forms. Mystery pack included.
- `example/` — Full walkthrough of the framework using a fictional project (The Lavender Cipher).
- `QUILL.md` — Instructions for using QUILL as your on-demand ghost writer.
- `SESSION.md` — Start every session here. Solves the memory gap.
- `STAGE-GATES.md` — Exit criteria for every stage. Use this before moving forward.
- `PROMPTS.md` — Every available prompt indexed by what you need right now.
- `AI-TRANSPARENCY.md` — What AI does well, what the writer owns, what to verify.
- `TRACKER.md` — Your master status document. Always know where you are.

> **On the publishing stage:** `06-publish/` is included for writers who self-publish or prepare their own submissions. If you are working with a traditional publisher or agent, treat it as a reference rather than part of the writing workflow. The creative apparatus ends at Stage 05.

---

## Genre Flexibility

This kit is strongest for plot-driven fiction — mystery, thriller, fantasy, romance, speculative fiction, historical fiction, literary fiction with a clear narrative engine — and can be adapted for other forms. Every prompt uses variables like `[GENRE]`, `[SETTING]`, `[NUMBER OF PROTAGONISTS]` that you fill in at the start of each book.

If you are writing memoir, nonfiction, poetry, or an experimental form, treat the stage prompts as a starting structure rather than a rulebook.

---

## Built With

- [Claude](https://claude.ai) — AI co-author
- [BookWeaver Publishing](https://bookweaverpublishing.com) — indie publishing framework

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## License

MIT — free to use, fork, and adapt. See `LICENSE`.
