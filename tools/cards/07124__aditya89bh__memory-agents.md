---
id: tool-07124
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: memory-agents
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/aditya89bh/memory-agents
created: 2026-07-18
updated: 2026-07-18
no: 7124
category: 画龙补充 / 扩容入库 — 补充源
repo: aditya89bh/memory-agents
stars: 0
url: https://github.com/aditya89bh/memory-agents
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# aditya89bh/memory-agents

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/aditya89bh/memory-agents
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：This repository documents a step-by-step journey into building memory agents. It covers short-term memory, summarization, long-term retrieval, salience, planning, and skill learning, treating memory as a core cognitive system rather than a feature.
- **本地描述**：memory-agents
- **拉取时间**：2026-07-25 19:11:34

---

# Memory Agents — From Continuity to Cognition

This repository is a progressive implementation of memory systems for AI agents.

The goal is not to build one chatbot with memory. The goal is to understand memory as a cognitive system: how agents keep continuity, compress experience, retrieve what matters, plan from outcomes, form skills, preserve identity, and eventually remember the world they act inside.

Memory is treated here as an architectural primitive, not a feature toggle.

---

## Core thesis

Most AI systems are stateless, reactive, short-lived, and context-fragile.

Real agents need memory that can:

- preserve continuity across turns
- decide what to forget
- retrieve relevant past experience
- influence future decisions
- turn repeated actions into skill
- maintain identity over time
- connect knowledge to environments and actions

The key shift is simple:

> Memory is not just what an agent stores. Memory is what changes what the agent does next.

---

## Project map

| Project | Theme | Core question | Status |
|---|---|---|---|
| Project 1 | Short-term memory | Can the agent maintain continuity across turns? | Complete |
| Project 1B | Summary memory | Can the agent compress older context without losing meaning? | Complete |
| Project 2 | Long-term memory | Can the agent retrieve relevant past information? | Complete |
| Project 3 | Unified memory stack | Can memory layers behave like one system? | Complete |
| Project 4 | Memory + planning | Can memory change the agent's decision? | Complete |
| Project 5 | Skill & task memory | Can repeated task attempts become reusable competence? | Complete |
| Project 6 | Identity memory | Can the agent remain consistent across time? | Planned |
| Project 7 | Embodied/world memory | Can memory attach to environments, states, and actions? | Planned |

---

## Architecture

```mermaid
flowchart TD
    A[User Input] --> B[Memory Gate]
    B --> C[Short-Term Memory]
    B --> D[Summary Memory]
    B --> E[Long-Term Retrieval]
    C --> F[Context Assembly]
    D --> F
    E --> F
    F --> G[Planning]
    G --> H[Action or Response]
    H --> I[Outcome Evaluation]
    I --> J[Memory Write]
    J --> C
    J --> D
    J --> E
```

The progression of this repo follows that architecture step by step.

---

## Projects

### Project 1 — Short-Term Memory: Continuity

**Goal:** Give the agent continuity across turns.

**What it proves:** A simple rolling memory buffer can preserve recent interaction state while enforcing deterministic forgetting.

**Built:**

- rolling window memory
- explicit forgetting
- deterministic context size
- clear separation between memory writing and memory reading

**Key insight:** Memory is not what you store. Memory is what you choose to forget.

Folder: `project-1-short-term-memory/`

---

### Project 1B — Summary Memory: Compression

**Goal:** Prevent context explosion while preserving meaning.

**What it proves:** Agents need compression, not infinite chronology.

**Built:**

- recent buffer
- running summary
- two-tier memory
- no recursive memory bloat

**Key insight:** Chronology does not scale. Compression is intelligence.

Folder: `project-1b-summary-memory/`

---

### Project 2 — Long-Term Memory: Retrieval

**Goal:** Move from recent context to searchable experience.

**What it proves:** The agent can retrieve relevant past information instead of only relying on what happened most recently.

Project 2 is split into four steps:

| Part | Focus | What it proves |
|---|---|---|
| 2A | Vector recall | Relevant memories can be retrieved using similarity search |
| 2B | Metadata-aware memory | Recall improves when memories have type, source, tags, and filters |
| 2C | Salience and gating | Not everything deserves to become long-term memory |
| 2D | Neural embeddings | Recall becomes more semantic and less keyword-bound |

**Key insight:** The agent should remember what matters right now, not only what happened last.

Folder: `project-2-long-term-memory/`

---

### Project 3 — Unified Memory Stack: Integration

**Goal:** Make short-term, summary, and long-term memory work as one system.

**What it proves:** Memory becomes useful when it is assembled into context through a disciplined read/write pipeline.

**Built:**

- unified `MemoryManager`
- memory gate
- context assembly pipeline
- clear read/write phases

**Key insight:** A real memory agent needs a memory operating system, not scattered memory functions.

Folder: `project-3-unified-memory-stack/`

---

### Project 4 — Memory + Planning: Cognition

**Goal:** Make memory influence decisions, not just answers.

**What it proves:** If the same request produces better behavior the second time because of stored experience, memory has become cognitive.

**Built:**

- action history memory
- outcome memory
- deterministic planner
- experience-based strategy change

**Example:** Last time this failed, choose a different strategy.

**Key insight:** Memory becomes intelligence when it changes future action.

Folder: `project-4-memory-planning/`

---

### Project 5 — Skill & Task Memory: Learning

**Goal:** Turn repetition into reusable competence.

**What it proves:** Repeated task attempts can become reusable skills that improve future execution.

**Built:**

- task attempt memory
- success/failure outcomes
- skill abstraction
- task-to-skill mapping

**Example:** This looks like a task I have done before.

**Key insight:** Skill is memory compressed into action.

Folder: `project-5-skill-memory/`

---

### Project 6 — Identity & Personality Memory

**Goal:** Make the agent consistent across weeks and months.

**Planned:**

- stable identity memory
- long-term user preferences
- trait resolution logic
- conflict handling between recent context and stable memory

**Example:** This user prefers concise answers and Python-first solutions.

Folder: `project-6-identity-memory/`

---

### Project 7 — Embodied / World Memory

**Goal:** Tie memory to environments, states, actions, and physical context.

**Planned:**

- spatial memory
- state-aware memory
- robotics world memory
- action outcome memory in environments

**Example:** In this environment, path B was safer last time.

Folder: `project-7-embodied-memory/`

---

## Design principles

- Memory is explicit, never implicit
- Retrieval happens before reasoning
- Forgetting is a feature
- Salience beats volume
- Context assembly is a first-class step
- Outcomes are learning signals
- Minimal frameworks, maximum clarity
- Colab-first, GitHub-second

---

## How to use this repo

Read the projects in order.

1. Start with continuity and forgetting.
2. Add compression.
3. Add retrieval.
4. Integrate memory layers.
5. Let memory influence planning.
6. Turn repeated outcomes into skills.
7. Extend memory into identity and embodiment.

This repo is designed as a learning path. Each project isolates one idea before combining it with the next.

---

## Status

| Area | Status |
|---|---|
| Projects 1–5 | Complete |
| Projects 6–7 | Planned |
| Architecture docs | Added |
| Glossary | Added |
| Roadmap | Added |

related:
  - methods/QUICK_START.md
---

## Final idea

If someone reads only this repo, they should understand one thing clearly:

> Memory is the bridge from reaction to cognition.
