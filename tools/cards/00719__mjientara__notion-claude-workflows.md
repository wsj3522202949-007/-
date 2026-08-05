---
id: tool-00719
type: tool
area: 库
status: active
tags: [协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: notion-claude-workflows
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/mjientara/notion-claude-workflows
created: 2026-07-18
updated: 2026-07-18
no: 719
category: 二、网文 / 长篇 AI 写作系统 库
repo: mjientara/notion-claude-workflows
stars: 0
url: https://github.com/mjientara/notion-claude-workflows
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# mjientara/notion-claude-workflows

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mjientara/notion-claude-workflows
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：ai-tools, automation, claude, mcp, notion, productivity, workflows
- **GitHub 描述**：Production-grade productivity workflows combining Notion and Claude — weekly OS, writing pipeline, decision log, meeting intelligence.
- **本地描述**：Production-grade productivity workflows combining Notion and Claude — weekly OS, writing pipeline, decision log, meeting intelligence.
- **拉取时间**：2026-07-23 23:00:00

---

# Notion + Claude Workflows

> Production-grade productivity workflows combining Notion and Claude Cowork. Built to replace — and outperform — enterprise alternatives like Microsoft Copilot and Google Gemini.

[![Tested with Claude](https://img.shields.io/badge/Tested_with-Claude_Sonnet-CC785C?style=flat&logo=anthropic&logoColor=white)](https://claude.ai)
[![Built for Notion](https://img.shields.io/badge/Built_for-Notion-000000?style=flat&logo=notion&logoColor=white)](https://notion.so)
[![Author](https://img.shields.io/badge/Author-Marcel_Jientara-7C3AED?style=flat)](https://github.com/mjientara)

Real workflows from real daily use. Not templates that look good in demos — systems that have survived contact with actual work.

---

## Why Notion + Claude beats enterprise AI assistants

Enterprise tools (Copilot, Gemini Workspace) are optimized for the *average* employee. Claude + Notion is optimized for *your specific context* — because you define the databases, the schemas, and the prompts.

The key insight: **Claude's context window is your knowledge base.** The better your Notion structure, the better Claude performs as a collaborator.

---

## Workflows

### 📋 Weekly Operating System
A complete weekly planning and review system.

- **Monday:** Claude pulls open tasks, drafts weekly priorities
- **Friday:** Claude reviews completions, carries forward blockers, drafts weekly summary
- Notion databases: `Tasks`, `Weekly Reviews`, `Projects`

→ `[See workflow](./weekly-os/)`

---

### ✍️ Writing Pipeline (Substack → GitHub)
How I write, edit, and publish essays across Substack and GitHub with zero friction.

- Draft in Notion → Review with Claude → Publish to Substack → Auto-sync to GitHub
- Claude role: structural feedback, headline variants, SEO optimization

→ `[See workflow](./writing-pipeline/)`

---

### 🎯 Decision Log
Never lose institutional memory. Every significant decision logged with context, alternatives considered, and outcome tracking.

- Claude helps fill in the "alternatives considered" section
- Searchable retrospective library

→ `[See workflow](./decision-log/)`

---

### 📊 Meeting Intelligence
From meeting notes to action items to follow-up drafts — without leaving Notion.

- Paste raw notes → Claude extracts actions, owners, deadlines
- Auto-populates Tasks database
- Drafts follow-up emails per attendee

→ `[See workflow](./meeting-intelligence/)`

---

## MCP Configuration

These workflows are supercharged when Claude has direct Notion access via MCP:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "OPENAPI_MCP_HEADERS": "{\"Authorization\": \"Bearer YOUR_TOKEN\", \"Notion-Version\": \"2022-06-28\"}"
      }
    }
  }
}
```

Full MCP setup guide → [mcp-server-configs](https://github.com/mjientara/mcp-server-configs)

---

## Getting started

1. Clone this repo
2. Pick a workflow from the list above
3. Follow the `SETUP.md` inside each workflow folder
4. Import the Notion template (link inside each folder)
5. Configure Claude with your Notion token via MCP

Each workflow has a `prompts.md` with the exact Claude prompts that power it.

---

## Structure

```
/
├── weekly-os/
│   ├── README.md
│   ├── SETUP.md
│   ├── prompts.md
│   └── notion-template-link.txt
├── writing-pipeline/
├── decision-log/
├── meeting-intelligence/
└── _shared/
    └── notion-schema-overview.md
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*By [Marcel Jientara](https://github.com/mjientara) · Read more at [Ahead by AI Design](https://mjientara.substack.com)*
