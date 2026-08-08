---
id: tool-00582
type: tool
area: 库
status: active
tags: [TeX, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: scientific-paper-toolkit
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/evgenyrvr/scientific-paper-toolkit
created: 2026-07-18
updated: 2026-07-18
no: 582
category: 二、网文 / 长篇 AI 写作系统 库
repo: evgenyrvr/scientific-paper-toolkit
stars: 0
url: https://github.com/evgenyrvr/scientific-paper-toolkit
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 21078b6057a24171
  - methods/最强写作方法论_全球最强综合版.md
---

# evgenyrvr/scientific-paper-toolkit

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/evgenyrvr/scientific-paper-toolkit
- **Stars**：0
- **语言**：TeX
- **License**：None
- **Topics**：—
- **GitHub 描述**：A scaffold for writing any scientific paper as a managed software project, using AI models as verifiable assistants with full audit trails.
- **本地描述**：A scaffold for writing any scientific paper as a managed software project, using AI models as verifiable assistants with full audit trails.
- **拉取时间**：2026-07-23 22:56:03

---

# Scientific Paper AI Lab — Universal Toolkit

A scaffold for writing any scientific paper as a managed software project, using AI models as verifiable assistants with full audit trails.

Works for physics, mathematics, chemistry, biology, astronomy, materials science, economics, and any other quantitative discipline.

---

## Scientific responsibility

**The human author is solely responsible for the scientific content of the paper.**

AI models in this toolkit act as executors, auditors, and reviewers — not as authors or decision-makers. Specifically:

- All scientific claims, assumptions, and conclusions must be approved by the human author.
- No AI output should be submitted as the author's own work without critical review and verification.
- References, equations, and numerical results generated or checked by AI must be independently verified by the human author before submission.
- AI use must be disclosed in the paper's Acknowledgements section in accordance with the policies of the target journal or preprint server.
- AI systems must not be listed as authors. Authorship implies accountability that AI cannot bear.

This framework is designed to make AI assistance **auditable and traceable**, not to transfer responsibility away from the author.

---

## What this is

This toolkit provides the complete methodology, skills, templates, and documentation for the "Vibe Research" approach to AI-assisted scientific writing:

- every step produces an inspectable `.md` artifact;
- models act as executors, not authors;
- human author retains final scientific responsibility;
- all claims trace to derivations, evidence, and code.

---

## Quick start

1. Unzip or clone into your project folder (`~/Research/your-paper-name/`)
2. Open in Visual Studio Code (Linux, macOS, or Windows + WSL)
3. Read `docs/07-step-by-step-usage-guide.md`
4. Fill in `project/01_research_question.md` with your problem
5. Run `python3 scripts/check_project_contract.py`
6. Start your first iteration: `python3 scripts/new_iteration.py`

---

## Folder structure

```text
.claude/           — CLAUDE.md contract + 12 specialist skills + 3 behavioral rules
docs/              — methodology, tools, model roles, protocols
project/           — master plan, research question, assumptions, claims, risks, tasks, dashboard
iterations/        — one .md file per work session (append-only log)
quality_reports/   — session logs, audit reports, decisions, plans
reviews/           — reviewer prompts, rebuttal matrix
templates/         — task report, derivation report, evidence card, handoff, session log, decision record
paper/             — LaTeX manuscript scaffold + references
notes/obsidian/    — Obsidian vault start pages
scripts/           — new_iteration.py, check_project_contract.py
MEMORY.md          — persistent cross-session learnings (loads automatically)
```

---

## Models and their roles

Any AI model can perform any role. There is no required mapping of model to task.

| Role | What it does | Who does it |
|------|-------------|-------------|
| Executor | Reads/writes project files, creates iteration reports, runs code, builds LaTeX | Any model with file access |
| Reviewer | Reviews an artifact in a fresh context; finds errors, gaps, overclaiming | Any model, fresh context |
| Human author | Final authority: scientific judgment, claim approval, submission | You — not interchangeable |

See `docs/03-model-roles.md` for the agent-agnostic workflow.

---

## Acknowledgements

If you use this toolkit for a published paper, please consider adding a line to your Acknowledgements section. For example:

> This work was carried out using the [Scientific Paper AI Lab toolkit](https://github.com/evgenyrvr/scientific-paper-toolkit), which structured AI-assisted research as a version-controlled project with verifiable artifacts and full audit trails.

Acknowledging the toolkit helps others discover it, supports its continued development, and makes the methodology transparent to reviewers and readers. It is separate from — and in addition to — any required disclosure of AI model usage.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## License

Use freely for any scientific work. Donations are welcome — see `DONATE.md`.
