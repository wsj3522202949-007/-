---
id: tool-01255
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: agno-story-generator
summary: 多 Agent 协作自动产文
source: https://github.com/cvoalex/agno-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1255
category: 二、网文 / 长篇 AI 写作系统 库
repo: cvoalex/agno-story-generator
stars: 1
url: https://github.com/cvoalex/agno-story-generator
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: e2627958c97d0542
  - methods/最强写作方法论_全球最强综合版.md
---

# cvoalex/agno-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/cvoalex/agno-story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Learning project demonstrating Agno AI framework with DeepSeek R1 for creative story generation
- **本地描述**：Learning project demonstrating Agno AI framework with DeepSeek R1 for creative story generation
- **拉取时间**：2026-07-23 23:15:42

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Learning - Agno AI Story Generator

This project demonstrates using the Agno AI framework with DeepSeek R1 to generate creative stories.

## Setup

1. Virtual environment is already created and activated:
   ```bash
   source venv/bin/activate
   ```

2. Dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

## Prerequisites

- Ollama must be running locally: `ollama serve`
- DeepSeek R1 model must be installed: `ollama pull deepseek-r1:32b`

## Usage

### Simple Ollama Version
```bash
python simple_story_generator.py
```

### Agno Framework Version
```bash
python story_generator.py
```

### Collaborative Writing Version
```bash
python collaborative_story_generator.py
```

### Team-based Writing Version
```bash
python team_story_generator.py
```

## Files

- `story_generator.py` - Uses Agno framework with DeepSeek R1
- `simple_story_generator.py` - Direct Ollama library implementation
- `collaborative_story_generator.py` - Multi-agent system with writer and editor collaboration
- `team_story_generator.py` - Uses Agno's team feature for coordinated writing
- `test_connection.py` - Tests Ollama connection and lists available models
- `requirements.txt` - Python dependencies

## Features

- Generates creative short stories (200-300 words)
- Uses DeepSeek R1's reasoning capabilities
- Supports streaming output
- Debug mode available in Agno version

## Customization

To generate different stories, modify the prompt in either script:
```python
prompt = "Write a short story about [your topic here]"
```
