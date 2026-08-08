---
id: tool-04339
type: tool
area: 库
status: active
tags: [互动叙事, Python, 协议未明, 需API密钥, 英文文档]
title: Discord_CharacterCreator_Bot
summary: 互动叙事/聊天写故事
source: https://github.com/kevmill29/discord_charactercreator_bot
created: 2026-07-18
updated: 2026-07-18
no: 4339
category: 四、长篇一致性 / RAG / 故事圣经 库
repo: kevmill29/Discord_CharacterCreator_Bot
stars: 0
url: https://github.com/kevmill29/discord_charactercreator_bot
tier: "C"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/人物思维蒸馏法.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 53251e39f34be61c
  - methods/模板库.md
---

# kevmill29/Discord_CharacterCreator_Bot

- **分类**：四、长篇一致性 / RAG / 故事圣经 库
- **链接**：https://github.com/kevmill29/discord_charactercreator_bot
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Self-hosted Discord roleplay bot that spawns AI character chatbots in dedicated threads — powered by a local LLM (Ollama), SQLite-backed memory, zero API costs.
- **本地描述**：Self-hosted Discord roleplay bot that spawns AI character chatbots in dedicated threads — powered by a local LLM (Ollama), SQLite-backed memory, zero API costs.
- **拉取时间**：2026-07-25 17:42:51

---

# Discobot

A Discord roleplay bot that spawns custom character chatbots in dedicated threads.
Each thread is an isolated, persistent conversation backed by SQLite and a
**local LLM** (Ollama by default — zero token cost). See `ARCHITECTURE.md` for the
full design.

## Prerequisites

1. **Python 3.11+**
2. **Ollama** running locally with the model pulled:
   ```
   ollama pull mistral-nemo:12b
   ```
3. **A Discord application** — https://discord.com/developers/applications
   - *Bot* tab → Add Bot → copy the token
   - Enable the **Message Content Intent** (Privileged Gateway Intents)
   - Invite URL scopes: `bot` + `applications.commands`; permissions:
     *Send Messages, Create Public Threads, Send Messages in Threads,
     Manage Threads, Read Message History*

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\python -m pip install -e ".[dev]"
copy .env.example .env    # then paste your DISCORD_TOKEN into .env
.\.venv\Scripts\python -m discobot
```

## Usage

| Command | What it does |
|---|related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---|
| `/character create <name> <prompt>` | Define a character (personality/backstory) |
| `/character list` | List your characters |
| `/character delete <name>` | Delete your character and its sessions |
| `/roleplay start <character>` | Spawn a roleplay thread with that character |
| `/forget` | Wipe the current thread's memory (confirmation button) |

Then just chat in the spawned thread — the character replies in-story, remembering
the last 15 messages / 3,000 tokens (configurable in `.env`).

## Development

```powershell
.\.venv\Scripts\python -m pytest        # unit + integration tests (no network)
.\.venv\Scripts\ruff check src tests    # lint
```

Pointing at a different backend (remote vLLM, OpenAI, etc.) is config-only:
set `LLM_BASE_URL`, `LLM_MODEL`, and `LLM_API_KEY` in `.env`.
