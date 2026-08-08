---
id: tool-04337
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 人物设定, RAG, 本地写作]
title: st-lorebook-generator
summary: 长篇人物/设定/伏笔一致性（RAG 记忆库）
source: https://github.com/chilleor/st-lorebook-generator
created: 2026-07-18
updated: 2026-07-18
no: 4337
category: 四、长篇一致性 / RAG / 故事圣经 库
repo: chilleor/st-lorebook-generator
stars: 0
url: https://github.com/chilleor/st-lorebook-generator
tier: "C"
use_case: "长篇人物/设定/伏笔一致性（RAG 记忆库）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/人物思维蒸馏法.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 070d4ea1ede4641f
  - methods/模板库.md
---

# chilleor/st-lorebook-generator

- **分类**：四、长篇一致性 / RAG / 故事圣经 库
- **链接**：https://github.com/chilleor/st-lorebook-generator
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：chilleor/st-lorebook-generator
- **拉取时间**：2026-07-25 17:42:44

---

# SillyTavern Lorebook Generator

A [SillyTavern](https://sillytavern.app) UI extension that uses the currently active LLM to **create or update lorebooks / worldinfo files** based on your chat context — characters, user persona, and message history.

![SillyTavern Lorebook Generator](https://img.shields.io/badge/SillyTavern-Extension-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Features

- **Create from scratch** — analyzes the active chat and generates a complete lorebook with keyword-triggered entries for locations, NPCs, factions, plot points, and world mechanics.
- **Update existing** — loads a lorebook you already have, then merges new information from the chat: adds new entries, updates stale ones, and preserves all existing UIDs.
- **Works with any LLM** — uses ST's `generateRaw()` API. Parses structured JSON output for Chat Completion backends; falls back to text-extraction for Text Completion backends.
- **Group chat support** — includes all active group members' character cards in the prompt.
- **Settings panel** — configure max messages, default mode, and a custom prompt prefix directly from ST's Extensions sidebar.
- **No server plugin needed** — pure frontend extension.

---

## Installation

### Option A — Manual install

1. Navigate to your SillyTavern `public/scripts/extensions/third-party/` folder.
2. Clone this repo into it:

```bash
cd /path/to/SillyTavern/public/scripts/extensions/third-party
git clone https://github.com/YOUR_USERNAME/st-lorebook-generator.git
```

3. Refresh SillyTavern in your browser.
4. Go to **Extensions → Manage Extensions** and enable **Lorebook Generator**.

### Option B — Docker dev environment (recommended for development)

See [Docker Dev Environment](#docker-dev-environment) below.

---

## Usage

1. **Open a chat** with at least one character (solo or group).
2. Click the **💡 Lore** button next to the message send button.
3. Choose a mode:
   - **Create from scratch** — optionally give the lorebook a name (auto-generated if blank).
   - **Update existing** — select a lorebook from the dropdown.
4. Click **Generate**.
5. The extension reads the chat context, sends it to the active LLM, parses the response, and saves the lorebook. A confirmation message appears when done.

The saved lorebook is immediately available in ST's **World Info** panel.

---

## Settings

Open **Extensions → Lorebook Generator** in ST's sidebar:

| Setting | Default | Description |
|---------|---------|-------------|
| Max chat messages | 30 | How many recent messages to include in the prompt |
| Default mode | Create | Whether the modal opens in Create or Update mode |
| Custom prompt prefix | *(empty)* | Optional extra instructions prepended to every generation |

Settings are persisted automatically via ST's extension settings storage.

---

## Docker Dev Environment

The repo ships with a `docker-compose.yml` for a self-contained local setup.

### Folder layout

```
~/dev/sillytavern-docker/
  docker-compose.yml
  config/               ← ST config files (auto-created on first run)
  data/                 ← ST user data (characters, chats, lorebooks)
  extensions/
    st-lorebook-generator/   ← this repo (bind-mounted into ST)
```

### First-run

```bash
# Create folder structure
mkdir -p ~/dev/sillytavern-docker/{config,data,extensions}

# Clone this repo into extensions/
cd ~/dev/sillytavern-docker/extensions
git clone https://github.com/YOUR_USERNAME/st-lorebook-generator.git

# Copy docker-compose.yml from this repo
cp st-lorebook-generator/docker-compose.yml ~/dev/sillytavern-docker/

# Start SillyTavern
cd ~/dev/sillytavern-docker
docker compose up -d

# Open in browser
open http://localhost:8000

# Tail logs
docker compose logs -f
```

### Hot reload workflow

ST loads extension JS at page load. To see your changes:

1. Edit any file in `extensions/st-lorebook-generator/`.
2. Hard-refresh the browser (`Cmd+Shift+R` / `Ctrl+Shift+R`).

No Docker restart needed — the folder is a live bind mount.

---

## Project Structure

```
st-lorebook-generator/
├── manifest.json          ← ST extension manifest
├── index.js               ← Entry point: button, modal, settings
├── modal.html             ← Modal template (loaded via fetch)
├── style.css              ← Dark-theme styles using ST CSS variables
├── lib/
│   ├── context.js         ← Reads characters, persona, chat history
│   ├── worldinfo.js       ← Lorebook list / load / save API calls
│   └── generate.js        ← Calls generateRaw(), parses JSON response
└── prompts/
    ├── _shared.js         ← System prompt + formatting helpers
    ├── create.js          ← Prompt builder for "create" mode
    └── update.js          ← Prompt builder for "update" mode
```

---

## Lorebook JSON format

The extension reads and writes SillyTavern's native lorebook format. Each entry has keyword triggers (`key`), lore text (`content`), ordering, and position metadata. See [ST World Info docs](https://docs.sillytavern.app/usage/core-concepts/worldinfo/) for details.

---

## Compatibility

| Requirement | Version |
|-------------|---------|
| SillyTavern | ≥ 1.12.0 |
| LLM backend | Any (Chat Completion or Text Completion) |

Structured JSON output (`responseSchema`) works best with Chat Completion APIs (OpenAI, Claude, etc.). For Text Completion APIs the extension parses JSON from the raw text response.

---

## Contributing

Pull requests welcome. Please open an issue first for significant changes.

related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---

## License

[MIT](https://github.com/chilleor/st-lorebook-generator/blob/main/LICENSE)
