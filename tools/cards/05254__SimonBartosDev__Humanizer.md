---
id: tool-05254
type: tool
area: 库
status: active
tags: [去AI味, JavaScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: Humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/simonbartosdev/humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5254
category: 一、去 AI 味 / Humanizer 库
repo: SimonBartosDev/Humanizer
stars: 0
url: https://github.com/simonbartosdev/humanizer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# SimonBartosDev/Humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/simonbartosdev/humanizer
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Text Humanizer — Transform AI-generated text into natural human writing. Powered by local LLM via Ollama.
- **本地描述**：AI Text Humanizer — Transform AI-generated text into natural human writing. Powered by local LLM via Ollama.
- **拉取时间**：2026-07-25 18:11:46

---

# 🧠 Humanizer

> Transform AI-generated text into natural, human-sounding writing that passes AI detectors.

A local AI text humanizer powered by **Ollama** running **Llama 3.1 8B** — no API keys, no costs, fully private.

## ✨ Features

- **3 Humanization Modes** — Light (subtle polish), Standard (full rewrite), Aggressive (from-scratch rewrite)
- **Iterative Detection Loop** — Humanizes → scores AI probability → re-refines until it passes (up to 3 passes)
- **AI-ism Pre-filter** — Strips 60+ common AI words/phrases before the LLM even touches the text
- **AI Detection Scoring** — Built-in AI probability scoring after each pass
- **Fully Local** — Runs entirely on your machine via Ollama. No API keys, no cloud, no data leaves your computer
- **Premium Dark UI** — Glassmorphism design with smooth animations

## 🚀 Quick Start

### Prerequisites

- [Node.js](https://nodejs.org/) (v18+)
- [Ollama](https://ollama.com/)

### Setup

```bash
# 1. Install Ollama (macOS)
brew install ollama
brew services start ollama

# 2. Pull the model (~4.7GB)
ollama pull llama3.1:8b

# 3. Clone & install
git clone https://github.com/SimonBartosDev/Humanizer.git
cd Humanizer
npm install

# 4. Run
npm run dev
```

Open **http://localhost:3000** and start humanizing!

## 🔧 How It Works

```
Input Text → Strip AI-isms → LLM Rewrite → AI Detection Score
                                    ↑                    ↓
                                    └── Refine ←── Score > 30%?
                                                        ↓
                                                 Score ≤ 30% → Output
```

1. **Pre-processing** — Strips common AI-flagged words (delve, utilize, furthermore, etc.)
2. **LLM Rewrite** — Llama 3.1 rewrites with persona-based prompts tuned for naturalness
3. **Detection Scoring** — The same model scores the output for AI probability
4. **Iterative Refinement** — If score > 30%, it refines targeting specific flagged issues
5. **Output** — Returns the humanized text with the final AI probability score

## 📁 Project Structure

```
Humanizer/
├── server.js          # Express backend, Ollama integration, iterative loop
├── public/
│   ├── index.html     # App layout
│   ├── style.css      # Dark theme, glassmorphism, animations
│   └── script.js      # Frontend logic
├── package.json
└── .gitignore
```

## ⚙️ Configuration

Set these environment variables to customize:

| Variable | Default | Description |
|---|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| `PORT` | `3000` | Server port |
| `OLLAMA_URL` | `http://localhost:11434` | Ollama API URL |
| `MODEL` | `llama3.1:8b` | Ollama model to use |

## 📝 License

MIT
