---
id: tool-04378
type: tool
area: 库
status: active
tags: [JavaScript, 协议传染, 本地优先, 英文文档, 人物设定, RAG, 本地写作]
title: Vessel
summary: 长篇人物/设定/伏笔一致性（RAG 记忆库）
source: https://github.com/pratikkothari34/vessel
created: 2026-07-18
updated: 2026-07-18
no: 4378
category: 四、长篇一致性 / RAG / 故事圣经 库
repo: PratikKothari34/Vessel
stars: 1
url: https://github.com/pratikkothari34/vessel
tier: "B"
use_case: "长篇人物/设定/伏笔一致性（RAG 记忆库）"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/人物思维蒸馏法.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: ea62ec1734393692
  - methods/模板库.md
---

# PratikKothari34/Vessel

- **分类**：四、长篇一致性 / RAG / 故事圣经 库
- **链接**：https://github.com/pratikkothari34/vessel
- **Stars**：1
- **语言**：JavaScript
- **License**：GPL-3.0
- **Topics**：ai-chat, electron, llm, local-first, ollama, privacy, react, roleplay, turso, windows
- **GitHub 描述**：Uncensored character.ai-style roleplay desktop app that runs 100% locally via Ollama. Long-term memory, multi-character personas, optional encrypted cloud sync.
- **本地描述**：Uncensored character.ai-style roleplay desktop app that runs 100% locally via Ollama. Long-term memory, multi-character personas, optional encrypted cloud sync.
- **拉取时间**：2026-07-25 17:45:05

---

# Vessel

