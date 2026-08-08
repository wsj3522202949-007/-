---
id: tool-00087
type: tool
area: 库
status: active
tags: [协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: prompt-engineering-os
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/edgeless-ai/prompt-engineering-os
created: 2026-07-18
updated: 2026-07-18
no: 87
category: 二、网文 / 长篇 AI 写作系统 库
repo: edgeless-ai/prompt-engineering-os
stars: 0
url: https://github.com/edgeless-ai/prompt-engineering-os
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: ded1b578529d147e
  - methods/最强写作方法论_全球最强综合版.md
---

# edgeless-ai/prompt-engineering-os

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/edgeless-ai/prompt-engineering-os
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：ai-agents, anthropic, claude, claude-code, llm, prompt-engineering, templates
- **GitHub 描述**：The complete system for writing AI prompts that work in production. 30 chapters, 8 template schemas, 100+ templates.
- **本地描述**：The complete system for writing AI prompts that work in production. 30 chapters, 8 template schemas, 100+ templates.
- **拉取时间**：2026-07-23 22:41:24

---

# The Prompt Engineering OS

[![Version](https://img.shields.io/badge/version-1.0.0-6366f1?style=flat-square)](https://github.com/edgeless-ai/prompt-engineering-os/releases)
[![License](https://img.shields.io/badge/license-MIT-10b981?style=flat-square)](LICENSE)

**Stop guessing. Start engineering.**

A structured system for writing AI prompts that work in production. 30 chapters, 8 template schemas, 100+ battle-tested templates.

Built from Anthropic's official documentation, 434 YouTube videos, academic research, and 18 months of real multi-agent pipeline work.

---

## The Core Four Framework

Every AI interaction optimizes four levers. When something isn't working, the fix is always one of these.

| Lever | What It Controls | Optimize For |
|-------|-----------------|-------------|
| **Context** | What the agent knows | Minimum viable context, not everything |
| **Model** | Which LLM runs it | Right-size to the task |
| **Prompt** | How the agent behaves | Structure over length |
| **Tools** | What the agent can do | Fewer focused tools over many generic |

When a pipeline fails, run through all four before rewriting anything. 90% of production failures trace back to one of these - not to a missing magic phrase.

---

## Template Selection Guide

Eight schemas. Pick the one that fits your situation.

| Schema | Use When |
|--------|----------|
| Skill Definition | Reusable workflow you'll call repeatedly |
| Slash Command | Lightweight, frequent operation |
| Agent System Prompt | Sub-agent in a multi-agent pipeline |
| Four-Block Prompt | One-shot structured request |
| ADW (YAML Workflow) | End-to-end automation |
| Mental Model (YAML) | Domain knowledge for agents |
| Closed-Loop | Task that needs to verify its own output |
| F-Thread Consensus | Multiple agents voting on a decision |

The full guide includes complete templates for all eight, with production examples and a decision tree.

---

## The Deadly Seven

The most common prompt mistakes. Each one seems reasonable. Each one consistently fails.

| Anti-Pattern | The Problem |
|-------------|------------|
| **Wall of Text** | Long unstructured paragraphs. The model loses signal in noise. |
| **Vague Success** | "Make it good." No measurable criteria = unpredictable output. |
| **Context Dumping** | Loading everything just in case. Dilutes attention on what matters. |
| **Missing Examples** | Describing desired output instead of showing it. |
| **No Self-Check** | Trusting output without verification steps. |
| **Monolith Prompt** | One giant prompt doing everything. Break it up. |
| **Adjectives Over Structure** | "Write a detailed, thorough..." is not a spec. |

The full guide breaks down each one with before/after examples and specific fixes.

---

## Key Patterns

Eight patterns extracted from 18 months of production use.

| Pattern | One-Liner |
|---------|-----------|
| Iron Law | Test first, code second |
| Reconnaissance | Look before you leap |
| One Question | Ask one thing at a time |
| Incremental Validation | Confirm before continuing |
| Black-Box Scripts | Use --help, not source code |
| Progressive Fallback | Try best option first, fall back gracefully |
| Simplicity Criterion | Simpler is better. Deletions that keep quality are wins. |
| Knowledge Delta | Compare new info against what you know before investing time |

---

## What's in the full system

The open-source content above is the framework overview. The full Prompt Engineering OS is a 30-chapter guide covering:

- **The Technique Hierarchy** - Anthropic's official 8 techniques, ordered by impact, with real examples (Chapters 4-11)
- **System Prompt Architecture** - how to design instructions that hold up under pressure (Chapter 12)
- **All 8 Template Schemas** - complete, copy-paste-ready templates with production examples (Chapter 13)
- **CLAUDE.md Engineering** - encoding your standards so you never re-explain them (Chapter 14)
- **The 7 Persuasion Principles for AI** - what actually influences model behavior and why (Chapter 17)
- **Multi-Agent Orchestration** - coordinator/worker patterns, subagent design, consensus voting (Chapters 20-24)
- **100+ Applied Templates** - for software engineering, writing, image generation, and business (Chapters 27-30)
- **Companion Files** - CLAUDE.md starter templates, skill schemas, quick reference cards (Pro tier)

**Available at [edgeless.gumroad.com](https://edgeless.gumroad.com/l/prompt-engineering-os)**

| Tier | Price | What's Included |
|------|-------|----------------|
| Starter | $29 | Full 30-chapter guide (HTML + PDF) |
| Professional | $59 | Guide + CLAUDE.md templates + skill schemas + reference cards |
| Team | $99 | Everything in Pro + 5-seat license + 12 months of updates |

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## About

Made by [Edgeless](https://edgeless.gumroad.com). Built for people who build with AI.

## License

The content in this repository is released under the [MIT License](https://github.com/edgeless-ai/prompt-engineering-os/blob/main/LICENSE). The full product is separately licensed - see the product page for terms.
