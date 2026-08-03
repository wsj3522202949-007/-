---
id: tool-01729
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: skills
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/sunhao25/skills
created: 2026-07-18
updated: 2026-07-18
no: 1729
category: 二、网文 / 长篇 AI 写作系统 库
repo: Sunhao25/skills
stars: 1
url: https://github.com/sunhao25/skills
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Sunhao25/skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sunhao25/skills
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：A curated monorepo of AI Agent Skills (SKILL.md) for skills.sh: reusable workflows, prompts & templates for writing, SaaS growth, analytics and ops. Skills only—Python/SQL live in separate repos.
- **本地描述**：A curated monorepo of AI Agent Skills (SKILL.md) for skills.sh: reusable workflows, prompts & templates for writing, SaaS growth, analytics and ops. Skills only—Python/SQL live in separate repos.
- **拉取时间**：2026-07-23 23:29:26

---

# Skills (AI Agent Skills Library)

This repository is a **skills library** for AI agents: a structured collection of reusable “Skill packs” that help an agent follow consistent workflows and produce stable, high-quality outputs.

A **Skill** is typically a folder that contains:
- `SKILL.md` — the entrypoint instructions (what the skill is for, how to use it, what to output)
- `references/` — optional long-form guides, checklists, examples (loaded only when needed)
- `templates/` or `assets/` — optional reusable templates, snippets, or resources

> This repo stores **skills only**. Code assets (Python/SQL/etc.) live in separate repositories.

---

## What is a “Skill” (and why use it)?

A skill is a **repeatable playbook** for an AI agent. Instead of writing the same prompts and rules again and again, you package them into a folder so the agent can:
- follow a standardized process
- reuse proven templates
- stay consistent across sessions
- scale to new tasks by adding new skill folders

---

## Compatibility (where these skills can be used)

These skills are designed for **AI agents that support “skill folders” / SKILL.md style workflows**, such as:
- agent environments that can load `SKILL.md` as instruction packs
- editors/agents that support skills or similar modular instruction systems
- the skills.sh ecosystem (when used as individual skills or via manual folder selection)

> Note: Not every tool supports “installing a subfolder as a skill” automatically.  
> If your agent can’t install from a subfolder, you can still copy the skill folder (the one containing `SKILL.md`) into your agent’s skills directory and use it the same way.

---

## Repository structure

This repo is organized by **high-level modules**.  
Each top-level folder represents a major use case category (a “big skill domain”).

Current modules:
- `writing/` — writing skills (novels, fanfic, erotica, etc.)

Planned modules (coming soon):
- `learning/` — study skills, tutoring workflows, exam prep, note-to-knowledge systems
- `coding/` — programming skills, code review, debugging playbooks, repo onboarding
- `data/` — data analysis skills, metric definitions, reporting workflows
- `hr/` — hiring, interviewing, performance review, HR comms playbooks
- `ops/` — operations, customer support playbooks, SOPs, incident response
- `product/` — PM workflows, PRDs, UX writing, launch checklists

---

## How to browse skills

1. Start from a module folder (e.g. `writing/`)
2. Choose a specific skill folder (e.g. `writing/novel-master/`)
3. Open `SKILL.md` to see:
   - what the skill does
   - required inputs
   - step-by-step workflow
   - output formats / templates

---

## Writing module: how it’s subdivided

Inside `writing/`, skills can be grouped by sub-types such as:
- `general/` — general fiction / web novel writing
- `fanfic/` — fan fiction specific workflows (canon handling, character voice, tags)
- `erotica/` — adult/erotica writing workflows (consent boundaries, tone control, pacing)

Example shape:
- `writing/general/<skill-name>/SKILL.md`
- `writing/fanfic/<skill-name>/SKILL.md`
- `writing/erotica/<skill-name>/SKILL.md`

> Any adult writing skills here are intended for **consenting adults and legal content only**.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Contributing / adding a new skill

When adding a new skill, follow this minimum standard:
1. Create a folder for the skill
2. Add `SKILL.md` (required)
3. Add optional `references/` for long guides and examples
4. Keep folder names short and category-based (avoid overly detailed file-like names)

Recommended minimal layout:
