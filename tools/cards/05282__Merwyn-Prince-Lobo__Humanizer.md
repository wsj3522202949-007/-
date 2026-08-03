---
id: tool-05282
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: Humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/merwyn-prince-lobo/humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5282
category: 一、去 AI 味 / Humanizer 库
repo: Merwyn-Prince-Lobo/Humanizer
stars: 0
url: https://github.com/merwyn-prince-lobo/humanizer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Merwyn-Prince-Lobo/Humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/merwyn-prince-lobo/humanizer
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A tiny local webapp that rewrites stiff/AI-sounding text using a local LLM (via [Ollama](https://ollama.com)). No accounts, no paywalls, no word limits, nothing leaves your machine.  Pipeline: **paste text → chunk it → feed each chunk to your chosen local model with a humanize prompt → stitch the rewritten chunks back together.**
- **本地描述**：A tiny local webapp that rewrites stiff/AI-sounding text using a local LLM (via [Ollama](https://ollama.com)). No accounts, no paywalls, no word limits, nothing leaves your machine.  Pipeline: **paste text → chunk it → feed each chunk to your chosen local model with a humanize prompt → stitch the rewritten chunks back together.**
- **拉取时间**：2026-07-25 18:12:49

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Local Text Humanizer

A tiny local webapp that rewrites stiff/AI-sounding text using a local LLM
(via [Ollama](https://ollama.com)). No accounts, no paywalls, no word limits,
nothing leaves your machine.

Pipeline:

**Paste text → Chunk it → Feed each chunk to your chosen local model with a
humanize prompt → Stitch the rewritten chunks back together.**

## Setup (One-time)

### 1. Install Ollama

#### Windows (PowerShell)

```powershell
winget install Ollama.Ollama
```

#### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Start Ollama and pull at least one model

```bash
ollama serve
ollama pull llama3.1:8b
ollama pull mistral
ollama pull qwen2.5:14b
```

Recommended starting points:

- `llama3.1:8b` – Good balance of speed and quality.
- `mistral` – Faster and smaller.
- `qwen2.5:14b` – Slower but produces noticeably more natural output.

You can also skip this step and pull models directly from inside the webapp.

### 3. Create and activate a virtual environment

#### Windows (PowerShell)

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

#### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

## Run it

Make sure Ollama is running:

```bash
ollama serve
```

Then start the app.

### Windows (PowerShell)

```powershell
python app.py
```

### Linux

```bash
python app.py
```

Open:

```
http://localhost:5000
```

## Using it

1. Pick a model from the dropdown, or type a new model name and click **Pull Model** if you don't already have it installed.
2. Set the chunk size if you want. The default is **500 words per chunk**. Smaller chunks mean more model calls but reduce the chance of the model drifting or summarizing long inputs.
3. Paste your text and click **Run Pipeline**.
4. Watch the progress blocks as each chunk is processed.
5. Copy or download the rewritten text when processing is complete.

## Notes

- Bigger models (14B+) generally produce more natural results but are slower on laptop GPUs. Start with `llama3.1:8b` and move to larger models if you need better quality.
- Since Ollama uses your GPU, avoid running other GPU-intensive applications (such as Minecraft with shaders or Assetto Corsa) while processing large documents.
- Everything runs locally using `localhost:11434` (Ollama) and `localhost:5000` (the webapp). No external network calls are made, and your text never leaves your machine.
- If you're using this for situations where AI detection matters (such as school submissions), remember that AI detectors and humanizers are constantly evolving. There are no guarantees that rewritten text will avoid detection.
