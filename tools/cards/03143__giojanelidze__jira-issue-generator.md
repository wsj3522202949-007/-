---
id: tool-03143
type: tool
area: 库
status: active
tags: [Claude插件, 协议未明, 需API密钥, 英文文档]
title: jira-issue-generator
summary: Claude Code 插件式写作流
source: https://github.com/giojanelidze/jira-issue-generator
created: 2026-07-18
updated: 2026-07-18
no: 3143
category: 六、多 Agent 小说生产 / 叙事引擎 库
repo: giojanelidze/jira-issue-generator
stars: 1
url: https://github.com/giojanelidze/jira-issue-generator
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 46f245d17b2e20b9
  - methods/网文写作最强SOP.md
---

# giojanelidze/jira-issue-generator

- **分类**：六、多 Agent 小说生产 / 叙事引擎 库
- **链接**：https://github.com/giojanelidze/jira-issue-generator
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：An AI-powered pipeline that transforms Figma designs into fully structured Jira issues. Three specialized agents work in sequence — analyzing designs, creating Epics, breaking them into User Stories, and decomposing Stories into Sub-tasks — all with human-in-the-loop confirmation at every step.
- **本地描述**：An AI-powered pipeline that transforms Figma designs into fully structured Jira issues. Three specialized agents work in sequence — analyzing designs, creating Epics, breaking them into User Stories, and decomposing Stories into Sub-tasks — all with human-in-the-loop confirmation at every step.
- **拉取时间**：2026-07-23 23:50:48

---

# Jira Pipeline Automator

An AI-powered pipeline that transforms Figma designs into fully structured Jira issues. Three specialized agents work in sequence — analyzing designs, creating Epics, breaking them into User Stories, and decomposing Stories into Sub-tasks — all with human-in-the-loop confirmation at every step.

## How It Works

