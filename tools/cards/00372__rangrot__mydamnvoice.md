---
id: tool-00372
type: tool
area: 库
status: active
tags: [TTS, Claude插件, 协议宽松, 本地优先, 英文文档, 本地写作]
title: mydamnvoice
summary: 小说转语音/有声书
source: https://github.com/rangrot/mydamnvoice
created: 2026-07-18
updated: 2026-07-18
no: 372
category: 二、网文 / 长篇 AI 写作系统 库
repo: rangrot/mydamnvoice
stars: 1
url: https://github.com/rangrot/mydamnvoice
tier: "B"
use_case: "小说转语音/有声书"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# rangrot/mydamnvoice

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rangrot/mydamnvoice
- **Stars**：1
- **语言**：None
- **License**：MIT
- **Topics**：ai, ai-skill, chatgpt, claude, claude-code, codex, cursor, gemini, open-source, stylometry, voice-profile, writing
- **GitHub 描述**： Open source AI skill that profiles your writing voice and generates prompts that sound like you
- **本地描述**：Open source AI skill that profiles your writing voice and generates prompts that sound like you
- **拉取时间**：2026-07-23 22:49:57

---

# MyDamnVoice

Your AI should sound like you wrote it.

![Install](https://img.shields.io/badge/install-npx%20skills%20add-blue)
![GitHub stars](https://img.shields.io/github/stars/rangrot/mydamnvoice)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Platforms](https://img.shields.io/badge/platforms-Claude%20%7C%20ChatGPT%20%7C%20Gemini%20%7C%20Cursor-lightgrey)

MyDamnVoice is an open-source AI skill that interviews you about your writing style, analyzes your samples, and generates a voice profile you can drop into any AI. Built on 60 years of computational stylometry research.

---

## The difference

Same prompt. Different voice.

### Startup CEO: "Tell your board that you're pivoting the product strategy"

**Voice profile:** Bottom line first, short sentences, specific deadlines. Uses "we need" not "you should." Ends every message with next steps. Formality 3/10.

> **Without MyDamnVoice**
>
> I'd be happy to help you prepare for that board conversation. Here's a framework for presenting a product strategy pivot: 1. Context & Rationale - What data/insights drove this decision? 2. The Pivot Details - Clear before/after comparison. 3. Resource Implications - Budget requirements and reallocation. Would you like me to help you develop any of these sections specifically?

> **With MyDamnVoice**
>
> We're pivoting. Current approach isn't delivering the growth metrics we need. Enterprise-first is burning cash faster than we're acquiring customers. Sales cycles are 8+ months, churn is 23%. New direction: self-serve with freemium. Engineering pivots Monday. Marketing shifts messaging by end of week. We execute or we're dead.

---

### Gen Z Social Media Manager: "Write an Instagram caption for a new product launch (vitamin C serum)"

**Voice profile:** Lowercase, self-aware, culturally literate. Starts with "ok so" or "the thing is." Never sounds like corporate. Formality 2/10.

> **Without MyDamnVoice**
>
> GLOW ALERT Our NEW Vitamin C Serum is HERE! Say hello to brighter, more radiant skin with our potent 20% formula that: Boosts collagen production. Fades dark spots & hyperpigmentation. Protects against environmental damage. Ready to transform your skincare routine? Limited launch offer: 25% off for the first 48 hours!

> **With MyDamnVoice**
>
> ok so i've been testing this vitamin C serum for like 3 months and honestly? my skin looks... good? which is weird bc i'm usually the person who buys skincare and then forgets to use it for weeks. also it doesn't pill up under makeup which is SHOCKING. sometimes the simplest things just work

---

### D&D Dungeon Master: "Start a D&D campaign with a rat, a dragon, and a pig saving a drowning fish"

**Voice profile:** Cracks jokes at the table between epic moments. Mixes casual profanity with poetic structure. Drops "chungus" and "Sikeeeee" like breadcrumbs. Punchy controlled chaos. Formality 2/10.

> **Without MyDamnVoice**
>
> At the edge of a slow river, a fish struggles near the surface. It thrashes weakly, gills flaring, as if the water itself has turned against it. Three unlikely figures stand on the muddy bank watching the spectacle unfold. The rat notices the fish first. "That fish is drowning," he says. The pig leans forward, studying the scene with confusion. "How does a fish drown?" he asks.

> **With MyDamnVoice**
>
> Behold. The fish is already drowning. Not metaphor drowning. Actual flapping panic drowning. Little silver idiot gulping river water like it owes him money. And standing on the muddy bank are three heroes. Which is generous wording. A rat with one eye and six opinions. The pig squints at the river like the concept of water personally offended him. "How the fuck does a fish drown."

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Install

```
Claude Code / Codex / Gemini CLI / Cursor:
  npx skills add rangrot/mydamnvoice

ChatGPT: Create a Custom GPT with the instructions from platforms/chatgpt-gpt/
Gemini: Create a Gem with the instructions from platforms/gemini-gem/
Any AI: Download SKILL.md and drop it into your chat
```

## What you get

- Full voice interview across 7 dimensions (tone, formality, energy, humor, perspective, vocabulary, sentence structure)
- Chat history analysis on supported platforms (automatic)
- Voice DNA summary
- Core attributes scored on a 1-10 scale
- Anti-patterns: words and phrases your AI should never use
- Platform-native export, auto-detected based on where the skill is running
- Portable markdown file that works in any AI tool
- Permanent save to your AI's memory or custom instructions

## The science

Every voice profile is grounded in computational stylometry, a field with 60+ years of peer-reviewed research into what makes one person's writing measurably different from another's. The same techniques used to attribute disputed authorship in forensic linguistics, applied here to teach AI how you write.

## Contributing

See [CONTRIBUTING.md](https://github.com/rangrot/mydamnvoice/blob/main/CONTRIBUTING.md) for guidelines on adding platform adapters, improving the interview flow, or submitting bug fixes.

For deeper analysis with 14 quantitative metrics, visit [mydamnvoice.com](https://mydamnvoice.com)

## License

[MIT](https://github.com/rangrot/mydamnvoice/blob/main/LICENSE)
