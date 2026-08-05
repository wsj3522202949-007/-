---
id: tool-00689
type: tool
area: 库
status: active
tags: [大纲规划, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: AI-xiaoshuo-workflow-opt
summary: 搭大纲/分卷/节拍
source: https://github.com/334962951-png/ai-xiaoshuo-workflow-opt
created: 2026-07-18
updated: 2026-07-18
no: 689
category: 二、网文 / 长篇 AI 写作系统 库
repo: 334962951-png/AI-xiaoshuo-workflow-opt
stars: 0
url: https://github.com/334962951-png/ai-xiaoshuo-workflow-opt
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 334962951-png/AI-xiaoshuo-workflow-opt

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/334962951-png/ai-xiaoshuo-workflow-opt
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：ai-writing, automation, fanqie, novel-workflow, playwright
- **GitHub 描述**：Team-ready AI novel workflow template with writing, review, state tracking, and Fanqie upload automation
- **本地描述**：Team-ready AI novel workflow template with writing, review, state tracking, and Fanqie upload automation
- **拉取时间**：2026-07-23 22:59:07

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Novel Workflow Template

A reusable workflow template for serialized novel production and Fanqie upload automation.

It combines chapter planning, draft generation, review gates, revision loops, state tracking, and publishing handoff into a single project structure that can be adapted to different long-form fiction projects.

## Overview

This repository is designed as a project template rather than a live novel repository. It keeps the workflow layer, upload tooling, configuration surface, and reusable writing templates, while excluding active manuscript content and runtime state.

Core capabilities:

- Chapter planning, drafting, review, and revision
- Multi-step quality gates and review policy control
- Publish-state bookkeeping and batch publishing flow
- Fanqie upload automation with fallback handoff paths
- Config-driven project semantics and reusable writing templates

## Repository Layout

- [pipeline.py](/D:/AI-xiaoshuo-workflow-opt/pipeline.py)
  Main workflow entrypoint for planning, generation, review, revision, status tracking, and publish orchestration.
- [fanqie_upload.py](/D:/AI-xiaoshuo-workflow-opt/fanqie_upload.py)
  Fanqie upload automation script.
- [cua_upload_bridge.py](/D:/AI-xiaoshuo-workflow-opt/cua_upload_bridge.py)
  Computer Use / TuriX fallback bridge when the main Playwright path cannot complete.
- [project_config.json](/D:/AI-xiaoshuo-workflow-opt/project_config.json)
  Project-level configuration for labels, story structure, prompt defaults, and file routing.
- [templates](/D:/AI-xiaoshuo-workflow-opt/templates)
  Reusable writing templates for worldbuilding, character setup, arcs, constraints, and status scaffolds.
- [state/review_policy.json](/D:/AI-xiaoshuo-workflow-opt/state/review_policy.json)
  Review gate policy used by the workflow.

## Getting Started

1. Clone the repository.
2. Install dependencies.
3. Copy `.env.example` to `.env`.
4. Update [project_config.json](/D:/AI-xiaoshuo-workflow-opt/project_config.json).
5. Copy the files in [templates](/D:/AI-xiaoshuo-workflow-opt/templates) into a private, ignored project directory.
6. Point `project_config.json > files` to those private project files.
7. Run `python pipeline.py doctor`.

Quick start details are available in [QUICKSTART_INTERNAL.md](/D:/AI-xiaoshuo-workflow-opt/QUICKSTART_INTERNAL.md).

## Recommended Project Pattern

Keep reusable workflow code in the repository, and keep live project materials outside version control.

Suggested ignored directories:

- `private_project/`
- `story_private/`
- `project_local/`

These are already included in [.gitignore](/D:/AI-xiaoshuo-workflow-opt/.gitignore).

Typical private content includes:

- Active manuscript files
- Project-specific story bibles
- Detailed outlines and revisions
- Runtime state snapshots
- Cookies, IDs, credentials, and local automation artifacts

## Common Commands

```powershell
python pipeline.py status
python pipeline.py doctor
python pipeline.py plan
python pipeline.py run --count 2
python pipeline.py review --chapter 12
python pipeline.py audit --from 1 --to 20 --summary-only
python pipeline.py publish
python pipeline.py publish --from 101 --to 105
python pipeline.py publish --fallback handoff
python pipeline.py browser-handoff --from 101 --to 105
python fanqie_upload.py login
python fanqie_upload.py upload --from 101 --to 105 --mode auto
```

## What To Commit

Safe to commit:

- Workflow code
- Upload tooling
- Configuration templates
- Generic writing templates
- Non-sensitive documentation

Do not commit:

- Active novel content
- Project-specific planning or editorial materials
- Runtime logs and review outputs
- Cookies, local IDs, or account-related files
- `.env` and other secrets

## License

See [LICENSE](/D:/AI-xiaoshuo-workflow-opt/LICENSE).
