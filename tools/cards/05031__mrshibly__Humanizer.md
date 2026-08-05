---
id: tool-05031
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, 协议宽松, 需API密钥, 英文文档]
title: Humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/mrshibly/humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5031
category: 一、去 AI 味 / Humanizer 库
repo: mrshibly/Humanizer
stars: 1
url: https://github.com/mrshibly/humanizer
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# mrshibly/Humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/mrshibly/humanizer
- **Stars**：1
- **语言**：None
- **License**：MIT
- **Topics**：agent-skills, ai-humanizer, anti-ai-detection, antigravity-skills, claude-code, claude-skills, cursor-skills, humanizer, opencode, prompt-engineering, writing-assistant
- **GitHub 描述**：The most advanced AI text humanization framework. 45+ patterns, perplexity/burstiness engineering, and multi-pass self-audit pipeline for Claude Code, OpenCode, and LLMs.
- **本地描述**：The most advanced AI text humanization framework. 45+ patterns, perplexity/burstiness engineering, and multi-pass self-audit pipeline for Claude Code, OpenCode, and LLMs.
- **拉取时间**：2026-07-25 18:03:34

---

!`[Humanizer Pro Banner](banner.png)`

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/mrshibly/humanizer.svg?style=social)](https://github.com/mrshibly/humanizer)
[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](SKILL.md)

**The most advanced AI text humanization framework for LLMs.** 

Humanizer Pro is a sophisticated engine designed to transform AI-generated text into natural, nuanced, and truly human-like prose. Unlike simple word-replacers, this framework utilizes **Perplexity & Burstiness Engineering** to systematically dismantle the statistical signatures that AI detectors (GPTZero, Originality.ai) use to flag machine-generated content.

---

## 🚀 Why Humanizer Pro?

AI detectors don't just look for buzzwords; they look for **predictability**. Humanizer Pro targets the "statistical soul" of AI writing across 45 distinct patterns.

| Feature | Standard AI | Humanizer Pro |
| :--- | :--- | :--- |
| **Patterns** | Repetitive, "tidy" | 45+ organic patterns |
| **Vocabulary** | *Delve, Tapestry, Pivotal* | Diverse, context-aware |
| **Rhythm** | Uniform sentence length | High Burstiness (varied) |
| **Logic** | Predictable "Rule of Three" | Messy, opinionated, real |
| **Detection** | Easily flagged (0% human) | Bypasses advanced detectors |

---

## 🛠️ Installation

### For [Claude Code](https://github.com/anthropic/claude-code)
Clone directly into your skills directory:
```bash
mkdir -p ~/.claude/skills
git clone https://github.com/mrshibly/humanizer.git ~/.claude/skills/humanizer
```

### For [OpenCode](https://github.com/opencode/opencode)
```bash
mkdir -p ~/.config/opencode/skills
git clone https://github.com/mrshibly/humanizer.git ~/.config/opencode/skills/humanizer
```

### For Manual Use
Simply copy the contents of `[SKILL.md](SKILL.md)` into your system prompt or custom instructions.

---

## 🧠 Core Methodology: The 8-Step Pipeline

1.  **Pattern Scan:** Identifies 45 common "AI markers."
2.  **Lexical De-Smoothing:** Replaces statistically predictable "AI-isms."
3.  **Burstiness Injection:** Randomizes sentence length and structure.
4.  **Perplexity Engineering:** Introduces "surprising" but accurate word choices.
5.  **Domain Calibration:** Adjusts tone for Academic, Tech, Marketing, or Casual modes.
6.  **Cognitive Fingerprinting:** Adds human-like thought pivots and self-corrections.
7.  **AI Audit:** A self-reflective pass to find remaining "machine smells."
8.  **Final Polish:** A read-aloud consistency check.

---

## 📖 Domain Modes

Humanizer Pro adapts its "messiness" based on your target audience:

*   🎓 **Academic:** Formal but not sterile. Replaces vague puffery with specific data.
*   💻 **Technical:** Concise, opinionated, and jargon-aware. Skip the fluff.
*   📣 **Marketing:** Persuasive through stories and facts, not buzzwords.
*   ☕ **Casual:** First-person, personality-forward, and intentionally "imperfect."
*   📧 **Professional:** Direct and action-oriented. No canned politeness.

---

## 🤝 Contributing

We are building the definitive library for human-AI collaboration. If you find a new AI "tell," please open a PR!

1.  Add the pattern to `SKILL.md`.
2.  Provide a before/after example in `examples/comparisons.md`.
3.  Submit your PR for review.

## 📜 License

MIT License. See `[LICENSE](LICENSE)` for details.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

*Based on research from [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) and 2026 AI detection benchmarks.*
