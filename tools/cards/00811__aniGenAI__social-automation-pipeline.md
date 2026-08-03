---
id: tool-00811
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议宽松, 需API密钥, 英文文档]
title: social-automation-pipeline
summary: 多 Agent 协作自动产文
source: https://github.com/anigenai/social-automation-pipeline
created: 2026-07-18
updated: 2026-07-18
no: 811
category: 二、网文 / 长篇 AI 写作系统 库
repo: aniGenAI/social-automation-pipeline
stars: 0
url: https://github.com/anigenai/social-automation-pipeline
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# aniGenAI/social-automation-pipeline

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/anigenai/social-automation-pipeline
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：langchain, langgraph, ollama, python
- **GitHub 描述**：AI-powered multi-agent content generation pipeline built with LangGraph, Ollama/Mistral, FastAPI, and Tavily — featuring web research, strategy generation, content writing, QA loops, and structured AI workflows.
- **本地描述**：AI-powered multi-agent content generation pipeline built with LangGraph, Ollama/Mistral, FastAPI, and Tavily — featuring web research, strategy generation, content writing, QA loops, and structured AI workflows.
- **拉取时间**：2026-07-23 23:02:41

---

# AI Content Pipeline Agent

An advanced multi-agent AI content generation system built using LangGraph, LangChain, Ollama/Mistral, and FastAPI.

This project demonstrates how to build a production-style AI workflow that can:

- Research topics using live web data
- Generate content strategies
- Write multi-platform content
- Perform AI-based QA review
- Retry and improve content automatically
- Expose workflows through APIs

---

# Features

## Multi-Agent Workflow

The system uses specialized AI agents for:

- Research
- Strategy
- Writing
- QA / Review

Each agent has a dedicated responsibility and communicates through shared graph state.

---

## LangGraph Orchestration

The workflow is orchestrated using LangGraph with:

- Stateful execution
- Conditional routing
- Retry loops
- Shared memory
- Dynamic graph execution

---

## Live Web Research

Integrated with Tavily for real-time web search and trend analysis.

Research agent can:
- Discover latest trends
- Analyze live search results
- Generate structured insights

---

## Structured Outputs

Uses Pydantic schemas for:

- Deterministic AI outputs
- JSON-safe responses
- Validation
- API-ready structures

---

## QA + Rewrite Loop

The QA agent:
- Reviews generated content
- Assigns quality scores
- Provides feedback
- Triggers rewrites automatically if quality is low

---

## FastAPI Backend

Exposes the workflow through REST APIs.

Includes:
- Swagger documentation
- Request validation
- Structured responses

---

# Tech Stack

## Core Frameworks

- LangGraph
- LangChain
- FastAPI
- Pydantic

---

## LLM Providers

Supports:

- Ollama
- Mistral AI

Architecture is provider-agnostic.

---

## Research Tools

- Tavily Search API

---

# Project Architecture

```text
Client
   ↓
FastAPI
   ↓
LangGraph Workflow
   ↓
Research Agent
   ↓
Strategy Agent
   ↓
Writer Agent
   ↓
QA Agent
   ↓
Conditional Retry Loop
```

---

# Workflow Diagram

```text
START
   │
   ▼
research
   │
   ▼
strategy
   │
   ▼
writer
   │
   ▼
qa
   │
 ┌─┴──────────┐
 ▼            ▼
END        rewrite
```

---

# Project Structure

```text
backend/
│
├── agents/
│   ├── research.py
│   ├── strategy.py
│   ├── writer.py
│   └── qa.py
│
├── api/
│   └── models.py
│
├── graph/
│   ├── state.py
│   └── workflow.py
│
├── schemas/
│   └── content.py
│
├── tools/
│   └── search.py
│
├── llm.py
├── main.py
├── requirements.txt
└── .env
```

---

# Installation

## 1. Clone Repository

```bash
git clone <repository_url>
cd backend
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

## Install Ollama

Download from:

https://ollama.com/download

---

## Pull Model

Recommended:

```bash
ollama pull llama3.1:8b
```

Better structured output model:

```bash
ollama pull qwen2.5:14b
```

---

## Start Ollama

```bash
ollama serve
```

---

# Environment Variables

Create a `.env` file:

```env
LLM_PROVIDER=ollama

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen2.5:14b

MISTRAL_API_KEY=your_mistral_key
MISTRAL_MODEL=mistral-large-latest

TAVILY_API_KEY=your_tavily_api_key
```

---

# Running the API

Start FastAPI server:

```bash
uvicorn main:api --reload
```

API will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# API Example

## POST `/generate-content`

### Request

```json
{
  "topic": "AI Agents in 2026",
  "audience": "AI engineers",
  "tone": "professional",
  "goal": "thought leadership",
  "formats": ["blog", "linkedin", "twitter"]
}
```

---

### Response

```json
{
  "status": "qa_passed",
  "qa_score": 8.7,
  "approved": true,
  "research": {},
  "strategy": {},
  "draft": {
    "blog": "...",
    "linkedin": "...",
    "twitter": "..."
  }
}
```

---

# Agent Responsibilities

## Research Agent

Responsible for:
- Web research
- Trends
- Pain points
- Opportunities

---

## Strategy Agent

Responsible for:
- Content angle
- Positioning
- Outline
- CTA strategy

---

## Writer Agent

Responsible for:
- Blog generation
- LinkedIn posts
- Twitter/X threads

---

## QA Agent

Responsible for:
- Content review
- Quality scoring
- Rewrite feedback
- Approval decisions

---

# Future Enhancements

Planned upgrades:

- Persistent database memory
- Human-in-the-loop approval
- Streaming responses
- Async execution
- Firecrawl scraping
- Multi-model routing
- Redis/PostgreSQL checkpointing
- Social media publishing
- Analytics feedback loop
- Vector database integration
- RAG knowledge base

---

# Recommended Models

| Use Case | Recommended Model |
|---|---|
| Local Development | llama3.1:8b |
| Structured Output | qwen2.5:14b |
| Production Writing | mistral-large |
| Fast QA | llama3.1 |

---

# Production Recommendations

For production deployments:

- Use PostgreSQL checkpointing
- Add Redis caching
- Enable async execution
- Add request logging
- Add observability/tracing
- Add rate limiting
- Add authentication

---

# License

MIT License

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Author

Built using:
- LangGraph
- LangChain
- Ollama
- FastAPI
- Pydantic
