---
id: tool-05303
type: tool
area: 库
status: active
tags: [Claude插件, TypeScript, 协议宽松, 本地优先, 英文文档, 本地写作]
title: slop-detector
summary: Claude Code 插件式写作流
source: https://github.com/cyranob/slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5303
category: 一、去 AI 味 / Humanizer 库
repo: CyranoB/slop-detector
stars: 1
url: https://github.com/cyranob/slop-detector
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# CyranoB/slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/cyranob/slop-detector
- **Stars**：1
- **语言**：TypeScript
- **License**：MIT
- **Topics**：ai, llm, nlp, slop
- **GitHub 描述**：Detect AI-like writing patterns in creative prose. Returns a 0-100 score where higher = more AI-like.
- **本地描述**：Detect AI-like writing patterns in creative prose. Returns a 0-100 score where higher = more AI-like.
- **拉取时间**：2026-07-25 18:13:35

---

# SLOP Detector

!`[SLOP Detector](assets/header.png)`

> “The SLOP Meter doesn’t measure truth or beauty. It measures how loudly your sentences clap for themselves. When the needle bursts through the dial and a small goblin emerges to applaud, you are probably no longer writing—you are performing.”

Detect AI-like writing patterns in creative prose. Returns a 0-100 score where higher = more AI-like.

SLOP Detector is inspired by the original slop-score project and is designed for creative writing analysis, not as a general-purpose AI detection system. It currently supports English text only.

## Quick Start

```bash
npx -y slop-detector
```

This starts an MCP server. Add it to your AI assistant:

**Claude Code:**
```bash
claude mcp add slop-detector -- npx -y slop-detector
```

**Codex:**
```bash
codex mcp add slop-detector -- npx -y slop-detector
```

**Claude Desktop** (`~/Library/Application Support/Claude/claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "slop-detector": {
      "command": "npx",
      "args": ["-y", "slop-detector"]
    }
  }
}
```

## What It Detects

| Component | Weight | What it finds |
|-----------|--------|---------------|
| **Slop Words** | 60% | Overused words like *delve*, *tapestry*, *paradigm*, *leverage* |
| **Contrast Patterns** | 25% | "Not X but Y" structures that LLMs love |
| **Trigrams** | 15% | Common 3-word phrases like "it is important" |

## Score Interpretation

| Score | Meaning |
|-------|------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 0-20 | Human-like writing |
| 20-40 | Mostly human, some AI patterns |
| 40-60 | Mixed, unclear origin |
| 60-80 | Likely AI-generated |
| 80-100 | Strong AI signature |

> **Rule of thumb:** Scores above 30 are suspicious.

## Usage

### As an MCP Tool

The `score_text` tool accepts text and returns:
- `slopScore`: 0-100 score
- `wordCount`, `charCount`: Text statistics  
- `metrics`: Detailed breakdown (words/trigrams/patterns per 1k)

### Command Line

```bash
# Install and build
npm install && npm run build

# Score a file
node dist/cli.js article.txt

# Score from stdin
echo "Let's delve into this tapestry of ideas" | node dist/cli.js -
pbpaste | node dist/cli.js -   # macOS clipboard
```

### As a Library

```typescript
import { slopScoreService } from 'slop-detector';

const result = await slopScoreService.computeScoreFromText(text, 'en');
console.log(result.slopScore); // 42.5
```

## Example Output

```
=== SLOP Score Analysis ===

Final Score: 67.3/100
Word Count: 342

Top Slop Words:
  "delve": 3×
  "tapestry": 2×

Contrast Patterns Found:
  "not just a product but a comprehensive solution"

Interpretation: Likely AI-generated with some editing
```

## How It Works

See **`[docs/IMPLEMENTATION.md](docs/IMPLEMENTATION.md)`** for:
- Detailed algorithm explanation
- Project structure
- How to add custom patterns

## Development

```bash
npm install          # Install dependencies
npm run build        # Compile TypeScript
npm test             # Run tests
npm run mcp          # Start MCP server locally
```

## Requirements

- Node.js 18+

## License

MIT

## Credits

Based on [slop-score](https://github.com/sam-paech/slop-score) by Samuel J. Paech and the [EQBench](https://eqbench.com/slop-score.html) methodology.
