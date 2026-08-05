---
id: tool-05308
type: tool
area: 库
status: active
tags: [去AI味, 协议未明, 本地优先, 英文文档, 本地写作]
title: humanizer-AI-writing
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/hessevalentino/humanizer-ai-writing
created: 2026-07-18
updated: 2026-07-18
no: 5308
category: 一、去 AI 味 / Humanizer 库
repo: Hessevalentino/humanizer-AI-writing
stars: 1
url: https://github.com/hessevalentino/humanizer-ai-writing
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Hessevalentino/humanizer-AI-writing

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/hessevalentino/humanizer-ai-writing
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：ai, human, humanizer, llm, robot, writing
- **GitHub 描述**：Professional content writer and humanizer that removes AI writing patterns and creates natural, human-sounding text.  Based on Wikipedia's "Signs of AI writing" guide, maintained by WikiProject AI Cleanup.
- **本地描述**：Professional content writer and humanizer that removes AI writing patterns and creates natural, human-sounding text.  Based on Wikipedia's "Signs of AI writing" guide, maintained by WikiProject AI Cleanup.
- **拉取时间**：2026-07-25 18:13:47

---

# Humanizer for Augment CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI](https://img.shields.io/badge/AI-Powered-blue.svg)](https://github.com/topics/artificial-intelligence)
[![Augment](https://img.shields.io/badge/Augment-CLI-green.svg)](https://www.augmentcode.com/)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red.svg)](https://opensource.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

Professional content writer and humanizer that removes AI writing patterns and creates natural, human-sounding text.

Based on [Wikipedia's "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, maintained by WikiProject AI Cleanup.

## Features

- **24 AI Pattern Detection** - Identifies and removes characteristic AI writing patterns
- **Multi-language Support** - Preserves input language automatically
- **Voice & Personality** - Adds authentic human perspective, not just removes patterns
- **Machine-readable Format** - Easy to adapt for different AI models
- **Augment CLI Ready** - Optimized for Augment CLI workflow

## Quick Start

### Installation

```bash
# Copy HUMANIZER.md to your Augment skills directory
cp HUMANIZER.md ~/.augment/skills/
```

### Usage

The humanizer automatically:
1. Detects input language
2. Identifies AI patterns
3. Rewrites problematic sections
4. Adds personality and voice
5. Preserves original meaning

## What It Detects

### Content Patterns
- Significance inflation ("pivotal moment", "testament to")
- Superficial analyses with -ing endings
- Promotional language ("nestled", "vibrant", "boasts")
- Vague attributions ("experts believe", "observers note")

### Language Patterns
- Overused AI vocabulary ("additionally", "delve", "landscape")
- Copula avoidance ("serves as" instead of "is")
- Rule of three overuse
- Elegant variation (excessive synonym cycling)

### Style Patterns
- Em dash overuse
- Emoji in headings
- Title Case headings
- Boldface overuse

### Communication Patterns
- Chatbot artifacts ("I hope this helps!")
- Knowledge-cutoff disclaimers
- Sycophantic tone

## Example

**Before (AI-sounding):**
> AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development...

**After (Humanized):**
> AI coding assistants speed up some tasks. In a 2024 study by Google, developers using Codex completed simple functions 55% faster than a control group, but showed no improvement on debugging...

## Key Insight

> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."
> 
> — Wikipedia: Signs of AI writing

## Adaptability

This humanizer is in machine-readable format (Markdown), making it:
- **Portable** - Works with various AI models (Claude, GPT, Gemini, local models)
- **Customizable** - Easy to modify for specific needs
- **Transparent** - All patterns documented and explained

## Credits

- Original concept: [blader/humanizer](https://github.com/blader/humanizer)
- Based on: [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Adapted for: Augment CLI

## License

MIT License - see `[LICENSE](LICENSE)` file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Links

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup)
- [Original Humanizer](https://github.com/blader/humanizer)
- [Augment Code](https://www.augmentcode.com/)

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

Made with ❤️ for better AI-human collaboration

