---
id: tool-00168
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: multi_capability_ai_assistant
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/afrozghauri/multi_capability_ai_assistant
created: 2026-07-18
updated: 2026-07-18
no: 168
category: 二、网文 / 长篇 AI 写作系统 库
repo: afrozghauri/multi_capability_ai_assistant
stars: 0
url: https://github.com/afrozghauri/multi_capability_ai_assistant
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 5699bf5eab3a66a1
  - methods/最强写作方法论_全球最强综合版.md
---

# afrozghauri/multi_capability_ai_assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/afrozghauri/multi_capability_ai_assistant
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A Python-based AI assistant with email writing, text summarization, and chat capabilities, powered by OpenAI and real-world tools.
- **本地描述**：A Python-based AI assistant with email writing, text summarization, and chat capabilities, powered by OpenAI and real-world tools.
- **拉取时间**：2026-07-23 22:43:55

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Multi-Capability AI Assistant

A Python-based AI assistant that combines three capabilities and four tools to handle a variety of requests intelligently.

## Capabilities

- **Email Writer**: Writes complete emails with subject lines. Supports formal, friendly, and casual tones. Automatically researches topics using news before writing when relevant.
- **Smart Summarizer**: Summarizes any text into 1-5 sentences depending on length preference. Shows original word count, summary word count, and reduction percentage.
- **Chat Assistant**: General-purpose conversational assistant with memory. Remembers previous exchanges within a session and can answer follow-up questions.

## Tools

- **Calculator**: Evaluates mathematical expressions including advanced functions like sqrt, sin, cos.
- **Web Search**: Searches the web using DuckDuckGo and returns real results.
- **Data Analyzer**: Accepts a list of numbers and returns count, sum, average, min, and max.
- **News Fetcher**: Fetches the latest real news headlines on any topic using NewsAPI.

## Installation

1. Clone the repository
2. Create and activate a virtual environment:
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
    pip install -r requirements.txt
```
4. Copy `.env.example` to `.env` and add your API keys:
```bash
    cp .env.example .env
```

## Configuration

Get your API keys from:
- OpenAI: https://platform.openai.com
- NewsAPI: https://newsapi.org

## Usage

```bash
python assistant.py
```

## Example Interactions

**Email Writer:**
You: write a formal email about requesting sick leave
**Summarizer:**
You: summarize: [paste any text here]
You: write a short summary of: [paste any text here]
**Chat:**
You: what is a quantum computer?
You: how does that compare to a regular computer?

**Tools via Chat:**
You: what is sqrt(256) + 100?
You: analyze this data: 5, 10, 15, 20, 25
You: get me the latest news about climate change
You: search the web for machine learning tutorials

## Commands

- `help` — show available capabilities and tools
- `quit` / `exit` / `bye` — exit the assistant
