---
id: tool-00638
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: copilot-copywriting-skill
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/eumakerdev/copilot-copywriting-skill
created: 2026-07-18
updated: 2026-07-18
no: 638
category: 二、网文 / 长篇 AI 写作系统 库
repo: eumakerdev/copilot-copywriting-skill
stars: 0
url: https://github.com/eumakerdev/copilot-copywriting-skill
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# eumakerdev/copilot-copywriting-skill

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/eumakerdev/copilot-copywriting-skill
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Copilot skill for conversion copywriting with anti-AI writing patterns. Produces human-sounding marketing copy.
- **本地描述**：Copilot skill for conversion copywriting with anti-AI writing patterns. Produces human-sounding marketing copy.
- **拉取时间**：2026-07-23 22:57:40

---

# copilot-copywriting-skill

A [GitHub Copilot Skill](https://code.visualstudio.com/docs/copilot/customization/agent-skills) for writing conversion-focused marketing copy that reads as unmistakably human.

## What it does

- Writes marketing copy for homepages, landing pages, pricing pages, feature pages, about pages
- Applies conversion copywriting frameworks (AIDA, PAS, headline formulas, page templates)
- **Enforces anti-AI writing patterns** — every piece of copy is checked against a ban list of 50+ AI vocabulary words, sentence patterns, and structural tells sourced from [Wikipedia's "Signs of AI Writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) and academic research

## Install

### Per-project (shared with team)

Copy the `copywriting/` folder into your project:

```
.github/skills/copywriting/
├── SKILL.md
└── references/
    ├── anti-ai-patterns.md
    ├── copy-frameworks.md
    └── natural-transitions.md
```

### Per-user (all your workspaces)

Copy to your personal Copilot skills folder:

**Windows:**
```
%USERPROFILE%\.copilot\skills\copywriting\
```

**macOS/Linux:**
```
~/.copilot/skills/copywriting/
```

## Usage

Type `/copywriting` in GitHub Copilot Chat, or just ask naturally:

- "Write homepage copy for [product]"
- "Improve this hero section — it sounds too AI"
- "Rewrite this landing page copy"
- "Write a pricing page for [product]"
- "This copy is weak, make it more compelling"

## What's inside

| File | Purpose |
|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `SKILL.md` | Main skill — copywriting principles, anti-AI rules, page frameworks, validation checklist |
| `references/anti-ai-patterns.md` | 50+ banned AI words, sentence patterns, structural tells, and human-writing signals |
| `references/copy-frameworks.md` | Headline formulas, page section types, structure templates |
| `references/natural-transitions.md` | Natural transition phrases with AI-tell warnings |

## Anti-AI highlights

The skill enforces:

- **Hard vocabulary ban** — "delve," "tapestry," "landscape" (figurative), "pivotal," "showcase," "foster," and 25+ more
- **Sentence pattern ban** — No dangling "-ing" editorial commentary, limited parallelisms
- **Structural pattern ban** — No rule-of-three everywhere, no challenges-then-optimism formula
- **Style rules** — Max 2 em dashes/page, no bold for emphasis in body text, varied list lengths
- **10-point validation checklist** — Applied before delivering any copy

## License

MIT
