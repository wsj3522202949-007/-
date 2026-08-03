---
id: tool-01604
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: aiready-skills
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/getaiready/aiready-skills
created: 2026-07-18
updated: 2026-07-18
no: 1604
category: 二、网文 / 长篇 AI 写作系统 库
repo: getaiready/aiready-skills
stars: 0
url: https://github.com/getaiready/aiready-skills
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# getaiready/aiready-skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/getaiready/aiready-skills
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：agent-skills, ai-agents, ai-coding, aiready, best-practices, claude, code-quality, copilot, cursor, procedural-knowledge, skills, skills-sh
- **GitHub 描述**：AIReady best practices skill for AI agents - procedural knowledge for writing maintainable code
- **本地描述**：AIReady best practices skill for AI agents - procedural knowledge for writing maintainable code
- **拉取时间**：2026-07-23 23:25:50

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# @aiready/skills

> AI-friendly coding practices packaged as agent skills for the [skills.sh](https://skills.sh/) ecosystem.

[![npm version](https://img.shields.io/npm/v/@aiready/skills.svg)](https://npmjs.com/package/@aiready/skills)

## Overview

This package provides procedural knowledge for AI coding agents to help them write and maintain code optimally.

## 🏛️ Architecture

```
                    🎯 USER
                      │
                      ▼
         🎛️  @aiready/cli (orchestrator)
          │     │     │     │     │     │     │     │     │
          ▼     ▼     ▼     ▼     ▼     ▼     ▼     ▼     ▼
        [PAT] [CTX] [CON] [AMP] [DEP] [DOC] [SIG] [AGT] [TST]
          │     │     │     │     │     │     │     │     │
          └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
                               │
                               ▼
                      🏢 @aiready/core

Legend:
  PAT = pattern-detect        CTX = context-analyzer
  CON = consistency           AMP = change-amplification
  DEP = deps-health           DOC = doc-drift
  SIG = ai-signal-clarity     AGT = agent-grounding
  TST = testability
  SKL = @aiready/skills ★  (support package — provides AI assistant skill files, not a scorer)
  ★   = YOU ARE HERE
```

## Available Skills

### aiready-best-practices

Guidelines for writing AI-friendly code. Use when:

- Writing new features or refactoring
- Reviewing pull requests
- Preparing codebases for AI adoption

## Installation

### For [skills.sh](https://skills.sh/)

```bash
npx skills add caopengau/aiready-skills
```

### For [Playbooks.com (Paks)](https://playbooks.com/)

```bash
paks install aiready-best-practices
```

## License

MIT
