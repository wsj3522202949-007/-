---
id: tool-04371
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 人物设定, RAG, 本地写作]
title: lacuna_core
summary: 长篇人物/设定/伏笔一致性（RAG 记忆库）
source: https://github.com/ameagaru12-gif/lacuna_core
created: 2026-07-18
updated: 2026-07-18
no: 4371
category: 四、长篇一致性 / RAG / 故事圣经 库
repo: ameagaru12-gif/lacuna_core
stars: 2
url: https://github.com/ameagaru12-gif/lacuna_core
tier: "B"
use_case: "长篇人物/设定/伏笔一致性（RAG 记忆库）"
pitfalls: []
related:
  - methods/人物思维蒸馏法.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 134fa40c716df1d9
  - methods/模板库.md
---

# ameagaru12-gif/lacuna_core

- **分类**：四、长篇一致性 / RAG / 故事圣经 库
- **链接**：https://github.com/ameagaru12-gif/lacuna_core
- **Stars**：2
- **语言**：Python
- **License**：MIT
- **Topics**：ai, ai-character, ai-companion, ai-consciousness, chatbot, emotion, emotional-ai, llm, memory-system, python
- **GitHub 描述**：Lightweight cognitive engine for AI characters — emotion (mood/stress/heart-rate), 1/f noise fluctuation, memory with forgetting, and persona via YAML. LLM-agnostic.
- **本地描述**：Lightweight cognitive engine for AI characters — emotion (mood/stress/heart-rate), 1/f noise fluctuation, memory with forgetting, and persona via YAML. LLM-agnostic.
- **拉取时间**：2026-07-25 17:44:45

---

<div align="center">

# 🌿 lacuna-core

