---
id: tool-05297
type: tool
area: 库
status: active
tags: [Claude插件, Shell, 协议宽松, 本地优先, 英文文档, 本地写作]
title: claude-slop-detector
summary: Claude Code 插件式写作流
source: https://github.com/aplaceforallmystuff/claude-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5297
category: 一、去 AI 味 / Humanizer 库
repo: aplaceforallmystuff/claude-slop-detector
stars: 7
url: https://github.com/aplaceforallmystuff/claude-slop-detector
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# aplaceforallmystuff/claude-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/aplaceforallmystuff/claude-slop-detector
- **Stars**：7
- **语言**：Shell
- **License**：MIT
- **Topics**：ai-detection, ai-writing, claude, claude-code, content-quality, slop-detection, writing-tools
- **GitHub 描述**：Claude Code skill for detecting AI-generated writing patterns (slop) in content
- **本地描述**：Claude Code skill for detecting AI-generated writing patterns (slop) in content
- **拉取时间**：2026-07-25 18:13:22

---

# Claude Slop Detector

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-blue)](https://claude.ai)

A Claude Code skill for detecting AI-generated writing patterns ("slop") in content.

## What is "Slop"?

AI slop is content that sounds generically AI-generated — the kind of writing that could be sent to anyone in your industry without modification. It's characterized by:

- Overused phrases like "delve into," "game-changer," and "it's worth noting"
- Uniform sentence lengths (every sentence 10-15 words)
- Staccato fragment spam (short. punchy. sentences. everywhere.)
- Over-balanced sections with diplomatic hedging
- Manufactured enthusiasm and fake personality

This skill helps you identify these patterns and fix them.

## Installation

### Option 1: Skills CLI

```bash
npx skills add aplaceforallmystuff/claude-slop-detector
```

### Option 2: Copy to your Claude Code skills directory

```bash
# Clone the repository
git clone https://github.com/aplaceforallmystuff/claude-slop-detector.git

# Copy to your Claude Code skills directory
cp -r claude-slop-detector/skills/slop-detector ~/.claude/skills/
```

### Option 3: Clone directly to skills directory

```bash
git clone https://github.com/aplaceforallmystuff/claude-slop-detector.git ~/.claude/skills/slop-detector
```

### Option 4: Manual installation

1. Create the directory: `mkdir -p ~/.claude/skills/slop-detector`
2. Download `[SKILL.md](skills/slop-detector/SKILL.md)` to that directory

## Usage

Once installed, the skill activates when you ask Claude Code to:

- "Check this draft for AI slop"
- "Audit this content for AI patterns"
- "Run slop detection on this file"
- "Is this writing too AI-sounding?"

### Example

```
> Check this draft for slop: "In today's digital landscape, it's worth noting
  that AI has become a game-changer for content creation. Let's delve into
  how you can leverage these cutting-edge solutions to unlock your potential."
```

Output:
```
## Slop Detection Report

**30-Second Test:** FAIL - could be sent to anyone
**Overall Slop Score:** 21 - High Risk

### Tier 1 Findings (Remove Immediately)
- "delve into" - Replace with: examine, explore, look at
- "game-changer" - Replace with: specific impact description
- "it's worth noting" - Remove entirely
- "cutting-edge solutions" - Replace with: specific tools/methods
- "unlock your potential" - Replace with: specific outcome
...
```

## How It Works

The skill uses a tiered detection system:

### Tier 1: Almost Always AI (Remove Immediately)
Phrases so strongly associated with AI that their presence alone suggests unedited output:
- "delve into" / "delve"
- "game-changing" / "revolutionary"
- "it's worth noting that"
- "moreover" / "furthermore"
- "unlock your potential"
- "cutting-edge solutions"

Research shows "delve" usage increased 10.45x post-ChatGPT (Finnish study, 56,878 essays).

### Tier 2: Suspicious (Check Context)
Problematic when overused or clustered:
- "here's the thing" (repeated)
- "at the end of the day"
- "comprehensive and thorough"
- "let's dive in"

### Tier 3: Watch for Patterns
Fine individually, problematic in clusters:
- "however" starting every paragraph
- "firstly," "secondly," "thirdly"
- "robust," "seamless," "scalable" together

### Structural Tells
Beyond phrases, the skill detects:
- **Sentence uniformity** - all sentences same length
- **Staccato fragment spam** - "Short. Punchy. Sentences."
- **Over-balanced sections** - diplomatic hedging everywhere
- **List addiction** - bullets where prose works better
- **Manufactured personality** - fake developer voice

## Slop Score

The skill calculates a numerical score:

| Score | Risk Level | Interpretation |
|-------|------------|----------------|
| 0-5 | Low | Minor edits needed |
| 6-12 | Medium | Significant editing required |
| 13+ | High | Likely unedited AI output |

## The 30-Second Test

The fastest way to identify AI slop:

> "Could this exact content be sent to anyone in my industry?"

If yes, it's slop. Specificity separates genuine insight from generic templates.

## License

MIT License - see `[LICENSE](LICENSE)`

## Acknowledgments

Detection patterns informed by:
- Finnish study on post-ChatGPT writing changes (56,878 essays)
- Georgia Tech analysis of 168.3M academic articles
- Biomedical literature analysis of AI marker co-occurrence

## Related Skills

Part of the [aplaceforallmystuff](https://skills.sh/aplaceforallmystuff) skills collection:

- **[the-antislop](https://github.com/aplaceforallmystuff/the-antislop)** — More comprehensive detection + editor mode (35+ patterns)
- **[voice-analyzer](https://github.com/aplaceforallmystuff/claude-voice-analyzer)** — Create a voice profile from your writing samples
- **[voice-editor](https://github.com/aplaceforallmystuff/claude-voice-editor)** — Edit content to match your voice profile

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

**The goal isn't perfect avoidance of any single phrase — it's writing that sounds like a specific human with specific opinions, not a very polite committee trying not to offend anyone.**
