---
id: tool-01498
type: tool
area: 库
status: active
tags: [CSS, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: WriterFlowAI
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/wecodark/writerflowai
created: 2026-07-18
updated: 2026-07-18
no: 1498
category: 二、网文 / 长篇 AI 写作系统 库
repo: WeCodark/WriterFlowAI
stars: 0
url: https://github.com/wecodark/writerflowai
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# WeCodark/WriterFlowAI

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/wecodark/writerflowai
- **Stars**：0
- **语言**：CSS
- **License**：None
- **Topics**：—
- **GitHub 描述**：A Copilot-style writing assistant for writers. WriterFlow uses Meta Llama 4 Scout via Groq to provide real-time, inline text suggestions as you write — displayed as ghost text that you can accept with a single Tab press.
- **本地描述**：A Copilot-style writing assistant for writers. WriterFlow uses Meta Llama 4 Scout via Groq to provide real-time, inline text suggestions as you write — displayed as ghost text that you can accept with a single Tab press.
- **拉取时间**：2026-07-23 23:22:47

---

# WriterFlow - AI Writing Assistant

A **Copilot-style writing assistant** for writers. WriterFlow uses **Meta Llama 4 Scout** via [Groq](https://groq.com) to provide real-time, inline text suggestions as you write — displayed as ghost text that you can accept with a single `Tab` press.

> Think GitHub Copilot, but for **stories, blogs, essays, and poetry** instead of code.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask)
![Groq](https://img.shields.io/badge/Groq-Meta%20Llama%204-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## What Is This?

WriterFlow is a distraction-free, dark-themed writing editor that runs in your browser. As you type, the AI reads your context and suggests the next sentence or phrase in **faded ghost text** — just like how Copilot autocompletes code. You can accept, dismiss, or just keep typing.

It also includes a **Rewrite** feature: select any text, give an instruction (e.g., *"make it more dramatic"*), and the AI rewrites it for you.

### Key Features

| Feature | Description |
|---|---|
| **Ghost Text Suggestions** | AI-generated continuations appear as faded text after you pause typing |
| **Tab to Accept** | Press `Tab` to accept a suggestion instantly |
| **7 Writing Genres** | General, Fiction, Academic, Poetry, Blog, Journalism, Screenplay |
| **7 Tones** | Neutral, Formal, Casual, Dramatic, Humorous, Melancholic, Inspiring |
| **Rewrite Selection** | Select text, press `Ctrl+Shift+R`, give instructions, AI rewrites it |
| **Prediction Confidence** | Right-hand panel displays alternative next words with percentage probabilities |
| **Premium Dark UI** | Beautiful, distraction-free editor with violet accents |
| **Live Word Count** | Real-time word and character count |

---

## Tech Stack

- **Backend:** Python + Flask
- **AI Model:** Meta Llama 4 Scout 17B (via Groq API)
- **Frontend:** Vanilla HTML, CSS, JavaScript
- **Design:** Dark mode, serif typography for writing, glassmorphism elements

---

## Project Structure

```
Word-predictor/
├── server.py              # Flask backend — handles API routes & Groq calls
├── requirements.txt       # Python dependencies
├── .env                   # Groq API key (create this yourself)
├── README.md              # You're reading this
└── static/
    ├── index.html         # Editor HTML layout
    ├── styles.css         # Premium dark theme styling
    └── app.js             # Ghost text engine & UI logic
```

---

## How to Run

### Prerequisites

- **Python 3.10+** installed on your machine
- A **Groq API Key** — get one free at [console.groq.com](https://console.groq.com)

### Step 1: Clone / Download the Project

```bash
cd Word-predictor
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `flask` — web server
- `flask-cors` — cross-origin support
- `groq` — Groq Python SDK
- `python-dotenv` — environment variable loader

### Step 3: Set Up Your API Key

Create a `.env` file in the project root (if not already present):

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Replace `your_groq_api_key_here` with your actual key from [Groq Console](https://console.groq.com/keys).

### Step 4: Run the Server

```bash
python3 server.py
```

You should see:

```
WriterFlow is running at http://localhost:8080
```

### Step 5: Open in Browser

Go to **[http://localhost:8080](http://localhost:8080)** and start writing!

---

## Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Tab` | Accept the current ghost suggestion |
| `Esc` | Dismiss the current suggestion |
| `Ctrl + Shift + R` | Open the Rewrite panel for selected text |

---

## Settings

Click the **gear icon** in the top-right corner to access:

- **Writing Genre** — Changes the AI's writing style (Fiction, Poetry, Academic, etc.)
- **Tone** — Adjusts the emotional quality (Dramatic, Humorous, Formal, etc.)
- **Suggestion Delay** — How long to wait after you stop typing before generating a suggestion (500ms - 3s)
- **AI Suggestions Toggle** — Turn suggestions on/off
- **Sound Effects** — Optional accept sound

---

## How It Works

1. **You type** in the editor
2. After a configurable pause (default 1.2s), the frontend sends your recent text to the Flask backend
3. The backend calls **Groq's API** with Meta Llama 4 Scout, asking for a suggestion and top alternative words with probabilities
4. The AI returns a structured JSON object
5. The top suggestion appears as **ghost text** (faded, inline) right after your cursor
6. Alternative predictions (e.g. *Dragon 15%*) slide in on a sleek right-hand panel
7. Press **Tab** to accept the ghost text into your document, or just keep typing to dismiss

```
You type:  "The old lighthouse stood at the edge of the cliff, its light"
AI ghost:  " sweeping across the dark waters"
            ^ faded text — press Tab to accept
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves the editor UI |
| `POST` | `/api/suggest` | Generates a text continuation |
| `POST` | `/api/rewrite` | Rewrites selected text with instructions |

### Example - Suggestion Request

```bash
curl -X POST http://localhost:8080/api/suggest \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The rain fell softly on the rooftop",
    "cursor_context": "The rain fell softly on the rooftop",
    "genre": "fiction",
    "tone": "melancholic"
  }'
```

### Example - Rewrite Request

```bash
curl -X POST http://localhost:8080/api/rewrite \
  -H "Content-Type: application/json" \
  -d '{
    "text": "It was raining outside.",
    "instruction": "Make it more poetic and vivid"
  }'
```

---

## Contributing

Feel free to fork and improve! Some ideas:

- [ ] Add paragraph-level suggestions
- [ ] Export to Markdown / PDF
- [ ] Local model support (Ollama)
- [ ] Multi-document tabs
- [ ] Collaboration mode

---

## License

This project is open source under the `[MIT License](LICENSE)`.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<p align="center">
  Built with Meta Llama and Groq <br>
  Happy Writing!
</p>
