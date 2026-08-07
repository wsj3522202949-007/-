---
id: tool-07422
type: tool
area: 库
status: active
tags: [多Agent, Claude插件, 协议未明, 需API密钥, 英文文档]
title: claude-novel-workflow
summary: 多 Agent 协作自动产文
source: https://github.com/mintotsukino/claude-novel-workflow
created: 2026-07-18
updated: 2026-07-18
no: 7422
category: 画龙补充 / 扩容入库 — 补充源
repo: mintotsukino/claude-novel-workflow
stars: 6
url: https://github.com/mintotsukino/claude-novel-workflow
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# mintotsukino/claude-novel-workflow

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/mintotsukino/claude-novel-workflow
- **Stars**：6
- **语言**：None
- **License**：NOASSERTION
- **Topics**：ai-writing, claude-code, creative-writing, fiction-writing, novel-writing, writing
- **GitHub 描述**：Canon-driven multi-agent Claude Code workflow for long-form fiction, with a real working novel as the example project.
- **本地描述**：claude-novel-workflow
- **拉取时间**：2026-07-25 19:21:24

---

# claude-novel-workflow

A canon-driven, multi-agent Claude Code workflow for long-form fiction writing — with a real, working project as the reference example.

Built and used by a Japanese light novel author (15+ traditionally published fantasy books, 1M+ views on a previous AI-assisted novel). This repo is the publishable snapshot of the workflow that produced **137,806 characters across 20 chapters in a single 96-minute Claude Code run** — at the author's own writing quality.

