---
id: tool-00618
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 英文文档, 大纲规划, 本地写作]
title: Creative-writing-skill
summary: 搭大纲/分卷/节拍
source: https://github.com/xbraindance/creative-writing-skill
created: 2026-07-18
updated: 2026-07-18
no: 618
category: 二、网文 / 长篇 AI 写作系统 库
repo: xbraindance/Creative-writing-skill
stars: 1
url: https://github.com/xbraindance/creative-writing-skill
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# xbraindance/Creative-writing-skill

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/xbraindance/creative-writing-skill
- **Stars**：1
- **语言**：None
- **License**：MIT
- **Topics**：creative-writing
- **GitHub 描述**：I skill to craft full stories, ideas, character sketches and plot outlines. Provides tools for every part of the writing process. Every draft auto-files into a persistent wiki for easy follow-up. Natural language interface.
- **本地描述**：I skill to craft full stories, ideas, character sketches and plot outlines. Provides tools for every part of the writing process. Every draft auto-files into a persistent wiki for easy follow-up. Natural language interface.
- **拉取时间**：2026-07-23 22:57:05

---

# Creative Writing with Verbalized Sampling

**TLDR:** I skill to craft full stories, ideas, character sketches and plot outlines. Provides tools for every part of the writing process. Every draft auto-files into a persistent wiki for easy follow-up. Natural language interface. 

Brainstorm (/brainstorm) → Define (/grill-me) → Structure (/plan) → Create (/write, /sketch) → Writers block/Unstick (/help) → Evaluate (/critic) → Refine (/write again).

A client-agnostic skill that unlocks LLM diversity for creative writing using **Verbalized Sampling (VS)** — a training-free prompting strategy from Zhang et al. It also persists your work across sessions in a structured, queryable wiki, with **automatic character and setting detection**.


---

> **Research Foundation:** This skill is directly inspired by and built upon the work of **Jiayi Zhang, Simon Yu, Derek Chong, Anthony Sicilia, Michael R. Tomz, Christopher D. Manning, and Weiyan Shi** — authors of *"Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity"* (arXiv:2510.01171v3, 2025).
>
> **Knowledge Foundation:** This skill incorporates a per-project Writer's Wiki based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). See `llm-wiki.md` in this folder for the full wiki specification.



## Why Choose This Skill

**Three core advantages:**

1. **Escape mode collapse.** Most LLMs converge on the same stereotype when asked to brainstorm. This skill uses Verbalized Sampling to generate a diverse distribution of responses—5+ genuinely different takes on your prompt, each with a probability score. Ask for story ideas and get radically different premises, not variations on the same one.

2. **Nothing gets lost.** Every draft, character sketch, outline, and research page auto-files into a persistent wiki. You never lose an idea to chat history. Every session picks up where the last one ended. Characters and settings you mention are automatically detected and offered as wiki pages—your world-building grows *by itself* as you write.

3. **No configuration needed.** Just write naturally. The skill reads your language ("give me 5 wildly different openings" vs. "polish this paragraph") and adapts automatically—no `/set` flags, no template arguments, no hidden settings. You think in words; the skill thinks in prompts.

## Why This Exists

Post-training alignment makes LLMs safer but causes **mode collapse**: the model converges on stereotypical responses. Ask for 5 jokes, get the same joke 5 times.

**Verbalized Sampling** fixes this by asking the model to generate a **distribution of responses with probabilities** — no retraining.

**The Writer's Wiki** keeps every idea, draft, character, and setting organized and retrievable across sessions. And when you write a draft with a new character, the skill **spots them automatically** and offers to build a wiki page.

## Quick Start

### Installation

Install the `Creative Writing skill` folder in your client's skills directory. Consult your client's documentation for the exact path.

```bash
skill_view(name='creative-writing-verbalized-sampling')
```

### Starting a Project

```
User: "Start a new project called The Glass Forest"
→ Creates projects/the-glass-forest/ with SCHEMA.md, index.md, log.md
→ Asks about genre, tone, POV
→ Wiki is ready
```

