---
id: tool-00882
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: Prompt2Chart
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/kamleshpa/prompt2chart
created: 2026-07-18
updated: 2026-07-18
no: 882
category: 二、网文 / 长篇 AI 写作系统 库
repo: Kamleshpa/Prompt2Chart
stars: 0
url: https://github.com/kamleshpa/prompt2chart
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Kamleshpa/Prompt2Chart

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/kamleshpa/prompt2chart
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Prompt2Chart is an AI-native analytics dashboard that converts natural-language questions into SQL, runs them on tabular data, and returns precise answers or interactive charts in seconds. Pin, move, resize, and personalize widgets to build live dashboards without writing queries manually.
- **本地描述**：Prompt2Chart is an AI-native analytics dashboard that converts natural-language questions into SQL, runs them on tabular data, and returns precise answers or interactive charts in seconds. Pin, move, resize, and personalize widgets to build live dashboards without writing queries manually.
- **拉取时间**：2026-07-23 23:04:45

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Dashboard (LLM + SQL + CSV)

Chat-based analytics dashboard where users ask questions in natural language, the app generates SQL, runs it on CSV data using DuckDB, and renders charts with Apache ECharts.

## Demo

### Chat to Chart and Pin
![Chat to Chart and Pin](docs/demo-chat-to-chart-and-pin.gif)

### Dataset Switching
![Dataset Switching](docs/demo-dataset-switch.gif)

## What You Get

- Natural language analytics via chat
- SQL-first query execution on CSV (`DuckDB` in memory)
- Multi-dataset support (switch between CSV files)
- Optional LLM planner + automatic SQL repair
- Chart pinning to dashboard
- Remove, drag, and resize pinned widgets
- Persistent widget layouts and saved pins
- Query/debug logs in `logs/app.log`

## Quick Start (Fork-and-Run)

### 1) Clone and enter project

```bash
git clone <your-fork-url>
cd ai_dashboard
```

### 2) Create virtual env and install dependencies

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

### 3) Configure environment (optional for LLM mode)

```bash
cp .env.example .env
```

Set values in `.env` (or export in shell):

```bash
export OPENAI_API_KEY="your_openai_api_key"
export OPENAI_MODEL="gpt-4o-mini"
export PORT=8001
```

If `OPENAI_API_KEY` is not set, app still works with deterministic fallback planning.

### 4) Run the app

```bash
.venv/bin/python server.py
```

Open: `http://127.0.0.1:8001`

## Example Questions

- `Show me monthly trend of ticket sales in last 12 months`
- `Which airline had the most sales?`
- `What is the average number of days between purchase date and travel date?`
- `Top 5 destination cities by number of tickets sold`
- `Show me trend of unique customers over time`

## Add Your Own Dataset

1. Put CSV into `data/` (example: `data/my_dataset.csv`)
2. (Recommended) Add schema metadata file:
   - `data/schema_descriptions/my_dataset.schema.json`
3. Switch dataset from UI dropdown

### Schema description format

```json
{
  "columns": {
    "column_name": {
      "description": "10-15 word plain language description",
      "semantic_tags": ["business", "meaning", "keywords"]
    }
  }
}
```

## Dashboard Widget Controls

On pinned widgets:

- **Drag** handle to move widget
- Bottom-right corner to resize
- **Remove** button to delete widget

All layout updates are persisted.

## Logs and Debugging

Logs are written to:

- terminal stdout
- `logs/app.log`

Each chat request logs:

- user prompt and dataset
- planner source (`llm`, `llm_repaired`, `fallback`)
- SQL validation/repair status
- LLM debug payload
- executed SQL
- execution time and row count

## Project Structure

- `server.py` - HTTP server and API routes
- `src/llm.py` - LLM planning and SQL repair
- `src/mcp_server.py` - SQL execution engine over CSV (DuckDB)
- `src/storage.py` - SQLite persistence for pins/layout
- `web/index.html` - UI shell
- `web/static/app.js` - chat, chart rendering, pin/layout actions
- `web/static/styles.css` - UI styles
- `data/` - CSV datasets and schema descriptions
- `logs/` - runtime logs

## Tech Stack

- Backend: Python (standard library HTTP server)
- Query engine: DuckDB
- Frontend charts: Apache ECharts ([docs](https://echarts.apache.org/en/index.html))
- Storage: SQLite

## Notes for GitHub Users

- `.gitignore` excludes local runtime files (`.venv`, logs, local DB).
- Sample CSV datasets are included for quick testing.
- You can safely fork and run without API key (fallback mode).

## Legal and Governance

- License: `MIT` (see `LICENSE`)
- Contribution guide: `CONTRIBUTING.md`
- Security reporting process: `SECURITY.md`
- Third-party dependencies retain their own licenses; review upstream terms before production distribution.

