---
id: tool-04074
type: tool
area: 库
status: active
tags: [TTS, 协议未明, 本地优先, 英文文档, 本地写作]
title: brand-voice-prompting
summary: 小说转语音/有声书
source: https://github.com/dirktbilisi/brand-voice-prompting
created: 2026-07-18
updated: 2026-07-18
no: 4074
category: 十一、有声书 / 小说转语音 TTS 库
repo: dirktbilisi/brand-voice-prompting
stars: 0
url: https://github.com/dirktbilisi/brand-voice-prompting
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/模板库.md
---

# dirktbilisi/brand-voice-prompting

- **分类**：十一、有声书 / 小说转语音 TTS 库
- **链接**：https://github.com/dirktbilisi/brand-voice-prompting
- **Stars**：0
- **语言**：None
- **License**：NOASSERTION
- **Topics**：ai, brand-voice, llm, pattern-library, prompt-engineering, writing
- **GitHub 描述**：A pattern library for keeping LLM-generated text aligned with a defined brand voice. Pre-flight blocks, templates, and concrete before/after examples.
- **本地描述**：A pattern library for keeping LLM-generated text aligned with a defined brand voice. Pre-flight blocks, templates, and concrete before/after examples.
- **拉取时间**：2026-07-24 00:03:06

---

# Brand Voice Prompting

> A pattern library for keeping LLM-generated text aligned with a defined brand voice — across drafts, iterations, and team members.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](./LICENSE)

---

## TL;DR

LLMs default to generic institutional voice. Adjective-based instructions ("confident, warm, expert") don't fix it. **A structured pre-flight block does** — six fields placed at the top of every voice-sensitive prompt.

Most brand voice work is **subtractive**, not additive. The forbidden vocabulary list is the highest-leverage field.

related:
  - methods/模板库.md
---

This repo is for anyone who has tried to make a model write "in our voice" and watched it drift back to generic AI prose by the third sentence.

## The problem

Large language models default to a kind of average institutional tone: warm, hedged, slightly American. That tone is fine — until your brand explicitly *isn't* that. If your voice is sharp, stripped, contrarian, or deeply local, every prompt is a small fight against the model's defaults.

Most teams handle this by:
- Pasting the entire brand-voice document into every prompt (works, but slow and expensive)
- Hoping a "use our brand voice" instruction is enough (it never is)
- Editing every output by hand (defeats the point)

There's a better pattern: **structured pre-flight blocks**.

## What's in this repo

- **[The Pattern](https://github.com/dirktbilisi/brand-voice-prompting/blob/main/pattern.md)** — the core idea: a structured pre-flight block that goes before every voice-sensitive prompt
- **[Brand Voice Template](https://github.com/dirktbilisi/brand-voice-prompting/blob/main/brand-voice-template.md)** — a fillable template for capturing your own brand voice in a model-readable format
- **[Examples](https://github.com/dirktbilisi/brand-voice-prompting/blob/main/examples/)** — anonymized before/after prompts showing the pattern in action
- **[Anti-patterns](https://github.com/dirktbilisi/brand-voice-prompting/blob/main/anti-patterns.md)** — what doesn't work and why

## Who this is for

- Solo operators writing in a defined voice (consultants, coaches, indie writers)
- Small teams trying to keep LLM-generated marketing text consistent
- Anyone who has read their own LLM output and thought "this could be from anyone"

If you have a 50-page brand guideline document already, this won't replace it — but it will make it actually usable in prompts.

## The core insight

Brand voice in prompts is not about adjectives. It's about **constraints + counterexamples**.

Telling a model "write in a confident, warm, expert tone" produces generic confident-warm-expert text.

Telling a model "do NOT use the words *unleash, journey, holistic, transformative*; do NOT begin with *In today's...*; one-line opening, no hedging" produces text that actually has a shape.

The pattern in this repo is built on this asymmetry: most brand voice work is **subtractive**, not additive.

## License

[CC BY 4.0](https://github.com/dirktbilisi/brand-voice-prompting/blob/main/LICENSE) — use, adapt, remix freely with attribution.

## Roadmap

- [ ] More before/after examples (different industries: SaaS, consulting, e-commerce, B2B)
- [ ] Domain-specific forbidden vocabulary lists (legal, medical, technical)
- [ ] Translation: German version (`pattern-de.md`)
- [ ] Companion tool: a small CLI that validates your generated text against your pre-flight block

Issues and pull requests welcome — see [Contributing](https://github.com/dirktbilisi/brand-voice-prompting/blob/main/CONTRIBUTING.md).

## Contributing

Real before/after examples from your own brand voice work are the most valuable contribution. See [CONTRIBUTING.md](https://github.com/dirktbilisi/brand-voice-prompting/blob/main/CONTRIBUTING.md) for what we're looking for.

## Maintainer

Built by [**Dirk Häger**](https://github.com/dirktbilisi) — independent learning architect at [focusinstitute.io](https://focusinstitute.io) · [LinkedIn](https://www.linkedin.com/in/dirkhaeger/)

If this saves you editing time, ⭐ star the repo or share with your team.
