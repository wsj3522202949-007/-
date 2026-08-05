---
id: tool-00928
type: tool
area: 库
status: active
tags: [RAG, 多Agent, Python, 协议未明, 本地优先, 英文文档, 人物设定, 本地写作]
title: auto-ops
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/raj1401/auto-ops
created: 2026-07-18
updated: 2026-07-18
no: 928
category: 二、网文 / 长篇 AI 写作系统 库
repo: raj1401/auto-ops
stars: 1
url: https://github.com/raj1401/auto-ops
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# raj1401/auto-ops

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/raj1401/auto-ops
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Auto-Ops is an agentic automation backend for lead research, outreach writing, and email drafting, designed for B2B workflows. 
- **本地描述**：Auto-Ops is an agentic automation backend for lead research, outreach writing, and email drafting, designed for B2B workflows.
- **拉取时间**：2026-07-23 23:06:08

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Auto-Ops

!`[Auto-Ops Multi-Agent Workflow](assets/auto-ops-diagram.png)`

Auto-Ops is an agentic automation backend for lead research, outreach writing, and email drafting, designed for B2B workflows. It leverages FastAPI to expose endpoints for running specialized agents and managing a TinyDB-based email database. The system is extensible and integrates with vector stores for document indexing and retrieval. The frontend written in React + TypeScript is available [here](https://github.com/raj1401/autoops-frontend).

!`[Auto-Ops Tech Stack](assets/auto-ops-tech.png)`

## Features

- **Lead Research**: Automates research on leads using the LeadResearcherAgent, returning a research brief and sources used.
- **Outreach Writing**: Generates outreach content based on a research brief using the OutreachWriterAgent.
- **Email Drafting**: Creates email drafts from outreach content using the EmailWriterAgent.
- **Database Management**: Stores and retrieves email-related data using TinyDB.
- **Document Indexing**: Indexes documents (e.g., `doc.txt`) into a vector store for agentic retrieval.

## API Endpoints

### 1. Lead Research

- **POST** `/lead-research`
- **Input**: JSON object with fields: `company`, `domain`, `industry`, `region`, `notes`
- **Output**: JSON with `brief` and `used_sources`

### 2. Outreach Writing

- **POST** `/outreach-write`
- **Input**: JSON object with a `brief` field (output from lead research)
- **Output**: JSON with outreach content

### 3. Email Writing

- **POST** `/email-write`
- **Input**: JSON object with an `outreach` field (output from outreach writing)
- **Output**: JSON with email draft result

### 4. Database Entries

- **GET** `/db-entries`
- **Output**: JSON list of all database entries

## Configuration

### Document Indexing

- The backend automatically indexes the contents of `doc.txt` into the vector store on startup. To change the indexed document, replace or edit `doc.txt` in the project root.

### Database Location

- The TinyDB database is stored in `autoops/email_database/emails.json`. You can change the path in `autoops/email_database/db.py` by modifying the `DB_PATH` variable.

### Agent Configuration

- Agent logic and configuration can be customized in the respective files under `autoops/agents/`.
- Vector store configuration is in `autoops/memory/vectorstore.py`.

## Starting the Backend

To start the FastAPI backend, run the following command from the project root:

```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Requirements

- Python 3.13+
- Install dependencies using [uv](https://github.com/astral-sh/uv) and your `pyproject.toml`/`uv.lock`:
  ```
  uv pip install --system
  ```
  This will install all dependencies specified in `pyproject.toml` and lock them according to `uv.lock`.

## Customization

- To allow CORS for additional frontend origins, edit the `allow_origins` list in `main.py`.
- To add new agents or endpoints, extend the FastAPI app in `main.py` and implement new agent classes in `autoops/agents/`.
