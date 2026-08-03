---
id: tool-07164
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档]
title: googleai
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/bisnuray/googleai
created: 2026-07-18
updated: 2026-07-18
no: 7164
category: 画龙补充 / 扩容入库 — 补充源
repo: bisnuray/googleai
stars: 9
url: https://github.com/bisnuray/googleai
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# bisnuray/googleai

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/bisnuray/googleai
- **Stars**：9
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：This Telegram bot uses the PaLM API, an advanced language model, to generate creative and coherent text based on user-provided prompts. Built using the aiogram library, the bot offers an interactive and engaging way to generate written content for various purposes, such as story ideas, creative writing, or even conversation starters. 
- **本地描述**：googleai
- **拉取时间**：2026-07-25 19:12:48

related:
  - methods/QUICK_START.md
---

# PaLM Telegram Bot

This repository contains the source code for a simple Telegram bot that uses the PaLM API to generate text based on user-provided prompts. The bot is built using the [aiogram ↗](https://docs.aiogram.dev/en/latest/dispatcher.html) library for asynchronous handling of the Telegram bot API.

## Features

- Accepts text prompts and generates text using the PaLM API.
- Provides generated text as a response in Telegram.
- Supports the `/start` command for welcoming users and the `/bard` command for generating text.

## Requirements

- Python 3.6 or higher
- `aiogram` library
- `google.generativeai` library
- PaLM API access: Obtain an API key from [Google's GenerativeAI Developer Portal ↗](https://developers.generativeai.google/)

## Installation

1. Clone the repository:

   `````
   git clone https://github.com/bisnuray/googleai/

2. Change the current directory:

   ````
   cd googleai
   ````

3. Install the required Python packages:

   ````
   pip install aiogram google-generativeai
   ````

4. Replace the `API_KEY` and `TG_BOT_TOKEN` placeholders in the `bot.py` script with your PaLM API key and Telegram bot token, respectively.

5. Run the `bot.py` script:

   ````
   python bot.py
   ````

## Usage

1. Start a conversation with your bot on Telegram.
2. Send the `/start` command to receive a welcome message.
3. Send the `/bard` command followed by a text prompt, e.g., `/bard Once upon a time`.
4. The bot will generate text based on the prompt and send it back as a message.
