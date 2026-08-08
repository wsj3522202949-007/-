---
id: tool-07346
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议未明, 需API密钥, 英文文档]
title: aum-golly-3-agentic-ai-poetry
summary: 多 Agent 协作自动产文
source: https://github.com/jumaaho/aum-golly-3-agentic-ai-poetry
created: 2026-07-18
updated: 2026-07-18
no: 7346
category: 画龙补充 / 扩容入库 — 补充源
repo: jumaaho/aum-golly-3-agentic-ai-poetry
stars: 0
url: https://github.com/jumaaho/aum-golly-3-agentic-ai-poetry
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: a61e5ccde64e3277
  - methods/QUICK_START.md
---

# jumaaho/aum-golly-3-agentic-ai-poetry

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/jumaaho/aum-golly-3-agentic-ai-poetry
- **Stars**：0
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：Multi-agent AI poetry generation system with iterative refinement pipeline
- **本地描述**：aum-golly-3-agentic-ai-poetry
- **拉取时间**：2026-07-25 19:18:35

related:
  - methods/QUICK_START.md
---

# Aum Golly 3: Agentic AI Poetry

A multi-agent AI pipeline for generating, refining, and evolving poetry through iterative collaboration between specialized AI agents. Supports OpenAI GPT, Anthropic Claude, and Google Gemini models.

This tool was used to create [Aum Golly 3 – Perfectly Fine Poems on Humanity by Artificial Intelligence](https://aumgolly.com) in 8 hours.

## Features

- **Multi-Agent Pipeline**: Generator → Critic → Editor → Continuity chain
- **Iterative Refinement**: Multiple rounds of critique and revision
- **Branching Mode**: Explore alternative directions from continuation prompts
- **Provider Agnostic**: Seamlessly mix models from OpenAI, Anthropic, and Google
- **Budget Control**: Token limits, cost tracking, and rate limiting
- **Form Support**: 15+ poetic forms including haiku, sonnet, ghazal, and freeform
- **Streamlit UI**: Web interface for configuration and job management

## Quick Start

### Prerequisites

- Python 3.8+
- API keys from at least one provider:
  - OpenAI (GPT models)
  - Anthropic (Claude models)
  - Google AI Studio (Gemini models)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jumaaho/aum-golly-3-agentic-ai-poetry.git
cd aum-golly-3-agentic-ai-poetry
```

2. Create virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure API keys:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

5. Run the application:
```bash
streamlit run main.py
# Or use the provided script:
./run_streamlit.sh
```

## Configuration

### Model Presets

The system includes several preset configurations:

- **Fast**: Quick generation using lighter models (Claude Haiku, GPT-4o-mini, Gemini Flash)
- **Mid-tier**: Balanced quality and cost (Claude Sonnet, GPT-4o, Gemini Pro)
- **Premium**: Highest quality (Claude Opus, GPT-5)
- **Single-model**: Use one model for all agents

Or mix and match models for each agent role.

### Poetic Forms

Choose from 15+ supported forms in `prompts/forms/`:
- Freeform, Haiku, Sonnet, Ghazal
- Prose poem, Fragment, Epistolary
- List poem, Short lyric, Urban humorous
- And more...

### Pipeline Modes

**Sequential Mode** (`core/chain.py`):
- Linear pipeline: Generate → Critique → Edit → Continue
- Depth control for iterative refinement
- Best for exploring a single direction

**Branching Mode** (`core/chain_branching.py`):
- Creates "before" and "after" branches from continuity prompts
- Exponential exploration of poem variations
- Hard depth limit for safety (MAX_BRANCHING_DEPTH = 4)

## Architecture

See [ARCHITECTURE.md](https://github.com/jumaaho/aum-golly-3-agentic-ai-poetry/blob/main/ARCHITECTURE.md) for detailed system design.

**Core Components:**
- `main.py` - Streamlit UI
- `agents/` - Specialized AI agents (generator, critic, editor, continuity, translator)
- `core/` - Pipeline logic, model routing, budget control, job management
- `prompts/` - Agent instructions and form templates

## Usage Example

1. Enter a seed prompt: "two men in a boat"
2. Select theme (optional): "memory"
3. Choose form: "Freeform"
4. Pick model preset: "Mid-tier"
5. Set depth: 3 (poem will evolve through 3 iterations)
6. Configure temperature: 0.7
7. Click "Submit Job"
8. Watch as the pipeline generates, critiques, and refines your poem

## Budget Control

The system includes built-in safeguards:
- Token limits per job
- Cost tracking in USD
- Rate limiting (requests/minute)
- Automatic job timeout

Configure in the UI or modify `core/budget.py`.

## Generated Content

Poems are saved to:
- `data/poems/{job_id}/` - Individual generation files
- `data/saved/` - Curated collection with metadata

## Sharing Your Work

If you create poems using this system and share them publicly, we'd appreciate a mention!

**Suggested attribution:**
```
Generated with the Aum Golly 3 Agentic AI Poetry Machine (https://aumgolly.com)
```

This helps others discover the tool and connects your work to the broader Aum Golly poetry project.

## License

This project is licensed under the **PolyForm Noncommercial 1.0.0** license.

You may use this software for:
- Personal projects and experimentation
- Research and education
- Noncommercial artistic work
- Nonprofit organizations

Commercial use requires a separate license. See [LICENSE](https://github.com/jumaaho/aum-golly-3-agentic-ai-poetry/blob/main/LICENSE) for full terms.

## Attribution

Copyright (C) 2025 Jukka Aalho

## Acknowledgments

Built with Claude Code as part of the Aum Golly poetry book series project.

## Contributing

This is a personal project, but issues and suggestions are welcome via GitHub Issues.
