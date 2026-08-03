---
id: tool-05049
type: tool
area: 库
status: active
tags: [TTS, Claude插件, 协议宽松, 本地优先, 英文文档, 本地写作]
title: stop-slop
summary: 小说转语音/有声书
source: https://github.com/tpffounder/stop-slop
created: 2026-07-18
updated: 2026-07-18
no: 5049
category: 一、去 AI 味 / Humanizer 库
repo: tpffounder/stop-slop
stars: 0
url: https://github.com/tpffounder/stop-slop
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# tpffounder/stop-slop

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/tpffounder/stop-slop
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Claude Code skill: AI slop detector — catch slop in prose, UI copy, and code before shipping
- **本地描述**：Claude Code skill: AI slop detector — catch slop in prose, UI copy, and code before shipping
- **拉取时间**：2026-07-25 18:04:13

---

# Stop Slop

A skill for removing AI tells from prose.

<img width="3840" height="2160" alt="G-Yg4RVbIAAhVxW" src="https://github.com/user-attachments/assets/902afc15-1f40-4a9d-af24-8cd67afb8ebf" />

## What this is

AI writing has patterns. Predictable phrases, structures, rhythms. This skill teaches Claude (or any LLM) to catch and remove them.

## Skill Structure

```
stop-slop/
├── SKILL.md              # Core instructions
├── references/
│   ├── phrases.md        # Phrases to remove
│   ├── structures.md     # Structural patterns to avoid
│   └── examples.md       # Before/after transformations
├── README.md
└── LICENSE
```

## Quick start

**Claude Code:** Add this folder as a skill.

**Claude Projects:** Upload `SKILL.md` and reference files to project knowledge.

**Custom instructions:** Copy core rules from `SKILL.md`.

**API calls:** Include `SKILL.md` in your system prompt. Reference files load on demand.

## What it catches

**Banned phrases** - Throat-clearing openers, emphasis crutches, business jargon, all adverbs, vague declaratives, meta-commentary. See `references/phrases.md`.

**Structural clichés** - Binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency, narrator-from-a-distance voice, passive voice. See `references/structures.md`.

**Sentence-level rules** - No Wh- sentence starters, no em dashes, no staccato fragmentation, no lazy extremes, active voice required.

## Scoring

Rate 1-10 on each dimension:

| Dimension | Question |
|-----------|-------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds human? |
| Density | Anything cuttable? |

Below 35/50: revise.

## Author

[Hardik Pandya](https://hvpandya.com)

## License

MIT. Use freely, share widely.