A local, private, **uncensored** character.ai-style roleplay desktop app for Windows.
Multiple characters, each with its own persona; long-term memory that survives the
model's context window; everything runs on your machine via [Ollama](https://ollama.com).
Optional encrypted cloud backup + multi-device sync via [Turso](https://turso.tech).

- **Local LLM** — no external API, no content filtering. Built on the Natsumura
  storytelling/roleplay model.
- **Multi-character** — create personas (name, persona, greeting, avatar, sampling),
  switch between them like character.ai.
- **Long-term memory** — small fast live window + rolling summary + embedding-based
  retrieval, so long stories stay coherent without slowing down.
- **Swipe variants** — regenerate a reply to get alternates; swipe `◀ 2/3 ▶`
  between them. All variants persist; the one you pick becomes canonical for memory.
- **Director / OOC mode** — steer the AI with out-of-character instructions
  (e.g. "focus on dialogue, less narration") via the ◈ toggle or a `//` prefix.
  Director notes guide behavior but are never written into the story or memory.
- **Response style** — per-character setting (balanced / dialogue-first /
  light-narration) to stop the model from only narrating instead of speaking.
- **Local-first storage** — SQLite (Turso) on disk; cloud sync is opt-in.

---

## Architecture

```
Electron main ──spawns──> Node/Express backend (127.0.0.1) ──HTTP──> Ollama
     │                          │
  React renderer           Turso (@tursodatabase/sync)  (local file; optional cloud sync)
  (Vite)                   characters / conversations / turns / archive(+embeddings)
```

The model's live window is kept small (32K) for speed. Older turns are folded into
a **rolling summary** (gemma3:4b) and **archived with embeddings** (nomic-embed-text);
relevant ones are recalled per message by cosine-ranking the stored embeddings in
JS (the Turso sync engine has no native vector search).

---

## Prerequisites

1. **Node.js 18+**
2. **Ollama** running locally, with three models:
   ```bash
   ollama pull Tohur/natsumura-storytelling-rp-llama-3.1:8b
   ollama pull gemma3:4b
   ollama pull nomic-embed-text
   ```
3. **The custom chat model** (built from the included `Modelfile`):
   ```bash
   ollama create vessel -f Modelfile
   ```

---

## Run (development)

```bash
# 1. backend deps (repo root)
npm install

# 2. app deps
cd app && npm install

# 3. (optional) config — copy and edit if you want cloud sync or different tuning
cp ../.env.example ../.env

# 4. launch (starts backend + Electron window)
npm run dev
```

The app spawns the backend automatically and waits for it to be healthy before
showing the window.

> **Note:** if `ELECTRON_RUN_AS_NODE=1` is set in your shell, the dev launcher
> (`app/scripts/dev.mjs`) clears it for the app process — otherwise Electron would
> run headless as plain Node.

---

## Configuration (`.env`)

All optional — sane defaults work for a local-only setup. See `.env.example` for the
full list. Key ones:

| Variable | Default | Purpose |
|---|---|---|
| `OLLAMA_MODEL` | `vessel` | Chat model |
| `SUMMARIZER_MODEL` | `gemma3:4b` | Rolling-summary model |
| `EMBED_MODEL` | `nomic-embed-text` | Embedding model (768-dim) |
| `LOCAL_DB_PATH` | `./data/scenario.db` | Local SQLite file |
| `TURSO_DATABASE_URL` | *(blank)* | Set to enable cloud sync |
| `TURSO_AUTH_TOKEN` | *(blank)* | Turso auth token |
| `VERBATIM_TURNS` | `8` | Recent turns kept verbatim |
| `SUMMARIZE_THRESHOLD` | `12` | When to archive old turns |
| `RETRIEVE_K` | `4` | Max recalled turns per message |

### Cloud sync (optional)

Local-first with offline writes — the app always works offline; the cloud is a
backup/mirror you can restore from or read on another machine. Every user brings
their **own** Turso database; no credentials ship with the app.

1. Create a Turso DB: `turso db create vessel`
2. Get the URL + token:
   ```bash
   turso db show vessel --url
   turso db tokens create vessel
   ```
3. In the app: **Settings → Cloud sync**, paste the URL + token, save, restart.
   The URL is persisted to `data/settings.json`; the token goes to the OS
   keychain (never written to disk). Dev alternative: `TURSO_DATABASE_URL` /
   `TURSO_AUTH_TOKEN` in `.env` — in-app values override `.env`.

The schema is created on both local and remote (retrieval is in-JS cosine — the
sync engine has no native vector index).

> **Storage tip:** keep `LOCAL_DB_PATH` **outside** a OneDrive/Dropbox-synced
> folder — file-syncers can lock the SQLite file mid-write.

---

## Install (Windows)

Grab the latest `Vessel Setup *.exe` from the
[Releases](https://github.com/PratikKothari34/Vessel/blob/main/../../releases) page and run it (one-click, per-user install).
You still need **Ollama + the three models** (see Prerequisites) on the machine.
Your data lives in `%APPDATA%/Vessel/data/` and survives updates.

### Or build the installer yourself

```bash
cd app
npm run package      # -> app/dist/*.exe (NSIS installer)
```

The backend (`src/`, `node_modules`, `Modelfile`) is bundled into the app's
resources. The installed app still requires **Ollama + the models** on the target
machine.

---

## Project layout

```
Vessel/
├── Modelfile               # ollama create vessel -f Modelfile
├── .env.example
├── src/backend/
│   ├── server.js           # Express + SSE /chat + REST
│   ├── db.js               # Turso sync client + schema + embedding codec
│   ├── memory.js           # summary + retrieval engine
│   └── characters.js       # character CRUD
└── app/                    # Electron + React (Vite)
    └── src/
        ├── main/           # spawns backend, creates window
        ├── preload/
        └── renderer/src/   # React UI (Gallery, Chat, Editor, Settings, Memory)
```

---

## Privacy

Everything is local by default: the LLM, the database, the conversations. No
telemetry, no external calls except to your own Ollama instance. Cloud sync is
strictly opt-in and only activates when you provide Turso credentials.

related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---

## License

[GPL-3.0](https://github.com/PratikKothari34/Vessel/blob/main/LICENSE) — free to use, modify, and redistribute; derivatives must
stay under the same license.
