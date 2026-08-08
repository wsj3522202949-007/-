---
id: tool-05228
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: wiki-ai-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/valpep/wiki-ai-detector
created: 2026-07-18
updated: 2026-07-18
no: 5228
category: 一、去 AI 味 / Humanizer 库
repo: Valpep/wiki-ai-detector
stars: 5
url: https://github.com/valpep/wiki-ai-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 051a56c9bd9c0976
  - methods/改稿润色指令库.md
---

# Valpep/wiki-ai-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/valpep/wiki-ai-detector
- **Stars**：5
- **语言**：None
- **License**：None
- **Topics**：claude-skills
- **GitHub 描述**：Detect AI-generated text using Wikipedia's empirical field guide – vocabulary patterns, structure tells, and formatting signals
- **本地描述**：Detect AI-generated text using Wikipedia's empirical field guide – vocabulary patterns, structure tells, and formatting signals
- **拉取时间**：2026-07-25 18:10:49

---

# wiki-ai-detector

An interpretable heuristic tool for reviewing possible AI-writing signals in text — based on Wikipedia's empirically documented field guide on LLM writing patterns, extended with deeper structural tells from recent observation of newer models.

This is not a definitive AI detector and does not prove authorship. It is designed for editorial review, triage, and analysis using explainable signals.

Works with any text: articles, emails, reports, marketing copy, Wikipedia drafts, social media posts.

---

## What it does

Scans text for characteristic signals across 16 categories:

- **Vocabulary density** — overused words like *pivotal, delve, underscore, tapestry, meticulous*
- **Content patterns** — significance inflation, "challenges" formula, vague attribution, "quietly" narratives, overgeneralization from few sources
- **Sentence structure** — copula avoidance, Latinate-over-Saxon preference, negative parallelisms, rule-of-three, elegant variation
- **Formatting tells** — title case headings, excessive bold, em dash overuse, curly quotes, markdown in non-markdown contexts
- **Communication leakage** — phrases like "I hope this helps", placeholders, chat artifacts
- **Citation & markup artifacts** — ChatGPT/Perplexity/Grok technical residue
- **Image & caption tells** — keyword-matched illustrations, inflated captions
- **Argumentative & discussion tells** — rhetorical anaphora, hallucinated references, refusal-to-concede patterns
- **Newer model evasion (2025+)** — what persists when models suppress classic tells
- **Older model tells** — *"It's important to note that…"*, *"In conclusion,"* and similar
- **Context-sensitive phrase restrictions** — phrases like *"genuinely"* or *"didn't see it coming"* used in contexts that don't earn the emotional weight
- **Deeper structural tells (Romero, 2025)** — abstraction trap, sensing without sensing, treadmill effect, subtext vacuum
- **Theatrical narration (multilingual, 2026)** — overt drumroll phrases, fake pauses, pseudo-dialogue with the reader, in EN/RU/UK
- **Decorative triplets** — the synonymic-third-member subtype of rule-of-three ("rich, vibrant, and dynamic culture")
- **Drumroll-in-disguise** — covert announcement via neutral connectives ("It's worth noting", "Стоит отметить", "Варто зазначити")
- **False idioms and calques** — word-by-word translations of English idioms that read as plausible but non-native (e.g. *«не дома в теме»* ← *at home in*)

---

## Signal strength

Not all signals are equal. The tool works by evaluating clusters, not isolated occurrences.

**Strong signals**
- citation residue (e.g. `turn0search0`, `contentReference[...]`)
- chat leakage and assistant phrases
- placeholders and formatting artifacts
- on modern models: deeper structural tells (Section 12) — abstraction without imagery, sensory descriptions that don't track reality, paragraphs that don't advance the argument, explicit explanation of every implication
- on modern models: in-disguise patterns (Sections 14–16) — decorative triplets in clusters, drumroll-in-disguise as paragraph rhythm, false calques

**Moderate signals**
- repetitive structure and transitions
- formulaic paragraph construction
- predictable rhetorical flow
- Latinate-over-Saxon vocabulary preference
- structural uniformity (every paragraph the same shape)

**Weak signals**
- isolated buzzwords
- generic polished phrasing
- common stylistic patterns
- a single decorative triplet, a single drumroll-in-disguise, or a single calque — these are tells only in clusters or at structural density

---

## Output

For each detected signal:
- quoted fragment
- signal category
- short explanation

Then:

**Final verdict:** Likely AI / Possibly AI / Likely Human
**Confidence:** Low / Medium / High

---

## How to use

Add `SKILL.md` as a skill in your Claude Cowork setup. Paste any text and ask:

> "Check this text for AI tells"

---

## Verdict logic

- One signal → coincidence
- Multiple signals in proximity → meaningful
- Dense clusters → strong indicator

The system weights patterns and repetition, not single words.

---

## Limitations

- Does not prove authorship
- False positives are possible
- Some signals depend on genre, tone, or platform
- Heavily edited AI text may not trigger obvious markers
- High-quality human writing can appear "AI-like"
- Different models produce different patterns
- Newer models (GPT-5.1+, Claude 4+) actively suppress known tells; rely on Sections 12 and 14–16 (deeper structural tells and in-disguise patterns) when classic markers are absent

---

## What this tool is for

- editorial review
- content triage
- explainable analysis
- understanding AI writing patterns

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Based on

- Wikipedia's community-maintained field guide on LLM writing patterns — refined through real editorial experience.
  Source: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Alberto Romero, "10 Signs of AI Writing That 99% of People Miss" (Medium, December 2025) — basis for Section 12 (deeper structural tells)
- Sections 14–16 (decorative triplets, drumroll-in-disguise, false idioms/calques) added based on practical observation in multilingual editorial review (EN/RU/UK), 2026
