---
id: tool-00195
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: data-story
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/dinesh0666/data-story
created: 2026-07-18
updated: 2026-07-18
no: 195
category: 二、网文 / 长篇 AI 写作系统 库
repo: dinesh0666/data-story
stars: 1
url: https://github.com/dinesh0666/data-story
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 69eef93472bda7f9
  - methods/最强写作方法论_全球最强综合版.md
---

# dinesh0666/data-story

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/dinesh0666/data-story
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：ai, anthropic, claude, claude-skills, data-analytics, data-profiling, llm
- **GitHub 描述**：Auto data profiler + AI narrative generator. Upload CSV/Excel → get an executive report. Built as a Claude Skill.
- **本地描述**：Auto data profiler + AI narrative generator. Upload CSV/Excel → get an executive report. Built as a Claude Skill.
- **拉取时间**：2026-07-23 22:44:42

---

# DataStory — Auto Data Profiler + Narrative Generator

> Upload any CSV or Excel file → get an AI-written executive data report in seconds.

A Claude Skill + React Artifact built with the Claude-in-Claude pattern using the Anthropic API.

![DataStory](https://img.shields.io/badge/Claude-Skill-blueviolet) ![License](https://img.shields.io/badge/license-MIT-green)

![DataStory Demo](demo.gif)

---

## What it does

1. **Profiles your data** — shape, nulls, distributions, outliers per column
2. **Calls Claude** — generates an executive narrative: key findings, anomaly callouts, quality score, insights, next steps
3. **Outputs a polished report** — interactive in-browser UI or a downloadable `.docx` Word document

---

## Repo structure

```
data-story/
├── skill/
│   ├── SKILL.md                  ← Install this in Claude.ai as a Skill
│   └── scripts/
│       ├── profile_data.py       ← Python: CSV/XLSX → JSON profile
│       ├── generate_report.js    ← Node: profile + narrative → .docx
│       └── run_datastory.sh      ← Shell: full pipeline orchestrator
└── app/
    └── DataStory.jsx             ← React artifact (Claude-in-Claude)
```

---

## Using the Skill (Claude.ai)

Install `skill/SKILL.md` as a Claude Skill. Once installed, Claude auto-triggers DataStory when you:

- Upload a `.csv` or `.xlsx` and ask for analysis
- Say *"profile my data"*, *"generate a report from this file"*, *"what does this dataset say"*

---

## Using the CLI scripts

```bash
pip install pandas openpyxl
npm install -g docx

export ANTHROPIC_API_KEY=sk-ant-...
bash skill/scripts/run_datastory.sh sales_data.csv
# Output: datastory_sales_data.docx
```

---

## Using the React Artifact

`app/DataStory.jsx` is a self-contained React component for Claude Artifacts.
Drag-and-drop a CSV/XLSX — profiling happens client-side, narrative via Anthropic API.

---

## Report sections

| Section | Description |
|---|---|
| Executive Summary | AI-written takeaway for non-technical stakeholders |
| Dataset Overview | Shape, missing %, column type breakdown |
| Key Findings | 5 AI-generated data insights |
| Anomalies & Concerns | Auto-flagged issues + AI-detected concerns |
| Column Profiles | Type, null %, stats per column |
| Column Insights | Per-column AI commentary |
| Data Quality Score | 0–100 with label (Poor / Fair / Good / Excellent) |
| Recommended Next Steps | 3 actionable AI suggestions |
| Sample Data | First 5 rows |

---

## Requirements

- Python 3.8+ · `pandas` · `openpyxl`
- Node.js 18+ · `docx` (`npm install -g docx`)
- Anthropic API key (narrative only — profiling works without it)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Built by [@dinesh0666](https://github.com/dinesh0666) · Inspired by [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
