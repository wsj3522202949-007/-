---
id: tool-05742
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: my-humanizer-es-en
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/ljmor/my-humanizer-es-en
created: 2026-07-18
updated: 2026-07-18
no: 5742
category: 一、去 AI 味 / Humanizer 库
repo: ljmor/my-humanizer-es-en
stars: 1
url: https://github.com/ljmor/my-humanizer-es-en
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: e112d154ddfd501f
  - methods/改稿润色指令库.md
---

# ljmor/my-humanizer-es-en

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ljmor/my-humanizer-es-en
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：ai-detection, claude-skills, compilatio, docx, english, gptzero, humanizer, spanish, turnitin
- **GitHub 描述**：Claude skill that humanizes AI-flagged academic & professional text (ES/EN) to pass stylometric detectors like Compilatio, Turnitin & GPTZero — keeping meaning, data and citations intact. Reads the detector's PDF report, rewrites only the flagged passages, rebuilds your .docx.
- **本地描述**：Claude skill that humanizes AI-flagged academic & professional text (ES/EN) to pass stylometric detectors like Compilatio, Turnitin & GPTZero — keeping meaning, data and citations intact. Reads the detector's PDF report, rewrites only the flagged passages, rebuilds your .docx.
- **拉取时间**：2026-07-25 18:29:57

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# my-humanizer-es-en

A Claude skill that rewrites AI-flagged academic and professional text (Spanish
and English) so it reads like a real person wrote it — and passes stylometric AI
detectors like **Compilatio Magister+, Turnitin, GPTZero and Originality.ai** —
while keeping the original meaning, data, and citations untouched.

Built from a real case: it took an academic article from **50% → 13% AI** on
Compilatio across three iterations, without changing a single citation.

## What it does

Detectors flag *rhythm and structure*, not vocabulary. This skill breaks the
uniform cadence of AI writing and adds human "burstiness":

- Kills the `statement: elaboration` colon habit (the strongest tell).
- Breaks symmetric enumerations ("two things:", "three fronts:").
- Mixes very short sentences with long ones (varied length = human).
- Adds first person and concrete, slightly messy detail where it fits.
- **Never touches** citations, numbers, dates, or the reference list.

## Two ways to use it

**With a detector report (best).** Give Claude the detector's PDF report and it
reads the colored highlights (blue = AI, green = similarity) straight from the
PDF, so it rewrites **only** the flagged passages, then rebuilds your `.docx`
without breaking its formatting.

**Without a report (blind mode).** No report? No problem. The skill runs its own
internal leak scan (`scan_leaks.py`) that scores every sentence for likely AI
tells — long sentences, colon-lists, symmetric enumerations, AI vocabulary,
em-dashes — ranks the worst ones, and rewrites those, then checks burstiness
metrics. It's a heuristic proxy for a detector: it finds what *probably* still
reads as AI so you can fix it before submitting anywhere.

Either way it keeps meaning, data and citations intact, and leaves the reference
list alone.

## Contents

```
my-humanizer-es-en/
├── SKILL.md                    # the skill (methodology + rulebook Claude follows)
└── scripts/
    ├── analyze_report.py       # report mode: extract blue (AI) / green (similarity) passages from a detector PDF
    ├── scan_leaks.py           # blind mode: heuristic AI-leak scanner (ES+EN), ranks the riskiest sentences
    ├── replace_paragraphs.py   # rewrite paragraphs inside a .docx, preserving formatting
    └── text_metrics.py         # measure burstiness: colon count, mean/stdev sentence length
```

### What knowledge is inside

The skill is self-contained. It folds in everything used to take the reference
article from 50% to 13%: the full Wikipedia "Signs of AI writing" pattern
catalogue (Spanish + English), the empirical findings from a real Compilatio
Magister+ loop (colon-lists and symmetric enumerations are the highest-value
fixes), burstiness metrics, the blind-mode leak scanner, and format-preserving
`.docx` editing. No other skills need to be installed for it to work.

## Install

### Option A — with the `skills` CLI (recommended)

```bash
npx skills add ljmor/my-humanizer-es-en
```

This installs it into `~/.claude/skills/my-humanizer-es-en/`, available to both
Claude Code and Claude Desktop.

### Option B — manual

```bash
git clone https://github.com/ljmor/my-humanizer-es-en.git
cp -r my-humanizer-es-en ~/.claude/skills/my-humanizer-es-en
```

### Python dependencies (used by the scripts)

```bash
python3 -m pip install pymupdf pypdf defusedxml
```

## Updating (if you already have a previous version installed)

**With the `skills` CLI:**

```bash
npx skills update my-humanizer-es-en
# or, to force a clean reinstall of the latest from GitHub:
npx skills remove my-humanizer-es-en
npx skills add ljmor/my-humanizer-es-en
```

**Manual:** overwrite the installed copy with the latest from the repo.

```bash
git -C my-humanizer-es-en pull        # in your local clone
rm -rf ~/.claude/skills/my-humanizer-es-en
cp -r my-humanizer-es-en ~/.claude/skills/my-humanizer-es-en
```

Restart Claude Code / Claude Desktop (or reload skills) so the updated `SKILL.md`
is picked up. Your previous version is simply replaced — nothing else to clean up.

## Use

In Claude Code or Claude Desktop, just ask:

- "humanize this for Compilatio"
- "baja el porcentaje de IA de este artículo"
- "parafrasea las secciones en azul de este informe"

…or run the skill directly with `/my-humanizer-es-en`. Hand Claude the document
(`.docx`) and, if you have it, the detector's report PDF. Claude analyzes the
report, rewrites the flagged text, rebuilds the document, and iterates with you
until the score hits your target.

## Honest limits (please read)

- **The score is an estimate, not a promise.** AI detection is statistical. The
  skill may not drop the percentage as much as you hope on a given run, and no
  tool can guarantee a specific number. Expect to iterate.
- **The blind-mode scanner is a proxy, not a detector.** It flags what *probably*
  reads as AI. Passing it is a good sign, not a certificate.
- **Institutional detectors are run by you.** Compilatio/Turnitin inside an LMS
  can't be called by the skill. The workflow is a loop: it delivers a version,
  you submit it and share the new report, it targets whatever is still flagged —
  each round usually lowers the score further.
- **It never fakes citations or data.** If the honest, human-sounding rewrite
  still trips a detector, the answer is another pass — not inventing sources.

## License

MIT
