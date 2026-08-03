---
id: tool-01157
type: tool
area: 库
status: active
tags: [互动叙事, 协议宽松, 本地优先, 英文文档, 本地写作]
title: remove-ai-writing-signs
summary: 互动叙事/聊天写故事
source: https://github.com/idcesares/remove-ai-writing-signs
created: 2026-07-18
updated: 2026-07-18
no: 1157
category: 二、网文 / 长篇 AI 写作系统 库
repo: idcesares/remove-ai-writing-signs
stars: 0
url: https://github.com/idcesares/remove-ai-writing-signs
tier: "C"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# idcesares/remove-ai-writing-signs

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/idcesares/remove-ai-writing-signs
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A reconstruction-editing system for removing AI writing patterns from English text. Works as a Claude skill, a system prompt for any LLM, or a manual editing methodology.
- **本地描述**：A reconstruction-editing system for removing AI writing patterns from English text. Works as a Claude skill, a system prompt for any LLM, or a manual editing methodology.
- **拉取时间**：2026-07-23 23:12:47

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Remove AI Writing Signs

A reconstruction-editing system for detecting and eliminating signs of
AI-generated writing in English text, producing genuinely human-sounding
output. Built primarily as a Claude skill, but the architecture works as a
methodology for any LLM, any editor, or any system where structured prompts
are useful.

## Why

AI text fails because it is **statistically average**. It regresses toward
the most common way to say anything. Human text succeeds because it is
**specific, uneven, and opinionated**.

Cosmetic cleanup — swapping "delve" for "explore," deleting em dashes,
breaking up triplets — doesn't fix the underlying problem. The text still
smells of significance inflation, false balance, vague attribution, and
trailing -ing analyses that fake depth. This system takes a reconstruction
approach: dismantle the text down to its claims, then rebuild it as a
specific human would write it.

The north star: after rewriting, could a Wikipedia editor or a writing
professor identify the text as AI-generated? If yes, the job isn't done.

## How it works

Text flows through one calibration step and five sequential passes:

- **Step 0 — Calibration.** Identify language, genre, length, pattern
  density, register, and AI-confidence. Pick a mode (express / standard /
  heavy) and an aggressiveness level. This step exists to prevent
  over-correction, the system's most common failure mode.
- **Pass 1 — Artifact removal.** Strip chatbot residue: conversational
  framing, citation tokens, markup bugs, hidden instructions.
- **Pass 2 — Vocabulary detoxification.** Replace AI-overused words using
  an era-mapped lexicon (GPT-4, GPT-4o, GPT-5+).
- **Pass 3 — Content deflation.** Remove significance inflation, vague
  attributions, notability assertions, and trailing -ing clauses.
- **Pass 4 — Structural reconstruction.** Restore sentence-length
  variation, fix copula avoidance, kill negative parallelisms and forced
  triplets, normalize section structure.
- **Pass 5 — Texture injection.** Add specificity, controlled asymmetry,
  and authorial signals where the genre supports it.

Before producing output, the rewrite is sanity-checked against an
anti-patterns reference that catches over-humanization: manufactured typos,
register violations, voice ventriloquism, and similar failure modes.

## Scope

**English only.** All native variants — US, UK, AU, CA, IE, IN — are in
scope, with the source variant preserved (no anglicizing "colour," no
americanizing "lift"). Non-English input is declined by default, or handled
with limited structural flagging only. PT-BR support is planned for v1.1.

The system is calibrated for six genres: encyclopedic, marketing, academic,
blog/op-ed, technical documentation, and fiction/creative. Each genre has
its own playbook with prioritize / tolerate / suppress notes per pass.

## Repo structure

```
remove-ai-writing-signs/
├── SKILL.md                       operational instructions
├── README.md                      this file
└── references/
    ├── genre-playbooks.md         per-genre calibration (6 genres)
    ├── vocabulary-by-era.md       GPT-4 / 4o / 5+ lexicon
    ├── structural-patterns.md     27 patterns with examples (P01–P27)
    ├── statistical-guide.md       metrics, thresholds, trigram lookup
    └── anti-patterns.md           over-humanization guardrails (AP01–AP10)
```

## Usage

The system is platform-agnostic. Three ways to use it:

**1. As an LLM skill / agent instruction set.**
Drop the directory into a skill-aware runtime (Claude Code, Claude Agent
SDK, Claude.ai skills, or any framework that supports skill-style
discovery via frontmatter). The trigger description in `SKILL.md` activates
the skill on prompts like "make this sound less AI," "humanize this,"
"this reads like ChatGPT," or "clean this up."

**2. As a system prompt.**
Concatenate `SKILL.md` (and any references you want loaded eagerly) into a
system prompt or operator instructions for any LLM — Claude, GPT, Gemini,
open-weight models. The 5-pass architecture works as standalone
methodology.

**3. As a manual editing methodology.**
A human editor can use the references directly. The pattern catalog
(P01–P27), the vocabulary lexicon, the genre playbooks, and the
anti-patterns guardrails are all usable without any model in the loop.

## What v1.0 covers

- 27 structural pattern families adapted from Wikipedia:Signs of AI writing
- Era-aware vocabulary (GPT-4 dominant 2023–2024, GPT-4o 2024–2025,
  GPT-5+ 2025–present)
- 6 genre playbooks calibrating aggressiveness to context
- 10 anti-patterns guarding against over-humanization
- Statistical metrics: burstiness, sentence-length CoV, type-token ratio,
  trigram repetition, with thresholds for AI / borderline / human
- Adaptive output modes (express / standard / heavy) sized to input
- Hidden-instruction defense in Pass 1
- 27-entry high-signal trigram lookup table

## Status

**v1.0 — stable.** English-only, 27 patterns, 6 genres, 10 anti-patterns.

**Planned:**
- v1.1 — PT-BR sibling (own lexicon, structural examples, statistical
  baselines)
- v1.2 — Trigger-description optimization tuned against real usage data

## Sources and credits

The pattern catalog and methodology draw on:

- **Wikipedia: Signs of AI writing** — community-maintained field guide
  that informed the 27 pattern families
- **Kobak et al. (2025)** — quantitative analysis of GPT-era vocabulary
  shifts
- **Juzek & Ward (2025)** — frequency studies of LLM word usage
- **Geng & Trotta (2025)** — copula avoidance and structural markers in
  AI-generated academic writing

## License

[MIT](LICENSE)
