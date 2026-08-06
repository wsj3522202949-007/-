---
id: tool-00936
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: fiction-character-memory-agent
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/jennyhuang17/fiction-character-memory-agent
created: 2026-07-18
updated: 2026-07-18
no: 936
category: 二、网文 / 长篇 AI 写作系统 库
repo: jennyhuang17/fiction-character-memory-agent
stars: 0
url: https://github.com/jennyhuang17/fiction-character-memory-agent
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

# jennyhuang17/fiction-character-memory-agent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jennyhuang17/fiction-character-memory-agent
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：An Information Retrieval assignment project using local character memory, TF-IDF search, and an LLM for context-grounded answers.
- **本地描述**：An Information Retrieval assignment project using local character memory, TF-IDF search, and an LLM for context-grounded answers.
- **拉取时间**：2026-07-23 23:06:22

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Fiction Character Memory Agent

This project is a small Information Retrieval agent for fiction writing. It stores fictional character facts in local JSON memory, retrieves relevant facts with TF-IDF, and uses an LLM to answer questions or check whether a fact belongs to a character.

The example data is synthetic and original. It is only for demonstrating the assignment idea.

## Why This Is an AI Agent

The system has a simple agent loop:

1. It stores and updates local memory.
2. It retrieves relevant context from memory.
3. It sends retrieved context to an LLM.
4. It answers or checks consistency based only on that context.

The agent can perform actions through separate skill files: adding memory, loading memory, searching memory, and checking consistency.

## Information Retrieval Component

The IR component uses TF-IDF retrieval from `scikit-learn`.

For search, ask, and check commands, the system:

1. Loads records from `data/character_memory.json`.
2. Builds searchable text from each character name and fact.
3. Converts the records and query into TF-IDF vectors.
4. Computes cosine similarity.
5. Returns the top relevant memory records.

This gives the LLM better context than the question alone.

Tags are stored as readable metadata, but they are not currently used in TF-IDF retrieval. This avoids a problem where shared tags could make unrelated facts about the same character look more relevant than they really are.

## Local Memory

The main memory file is:

```bash
data/character_memory.json
```

If this file is missing or empty, the agent initializes it from:

```bash
data/toy_characters.json
```

Each memory record stores:

- `id`
- `character`
- `fact`
- `tags`
- `source`
- `timestamp`

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example` as a guide:

```bash
BERGET_API_KEY=your_api_key_here
```

Do not commit your real `.env` file.

The LLM call uses Berget AI through the OpenAI-compatible `openai` Python client.

## Quick Start

Run these commands in order to test the main workflow:

```bash
python agent.py list
python agent.py search "fears responsibility"
python agent.py ask "Which character avoids making promises?"
python agent.py check --character "Milo Vale" --fact "avoids making promises"
```

## Example Commands

Initialize or inspect toy memory:

```bash
python agent.py list
```

Add a new character fact:

```bash
python agent.py add --character "Lena Frost" --fact "Lena refuses shortcuts through frozen tunnels."
```

Search stored memory:

```bash
python agent.py search "fears responsibility"
```

Ask a question over stored memory:

```bash
python agent.py ask "Which character avoids making promises?"
```

Check whether a fact belongs to a character:

```bash
python agent.py check --character "Milo Vale" --fact "avoids making promises"
```

## Expected Outputs

The `search` command prints:

- matched character
- fact
- similarity score
- source

Example:

```text
Character: Lena Frost
Fact: Lena avoids making promises because she fears responsibility.
Similarity score: 0.529
Source: toy_characters
```

The `ask` command retrieves relevant facts, sends them to the LLM, and prints an answer plus the retrieved memory used.

The `check` command retrieves relevant facts and asks the LLM to explain whether the proposed fact belongs to the given character or appears to belong to another character.

## Demo and Report

- Demo video: [demo.mp4](https://github.com/jennyhuang17/fiction-character-memory-agent/blob/main/demo.mp4)
- Short report: [report.pdf](https://github.com/jennyhuang17/fiction-character-memory-agent/blob/main/report.pdf)

## Project Structure

```text
.
├── agent.py
├── soul.md
├── .env.example
├── requirements.txt
├── README.md
├── data/
│   ├── character_memory.json
│   └── toy_characters.json
└── skills/
    ├── add_memory.py
    ├── load_memory.py
    ├── search_memory.py
    └── check_consistency.py
```

## Limitations and Future Work

- TF-IDF is simple and transparent, but it does not understand meaning as deeply as embeddings.
- The memory is a local JSON file, not a database.
- The project uses a small synthetic toy dataset.
- Users could add tags as extra metadata in a future version.
