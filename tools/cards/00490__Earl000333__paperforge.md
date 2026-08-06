---
id: tool-00490
type: tool
area: 库
status: active
tags: [提示词, Claude插件, 协议未明, 本地优先, 中文友好, 多Agent, 本地写作]
title: paperforge
summary: 提示词/写作工作流
source: https://github.com/earl000333/paperforge
created: 2026-07-18
updated: 2026-07-18
no: 490
category: 二、网文 / 长篇 AI 写作系统 库
repo: Earl000333/paperforge
stars: 3
url: https://github.com/earl000333/paperforge
tier: "B"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Earl000333/paperforge

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/earl000333/paperforge
- **Stars**：3
- **语言**：None
- **License**：None
- **Topics**：academic-writing, ai-writing, claude, codex, cursor, latex, paper-writing, patent-writing, prompt-engineering, research-writing
- **GitHub 描述**：AI research writing, reusable agent skills, and paper-to-patent prompt workflows.
- **本地描述**：AI research writing, reusable agent skills, and paper-to-patent prompt workflows.
- **拉取时间**：2026-07-23 22:53:22

---

# PaperForge

![PaperForge](https://github.com/Earl000333/paperforge/blob/main/assets/banner.png)

**English** | [简体中文](https://github.com/Earl000333/paperforge/blob/main/README.zh-CN.md)

PaperForge is a bilingual repository for AI research writing, reusable agent-native prompt workflows, and paper-to-patent drafting. The project organizes prompt templates, `SKILL.md` packs, writing guides, and visual assets into a structure designed for browsing, reuse, and extension.

## Scope

| Area | Contents |
| --- | --- |
| Research Writing | Translation, rewriting, polishing, logic checking, experiment analysis, reviewer-style auditing |
| Agent Reuse | `SKILL.md` packages for Codex, Claude Code, and Cursor |
| Patent Drafting | Technical problem extraction, solution framing, implementation writing, and claim-seed drafting |

## Repository Structure

![Knowledge Map](https://github.com/Earl000333/paperforge/blob/main/assets/prompt-map.svg)

```text
PaperForge
├─ assets/                        # Banner, maps, and visual diagrams
├─ docs/                          # Guides and structure docs
├─ prompts/                       # Standalone prompt templates
│  ├─ 01-translation/
│  ├─ 02-revision/
│  ├─ 03-analysis/
│  ├─ 04-visuals/
│  ├─ 05-strategy/
│  └─ 06-patent/
├─ skills/                        # Reusable SKILL.md packs for agents
├─ images/                        # Supporting images and screenshots
├─ README.md
└─ README.zh-CN.md
```

## Entry Points

### Prompt Library

[prompts/README.md](https://github.com/Earl000333/paperforge/blob/main/prompts/README.md)

- translation between Chinese and English
- academic rewriting and polishing
- logic review and de-AI rewriting
- experiment analysis and reviewer-style auditing
- figure, table, and architecture-diagram writing
- paper-to-patent drafting

### Skill Packs

[skills/README.md](https://github.com/Earl000333/paperforge/blob/main/skills/README.md)

| Tool | Directory |
| --- | --- |
| Codex | `~/.codex/skills/<skill-name>/SKILL.md` |
| Claude Code | `.claude/skills/<skill-name>/SKILL.md` |
| Cursor | `.cursor/skills/<skill-name>/SKILL.md` or a compatible skills directory |

### Documentation

1. [docs/knowledge-base.md](https://github.com/Earl000333/paperforge/blob/main/docs/knowledge-base.md)
2. [docs/skill-adoption.md](https://github.com/Earl000333/paperforge/blob/main/docs/skill-adoption.md)
3. [docs/paper-to-patent-guide.md](https://github.com/Earl000333/paperforge/blob/main/docs/paper-to-patent-guide.md)
4. [docs/structure-tree.md](https://github.com/Earl000333/paperforge/blob/main/docs/structure-tree.md)

## Prompt Index

| Category | Module | File |
| --- | --- | --- |
| Translation | Chinese to English | [prompts/01-translation/zh-to-en.md](https://github.com/Earl000333/paperforge/blob/main/prompts/01-translation/zh-to-en.md) |
| Translation | English to Chinese | [prompts/01-translation/en-to-zh.md](https://github.com/Earl000333/paperforge/blob/main/prompts/01-translation/en-to-zh.md) |
| Translation | Chinese to academic Chinese | [prompts/02-revision/zh-to-zh-academic-rewrite.md](https://github.com/Earl000333/paperforge/blob/main/prompts/02-revision/zh-to-zh-academic-rewrite.md) |
| Revision | Shorten | [prompts/02-revision/shorten.md](https://github.com/Earl000333/paperforge/blob/main/prompts/02-revision/shorten.md) |
| Revision | Expand | [prompts/02-revision/expand.md](https://github.com/Earl000333/paperforge/blob/main/prompts/02-revision/expand.md) |
| Revision | English polish | [prompts/02-revision/english-polish.md](https://github.com/Earl000333/paperforge/blob/main/prompts/02-revision/english-polish.md) |
| Revision | Chinese polish | [prompts/02-revision/chinese-polish.md](https://github.com/Earl000333/paperforge/blob/main/prompts/02-revision/chinese-polish.md) |
| Revision | Logic check | [prompts/02-revision/logic-check.md](https://github.com/Earl000333/paperforge/blob/main/prompts/02-revision/logic-check.md) |
| Revision | De-AI (LaTeX English) | [prompts/02-revision/de-ai-latex.md](https://github.com/Earl000333/paperforge/blob/main/prompts/02-revision/de-ai-latex.md) |
| Revision | De-AI (Word Chinese) | [prompts/02-revision/de-ai-word.md](https://github.com/Earl000333/paperforge/blob/main/prompts/02-revision/de-ai-word.md) |
| Analysis | Experiment analysis | [prompts/03-analysis/experiment-analysis.md](https://github.com/Earl000333/paperforge/blob/main/prompts/03-analysis/experiment-analysis.md) |
| Analysis | Reviewer audit | [prompts/03-analysis/reviewer-audit.md](https://github.com/Earl000333/paperforge/blob/main/prompts/03-analysis/reviewer-audit.md) |
| Visuals | Paper architecture diagram | [prompts/04-visuals/paper-architecture-diagram.md](https://github.com/Earl000333/paperforge/blob/main/prompts/04-visuals/paper-architecture-diagram.md) |
| Visuals | Figure recommendation | [prompts/04-visuals/experiment-figure-recommendation.md](https://github.com/Earl000333/paperforge/blob/main/prompts/04-visuals/experiment-figure-recommendation.md) |
| Visuals | Figure caption | [prompts/04-visuals/figure-caption.md](https://github.com/Earl000333/paperforge/blob/main/prompts/04-visuals/figure-caption.md) |
| Visuals | Table caption | [prompts/04-visuals/table-caption.md](https://github.com/Earl000333/paperforge/blob/main/prompts/04-visuals/table-caption.md) |
| Strategy | Model selection | [prompts/05-strategy/model-selection.md](https://github.com/Earl000333/paperforge/blob/main/prompts/05-strategy/model-selection.md) |
| Patent | Paper to patent | [prompts/06-patent/paper-to-patent.md](https://github.com/Earl000333/paperforge/blob/main/prompts/06-patent/paper-to-patent.md) |

## Skill Index

| Skill | Purpose | File |
| --- | --- | --- |
| `paper-zh-to-en` | Convert Chinese research drafts into English LaTeX | [skills/paper-zh-to-en/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-zh-to-en/SKILL.md) |
| `paper-en-to-zh` | Directly translate English paper text into Chinese | [skills/paper-en-to-zh/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-en-to-zh/SKILL.md) |
| `paper-zh-rewrite` | Rewrite rough Chinese notes into academic Chinese prose | [skills/paper-zh-rewrite/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-zh-rewrite/SKILL.md) |
| `paper-shorten` | Compress English paper text with minimal semantic loss | [skills/paper-shorten/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-shorten/SKILL.md) |
| `paper-expand` | Expand sparse English academic text with stronger logic | [skills/paper-expand/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-expand/SKILL.md) |
| `paper-polish-en` | Deep polish for English paper writing | [skills/paper-polish-en/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-polish-en/SKILL.md) |
| `paper-polish-zh` | Formal polish for Chinese paper writing | [skills/paper-polish-zh/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-polish-zh/SKILL.md) |
| `paper-logic-check` | Audit logical gaps and evidence chains | [skills/paper-logic-check/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-logic-check/SKILL.md) |
| `paper-humanize-latex` | Remove obvious AI traces from English LaTeX | [skills/paper-humanize-latex/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-humanize-latex/SKILL.md) |
| `paper-humanize-word` | Remove obvious AI traces from Chinese Word prose | [skills/paper-humanize-word/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-humanize-word/SKILL.md) |
| `paper-experiment-analysis` | Turn result tables into paper-ready analysis text | [skills/paper-experiment-analysis/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-experiment-analysis/SKILL.md) |
| `paper-reviewer-audit` | Review a paper like a conference reviewer | [skills/paper-reviewer-audit/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-reviewer-audit/SKILL.md) |
| `paper-to-patent` | Turn paper content into patent-oriented technical writing | [skills/paper-to-patent/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-to-patent/SKILL.md) |

## Paper-to-Patent Module

![Paper to Patent Flow](https://github.com/Earl000333/paperforge/blob/main/assets/patent-flow.svg)

| In a Paper | In Patent-Oriented Writing |
| --- | related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- |
| Research problem | Technical problem |
| Contribution | Technical solution |
| Method modules | Device units or method steps |
| Algorithm flow | Implementation procedure |
| Experimental outcome | Technical effect |
| Comparative analysis | Support for scope and utility |

Direct prompt entry: [prompts/06-patent/paper-to-patent.md](https://github.com/Earl000333/paperforge/blob/main/prompts/06-patent/paper-to-patent.md)

Reusable skill entry: [skills/paper-to-patent/SKILL.md](https://github.com/Earl000333/paperforge/blob/main/skills/paper-to-patent/SKILL.md)
