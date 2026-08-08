---
id: tool-01222
type: tool
area: 库
status: active
tags: [RAG, Python, 协议未明, 本地优先, 英文文档, 人物设定, 本地写作]
title: ai-writing-assistant-rag-mcp
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/jeanycyang/ai-writing-assistant-rag-mcp
created: 2026-07-18
updated: 2026-07-18
no: 1222
category: 二、网文 / 长篇 AI 写作系统 库
repo: jeanycyang/ai-writing-assistant-rag-mcp
stars: 0
url: https://github.com/jeanycyang/ai-writing-assistant-rag-mcp
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: ccc3dca864854453
  - methods/最强写作方法论_全球最强综合版.md
---

# jeanycyang/ai-writing-assistant-rag-mcp

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jeanycyang/ai-writing-assistant-rag-mcp
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：MCP tools for pgvector-backed RAG in AI writing workflows
- **本地描述**：MCP tools for pgvector-backed RAG in AI writing workflows
- **拉取时间**：2026-07-23 23:14:43

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Writing Assistance MCP RAG

A retrieval-augmented generation system for AI writing assistance.

## Architecture

- `postgres`: PostgreSQL with `pgvector` for structured summary embeddings and raw-text embeddings.
- `rag-api`: FastAPI retrieval service with vendor-neutral HTTP contracts.

## Preparation
- `scripts/ingest_data.py`: Local ingestion entry point for summary markdown and raw episode text.
- See [Ingest Data](#ingest-data)

## Usage

### For Local Client
- `services/codex_mcp/server.py`: MCP protocol handler used by the local STDIO server and the HTTP MCP endpoint.
- See [Codex Writing Workspace](#codex-writing-workspace)

### For Remote AI Services
- Run `make funnel-up` to start the Tailscale Funnel service. Then set up the MCP integration on your remote AI provider.
- See [Remote MCP Over HTTPS](#remote-mcp-over-https)

## Python Setup

Use the project virtual environment for every local Python command.

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
```

## Codex Writing Workspace

That workspace is intentionally documentation-only:

- `AGENTS.md`
- `PROMPTS.md`
- `.codex/config.toml`

It does not contain Python or shell launcher files, so Codex is less likely to inspect implementation code by accident during writing sessions.

The workspace MCP config starts the server from the parent repo.

### Remote MCP Over HTTPS

The preferred public transport is Tailscale Funnel in front of `rag-api`.

The existing `rag-api` service exposes MCP JSON-RPC over HTTP at:

- `POST /mcp`
- `POST /mcp/{work}`

With Funnel, the public MCP URL becomes:

```text
https://<device-name>.<tailnet>.ts.net/mcp
```

```bash
make funnel-up
make funnel-status
make funnel-url
make funnel-down
```

Default behavior:

- proxies to local `http://127.0.0.1:${RAG_API_PORT:-8001}`
- publishes it on Funnel HTTPS port `443`
- prints the fixed `*.ts.net` URL and the `/mcp` endpoint

Prerequisites:

- Tailscale is installed and logged in on this machine
- MagicDNS and HTTPS are enabled for the tailnet
- Funnel is allowed for the tailnet and this device
- `rag-api` is healthy on the local target port

Example initialize request:

```bash
curl -s https://<device-name>.<tailnet>.ts.net/mcp \
  -H 'content-type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"remote-client","version":"0.1.0"}}}'
```

## Ingest Data

TODO: Use different databases for different works. Support multiple works.

Current implementation direction:

- keep the default database on the existing endpoints
- named work endpoints reuse the same PostgreSQL server/credentials and only switch the database name
- `/mcp/work_id_1` uses the `work_id_1` database, `/mcp/work_id_2` uses the `work_id_2` database
- `AI_WRITING_WORK=work_id_1` binds the local STDIO MCP server to the `work_id_1` database
- use `POST /mcp/{work}` to bind MCP to one work database without exposing work selection to the model
- use `POST /works/{work}/...` retrieval endpoints for direct HTTP access
- use `python scripts/ingest_data.py --work <work>` to ingest into a named work database

Production rule:

- `data/sample` is test/demo data only
- do not use `data/sample` for production ingestion
- for production, always ingest from the real OCR roots explicitly, or set `.env` to those real OCR roots

If sample/demo records were already imported into PostgreSQL, remove them before production import:

```bash
source venv/bin/activate
python scripts/cleanup_sample_data.py
```

Or via `make`:

```bash
make cleanup-sample-data
```

```bash
source venv/bin/activate
python scripts/ingest_data.py --summary-dir data/sample/summaries --raw-dir data/sample/raw
python scripts/ingest_data.py --work sample --summary-dir data/sample/summaries --raw-dir data/sample/raw
```

The ingestion pipeline:

- parses structured summary markdown
- validates required fields
- builds retrieval-friendly `embedding_text`
- chunks raw text while preserving chapter and paragraph linkage
- computes embeddings with `sentence-transformers`
- upserts records by stable external IDs, with `source_hash` stored for inspection

Default embedding choice: `BAAI/bge-m3`. It is multilingual and practical for Traditional Chinese (Taiwan) text in a Mac-centric local setup. The embedding layer is abstracted so a different provider can be added later without changing the retrieval API.

Query embeddings are generated outside `rag-api`. The shared vectorized client is used by the local MCP server, so `rag-api` stays retrieval-only and does not depend on PyTorch.

## Testing

```bash
source venv/bin/activate
pytest
```

## Reset and Rebuild

```bash
docker compose down -v
docker compose up --build
```
