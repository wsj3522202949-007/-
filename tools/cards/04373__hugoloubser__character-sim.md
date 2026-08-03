---
id: tool-04373
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 人物设定, RAG]
title: character-sim
summary: 长篇人物/设定/伏笔一致性（RAG 记忆库）
source: https://github.com/hugoloubser/character-sim
created: 2026-07-18
updated: 2026-07-18
no: 4373
category: 四、长篇一致性 / RAG / 故事圣经 库
repo: hugoloubser/character-sim
stars: 0
url: https://github.com/hugoloubser/character-sim
tier: "C"
use_case: "长篇人物/设定/伏笔一致性（RAG 记忆库）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---

# hugoloubser/character-sim

- **分类**：四、长篇一致性 / RAG / 故事圣经 库
- **链接**：https://github.com/hugoloubser/character-sim
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：System for creating and managing interactive, LLM-backed characters with rich personalities, dynamic evolution, and authentic multi-character dialogue. Characters maintain consistent behaviour rooted in MBTI/OCEAN personality science, tiered memory, and real-time trait evolution, producing emergent interactions that grow more nuanced over time.
- **本地描述**：System for creating and managing interactive, LLM-backed characters with rich personalities, dynamic evolution, and authentic multi-character dialogue. Characters maintain consistent behaviour rooted in MBTI/OCEAN personality science, tiered memory, and real-time trait evolution, producing emergent interactions that grow more nuanced over time.
- **拉取时间**：2026-07-25 17:44:50

---

# 🎭 Character Creator

An advanced system for creating and managing interactive, LLM-backed characters
with rich personalities, dynamic evolution, and authentic multi-character
dialogue. Characters maintain consistent behaviour rooted in MBTI/OCEAN
personality science, tiered memory, and real-time trait evolution — producing
emergent interactions that grow more nuanced over time.

## Features

### Personality & Identity
- **9-Axis Personality Model** — assertiveness, warmth, openness,
  conscientiousness, emotional stability, humour, formality, extraversion,
  and agreeableness (0 – 1 continuous scale)
- **MBTI Integration** — all 16 types with archetype labels, compatibility
  scoring, and communication-style inference
- **Values, Beliefs & Quirks** — speech patterns, strengths, weaknesses,
  dislikes, and priority keywords that shape every response
- **Heredity** — breed new characters from two parents via single-gene
  crossover with Gaussian mutation

### Memory & Cognition
- **Tiered Memory** — working → short-term → long-term condensation pipeline
  with emotional weighting and salience decay
- **Ground-Truth Log** — immutable record of raw exchanges for auditing
- **Emotional State Tracking** — current emotion influences dialogue and
  internal monologue

### Dynamic Character Evolution
- **Experience Classification** — every exchange is tagged by type (conflict,
  vulnerability, success, discovery, etc.)
- **Trait Micro-Shifts** — personality traits drift in response to classified
  experiences via influence vectors
- **Self-Reflection** — periodic LLM-generated self-model capturing
  self-concept, emotional awareness, and growth edges
- **Cognitive Dissonance** — automatic detection of value/behaviour
  misalignment that surfaces internal tension
- **Milestone Reviews** — LLM-adjudicated scene-end personality review with
  validated trait shifts and narrative summary

### Dialogue Engine
- **Multi-Character Scenes** — 2 – 5 characters with personality-weighted
  speaker selection (extraversion, assertiveness, warmth, openness,
  compatibility)
- **Internal Monologue** — private thoughts reflecting hidden motivations and
  active dissonances
- **Step-Wise & Continuous Modes** — advance one exchange at a time or run
  the full scene automatically
- **User Participation** — jump into any scene as yourself with your own
  profile

### LLM Integration
- **Three Providers** — OpenAI, Anthropic, and Google (Gemini via
  OpenAI-compatible endpoint) with async support
- **Structured Output** — `generate_with_format()` for typed JSON responses
- **Transparent Instrumentation** — every LLM call is recorded with latency,
  tokens, call type, and success/failure via `InstrumentedProvider`
- **Prompt Templates** — reusable, validated templates in `llm/prompts.py`

### Observability
- **Metrics Dashboard** — real-time Streamlit page with KPIs, subsystem
  breakdowns, latency charts, cumulative timeline, and CSV export
- **JSONL Persistence** — metrics survive across sessions via file-backed
  `MetricsCollector`
- **Structured Logging** — `structlog` throughout the system

### Persistence
- **SQLite** — character database with full CRUD and interaction archive with
  scene metadata and exchange history
- **Repository Pattern** — swappable backends (in-memory, SQLite, extensible
  to Postgres)

