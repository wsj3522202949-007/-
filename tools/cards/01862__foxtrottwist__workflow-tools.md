---
id: tool-01862
type: tool
area: 库
status: active
tags: [提示词, Claude插件, 校对, Shell, 协议宽松, 本地优先, 英文文档, 改稿润色, 本地写作]
title: workflow-tools
summary: 错别字/语法/风格校对
source: https://github.com/foxtrottwist/workflow-tools
created: 2026-07-18
updated: 2026-07-18
no: 1862
category: 二、网文 / 长篇 AI 写作系统 库
repo: foxtrottwist/workflow-tools
stars: 1
url: https://github.com/foxtrottwist/workflow-tools
tier: "B"
use_case: "错别字/语法/风格校对"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 78cf955fee399ed7
  - methods/最强写作方法论_全球最强综合版.md
---

# foxtrottwist/workflow-tools

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/foxtrottwist/workflow-tools
- **Stars**：1
- **语言**：Shell
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Claude Code plugin — task orchestration, writing tools, prompt development, context migration, code auditing, and macOS Shortcuts automation
- **本地描述**：Claude Code plugin — task orchestration, writing tools, prompt development, context migration, code auditing, and macOS Shortcuts automation
- **拉取时间**：2026-07-23 23:33:17

---

# workflow-tools

A Claude Code plugin bundling ten skills and four specialized agents for productivity and development workflows.

## What's included

### Productivity Skills

| Skill | Trigger | What it does |
|-------|---------|--------------|
| **iter** | `/iter`, "help me build", "implement", "research" | Task orchestration with verification gates. Auto-detects development or knowledge work mode. |
| **writing** | `/write`, "compose", "draft", "proofread" | Written communication with quality standards. Compose, proofread, or create professional content. |
| **instruction-dev** | `/instruction-dev`, "create a prompt", "write a CLAUDE.md", "review my skill" | Instruction authoring for prompt templates, CLAUDE.md, skills, and agent definitions. |
| **sharpen** | "sharpen", "refine my thinking", "focus this idea" | Refine raw thoughts into focused statements of intent through guided questioning. |
| **chat-migration** | `/chat-migration`, "save context", "hitting context limit" | Capture conversation context into structured handoff documents for new chats. |
| **code-audit** | `/code-audit`, "verify documentation", "check docs match code" | Documentation-code alignment verification using parallel subagents. |
| **azure-devops** | "review PR", "PR comments", "az repos", "az devops" | Azure DevOps CLI recipes for PR operations via `az repos` and `az devops invoke`. |
| **scaffold** | "set up project", "scaffold" | Set up a project for agent-assisted development with feedback loops and guardrails. |

### Development Discipline Skills

| Skill | Trigger | What it does |
|-------|---------|--------------|
| **tdd** | Starting feature work, bug fixes, refactoring | Enforce RED-GREEN-REFACTOR discipline. No production code without a failing test. |
| **systematic-debugging** | Bugs, test failures, unexpected behavior | Find root cause before proposing fixes. Investigation-first approach. |

### Agents

| Agent | Role |
|-------|---related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| **researcher** | Deep information gathering and synthesis |
| **verifier** | Adversarial review of completed work against acceptance criteria |
| **orchestrator** | Task decomposition and planning for multi-step work |
| **editor** | Review written content against quality standards |

## Install

```
/plugin marketplace add Foxtrottwist/workflow-tools
/plugin install workflow-tools@workflow-tools
```

Or from the CLI:

```bash
claude plugin marketplace add Foxtrottwist/workflow-tools
claude plugin install workflow-tools@workflow-tools
```

## Development

### Local testing

```bash
claude --plugin-dir .
```

Running `/doctor` during local development will show a warning about `CLAUDE_PLUGIN_ROOT` being missing. This is expected — Claude Code sets that variable automatically at install time.

### Structure

```
workflow-tools/
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
├── .mcp.json
├── skills/
│   ├── iter/
│   ├── writing/
│   ├── instruction-dev/
│   ├── sharpen/
│   ├── chat-migration/
│   ├── code-audit/
│   ├── azure-devops/
│   ├── tdd/
│   ├── systematic-debugging/
│   └── scaffold/
├── agents/
│   ├── researcher.md
│   ├── verifier.md
│   ├── orchestrator.md
│   └── editor.md
├── hooks/
│   ├── hooks.json
│   ├── verification-nudge.sh
│   ├── claude-md-bloat-guard.sh
│   └── skill-quality-guard.sh
├── scripts/
├── build.sh
├── package.sh
└── LICENSE
```

## License

MIT
