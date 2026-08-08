---
id: tool-07165
type: tool
area: 库
status: active
tags: [互动叙事, Python, 协议未明, 需API密钥, 英文文档]
title: plath-and-poetry
summary: 互动叙事/聊天写故事
source: https://github.com/bkanumuri1/plath-and-poetry
created: 2026-07-18
updated: 2026-07-18
no: 7165
category: 画龙补充 / 扩容入库 — 补充源
repo: bkanumuri1/plath-and-poetry
stars: 0
url: https://github.com/bkanumuri1/plath-and-poetry
tier: "C"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4f06647591c912fb
  - methods/QUICK_START.md
---

# bkanumuri1/plath-and-poetry

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/bkanumuri1/plath-and-poetry
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：plath-and-poetry
- **拉取时间**：2026-07-25 19:12:49

---

Try it out here: https://plathandpoetry.streamlit.app/

# 📝 Plath & Poetry: An AI-Powered Poem Generator

**Plath & Poetry** is a generative AI app that creates emotionally rich, two-line poems inspired by the haunting style of Sylvia Plath. Built with OpenAI's GPT-3.5 Turbo, LangChain, and Streamlit, this project blends large language models with artistic expression.

> “Whether you want a spark of melancholy or a poetic lift of hope — let AI channel Sylvia for you.”

---

## 🚀 Features

- 🧠 **Contextual Memory**: Remembers past prompts within a session to generate thematically connected poems.
- 🎭 **Sylvia Plath Style**: System prompt engineering imitates Plath’s poetic voice and tone.
- 🌐 **Streamlit Interface**: Simple, responsive UI for real-time interaction.
- 🪄 **LangChain Integration**: Uses structured prompt chaining and memory for dynamic, responsive LLM behavior.

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **LLM**: OpenAI GPT-3.5 Turbo
- **AI Framework**: LangChain
- **Memory**: `ConversationBufferMemory` + `StreamlitChatMessageHistory`
- **Deployment-ready**: Works locally or on platforms like Streamlit Cloud

related:
  - methods/QUICK_START.md
---

## 📦 Project Structure

```text
plath-and-poetry/
├── chatbot/
│   ├── app.py              # Main Streamlit app with memory + LLM integration
│   └── localllama.py       # (Optional) Local OLlama script
├── .devcontainer/
│   └── devcontainer.json   # VS Code dev container config
├── .env                    # Your API keys (excluded via .gitignore)
├── .gitattributes
├── .gitignore              # Prevents sensitive/config files from being committed
├── readme.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## 🧪 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/bkanumuri1/plath-and-poetry.git
cd plath-and-poetry
```

### 2. Set Up Environment Variables

Create a .env file using the example:

```bash
cp .env.example .env
```

Then fill in your OpenAI and LangChain keys:

```bash
OPENAI_API_KEY=your_openai_key
LANGCHAIN_API_KEY=your_langchain_key
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

## 🎯 Why I Built This

As a software engineer with a passion for AI, I wanted to explore how language models could be used for creative self-expression. This project allowed me to apply my knowledge of LangChain and LLM APIs in a poetic and emotionally resonant way.

## 🧠 Next Up

🎛 Mood/style selector

- lets users select a mood for the poem e.g., melancholic, hopeful, dark, playful, surreal

📜 Multi-line/ Dynamic Length Output

- lets users select how many lines they want e.g. 2,4, or a haiku.

🔗 Export & Share Options

- allows users to copy/share poems.

## 🔒 Security

This project uses environment variables to protect API keys. The .env file is excluded via .gitignore. Do not commit your keys to GitHub.
