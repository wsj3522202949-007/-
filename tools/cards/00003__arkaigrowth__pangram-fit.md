---
id: tool-04804
type: tool
area: 库
status: active
tags: [协议未明, 需API密钥, 英文文档, 去AI味]
title: pangram-fit
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/arkaigrowth/pangram-fit
created: 2026-07-18
updated: 2026-07-18
$13
category: 一、去 AI 味 / Humanizer 库
repo: arkaigrowth/pangram-fit
stars: 0
language: Python
license: MIT
url: https://github.com/arkaigrowth/pangram-fit
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: b3035e1004e89c1c
  - methods/改稿润色指令库.md
---

# pangram-fit

A shell-first primitive that treats an AI-text detector as a **fitness function**
for rewriting, and runs every rewrite through a deterministic **claims-diff**: an
inspectable fabrication gate that flags factual claim candidates present in the
rewrite but absent from the source. It embeds no model. The calling agent (Claude
Code or Codex) is the rewriter; this package is its scorer and its fabrication
gate. The gate is heuristic and tuned to over-flag rather than under-flag, with
known residual gaps documented in [Limitations](#limitations).

The loop:

```
   you rewrite  -->  claims-diff (free gate)  -->  score (paid fitness)
      ^                     | flags new claims          |
      +---------------------+---------------------------+
                  iterate on real, grounded edits only
```

## Why it works this way

Most "humanizer" tools optimize a single number and happily invent biography to
get there. That is the failure mode this design refuses. Two ideas keep it honest:

1. **Detector as fitness function, not oracle.** A low Pangram score is
   *necessary, not sufficient*. It means "reads less like AI," not "is true" and
   not "is good." The score guides edits; it never authorizes them.
2. **Claims-diff as a fabrication gate tuned to over-flag.** Before a rewrite is
   accepted, the source text is used as its own allowlist. The gate extracts
   candidate claims from the rewrite (proper nouns, numbers, dates, quantities,
   URLs, handles, locations, and first-person episodic predicates) and marks each
   as supported or unsupported against a normalized view of the source (or an
   optional `--facts` file). Any unsupported claim sets `truth_required` and the
   step exits non-zero. There is no separate "maybe" state: a claim the gate
   cannot match to the source is treated as unsupported, so uncertainty flags
   rather than passes.

The detector is the fitness function, the claims-diff is the constraint, and the
agent is the optimizer. The one unforgivable move is fabricating to pass the score.

## Install

Zero runtime dependencies (Python standard library only, `urllib` rather than
`requests`), which keeps it runnable inside restricted sandboxes.

```bash
# clone, then from the repo root:
uv run pangram-fit version

# run the test suite (pytest is an optional dependency):
uv run --extra test pytest -q
```

Requires Python 3.9 or newer. Without `uv`, a plain `pip install -e .` works too.

## Quickstart

Scoring calls the Pangram Labs `/v3` API and needs a key (see Limitations). The
free gates below need no key and make no network calls.

```bash
# free: mechanical AI-tell hints (advisory only, never a verdict)
echo "In today's fast-paced world, we leverage synergy." | uv run pangram-fit lint -

# free: does the rewrite invent any fact the source lacks?
# (claims-diff reads two files: --prev is the source, --revised is the rewrite)
printf 'I worked at a bakery in Chicago.'              > prev.txt
printf 'I ran a famous bakery in Paris for ten years.' > revised.txt
uv run pangram-fit claims-diff --prev prev.txt --revised revised.txt
# -> truth_required: true  (new place, new duration) and exit code 6

# paid: the fitness score (needs PANGRAM_API_KEY)
echo "your text here" | uv run pangram-fit score -
```

Every subcommand that does work emits exactly one JSON object on stdout and
returns a documented exit code.

## Exit-code contract

| code | name | meaning |
|---|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 0 | OK | success |
| 2 | BAD_US
