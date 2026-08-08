---
id: tool-00482
type: tool
area: 库
status: active
tags: [多Agent, Claude插件, 协议未明, 需API密钥, 英文文档]
title: claude-plugins
summary: 多 Agent 协作自动产文
source: https://github.com/cs-doug/claude-plugins
created: 2026-07-18
updated: 2026-07-18
no: 482
category: 二、网文 / 长篇 AI 写作系统 库
repo: cs-doug/claude-plugins
stars: 0
url: https://github.com/cs-doug/claude-plugins
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1814f95e36736599
  - methods/最强写作方法论_全球最强综合版.md
---

# cs-doug/claude-plugins

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/cs-doug/claude-plugins
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：claude-plugins is a ready-to-install AI engineering team for Claude Code and GitHub Copilot — 25 specialized agents (CTO, Security Architect, QA Engineer, FinOps, etc.) organized into 7 domain plugins, with 12 slash commands and 8 multi-agent orchestrator workflows that chain agents together for full SDLC tasks like PRD writing, code review, deploy
- **本地描述**：claude-plugins is a ready-to-install AI engineering team for Claude Code and GitHub Copilot — 25 specialized agents (CTO, Security Architect, QA Engineer, FinOps, etc.) organized into 7 domain plugins, with 12 slash commands and 8 multi-agent orchestrator workflows that chain agents together for full SDLC tasks like PRD writing, code review, deploy
- **拉取时间**：2026-07-23 22:53:08

---

# AI Agent Team

A team of **33 specialized AI agents** covering the full software engineering lifecycle — from strategy and architecture to development, testing, deployment, and marketing. Works on both **Claude Code** (primary) and **GitHub Copilot** (secondary) without maintaining duplicate configurations.

---

## The Team

### Leadership (6 agents)
| Agent | Model | Role |
|-------|-------|------|
| CTO | Opus | Technology strategy, build vs buy, architectural governance |
| VP of Engineering | Opus | Engineering excellence, DORA metrics, delivery velocity |
| Director of Engineering | Sonnet | Cross-team coordination, roadmap execution |
| Engineering Manager | Haiku | Sprint management, capacity planning, blocker removal |
| Product Manager | Sonnet | PRDs, user stories, prioritization (RICE), roadmap |
| Scrum Master | Haiku | Agile ceremonies, retrospectives, sprint health |

### Architecture (5 agents)
| Agent | Model | Role |
|-------|-------|------|
| Technical Architect | Opus | System design, TDDs, tech stack decisions, ADRs |
| Security Architect | Opus | Threat modeling (STRIDE), OWASP, compliance |
| Data Architect | Sonnet | Data modeling, ETL/ELT, data governance |
| AI/ML Architect | Sonnet | ML system design, MLOps, RAG, LLM integration |
| Architecture Docs Agent | Sonnet | Doc auditing, drift detection, ADR generation |

### Cloud (4 agents)
| Agent | Model | Role |
|-------|-------|------|
| AWS Cloud Architect | Sonnet | AWS Well-Architected, CDK/Terraform, multi-account |
| Azure Cloud Architect | Sonnet | Azure landing zones, Bicep/Terraform, Entra ID |
| GCP Cloud Architect | Sonnet | GKE, BigQuery, Workload Identity, VPC Service Controls |
| OCI Cloud Architect | Sonnet | Compartments, OKE, Autonomous Database |

