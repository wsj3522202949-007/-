---
id: tool-01371
type: tool
area: 库
status: active
tags: [互动叙事, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: Story-Forge-Backend
summary: 互动叙事/聊天写故事
source: https://github.com/mattocad/story-forge-backend
created: 2026-07-18
updated: 2026-07-18
no: 1371
category: 二、网文 / 长篇 AI 写作系统 库
repo: mattocad/Story-Forge-Backend
stars: 3
url: https://github.com/mattocad/story-forge-backend
tier: "B"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# mattocad/Story-Forge-Backend

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mattocad/story-forge-backend
- **Stars**：3
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Story Forge is an interactive fiction platform that transforms traditional storybooks into AI-powered text-adventure games using local large language models (LLMs). This backend, built with FastAPI, handles narrative generation by querying local models through the Ollama framework.
- **本地描述**：Story Forge is an interactive fiction platform that transforms traditional storybooks into AI-powered text-adventure games using local large language models (LLMs). This backend, built with FastAPI, handles narrative generation by querying local models through the Ollama framework.
- **拉取时间**：2026-07-23 23:19:06

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Story Forge – Backend

Story Forge is an interactive fiction platform that transforms traditional storybooks into AI-powered text-adventure games using local large language models (LLMs). This backend, built with FastAPI, handles narrative generation by querying local models through the Ollama framework.

## Features

- FastAPI server with RESTful endpoints
- Local LLM integration (tested with LLaMA 2 and 3 via Ollama)
- Structured narrative control using YAML-based "Story Cards"
- Adjustable model temperature to toggle narrative strictness
- Session restart, input handling, and export functionality

## Requirements

- Python 3.10 or higher
- [Ollama](https://ollama.com/) installed locally and running a supported model
- pip packages listed in `requirements.txt`

## Installation

git clone https://github.com/yourusername/storyforge-backend.git
cd storyforge-backend
pip install -r requirements.txt
Running the Server
bash
Copy
Edit
uvicorn main:app --reload
This starts the backend on http://localhost:8000.

API Endpoints
POST /start: Initializes a new game session

POST /choice: Submits a player decision (e.g., "1", "2", "3")

POST /restart: Resets the current session

GET /export: Returns the session transcript as plain text

## Project Structure
graphql
Copy
Edit
storyforge-backend/
├── main.py                # FastAPI app and routing
├── prompts/
│   └── system_prompt.txt  # Base prompt for initializing gameplay
├── models/
│   └── story_card.yaml    # Narrative structure and event guide
├── utils/
│   └── game_loop.py       # Core interaction logic
└── requirements.txt

## Notes
Story Cards guide AI output to maintain consistency with the original narrative.

Responses are turn-based and triggered by numerical choices.

Backend was tested with llama3:8b and performs best with a context window over 8,000 tokens.

## License
Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
© 2025 Matthew Nazarian
