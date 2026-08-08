---
id: tool-01698
type: tool
area: 库
status: active
tags: [提示词, 协议未明, 本地优先, 英文文档, 多Agent, 本地写作]
title: agent-prompts
summary: 提示词/写作工作流
source: https://github.com/rsvertiz/agent-prompts
created: 2026-07-18
updated: 2026-07-18
no: 1698
category: 二、网文 / 长篇 AI 写作系统 库
repo: rsvertiz/agent-prompts
stars: 0
url: https://github.com/rsvertiz/agent-prompts
tier: "C"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 82c001d8648d02a0
  - methods/最强写作方法论_全球最强综合版.md
---

# rsvertiz/agent-prompts

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rsvertiz/agent-prompts
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Reusable AI agent prompt library for .NET development projects. Includes specialized agents for architecture review, security auditing, feature planning, test writing, documentation, and truth-keeping.
- **本地描述**：Reusable AI agent prompt library for .NET development projects. Includes specialized agents for architecture review, security auditing, feature planning, test writing, documentation, and truth-keeping.
- **拉取时间**：2026-07-23 23:28:32

---

# Agent Prompts Library

A reusable library of AI agent system prompts for .NET development projects.
Each agent is a specialist with a clearly defined role, responsibilities, and output format.
Built to work with Claude Projects or any Claude-compatible interface.

---

## The Team

| Agent | Role | When to Call |
|---|---|---|
| [Architect](https://github.com/rsvertiz/agent-prompts/blob/main/agents/architect/prompt.md) | Code review & pattern enforcement | Before every commit |
| [Security Auditor](https://github.com/rsvertiz/agent-prompts/blob/main/agents/security-auditor/prompt.md) | Security & compliance review | Any change touching APIs, storage, or credentials |
| [Feature Planner](https://github.com/rsvertiz/agent-prompts/blob/main/agents/feature-planner/prompt.md) | Backlog & implementation breakdown | Before starting any new feature |
| [Test Writer](https://github.com/rsvertiz/agent-prompts/blob/main/agents/test-writer/prompt.md) | Unit test generation | After any new Service or ViewModel |
| [Doc Keeper](https://github.com/rsvertiz/agent-prompts/blob/main/agents/doc-keeper/prompt.md) | Documentation maintenance | After any merged feature |
| [Lighthouse](https://github.com/rsvertiz/agent-prompts/blob/main/agents/lighthouse/prompt.md) | Truth, integrity & hallucination detection | Before planning, before merging, when something feels off |

---

## Workflow

```
                    [ LIGHTHOUSE ]
                     watches all
                          ↓
[Planner] → [You Build] → [Architect] → [Security Auditor]
                                               ↓
                    [Doc Keeper] ← [Test Writer]
```

The Lighthouse sits above the pipeline and can be called at any point.
It has authority to challenge the output of any other agent.

---

## How to Use an Agent

1. Open the agent's `prompt.md`
2. Copy everything inside the triple-backtick `SYSTEM PROMPT` block
3. Paste it as the system prompt in a new Claude Project
4. Update the `PROJECT CONTEXT` block at the top with your project's details
5. Start a conversation — paste code, plans, or diffs as your message

That's it. No code, no SDK, no setup beyond a Claude account.

---

## How to Reuse for a New Project

The `PROJECT CONTEXT` block at the top of each `prompt.md` is the **only section you need to change** per project. Everything else — responsibilities, output format, constraints — is universal.

**Steps:**
1. Copy `project-context.template.json` and fill in your project's details
2. Open each agent's `prompt.md` and replace the `PROJECT CONTEXT` block using your template values
3. Paste the updated prompt into a Claude Project as the system prompt
4. Adapting all 6 agents to a new project takes roughly 15-20 minutes

---

## Repository Structure

```
/agents
  /architect
    prompt.md          ← system prompt + usage guide
  /security-auditor
    prompt.md
  /feature-planner
    prompt.md
  /test-writer
    prompt.md
  /doc-keeper
    prompt.md
  /lighthouse
    prompt.md
project-context.template.json   ← fill this in for each new project
CHANGELOG.md                    ← version history for all agent prompts
README.md
```

---

## Versioning & Improvement

Each prompt has a version number in its header. When an agent misses something real on a project, that's a bug — open an issue, improve the prompt, bump the version, and log it in `CHANGELOG.md`.

This library should get sharper with every project that uses it.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Projects Using This Library

- [smart-budget-tracker](https://github.com/rsvertiz/smart-budget-tracker) — AI-driven personal financial management app (.NET MAUI 9)
