---
id: tool-05276
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: deslop
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/jeanstory/deslop
created: 2026-07-18
updated: 2026-07-18
no: 5276
category: 一、去 AI 味 / Humanizer 库
repo: JeanStory/deslop
stars: 0
url: https://github.com/jeanstory/deslop
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d1b90bf756ac3498
  - methods/改稿润色指令库.md
---

# JeanStory/deslop

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/jeanstory/deslop
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：ai, ai-detection, detector, editing, linter, llm, prose, slop, writing, zero-dependency
- **GitHub 描述**：Deterministic, zero-dependency detector for AI-generated 'slop' tells in prose.
- **本地描述**：Deterministic, zero-dependency detector for AI-generated 'slop' tells in prose.
- **拉取时间**：2026-07-25 18:12:35

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# deslop

**A deterministic, zero-dependency detector for AI-generated "slop" in prose.**

`deslop` finds the tells that mark machine-generated text — throat-clearing
openers, "not X, it's Y" contrasts, em-dash pile-ups, empty emphasis crutches,
adverb crutches, lazy extremes ("always", "never", "everyone") — and reports
each one with a character span, a category, and an actionable fix hint.

No models. No API calls. No network. No dependencies. Pure Python, fully
deterministic, and it runs in milliseconds — so you can drop it into a CI gate,
a pre-commit hook, or an editor.

## Why negative-space scoring?

You cannot reliably score "good writing." You *can* reliably detect the finite,
enumerable tells that mark AI slop. So `deslop` flips the problem: instead of
rewarding virtues, it enumerates the anti-patterns, localizes every span, and
gates on their **density**. Quality is measured by the *absence* of tells.

## Install

```bash
pip install deslop
```

Or run straight from a clone (zero dependencies, nothing to build):

```bash
git clone https://github.com/JeanStory/deslop
cd deslop && python -c "import sys; sys.path.insert(0,'src'); import deslop; print(deslop.explain('Here\'s the thing: it\'s not about speed, it\'s about trust.'))"
```

## CLI

```bash
# check a string
deslop "Here's the thing: it's not about speed, it's about trust."

# check a file
deslop README.md

# from a pipe
cat draft.md | deslop

# machine-readable
deslop --json draft.md

# CI gate: exit 1 if the text scores below 35/50
deslop --check --min 35 draft.md
```

Example output:

```
verdict=revise  score=28/50  words=11
dimensions: throat_clearing=..., binary_contrast=..., ...
hits:
  [throat_clearing] "Here's the thing" @0-16  -> Cut it. State the point.
  [binary_contrast] "not about speed, it's about trust" @...  -> Pick one claim; drop the false pivot.
```

## Python API

```python
import deslop

hits = deslop.detect("Let me walk you through the architecture.")
for h in hits:
    print(h.category, repr(h.matched), h.start, h.end, "->", h.hint)

report = deslop.score(draft_text)
print(report.verdict, report.total, "/50")   # "pass" | "revise"

print(deslop.explain(draft_text))             # human-readable summary
```

- `detect(text) -> list[Hit]` — every tell, with `category`, `pattern_class`,
  `matched`, `start`, `end`, `hint`.
- `score(text) -> Report` — 5-dimension rubric, `total` out of 50, and a
  `pass`/`revise` verdict (mirrors the "below 35/50: revise" rule).
- `explain(text) -> str` — formatted, human-readable report.

## Three pattern classes

1. **Literal** — fixed throat-clearing openers, business jargon, meta-commentary,
   emphasis crutches, vague declaratives.
2. **Structural** — regex shapes: binary contrast (`not X, it's Y`), negative
   listing, em-dash pile-up, Wh- sentence starters, false agency, passive voice.
3. **Word** — adverb crutches (`-ly` plus named offenders) and lazy extremes
   (`every`, `always`, `never`, ...).

## What makes it better than a substring blocklist

- **Word-boundary matching**: `just` never fires inside `adjust`, `really` never
  inside `real estate`, `period` never inside `periodic`. A naive substring
  blocklist produces these false positives; `deslop` produces zero.
- **Span localization**: every hit carries exact character offsets, so an editor
  can highlight or auto-fix it.
- **Category + fix hint** per hit, not a binary yes/no.
- **A density rubric** with a `pass`/`revise` gate.

## Tests

Zero-dependency, runs anywhere:

```bash
cd tests && python test_core.py
```

The suite covers unit tests for each pattern class *and* a head-to-head
comparison against a naive substring baseline across recall, false-positive
discipline, span accuracy, and actionability.

## Support this project

If `deslop` saves you from shipping robotic prose, consider sponsoring its
development via **GitHub Sponsors** (see `.github/FUNDING.yml`). Sponsorship keeps
the pattern tables current as new AI tells emerge.

## License

MIT © 2026 JeanStory
