---
id: tool-04906
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议未明, 需API密钥, 英文文档]
title: equalizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/asarrafi47/equalizer
created: 2026-07-18
updated: 2026-07-18
no: 4906
category: 一、去 AI 味 / Humanizer 库
repo: asarrafi47/equalizer
stars: 0
url: https://github.com/asarrafi47/equalizer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: b2fdf5cf752b0d50
  - methods/改稿润色指令库.md
---

# asarrafi47/equalizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/asarrafi47/equalizer
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Mac-native AI text humanizer with detector-driven stealth rewrites
- **本地描述**：Mac-native AI text humanizer with detector-driven stealth rewrites
- **拉取时间**：2026-07-25 17:58:52

---

# Equalizer

A Mac-native desktop app powered by **Apple Intelligence**. Rewrite AI-generated content so it reads naturally, like [humanize.ai](https://humanizeai.com/).

On launch, Equalizer starts the [apfel](https://github.com/Arthur-Ficial/apfel) bridge and opens in its own window — no browser needed.

## Requirements

- macOS 26+ (Tahoe) on **Apple Silicon** (M1 or later)
- **Apple Intelligence** enabled in System Settings
- Python 3.12+
- [Homebrew](https://brew.sh/) (for installing apfel)

## Quick start

### Install as a Mac app (recommended)

```bash
./install.sh
```

This sets everything up and installs **Equalizer** to your **Applications** folder.

Then open it like any other app:
- **Spotlight:** ⌘+Space → type `Equalizer`
- **Applications** folder in Finder
- Drag it to your **Dock**

No Terminal window — it opens as a native desktop app.

### Run from Terminal (development)

```bash
./start.sh
```

## How it works

```
python -m app
    │
    ├─► starts apfel --serve  (Apple Intelligence bridge, if not already running)
    │
    ├─► starts FastAPI backend on :8000
    │
    └─► opens native macOS window (pywebview)
            │
            └─► humanize requests → apfel → on-device Foundation Model
```

Everything runs on your Mac. No cloud API keys, no Docker required.

## API

```bash
curl -X POST http://127.0.0.1:8000/api/v1/humanize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Furthermore, it is important to note that artificial intelligence has revolutionized numerous industries.",
    "mode": "ultra",
    "tone": "casual"
  }'
```

Interactive docs: http://127.0.0.1:8000/docs

## Configuration

Copy `.env.example` to `.env` to customize:

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_PROVIDER` | `apple` | `apple`, `ollama`, or `openai` |
| `APPLE_AUTO_START_BRIDGE` | `true` | Start apfel automatically on launch |
| `APPLE_BASE_URL` | `http://localhost:11434/v1` | Bridge API endpoint |
| `APP_PORT` | `8000` | Web UI port |

Set `APPLE_AUTO_START_BRIDGE=false` if you prefer to run the bridge yourself in a separate terminal.

## Apple models: on-device vs cloud (PCC)

Equalizer supports two Apple Intelligence tiers:

| Tier | Model ID | Bridge | Size | Context |
|------|----------|--------|------|------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| **On-device** (default) | `apple-foundationmodel` | `apfel --serve` | ~3B params | 4K tokens |
| **On-device** (fm CLI) | `system` | `fm serve` | ~3B params | 4K tokens |
| **Cloud (PCC)** | `pcc` | `fm serve` | Large server model | 32K tokens |

**apfel only exposes the on-device model.** For Apple's bigger **Private Cloud Compute** model, use the built-in `fm` CLI (macOS 27+).

### Switch to the cloud model (PCC)

**Step 1 — Start the bridge in Terminal** (must stay open):

```bash
fm serve --port 1976
```

PCC requires a **foreground Terminal** — Equalizer cannot auto-start it in the background.

**Step 2 — Configure Equalizer** (create `.env` from `.env.example`):

```env
LLM_PROVIDER=apple
APPLE_BRIDGE=fm
APPLE_MODEL=pcc
APPLE_BASE_URL=http://localhost:1976/v1
APPLE_AUTO_START_BRIDGE=false
```

**Step 3 — Restart Equalizer**

### Requirements for PCC

- macOS 27+ with `/usr/bin/fm`
- Apple Intelligence enabled, signed into iCloud
- Internet connection
- Daily usage limits apply (managed by Apple per iCloud account)
- For **App Store apps**: Apple developer entitlement required ([Private Cloud Compute](https://developer.apple.com/private-cloud-compute/)). CLI `fm serve` usage from Terminal is for personal/local use.

### Check what's available on your Mac

```bash
fm available          # shows if system and pcc are available
fm serve --port 1976  # then in another terminal:
curl http://localhost:1976/v1/models
```

## Optional: Ollama or OpenAI

Change `LLM_PROVIDER` in `.env`:

```
LLM_PROVIDER=ollama   # requires ollama running locally
LLM_PROVIDER=openai   # requires OPENAI_API_KEY
```

Docker + Ollama setup is still available via `docker compose up` if you want it on non-Mac machines.

## Project structure

```
equalizer/
├── app/
│   ├── main.py       # FastAPI app + startup lifecycle
│   ├── bridge.py     # Auto-starts apfel
│   ├── desktop.py    # Native window launcher
│   ├── humanizer.py  # Core logic
│   ├── llm.py        # LLM clients
│   └── prompts.py    # Humanization prompts
├── start.sh          # One-command launcher
├── scripts/
│   └── create-macos-app.sh  # Build Equalizer.app
└── requirements.txt
```

## License

MIT