### Just Write Naturally

Describe what you want. The skill figures out the rest and files everything automatically.

| You Say | What Happens |
|---------|-------------|
| "Give me lots of different story ideas about time travel" | Returns 10+ concepts; files in `brainstorm/` |
| "Write a polished poem about rain" | Returns 5 refined poems; files in `write/` |
| "Tell me about Elara Voss" | Generates diverse character takes; files in `characters/` |
| "What's The Forge City like?" | Generates atmospheric interpretations; files in `settings/` |
| "Plan out a mystery novel set in a bakery" | Returns plot outlines; files in `plan/` |
|| "What was I working on last time?" | Reads the wiki log and summarizes |
|| "I'm stuck on Chapter 3" | Diagnoses the blockage; offers 5 paths forward; files in `help/` |
|| "Critique my latest chapter" | Structured review with severity, evidence, fixes; files in `critic/` |

---

## Commands

### Writing Phase Commands

| Command | What it does | Wiki Folder | Natural Triggers |
|---------|-------------|-------------|------------------|
| `/plan` | Generate diverse outlines | `plan/` | "plan," "outline," "directions" |
| `/write` | Generate polished drafts | `write/` | "write," "draft," "story," "poem" |
| `/sketch` | Quick, unpolished drafts | `sketch/` | "sketch," "quick," "rough" |
| `/brainstorm` | Maximum diversity ideas | `brainstorm/` | "brainstorm," "ideas," "concepts" |

### Entity Commands

| Command | What it does | Wiki Folder | Natural Triggers |
|---------|-------------|-------------|------------------|
| `/character` | Generate diverse character interpretations | `characters/` | "who is," "tell me about [name]," "character sheet" |
| `/setting` | Generate diverse world-building takes | `settings/` | "describe [place]," "what's [place] like," "world-building" |
| `/theme` | Generate theme explorations | `themes/` | "explore the theme of," "symbolism of" |
| `/grill-me` | Structured story-definition interview | `plan/`, `characters/`, `settings/`, `themes/` | "help me plan," "i have an idea," "structure my novel" |

### Utility Commands

| Command | What it does |
|---------|-------------|
| `/world` | Show project overview: characters, settings, recent drafts, open threads |
| `/link` | Scan drafts for unlinked entities and suggest missing wiki pages |
| `/project "name"` | Switch to or create a project |
| `/lint` | Audit wiki for orphans, broken links, stale content |
| `/review` | Alias for `/world` — summarize project state |

### Support Commands

| Command | What it does | Wiki Folder | Natural Triggers |
|---------|-------------|-------------|------------------|
| `/help` | Diagnose blockage and offer targeted options to continue | `help/` | "i'm stuck," "what happens next," "this feels flat," "writer's block" |
| `/critic` | Structured critique of drafts with severity, evidence, and fixes | `critic/` | "critique," "review," "does this work," "what's wrong with" |
| `/research` | Web-sourced research on concept, audience, market, or comp titles | `research/` | "research X," "who reads X," "comp titles for X," "what's the market for X" |

---

## Automatic Character & Setting Detection

### How It Works

**After every draft is filed**, the skill silently scans the text for:
- **Named proper nouns:** "Elara Voss," "The Forge City," "Bernard the Bear"
- **Recurring capitalized terms:** Terms that appear 2+ times and aren't common words
- **Frontmatter hints:** `pov-character:` or `setting:` fields

For each detected entity, the skill checks if a wiki page exists. **If not, it generates a starting sketch and asks you:**

> "I noticed a character named **Elara Voss** in your draft. Here's a quick sketch — want me to develop her into a full character page?"
>
> Elara Voss: A disgraced cartographer who falsified a map that started a war. Now she drinks in port cities and takes dangerous mapping jobs no one else wants.
>
> [Yes, develop her] [Not now] [Ignore this name]

### Cross-Reference Auto-Linking

