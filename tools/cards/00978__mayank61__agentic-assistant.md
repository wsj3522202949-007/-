---
id: tool-00978
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: agentic-assistant
summary: 多 Agent 协作自动产文
source: https://github.com/mayank61/agentic-assistant
created: 2026-07-18
updated: 2026-07-18
no: 978
category: 二、网文 / 长篇 AI 写作系统 库
repo: mayank61/agentic-assistant
stars: 0
url: https://github.com/mayank61/agentic-assistant
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 0b242d5877017a63
  - methods/最强写作方法论_全球最强综合版.md
---

# mayank61/agentic-assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mayank61/agentic-assistant
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A Python-based agentic AI assistant that uses tool calling to perform actions like generating QR codes, checking weather, writing files, and more — powered by LLMs with a controlled agent loop.
- **本地描述**：A Python-based agentic AI assistant that uses tool calling to perform actions like generating QR codes, checking weather, writing files, and more — powered by LLMs with a controlled agent loop.
- **拉取时间**：2026-07-23 23:07:34

---

# 🤖 Agentic Assistant (Tool-Calling AI)

A function-calling agent built using Groq LLMs.
It supports:
- Checking time
- Fetching weather
- Generating QR codes
- Writing to files

## 🚀 How to Run
```bash
python app.py
``` 


# 🤖 Agentic Assistant — AI Tool-Calling Agent

This project is a **function-calling AI agent** that uses LLMs (e.g., Groq / LLaMA) to perform real-world tasks like:

- Getting current time
- Fetching weather from IP
- Writing text files
- Generating QR codes with logos

All actions are done through a controlled **agent loop** with single tool execution per turn.

---

## 🚀 Features

✔️ Dynamic tool routing  
✔️ Loop safety (no infinite tool calls)  
✔️ Structured tool responses  
✔️ ReAct-style flow (Think → Act → Observe → Answer)  
✔️ Modular architecture

---

## 🧠 Example Commands

| Input | What Happens |
|--------|---------------|
| `What time is it?` | Calls time tool |
| `Save the weather into weather.txt` | weather → write file |
| `Make a QR code for https://google.com using logo.jpg` | generate QR pic |

---

## 🏗 Architecture

LLM → Tool Call → Execute → Inject Result → LLM → Final Answer

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🔧 Setup

```bash
git clone https://github.com/mayank61/agentic-assistant
cd agentic-assistant
pip install -r requirements.txt
python app.py



