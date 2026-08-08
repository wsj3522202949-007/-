---
id: tool-01260
type: tool
area: 库
status: active
tags: [提示词, 协议未明, 本地优先, 英文文档, 多Agent, 本地写作]
title: poppet-rp-framework
summary: 提示词/写作工作流
source: https://github.com/huzderu/poppet-rp-framework
created: 2026-07-18
updated: 2026-07-18
no: 1260
category: 二、网文 / 长篇 AI 写作系统 库
repo: Huzderu/poppet-rp-framework
stars: 15
url: https://github.com/huzderu/poppet-rp-framework
tier: "B"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 7045a320a2e5081f
  - methods/最强写作方法论_全球最强综合版.md
---

# Huzderu/poppet-rp-framework

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/huzderu/poppet-rp-framework
- **Stars**：15
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Comprehensive prompt engineering framework that eliminates AI writing failures and enforces ultra-realistic character behavior in roleplay. Includes COT template and specialized prompts for authentic reactions, physical realism, and plot progression.
- **本地描述**：Comprehensive prompt engineering framework that eliminates AI writing failures and enforces ultra-realistic character behavior in roleplay. Includes COT template and specialized prompts for authentic reactions, physical realism, and plot progression.
- **拉取时间**：2026-07-23 23:15:50

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Poppet - Ultra-Realism Anti Slop SillyTavern Preset

A comprehensive SillyTavern preset designed to eliminate common AI writing failures and enforce ultra-realistic character behavior in roleplay scenarios.

## What It Solves

**Common AI Problems:**
- Purple prose and melodramatic reactions ("words hit like a physical blow", "Not X but Y")
- Echoing user's words
- Characters knowing things they shouldn't (omniscience violations)
- Unrealistic physical capabilities
- Plot stagnation and reactive-only responses
- Generic emotional responses ignoring character background
- Meta-convenient solutions and wish-fulfillment scenarios
- Overly serious characters lacking natural humor
- Dialogue-heavy scenes missing body language and non-verbal cues

## Core Components

**Chain of Thought (COT) Template:** 10-section mandatory thinking process that forces systematic evaluation of realism, character consistency, plot progression, and technical implementation before generating responses.

**Specialized Prompts:**
- Authentic Reactions (anti-melodrama)
- Anti-Convenience Protocol
- Skill Limitations & Economic Reality  
- Natural Humor & Levity
- Non-Verbal Communication
- Physical Realism constraints
- Cultural authenticity checks

## Features

- **Ultra-realism focus:** Characters behave like actual people, not fictional archetypes
- **Setting-adaptable:** Works across modern, historical, and fantasy contexts
- **Anti-stagnation:** Built-in checks for plot progression and user engagement
- **Comprehensive coverage:** Addresses technical writing, psychology, world-building, and pacing

Tested primarily with Google Gemini but should work with any thinking instruction-following LLM (Deepseek Reasoner, GPT, Claude).
