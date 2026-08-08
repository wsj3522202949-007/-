---
id: tool-00209
type: tool
area: 库
status: active
tags: [提示词, JavaScript, 协议未明, 需API密钥, 英文文档, 多Agent]
title: prompting-glossary
summary: 提示词/写作工作流
source: https://github.com/jstahl666/prompting-glossary
created: 2026-07-18
updated: 2026-07-18
no: 209
category: 二、网文 / 长篇 AI 写作系统 库
repo: jstahl666/prompting-glossary
stars: 0
url: https://github.com/jstahl666/prompting-glossary
tier: "C"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1bdc7717378c54ad
  - methods/最强写作方法论_全球最强综合版.md
---

# jstahl666/prompting-glossary

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jstahl666/prompting-glossary
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A personal reference for writing better prompts and skills for AI coding/assistant agents — 90+ terms with definitions, when-to-use, pitfalls, examples, and citations.
- **本地描述**：A personal reference for writing better prompts and skills for AI coding/assistant agents — 90+ terms with definitions, when-to-use, pitfalls, examples, and citations.
- **拉取时间**：2026-07-23 22:45:08

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Prompting & Skills

A personal reference for writing better prompts and skills for AI coding/assistant
agents — what the words mean, when to reach for each move, and where they come from.

Built by surveying the most popular public skill repositories (Matt Pocock's skills,
Anthropic's official skills + docs, Superpowers, Spec Kit, the Karpathy CLAUDE.md, the
`awesome-*` lists) and the prompt-engineering canon (Anthropic, OpenAI, Google, DAIR).

## Files

- **🔎 [Searchable web app](https://jstahl666.github.io/prompting-glossary/)** — search all 122
  terms by keyword *or* by what you're trying to do, from any browser. No install, no login.
- **[cheatsheet.md](https://github.com/jstahl666/prompting-glossary/blob/main/cheatsheet.md)** — one-liner per term, grouped by purpose. Start here
  when you just need to jog your memory or scan for the right word.
- **[glossary.md](https://github.com/jstahl666/prompting-glossary/blob/main/glossary.md)** — the full reference. Each of the 122 terms has a
  definition, when-to-use, pitfalls, a concrete example you could type, and a citation.

## How to use it

Open the [searchable web app](https://jstahl666.github.io/prompting-glossary/) and type what
you're trying to do. Or, when you hit a term in someone's skill you don't recognize, scan the
cheat-sheet, then open the glossary entry for depth.

**Fastest wins:** be specific · give examples (few-shot) · separate instructions from
pasted data (delimiters) · ask for step-by-step reasoning (chain-of-thought) · set
standing rules once (system prompt) · align *before* building (grilling).

## Keeping it current

This is meant to grow. When you come across a new term or pattern worth keeping, add an
entry to `glossary.md` (full format) and a one-liner to `cheatsheet.md`.

**After editing `glossary.md`, regenerate the search data so the web app stays in sync:**

```
python build_search_data.py
```

That rewrites `glossary-data.js` (which the search page reads). Commit both files. The prompting
ecosystem moves fast, so the sources at the bottom of the glossary are worth re-checking periodically.
