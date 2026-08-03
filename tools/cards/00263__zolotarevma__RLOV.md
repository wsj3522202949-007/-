---
id: tool-00263
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: RLOV
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/zolotarevma/rlov
created: 2026-07-18
updated: 2026-07-18
no: 263
category: 二、网文 / 长篇 AI 写作系统 库
repo: zolotarevma/RLOV
stars: 0
url: https://github.com/zolotarevma/rlov
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# zolotarevma/RLOV

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/zolotarevma/rlov
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：RLOV: a modular framework for adaptive story generation in RPG/quest games (DQN planner + LLM generator + validator) / Модульный фреймворк для адаптивной генерации сюжетов в RPG/квестах (DQN-планировщик + LLM-генерация + валидатор)
- **本地描述**：RLOV: a modular framework for adaptive story generation in RPG/quest games (DQN planner + LLM generator + validator) / Модульный фреймворк для адаптивной генерации сюжетов в RPG/квестах (DQN-планировщик + LLM-генерация + валидатор)
- **拉取时间**：2026-07-23 22:46:45

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# RLOV: RL-LLM Orchestrator with Validation

A hybrid system for generating adaptive storylines in turn-based quest/RPG video games. Prototype developed as part of a bachelor's thesis.

## Core Components

- **RL Planner** (DQN) — learnable macro-management of narrative beacons.
- **LLM Generator** — creates scenes and dialogues using large language models (local Ollama, Gemini, OpenRouter, GigaChat).
- **Validation Module** — formal graph verification and JSON response checking for LLM output.

## Installation

```bash
git clone https://github.com/zolotarevma/RLOV
cd RLOV
pip install -r requirements.txt
```

## API Key Setup

For cloud-based LLMs, set the following environment variables:

- `OPENROUTER_API_KEY` — OpenRouter API key (https://openrouter.ai/keys)
- `GEMINI_API_KEY` — Google AI Studio API key (https://makersuite.google.com/app/apikey)
- `GIGACHAT_AUTHORIZATION_KEY` – GigaChat authorization key ([GigaChat API dashboard](https://developers.sber.ru/studio))

Local models run via [Ollama](https://ollama.com).

## Configuration

All parameters are in `config.py`:

- `LLM_CLIENT` — `"stub"`, `"ollama"`, `"gemini"`, `"openrouter"` or `gigachat`
- `LANGUAGE` – `"en"` or `"ru"` (scene generation language)
- `OLLAMA_MODEL` — model name (e.g., `"llama3.1:8b"`)
- `PLANNER` — `"heuristic"` or `"dqn"`
- `GIGACHAT_MODEL` – GigaChat model (default `"GigaChat-2"`)

## Usage

Interactive mode (console game):
```bash
python main.py
```

## Batch experiment

```bash
python experiments/run_experiment.py dqn 20
```

## Planner comparison

```bash
python experiments/compare_planners.py 30
```

## Pre-trained RL Models

The `.backups` folder contains pre-trained models for two scenarios:
- `dqn_model_mayor.pt` / `flags_order_mayor.json` – for the "Mayor's Support" scenario (mayor_support.json)
- `dqn_model_expedition.pt` / `flags_order_expedition.json` – for the "Expedition" scenario (expedition.json)

To use a pre-trained model, copy the required pair to the project root and rename them:
```bash
cp .backups/dqn_model_mayor.pt dqn_model.pt
cp .backups/flags_order_mayor.json flags_order.json
```

## Scenarios

The project includes two non-linear scenarios:

- **Mayor's Support** (`experiments/scenarios/mayor_support.json`) – the main scenario used in the thesis, with 16 beacons and 3 endings.
- **Expedition to the Forgotten Temple** (`experiments/scenarios/expedition.json`) – a more complex scenario with multiple macro-choice points for the RL agent, used in advanced experiments.

Both scenarios are available in English and Russian (`*_ru.json`).

## Graphical Interface

A **Streamlit**-based web interface (`app_gui.py`) turns the console prototype into an interactive demo with a dark RPG theme.

**Features:**
- Visual display of scene, dialogues, and action choices.
- Filtering of completed quests.
- Automatic RL macro-choice with a loading animation.
- Colour-coded ending screens (🏆 perfect, ⚖️ good, 💀 bad).
- «Restart» button in the sidebar.

**Launch:**
```bash
streamlit run app_gui.py
```

## Author

Maxim Zolotarev, St Petersburg University, 2026.
