---
id: tool-01174
type: tool
area: 库
status: active
tags: [多Agent, Claude插件, Shell, 协议未明, 需API密钥, 英文文档]
title: skills
summary: 多 Agent 协作自动产文
source: https://github.com/massgen/skills
created: 2026-07-18
updated: 2026-07-18
no: 1174
category: 二、网文 / 长篇 AI 写作系统 库
repo: massgen/skills
stars: 7
url: https://github.com/massgen/skills
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# massgen/skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/massgen/skills
- **Stars**：7
- **语言**：Shell
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：Official MassGen skills for AI coding agents (Claude Code, Codex, Copilot, Cursor). Multi-agent evaluation, planning, spec writing, and general-purpose task execution.
- **本地描述**：Official MassGen skills for AI coding agents (Claude Code, Codex, Copilot, Cursor). Multi-agent evaluation, planning, spec writing, and general-purpose task execution.
- **拉取时间**：2026-07-23 23:13:16

---

# 🧠 massgen/skills

[MassGen](https://github.com/massgen/massgen) is a multi-agent system that coordinates multiple AI agents to solve complex tasks through parallel processing, iterative refinement, and consensus voting.

These are the official **Agent Skills** for MassGen — install them to invoke MassGen directly from your AI coding agent. Built on the open [Agent Skills](https://agentskills.io/home) standard. Write once, use everywhere.

📖 [Documentation](https://docs.massgen.ai/en/latest/user_guide/skills.html) · 🚀 [MassGen](https://github.com/massgen/massgen) · 💬 [Discord](https://discord.massgen.ai)

---

## ⚡ Install

```bash
npx skills add massgen/skills --all
```

That's it. Works with Claude Code, Cursor, Codex, Windsurf, GitHub Copilot, Gemini CLI, Goose, Amp, and [40+ other agents](https://skills.sh).

To install to a specific agent only:

```bash
npx skills add massgen/skills -a claude-code
npx skills add massgen/skills -a codex
npx skills add massgen/skills -a cursor
npx skills add massgen/skills -a copilot
npx skills add massgen/skills -a gemini-cli
npx skills add massgen/skills -a windsurf
```

See [Vercel's skills docs](https://vercel.com/docs/agent-resources/skills) for more on the `npx skills` CLI.

<details>
<summary>Manual install (any agent)</summary>

```bash
git clone https://github.com/massgen/skills.git /tmp/massgen-skills
cp -r /tmp/massgen-skills/massgen ~/.claude/skills/massgen   # or ~/.codex/skills/, ~/.agents/skills/, etc.
```

</details>

---

## 📋 What's Included

The **MassGen skill** gives your agent four modes:

| Mode | Purpose | Output |
|------|---------|--------|
| 🎯 **General** (default) | Any task — writing, code, research, design | Winner's deliverables + workspace files |
| 🔍 **Evaluate** | Critique existing work | `critique_packet.md`, `verdict.json`, `next_tasks.json` |
| 📐 **Plan** | Create structured project plans | `project_plan.json` with task DAG |
| 📝 **Spec** | Create requirements specifications | `project_spec.json` with EARS requirements |

---

## 💡 Before You Start

The skill will walk you through setup if needed, but things go smoother if you already have:

1. **MassGen installed**: `pip install massgen`
2. **An AI provider authenticated**: API key (e.g., `OPENAI_API_KEY`) or login-based auth (e.g., `claude` or `codex` login)
3. **A config file**: Run `massgen --quickstart` to create `.massgen/config.yaml`

> **Note:** First-time setup requires human input (provider selection, API keys). After that, the skill runs autonomously.

---

## 🔄 Updating

```bash
npx skills update
```

This repo is automatically synced from the main [MassGen repository](https://github.com/massgen/massgen) on every merge to `main`.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 📄 License

Apache 2.0 — see [LICENSE](https://github.com/massgen/skills/blob/main/LICENSE) for details.