### Engineering (15 agents)
| Agent | Model | Role |
|-------|-------|------|
| Full-Stack Developer | Sonnet | React/TypeScript, Node.js/Python, APIs, Docker |
| QA Engineer | Haiku | Test strategy, Playwright, Jest, automation |
| MongoDB DBA | Haiku | Schema design, indexing, aggregation pipelines |
| Prompt Engineer | Sonnet | Prompt optimization, RAG design, context engineering |
| Release Manager | Sonnet | Versioning, changelogs, deployment coordination |
| Technical Writer | Haiku | API docs, HOWTOs, runbooks, READMEs |
| Test Coverage Agent | Sonnet | Coverage audits, gap analysis, test generation |
| PR Reviewer | Sonnet | Azure DevOps PR reviews, diff analysis, line-level comments |
| PR Comment Resolver | Sonnet | Fetch open PR threads, fix code per reviewer feedback, auto-resolve threads |
| Code Reviewer | Opus | CLAUDE.md compliance, bug detection, git history analysis, confidence-scored findings |
| Code Simplifier | Opus | Simplify code for clarity and maintainability while preserving functionality |
| Comment Analyzer | — | Verify comment accuracy, detect comment rot, assess long-term maintainability |
| PR Test Analyzer | — | Review test coverage quality, identify critical gaps, evaluate behavioral coverage |
| Silent Failure Hunter | — | Audit error handling, catch blocks, and fallback logic for silent failures |
| Type Design Analyzer | — | Analyze type encapsulation and invariant expression; rate type design quality |

### Platform (2 agents)
| Agent | Model | Role |
|-------|-------|------|
| Corestack Expert | Haiku | Cloud governance, compliance policies, cost guardrails |
| FinOps Expert | Haiku | Cost analysis, rightsizing, reserved instances |

### Marketing (1 agent)
| Agent | Model | Role |
|-------|-------|------|
| Marketing/Content | Haiku | Blog posts, release announcements, marketing copy |

---

## Orchestrator Modes

Activate multi-agent workflows with a single command:

| Mode | Command | Agent Chain |
|------|---------|-------------|
| Plan Mode | `/orchestrators:prd-workflow` | PM → Technical Architect → Scrum Master |
| Brainstorming | `/orchestrators:brainstorm` | CTO → PM → AI/ML Architect |
| Development | `/orchestrators:full-sdlc` | Full-Stack Dev → QA → MongoDB DBA |
| Code Review | `/orchestrators:code-review-flow` | Technical Architect → Security Architect → Full-Stack Dev |
| Bug Fix | `/orchestrators:bug-fix-flow` | Full-Stack Dev → QA → Test Coverage Agent |
| Deployment | `/orchestrators:deploy-flow` | Cloud Architect → FinOps → QA |
| Documentation | `/orchestrators:doc-flow` | PM → Technical Writer → Prompt Engineer |
| Sprint Planning | `/orchestrators:sprint-workflow` | Scrum Master → Eng Manager → PM |

---

## Slash Commands

Commands are namespaced by plugin. Use `/plugin:command` syntax in Claude Code.

| Command | Plugin | Description |
|---------|--------|-------------|
| `/leadership:create-prd` | leadership | Create a Product Requirements Document |
| `/leadership:sprint-planning` | leadership | Run sprint planning with estimation and capacity check |
| `/architecture:create-tdd` | architecture | Create a Technical Design Document |
| `/architecture:threat-model` | architecture | Create a STRIDE threat model |
| `/architecture:update-architecture-docs` | architecture | Scan and update stale architecture documentation |
| `/cloud:cost-estimate` | cloud | Estimate cloud infrastructure costs |
| `/cloud:deploy` | cloud | Execute a deployment with health checks and rollback plan |
| `/engineering:code-review` | engineering | Multi-layer code review (quality + security + performance) |
| `/engineering:bug-fix` | engineering | Diagnose and fix a bug end-to-end |
| `/engineering:release-notes` | engineering | Generate release notes from git log |
| `/engineering:document` | engineering | Generate API docs, HOWTOs, READMEs, or runbooks |
| `/engineering:coverage-audit` | engineering | Audit test coverage and generate missing tests |
| `/engineering:pr-review` | engineering | Review an Azure DevOps PR and post line-level comments |
| `/engineering:pr-fix-comments` | engineering | Fetch open PR threads, fix code per comments, auto-resolve threads |
| `/engineering:code-review` | engineering | Comprehensive local code review using specialized agents (comments, tests, errors, types, code, simplify) |

