---
id: tool-01810
type: tool
area: 库
status: active
tags: [提示词, 协议未明, 本地优先, 英文文档, 多Agent, 本地写作]
title: ai-prompts
summary: 提示词/写作工作流
source: https://github.com/soufianeoi/ai-prompts
created: 2026-07-18
updated: 2026-07-18
no: 1810
category: 二、网文 / 长篇 AI 写作系统 库
repo: soufianeoi/ai-prompts
stars: 0
url: https://github.com/soufianeoi/ai-prompts
tier: "C"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# soufianeoi/ai-prompts

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/soufianeoi/ai-prompts
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Curated, tested prompt library for coding, writing, analysis, and creative tasks - organized by category with expected outputs
- **本地描述**：Curated, tested prompt library for coding, writing, analysis, and creative tasks - organized by category with expected outputs
- **拉取时间**：2026-07-23 23:31:50

---

<div align="center">
  <img src="https://img.shields.io/badge/ai-prompts-8A2BE2?style=for-the-badge" alt="AI Prompts">
  <img src="https://img.shields.io/badge/31%20prompts-00c853?style=for-the-badge" alt="31 Prompts">
  <img src="https://img.shields.io/badge/license-MIT-00c8ff?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-ff6b35?style=for-the-badge" alt="PRs Welcome">
</div>

<br>

<div align="center">
  <h1>AI Prompts</h1>
  <p><em>Curated, tested, production-ready prompts organized by category</em></p>
  <p><strong>Good prompts get good outputs.</strong></p>
</div>

---

A collection of carefully crafted prompts for various AI tasks. Every prompt includes the category, use case, expected output, and optimization tips. Designed to be copy-pasted and adapted immediately.

## Quick Start

1. Browse a category below
2. Find a prompt that matches your task
3. Copy the prompt template
4. Replace the `[bracketed]` placeholders with your specifics

## Categories

| Category | Prompts | Description |
|----------|---------|-------------|
| [Coding](coding/) | 7 | Code generation, debugging, refactoring, architecture, testing |
| [Writing](writing/) | 6 | Articles, emails, docs, commit messages, product copy, press releases |
| [Analysis](analysis/) | 6 | Sentiment, research, decisions, SWOT, data extraction, competitive analysis |
| [Creative](creative/) | 6 | Characters, worlds, game mechanics, brainstorming, dialogue, poetry |
| [Reasoning](reasoning/) | 6 | Chain-of-thought, logic puzzles, debate, first principles, ethics, decision trees |

## Prompt Index

### Coding

| Prompt | Best For |
|--------|----------|
| [Debug an Error](coding/debug-error.md) | Finding root causes from stack traces |
| [Code Review](coding/code-review.md) | Getting senior-engineer-level PR feedback |
| [Refactor Legacy Code](coding/refactor-legacy-code.md) | Modernizing old code safely |
| [Write Unit Tests](coding/write-unit-tests.md) | Comprehensive test coverage |
| [Design a REST API](coding/design-api.md) | Complete API specs with schemas |
| [Explain Code](coding/explain-code.md) | Understanding unfamiliar code |
| [Optimize a Database Query](coding/optimize-query.md) | Fixing slow queries with indexing |

### Writing

| Prompt | Best For |
|--------|----------|
| [Write a Technical Article](writing/technical-article.md) | Blog posts and tutorials |
| [Write a Cold Email](writing/cold-email.md) | Outreach that gets replies |
| [Write API Documentation](writing/api-docs.md) | Developer-friendly API docs |
| [Write a Git Commit Message](writing/commit-message.md) | Conventional commits done right |
| [Write a Product Description](writing/product-description.md) | Converting product copy |
| [Write a Press Release](writing/press-release.md) | Professional announcements |

### Analysis

| Prompt | Best For |
|--------|----------|
| [Sentiment Analysis](analysis/sentiment-analysis.md) | Tone and emotion detection |
| [Research Summary](analysis/research-summary.md) | Distilling papers and articles |
| [Decision Matrix](analysis/decision-matrix.md) | Weighted option comparison |
| [SWOT Analysis](analysis/swot-analysis.md) | Strategic positioning |
| [Data Extraction](analysis/data-extraction.md) | Structured data from text |
| [Competitive Analysis](analysis/competitive-analysis.md) | Market gap identification |

### Creative

| Prompt | Best For |
|--------|----------|
| [Character Design](creative/character-design.md) | Memorable story/game characters |
| [World Building](creative/world-building.md) | Immersive fictional settings |
| [Game Mechanic Design](creative/game-mechanic.md) | Balanced, fun game systems |
| [Brainstorming Session](creative/brainstorming.md) | Diverse idea generation |
| [Dialogue Writing](creative/dialogue-writing.md) | Natural character conversations |
| [Poetry Generation](creative/poetry.md) | Form-conscious verse |

### Reasoning

| Prompt | Best For |
|--------|----------|
| [Chain of Thought](reasoning/chain-of-thought.md) | Step-by-step problem solving |
| [Logic Puzzle Solver](reasoning/logic-puzzle.md) | Grid puzzles and deduction |
| [Debate Analysis](reasoning/debate-analysis.md) | Balanced multi-perspective analysis |
| [First Principles](reasoning/first-principles.md) | Breaking down assumptions |
| [Ethical Dilemma](reasoning/ethical-dilemma.md) | Multi-framework ethics |
| [Decision Tree](reasoning/decision-tree.md) | Risk-aware choice mapping |

## Prompt Format

Every prompt follows this structure:

```markdown
# Title

**Category:** category
**Model:** Recommended models
**Use case:** What this solves

## Prompt

The actual prompt template with [placeholders].

## Expected Output

What you should expect from a good response.

## Tips

- Model-specific recommendations
- Parameter adjustments
- Variations to try
```

## Model Recommendations

| Task Type | Recommended Model | Temperature |
|-----------|------------------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Code generation | Claude / GPT-4 | 0 - 0.3 |
| Creative writing | Claude / GPT-4 | 0.7 - 1.0 |
| Analysis | GPT-4 / Claude | 0 - 0.3 |
| Brainstorming | Any (high temp) | 0.9+ |
| Reasoning | Claude / GPT-4 | 0 - 0.3 |
| Technical docs | Claude / GPT-4 | 0.3 - 0.5 |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new prompts.

## License

MIT &mdash; use freely, adapt widely.
