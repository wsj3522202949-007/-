---
id: tool-05190
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: clinical-paper-agent-prompts
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ruanfire/clinical-paper-agent-prompts
created: 2026-07-18
updated: 2026-07-18
no: 5190
category: 一、去 AI 味 / Humanizer 库
repo: ruanfire/clinical-paper-agent-prompts
stars: 1
url: https://github.com/ruanfire/clinical-paper-agent-prompts
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 322e8abf4cda2673
  - methods/改稿润色指令库.md
---

# ruanfire/clinical-paper-agent-prompts

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ruanfire/clinical-paper-agent-prompts
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：A complete clinical research paper production pipeline with 14 specialized AI agents — from raw data quality grading and fraud detection through SAP, statistics, writing, peer review, revision, and submission-ready deliverables including cover letter and graphical abstract.
- **本地描述**：A complete clinical research paper production pipeline with 14 specialized AI agents — from raw data quality grading and fraud detection through SAP, statistics, writing, peer review, revision, and submission-ready deliverables including cover letter and graphical abstract.
- **拉取时间**：2026-07-25 18:09:25

---

# Clinical Paper Agent Prompts

> A complete set of **14 AI Agent role prompts** for collaborative clinical research paper writing. Zero dependencies — works with any LLM (ChatGPT, Claude, DeepSeek, etc.).

## Overview

**14 specialized Agent prompts** for writing original clinical research papers from raw data (Excel/CSV/SPSS). Each Agent handles one stage of the paper production pipeline:

| Step | Agent | Role | Responsibility |
|------|-------|------|---------------|
| 1 | Agent1 | Data Manager + QC Rating | Data QC, quality grading (A-F), cleaning |
| 2 | Agent2 | Senior Statistician | Statistical Analysis Plan (SAP) |
| 3a | Agent3a | Gold Statistician | Code execution + figures/tables |
| 3b | Agent3b | Literature Searcher | Structured literature retrieval |
| 4a | Agent4a | Introduction Writer | Introduction section (3-paragraph structure) |
| 4b | Agent4b | Methods+Results Writer | Methods & Results sections |
| 5 | Agent5 | Discussion Writer | Discussion + 3-4 limitations with mitigations |
| 5.5 | Agent8 | Abstract Writer | Title + Abstract + Keywords |
| 6a/b/c | Agent6a/b/c | 3 Reviewers | Clinical/Logic/Statistics review |
| 7 | Agent7 | Revision Editor | Response to reviewers + final check |
| 7b | Agent9 | Cover Letter Writer | Submission cover letter + reviewer suggestions |
| 7b | Agent10 | Graphical Abstract | Visual abstract description |

## Key Features (v3.0.0)

- **Data quality rating system**: A/B/C/D/F grade with fraud detection (F-level halts pipeline)
- **Structured 3-paragraph Introduction**: Burden → Gap → Purpose
- **Limitation pattern**: Each limitation includes what was done + what's next
- **Cover Letter + Graphical Abstract**: Ready for submission
- **3 independent reviewers**: Clinical + Logic + Statistics

## How to Use

1. Run the pipeline sequentially (Step 0 → 7)
2. For each step, copy the corresponding Agent prompt into your LLM
3. Provide necessary context (study background, data, interim results)
4. One person should act as the **Orchestrator** (managing context flow between steps)

A detailed pipeline flowchart is available in `pipeline_overview.md`.

## File Structure

| Version | File Pattern | Dependencies | When to Use |
|---------|-------------|-------------|-------------|
| Full | `agent*_role_full.md` | Zero | Any LLM, standalone use |
| Lite | `agent*_role_lite.md` | Hermes skill ecosystem | Only in Hermes Agent |

## Recommended Models

| Agent | Recommended Model | Rationale |
|-------|-------------------|--------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| Agent2 (SAP) | Gemini Flash Lite | Stable reasoning, low cost |
| Agent3a (Stats code) | Claude Haiku / GPT-4o | Strong code generation |
| Agent4a/b (Writing) | Claude Sonnet 4.6 (Intro) / Qwen 3.5 Plus (Methods+Res) | Strong English writing + cost-effective |
| Agent5 (Discussion) | DeepSeek V4 Pro | Deep analysis, strong reasoning |
| Other Agents | DeepSeek V4 Flash / GPT-4o mini | Sufficient, fast |

## Case Study

`examples/omg_gmg_case_study/` contains a complete trial run on an Ocular Myasthenia Gravis (OMG) → Generalized MG conversion prediction model, including:
- Study profile
- Statistical results
- Literature pool
- Final manuscript

## License

MIT
