---
id: tool-01183
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ai-coding-agent
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/antonia225/ai-coding-agent
created: 2026-07-18
updated: 2026-07-18
no: 1183
category: 二、网文 / 长篇 AI 写作系统 库
repo: antonia225/ai-coding-agent
stars: 0
url: https://github.com/antonia225/ai-coding-agent
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 691688c67f1c9b4b
  - methods/最强写作方法论_全球最强综合版.md
---

# antonia225/ai-coding-agent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/antonia225/ai-coding-agent
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI coding assistant powered by Claude via OpenRouter, with tool calling for reading/writing files and running shell commands.
- **本地描述**：AI coding assistant powered by Claude via OpenRouter, with tool calling for reading/writing files and running shell commands.
- **拉取时间**：2026-07-23 23:13:32

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Coding Agent

An AI-powered coding assistant that leverages Large Language Models (LLMs) to understand code and execute actions through intelligent tool calling. Built with OpenAI-compatible APIs and featuring a robust agent loop architecture.

## Features

- **LLM Integration**: Powered by Claude Haiku 4.5 via OpenRouter API
- **Tool Execution**: Read files, write files, and execute shell commands
- **Agent Loop**: Iterative processing with multi-tool coordination
- **Error Handling**: Graceful error handling and recovery
- **Logging**: Comprehensive logging for debugging and monitoring
- **Type Safe**: Full type hints throughout the codebase

## Architecture

```
app/
├── __init__.py       # Package initialization
├── main.py           # CLI entry point and argument parsing
├── agent.py          # Agent loop implementation
├── tools.py          # Tool definitions and handlers
└── config.py         # Configuration and constants
```

### Components

- **Agent**: Main orchestrator that manages the conversation loop with the LLM
- **Tools**: Expandable tool system supporting file operations and shell commands
- **Config**: Centralized configuration management for API keys and model selection

## Prerequisites

- Python >= 3.14
- OpenRouter API key

## Installation

1. Set up Python environment:
```sh
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```sh
pip install -r requirements.txt
# or with uv:
uv pip install -r requirements.txt
```

3. Set up environment variables:
```sh
export OPENROUTER_API_KEY="your-api-key-here"
# Optionally set custom base URL:
export OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
```

## Usage

Run the assistant with a prompt:

```sh
python app/main.py -p "Create a Python script that prints hello world"
```

Or use the provided shell script:

```sh
./your_program.sh -p "Your prompt here"
```

### Examples

**Read a file:**
```sh
python app/main.py -p "Read the contents of README.md"
```

**Write code:**
```sh
python app/main.py -p "Create a new Python file called test.py with a simple function"
```

**Execute commands:**
```sh
python app/main.py -p "Run 'ls -la' and tell me what files are in the current directory"
```

## Development

### Running tests:
```sh
pytest tests/
```

### Linting and formatting:
```sh
flake8 app/
mypy app/
```

### Enable debug logging:
```sh
LOGLEVEL=DEBUG python app/main.py -p "Your prompt"
```

## API Integration

This project uses the OpenAI-compatible API format (OpenRouter). The implementation supports:

- **Tool Calling**: LLM-driven function invocation
- **Streaming**: Compatible with streaming responses
- **Error Recovery**: Automatic retry and error handling

## Available Tools

1. **Read**: Read file contents
   - Parameter: `file_path` (string)

2. **Write**: Write content to a file
   - Parameters: `file_path` (string), `content` (string)

3. **Bash**: Execute shell commands
   - Parameter: `command` (string)

## Performance Considerations

- API calls are synchronous and blocking
- Large file operations may impact performance
- Shell command execution has security implications (see Security section)

## Security

⚠️ **Important**: This is a demonstration project. In production:

- Implement command sandboxing for shell execution
- Validate file paths to prevent directory traversal
- Use principle of least privilege for file operations
- Add rate limiting and usage monitoring
- Implement audit logging for sensitive operations

## Error Handling

The application includes comprehensive error handling:

- Missing or invalid API keys are detected on startup
- File operation errors are caught and reported
- Command execution errors are logged and returned to the LLM
- API failures trigger appropriate error messages

## Troubleshooting

**"OPENROUTER_API_KEY is not set"**
- Ensure you've set the environment variable: `export OPENROUTER_API_KEY="your-key"`

**Connection errors**
- Verify your API key is valid
- Check your internet connection
- Ensure OpenRouter service is accessible

**File operation fails**
- Check file paths are accessible
- Ensure proper read/write permissions

## Acknowledgments

- [CodeCrafters](https://codecrafters.io) - Challenge inspiration
- [OpenRouter](https://openrouter.ai) - API provider
- [OpenAI Python SDK](https://github.com/openai/openai-python)

## Resources

- [OpenRouter API Documentation](https://openrouter.ai/docs)
- [OpenAI Tool Use Guide](https://platform.openai.com/docs/guides/function-calling)
- [Agent Design Patterns](https://python.langchain.com/docs/modules/agents/)
