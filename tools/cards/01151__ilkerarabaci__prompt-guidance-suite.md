---
id: tool-01151
type: tool
area: 库
status: active
tags: [多Agent, 协议宽松, 本地优先, 英文文档, 本地写作]
title: prompt-guidance-suite
summary: 多 Agent 协作自动产文
source: https://github.com/ilkerarabaci/prompt-guidance-suite
created: 2026-07-18
updated: 2026-07-18
no: 1151
category: 二、网文 / 长篇 AI 写作系统 库
repo: ilkerarabaci/prompt-guidance-suite
stars: 3
url: https://github.com/ilkerarabaci/prompt-guidance-suite
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ilkerarabaci/prompt-guidance-suite

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ilkerarabaci/prompt-guidance-suite
- **Stars**：3
- **语言**：None
- **License**：MIT
- **Topics**：academic-writing, agentic-workflows, automation, chatgpt, coding, executive-writing, prompting, research, skills, writing
- **GitHub 描述**：Reusable ChatGPT skills for structured conversations, research, coding, executive writing, academic writing, and workflow-style automation.
- **本地描述**：Reusable ChatGPT skills for structured conversations, research, coding, executive writing, academic writing, and workflow-style automation.
- **拉取时间**：2026-07-23 23:12:37

---

# Prompt Guidance Suite

Reusable ChatGPT skills for better research, coding, writing, and workflow-style execution.

Prompt Guidance Suite is an open collection of installable ChatGPT skills that package high-value prompting patterns into reusable guidance layers. Instead of repeating the same instructions in every conversation, you install a skill once and let ChatGPT apply it when the task fits.

## Included skills

| Skill | What it improves | Best for |
|---|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| **Prompt Guidance Companion** | General answer quality, structure, follow-through, and completion | Everyday conversations, planning, summarization, decision support |
| **Research Heavy Guidance** | Evidence gathering, source comparison, synthesis, and conflict resolution | Research, market scans, policy review, deep comparisons |
| **Code Development Guidance** | Root-cause analysis, patch planning, refactoring, testing, and implementation discipline | Debugging, code review, API work, system design |
| **Executive Writing Guidance** | Concision, recommendation-oriented writing, and leadership-friendly framing | Memos, briefings, stakeholder updates, decision notes |
| **Academic Writing Guidance** | Thesis discipline, careful claims, counterarguments, and limitations | Essays, literature reviews, scholarly drafts, research proposals |
| **Agentic Automation Guidance** | Multi-step execution, dependency handling, validation, and progress tracking | Workflow design, semi-autonomous tasks, operational runbooks |

## Why use this repository?

These skills are meant to solve a simple problem: good prompting is often repetitive.

Many people eventually develop the same kinds of reusable instructions:
- be explicit about output format
- do not stop at a partial answer
- separate facts from assumptions
- verify before concluding
- adapt tone to the audience
- structure multi-step work clearly

This repository packages those patterns into installable skills so they can be reused consistently across conversations.

## Who this is for

This suite is useful for:
- individual power users who want more consistent outputs
- researchers who need better synthesis and evidence handling
- developers who want more disciplined coding assistance
- leaders and operators who want concise, decision-ready writing
- students and writers who want stronger academic structure
- teams experimenting with workflow-style AI usage

## Installation

Install any skill in ChatGPT:

1. Open **Skills**.
2. Click **New skill**.
3. Choose **Upload from your computer**.
4. Upload one of the ZIP files from `release-assets/`.

Each ZIP is installable independently.

## Where to start

Start with **Prompt Guidance Companion** if you want a default upgrade for general conversations.

Add specialist skills when the task clearly fits a mode:
- use **Research Heavy Guidance** when the answer depends on evidence, comparison, or synthesis
- use **Code Development Guidance** when the work should end in a safe fix, design, or testable implementation
- use **Executive Writing Guidance** when the audience is leadership and the output must be concise and actionable
- use **Academic Writing Guidance** when the writing needs careful argument structure and explicit limitation handling
- use **Agentic Automation Guidance** when the task behaves like a workflow with inputs, dependencies, checks, and state

## Example prompts

### Prompt Guidance Companion
- Explain this topic in five precise bullets and end with knowns, unknowns, and next step.
- Turn these messy notes into a clean decision memo with assumptions clearly labeled.
- Compare these two options and recommend one, but show your reasoning and key tradeoffs.

### Research Heavy Guidance
- Research this question from multiple sources, resolve conflicts, and end with a confident synthesis.
- Break this topic into subquestions first, then answer each one with evidence.
- Compare three approaches to this problem and explain which conditions favor each one.

### Code Development Guidance
- Find the root cause, propose the smallest safe fix, and include a test plan.
- Refactor this without changing behavior; explain tradeoffs and edge cases.
- Design the API contract first, then show an implementation outline and validation steps.

### Executive Writing Guidance
- Rewrite this for a CIO. Lead with the bottom line and close with a recommendation.
- Produce a one-page steering committee update: status, risks, decisions, and asks.
- Turn this raw project update into a concise leadership note with one clear recommendation.

### Academic Writing Guidance
- Turn this claim into an academic introduction with thesis, counterargument, and limitation.
- Draft a mini literature review with thesis, antithesis, and synthesis.
- Rewrite this paragraph in a more careful scholarly tone without overstating the evidence.

### Agentic Automation Guidance
- Treat this as a workflow. Define steps, dependencies, validations, blockers, and outputs.
- Create an execution plan with status checkpoints and rollback considerations.
- Map this recurring task into a repeatable process with inputs, decisions, and handoffs.

## Repository structure

```text
prompt-guidance-suite/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── GITHUB_METADATA.md
├── PUBLIC_RELEASE_VERIFICATION.md
├── RELEASE_NOTES/
│   └── v1.0.0.md
├── release-assets/
│   ├── prompt-guidance-companion.zip
│   ├── research-heavy-guidance.zip
│   ├── code-development-guidance.zip
│   ├── executive-writing-guidance.zip
│   ├── academic-writing-guidance.zip
│   └── agentic-automation-guidance.zip
└── skills/
    ├── prompt-guidance-companion/
    ├── research-heavy-guidance/
    ├── code-development-guidance/
    ├── executive-writing-guidance/
    ├── academic-writing-guidance/
    └── agentic-automation-guidance/
```

## Release model

This repository keeps both:
- **source folders** under `skills/` for inspection and iteration
- **install-ready ZIP files** under `release-assets/` for direct upload into ChatGPT

A clean public release should include:
- updated skill source folders
- validated ZIP assets
- release notes
- a short summary of what changed

## Quality bar

Before publishing a new release:
- confirm every skill installs successfully
- verify `SKILL.md` and `agents/openai.yaml` are present at the correct paths
- test several prompts for each skill
- review naming, descriptions, and examples for clarity
- attach the latest ZIP files to the GitHub release

## Security

Please review `SECURITY.md` for vulnerability reporting guidance.

## Publishing to GitHub

See `GITHUB_PUBLISHING_GUIDE.md` for a step-by-step release flow using either the GitHub web interface or Git locally.

## Contributing

Contributions are welcome. See `CONTRIBUTING.md` for the expected structure and release flow.

Good contribution ideas include:
- clearer examples
- tighter instructions
- better trigger descriptions
- new specialist skills that complement the suite
- documentation improvements

## License

MIT
