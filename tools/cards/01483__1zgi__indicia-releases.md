---
id: tool-01483
type: tool
area: 库
status: active
tags: [校对, Ruby, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: indicia-releases
summary: 错别字/语法/风格校对
source: https://github.com/1zgi/indicia-releases
created: 2026-07-18
updated: 2026-07-18
no: 1483
category: 二、网文 / 长篇 AI 写作系统 库
repo: 1zgi/indicia-releases
stars: 0
url: https://github.com/1zgi/indicia-releases
tier: "C"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 1zgi/indicia-releases

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/1zgi/indicia-releases
- **Stars**：0
- **语言**：Ruby
- **License**：None
- **Topics**：—
- **GitHub 描述**：Indicia — floating AI prompt improver and IELTS writing tutor (releases)
- **本地描述**：Indicia — floating AI prompt improver and IELTS writing tutor (releases)
- **拉取时间**：2026-07-23 23:22:20

---

# Indicia

A minimal, floating desktop app (macOS, Linux, Windows) that improves your AI prompts and scores your English writing using IELTS criteria. Runs fully offline with a local Ollama LLM.

## Features

- **Prompt analysis** — refined text, IELTS band score, vocabulary upgrades, and prompt rating (powered by Qwen3)
- **Vision mode** — drag, paste, or browse an image with a text description to generate professional AI prompts using Qwen3-VL vision model
- **Real-time spellcheck** — underlines mistakes as you type, click for correction suggestions
- **Translation** — translate prompts from any language to English using Helsinki-NLP OPUS-MT models (downloaded on demand)
- **Theming** — light/dark mode with 6 accent color palettes
- **Global hotkey** — Cmd+Shift+P (macOS) or Ctrl+Shift+P (Linux/Windows)
- **Fully offline** — all AI processing runs locally via Ollama, no data leaves your machine
- **Native build** — compiled to native binary with Nuitka (no Python runtime needed)

## Requirements

- macOS (Apple Silicon), Linux (x86_64), or Windows (x86_64)

Ollama and the required AI models are installed automatically on first launch.

## Install

### macOS (Homebrew)

```bash
brew tap 1zgi/indicia https://github.com/1zgi/indicia-releases
brew install --cask indicia
```

To update: `brew upgrade --cask indicia`

### Windows (Scoop)

```powershell
scoop bucket add indicia https://github.com/1zgi/indicia-releases
scoop install indicia
```

To update: `scoop update indicia`

### Linux / Ubuntu (.deb)

Download `indicia_X.Y.Z_amd64.deb` from [Releases](https://github.com/1zgi/indicia-releases/releases), then:

```bash
sudo dpkg -i indicia_*.deb
```

To update: download the new `.deb` and run `dpkg -i` again.

### Manual download (all platforms)

Pre-built binaries for macOS, Linux, and Windows are available on the [Releases](https://github.com/1zgi/indicia-releases/releases) page.

## First launch

Everything sets up automatically in the background:

1. **Ollama** — if not installed, downloads and installs automatically (~500MB)
2. **AI models** — pulls Qwen3 and Qwen3-VL from Ollama (progress shown in-app)
3. **Translation engine** — creates an isolated Python environment with torch + transformers (progress shown in translation panel)

The app is usable immediately while setup runs in the background.

### Model management

- Click **⚙** to open Settings — view, switch, or pull Ollama models
- Type `list` in the model name field to browse all available models from the Ollama library
- Pull any model by name (e.g. `llama3.1`, `gemma3`, `deepseek-r1`)

### Translation models

- Click **文A** to open the translation panel
- Click **Browse Models** to see available language pairs from HuggingFace
- Pick a language (e.g. TR → EN) and click **Pull** to download (~300MB each)
- Select the downloaded model and click **Translate**

> **Note:** Translation requires Python 3.12+ on your system. macOS and Linux include it by default. Windows users may need to install it from [python.org](https://python.org).

## Windows — SmartScreen warning

The Windows build is **not code-signed**, so SmartScreen will show a **"Windows protected your PC"** warning on first launch.

To proceed:
1. Click **"More info"**
2. Click **"Run anyway"**

## macOS — permissions setup

Indicia needs Accessibility and Input Monitoring permissions for the global hotkey (Cmd+Shift+P). On first launch, macOS will prompt you to grant access in **System Settings > Privacy & Security**.

## Auto-start at login

**macOS:**
```bash
# Indicia includes a LaunchAgent plist — copy it:
cp /Applications/Indicia.app/Contents/Resources/com.ctrlrings.indicia.plist ~/Library/LaunchAgents/
```

**Linux:**
```bash
cp /usr/share/applications/indicia.desktop ~/.config/autostart/
```

**Windows:** Add a shortcut to `Indicia.exe` in `shell:startup` (press `Win+R`, type `shell:startup`).

## Keyboard shortcuts

| Shortcut | Action |
|----------|-----related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `Cmd+Shift+P` / `Ctrl+Shift+P` | Toggle window visibility |
| `Cmd+V` / `Ctrl+V` | Paste image (auto-switches to image mode) |
| `Enter` | Send prompt for analysis |
| `Shift+Enter` | New line |
| `Escape` | Hide window |
| `Cmd+Q` / `Ctrl+Q` | Quit |

## Uninstall

**macOS:**
```bash
brew uninstall --cask indicia
brew untap 1zgi/indicia
rm -rf ~/.cache/indicia                          # remove downloaded translation models
rm -f ~/Library/LaunchAgents/com.ctrlrings.indicia.plist  # remove auto-start
```

**Windows:**
```powershell
scoop uninstall indicia
scoop bucket rm indicia
Remove-Item -Recurse "$env:USERPROFILE\.cache\indicia"   # remove downloaded translation models
```

**Linux:**
```bash
sudo dpkg -r indicia
rm -rf ~/.cache/indicia                          # remove downloaded translation models
rm -f ~/.config/autostart/indicia.desktop        # remove auto-start
```

## License

Free to use.