### APIs & UIs
- **Streamlit UI** — onboarding, character workshop, scene director,
  interaction archive, metrics dashboard, and settings
- **FastAPI REST API** — character CRUD, dialogue generation, and scene
  management with Swagger UI at `/docs`

### Code Quality
- **391 tests** (16 test files) with strict markers and verbose output
- **Ruff** — 20+ rule categories, zero tolerance, enforced via pre-commit
- **mypy** — static type checking with Pydantic plugin
- **Bandit** — security scanning
- **Conventional Commits** via Commitizen
- **49 named constants** — no magic literals

## Project Structure

```
character_creator/
├── src/character_creator/
│   ├── core/
│   │   ├── character.py         # Character entity with memory & evolution state
│   │   ├── constants.py         # Named constants (single source of truth)
│   │   ├── database.py          # Repository pattern (SQLite + in-memory)
│   │   ├── dialogue.py          # Dialogue engine, speaker selection, scene flow
│   │   ├── heredity.py          # Genetic crossover and mutation
│   │   ├── interaction.py       # InteractionRecord & SQLite archive
│   │   ├── memory.py            # Background, Memory, Values models
│   │   ├── memory_tiered.py     # Tiered memory store & condenser
│   │   ├── personality.py       # PersonalityTraits, MBTI, compatibility
│   │   ├── self_model.py        # Self-reflection & dissonance detection
│   │   └── trait_evolution.py   # Experience classification & trait shifts
│   ├── llm/
│   │   ├── metrics.py           # MetricsCollector, InstrumentedProvider
│   │   ├── prompts.py           # Prompt templates
│   │   └── providers.py         # OpenAI, Anthropic, Google providers
│   ├── api/
│   │   ├── main.py              # FastAPI app
│   │   ├── models.py            # Pydantic request/response models
│   │   └── routes/              # Character & interaction endpoints
│   ├── ui/
│   │   ├── app.py               # Streamlit application
│   │   └── dashboard.py         # Metrics dashboard page
│   ├── utils/
│   │   ├── config.py            # pydantic-settings configuration
│   │   ├── logging.py           # structlog setup
│   │   ├── path.py              # Import path utilities
│   │   └── validators.py        # Input validation
│   └── demos/
│       ├── basic_interaction.py
│       ├── live_dialogue.py
│       └── multi_character_scene.py
├── tests/                        # 391 tests across 16 files
├── local/                        # Git-ignored runtime data
├── pyproject.toml
├── ruff.toml
└── .pre-commit-config.yaml
```

## Installation

### Prerequisites
- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager

### Setup

```bash
cd character_creator
uv venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
uv pip install -e ".[dev]"
```

### Configuration

Copy `.env.example` to `local/.env` and add at least one API key:

```
LLM_PROVIDER=google               # openai | anthropic | google
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...
DEFAULT_MODEL=gemini-2.0-flash
```

## Quick Start

### Streamlit UI

```bash
streamlit run src/character_creator/ui/app.py
```

Opens at `http://localhost:8501` with onboarding, character workshop, scene
director, archive, dashboard, and settings pages.

### FastAPI Service

```bash
uvicorn character_creator.api.main:app --reload
```

Swagger UI at `http://localhost:8000/docs`.

### Demo Scripts

```bash
python -m character_creator.demos.basic_interaction
python -m character_creator.demos.multi_character_scene
python -m character_creator.demos.live_dialogue
```

## Documentation

| Document | Audience | Description |
|----------|----------|----------related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---|
| [INSTALLATION_SETUP.md](INSTALLATION_SETUP.md) | Everyone | Prerequisites, environment setup, troubleshooting |
| [QUICKSTART.md](QUICKSTART.md) | Everyone | 5-minute start guide |
| [USER_GUIDE.md](USER_GUIDE.md) | End users | Streamlit UI walkthrough |
| [API_DOCUMENTATION.md](API_DOCUMENTATION.md) | Integrators | REST API reference with examples |
| [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) | Contributors | Architecture patterns, extension points, testing |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Contributors | System design and design decisions |

## Code Quality

```bash
# Lint
python -m ruff check src/ tests/

# Format
python -m ruff format src/ tests/

# Type check
mypy src/

# Test
python -m pytest tests/ -v

# All pre-commit hooks
pre-commit run --all-files
```

## Contributing

1. All code must pass Ruff, mypy, and Bandit checks.
2. Every function requires complete type hints.
3. New functionality requires tests.
4. Constants go in `core/constants.py`.
5. Commit messages follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

## License

MIT
