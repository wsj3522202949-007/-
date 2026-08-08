---
id: tool-01470
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 本地写作]
title: multi-step-story-generator
summary: 搭大纲/分卷/节拍
source: https://github.com/kkmkoi/multi-step-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1470
category: 二、网文 / 长篇 AI 写作系统 库
repo: kkmkoi/multi-step-story-generator
stars: 0
url: https://github.com/kkmkoi/multi-step-story-generator
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 324315b76a43b6ba
  - methods/最强写作方法论_全球最强综合版.md
---

# kkmkoi/multi-step-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/kkmkoi/multi-step-story-generator
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A Python tool that turns a short prompt into a long-form fictional story via a 3-step pipeline: 1) generate a structured plot outline, 2) write each section independently, 3) assemble and refine. Outputs plot_outline.json and final_story.md.
- **本地描述**：A Python tool that turns a short prompt into a long-form fictional story via a 3-step pipeline: 1) generate a structured plot outline, 2) write each section independently, 3) assemble and refine. Outputs plot_outline.json and final_story.md.
- **拉取时间**：2026-07-23 23:21:57

---

# Full-Length Novel Generation Mini Project 

## 1. Purpose
Generate a novella-length (≈15k–25k words) work of fiction automatically using staged large language model (LLM) prompting: (1) structured outline → (2) long-form chapter drafts → (3) refinement & assembly.

## 2. High-Level Workflow
1. Plot Outline (generate_outline.py)
   - Craft a 5-part architecture: Introduction, RisingAction, Climax, FallingAction, Resolution.
   - Enforces 150–250+ words per section to support later long chapters.
2. Chapter Generation (generate_chapters.py)
   - Expands each outline section into a 3k–5k word literary chapter using multi‑persona system prompt.
3. Editorial Assembly (assemble_story.py)
   - (Planned/partial) Refines raw chapters, assigns evocative titles, produces summaries for continuity, polishes final manuscript, and builds final markdown + table of contents.
4. Orchestrator (main.py)
   - Guides user, analyzes the initial prompt, runs all stages sequentially, prints basic quality stats.

## 3. Repository Structure 
```
pre/
  generate_outline.py      # Outline creation via advanced structural prompt
  generate_chapters.py     # Long-form chapter drafting
  assemble_story.py        # Refinement, titling, summaries, polishing 
  main.py                  # End‑to‑end pipeline driver
  README.md                # This file
```
Output directory is derived from the sanitized user prompt. Files produced:
- plot_outline.json
- <SectionName>.txt (5 raw chapters)
- final_story.md (after assembly / polishing)
- table_of_contents.md (after assembly)

## 4. Core Design Choices
| Aspect | Rationale |
| ------ | ------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- |
| Fixed 5-act macro-structure | Predictable loop & simpler downstream logic |
| Rich system prompts (role blending) | Encourage stylistic consistency & depth |
| Large max_tokens (10k–15k) | Allow multi-thousand word outputs per request |
| JSON outline contract | Deterministic parsing & iteration |
| Sanitized folder + filenames | Cross-platform safe persistence |


## 5. Quick Start
```
cd pre
python generate_outline.py     # Step 1: outline
python generate_chapters.py    # Step 2: chapters
python assemble_story.py       # Step 3: (refine & assemble)
# OR run the unified pipeline:
python main.py
```
Follow on‑screen prompt to enter a detailed story premise.

## 6. Example Prompt
```
A lonely lighthouse keeper discovers an ancient organism that warps memory and time, forcing him to confront isolation and identity across decades.
```

## 7. Metrics Produced
- Prompt heuristic rating
- Total word count, per‑chapter average (final assembly)
- Sentence estimate & avg words / sentence (readability proxy)

