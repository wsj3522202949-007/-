---
id: tool-01319
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: air
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ai-zen/air
created: 2026-07-18
updated: 2026-07-18
no: 1319
category: 二、网文 / 长篇 AI 写作系统 库
repo: ai-zen/air
stars: 0
url: https://github.com/ai-zen/air
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ai-zen/air

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ai-zen/air
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Do 99% of things with 1% of the features.  A minimalist AI CLI assistant. Just one shell tool — the AI remembers things by writing to the filesystem, and automatically migrates context when it gets too long.
- **本地描述**：Do 99% of things with 1% of the features.  A minimalist AI CLI assistant. Just one shell tool — the AI remembers things by writing to the filesystem, and automatically migrates context when it gets too long.
- **拉取时间**：2026-07-23 23:17:35

---

# air

> Do 99% of things with 1% of the features.

A minimalist AI CLI assistant. Just one shell tool — the AI remembers things by writing to the filesystem, and automatically migrates context when it gets too long.

## Installation

```bash
# Global install (recommended)
npm install -g @ai-zen/air

# Or build from source
git clone git@github.com:ai-zen/air.git
cd air
npm install
npm run build
npm install -g .
```

## Usage

```bash
# Set API Key (DeepSeek)
air key sk-xxxxxxxxxxxxxxxx

# Interactive mode (auto-resumes last conversation)
air

# One-shot message
air use shell to list files in current directory

# View config
air config

# Install fallback hook (redirects unknown commands to air)
air hook install

# Uninstall fallback hook
air hook uninstall
```

### Interactive Commands

| Command | Description |
|---------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `/exit` `/quit` | Exit |
| `/save` | Save snapshot |
| `/load` | Load snapshot |
| `/new` | Clear context and start fresh |
| `/back` | Recall a message (optionally edit and resend) |
| `/editor` | Open system editor for multi-line input |
| `/help` | Help |

### Fallback Terminal Hook

When installed, any command that doesn't exist in your shell gets automatically forwarded to `air`. The AI will interpret what you meant and help you out.

```bash
$ gred "hello" file.txt
# → command not found → auto-redirects to air
# → AI: "Did you mean grep?"
```

## Design

```
~/.ai-zen/air/
├── config.json       # { "apiKey": "sk-xxx" }
├── context.json      # [ { role, content }, ... ]    Current conversation
├── snapshots/        # Auto snapshots before migration or /save
└── memory/           # Long-term memory written by AI (*.md)
```

### Core Philosophy

- **Model**: DeepSeek-V4-Flash (hardcoded, only one)
- **Tool**: Just one `shell` tool — the AI executes commands, reads and writes files through it
- **Memory**: The AI decides what to remember, writes to `memory/*.md` via shell, reads on next startup. No extra persistence mechanism
- **Context**: Auto-migrates when JSON serialization exceeds 500K chars, takes a snapshot before migration
- **Rules**: Consult the user before making changes. Dangerous operations require explicit written confirmation. The user takes responsibility for their own instructions

## Project Structure

```
src/
├── cli.ts                # CLI entry, commander
├── config.ts             # Config, context, snapshot read/write
├── delta-renderer.ts     # Stream renderer
├── hook.ts               # Fallback terminal hook (install/uninstall)
├── migration.ts          # Context counting & migration
├── tools.ts              # Tool definitions — shell
├── agent-factory.ts      # Agent factory — build model & agent
├── agent-runtime.ts      # Core runtime — send, chat loop
├── agent-types.ts        # Type definitions (ChatCtx, etc.)
├── agent-constants.ts    # System prompt & constants
├── agent-commands/       # Interactive command handlers
│   ├── index.ts          # dispatchCommand() — command router
│   ├── back.ts           # /back — recall & resend
│   ├── editor.ts         # /editor — multi-line input
│   ├── exit.ts           # /exit — quit
│   ├── help.ts           # /help
│   ├── load.ts           # /load — load snapshot
│   ├── new.ts            # /new — new session
│   └── save.ts           # /save — save snapshot
└── __tests__/
    ├── chat.test.ts      # Chat session tests
    ├── config.test.ts    # Config/context/snapshot tests
    ├── main.test.ts      # contextSize/shouldMigrate tests
    ├── e2e.test.ts       # End-to-end tests
    └── tools.test.ts     # Shell tool structure tests
```

~76 KB, 879 lines (excluding tests).

## Tests

```bash
npm test
```
