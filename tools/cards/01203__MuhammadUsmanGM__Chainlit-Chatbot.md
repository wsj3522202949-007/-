---
id: tool-01203
type: tool
area: 库
status: active
tags: [互动叙事, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: Chainlit-Chatbot
summary: 互动叙事/聊天写故事
source: https://github.com/muhammadusmangm/chainlit-chatbot
created: 2026-07-18
updated: 2026-07-18
no: 1203
category: 二、网文 / 长篇 AI 写作系统 库
repo: MuhammadUsmanGM/Chainlit-Chatbot
stars: 7
url: https://github.com/muhammadusmangm/chainlit-chatbot
tier: "B"
use_case: "互动叙事/聊天写故事"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 67c06e7c121691a1
  - methods/最强写作方法论_全球最强综合版.md
---

# MuhammadUsmanGM/Chainlit-Chatbot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/muhammadusmangm/chainlit-chatbot
- **Stars**：7
- **语言**：Python
- **License**：MIT
- **Topics**：ai-assistant, chainlit, openai, openrouter, python, together-ai, tool-integration, uv
- **GitHub 描述**：AI Assistant with Chainlit Interface A multi-functional AI chatbot built with Chainlit, supporting tools like weather updates, news, jokes, currency exchange, and intelligent agents for writing, email generation, prompt egineering and translation. Users can switch between LLMs like Gemini, Llama, and Exaone, with interactive UI and chat history
- **本地描述**：AI Assistant with Chainlit Interface A multi-functional AI chatbot built with Chainlit, supporting tools like weather updates, news, jokes, currency exchange, and intelligent agents for writing, email generation, prompt egineering and translation. Users can switch between LLMs like Gemini, Llama, and Exaone, with interactive UI and chat history
- **拉取时间**：2026-07-23 23:14:09

---

# 🧠 Multi-Tool Chatbot  
**(Chainlit + TogetherAI + OpenRouter + Gemini)**


[![Chainlit App](https://img.shields.io/badge/Chainlit-Launch-blue?logo=chatbot)](https://chainlit-chatbot-production.up.railway.app/)


[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Chainlit](https://img.shields.io/badge/Built%20With-Chainlit-FF5F00)](https://www.chainlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#license)

An advanced, modular AI assistant built with [Chainlit](https://www.chainlit.io/), integrated with multiple LLM providers like **Gemini**, **TogetherAI**, and **OpenRouter**, and powered by a suite of useful tools for enhanced user interaction.

---

## ✨ Key Features

- ✅ **Multi-LLM Support** – Gemini, Together Meta, Exaone, OpenRouter DeepSeek  
- 🔧 **Tool-Based Modular Architecture** – Easy integration via `function_tool`  
- 🧠 **Dynamic Model Configuration** – Switch profiles on the fly  
- 💬 **Live Typing & Streamed Responses** – Real-time interaction  
- 🧾 **Persistent Chat History** – Auto-saves to JSON  
- 🎯 **Starter Prompts** – For better user engagement

---

## 🧰 Built-in Tools

- 🌦️ **Weather Checker**  
- 🗞️ **News Fetcher**  
- 😂 **Programming Joke Teller**  
- 💱 **Currency Exchange Lookup**  
- ✍️ **EasyWriter** – Writing assistant  
- 📧 **EmailWriter** – Email generator  
- 🌏 **Language Translator**  
- 🧪 **Prompt Engineer**
- 🌐 **IP Geolocation**
- 🪲 **Code Debugger** - Debug and improve code


related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🔮 Built-in Language Hand-Off Tools

Easily switch or hand off tasks between:

- ✨ English Language
- ✨ Urdu Language

## 📁 Project Structure


├── main.py # Entry point with chat logic, streaming, and tools
├── my_secrets.py # Handles environment variables securely
├── .env # API keys and config (not committed)
├──images #contain output and interface images
├──public #contain svg logos for starter tools
└── chat_history.json # Chat history output file (on session end)

## 📬 Contact

For questions, reach out via GitHub Issues or [muhammadusman5965etc@gmail.com](mailto:muhammadusman5965etc@gmail.com)

## 🚆Interface Preview

![Interface](https://github.com/MuhammadUsmanGM/Chainlit-Chatbot/blob/main//images/Interface.png)

## 📤Sample Output

![Output](https://github.com/MuhammadUsmanGM/Chainlit-Chatbot/blob/main//images/Output.png)
