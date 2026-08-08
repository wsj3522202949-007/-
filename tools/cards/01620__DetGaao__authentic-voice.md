---
id: tool-01620
type: tool
area: 库
status: active
tags: [TTS, Claude插件, 协议宽松, 本地优先, 英文文档, 本地写作]
title: authentic-voice
summary: 小说转语音/有声书
source: https://github.com/detgaao/authentic-voice
created: 2026-07-18
updated: 2026-07-18
no: 1620
category: 二、网文 / 长篇 AI 写作系统 库
repo: DetGaao/authentic-voice
stars: 0
url: https://github.com/detgaao/authentic-voice
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8041a6e37895f4ce
  - methods/最强写作方法论_全球最强综合版.md
---

# DetGaao/authentic-voice

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/detgaao/authentic-voice
- **Stars**：0
- **语言**：None
- **License**：Apache-2.0
- **Topics**：agent-skills, ai-writing, claude-code, copilot, cursor, llm, windsurf, writing-style
- **GitHub 描述**：Stop your AI from writing like an AI. An agent skill for authentic, human-sounding text.
- **本地描述**：Stop your AI from writing like an AI. An agent skill for authentic, human-sounding text.
- **拉取时间**：2026-07-23 23:26:17

---

# Authentic Voice

Stop your AI from writing like an AI.

One skill. No dependencies. Install in 5 seconds.

## What it does

Authentic Voice is an [agent skill](https://agentskills.io) that rewrites how your AI assistant produces text. It targets the patterns that make AI output immediately recognizable: the banned vocabulary ("delve," "tapestry," "stands as a testament"), the structural tells (rule of three, hedging everything, participial padding), and the formatting habits (bold everything, em dashes everywhere).

It works across five writing contexts — email, documentation, website copy, marketing, and general prose — with tone rules specific to each.

## Install

```bash
npx skills add DetGaao/authentic-voice --global
```

Or project-level:

```bash
npx skills add DetGaao/authentic-voice
```

## Before and after

**Vocabulary cleanup:**

| Before (default AI) | After (with authentic-voice) |
|---|---|
| "Let's delve into the intricacies of the authentication system." | "Here's how the auth system works." |
| "The platform boasts a vibrant ecosystem, showcasing innovative solutions." | "The platform has 200+ plugins and an active developer community." |
| "This stands as a testament to the team's meticulous commitment to quality." | "The team caught it because they test every release against production data." |

**Structural pattern fixes:**

| Before (default AI) | After (with authentic-voice) |
|---|---|
| "It's not just a tool — it's a partner in your creative journey." | "It handles the repetitive parts so you can focus on the interesting ones." |
| "The system is fast, reliable, and scalable." | "The system handles 50K concurrent users without breaking a sweat." |
| "The team shipped the feature, showcasing their dedication to user satisfaction." | "The team shipped the feature on Thursday." |
| "It could potentially be argued that this approach might represent a viable solution." | "This approach works. Here's why." |

**Email tone:**

| Before (default AI) | After (with authentic-voice) |
|---|---|
| "I hope this email finds you well. I wanted to reach out regarding the upcoming deadline. Please don't hesitate to reach out if you have any questions." | "The deadline is Friday. Let me know if that's a problem." |

## What's inside

| Section | What it covers |
|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Writing contexts | Context-specific register and tone (email, doc, copy, marketing, general) |
| Banned vocabulary | ~30 hard-banned words/phrases, ~10 soft-banned with exceptions |
| Structural patterns | 8 AI writing patterns to avoid (hedging, elegant variation, copula avoidance, etc.) |
| Formatting tells | Excessive bolding, em dash overuse, bullet-with-bold-header defaults |
| Tone rules | Per-context guidance (how email differs from docs differs from marketing) |
| Self-check | 5-point checklist before delivering any text |

## Usage

The skill activates automatically for any writing task. You can also invoke it directly:

```
/authentic-voice          # general context
/authentic-voice email    # email-specific rules
/authentic-voice copy     # website copy rules
/authentic-voice marketing
/authentic-voice doc
```

## Why this exists

Every LLM draws from the same training distribution. Without intervention, they all produce the same tells: "delve into the intricacies," "not just X, but also Y," three bullet points with bold headers, hedged conclusions. People notice. Search engines notice.

This skill was built from [documented AI writing patterns](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI-generated_content) and refined through daily use. It's opinionated by design — the point is to break the defaults, not offer suggestions.

## Compatibility

Works with any agent that supports the [Agent Skills](https://agentskills.io) format:

- Claude Code
- Cursor
- Windsurf
- Copilot CLI
- Any skills-compatible agent

## Contributing

Found a pattern that should be banned? A context that needs its own rules? Open an issue or PR. See [CONTRIBUTING.md](https://github.com/DetGaao/authentic-voice/blob/main/CONTRIBUTING.md) for guidelines and issue templates.

## License

Apache-2.0. See [LICENSE](https://github.com/DetGaao/authentic-voice/blob/main/LICENSE) for details.
