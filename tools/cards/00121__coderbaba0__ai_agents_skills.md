---
id: tool-00121
type: tool
area: 库
status: active
tags: [Shell, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ai_agents_skills
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/coderbaba0/ai_agents_skills
created: 2026-07-18
updated: 2026-07-18
no: 121
category: 二、网文 / 长篇 AI 写作系统 库
repo: coderbaba0/ai_agents_skills
stars: 0
url: https://github.com/coderbaba0/ai_agents_skills
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: f077df9d2a0cd3c6
  - methods/最强写作方法论_全球最强综合版.md
---

# coderbaba0/ai_agents_skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/coderbaba0/ai_agents_skills
- **Stars**：0
- **语言**：Shell
- **License**：MIT
- **Topics**：agent-skills, ai, ai-agents
- **GitHub 描述**：This is a repository of reusable “agent skills” — structured workflows for an AI assistant. Each folder is one skill that handles a specific task (planning, coding, tooling, or writing). Together, they let you install and run these workflows in projects via simple commands. 
- **本地描述**：This is a repository of reusable “agent skills” — structured workflows for an AI assistant. Each folder is one skill that handles a specific task (planning, coding, tooling, or writing). Together, they let you install and run these workflows in projects via simple commands.
- **拉取时间**：2026-07-23 22:42:30

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Agent Skills
.claude dir

Agent Skills is a public, developer‑focused collection of reusable AI agent workflows. Each top‑level folder is a skill that automates a concrete software development task such as product planning, PRD writing, technical design, test‑driven development, codebase refactors, tooling setup, or knowledge management. The goal is to speed up real‑world engineering work with structured, repeatable playbooks you can install and run in your projects.

## How to Install a Skill

```
npx skills@latest add coderbabo/ai_agents_skills/<skill-name>
```

## How to Use (Step by Step)

1. Pick a skill folder from this repo (for example: `tdd` or `write-a-prd`).
2. Install it using the command above and replace `<skill-name>` with the folder name.
3. Follow the instructions inside that skill’s `SKILL.md`.
4. Run the workflow with your AI agent in your project.

Tip: Each skill is independent, so you can install only what you need.

## What You Can Do With This Repo

Use these skills to turn fuzzy ideas into plans, turn plans into GitHub issues, and turn issues into implemented code. This repository is designed for software engineers, tech leads, product engineers, and teams who want consistent AI workflows for planning, development, and maintenance.

## Why It Exists

AI is most useful when it follows a structured workflow. These skills provide that structure so tasks like PRD creation, implementation planning, bug triage, refactoring, and pre‑commit setup are fast, repeatable, and reviewable.

## Benefits

- Faster planning and clearer requirements
- Consistent execution across team members
- Better code quality through TDD and tooling
- Safer git usage with guardrails
- Cleaner documentation and shared vocabulary

## Keywords

AI agent skills, developer productivity, software engineering workflows, PRD, product requirements document, implementation plan, GitHub issues, TDD, test‑driven development, refactoring, codebase architecture, pre‑commit hooks, lint‑staged, Prettier, tooling automation, knowledge management, Obsidian, technical writing.

## Planning & Design

- **write-a-prd** — Create a PRD via interview + codebase exploration; files a GitHub issue.
- **prd-to-plan** — Turn a PRD into a multi‑phase implementation plan.
- **prd-to-issues** — Split a PRD into small, grab‑and‑go GitHub issues.
- **grill-me** — Stress‑test a plan with tough questions until it is clear.
- **design-an-interface** — Generate multiple UI/UX designs for a module.
- **request-refactor-plan** — Build a tiny‑commit refactor plan and file it as an issue.

## Development

- **tdd** — Build features or fixes with red‑green‑refactor loops.
- **triage-issue** — Investigate a bug and produce a fix plan as a GitHub issue.
- **improve-codebase-architecture** — Find architectural improvements and improve testability.
- **migrate-to-shoehorn** — Replace `as` assertions with `@total-typescript/shoehorn` in tests.
- **scaffold-exercises** — Generate exercise folders with problems, solutions, and explainers.

## Tooling & Setup

- **setup-pre-commit** — Configure Husky pre‑commit hooks, lint‑staged, Prettier, type checks, tests.
- **git-guardrails-claude-code** — Block dangerous git commands before they run.

## Writing & Knowledge

- **write-a-skill** — Create a new skill with proper structure and resources.
- **edit-article** — Improve articles by restructuring and tightening prose.
- **ubiquitous-language** — Generate a DDD‑style glossary from a conversation.
- **obsidian-vault** — Create/search/manage notes in an Obsidian vault.

## How to Choose a Skill

Pick the skill that matches your task. Planning and Design skills help before coding. Development skills help while coding. Tooling and Setup skills keep quality high. Writing and Knowledge skills help you document and share decisions.
