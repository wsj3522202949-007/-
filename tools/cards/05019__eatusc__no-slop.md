---
id: tool-05019
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: no-slop
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/eatusc/no-slop
created: 2026-07-18
updated: 2026-07-18
no: 5019
category: 一、去 AI 味 / Humanizer 库
repo: eatusc/no-slop
stars: 1
url: https://github.com/eatusc/no-slop
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# eatusc/no-slop

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/eatusc/no-slop
- **Stars**：1
- **语言**：JavaScript
- **License**：MIT
- **Topics**：ai, ai-writing-detector, cli, developer-tools, django, django-rest-framework, javascript, local-first, mcp, mcp-server, model-context-protocol, nlp, python, rest-api, text-processing, vite, writing-tools
- **GitHub 描述**：Local-first AI writing detector and cleanup engine with REST APIs, CLI, Django/DRF, and native MCP tools.
- **本地描述**：Local-first AI writing detector and cleanup engine with REST APIs, CLI, Django/DRF, and native MCP tools.
- **拉取时间**：2026-07-25 18:03:08

---

# No Slop

[![CI](https://github.com/eatusc/no-slop/actions/workflows/ci.yml/badge.svg)](https://github.com/eatusc/no-slop/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Local-first AI writing cleanup for humans and agents. No Slop detects common
LLM-writing patterns, rewrites safe mechanical issues, scores the input, and
flags structural problems that need human judgment.

The same deterministic text engine powers a browser UI, seven local API route
families, a command-line tool, and a native Model Context Protocol (MCP) server.
A Django REST Framework port provides the same core response contract for a
Python backend.

![No Slop cleaning a sample of AI text: the Slopometer scores it 100/100 and the diff view shows 16 fixes](https://github.com/eatusc/no-slop/blob/main/docs/media/hero.png)

## Why it is useful

- **Deterministic cleanup:** remove em-dash overload, decorative emoji, filler
  openers, throat-clearing transitions, hype phrases, and inflated vocabulary.
- **AI-writing detection:** produce a 0-100 score with a signal breakdown.
- **Human-in-the-loop review:** flag risky structural patterns instead of
  pretending every rewrite can be safely automated.
- **Agent integration:** expose `deslop` and `slop_score` as native MCP tools.
- **Multiple interfaces, one engine:** browser, REST-style API, CLI, and MCP all
  call [`src/deslop.js`](https://github.com/eatusc/no-slop/blob/main/src/deslop.js).
- **Local by default:** the server binds to `127.0.0.1`; the deterministic engine
  does not require a hosted service or API key.

## Architecture

| Surface | Technology | Purpose |
|---|---|---|
| Web application | Vite + vanilla JavaScript | Live cleanup, diff, scoring, examples, and voice rules |
| Local API | Node/Vite middleware | Text cleanup, AI rewrite orchestration, style learning, examples, and editable docs |
| MCP server | Model Context Protocol over stdio | Native tools for Claude Code, Claude Desktop, Cursor, and other MCP clients |
| CLI | Node.js | Shell pipelines, files, clipboard workflows, and automation |
| Python API | Django + Django REST Framework | Alternative backend with validation, throttling, CORS controls, and 18 tests |
| Core engine | Dependency-free JavaScript | Shared cleanup, scoring, and structural flag detection |

```text
Browser UI ─┐
Local API ──┼──> src/deslop.js <── CLI
MCP server ─┘          │
                      └── deterministic cleanup + score + flags

Django/DRF API ──> Python port with the same response contract
```

## Quick start

Requires Node.js 20 or newer.

```bash
git clone https://github.com/eatusc/no-slop.git
cd no-slop
npm install
npm run dev
```

Open [http://localhost:4242](http://localhost:4242).

## HTTP API

The main integration endpoint accepts raw text or JSON:

```bash
curl -s -X POST http://localhost:4242/api/deslop \
  -H "Content-Type: application/json" \
  -d '{"text":"Furthermore, our seamless platform leverages cutting-edge AI. 🚀"}'
```

Example response:

```json
{
  "clean": "Our smooth platform uses advanced AI.",
  "slop": {
    "score": 100,
    "label": "Pure slop",
    "signals": {
      "transitions": 1,
      "emoji": 1,
      "words": 3
    }
  },
  "fixes": {
    "total": 5,
    "byCategory": [
      { "label": "Emoji", "count": 1 },
      { "label": "Throat-clearing transitions", "count": 1 },
      { "label": "Inflated words", "count": 3 }
    ]
  },
  "flags": [],
  "words": {
    "in": 8,
    "out": 6
  }
}
```

Return only clean text for shell pipelines:

```bash
curl -s -X POST "http://localhost:4242/api/deslop?clean=1" \
  --data-binary @draft.md > draft.clean.md
```

The application also has local routes for AI-assisted rewrites, learned style
examples, rule consolidation, the example corpus, and editable documentation.
See the complete route and security reference in [`API.md`](https://github.com/eatusc/no-slop/blob/main/API.md).

## Native MCP server

No HTTP server is required for MCP. The stdio server imports the core engine
directly and exposes two tools:

| Tool | Input | Result |
|---|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| `deslop` | `{ "text": "..." }` | Clean text, score, fixes, flags, and a JSON report |
| `slop_score` | `{ "text": "..." }` | Score and label without rewriting |

Register it with Claude Code:

```bash
claude mcp add -s user noslop -- node /ABSOLUTE/PATH/no-slop/mcp/server.mjs
```

Claude Desktop or Cursor configuration:

```json
{
  "mcpServers": {
    "noslop": {
      "command": "node",
      "args": ["/ABSOLUTE/PATH/no-slop/mcp/server.mjs"]
    }
  }
}
```

Test the full MCP client/server exchange:

```bash
npm run test:mcp
```

See [`mcp/README.md`](https://github.com/eatusc/no-slop/blob/main/mcp/README.md) for details.

## CLI

The CLI works without a server:

```bash
echo "We leverage a robust solution." | npm run deslop -- --report
node cli/deslop.mjs draft.md > draft.clean.md
node cli/deslop.mjs --json < draft.md
```

Example macOS clipboard workflow:

```bash
pbpaste | node cli/deslop.mjs | pbcopy
```

## Local AI rewrite and voice learning

The deterministic engine handles changes that are safe to automate. For heavier
rewrites, `POST /api/rewrite` orchestrates a locally installed Claude or Codex
CLI. How the pipeline works:

- **Your CLI login, no API keys.** The server spawns `claude -p` or
  `codex exec` as subprocesses and rides whatever authentication those tools
  already have. It never accepts, stores, or forwards a hosted API key. Codex
  runs in a read-only sandbox with an ephemeral session; both engines get a
  hard 180-second timeout with stdin closed.
- **Few-shot retrieval without dependencies.** Every time you accept a rewrite
  you like (or hand-edit one), the before/after pair is saved locally via
  `POST /api/style`. On the next rewrite, the server tokenizes the input,
  builds term-frequency vectors, and ranks all learned pairs by lexical cosine
  similarity (with a stopword list, no embeddings, no libraries), then packs
  the seed examples plus the top 8 most relevant learned pairs into the system
  prompt. The style bank scales to hundreds of examples without bloating the
  prompt.
- **Consolidate voice.** Once you have at least 3 saved edits,
  `POST /api/consolidate` sends the whole before/after corpus back through the
  Claude CLI and asks it to distill 8-15 concrete imperative rules from your
  actual editing patterns. The result is written into a marker-bounded section
  of [`voice.md`](https://github.com/eatusc/no-slop/blob/main/voice.md) (`<!-- LEARNED:START -->` to
  `<!-- LEARNED:END -->`) with an atomic tmp-file rename, so repeated
  consolidations replace only that section and the hand-written voice guide
  around it is never touched.
- **Prompt hygiene.** The system prompt sends a distilled "tells to avoid"
  list instead of the full word-swap table (which pushes models toward literal
  substitution instead of rewriting), and strips the quoted example sentences
  from `voice.md` so the model cannot parrot them as openers.

The associated route families are:

- `POST /api/rewrite`
- `GET`, `POST`, and `DELETE /api/style`
- `POST /api/consolidate`
- `GET /api/examples` and `POST /api/examples/dismiss`
- `GET` and `POST /api/doc/{rules|voice|api}`

Personal learned examples are gitignored. AI rewrite routes require a locally
installed and authenticated CLI; the deterministic engine, API, CLI, and MCP
tools do not.

## Django REST Framework implementation

[`django_api/`](https://github.com/eatusc/no-slop/tree/main/django_api/) ports the engine and API contract to Python,
Django, and Django REST Framework. It includes:

- JSON and `text/plain` request parsing
- request validation and a 4 MB limit
- local-development CORS controls
- anonymous rate limiting
- 18 endpoint, regression, throttling, and parity tests

```bash
cd django_api
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py test deslop
python manage.py runserver 127.0.0.1:8420
```

Parity between the JavaScript and Python engines is enforced in CI:
[`scripts/parity-check.mjs`](https://github.com/eatusc/no-slop/tree/main/scripts/parity-check.mjs) runs both engines over
shared fixtures plus the full example corpus and fails on any output
difference. See [`django_api/README.md`](https://github.com/eatusc/no-slop/blob/main/django_api/README.md) for
implementation notes.

## Development and validation

```bash
npm run build       # production Vite build
npm test            # Node engine regression tests
npm run test:mcp    # real MCP stdio client/server smoke test
npm run test:parity # diff Node and Python engine output on shared fixtures
npm run check       # all Node checks
```

CI runs the Node build, engine tests, MCP smoke test, cross-engine parity
check, and Django test suite on every push and pull request to `main`.

## Security model

The local server can invoke installed AI CLIs and update local style/doc files,
so it intentionally binds only to loopback. API requests with a non-localhost
browser `Origin` are rejected. Do not reverse-proxy or expose port 4242 to a
network without adding authentication and authorization.

See [`SECURITY.md`](https://github.com/eatusc/no-slop/blob/main/SECURITY.md) for reporting and deployment guidance.

## License

Code is available under the [MIT License](https://github.com/eatusc/no-slop/blob/main/LICENSE). Example captions are sample
content. Third-party essay text is not included; the long-form writing rules are
general writing guidance.
