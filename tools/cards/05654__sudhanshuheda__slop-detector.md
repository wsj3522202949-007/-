---
id: tool-05654
type: tool
area: 库
status: active
tags: [Claude插件, 协议未明, 需API密钥, 英文文档]
title: slop-detector
summary: Claude Code 插件式写作流
source: https://github.com/sudhanshuheda/slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5654
category: 一、去 AI 味 / Humanizer 库
repo: sudhanshuheda/slop-detector
stars: 1
url: https://github.com/sudhanshuheda/slop-detector
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 42aacc52690f59d1
  - methods/改稿润色指令库.md
---

# sudhanshuheda/slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sudhanshuheda/slop-detector
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Claude Code plugin to detect AI-generated emails and label them as slop
- **本地描述**：Claude Code plugin to detect AI-generated emails and label them as slop
- **拉取时间**：2026-07-25 18:26:44

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Slop Detector

A Claude Code plugin that detects AI-generated emails and labels them as "slop" in Gmail.

Uses [Pangram Labs](https://pangram.com) for AI text detection.

## Installation

### 1. Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- Gmail account
- [Pangram Labs API key](https://pangram.com) ($5 for 100 credits to start)

### 2. Set up Gmail MCP

Add the Gmail MCP server to Claude Code:

```bash
claude mcp add gmail -- npx -y @gongrzhe/server-gmail-autoauth-mcp
```

Restart Claude Code, then authenticate with your Gmail account when prompted.

### 3. Set Pangram API Key

```bash
export PANGRAM_API_KEY=your-api-key-here
```

Add to your shell profile (`~/.zshrc` or `~/.bashrc`) for persistence:

```bash
echo 'export PANGRAM_API_KEY=your-api-key-here' >> ~/.zshrc
```

### 4. Install the Plugin

```bash
/plugin marketplace add sudhanshuheda/slop-detector
/plugin install slop-detector
```

## Usage

Scan your recent emails for AI slop:

```
/slop-detector:scan
```

This will:
1. Fetch unread emails from the last 24 hours
2. Analyze each email with Pangram Labs AI detection
3. Apply a "slop" label to emails detected as AI-generated (>70% AI score)
4. Report a summary of findings

## How It Works

The plugin sends email body text to Pangram Labs' AI detection API. Emails scoring above 70% on the `fraction_ai` metric are labeled as slop.

**Detection threshold**: 0.7 (70% AI likelihood)

## Cost

- Gmail MCP: Free (uses your Google account)
- Pangram Labs: ~1 credit per email scanned
  - $5 = 100 credits
  - $100/month = 2000 credits (Developer plan)

## Troubleshooting

### "PANGRAM_API_KEY not set"
Set the environment variable before running Claude Code:
```bash
export PANGRAM_API_KEY=your-key
claude
```

### Gmail MCP not connecting
1. Restart Claude Code after adding the MCP
2. Check MCP status: `claude mcp list`
3. Re-authenticate if needed

### False positives
The 0.7 threshold can be adjusted in the skill. Lower = more aggressive detection, higher = fewer false positives.

## License

MIT