When a draft has `pov-character: Elara Voss` in its frontmatter:
1. The skill verifies `characters/elara-voss.md` exists
2. If missing, offers to create it
3. If it exists, adds a backlink: "Appears in: [[write/chapter-01.md]]"
4. The draft gets updated with `[[characters/elara-voss.md]]`

### Passive Discovery with `/link`

Running `/link` scans all drafts and reports:
- Characters mentioned but missing from `characters/`
- Settings mentioned but missing from `settings/`
- Scenes missing POV character or setting links

---

## The Writer's Wiki

```
the-glass-forest/
├── SCHEMA.md           # Genre, tone, naming rules
├── index.md            # Catalog of all content
├── log.md              # Session history
├── entities/
│   └── ignore-list.md  # Names and terms to skip during auto-detection
├── characters/         # Character sheets, arcs, relationships
├── settings/           # World-building, locations
├── themes/             # Themes, motifs, symbols
├── plan/               # Outlines, plot structures
├── write/              # Polished drafts, scenes
├── sketch/             # Rough drafts, fragments
├── brainstorm/         # Raw ideas, concept dumps
├── help/               # Creative triage sessions
├── critic/             # Structured critiques
├── research/           # Audience, market, and comp-title research
└── _archive/           # Abandoned content (never delete — archive instead)
```

### Why a Wiki?

