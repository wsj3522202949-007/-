---
id: tool-07381
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, 协议宽松, 本地优先, 英文文档, 本地写作]
title: humanize-writing-skill
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/lguz/humanize-writing-skill
created: 2026-07-18
updated: 2026-07-18
no: 7381
category: 画龙补充 / 扩容入库 — 补充源
repo: lguz/humanize-writing-skill
stars: 20
url: https://github.com/lguz/humanize-writing-skill
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: f92ccb0bae9c054c
  - methods/QUICK_START.md
---

# lguz/humanize-writing-skill

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/lguz/humanize-writing-skill
- **Stars**：20
- **语言**：None
- **License**：MIT
- **Topics**：ai-content, ai-text-humanizer, ai-writing-detection, chatgpt-prompt, claude-code, claude-code-skill, cursor-rules, humanize-ai-writing, humanize-text, llm-prompt, writing-prompt, writing-tools
- **GitHub 描述**：Rewrite AI-generated text to sound human. 3-pass editing system with 36+ banned words, 10 structural patterns, and a quality checklist. Works with any LLM — Claude, ChatGPT, Gemini, Cursor, Windsurf. Also available as a Claude Code plugin.
- **本地描述**：humanize-writing-skill
- **拉取时间**：2026-07-25 19:20:12

related:
  - methods/QUICK_START.md
---

# Humanize Writing

A prompt-based writing editor that rewrites AI-generated text to sound like a real human wrote it.

It catches the patterns that make AI writing obvious — the vocabulary, the sentence structures, the too-perfect tone — and fixes them through a systematic 3-pass editing process.

Works with **any LLM**: Claude, ChatGPT, Gemini, Cursor, Windsurf, or anything that accepts a system prompt. Also available as a one-command install for Claude Code users.

## How It Works

The system runs your text through three passes:

**Pass 1: Kill the AI Vocabulary** — Replaces words like "delve," "leverage," "tapestry," and 30+ other statistically overused AI words with simpler human alternatives.

**Pass 2: Break the AI Structures** — Eliminates structural patterns like parallel negation ("Not X, but Y"), tricolons (groups of three), em dash overuse, rhetorical Q+A, and mirror structures. These are stronger tells than vocabulary.

**Pass 3: Add Human Texture** — Varies sentence length, adds contractions, lets some thoughts stay unresolved, and makes the author's actual opinion visible.

Also includes special rules for LinkedIn posts and a 14-point quality checklist that runs before returning any rewrite.

## Quick Start (Any LLM)

The entire system is two markdown files. You can use them right now:

1. **[SKILL.md](https://github.com/lguz/humanize-writing-skill/blob/main/skills/humanize-writing/SKILL.md)** — The main instructions (the 3-pass process, LinkedIn rules, quality checklist)
2. **[ai-patterns-dictionary.md](https://github.com/lguz/humanize-writing-skill/blob/main/skills/humanize-writing/references/ai-patterns-dictionary.md)** — The reference dictionary (36+ banned words, 10 structural patterns, tone tells)

Copy the contents of both files into your LLM's system prompt or custom instructions, then paste any text you want humanized.

## Setup by Platform

### Claude Code (Plugin Install)

One command, and it works automatically whenever you ask to humanize text:

```bash
claude plugin marketplace add https://github.com/lguz/humanize-writing-skill
```

After that, just say things like "humanize this" or "make this sound less AI" and Claude Code will use the skill automatically.

### Claude Code (Manual Install)

Copy the skill files into your Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills/humanize-writing/references
curl -o ~/.claude/skills/humanize-writing/SKILL.md https://raw.githubusercontent.com/lguz/humanize-writing-skill/main/skills/humanize-writing/SKILL.md
curl -o ~/.claude/skills/humanize-writing/references/ai-patterns-dictionary.md https://raw.githubusercontent.com/lguz/humanize-writing-skill/main/skills/humanize-writing/references/ai-patterns-dictionary.md
```

### ChatGPT / Custom GPT

1. Go to **ChatGPT** → create a new GPT (or use "Custom Instructions" in settings)
2. Paste the contents of [SKILL.md](https://github.com/lguz/humanize-writing-skill/blob/main/skills/humanize-writing/SKILL.md) into the system prompt / instructions field
3. Paste the contents of [ai-patterns-dictionary.md](https://github.com/lguz/humanize-writing-skill/blob/main/skills/humanize-writing/references/ai-patterns-dictionary.md) below it (or upload it as a knowledge file)
4. Start a conversation and paste any text you want humanized

### Cursor / Windsurf

1. Create a rules file in your project (e.g., `.cursor/rules/humanize-writing.md` or `.windsurfrules`)
2. Paste the contents of both files into it
3. When editing text in the IDE, reference the rule or ask the AI to humanize your writing

### Any Other LLM

Copy the contents of both markdown files into whatever "system prompt," "custom instructions," or "context" field your tool provides. The instructions are model-agnostic — they work with any LLM that can follow structured prompts.

## What's Inside

```
skills/humanize-writing/
├── SKILL.md                              # 3-pass rewriting process + quality checklist
└── references/
    └── ai-patterns-dictionary.md         # Banned words, structural patterns, tone tells
```

### The AI Patterns Dictionary Covers

- **Tier 1 Banned Words** (18 words) — Strongest AI signals like "delve," "tapestry," "pivotal," "testament"
- **Tier 2 Banned Words** (18 words) — Moderate signals like "crucial," "leverage," "seamless," "robust"
- **Tier 3 Transitions** — Words that are fine alone but AI clusters unnaturally ("Furthermore," "Moreover," "Additionally")
- **10 Structural Patterns** — Parallel negation, tricolons, em dash overuse, rhetorical Q+A, mirror structures, dramatic reveals, and more
- **Tone & Voice Tells** — Uniform sentence length, hedging, over-positivity, absence of personal voice
- **Content Red Flags** — Generic conclusions, missing concrete details, regression to generic statements

## Writing Philosophy

Based on the principles behind Paul Graham's writing style: clarity over cleverness, directness over decoration. Good writing sounds like a smart person thinking out loud. The goal is invisible editing — the reader should never think about *how* something was written.

## Sources

The AI patterns dictionary draws from:

- [Wikipedia: Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [GPTZero AI Vocabulary Research](https://gptzero.me/ai-vocabulary)
- [Chris Herbert's ChatGPT Overused Words](https://gist.github.com/chrisgherbert/c734ec50ae464135be57cd03b84281f9)
- [Sabrina Ramonov's Humanizer Prompt](https://github.com/SabrinaRamonov/prompts/blob/main/humanize_ai_writing.md)
- [God of Prompt: 500 ChatGPT Overused Words](https://www.godofprompt.ai/blog/500-chatgpt-overused-words-heres-how-to-avoid-them)

## License

MIT
