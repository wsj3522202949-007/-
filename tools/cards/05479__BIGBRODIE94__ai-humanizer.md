---
id: tool-05479
type: tool
area: 库
status: active
tags: [去AI味, TypeScript, 协议未明, 需API密钥, 英文文档]
title: ai-humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/bigbrodie94/ai-humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5479
category: 一、去 AI 味 / Humanizer 库
repo: BIGBRODIE94/ai-humanizer
stars: 2
url: https://github.com/bigbrodie94/ai-humanizer
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# BIGBRODIE94/ai-humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/bigbrodie94/ai-humanizer
- **Stars**：2
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Advanced AI Text Detection & Humanization CLI - 6-layer detection engine with Shannon entropy, TF-IDF similarity, Zipf's law analysis, and multi-LLM humanization
- **本地描述**：Advanced AI Text Detection & Humanization CLI - 6-layer detection engine with Shannon entropy, TF-IDF similarity, Zipf's law analysis, and multi-LLM humanization
- **拉取时间**：2026-07-25 18:20:13

---

# AI Humanizer

Advanced CLI tool for detecting AI-generated text and rewriting it to be 100% undetectable. Uses multi-layer analysis (statistical + pattern recognition + LLM verification) and multi-pass humanization with support for OpenAI, Anthropic, and Google Gemini.

## Quick Start

```bash
# Install dependencies
npm install

# Configure API keys (at least one required for humanization)
cp .env.example .env
# Edit .env with your API keys

# Run detection (local analysis — no API key needed)
npx tsx src/index.ts detect --local "Your text here"

# Run humanization (requires API key)
npx tsx src/index.ts humanize "Your text here" --style casual

# Launch interactive mode
npx tsx src/index.ts interactive
```

## Commands

### `detect` — AI Text Detection

Analyzes text with a 3-layer scoring system and returns an AI probability score (0-100%).

```bash
# Detect from inline text (local analysis only)
ai-humanizer detect --local "In today's rapidly evolving landscape..."

# Detect from file with LLM verification
ai-humanizer detect -f essay.txt

# Use a specific provider
ai-humanizer detect -f essay.txt -p anthropic
```

### `humanize` — Text Humanization

Rewrites AI-generated text through a multi-pass pipeline to make it undetectable.

```bash
# Humanize inline text
ai-humanizer humanize "AI text here" --style casual

# Humanize a file (saves to essay-humanized.txt)
ai-humanizer humanize -f essay.txt --style academic

# Custom output path, provider, and passes
ai-humanizer humanize -f essay.txt -o output.txt -p openai --passes 5 --target 15
```

**Styles:** `casual`, `academic`, `professional`, `student`

### `batch` — Batch Processing

Process multiple text files in a directory.

```bash
# Detect AI in all text files
ai-humanizer batch ./essays/ --mode detect --local

# Humanize all .txt files
ai-humanizer batch ./essays/ --mode humanize --pattern "*.txt" --style professional
```

### `interactive` — Guided Mode

Step-by-step guided interface with prompts for all options.

```bash
ai-humanizer interactive
# or
ai-humanizer i
```

### `config` — Configuration

```bash
# Show current config
ai-humanizer config --show

# Interactive config setup
ai-humanizer config

# Reset to defaults
ai-humanizer config --reset
```

## Detection Engine

Three scoring layers combined with weighted averaging:

| Layer | Weight (with LLM) | Weight (local only) | What it measures |
|-------|-------------------|---------------------|------------------|
| Statistical Analysis | 30% | 50% | Perplexity, burstiness, vocabulary richness, repetition density |
| Pattern Recognition | 30% | 50% | Hedging phrases, transition overuse, structure uniformity, passive voice, AI clichés |
| LLM Verification | 40% | — | Cross-LLM analysis with specialized detection prompts |

An additional linguistic adjustment (contractions, first-person usage, readability) shifts the score ±20 points.

## Humanization Pipeline

1. **Local Pre-processing** — Replaces 50+ AI-giveaway words/phrases with natural alternatives
2. **Structure Breaking** — Varies sentence/paragraph lengths, merges/splits sentences
3. **Style Rewriting** — Rewrites in a specific human archetype (casual, academic, etc.)
4. **Imperfection Layer** — Adds natural quirks: contractions, asides, varied punctuation
5. **Verification Loop** — Re-checks AI score and iterates until below target threshold

## API Keys

Set via environment variables (`.env` file) or through `ai-humanizer config`:

| Provider | Variable | Models |
|----------|----------|-----related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| OpenAI | `OPENAI_API_KEY` | gpt-4o, gpt-4o-mini |
| Anthropic | `ANTHROPIC_API_KEY` | claude-sonnet, claude-haiku |
| Google | `GOOGLE_API_KEY` | gemini-1.5-pro, gemini-1.5-flash |

Detection works locally without any API keys. Humanization requires at least one configured provider.

## Development

```bash
npm run dev           # Run with tsx (development)
npm run typecheck     # TypeScript type checking
npm run build         # Build for production with tsup
```