- **Persistence:** Ideas survive across sessions
- **Cross-references:** Scenes link to characters; characters link to scenes
- **Evolution tracking:** Watch a brainstorm become a sketch, then a draft
- **Automatic entities:** New characters and settings are caught and catalogued
- **[Obsidian](https://obsidian.md)-ready:** Open the folder as a vault and browse the knowledge graph in real-time

---

## Natural Language Intent Guide

### Quantity
- **"a couple"** → 2 | **"a few"** → 3–4 | **"some"** → 5 | **"lots of"** → 10 (2 batches)

### Quality
- **"polished," "final draft"** → VS-CoT, lower temperature
- **"quick," "rough"** → VS-Standard
- **"weird," "wildly different," "surprise me"** → VS-Multi, higher temp

### Phase & Entity
- **"plan," "outline"** → `/plan`
- **"write," "draft"** → `/write`
- **"who is [name]"** → `/character`
- **"what's [place] like"** → `/setting`
- **"explore the theme of"** → `/theme`
- **"help me plan my story," "i have an idea," "what should i write"** → `/grill-me`
- **"i'm stuck," "what happens next," "this feels flat," "writer's block"** → `/help`
- **"critique," "review," "does this work," "what's wrong with"** → `/critic`
- **"research X," "what's been written about X"** → `/research` (concept)
- **"who reads X," "audience for X," "reader profile"** → `/research` (audience)
- **"comp titles for X," "books like X"** → `/research` (comp-titles)
- **"what's the market for X," "genre demand," "how does X position"** → `/research` (market)

---

### Story Definition with `/grill-me`

The `/grill-me` command is a structured interview that walks you from a vague idea to a complete story bible with characters, setting, plot, and chapter outline. At every step it generates diverse options using VS-Multi so you discover angles you wouldn't have thought of alone.

**Typical flow:**
```
User: "i have an idea but don't know where to start"
→ Agent: "What sparked this story?"
→ User: "A dream about a city that only exists at night"
→ Agent (VS-Multi): Here are 5 different takes on that idea:
   1. A cartographer maps a nocturnal city that pays in memories...
   2. An insomniac projects a metropolis from her subconscious...
   3. A black-market courier delivers contraband to a night-only city...
   4. A prison city for dream-creatures opens its gates at sunset...
   5. Ruins rebuild themselves each night—something inside wants out...

→ User picks and combines, then agent drills into characters, setting, stakes,
   theme, structure, narrative order, and chapter-by-chapter outline.

→ At the "How do you want the reader to experience time?" step, the agent suggests:
   1. Linear — A→B→C, cause and effect in real time
   2. In Medias Res — Start in the middle, circle back
   3. Framed / Nested — Present narrator tells past story
   4. Non-Linear — Puzzle-piece timeline
   5. Reverse Chronology — End to beginning
   6. Episodic / Parallel Threads — Converging timelines

→ After 4 phases, the agent files:
   plan/story-bible.md      # One-page reference with narrative order
   plan/story-outline.md     # Full chapter breakdown with time markers
   characters/               # Defined characters with arcs
   settings/                 # Key locations with atmosphere
   themes/                   # Central themes and motifs
```

**Resume with awareness:**
```
User: /grill-me resume
→ Agent reads the checkpoint and sees it paused at Phase 3 (Draft) on April 27.
→ Agent reads log.md and sees that since then:
   - New character created: Mira Thorn (characters/mira-thorn.md) on April 28
   - New draft: write/chapter-03.md on April 29
→ Agent: "Since you paused, the wiki has grown: Mira Thorn was added as a character,
   and Chapter 3 was drafted. Should I incorporate these into the story bible and outline?"
→ Writer: "Yes, make Mira the rival."
→ Agent updates story-bible.md and story-outline.md, then resumes at Phase 3.
```

## What You Get

### Before (Direct Prompting)
```
> Tell me a joke about coffee.
→ "Why did the coffee file a police report? Because it got mugged!" (x5)
```

### After (Verbalized Sampling)
```
> /write "5 jokes about coffee"
→ 1. "Espresso may not solve all your problems, but it's a good shot." (prob: 0.12)
  2. "Error 404: Coffee not found. Please restart human." (prob: 0.07)
  3. "Why did the latte go to therapy? It had too much foam to deal with." (prob: 0.15)
  4. "Cold brew is just coffee that took a gap year to find itself." (prob: 0.07)
  5. "Coffee: because anger management is too expensive." (prob: 0.06)
```

### Entity Generation
```
> /character "Elara Voss, a disgraced cartographer"
→ 1. Elara was fired for falsifying a map that started a war. (prob: 0.14)
  2. Her "disgrace" was a cover — she's a spy for the guild. (prob: 0.11)
  3. She never falsified anything; her rival forged the evidence. (prob: 0.08)
```

### Automatic Detection
```
User writes a draft mentioning "Mira Thorn" and "The Black Spire"
→ "I noticed these entities in your draft. Create wiki pages?"
  - Mira Thorn (character) — [Create] [Skip]
  - The Black Spire (setting) — [Create] [Skip]
```

### Research
```
> /research comp titles for a cozy fantasy with a witch-run bakery
→ # Comp Titles: Cozy Fantasy / Witch Bakery
  1. A Marvellous Light — Casey McQuiston, 2021
     Sales-band signal: bestseller list
     Why it's a comp: cozy supernatural mystery with queer romance; same "soft magic in a shop" energy
  2. The House in the Cerulean Sea — TJ Klune, 2020
     Sales-band signal: bestseller / >200k copies first year
     Why it's a comp: found-family warmth, low-stakes conflict, ensemble magical community
  3. Legends & Lattes — Travis Baldree, 2022
     Sales-band signal: breakout indie → Tor; ~150k first year
     Why it's a comp: THE template for cozy fantasy with food/shop setting
  ...
  Comparable Performance Range: books with this profile typically ship
  in the 20k–80k first-year band; outliers (top 5%) reach 150k+.
  confidence: medium (public web signals only)
  → Filed: research/comp-cozy-fantasy-witch-bakery-2026-04-28.md
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Acknowledgements

- **Zhang et al.** for Verbalized Sampling (arXiv:2510.01171v3)
- **Andrej Karpathy** for the LLM Wiki pattern

- Paper: https://arxiv.org/abs/2510.01171
- VS Website: https://www.verbalized-sampling.com/
- VS Code: https://github.com/CHATS-lab/verbalized-sampling
- Karpathy LLM Wiki: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Writer's Wiki Spec: `llm-wiki.md` (in this folder)
