---
id: tool-05264
type: tool
area: 库
status: active
tags: [Claude插件, JavaScript, 协议宽松, 需API密钥, 英文文档]
title: chief-editor-mcp
summary: Claude Code 插件式写作流
source: https://github.com/quickminds-be/chief-editor-mcp
created: 2026-07-18
updated: 2026-07-18
no: 5264
category: 一、去 AI 味 / Humanizer 库
repo: quickminds-be/chief-editor-mcp
stars: 0
url: https://github.com/quickminds-be/chief-editor-mcp
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 414ba6bd6e688a38
  - methods/改稿润色指令库.md
---

# quickminds-be/chief-editor-mcp

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/quickminds-be/chief-editor-mcp
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：ai-detection, claude, llm-detection, mcp, mcp-server, model-context-protocol, slop-detector, text-analysis, writing-analysis, x402
- **GitHub 描述**：MCP server for the Chief Editor AI slop detector — analyses text for AI-generated writing patterns
- **本地描述**：MCP server for the Chief Editor AI slop detector — analyses text for AI-generated writing patterns
- **拉取时间**：2026-07-25 18:12:08

---

# chief-editor-mcp

MCP server for the [Chief Editor](https://api.reviewsandnotes.com) AI slop detector. Analyses text for AI-generated writing patterns and returns three scored dimensions — sloppiness, originality, and hype — with per-pattern annotations.

## Tools

### `analyze_text`

Analyse text for AI-generated writing patterns. Returns:

- **sloppiness** (0–1): structural LLM tells, filler phrases, robotic pacing, punctuation overuse → `clean` / `sloppy` / `ai_slop`
- **originality** (0–1): cliché density relative to word count → `original` / `bland` / `generic`
- **hype** (0–1): superlative/intensifier density → `grounded` / `salesy` / `overblown`
- **flags**: per-pattern detections with positions, matched text, rule IDs, and reasons
- **meta**: pacing, em-dash density, semicolon density, superlative density, cliché density labels

### `get_price`

Get the cost to analyse a text before paying. Free, no authentication required.

| Tier   | Words    | Price  |
|--------|----------|--------|
| small  | 0–100    | $0.02  |
| medium | 101–500  | $0.04  |
| large  | 501–2000 | $0.08  |

## Setup

### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "chief-editor": {
      "command": "npx",
      "args": ["-y", "chief-editor-mcp"],
      "env": {
        "CHIEF_EDITOR_API_KEY": "your-api-key"
      }
    }
  }
}
```

### Claude Code

```bash
claude mcp add chief-editor -- npx -y chief-editor-mcp
```

### Environment variables

| Variable | Default | Description |
|----------|---------|----------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| `CHIEF_EDITOR_API_KEY` | — | API key (bypasses x402 payment) |
| `CHIEF_EDITOR_URL` | `https://api.reviewsandnotes.com` | API base URL |

## API

Full OpenAPI spec: https://api.reviewsandnotes.com/openapi.yaml

Machine-readable description: https://api.reviewsandnotes.com/.well-known/llms.txt

## License

MIT
