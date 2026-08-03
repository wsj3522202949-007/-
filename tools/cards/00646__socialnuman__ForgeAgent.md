---
id: tool-00646
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ForgeAgent
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/socialnuman/forgeagent
created: 2026-07-18
updated: 2026-07-18
no: 646
category: 二、网文 / 长篇 AI 写作系统 库
repo: socialnuman/ForgeAgent
stars: 1
url: https://github.com/socialnuman/forgeagent
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# socialnuman/ForgeAgent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/socialnuman/forgeagent
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Terminal-based AI coding assistant powered by LangChain, Gemini, and Rich — with filesystem tools for reading, writing, and managing projects directly from the CLI.
- **本地描述**：Terminal-based AI coding assistant powered by LangChain, Gemini, and Rich — with filesystem tools for reading, writing, and managing projects directly from the CLI.
- **拉取时间**：2026-07-23 22:57:54

---

# ForgeAgent

Terminal-based AI coding assistant powered by LangChain, Gemini, and Rich.

ForgeAgent can:
- Navigate directories
- Read files
- Create and edit files
- Create folders
- Stream AI responses in real time
- Display beautiful terminal output using Rich

---

## Features

- ⚡ Gemini 2.5 Flash integration
- 🧠 LangChain agent architecture
- 📂 File system tools
- 🛠️ Directory management
- 🎨 Rich terminal UI
- 🔄 Streaming responses
- 🔐 Environment variable support with dotenv

---

## Demo

```bash
Enter your query: create a notes folder and add todo.txt
```

Example output:

```bash
🔧 Using tool: create_directory
🗒️ Tool Result:
Successfully created directory notes

🔧 Using tool: write_file
🗒️ Tool Result:
File todo.txt created successfully.
```

---

## Project Structure

```bash
.
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/forgeagent.git
cd forgeagent
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## Run the Agent

```bash
python main.py
```

---

## Example Queries

```text
List files in this directory
```

```text
Create a folder called src/components
```

```text
Read app.py
```

```text
Create a README file for my project
```

---

## Tech Stack

- Python
- LangChain
- Google Gemini
- Rich
- python-dotenv

---

## Future Improvements

- Command history
- Multi-file editing
- Syntax highlighting
- Sandboxed execution
- Memory support
- MCP integration
- Voice commands
- Git integration

---

## License

MIT License

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Acknowledgements

Built using:
- LangChain
- Google Gemini
- Rich
