---
id: tool-04370
type: tool
area: 库
status: active
tags: [RAG, Python, 协议未明, 本地优先, 英文文档, 人物设定, 本地写作]
title: baseline
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/aaelfe/baseline
created: 2026-07-18
updated: 2026-07-18
no: 4370
category: 四、长篇一致性 / RAG / 故事圣经 库
repo: aaelfe/baseline
stars: 0
url: https://github.com/aaelfe/baseline
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/人物思维蒸馏法.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 3e10e73505aa4738
  - methods/模板库.md
---

# aaelfe/baseline

- **分类**：四、长篇一致性 / RAG / 故事圣经 库
- **链接**：https://github.com/aaelfe/baseline
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Test harness for evaluating LLM character persistence, personality consistency, and drift across models and memory architectures
- **本地描述**：Test harness for evaluating LLM character persistence, personality consistency, and drift across models and memory architectures
- **拉取时间**：2026-07-25 17:44:43

related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---

# Baseline

A test harness for evaluating how well LLMs maintain persistent character identities over time.

Named after the [baseline test](https://bladerunner.fandom.com/wiki/Baseline_Test) from Blade Runner 2049 — a drift detection test for artificial beings.

## What It Does

Baseline defines characters as structured config, runs them through simulated scenarios with scripted events and interactions, then probes them at intervals for factual recall, personality consistency, hallucination, and relationship continuity. A separate judge model scores everything, producing degradation curves over time.

The memory/persistence backend is swappable — same characters, same simulation, same probes, different implementations. Results are directly comparable across backends and models.

## Core Concepts

- **Characters**: Defined as YAML config with identity, personality traits, opinions, relationships, speech patterns, and known memories. Every aspect is auditable against responses.
- **Scenarios**: Structured simulation loops that put characters through daily cycles of events and interactions.
- **Probes**: Evaluation questions injected at intervals that test factual recall, personality consistency, hallucination resistance, and relationship continuity.
- **Judge**: A separate LLM that scores probe responses against character definitions and event history.
- **Backends**: Pluggable memory/persistence implementations (naive context stuffing, summarization, RAG, Letta, custom).

## Project Status

Early development. Not yet functional.

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Run a simulation
baseline run --scenario scenarios/daily_check_in.yaml --characters characters/ --backend naive --days 30

# Evaluate results
baseline evaluate --run-id <run_id>

# Compare backends
baseline compare --run-ids <id1> <id2> <id3>
```

## Project Structure

```
baseline/
  __init__.py
  cli.py              # CLI entry point
  character.py         # Character definition loading and validation
  simulation.py        # Simulation loop engine
  judge.py             # LLM judge for scoring probe responses
  backends/
    __init__.py
    base.py            # Backend interface
    naive.py           # Raw context window stuffing
    summarization.py   # Compress older interactions into summaries
    rag.py             # Vector DB retrieval
  probes/
    __init__.py
    base.py            # Probe interface
    recall.py          # Factual recall probes
    consistency.py     # Personality consistency probes
    hallucination.py   # Hallucination detection probes
    relationship.py    # Relationship continuity probes
characters/            # Example character definitions (YAML)
scenarios/             # Scenario definitions (YAML)
tests/                 # Test suite
```

## License

MIT