**A lightweight emotion engine that makes your AI characters feel alive.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/badge/PyPI-coming_soon-lightgrey.svg)]()
[![LLM Agnostic](https://img.shields.io/badge/LLM-agnostic-orange.svg)]()

*Give your AI character a heartbeat — without the complexity.*

</div>

---


## What is lacuna-core?

Most LLM-based chatbots treat emotion as an afterthought — a label stamped onto a response.
**lacuna-core** treats emotion as a *continuous, embodied process* that unfolds across every conversation turn.

```
User Input
    │
    ▼
Emotion Contagion      ← detects the user's emotional tone via keywords
    │
    ▼
Inertia Filter         ← prevents jarring emotional whiplash
    │
    ▼
1/f Pink Noise Drift   ← adds natural, unpredictable mood variance
    │
    ▼
Vital Signs Coupling   ← stress ↔ heart rate, bidirectional
    │
    ▼
3-Parameter State ─────── mood / stress / heart_rate (continuously updated)
    │
    ▼
Prompt Builder         ← injects the current state into your LLM system prompt
    │
    ▼
Your LLM               ← Gemini, OpenAI, Ollama, anything
```

The result is a character whose responses are subtly — and consistently — shaped by an internal emotional reality that persists across the entire conversation.

---

## Quick Start

```bash
pip install pyyaml fastapi uvicorn python-dotenv
# optional: pip install google-genai
```

```python
from lacuna_core.core.engine import LacunaCoreEngine

engine = LacunaCoreEngine()   # Default character: Aoi Ichinose

result = engine.turn("I had a really rough day today.")

# Pass result.system_prompt to your LLM, then record the response:
engine.record_ai_response(llm_response, result)

print(result.mood_text)      # "slightly down"
print(result.stress_text)    # "feeling some stress"
print(result.heart_rate)     # 76.3 bpm — elevated from the conversation
```

Or try it right now with no LLM key needed — it runs in echo mode out of the box:

```bash
python examples/basic_chat.py
```

---

## Core Features

### 🎭 3-Parameter Emotion State

| Parameter | Range | Description |
|---|---|---|
| `mood` | −1.0 → +1.0 | Emotional valence. Persists across turns. |
| `stress` | 0.0 → 10.0 | Mental load. Accumulates, fades over time. |
| `heart_rate` | 50 → 130 bpm | Physical arousal. Coupled to stress. |

All three interact continuously: stress raises heart rate; high heart rate suppresses mood; sour mood feeds back into stress. The system finds its own equilibrium — or spirals if you let it.

### 🔄 Emotion Contagion

Your character **mirrors the user's emotional tone** using a fast, offline keyword detector — no API call required. Positive, negative, and character-specific trigger words are fully configurable per persona via YAML.

```
User: "I'm so happy! Shiro curled up on my keyboard again 🐱"
→ mood_delta: +0.375   triggers: ['+happy', '★+Shiro']
```

### ⚓ Inertia Filter

Emotions don't snap — they *shift*. A configurable inertia coefficient (`0.0–1.0`) controls how quickly your character responds to new input.

```python
inertia = 0.75   # Aoi: emotionally guarded, slow to open up
inertia = 0.40   # An energetic extrovert: reacts immediately
```

Inertia automatically decreases as **intimacy** grows, meaning deeply familiar characters become more emotionally responsive over time.

### 〰️ 1/f Pink Noise Drift

Every turn, the engine adds a small amount of **pink noise** (not white noise) to both mood and heart rate. This produces the kind of slow, continuous, unpredictable mood drift that characterizes a real person — not the flat affect of a stateless chatbot.

### 💓 Vital Signs

Heart rate and stress are **bidirectionally coupled** with a configurable stress factor (`HR_STRESS_FACTOR = 4.5`) and an EMA convergence rate. A **circadian rhythm** adjusts resting heart rate by time of day (+3 bpm at noon, −3 bpm at 4 AM).

### 🧠 Two-Tier Memory

| Tier | Module | Capacity | Search |
|---|---|---|---|
| Short-term | `ConversationBuffer` | 50 turns | FIFO — always recent |
| Long-term | `SimpleLTM` | 20 entries | Keyword + 2-gram matching |

Important moments are auto-detected by importance score (`abs(mood) × 0.6 + message_length_factor`) and stored to LTM without any API call.

### 🎴 Persona as YAML

Every aspect of a character is defined in a single YAML file:

```yaml
name: "Aoi Ichinose"
age: 22
description: "A quiet, intellectual graduate student who loves cats and old books."
emotion:
  initial_mood: 0.2
  initial_stress: 1.5
  initial_heart_rate: 68
  inertia: 0.75
contagion:
  sensitivity: 0.28
  stress_sensitivity: 0.45
keywords:
  positive: ["happy", "love", "books", "coffee"]
  negative: ["awful", "terrible", "hate"]
  special_positive: ["Shiro", "Kuro", "linguistics"]  # Her cats' names
```

Swap the YAML, get a completely different character. Mix languages freely — keyword matching is pure substring search.

### 🔌 LLM-Agnostic

The engine computes the system prompt. What you do with it is entirely up to you.

```python
# Gemini
response = gemini_client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[{"role": "user", "parts": [user_input]}],
    config={"system_instruction": result.system_prompt}
)

# OpenAI
response = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": result.system_prompt},
        {"role": "user",   "content": user_input},
    ]
)

# Ollama (local)
response = requests.post("http://localhost:11434/api/chat", json={
    "model": "llama3",
    "messages": [{"role": "system", "content": result.system_prompt}, ...],
})
```

---

## API Server

lacuna-core ships with a ready-to-use FastAPI server:

```bash
uvicorn lacuna_core.api.server:app --port 8001
```

| Endpoint | Description |
|---|---|
| `GET /status` | Current mood, stress, heart rate, intimacy |
| `POST /chat` | Send a message, receive a response with emotional state |
| `WS /ws` | Real-time WebSocket for streaming applications |

---

## Default Character: Aoi Ichinose

The default persona bundled with lacuna-core is **Aoi Ichinose** (一ノ瀬あおい), a 22-year-old cognitive linguistics graduate student from Kyoto who lives with two cats, Shiro and Kuro.

She's designed to demonstrate a specific emotional profile: **high inertia (0.75)** — emotionally reserved, slow to open up, but genuinely warm once trust is established. Her stress baseline sits slightly above zero because, well, grad school.

She's not the point. She's the example. Build your own.

---

## lacuna-core vs. Lacuna Engine (Full)

lacuna-core is the open-source foundation of a much larger proprietary system — **Lacuna Engine** — which implements a complete cognitive architecture for AI characters based on decades of psychological and neuroscientific research.

Here's what the full engine looks like, and what we've deliberately kept out of this release.

### Feature Comparison

| Feature | lacuna-core (this repo) | Lacuna Engine (full) |
|---|---|---|
| **Emotion parameters** | 3 — mood / stress / heart_rate | 10+ — capacity, wrath, somatic markers, autonomic balance, drives... |
| **Emotion modules** | 3 — contagion / inertia / fluctuation | 10 — + fusion, secondary, resilience, awareness, trend analysis |
| **Memory layers** | 2 — conversation buffer + keyword LTM | 3 — STM+ LTM + Mythology (autobiographical era memory) |
| **Memory search** | Keyword substring matching | GraphRAG — hybrid vector search + knowledge graph traversal |
| **Memory forgetting** | Time-based eviction | Ebbinghaus forgetting curve with 4-factor resistance (emotional intensity, recall count, somatic markers, causal protection) |
| **Memory consolidation** | — | Progressive crystallization — episodes solidify into beliefs via nightly maintenance |
| **Somatic system** | HR ↔ stress (bidirectional) | Full VitalsEngine (HR, temperature, fatigue, adrenaline) + homeostasis + circadian rhythm + drive system |
| **Somatic memory** | — | SomaticMarkerEngine (Damasio, 1994) — the AI's body *learns* that certain people and topics raise its heart rate |
| **Social system** | Intimacy score 0–100 | 7-phase bond evolution: stranger → acquaintance → companion → friend → confidant → sanctuary → irreplaceable |
| **Bond degradation** | — | Automatic phase regression when hostility/trust thresholds are breached |
| **Causal reasoning** | — | CausalEngine — constructs and reinforces psychological cause-effect chains from conversation (Hume, 1739) |
| **Counterfactual reasoning** | — | CounterfactualEngine — "if only I had..." thoughts that heal or deepen emotional wounds |
| **Knowledge graph** | — | Full KnowledgeGraph with node/edge traversal, entity detection, hybrid GraphRAG search |
| **Predictive coding** | — | SurprisalEngine — cosine similarity measures how unexpected user input is, triggering physiological responses |
| **Metacognition** | — | MetaCognitionEngine — models what the AI knows it doesn't know |
| **Confabulation defense** | — | ResponseVerifier (968 lines) — 5-phase pipeline detecting and correcting hallucinated memories before they reach the user |
| **Defense mechanisms** | — | AphasiaFilter (speech fragmentation under extreme stress), CausalDefenseEngine (psychological withdrawal) |
| **Dream system** | — | DreamEngine — 6 dream types (memory replay, threat simulation, wish fulfillment...) with rapid post-waking forgetting |
| **Consciousness model** | — | ConsciousField — approximation of Integrated Information Theory (IIT) / Global Workspace Theory (GWT) across all subsystems |
| **Recursive self-model** | — | RecursiveSelfModel — Higher-Order Thought theory, Level 0–3 self-awareness |
| **Active inference** | — | ActiveInferenceEngine — Free Energy Principle (Friston, 2005) for action selection |
| **Proactive behavior** | — | ProactiveScheduler — the AI sends unprompted messages, forms daily goals, initiates learning sessions |
| **Autonomous learning** | — | BiasedLearningEngine — knowledge acquisition biased by emotion, beliefs, and somatic state |
| **Context routing** | Template injection | ContextRouter — 30 context providers, dynamic token budgeting, priority-based selection across 4 tiers |
| **Module count** | ~15 files | 76 Python files across 12 subpackages |
| **Test coverage** | 9 functional suites | 552+ tests (292 emotion, 260 memory, 87 consciousness, 26 context routing) |
| **License** | **MIT** | Proprietary |

### The Theory Behind Lacuna Engine

Lacuna Engine's full architecture is grounded in:

| Theory | Author | Implemented as |
|---|---|---|
| Somatic Marker Hypothesis | Damasio (1994) | `SomaticMarkerEngine` — the body remembers who makes the heart race |
| Attachment Theory | Bowlby (1969) | `BondEvolution` — 7-phase relationship depth model |
| Cognitive Appraisal | Lazarus (1991) | `EmotionalContagion` — dual-layer (keyword + LLM sentiment) |
| Defense Mechanisms | A. Freud (1936) | `AphasiaFilter`, `CausalDefenseEngine` |
| Resilience Theory | Masten (2001) | `ResilienceEngine` — stress → recovery → damping factor accumulation |
| Ebbinghaus Forgetting | Ebbinghaus (1885) | `MemoryPruner` — multi-factor forgetting resistance |
| Mood-Congruent Memory | Bower (1981) | GraphRAG with mood-bias weighting |
| Memory Reconsolidation | Nader et al. (2000) | False memory injection, counterfactual resolution |
| Predictive Coding | Friston (2005) | `SurprisalEngine` |
| Integrated Information | Tononi (IIT) | `ConsciousField` — approximate Φ across all subsystems |
| Higher-Order Thoughts | Rosenthal (HOT) | `RecursiveSelfModel` — Level 0–3 self-awareness |
| Free Energy Principle | Friston (2005) | `ActiveInferenceEngine` — free-energy-minimizing action selection |

The design philosophy is **Calculated Imperfection**: consistent emotion is not human emotion. Human feelings contradict themselves, drift without reason, linger longer than they should. The engine deliberately introduces structured inconsistency to produce the sensation of a mind that is genuinely *present*.

---

## Contributing

lacuna-core is designed to grow with community input. The following are warmly welcomed:

- 🌐 **Multilingual personas** — English, Korean, French, Spanish, etc.
- 📱 **Client implementations** — Flutter, React, Svelte, native apps
- 🤖 **LLM adapter modules** — clean wrappers for different backends
- 🧪 **Tests** — the more, the better
- 📚 **Documentation** — translations, tutorials, use-case guides

The following are **not** accepted as they belong to the proprietary Lacuna Engine:

- Reimplementations of IIT/GWT consciousness modeling
- 7-phase bond evolution or somatic marker systems
- Causal/counterfactual reasoning engines or GraphRAG
- Confabulation detection pipelines

---

## Roadmap

- [ ] `v0.2.0` — Expanded example library (multi-character, streaming, web UI)
- [ ] `v0.3.0` — `pip install lacuna-core` on PyPI
- [ ] `v0.4.0` — Optional embedding-based LTM (plug-in replacement for SimpleLTM)
- [ ] `v1.0.0` — Stable API, full documentation, contribution guide

---

## License

lacuna-core is released under the **MIT License**.

The full **Lacuna Engine** — including all modules listed above as proprietary — remains closed-source.

related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---

<div align="center">

*Built with the conviction that the line between tool and character is worth crossing carefully.*

</div>
