---
id: tool-00933
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: llm-discussion
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/felixsoderstrom/llm-discussion
created: 2026-07-18
updated: 2026-07-18
no: 933
category: 二、网文 / 长篇 AI 写作系统 库
repo: FelixSoderstrom/llm-discussion
stars: 1
url: https://github.com/felixsoderstrom/llm-discussion
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 0f09f3be8d4c4f03
  - methods/最强写作方法论_全球最强综合版.md
---

# FelixSoderstrom/llm-discussion

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/felixsoderstrom/llm-discussion
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：ai, chatbot, chatgpt, claude, large-language-models, prompt-engineering
- **GitHub 描述**：A discussion chatroom for large language models to discuss their biases over any topic you feed them. Dynamic system prompt writing creates multiple biases and takes on any topic you throw at them.
- **本地描述**：A discussion chatroom for large language models to discuss their biases over any topic you feed them. Dynamic system prompt writing creates multiple biases and takes on any topic you throw at them.
- **拉取时间**：2026-07-23 23:06:16

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# LLM Chatroom

A command-line application that creates a simulated discussion between AI agents on a topic or question provided by the user.

## Overview

LLM Chatroom uses OpenAI's API to simulate a conversation between multiple AI agents. The agents discuss the provided topic, offer different perspectives, and generate a final summary of the conversation. This can be useful for:

- Exploring different viewpoints on a complex topic
- Generating ideas through simulated brainstorming
- Understanding nuanced arguments around a subject
- Teaching through simulated discussions

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/FelixSoderstrom/llm-discussion.git
   cd llm-discussion
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the application from the command line:

```
python main.py
```

When prompted, enter a topic or question for the AI agents to discuss. For example:
- "What are the ethical implications of AI development?"
- "Discuss the pros and cons of remote work"
- "How might climate change affect global agriculture in the next 50 years?"

The AI agents will conduct a discussion, and the application will:
1. Display the conversation in real-time
2. Generate a final summary of the discussion
3. Save the complete chat history to the `chat_logs` directory

## Project Structure

```
llm-discussion/
├── .env                  # Environment variables including API keys
├── main.py               # Entry point for the application
├── requirements.txt      # Python dependencies
├── chat_logs/            # Directory containing saved chat histories
└── src/
    └── chat/
        ├── chatroom.py   # Chatroom class that manages the AI discussion
        └── ...           # Other modules related to the chat functionality
```

## Requirements

- Python 3.6+
- OpenAI API key
- Required Python packages (see requirements.txt)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 