![claude-novel-workflow repository overview](https://github.com/mintotsukino/claude-novel-workflow/blob/main/docs/assets/repository-overview.png)

---

## What This Is

Three things, in one repo:

1. **A working example** (`example_project/`) — A real, in-progress 100-chapter web novel. 70 chapters drafted on the author's machine (~455,000 Japanese characters); **the public copy includes the prose, briefs, plots, and scene cards for ep001–ep010**, plus the full canon snapshot at ep070 state, one batch review (ep002–ep006), and the full style engine. ep011–ep070 prose is held back for spoiler reasons.
2. **English-language templates** (`templates/`) — Blank versions of every canon and per-episode file, with guidance comments. Use these to start your own project.
3. **Documentation** (`docs/`) — Philosophy, architecture, getting started, three-layer review system, how to adapt the example, case study with real numbers.

---

## What This Is Not

- **Not a template you copy and fill in.** The example project's contents are story-specific. The architecture transfers; the contents don't.
- **Not a "press a button, get a novel" tool.** It's a structured, iterative workflow that requires you to build canon, exercise judgment, and polish drafts by hand.
- **Not a maintained product.** This is a published snapshot of a real working project. It will not receive ongoing updates or feature releases. Fork it freely.

---

## Who This Is For

You'll get value from this if you're:

- A novelist (published or aspiring) experimenting seriously with AI-assisted writing.
- Comfortable with markdown files and a terminal.
- Willing to spend a few days building canon before drafting prose.
- Using Claude Code (Pro, Max, or API access).

You won't get value if you want:

- An AI that writes a novel from a one-line prompt.
- A finished product without canon work.
- Generic prose that "sounds good" without any specific voice.

---

## The Core Idea

> AI doesn't write a novel. AI **drafts massively, in compliance with a canon you build.**

The bottleneck is not the prompt, the model, or the chat history. The bottleneck is the **canon**: a set of structured files that define your story's "physical laws":

- `canon.md` — The engine. What makes this story THIS story (hard rules, story-level promises, index).
- `character_bible.md` — Who exists, how they talk, what they're called.
- `world_bible.md` — Physical, social, magical rules.
- `glossary.md` — Every term, locked.
- `timeline.md` — Events in order, foreshadowing ledger.
- `style_guide.md` — How your prose sounds.
- `forbidden_patterns.md` — What your prose will never do.

Build these well, and a competent AI agent can draft 20 chapters in your voice. Skip them, and you get the generic AI prose everyone complains about.

See [`docs/PHILOSOPHY.md`](https://github.com/mintotsukino/claude-novel-workflow/blob/main/docs/PHILOSOPHY.md) for the full argument.

---

## Bonus: The JET Story-Design Framework

Most repos like this stop at "here's the pipeline." This one includes the **author's story-design framework** itself — the thing the pipeline is building toward.

**JET is an original story-design framework in the tradition of operational craft systems like Save the Cat or the Three-Act Structure** — one author's working theory, developed across 15+ traditionally published light novels plus an AI-assisted novel that surpassed 1M views. Unlike Save the Cat (which describes story shape), JET models the *reader's emotional state* across the story — what emotions are being fed, in what mix, at what tempo.

JET was originally optimized for the Japanese web-fiction market (Kakuyomu, Narou), but the underlying model is genre-agnostic. The 7-variable reader-emotion model, the 11 universal rules, the 4 OS-class engine archetypes — all of it will likely improve a story written in any language for any audience.

**Crucially: JET is operational.** Every variable in the model can be scored on a chapter by an AI agent (or a human reviewer). This is what makes it usable as a quality-evaluation tool inside the multi-agent pipeline — when an AI judges whether a draft is "good," it needs an explicit framework to judge against. JET is that framework in this project.

See [`docs/JET_OS_PRIMER.md`](https://github.com/mintotsukino/claude-novel-workflow/blob/main/docs/JET_OS_PRIMER.md) for the full primer — variables, rules, OS classes, and how to use the framework as both an authoring tool and an AI-evaluation scaffold.

---

## Bonus: AI Draft vs. Human-Polished Versions, Side by Side

`example_project/07_draft/` contains **two parallel versions of the first 10 chapters**:

- **`episodes/ep001.md` – `ep010.md`** — The **raw AI-generated drafts** as the multi-agent pipeline produced them.
- **`episodes_polished/ep001.md` – `ep010.md`** — The **human-polished final versions** as actually published on Kakuyomu, with the explicit "AI本文利用" (AI-text-used) tag.

Read them side by side and the slogan stops being marketing:

> **AI replaces the typing, not the writing.**

You'll see what the 30–60 min/chapter polish step actually changes — sentence-level rhythm, voice nuance, ending beats, the careful trimming of AI's safety-net verbosity. The structural skeleton is the AI's; the prose's *feel* is the human's. Both stages are necessary; neither is sufficient.

This is the most operational answer we know to "but is it actually any good if AI helps write it?" — the work has 32,982 published characters and a real reader audience to prove the answer.

---

## Quick Tour

```
claude-novel-workflow/
├── README.md             ← you are here
├── CLAUDE.md             ← instructions for Claude Code in this repo
├── LICENSE
│
├── docs/                 ← philosophy, architecture, how-to guides
│
├── example_project/      ← real working project (Japanese)
│   ├── 90_canon/         ← canon files (reflect ep070 state)
│   ├── 92_style_engine/  ← style + forbidden patterns (20 rules)
│   ├── 07_draft/         ← writing briefs + prose for ep001–ep010 (first 10 of 70 drafted chapters made public; rest withheld for spoiler reasons)
│   ├── 08_review/        ← one real batch review (ep002–ep006) as a worked example
│   └── ...
│
└── templates/            ← English-language blank templates (mirrors example_project structure)
    ├── CLAUDE.md         ← Claude Code instructions (at project root when forked)
    ├── UNIVERSAL_PROMPT.md  ← prompt for any chat AI (paste as system prompt)
    ├── GPTS_GEMS_PROMPT.md  ← prompt for OpenAI GPTs / Google Gems
    ├── 00_meta/          ← project brief, decision log, AI work log
    ├── 01_theme/         ← theme, genre OS, reader OS
    ├── 02_logline/       ← logline, synopsis, title, blurb
    ├── 03_project_design/ ← project design, emotion curve, characters/world/systems
    ├── 04_chapter_design/ ← arc index, arc design
    ├── 05_scene_cards/   ← scene cards template
    ├── 06_plot/          ← plot template
    ├── 07_draft/         ← writing brief template + episodes/
    ├── 08_review/        ← batch review template
    ├── 09_revision/      ← revision plan, revision log
    ├── 90_canon/         ← character bible, world bible, glossary, timeline, canon
    ├── 91_jet_engine/    ← JET-OS variables, selected OS, project JET design
    ├── 92_style_engine/  ← style guide, forbidden patterns, voice samples
    ├── 93_data/          ← analysis, market, reference subfolders
    ├── 93_exports/       ← handoff brief templates
    ├── _INBOX/           ← drop-zone for raw manuscript and reference materials
    ├── _workflows/       ← 5 operational workflows (import, update, revision, audit, handoff)
    └── config/           ← project.yml, workflow.yml, ai_roles.yml
```

---

## How to Start

### If you want to study the example first

Read in this order:

1. [`docs/PHILOSOPHY.md`](https://github.com/mintotsukino/claude-novel-workflow/blob/main/docs/PHILOSOPHY.md) — Why the approach works.
2. [`docs/ARCHITECTURE.md`](https://github.com/mintotsukino/claude-novel-workflow/blob/main/docs/ARCHITECTURE.md) — How the folders are organized and why.
3. [`docs/JET_OS_PRIMER.md`](https://github.com/mintotsukino/claude-novel-workflow/blob/main/docs/JET_OS_PRIMER.md) — The story-design framework the pipeline targets.
4. [`example_project/README.md`](example_project/README.md) — Tour of the working project.
5. [`docs/THREE_LAYER_REVIEW.md`](https://github.com/mintotsukino/claude-novel-workflow/blob/main/docs/THREE_LAYER_REVIEW.md) — How chapter review actually works.
6. [`docs/CASE_STUDY.md`](https://github.com/mintotsukino/claude-novel-workflow/blob/main/docs/CASE_STUDY.md) — Real numbers from real sprints.

### If you want to start your own project

This repo supports **two starting paths**, depending on what you bring:

**Path A: Fresh start (no existing materials yet)**

You're starting a novel from zero. No manuscript, no notes, just an idea.

1. [`docs/GETTING_STARTED.md`](https://github.com/mintotsukino/claude-novel-workflow/blob/main/docs/GETTING_STARTED.md) — Step-by-step from empty folder to first drafted chapter.
2. [`docs/HOW_TO_ADAPT.md`](https://github.com/mintotsukino/claude-novel-workflow/blob/main/docs/HOW_TO_ADAPT.md) — What to copy from the example, what to throw away, what to adapt.

Typical sequence:

1. Create a fresh folder outside this repo (or use `cp -r templates/ my-novel/` to bootstrap from the complete template skeleton).
2. The AI instruction file (`templates/CLAUDE.md`) is already at the template root — copy it to your project root.
3. Open Claude Code in the folder. Run `init`.
4. Ask Claude to interview you to fill in the canon files (start with `90_canon/` and `92_style_engine/`, dropping the `.template` from filenames).
5. Write your first 5 chapters by hand, with Claude's help.
6. Only then consider building a multi-agent pipeline.

(Codex users: copy `CLAUDE.md` to `AGENTS.md` — the instructions are environment-agnostic.)

**Path B: Existing manuscript (you already have material)**

You have a partial or complete manuscript, plus scattered notes — and you want to organize it into a canon-driven project.

1. [`docs/EXISTING_PROJECT_IMPORT.md`](https://github.com/mintotsukino/claude-novel-workflow/blob/main/docs/EXISTING_PROJECT_IMPORT.md) — Bootstrap process for importing existing work.
2. [`docs/HOW_TO_ADAPT.md`](https://github.com/mintotsukino/claude-novel-workflow/blob/main/docs/HOW_TO_ADAPT.md) — Same adaptation guide as Path A.

Typical sequence:

1. Create a fresh folder outside this repo.
2. Copy the full `templates/` directory into it.
3. Drop all your existing materials (manuscript, notes, settings) into `_INBOX/`.
4. Open Claude Code in the folder.
5. Run **Workflow 01 (First Import)** — the AI organizes the materials into the canon-driven structure.
6. Resolve any `TODO_CONFIRM` items the AI flagged.
7. From here, treat it like a Path A project.

The five workflows (First Import, Incremental Update, Revision, Canon Audit, Handoff) live in `templates/_workflows/`. They're the operational verbs of a canon-driven project — keep them handy.

---

## What's in the Example That You Won't Get from the Templates

The templates are clean starting points. The example project is what 70 chapters of actual practice produces — though the **public copy only ships a representative slice**:

- A `forbidden_patterns.md` with 20 rules refined across all 70 chapters of drafting (full file included).
- A `character_bible.md` with inter-character calling rules tables, layered naming conventions (4-layer misperception structure), and special speaker-target pairings (full file included, reflects ep070 state).
- **Real writing briefs for ep001–ep010** (10 of 70 — the rest are held back to avoid spoilers).
- **One real batch review** (`ep002-ep006_batch_review.md`) as a worked example of what multi-lens review actually catches. Other sprint reviews exist in the author's working copy but contain spoilers for later arcs.
- A `91_jet_engine/` folder containing the author's working version of the JET reader-emotion model (full file set included; idiosyncratic but instructive).

The example is here to be studied, not copied. The templates are here to be filled in.

---

## Background

The original Reddit post that introduced this workflow (with discussion in the comments):

**[r/WritingWithAI — Published novelist (15+ fantasy books, 1M+ views on a fully AI-written work). Got Claude Code to generate 137,806 characters across 20 chapters in one prompt — at my own writing quality.](https://www.reddit.com/r/WritingWithAI/comments/1u6g6e4/published_novelist_15_fantasy_books_1m_views_on_a/)**

The post hit 130+ upvotes and 90+ comments within 24 hours, dominating the top of the subreddit. Much of the deeper technical discussion happens in the comments. This repo is the codebase counterpart — what was described prose-only in the post, you can now read as actual files.

> **Note on the post title's phrase "fully AI-written"**: this refers to the **prose generation step** — the multi-agent pipeline produces complete chapter prose without human intervention during the run itself. The version that's *published to readers* still goes through 30–60 minutes of author polish per chapter. See the side-by-side comparison in `example_project/07_draft/episodes/` (AI drafts) vs `example_project/07_draft/episodes_polished/` (published versions), and `docs/PHILOSOPHY.md` for the framing: *"AI replaces the typing, not the writing."*

---

## A Note on the Previous 1M-View Work

The "1M+ views" novel referenced in the Reddit post and in the case study is a **different, earlier work** by the same author — not the example project in this repo. It used a less mature pipeline. The example project in this repo is the next iteration of the author's process.

The 1M-view proof point matters because it demonstrates that **AI-assisted fiction has a real audience** when the work is good and tagged honestly. The pipeline in this repo is what comes after taking that lesson and building infrastructure around it.

---

## License

- **The pipeline structure, templates, and documentation** are licensed under [CC BY 4.0](https://github.com/mintotsukino/claude-novel-workflow/blob/main/LICENSE) — adapt and build on it, with attribution.
- **The prose content** in `example_project/07_draft/episodes/` plus the story-specific contents of `example_project/90_canon/` remain the original author's copyrighted work and are not licensed for reuse, derivative works, or republication.

In short: **steal the architecture, don't steal the story.**

---

## Honest Disclaimer

A few things to keep in mind before you treat anything in this repo as authoritative:

- **This repo was built in collaboration with AI tools** (Claude Code in particular, plus conversational AI for ideation and drafting). The structure, the documentation, and most of the prose you're reading here are the result of human-AI collaboration, not solo human work. That's the same approach the repo describes — applied to the repo itself.
- **This is not "the best" template. It's one working example.** It reflects how one author (writing Japanese light novels in 2026) currently runs a long-form fiction project. The folder structure, the JET framework, the 5 workflows, the multi-lens review pipeline — all of it is **a snapshot of one practitioner's working method**, not an industry standard.
- **The repo will keep evolving on the author's machine** as new projects teach new lessons. What you see here is a point-in-time picture. Different genres, different scales, different goals will need different shapes. The author already runs slightly different variants per project.
- **Customize ruthlessly.** Your story is not the example story. Your voice is not the example voice. Your readers are not Kakuyomu readers. Treat every file in `templates/` as a starting point, not a recipe. Throw out what doesn't fit. Add what's missing. The structure exists to serve your work, not the other way around.
- **Treat this as reference, not gospel.** If something in this repo doesn't match what's working for you, trust what's working for you. Update your version. Ignore the rest.

The author shares this in the spirit of "here's what's working for me right now, take what helps." That's all the claim being made.

### 日本語まとめ

このリポジトリは AI と協働で開発したものです。「これが小説制作のベストなテンプレート」ではなく、**一人の作家がいまの時点で運用している構成の一例**にすぎません。著者側でも作品ごとに少しずつ変えていきますし、今後も変わり続けます。**自分のプロジェクトに合わせて、いいとこ取りして、合わないところは捨てて、自分の最適解を見つけてください**。あくまで参考に。

---

## Use & Warranty

### Use freely

The pipeline structure, templates, documentation, and workflow patterns in this repo are released under [CC BY 4.0](https://github.com/mintotsukino/claude-novel-workflow/blob/main/LICENSE). That means:

- **Personal use** — yes, freely.
- **Commercial use** — yes, freely. Use this in your indie author business, your studio, your publishing house. Build paid products on top of it. Sell novels you wrote with it.
- **Academic / educational use** — yes, freely. Teach with it, cite it in papers, build curricula on it.
- **Modification** — yes, freely. Adapt, extend, restructure, rename, gut whatever doesn't serve you.
- **Redistribution** — yes, freely, with attribution to the original (link this repo).

The only thing you can't do under this license is reuse the **prose content** in `example_project/07_draft/episodes/` and `episodes_polished/`, and the story-specific contents of `example_project/90_canon/` — those remain the original author's copyrighted creative work. See [LICENSE](https://github.com/mintotsukino/claude-novel-workflow/blob/main/LICENSE) for full terms.

In short: **the architecture is yours to take. The story isn't.**

### No warranty — use at your own risk

This repository is provided **"as is"**, with no warranty of any kind, express or implied. That includes (but isn't limited to):

- No warranty of fitness for any particular purpose
- No guarantee that using this pipeline will improve your writing, sell your novels, save you time, produce good output, or work at all in your environment
- No guarantee that the AI tools this pipeline depends on (Claude Code, Codex, etc.) will continue to behave as described
- No guarantee that the workflows will work without modification on your project, your machine, your operating system, your stack

**The author accepts no liability for any outcome of using this repository.** Including but not limited to:

- Lost time, lost work, lost revenue
- Data loss from automated pipeline runs
- Reputational harm from publishing AI-assisted work
- API costs incurred running pipelines
- Disputes with platforms, publishers, collaborators, or readers
- Any direct, indirect, incidental, consequential, or punitive damages

If you use this pipeline, you do so on your own judgment and at your own risk. Test on copies. Back up your work. Read the AI provider's terms. Read your publishing platform's terms. Make your own informed decisions.

### 日本語まとめ

**自由に使ってください** — 個人利用・商用利用・教育利用・改変・再配布、すべて自由です（attribution 必須、本文は対象外）。
**ただし無保証です** — このリポジトリは現状のまま提供されます。使用結果について、著者はいかなる責任も負いません(時間・収益・データ・評判・API費用・プラットフォームとの紛争などすべて含む)。使用は完全に自己責任で、自分のプロジェクトの判断とリスク許容範囲で運用してください。

---

## Spoilers

`example_project/` contains the full plot, character arcs, and 70 drafted chapters of an ongoing novel. Reading it spoils the story.

If you'd rather read the actual novel first, find it on Kakuyomu (Japanese only). Otherwise, treat the example as architectural reference rather than reading material.

---

## Contributing

This repo is not actively maintained. PRs may be reviewed slowly or not at all. Issues are welcome for clarification questions but will not drive ongoing development.

The recommended way to "contribute" is to **fork the repo, build your own canon-driven pipeline, and share what you learn** — with attribution back to this repo if it was useful.

related:
  - methods/QUICK_START.md
---

## Credits

Author: **MintoTsukino** — A Japanese light novel author publishing on Kakuyomu.

- GitHub: [@MintoTsukino](https://github.com/MintoTsukino)
- Reddit: [u/Quick_Impression7723](https://www.reddit.com/user/Quick_Impression7723/)

Pipeline development assistance: Claude (Anthropic), through extensive Claude Code sessions.

Inspired by the structured-pre-writing tradition in Japanese light novel craft, adapted for AI-assisted multi-agent workflows.