---

## Repository Structure

```
.
├── .claude/
│   ├── CLAUDE.md                  # Agent memory foundation (all agents read this)
│   ├── settings.json              # Hook events + permissions config
│   ├── hooks/                     # 8 automation scripts
│   └── memory/                    # Shared project state
│       ├── project-state.md       # Tech stack, services, key decisions
│       ├── sprint-context.md      # Active sprint, tickets, capacity
│       └── decisions.md           # Architecture Decision Records (ADRs)
├── plugins/                       # Self-contained installable plugins
│   ├── leadership/                # /leadership:* commands
│   │   ├── .claude-plugin/plugin.json
│   │   ├── agents/                # 6 agents (CTO, VP Eng, Director, EM, PM, Scrum Master)
│   │   ├── skills/                # prd-writing, agile, project-context
│   │   └── commands/              # create-prd, sprint-planning
│   ├── architecture/              # /architecture:* commands
│   │   ├── .claude-plugin/plugin.json
│   │   ├── agents/                # 5 agents (Technical, Security, Data, AI/ML, Arch Docs)
│   │   ├── skills/                # architecture, security, tdd-writing, architecture-docs
│   │   └── commands/              # create-tdd, threat-model, update-architecture-docs
│   ├── cloud/                     # /cloud:* commands
│   │   ├── .claude-plugin/plugin.json
│   │   ├── agents/                # 4 agents (AWS, Azure, GCP, OCI)
│   │   ├── skills/                # cloud-aws, cloud-azure, cloud-gcp, cloud-oci
│   │   └── commands/              # cost-estimate, deploy
│   ├── engineering/               # /engineering:* commands
│   │   ├── .claude-plugin/plugin.json
│   │   ├── agents/                # 15 agents (Full-Stack, QA, MongoDB DBA, Prompt, Release, Writer, Test Coverage, PR Reviewer, PR Comment Resolver, Code Reviewer, Code Simplifier, Comment Analyzer, PR Test Analyzer, Silent Failure Hunter, Type Design Analyzer)
│   │   ├── skills/                # mongodb, prompt-engineering, test-coverage
│   │   └── commands/              # code-review, bug-fix, release-notes, document, coverage-audit, pr-review, pr-fix-comments
│   ├── platform/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── agents/                # 2 agents (Corestack, FinOps)
│   │   └── skills/                # finops, corestack
│   ├── marketing/
│   │   ├── .claude-plugin/plugin.json
│   │   └── agents/                # 1 agent (Marketing/Content)
│   └── orchestrators/             # /orchestrators:* commands
│       ├── .claude-plugin/plugin.json
│       └── commands/              # 8 multi-agent workflow orchestrators
├── .github/
│   ├── prompts/                   # Auto-generated Copilot prompts (from sync script)
│   ├── workflows/                 # CI: validation + prompt sync
│   └── instructions/              # Scoped Copilot instructions (arch/security/testing)
├── .mcp.json                      # MCP server config (Firecrawl, Perplexity, Playwright, Hunter, GitHub)
├── .claude-plugin/
│   └── marketplace.json           # Plugin registry (references all 7 plugin.json manifests)
├── .claude/scripts/
│   ├── setup-symlinks.sh          # One-time setup after clone
│   ├── sync-commands.sh           # Sync plugin commands → Copilot prompts
│   ├── ado_pr_review.py           # PR review: list PRs, fetch git diff, post line-level comments, discover CLAUDE.md, git history, prior PR comments
│   ├── ado_create_feature.py      # Create ADO Features
│   ├── ado_create_userstory.py    # Create ADO User Stories
│   ├── ado_create_task.py         # Create ADO Tasks
│   ├── ado_sprint_status.py       # Sprint burndown and health report
│   ├── ado_weekly_status.py       # Weekly leadership status email
│   ├── ado_capacity_plan.py       # Team capacity vs. workload
│   ├── ado_bulk_create.py         # Bulk Feature→Story→Task from JSON
│   └── requirements.txt           # Python dependencies (azure-devops)
├── docs/                          # Usage guides with real-world examples
│   ├── agents.md                  # All 25 agents with use cases
│   ├── commands.md                # All 12 commands with scenarios
│   └── orchestrators.md           # All 8 orchestrators with end-to-end examples
└── references/
    └── wshobson_agents/           # Reference: wshobson/agents (72 plugins, 496 agents)
```

