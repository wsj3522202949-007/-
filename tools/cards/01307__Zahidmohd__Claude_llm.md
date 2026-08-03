---
id: tool-01307
type: tool
area: 库
status: active
tags: [Claude插件, TypeScript, 协议未明, 需API密钥, 英文文档]
title: Claude_llm
summary: Claude Code 插件式写作流
source: https://github.com/zahidmohd/claude_llm
created: 2026-07-18
updated: 2026-07-18
no: 1307
category: 二、网文 / 长篇 AI 写作系统 库
repo: Zahidmohd/Claude_llm
stars: 0
url: https://github.com/zahidmohd/claude_llm
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Zahidmohd/Claude_llm

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/zahidmohd/claude_llm
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A terminal-based AI coding assistant built in TypeScript. It connects to an LLM to autonomously perform tasks. Features include an agent loop and tools for reading, writing, and executing shell commands. This allows the AI to understand your codebase, apply edits, and run tests iteratively.
- **本地描述**：A terminal-based AI coding assistant built in TypeScript. It connects to an LLM to autonomously perform tasks. Features include an agent loop and tools for reading, writing, and executing shell commands. This allows the AI to understand your codebase, apply edits, and run tests iteratively.
- **拉取时间**：2026-07-23 23:17:13

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Coding Assistant (Claude Code Clone)

A terminal-based AI coding assistant built in TypeScript that autonomously performs coding tasks. This agent connects to Large Language Models (LLMs) to understand instructions, read codebase context, apply file edits, and execute shell commands iteratively until the task is complete.

## Features

- **Autonomous Agent Loop**: Maintains conversation context and executes multiple steps to solve complex problems.
- **File System Operations**: 
  - **Read**: access file contents to understand the codebase.
  - **Write**: create and modify files to implement changes.
- **Shell Integration**: Execute bash commands directly to run tests, manage files, or gather system information.
- **LLM Integration**: Built to work with OpenAI-compatible APIs (configured for Anthropic models via OpenRouter).

## Prerequisites

- [Bun](https://bun.sh) runtime (v1.2+)
- An API Key (e.g., from OpenRouter)

## Setup

1.  **Clone the repository**
2.  **Install dependencies**:
    ```bash
    bun install
    ```
3.  **Configure Environment**:
    Create a `.env` file in the root directory and add your API credentials:
    ```env
    OPENROUTER_API_KEY=your_api_key_here
    OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
    ```

## Usage

Run the assistant by passing a prompt with the `-p` flag:

```bash
bun run app/main.ts -p "Read README.md and summarize its contents."
```

Or using the provided shell script:

```bash
./your_program.sh -p "Create a new file called hello.ts that prints 'Hello World'"
```

## How It Works

The assistant operates in a continuous loop:
1.  **Think**: Sends the current conversation history and available tools (Read, Write, Bash) to the LLM.
2.  **Act**: If the LLM requests a tool call, the agent parses the arguments and executes the corresponding function (file I/O or shell command).
3.  **Observe**:The tool's output is fed back into the conversation history.
4.  **Repeat**: The process continues until the LLM determines the task is complete or provides a final answer.
