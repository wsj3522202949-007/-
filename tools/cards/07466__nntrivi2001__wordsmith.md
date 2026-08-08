---
id: tool-07466
type: tool
area: 库
status: active
tags: [RAG, Claude插件, Python, 协议传染, 本地优先, 英文文档, 人物设定, 本地写作]
title: wordsmith
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/nntrivi2001/wordsmith
created: 2026-07-18
updated: 2026-07-18
no: 7466
category: 画龙补充 / 扩容入库 — 补充源
repo: nntrivi2001/wordsmith
stars: 2
url: https://github.com/nntrivi2001/wordsmith
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1451741599ea1098
  - methods/QUICK_START.md
---

# nntrivi2001/wordsmith

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/nntrivi2001/wordsmith
- **Stars**：2
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：ai-writing, claude-code, plugin, story-generator, vietnamese, webnovel, wordsmith
- **GitHub 描述**：Webnovel Writer - Long-form web novel creation system built on Claude Code
- **本地描述**：wordsmith
- **拉取时间**：2026-07-25 19:22:46

---

# Wordsmith

Long-form webnovel writing system with integrated Vietnamese writing patterns.

## Features

- 8 skills: write, plan, review, init, query, resume, dashboard, learn
- 7 specialized agents for consistency, continuity, pacing, and more
- RAG with local vector index
- Vietnamese writing patterns from 4 reference sources

## Installation

Add to `CLAUDE_PLUGIN_PATHS` in your Claude Code settings:

```json
{
  "CLAUDE_PLUGIN_PATHS": [
    "/path/to/wordsmith"
  ]
}
```

## Usage

```bash
/wordsmith-write        # Write a new chapter
/wordsmith-write --fast # Fast mode
/wordsmith-plan         # Plan plot/outline
/wordsmith-review       # Review written chapter
/wordsmith-init         # Initialize new project
/wordsmith-dashboard    # Open visual dashboard
/wordsmith-learn        # Extract patterns from session
```

## Vietnamese Writing Rules

See `STYLE_GUIDE_VN.md` for full details.

Key rules:
- Units: Use `mét, cm, km, kg` (not Chinese units)
- Dialogue: `"Content" - action tag`
- Inner thoughts: Third-person, no quotes
- Minimum 8 words per sentence
- Scene breaks: `---` for major, `*— Hết Chương X —*` for end

## Structure

```
wordsmith/
├── skills/        # 8 main skills
├── agents/        # 7 specialized agents
├── references/    # Shared references
├── genres/       # Genre-specific templates
├── scripts/       # Python scripts
├── dashboard/     # Web dashboard
└── STYLE_GUIDE_VN.md
```

## Author

nntrivi2001

## Version

| version | notes |
|------|---related:
  - methods/QUICK_START.md
---|
| **v1.0.0 (current)** | Initial release |

