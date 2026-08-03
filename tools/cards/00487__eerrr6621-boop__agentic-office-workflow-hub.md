---
id: tool-00487
type: tool
area: 库
status: active
tags: [多Agent, 互动叙事, Python, 协议未明, 需API密钥, 英文文档]
title: agentic-office-workflow-hub
summary: 多 Agent 协作自动产文
source: https://github.com/eerrr6621-boop/agentic-office-workflow-hub
created: 2026-07-18
updated: 2026-07-18
no: 487
category: 二、网文 / 长篇 AI 写作系统 库
repo: eerrr6621-boop/agentic-office-workflow-hub
stars: 0
url: https://github.com/eerrr6621-boop/agentic-office-workflow-hub
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# eerrr6621-boop/agentic-office-workflow-hub

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/eerrr6621-boop/agentic-office-workflow-hub
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Sanitized case study of an AI Agent office automation workflow with multi-channel delivery, knowledge-base writing, and server runtime evidence.
- **本地描述**：Sanitized case study of an AI Agent office automation workflow with multi-channel delivery, knowledge-base writing, and server runtime evidence.
- **拉取时间**：2026-07-23 22:53:16

---

# Agentic Office Workflow Hub

> A production-style AI office automation prototype that connects research, writing, knowledge capture, scheduled delivery, and multi-channel agent operations.

![status](https://img.shields.io/badge/status-sanitized%20demo-2f855a)
![agent](https://img.shields.io/badge/agent%20workflow-Codex%20%2B%20OpenClaw-2563eb)
![security](https://img.shields.io/badge/secrets-redacted-f97316)
![docs](https://img.shields.io/badge/docs-portfolio%20ready-0ea5e9)

## What This Project Proves

This repository documents a real server-side Agent workflow prototype that was used to validate:

- Multi-channel AI assistant routing through Feishu, WeChat, and a wearable-device bridge.
- Scheduled AI information delivery, including weather, noon AI news, and evening AI tools/skills briefings.
- Knowledge-base driven formal writing workflows for communications drafts, training reports, visit reports, and office materials.
- Operational guardrails: systemd services, cron jobs, delivery retries, health checks, log-based debugging, and controlled decommissioning.
- A later migration path from a brittle all-in-one Agent gateway to a cleaner Codex + MCP workflow.

The goal was not to build a toy chatbot. The goal was to test whether AI agents could become a practical personal office operating layer: researching, remembering, drafting, delivering, and monitoring work with minimal manual glue.

## Live Evidence

The screenshot below is generated from sanitized server terminal logs. It shows the Agent gateway startup, model routing, plugin registration, WeChat/Feishu/Rokid channel startup, scheduled cron workflows, delivery logs, and cleanup verification.

![Sanitized server runtime logs](server-agent-logs-sanitized-20260430.png)

## Architecture

```mermaid
flowchart LR
    User["User / Operator"] --> Codex["Codex Agent"]
    Codex --> MCP["MCP Tool Layer"]
    MCP --> Search["Search APIs<br/>Brave / Firecrawl / YouTube"]
    MCP --> Notion["Notion Knowledge Base"]
    MCP --> Docs["DOCX / Spreadsheet / Presentation Tools"]

    subgraph Server["Cloud Server Prototype"]
        Gateway["Agent Gateway"]
        Cron["Scheduled Jobs"]
        Guard["Delivery Guard<br/>retry + dedupe"]
        Logs["Runtime Logs"]
    end

    Gateway --> Feishu["Feishu Writing Assistant"]
    Gateway --> WeChat["WeChat Push Channel"]
    Gateway --> Rokid["Wearable Bridge Prototype"]
    Cron --> Guard
    Guard --> WeChat
    Gateway --> Logs
    Logs --> Evidence["Sanitized Evidence"]

    Codex --> Server
    Evidence --> GitHub["This Repository"]
```

## Core Outcomes

| Area | Outcome |
| --- | related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- |
| Agent runtime | Deployed and operated a server-side Agent gateway with model routing and plugin loading. |
| Multi-channel integration | Validated Feishu writing, WeChat push, and wearable-device bridge workflows. |
| Scheduled automation | Implemented morning weather, noon AI news, and evening AI tools/skills briefing schedules. |
| Delivery reliability | Added delivery guard behavior, status logs, retry paths, and fallback diagnostics. |
| Knowledge-driven writing | Organized source materials, best drafts, document patterns, constraints, and house style for formal Chinese writing. |
| Security posture | Produced a sanitized public version and intentionally excluded raw tokens, secrets, private chat screenshots, and credentials. |

## Repository Map

```text
.
├── README.md
├── APPLICATION_TEXT.md
├── ARCHITECTURE.md
├── IMPACT.md
├── OPERATIONS.md
├── SECURITY.md
├── WRITING_KNOWLEDGE_WORKFLOW.md
├── server-agent-logs-sanitized-20260430.png
├── server-agent-logs-sanitized-20260430.txt
├── agent-config.example.json
├── agent-crontab.example
├── agent-gateway.service.example
├── sanitize_logs.py
└── verify_no_secrets.py
```

## Why This Matters

Office work is usually fragmented: search in one place, draft in another, store materials somewhere else, then manually send reminders and summaries. This prototype explored the opposite direction: an Agent-centered workbench that can gather information, preserve context, generate formal outputs, and deliver them through real channels.

The most valuable lesson was architectural. A capable AI assistant should not hide everything inside one fragile bot. The more robust design is:

- Use Codex as the primary reasoning and production agent.
- Use MCP as the tool boundary for search, Notion, GitHub, YouTube, Firecrawl, and document work.
- Use small, inspectable services only when automation needs to run unattended.
- Keep secrets local or server-side, never inside public repositories.

## Security Note

This is a public, sanitized portfolio repository. Raw server archives, private knowledge bases, API tokens, conversation logs, and personal/company source materials are intentionally excluded.

See [SECURITY.md](SECURITY.md) for the sanitization policy.
