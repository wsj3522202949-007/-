---
id: tool-01036
type: tool
area: 库
status: active
tags: [提示词, 协议宽松, 需API密钥, 中文友好, 多Agent]
title: personal-review-prompt
summary: 提示词/写作工作流
source: https://github.com/zenia-liu/personal-review-prompt
created: 2026-07-18
updated: 2026-07-18
no: 1036
category: 二、网文 / 长篇 AI 写作系统 库
repo: zenia-liu/personal-review-prompt
stars: 0
url: https://github.com/zenia-liu/personal-review-prompt
tier: "C"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# zenia-liu/personal-review-prompt

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/zenia-liu/personal-review-prompt
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A structured AI prompt template for conducting in-depth personal experience reviews through a two-phase interview and writing process.
- **本地描述**：A structured AI prompt template for conducting in-depth personal experience reviews through a two-phase interview and writing process.
- **拉取时间**：2026-07-23 23:09:12

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Personal Experience Review Prompt Template

A structured AI prompt template for conducting in-depth personal experience reviews through a two-phase interview and writing process.

`[中文文档](README.zh-CN.md)`

## What Is This?

This is a prompt template designed to help you systematically review and reflect on any period of your life — career development, entrepreneurial journey, learning and growth, annual summary, and more.

Instead of asking AI to "help me write a review," this template turns AI into a professional interviewer who asks targeted follow-up questions phase by phase, and then produces a comprehensive review document with three parts:

1. **My Story** — A first-person chronological narrative of your experience
2. **An Observer's Commentary** — An objective third-party analysis of your patterns, strengths, and weaknesses
3. **Issues to Address** — Prioritized problems with actionable next steps

## How It Works

The template follows a two-phase process:

### Phase 1: Interview

You provide a rough starting point (timeline + brief description). The AI then asks follow-up questions to dig deeper into:

- What exactly you did (specific projects, actions, deliverables)
- Why you did it (context, motivation, catalyst)
- What the results were (outcomes, feedback, gains and losses)
- Your subjective feelings and thoughts at the time
- Causal relationships and turning points between events

The AI asks one direction at a time, never overwhelming you. When a period is covered, it moves on to the next.

### Phase 2: Writing

After the full interview, the AI produces a complete review document with the three parts described above.

## Quick Start

1. Go to `[`prompt/en.md`](prompt/en.md)` (or `[`prompt/zh-CN.md`](prompt/zh-CN.md)` for Chinese)
2. Copy the **System Instructions** block
3. Paste it at the beginning of a new AI conversation
4. Follow it with your own opening narrative, e.g.:

> I want to review my career development over the past year. The starting point is June 2025. I had just left Company A because... Then I spent two months job hunting... In September, I joined Company B... Start by asking me follow-up questions about these, and after you're done, I'll continue with what happened next.

**Tip:** If you use Claude Projects, paste the System Instructions into the Project's Custom Instructions for automatic application in every new conversation.

## File Structure

```
personal-review-prompt/
├── README.md              # English README (this file)
├── README.zh-CN.md        # Chinese README
├── prompt/
│   ├── en.md              # English prompt template
│   └── zh-CN.md           # Chinese prompt template
├── examples/
│   ├── en.md              # English example output
│   └── zh-CN.md           # Chinese example output
└── LICENSE                # MIT License
```

## Design Principles

- **Interview-first approach**: The AI doesn't jump to conclusions — it asks questions first to understand your full story
- **One question at a time**: Never overwhelming, always focused
- **Objective and direct**: No excessive comfort or flattery — honest analysis is the goal
- **Actionable output**: Every identified issue comes with concrete next steps
- **Priority-based problem solving**: Foundational issues > high-leverage issues > specific skill gaps

## Compatible AI Tools

This template works with any AI model that supports system instructions or long-context conversations, including:

- Claude (Anthropic)
- ChatGPT (OpenAI)
- Gemini (Google)
- DeepSeek
- And other similar AI assistants

## License

`[MIT](LICENSE)` — Feel free to use, modify, and distribute.
