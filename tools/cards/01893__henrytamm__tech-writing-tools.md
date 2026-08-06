---
id: tool-01893
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: tech-writing-tools
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/henrytamm/tech-writing-tools
created: 2026-07-18
updated: 2026-07-18
no: 1893
category: 二、网文 / 长篇 AI 写作系统 库
repo: henrytamm/tech-writing-tools
stars: 0
url: https://github.com/henrytamm/tech-writing-tools
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# henrytamm/tech-writing-tools

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/henrytamm/tech-writing-tools
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Automation tools for technical writing workflows — Slack intake processing, doc request routing, version control automation, and more.
- **本地描述**：Automation tools for technical writing workflows — Slack intake processing, doc request routing, version control automation, and more.
- **拉取时间**：2026-07-23 23:34:10

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# tech-writing-tools

A collection of automation tools for technical writing workflows. Built to eliminate repetitive tasks and let writers focus on writing.

These tools were born from real documentation work — managing DITA XML content, coordinating with engineering teams, and handling intake requests across Slack and work item trackers. Each one started as a manual process that took too long.

## Tools

### [Slack Intake Processor](https://github.com/henrytamm/tech-writing-tools/tree/main/slack-intake-processor/)

An AI agent that monitors a Slack channel for documentation requests on a daily schedule. It validates completeness, asks follow-up questions when info is missing, creates work items, routes to the right writer, and sends a daily summary.

**Impact:** Eliminated 30-60 minutes of daily manual triage. Requests are acknowledged in minutes instead of hours.

### [Doc Request Skill](https://github.com/henrytamm/tech-writing-tools/tree/main/doc-request-skill/)

An AI-powered slash command that lets anyone submit documentation requests through natural language. It classifies complexity (typo fix vs. new feature), only asks for what's actually needed, and creates the work item + Slack post in one step.

**Impact:** Reduced request submission from a 15-field form to a single sentence. Incomplete requests are caught immediately instead of discovered days later.

### [P4 Changelist Automation](https://github.com/henrytamm/tech-writing-tools/tree/main/p4-changelist-automation/)

A shell script that automates Perforce changelist creation for documentation workflows. Opens files, creates a properly-formatted changelist, and moves everything into it — one command instead of 5-10 manual steps.

**Impact:** Changelist creation went from 5-10 minutes of error-prone typing to a single command.

### [Release Note Drafter](https://github.com/henrytamm/tech-writing-tools/tree/main/release-note-drafter/)

Two AI-powered skills that automate release note creation end-to-end:
- **`/rn-drafter`** — Full scaffolding: creates DITA XML topic, updates ditamap, reltable, and parent topic, creates a version control changelist. One command produces 4 file edits.
- **`/rn-short-desc`** — Content drafting assistant: generates 3 options for the short description following strict style guidelines, then drafts the Where/When/How body.

**Impact:** Release note creation went from 30-45 minutes of manual file editing to ~2 minutes of answering prompts.

### [MCP Auth Utilities](https://github.com/henrytamm/tech-writing-tools/tree/main/mcp-auth-utilities/)

Slash commands for managing MCP (Model Context Protocol) server authentication and profiles:
- Browser-based OAuth flow
- Device Code Flow for headless/SSH environments
- Profile switching for multi-workflow setups

**Impact:** Auth management becomes a one-liner instead of hunting for binaries and environment variables.

### [Resume PDF Generator](https://github.com/henrytamm/tech-writing-tools/tree/main/resume-pdf-generator/)

A Python script that generates a clean, single-page resume PDF from structured data. No LaTeX, no Word — version-controlled and reproducible.

## Philosophy

1. **Automate the boring parts.** Writers should write, not copy-paste between Slack and Jira.
2. **Adapt to the user.** A typo report doesn't need the same form as a new feature request.
3. **Never block.** A partial request in the system is better than a complete request that never gets filed.
4. **Dedup before everything.** The worst automation outcome is duplicate work items.

## Tech Stack

- **Shell scripts** for version control automation (Perforce)
- **Python** (ReportLab) for PDF generation
- **YAML + AI prompts** for agent-based automation (MCP-compatible AI tooling)
- **Slack + work item tracker integrations** via MCP (Model Context Protocol)

## Setup

Each tool has its own README with setup instructions. Most require:

- An MCP-compatible AI coding tool for the AI-powered skills
- Python 3.9+ for the PDF generator
- Perforce CLI (`p4`) for the changelist tool
- MCP integrations for Slack and your work item tracker

## License

MIT
