---
id: tool-07348
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 本地写作]
title: lm_world_gen
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/jwest33/lm_world_gen
created: 2026-07-18
updated: 2026-07-18
no: 7348
category: 画龙补充 / 扩容入库 — 补充源
repo: jwest33/lm_world_gen
stars: 9
url: https://github.com/jwest33/lm_world_gen
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: bfff359d1ebce5ab
  - methods/QUICK_START.md
---

# jwest33/lm_world_gen

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/jwest33/lm_world_gen
- **Stars**：9
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Generate complete fictional world content (regions, factions, characters, dialog trees) using LLMs. 
- **本地描述**：lm_world_gen
- **拉取时间**：2026-07-25 19:18:40

related:
  - methods/QUICK_START.md
---

# Fictional World Generation Pipeline

Generate complete fictional world content (regions, factions, characters, dialog trees) using LLMs. 

## Requirements

- Python 3.11+
- An OpenAI-compatible API (llama.cpp, ollama, vLLM, OpenAI, etc.)

Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### 1. Start an LLM Server

Any OpenAI-compatible API works:

```bash
# llama.cpp
llama-server --model <model.gguf> --port 8080

# ollama
ollama serve  # uses port 11434

# or use OpenAI API directly
```

### 2. Generate World Content

```bash
python lm_world_gen.py
```

This reads `world_config.yaml` and generates content to `generated_world.json`.

**Options:**
```bash
python lm_world_gen.py --base-url http://localhost:11434/v1  # ollama
python lm_world_gen.py --config my_game.yaml                 # different config
python lm_world_gen.py --resume                              # resume interrupted generation
python lm_world_gen.py --regions 3 --factions 5              # customize counts
python lm_world_gen.py --output my_world.json                # custom output file
```

### 3. View & Edit in Browser

Open `world-viewer/index.html` in a browser. Use "Load JSON" to open your `generated_world.json`.

With an LLM server running, the editor can also generate new content and regenerate fields.

## Configuration

Edit `world_config.yaml` to customize:
- Game name and seed concept
- Tone and naming conventions
- Lore, creatures, and phenomena
- Dialog examples and mechanics

The config is required - generation will fail without it.

## License

[MIT](https://github.com/jwest33/lm_world_gen/blob/main/LICENSE)
