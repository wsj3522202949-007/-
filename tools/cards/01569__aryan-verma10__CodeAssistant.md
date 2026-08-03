---
id: tool-01569
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: CodeAssistant
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/aryan-verma10/codeassistant
created: 2026-07-18
updated: 2026-07-18
no: 1569
category: 二、网文 / 长篇 AI 写作系统 库
repo: aryan-verma10/CodeAssistant
stars: 1
url: https://github.com/aryan-verma10/codeassistant
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# aryan-verma10/CodeAssistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/aryan-verma10/codeassistant
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：CodeAssistant is open source project helps in writing the code easily. Starting it with the basic MCP version.
- **本地描述**：CodeAssistant is open source project helps in writing the code easily. Starting it with the basic MCP version.
- **拉取时间**：2026-07-23 23:24:50

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# CodeAssistant

CodeAssistant is a lightweight AI-powered assistant that uses the Gemini API together with the Model Context Protocol (MCP) to interact with files and project resources. The current implementation focuses on a filesystem-enabled assistant that can inspect, read, write, and execute commands inside a demo workspace.

## What this project does

The assistant provides a simple command-line chat experience where you can ask for help with software projects. It can:

- understand natural-language requests
- call tools exposed by MCP servers
- inspect files and directories
- read and write files in the demo project
- run shell commands inside the workspace

This makes it useful for local development workflows such as exploring a project, reading source files, or making small edits without leaving the terminal.

## Architecture overview

The project is organized into three main parts:

- app/: the Python application layer
  - app/main.py starts the assistant and connects to MCP servers
  - app/agent.py manages the chat loop and tool execution
  - app/llm.py wraps the Gemini API and maps MCP tools into model-callable tools
  - app/prompts.py defines the system prompt for the assistant
- mcp_servers/: MCP server implementations
  - mcp_servers/file_system/ contains the working filesystem server and tool handlers
  - mcp_servers/git/, mcp_servers/postgres/, and mcp_servers/terminal/ are present as scaffolds for future expansion
- demo_project/: sample workspace used by the filesystem tools

## Current capabilities

The working MCP server currently provides these tools:

- list_directory_tool(path)
- read_file_tool(path)
- write_file_tool(path, content)
- execute_command_tool(command)

These tools are discovered by the application at startup and made available to the Gemini model during a conversation.

## Project structure

```text
.
├── app/
│   ├── agent.py
│   ├── config.py
│   ├── llm.py
│   ├── main.py
│   ├── prompts.py
│   └── mcp_client/
│       ├── client.py
│       ├── manager.py
│       └── transport.py
├── demo_project/
│   ├── backend/
│   └── frontend/
├── mcp_servers/
│   ├── file_system/
│   ├── git/
│   ├── postgres/
│   └── terminal/
└── README.md
```

## Requirements

- Python 3.10+
- A Gemini API key from Google AI Studio
- The following Python packages:
  - google-genai
  - mcp
  - python-dotenv

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install the dependencies:

```bash
pip install google-genai mcp python-dotenv
```

3. Create a .env file in the project root with your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Optional environment variables defined in app/config.py are also supported:

```env
MODEL_NAME=gemini-3.1-flash-lite
TEMPERATURE=0.1
WORKSPACE=demo_project
```

## Running the assistant

Start the CLI assistant from the project root:

```bash
python app/main.py
```

You will see a prompt like:

```text
You:
```

Example requests:

- "List the files in the demo project"
- "Read the backend main file"
- "Show the contents of the frontend chat page"
- "Write a small note into the demo workspace"

## How it works

1. app/main.py starts the assistant and connects to the filesystem MCP server.
2. The MCP manager discovers tools exposed by the server.
3. The agent sends the user request and available tool definitions to the Gemini model.
4. If the model decides it needs file or shell access, the agent executes the appropriate MCP tool and returns the result to the user.

## Security note

The execute_command_tool can run shell commands inside the workspace. Use this only in trusted environments and avoid exposing it to untrusted input.

## Current status

This repository already contains a working filesystem-based MCP integration. The git, postgres, and terminal integrations are currently scaffolded and can be expanded later for broader project automation.

## Future improvements

Possible next steps for this project include:

- adding more MCP servers for git, database, and terminal workflows
- improving error handling and tool validation
- supporting richer multi-turn interactions
- adding a web UI or API wrapper
