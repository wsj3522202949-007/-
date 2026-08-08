---
id: tool-01499
type: tool
area: 库
status: active
tags: [Shell, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: okr-copilot
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/dmytro-yarmak/okr-copilot
created: 2026-07-18
updated: 2026-07-18
no: 1499
category: 二、网文 / 长篇 AI 写作系统 库
repo: dmytro-yarmak/okr-copilot
stars: 2
url: https://github.com/dmytro-yarmak/okr-copilot
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4bf7fabad7efd53c
  - methods/最强写作方法论_全球最强综合版.md
---

# dmytro-yarmak/okr-copilot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/dmytro-yarmak/okr-copilot
- **Stars**：2
- **语言**：Shell
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered OKR assistant toolkit with persona-based reviews (CEO, team lead, IC) and skills for writing outcome-oriented OKRs, defining KRs (outcome/output/input), and checking alignment to strategy.
- **本地描述**：AI-powered OKR assistant toolkit with persona-based reviews (CEO, team lead, IC) and skills for writing outcome-oriented OKRs, defining KRs (outcome/output/input), and checking alignment to strategy.
- **拉取时间**：2026-07-23 23:22:48

---

# OKR Co-pilot

> AI as your OKR co-pilot, not an autopilot.

This repository provides tools, personas, and skills for using AI to enhance your OKR (Objectives and Key Results) process while keeping humans in the driver's seat.

## Philosophy

**Co-pilot, not Autopilot**: AI assists your strategic thinking but doesn't take over.

- One question at a time
- Human makes all final decisions
- AI challenges, suggests, and refines - never dictates

## Practice Context

Use our fictional company **Nexora** to practice OKR creation. The company context is spread across multiple documents — just like in a real organization:

| Document | Description |
|----------|-------------|
| [Q4 2025 Board Update](https://github.com/dmytro-yarmak/okr-copilot/blob/main/context/nexora-docs/q4-2025-board-update.md) | Financials, ARR, margins, cash position, risks |
| [Strategy Memo 2026](https://github.com/dmytro-yarmak/okr-copilot/blob/main/context/nexora-docs/strategy-memo-2026.md) | CEO's vision, strategic pillars, priorities |
| [All-Hands Notes — Jan 2026](https://github.com/dmytro-yarmak/okr-copilot/blob/main/context/nexora-docs/all-hands-notes-jan-2026.md) | Leadership updates, challenges, Q&A |
| [Product Roadmap H1 2026](https://github.com/dmytro-yarmak/okr-copilot/blob/main/context/nexora-docs/product-roadmap-h1-2026.md) | AI features, enterprise hardening, tech debt |
| [Competitive Landscape](https://github.com/dmytro-yarmak/okr-copilot/blob/main/context/nexora-docs/competitive-landscape-q1-2026.md) | Competitor profiles, win/loss analysis |
| [Sales Pipeline Report](https://github.com/dmytro-yarmak/okr-copilot/blob/main/context/nexora-docs/sales-pipeline-q1-2026.md) | Pipeline by segment, top deals, team metrics |
| [Customer Success Review](https://github.com/dmytro-yarmak/okr-copilot/blob/main/context/nexora-docs/customer-success-review-q4-2025.md) | Churn, NPS, health scores, expansion |
| [Hiring Plan 2026](https://github.com/dmytro-yarmak/okr-copilot/blob/main/context/nexora-docs/hiring-plan-2026.md) | Headcount, critical roles, attrition data |

**Exercise:** Ask Claude to synthesize these documents into a company overview, then use it to create team-level OKRs.

---

## Quick Start

### 1. Set Co-pilot Mode

Start any AI session with this opening prompt:

```
You are my OKR co-pilot. Ask one question at a time.
I'm the driver - I make all final decisions.
Start by asking: What's the most important thing your team needs to achieve?
```

### 2. Use Expert Personas

Get different perspectives on your OKRs:

| Persona | Best For | Key Focus |
|---------|----------|-----------|
| [Christina Wodtke](https://github.com/dmytro-yarmak/okr-copilot/blob/main/personas/christina-wodtke.md) | Focus & prioritization | "Is this the ONE thing?" |
| [John Doerr](https://github.com/dmytro-yarmak/okr-copilot/blob/main/personas/john-doerr.md) | Ambition & alignment | "Is this ambitious enough?" |
| [OKR Champion](https://github.com/dmytro-yarmak/okr-copilot/blob/main/personas/okr-champion.md) | Process & facilitation | "Have you aligned with others?" |
| [CEO](https://github.com/dmytro-yarmak/okr-copilot/blob/main/personas/ceo.md) | Strategy & vision | "Does this move us toward our vision?" |
| [Team Member](https://github.com/dmytro-yarmak/okr-copilot/blob/main/personas/team-member.md) | Reality & execution | "Can we actually do this?" |

### 3. Set Ground Rules Once

Define organizational OKR rules to reuse in future sessions:

[`/okr-ground-rules`](https://github.com/dmytro-yarmak/okr-copilot/blob/main/skills/okr-ground-rules.md) or `$okr-ground-rules` - Helps you define:
- OKR levels and cycle cadence
- Focus limits (<=3 Objectives, 2-4 KRs)
- OKR type expectations (aspirational, committed, learning)
- KR design, ownership, alignment, transparency, and incentives

Rules are saved in [`context/okr-ground-rules.md`](https://github.com/dmytro-yarmak/okr-copilot/blob/main/context/okr-ground-rules.md).

### 4. Draft, Rewrite, Review, and Audit

Use separate skills for drafting vs KR rewriting vs refinement vs strict audit:

- [`/okr-write`](https://github.com/dmytro-yarmak/okr-copilot/blob/main/skills/okr-write.md) or `$okr-write` - Guided draft creation from scratch (one question at a time)
- [`/okr-outcome-kr`](https://github.com/dmytro-yarmak/okr-copilot/blob/main/skills/okr-outcome-kr.md) or `$okr-outcome-kr` - Convert input/output KRs into stronger outcome KRs with KPI grounding
- [`/okr-review`](https://github.com/dmytro-yarmak/okr-copilot/blob/main/skills/okr-review.md) or `$okr-review` - Guided refinement of an existing draft (one question at a time)
- [`/okr-audit`](https://github.com/dmytro-yarmak/okr-copilot/blob/main/skills/okr-audit.md) or `$okr-audit` - Mostly autonomous expert scorecard and risk audit

Backward compatibility:
- If `/okr-review` or `$okr-review` is used for strict audit, it routes to `okr-audit`.
- If review starts without a draft, it asks for paste/link or routes to `okr-write`.

## For Codex CLI Users

Clone the repo, then install Codex skills from this repository:

```bash
./scripts/install-codex-skills.sh
```

Or use the Make target:

```bash
make install-codex-skills
```

What this does:

- Copies skills from `codex-skills/` into `~/.codex/skills/`
- Installs `okr-ground-rules`, `okr-write`, `okr-outcome-kr`, `okr-review`, and `okr-audit` for `$skill-name` invocation

Then restart Codex and use:

- `$okr-ground-rules`
- `$okr-write`
- `$okr-outcome-kr`
- `$okr-review`
- `$okr-audit`

## For Claude Code Users

Copy this repo and use with Claude Code:

1. Clone the repository
2. The `CLAUDE.md` file configures personas and skills
3. Use `@persona-name` to activate a perspective
4. Use `/okr-ground-rules` to set reusable rules
5. Use `/okr-write` to draft new OKRs
6. Use `/okr-outcome-kr` to convert weak KRs into outcome KRs
7. Use `/okr-review` to refine draft OKRs
8. Use `/okr-audit` for strict scorecard audit

## MCP Integrations

Connect your OKR co-pilot to:

- **Google Docs** - Collaborative OKR documents
- **Jira** - Link OKRs to execution
- **Oboard** - OKR management platform

See the `/mcp` directory for integration guides.

## Resources

- [Radical Focus](https://www.amazon.com/Radical-Focus-Achieving-Important-Objectives/dp/0996006028) by Christina Wodtke
- [Measure What Matters](https://www.whatmatters.com/) by John Doerr
- [What Matters](https://www.whatmatters.com/) - OKR resources and examples

## Contributing

This repo is designed to be forked and customized for your organization. Add your own:

- Personas (industry experts, internal leaders)
- Skills (your OKR workflow)
- MCP integrations (your tools)

## License

MIT - Use freely, modify for your needs.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*Created for the webinar: "AI as Your OKR Co-pilot, Not an Autopilot"*
