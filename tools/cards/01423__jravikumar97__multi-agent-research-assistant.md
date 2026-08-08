---
id: tool-01423
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议未明, 需API密钥, 英文文档]
title: multi-agent-research-assistant
summary: 多 Agent 协作自动产文
source: https://github.com/jravikumar97/multi-agent-research-assistant
created: 2026-07-18
updated: 2026-07-18
no: 1423
category: 二、网文 / 长篇 AI 写作系统 库
repo: jravikumar97/multi-agent-research-assistant
stars: 0
url: https://github.com/jravikumar97/multi-agent-research-assistant
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: b6e5d7594af1a407
  - methods/最强写作方法论_全球最强综合版.md
---

# jravikumar97/multi-agent-research-assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jravikumar97/multi-agent-research-assistant
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered multi-agent system designed to automate research tasks. The system leverages advanced NLP models and integrated tools to gather, structure, and save research data. It includes specialized agents for research, writing, and saving, orchestrated seamlessly to enhance the research process.
- **本地描述**：AI-powered multi-agent system designed to automate research tasks. The system leverages advanced NLP models and integrated tools to gather, structure, and save research data. It includes specialized agents for research, writing, and saving, orchestrated seamlessly to enhance the research process.
- **拉取时间**：2026-07-23 23:20:35

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Research AI Multi-Agent System

A multi-agent system that helps with research tasks by breaking down the process into three specialized agents: research, writing, and saving.

## Overview

This project implements a research assistant that uses multiple AI agents to:
1. Research a topic using various tools
2. Structure and format the research findings
3. Save the results to a file

## Components

### Agents

1. **Research Agent**
   - Uses search and Wikipedia tools to gather information
   - Collects facts and data about the specified topic

2. **Writer Agent**
   - Takes the raw research and structures it into a clear format
   - Creates a comprehensive summary with sources and tools used

3. **Save Agent**
   - Handles saving the final output to a file
   - Manages file operations and storage

### Tools

- Search Tool: Performs web searches for information
- Wikipedia Tool: Accesses Wikipedia articles
- Save Tool: Handles file operations

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd research-AI-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your Anthropic API key:
```
ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

Run the main script:
```bash
python main.py
```

When prompted, enter your research query. The system will:
1. Research the topic using available tools
2. Structure and format the findings
3. Save the results to a file

## Project Structure

```
research-AI-agent/
├── agents/
│   ├── research_agent.py
│   ├── writer_agent.py
│   └── save_agent.py
├── tools/
│   ├── search_tool.py
│   ├── wiki_tool.py
│   └── save_tool.py
├── models/
│   └── research_output.py
├── main.py
├── config.py
├── requirements.txt
└── .env
```

## Dependencies

- langchain
- langchain-anthropic
- anthropic
- python-dotenv
- pydantic
- duckduckgo-search# multi-agent-research-assistant