The pipeline runs as a single continuous session inside [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Each agent reads the output of the previous one and feeds the next:

```
Figma Design
     │
     ▼
┌─────────────┐     ┌──────────────────┐     ┌───────────────────┐
│ Epic Creator │ ──▶ │ Story Creator    │ ──▶ │ Sub-tasks Creator │
│  (Agent 1)   │     │   (Agent 2)      │     │    (Agent 3)      │
└─────────────┘     └──────────────────┘     └───────────────────┘
     │                      │                         │
     ▼                      ▼                         ▼
  Jira Epic           Jira Stories            Jira Sub-tasks
  (EZSP-1)         (EZSP-2, EZSP-3…)      (EZSP-10, EZSP-11…)
```

## Agents

### 1. Epic Creator (`epic_creator.md`)

Analyzes a Figma design and creates a Jira Epic capturing the feature's goal, target user, and scope.

**What it does:**
- Parses the Figma URL and fetches the design via the Figma REST API
- Identifies screens, core functionality, target users, and UI patterns
- Drafts an Epic with a polished ADF description (overview, scope, Figma link)
- Runs a duplicate check before creation
- Sets custom fields: CAPEX, Feature Type, Market Place

**Inputs (collected interactively if not provided):**

| Field | Required | Default |
|-------|----------|---------|
| Figma URL | Yes | — |
| Feature description | Yes | — |
| CAPEX | No | `No` |
| Feature Type | No | `New` |
| Market Place | No | `.com` |

**Outputs:** `epic_key`, `epic_summary`, `screens`, `features`, `target_user`, `figma_url`

---

### 2. User Story Creator (`user_story_creator.md`)

Takes the Epic context and breaks the feature into focused, INVEST-style User Stories — one per screen or per discrete user goal.

**What it does:**
- Loads Epic context from the previous agent (or re-fetches Figma data if needed)
- Drafts Stories with proper user-story sentences, acceptance criteria (min 3 per Story, at least 1 non-happy-path), and design references
- Runs per-Story duplicate checks
- Verifies Epic linkage after creation (with automatic fallback repair)
- Reports partial failures with a recovery table

**Outputs:** `story_keys`, `stories` (key, summary, screen, URL)

related:
  - methods/网文写作最强SOP.md
---

### 3. Sub-tasks Creator (`sub-tasks_creator.md`)

Analyzes each Story and decides whether it needs decomposition into implementation-oriented Sub-tasks. Skips atomic Stories.

**What it does:**
- Fetches full Story details from Jira (description + acceptance criteria)
- Applies a necessity check — only creates sub-tasks when genuinely needed (multi-discipline, parallel work, complex scope)
- Tags each sub-task by engineering discipline: `[FE]`, `[BE]`, `[QA]`, `[Design]`, `[Analytics]`
- Verifies parent Story linkage after creation

**Outputs:** `subtask_keys`, `subtasks` (key, summary, discipline, parent Story), `skipped_stories`

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and authenticated
- [Atlassian Rovo MCP server](https://www.npmjs.com/package/@anthropic/claude-code-mcp-atlassian) configured (preferred) or Jira REST API access
- A Figma Personal Access Token
- A Jira API token with issue creation permissions on your target project

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repo-url>
   cd jira-pipeline-automator
   ```

2. **Configure credentials** in `config.json`:

   ```json
   {
     "figma_token": "your-figma-personal-access-token",
     "jira_email": "your-email@company.com",
     "jira_domain": "https://your-domain.atlassian.net",
     "jira_token": "your-jira-api-token",
     "jira_project_key": "YOUR_PROJECT"
   }
   ```

3. **Update `claude.md`** if your Jira project key differs from the default.

## Usage

Start Claude Code in the project directory and run the pipeline:

```bash
claude
```

Then tell Claude to run the pipeline:

```
Run the pipeline for this Figma design:
https://www.figma.com/design/ABC123/My-Feature?node-id=100-200
```

Or run step-by-step:

```
Run epic_creator for:
- Figma: https://www.figma.com/design/ABC123/My-Feature?node-id=100-200
- Description: A new onboarding flow for first-time users
```

Each agent will:
1. Collect any missing inputs interactively
2. Analyze the design / context
3. Show a **confirmation preview** and wait for your approval
4. Create the Jira issues only after you type `confirm`

## Safety & Guardrails

Every agent enforces these protections:

- **Confirmation gates** — Nothing is created in Jira without explicit user approval. You can confirm all, a subset, or abort.
- **Duplicate detection** — JQL-based dedup checks run before every creation to prevent duplicate issues.
- **No hallucination** — Agents never fabricate Jira keys, screen names, or field values. Missing information triggers a prompt, not a guess.
- **Partial-failure recovery** — If a batch fails mid-way, a recovery table shows exactly what was created so nothing is lost.
- **Secrets handling** — Tokens are never logged, echoed, or written into Jira issue bodies.
- **Project scoping** — Agents refuse to write to any project other than the configured key.
- **Input validation** — Figma URLs, field values, and labels are validated against strict patterns before use.

## Project Structure

```
.
├── claude.md                 # Orchestrator — defines the pipeline and environment
├── config.json               # Credentials and project configuration
├── epic_creator.md           # Agent 1 — Figma → Jira Epic
├── user_story_creator.md     # Agent 2 — Epic → User Stories
├── sub-tasks_creator.md      # Agent 3 — Stories → Sub-tasks
└── README.md
```

## Customization

### Custom Fields

Each agent owns the Jira custom field mappings for its issue type. To update field IDs or allowed values:

- Epic fields → `epic_creator.md` (CAPEX, Feature Type, Market Place)
- Story fields → `user_story_creator.md` (priority, labels)
- Sub-task fields → `sub-tasks_creator.md` (priority, assignee)

### Adding a New Market

Add the new market code and its Jira option ID to the Market Place mapping table in `epic_creator.md`.

### Changing the Target Project

1. Update `jira_project_key` in `config.json`
2. Update the project key references in `claude.md` and all three agent specs
3. Verify that Epic, Story, and Sub-task issue types exist in the new project

## License

Private — internal use only.
