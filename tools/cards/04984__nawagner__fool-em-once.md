---
id: tool-04984
type: tool
area: 库
status: active
tags: [去AI味, HTML, 协议宽松, 本地优先, 英文文档, 本地写作]
title: fool-em-once
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/nawagner/fool-em-once
created: 2026-07-18
updated: 2026-07-18
no: 4984
category: 一、去 AI 味 / Humanizer 库
repo: nawagner/fool-em-once
stars: 0
url: https://github.com/nawagner/fool-em-once
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# nawagner/fool-em-once

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/nawagner/fool-em-once
- **Stars**：0
- **语言**：HTML
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Small experiment on AI text detectors and text-humanizers for student-like texts
- **本地描述**：Small experiment on AI text detectors and text-humanizers for student-like texts
- **拉取时间**：2026-07-25 18:01:54

---

# fool-em-once — AI detection vs. humanizers, over time

An ongoing series testing a simple question: **can a cheap "humanizer" tool disguise
AI-generated student essays well enough to beat AI-text detectors?** Each study repeats the
same core experiment as the tools evolve, so we can watch how the cat-and-mouse game between
humanizers and detectors changes from version to version.

**[▶ View the interactive comparison hub →](https://nawagner.github.io/fool-em-once/)**

---

## The studies

| # | Study | Date | Detector | Humanizer | Essay generators | Clean bypass* |
|---|-------|------|----------|-----------|------------------|---------------|
| 1 | [**fool-em-once**](studies/01-original/) | Jan 2026 | Pangram 3.0 (3‑way: AI / AI‑assisted / human) | WriteHuman.ai | Gemini 3 Flash, GPT‑5.2 | **89%** |
| 2 | [**fool-em-twice**](studies/02-sequel/) | Jul 2026 | **Pangram 3.3.2** (3‑way, improved recall on humanized text) | **Walter Writes** | **Claude (Claude Code), GPT‑5.5 (Codex)** | **40%** |

\* *Clean bypass = share of AI essays that came back labeled fully **Human** after humanization
(baseline detection was ~100% in both studies). See the note on methodology below — the two
studies changed several variables at once, so this is a snapshot of the landscape over time,
not a controlled A/B test of a single tool.*

---

## What changed between Study 1 and Study 2

The story is **the detector got much harder to fool — not that it gained a new category.**

Both studies used a **three-way** Pangram. Pangram 3.0 introduced the "AI-assisted" middle tier in
December 2025, and the January study ran on it: the original results already contain **4 essays
labeled "mix of AI-generated and human-written"** — Pangram's AI-assisted verdict. So the detector
was never binary; what changed is how often humanized text still slipped all the way to a
fully-human verdict.

Scored the same way both times (a "bypass" = the essay came back a confident, fully-**human**
verdict), here is where humanized essays landed:

| Post-humanization verdict | Study 1 · Pangram 3.0 | Study 2 · Pangram 3.3.2 |
|---|---|---|
| Fully **Human** (clean bypass) | **89%** (34/38) | **40%** (16/40) |
| **Mixed / AI-assisted** (caught in the middle) | 11% (4/38) | 37.5% (15/40) |
| Fully **AI** (still caught) | 0% | 22.5% (9/40) |

The newer model (whose card advertises *"improved recall on humanized texts"*) pins far more
humanized essays in the AI-assisted middle — and catches some outright — instead of letting them
reach "human." That is the whole **89% → 40%** drop.

The looser reading tells the same story from the other side: if you only count a confident "AI"
flag as a catch, Study 2's humanizer knocked **77.5%** of essays out of it — but 60% of those still
carried an AI-assisted signal a teacher could act on, whereas in Study 1 the humanizer pushed
nearly everything all the way to "human."

**Bottom line:** the 2026‑01 attack (humanize → reach a fully-human verdict) is much weaker against
the 2026‑07 detector, but humanizers are not dead — four in ten AI essays still passed as fully
human. Detection remains a signal, not proof.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## How to read this repo

```
fool-em-once/
├── index.html              # interactive comparison hub (the page above)
├── README.md               # you are here
└── studies/
    ├── 01-original/        # Study 1 — full methodology, data, and viewer
    │   ├── README.md           # Study 1 write-up + methodology
    │   ├── index.html          # Study 1 published results page
    │   ├── output/results-viewer.html
    │   ├── data/  src/  tests/
    │   └── SOURCE_PROMPT.md, IMPLEMENTATION_PLAN.md
    └── 02-sequel/          # Study 2 — full methodology, data, and viewer
        ├── README.md           # Study 2 write-up + methodology
        ├── index.html          # Study 2 interactive results viewer
        └── data/  src/
```

Each study folder is **self-contained and documents its own methodology**, so the two experiments
stay independently reproducible. The top-level [`index.html`](index.html) links out to both.

## A note on methodology & comparability

These are pilot-scale studies (~40 essays each) and they intentionally use *current* tools at each
point in time, so several variables moved between them: the detector, the humanizer, and the essay
generators all changed. That makes the series a good picture of **how the landscape evolves**, but
it means you can't attribute the 89% → 40% drop to the detector alone. The controlled, deliberate
change is the detector/humanizer generation; the generator swap (Gemini/GPT‑5.2 → Claude/GPT‑5.5)
is a confound to keep in mind. Per-study details, exact endpoints, and limitations are documented
in each study's README.

*Study 1: Claude Code w/ Nicholas Wagner, Jan 2026. Study 2: Claude Code w/ Nicholas Wagner, Jul 2026.*
