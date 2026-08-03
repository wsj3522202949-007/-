---
id: tool-01388
type: tool
area: 库
status: active
tags: [Claude插件, 协议未明, 本地优先, 英文文档, 本地写作]
title: BA-delivery-toolkit
summary: Claude Code 插件式写作流
source: https://github.com/martajuliazielinska/ba-delivery-toolkit
created: 2026-07-18
updated: 2026-07-18
no: 1388
category: 二、网文 / 长篇 AI 写作系统 库
repo: martajuliazielinska/BA-delivery-toolkit
stars: 0
url: https://github.com/martajuliazielinska/ba-delivery-toolkit
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# martajuliazielinska/BA-delivery-toolkit

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/martajuliazielinska/ba-delivery-toolkit
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI agent toolkit for IT Business Analysts in delivery models. Eight agents: input quality gate, discovery, Lotus Blossom expansion, backlog prioritization, definition of ready, user story writing, decision logging, and AC validation. Built with Claude Code. Compatible with Copilot 365.
- **本地描述**：AI agent toolkit for IT Business Analysts in delivery models. Eight agents: input quality gate, discovery, Lotus Blossom expansion, backlog prioritization, definition of ready, user story writing, decision logging, and AC validation. Built with Claude Code. Compatible with Copilot 365.
- **拉取时间**：2026-07-23 23:19:36

---

# BA Delivery Toolkit
**AI agents for Business Analysts — built for delivery teams**

*Author: Marta Julia Zielinska | v1.2 | May 2026*

---

## What is this?

A set of AI agents designed to help Business Analysts do their daily work faster and more consistently.

Instead of starting from scratch on every project, you give an agent the right input — and it produces a structured first draft. You review it, approve it, and move on.

**The rule is simple: AI drafts. You decide.**

---

## The Core Problem This Toolkit Solves

AI output is only as good as the input it receives. A weak brief produces weak requirements. Weak requirements produce rework. Rework is the most expensive thing in delivery.

The toolkit addresses this at every stage — starting with a quality gate before any AI generation begins.

---

## The Eight Agents

| # | Agent | Command | When to use |
|---|---|---|---|
| 0 | Push Back Agent | `/check-input [brd/epic/story]` | Always first — validates input quality |
| 1a | Discovery Agent | `/discover` | After PASS — maps requirements from transcript |
| 1b | Discovery Expansion | `/expand` | After PASS but problem too broad — Lotus Blossom |
| 2 | Backlog Prioritization | `/prioritize` | Before sprint — ranks requirements |
| 3 | Definition of Ready | `/check-dor` | Before dev handover — validates story |
| 4 | User Story Agent | `/create-story [feature] [persona]` | Writes story + Gherkin AC |
| 5 | Decision Log | `/log-session` | End of every session |
| 6 | AC Validator | `/validate-ac` | After build — compares to original AC |

---

## Agent Details

### 0. Push Back Agent — `/check-input [brd|epic|story]`
**What it does:** Evaluates input quality before any generation starts. Returns PASS or FAIL with specific questions to ask the business. Includes SCAMPER technique for when the business is stuck.
**Rule:** One FAIL criterion is enough to stop. Never generates requirements from weak input.

### 1a. Discovery Agent — `/discover`
**What it does:** Takes meeting notes or brief and structures them into requirements per stakeholder with success metrics.
**Only runs after:** `/check-input` returns PASS.

### 1b. Discovery Expansion Agent — `/expand`
**What it does:** Uses the Lotus Blossom technique to map 8 broad areas around a validated problem. BA picks 1-2 areas to expand into 8 specific questions each. Narrows focus before requirements are written.
**Use when:** Problem is valid but too wide for /discover to produce focused output.

### 2. Backlog Prioritization Agent — `/prioritize`
**What it does:** Scores and ranks requirements using RICE framework before sprint planning.

### 3. Definition of Ready Agent — `/check-dor`
**What it does:** Checks every story against DoR checklist before dev handover. PASS or FAIL with specific gaps listed.

### 4. User Story Agent — `/create-story [feature] [persona]`
**What it does:** Writes one story at a time in standard format with Gherkin AC. Waits for BA approval before next story.

### 5. Decision Log Agent — `/log-session`
**What it does:** Records decisions made each session — what, why, what next. Run at end of every session without exception.

### 6. AC Validator — `/validate-ac`
**What it does:** Compares finished build against original AC. Returns gap table — Met, Partial, Not Met.

---

## The Flow INPUT (transcript / BRD / brief)
↓
/check-input → FAIL? → Questions to business → SCAMPER if stuck → try again
↓ PASS
Problem broad? → /expand (Lotus Blossom) → narrow focus
↓
/discover → Requirements map
↓
/prioritize → Ranked backlog
↓
/create-story → User story + AC
↓
/check-dor → PASS?
↓
Dev handover
↓
/validate-ac → Gap report
↓
/log-session → Decision log updated Human approves every step. No agent proceeds without BA sign-off.

---

## POC Hypothesis

A structured quality gate between AI-generated content and BA approval reduces rework loops in delivery.

**Baseline:** Clarification meetings per sprint + stories returned from dev.
**Success:** Fewer meetings. Fewer returned stories.
**Failure:** Same or more rework despite using agents.

---

## Compatibility

| Tool | Status | Notes |
|---|---|---|
| Claude Code | ✅ Full — all 8 agents | Requires API key |
| Copilot 365 | ✅ Partial — manual prompts | No automation, copy instructions |
| Copilot Studio | ✅ Partial — 4 agents | Requires Jira + Confluence connectors |
| Rovo (Atlassian) | 🔄 Planned | |

---

## How to Start

1. Copy `projects/template/` → rename to your project
2. Fill in `PROJECT.md` — 15 minutes, once per project
3. Run `/check-input brd` → paste your brief
4. PASS → `/expand` if broad, `/discover` if focused
5. End every session with `/log-session`

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*MIT License | Marta Julia Zielinska 2026*
