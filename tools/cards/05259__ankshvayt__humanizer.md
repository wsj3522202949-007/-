---
id: tool-05259
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, 协议未明, 需API密钥, 英文文档]
title: humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/ankshvayt/humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5259
category: 一、去 AI 味 / Humanizer 库
repo: ankshvayt/humanizer
stars: 1
url: https://github.com/ankshvayt/humanizer
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 3d1b3587c3791deb
  - methods/改稿润色指令库.md
---

# ankshvayt/humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ankshvayt/humanizer
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Prompt-based skill that removes signs of AI-generated writing. Works with any LLM — ChatGPT, Claude, Gemini, Cursor, Copilot, etc.
- **本地描述**：Prompt-based skill that removes signs of AI-generated writing. Works with any LLM — ChatGPT, Claude, Gemini, Cursor, Copilot, etc.
- **拉取时间**：2026-07-25 18:11:57

---

# Humanizer

A prompt-based skill that removes signs of AI-generated writing from text, making it sound more natural and human. Works with any LLM or AI assistant.

## Compatibility

The core artifact is `SKILL.md` -- a self-contained instruction set that any AI model can follow. No code, no dependencies, just a markdown file you feed to your tool of choice.

| Platform | How it works |
|----------|-------------|
| Claude Code | Install as a skill (reads `SKILL.md` automatically) |
| Cursor / Windsurf | Add as a skill or rule file |
| ChatGPT | Paste into Custom Instructions or a GPT's system prompt |
| Gemini | Paste into system instructions |
| Copilot Chat | Paste as context or use as a prompt file |
| Any LLM API | Include as a system message |

## Installation

### Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/ankshvayt/humanizer.git ~/.claude/skills/humanizer
```

Or copy just the skill file:

```bash
mkdir -p ~/.claude/skills/humanizer
cp SKILL.md ~/.claude/skills/humanizer/
```

### Cursor

Copy `SKILL.md` into your Cursor skills directory:

```bash
mkdir -p ~/.cursor/skills/humanizer
cp SKILL.md ~/.cursor/skills/humanizer/
```

Or add it as a project-level rule in `.cursor/rules/`.

### ChatGPT / Custom GPTs

1. Open ChatGPT settings (or create/edit a GPT)
2. Paste the contents of `SKILL.md` into the **Custom Instructions** or **System Prompt** field
3. Start a conversation and ask it to humanize your text

### Gemini

1. Open Google AI Studio or Gemini API settings
2. Paste the contents of `SKILL.md` into the **System Instructions** field
3. Provide text to humanize in your message

### Any LLM API (OpenAI, Anthropic, etc.)

Include the contents of `SKILL.md` as the system message in your API call:

```python
with open("SKILL.md") as f:
    system_prompt = f.read()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Humanize this text: ..."}
    ]
)
```

## Usage

However you've loaded the skill, just give the AI text and ask it to humanize:

```
Humanize this text:

[paste your text here]
```

The skill instructs the AI to:
1. Draft a rewrite removing AI patterns
2. Self-audit with "What makes the below so obviously AI generated?"
3. Produce a final version after the audit

## Overview

Based on [Wikipedia's "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, maintained by WikiProject AI Cleanup. This comes from observations of thousands of instances of AI-generated text.

### Key insight from Wikipedia

> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

## 24 Patterns detected (with before/after examples)

### Content patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 1 | **Significance inflation** | "marking a pivotal moment in the evolution of..." | "was established in 1989 to collect regional statistics" |
| 2 | **Notability name-dropping** | "cited in NYT, BBC, FT, and The Hindu" | "In a 2024 NYT interview, she argued..." |
| 3 | **Superficial -ing analyses** | "symbolizing... reflecting... showcasing..." | Remove or expand with actual sources |
| 4 | **Promotional language** | "nestled within the breathtaking region" | "is a town in the Gonder region" |
| 5 | **Vague attributions** | "Experts believe it plays a crucial role" | "according to a 2019 survey by..." |
| 6 | **Formulaic challenges** | "Despite challenges... continues to thrive" | Specific facts about actual challenges |

### Language patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 7 | **AI vocabulary** | "Additionally... testament... landscape... showcasing" | "also... remain common" |
| 8 | **Copula avoidance** | "serves as... features... boasts" | "is... has" |
| 9 | **Negative parallelisms** | "It's not just X, it's Y" | State the point directly |
| 10 | **Rule of three** | "innovation, inspiration, and insights" | Use natural number of items |
| 11 | **Synonym cycling** | "protagonist... main character... central figure... hero" | "protagonist" (repeat when clearest) |
| 12 | **False ranges** | "from the Big Bang to dark matter" | List topics directly |

### Style patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 13 | **Em dash overuse** | "institutions--not the people--yet this continues--" | Use commas or periods |
| 14 | **Boldface overuse** | "**OKRs**, **KPIs**, **BMC**" | "OKRs, KPIs, BMC" |
| 15 | **Inline-header lists** | "**Performance:** Performance improved" | Convert to prose |
| 16 | **Title Case Headings** | "Strategic Negotiations And Partnerships" | "Strategic negotiations and partnerships" |
| 17 | **Emojis** | "Launch Phase: Key Insight:" | Remove emojis |
| 18 | **Curly quotes** | `said \u201cthe project\u201d` | `said "the project"` |

### Communication patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 19 | **Chatbot artifacts** | "I hope this helps! Let me know if..." | Remove entirely |
| 20 | **Cutoff disclaimers** | "While details are limited in available sources..." | Find sources or remove |
| 21 | **Sycophantic tone** | "Great question! You're absolutely right!" | Respond directly |

### Filler and hedging

| # | Pattern | Before | After |
|---|---------|--------|----related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 22 | **Filler phrases** | "In order to", "Due to the fact that" | "To", "Because" |
| 23 | **Excessive hedging** | "could potentially possibly" | "may" |
| 24 | **Generic conclusions** | "The future looks bright" | Specific plans or facts |

## Full example

**Before (AI-sounding):**
> Great question! Here is an essay on this topic. I hope this helps!
>
> AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development. In today's rapidly evolving technological landscape, these groundbreaking tools--nestled at the intersection of research and practice--are reshaping how engineers ideate, iterate, and deliver, underscoring their vital role in modern workflows.
>
> At its core, the value proposition is clear: streamlining processes, enhancing collaboration, and fostering alignment. It's not just about autocomplete; it's about unlocking creativity at scale, ensuring that organizations can remain agile while delivering seamless, intuitive, and powerful experiences to users. The tool serves as a catalyst. The assistant functions as a partner. The system stands as a foundation for innovation.

**After (humanized):**
> AI coding assistants can speed up the boring parts of the job. They're great at boilerplate: config files and the little glue code you don't want to write. They can also help you sketch a test, but you still have to read it.
>
> The dangerous part is how confident the suggestions look. I've accepted code that compiled and passed lint, then discovered later it missed the point because I stopped paying attention.
>
> If you treat it like autocomplete and review every line, it's useful. If you use it to avoid thinking, it will help you ship bugs faster.
>
> The only real backstop is tests. Without them, you're mostly judging vibes.

## References

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) - Primary source
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) - Maintaining organization

## Version history

- **1.0.0** - Initial release: platform-agnostic humanizer skill, works with any AI

## Acknowledgments

This repo is inspired by [blader/humanizer](https://github.com/blader/humanizer), a Claude Code skill by Siqi Chen. The original is Claude-specific; this fork generalizes it to work with any AI.

## License

MIT
