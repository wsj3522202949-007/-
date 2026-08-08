---
id: tool-01634
type: tool
area: 库
status: active
tags: [Go, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: clio
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/julien-jungo/clio
created: 2026-07-18
updated: 2026-07-18
no: 1634
category: 二、网文 / 长篇 AI 写作系统 库
repo: julien-jungo/clio
stars: 0
url: https://github.com/julien-jungo/clio
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
content_hash: ee4690f0a62ab6bc
  - methods/最强写作方法论_全球最强综合版.md
---

# julien-jungo/clio

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/julien-jungo/clio
- **Stars**：0
- **语言**：Go
- **License**：None
- **Topics**：—
- **GitHub 描述**：A terminal-based coding assistant built in Go, backed by an LLM with tool use capable of reading and writing files, running shell commands, and helping with coding tasks.
- **本地描述**：A terminal-based coding assistant built in Go, backed by an LLM with tool use capable of reading and writing files, running shell commands, and helping with coding tasks.
- **拉取时间**：2026-07-23 23:26:41

---

# clio

A terminal-based coding assistant built in Go. Clio provides an interactive chat UI right in your terminal, backed by an LLM with tool use via OpenRouter. It can read and write files, execute shell commands, and iterate on code — acting as a pair programmer that lives in your terminal.

<img src="assets/screenshot.png" alt="screenshot" width="600">

## Setup

```sh
export OPENROUTER_API_KEY="your-key-here"
```

## Usage

```sh
go run ./app
```

Type a message and press Enter to chat. Ctrl+C to quit.

## Configuration

| Variable              | Default                        | Description             |
|-----------------------|--------------------------------|-------------------------|
| `OPENROUTER_API_KEY`  | *(required)*                   | Your OpenRouter API key |
| `OPENROUTER_BASE_URL` | `https://openrouter.ai/api/v1` | API base URL            |
| `CLIO_MODEL`          | `anthropic/claude-haiku-4.5`   | Model to use            |

## Tools

| Tool  | Description                           |
|-------|------------------------------------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Read  | Read file contents                    |
| Write | Write content to a file               |
| Bash  | Execute a shell command (30s timeout) |