---

## Quick Start

### 1. Clone and set up
```bash
git clone <this-repo>
cd my-ai-agent-team
bash .claude/scripts/setup-symlinks.sh
```

### 2. Configure MCP tools
Add to your shell profile (`.zshrc` / `.bashrc`):
```bash
export PERPLEXITY_API_KEY="your-key"
export FIRECRAWL_API_KEY="your-key"
export HUNTER_API_KEY="your-key"
export GITHUB_PERSONAL_ACCESS_TOKEN="your-token"
```

### 3. Fill in project context
Edit `.claude/memory/project-state.md` with your project's tech stack and context. Agents read this at session start.

### 4. Start using agents
```bash
# In Claude Code — just describe what you need:
"Design the authentication system for our API"        # → Technical Architect activates
"Write tests for src/orders/service.ts"               # → QA Engineer + Test Coverage Agent
"We have a 500 error on /api/checkout — fix it"       # → Full-Stack Dev + bug-fix-flow

# Or use plugin-namespaced commands directly:
/leadership:create-prd "user dashboard with analytics"
/orchestrators:code-review-flow --pr 142
/engineering:coverage-audit --threshold 80
```

---

## Compatibility

| Tool | Support | Method |
|------|---------|--------|
| Claude Code | ✅ Native | `.claude/` directory |
| GitHub Copilot | ✅ Via symlinks + sync | `.github/` directory |
| Cursor | ✅ Via AGENTS.md symlink | Root `AGENTS.md` |

The `.claude/scripts/setup-symlinks.sh` script wires everything up after clone. The `.claude/scripts/sync-commands.sh` script (also runs in CI on push) translates Claude commands to Copilot prompt format automatically.

---

## MCP Integrations

| Tool | Agents | Purpose |
|------|--------|---------|
| Perplexity | CTO, PM, Prompt Engineer | Web research and knowledge lookup |
| Firecrawl | PM, FinOps Expert | Web scraping and data extraction |
| Playwright | QA Engineer | Browser automation and E2E testing |
| Hunter | Marketing/Content | Email finding for outreach |
| GitHub MCP | Release Manager, Eng Manager | PR/issue/repo management |

---

## Documentation

| Doc | Contents |
|-----|----------|
| [docs/agents.md](https://github.com/cs-doug/claude-plugins/blob/main/docs/agents.md) | Usage guide for all 26 agents with real-world examples |
| [docs/commands.md](https://github.com/cs-doug/claude-plugins/blob/main/docs/commands.md) | Reference for all 12 slash commands with scenarios |
| [docs/orchestrators.md](https://github.com/cs-doug/claude-plugins/blob/main/docs/orchestrators.md) | Multi-agent workflow guide with end-to-end examples |
| [INSTRUCTIONS.MD](https://github.com/cs-doug/claude-plugins/blob/main/INSTRUCTIONS.MD) | Installation, setup, and configuration guide |

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Inspired By
- [wshobson/agents](https://github.com/wshobson/agents) — 72 plugin reference library (included as `references/wshobson_agents/`)
- [Anthropic Claude Plugins](https://github.com/anthropics/claude-code) — Official plugin examples (included as `references/claude-plugins-official/`); `code-review` plugin's confidence-scoring and multi-agent PR workflow patterns are incorporated into the engineering plugin
