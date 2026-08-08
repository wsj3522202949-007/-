---
id: tool-05187
type: tool
area: 库
status: active
tags: [Claude插件, 协议未明, 本地优先, 英文文档, 本地写作]
title: humanizer
summary: Claude Code 插件式写作流
source: https://github.com/rbaddam/humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5187
category: 一、去 AI 味 / Humanizer 库
repo: rbaddam/humanizer
stars: 0
url: https://github.com/rbaddam/humanizer
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: c76c99f575533ead
  - methods/改稿润色指令库.md
---

# rbaddam/humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rbaddam/humanizer
- **Stars**：0
- **语言**：None
- **License**：NOASSERTION
- **Topics**：ai-text, ai-writing, chatgpt, claude, claude-code, claude-skill, copilot, developer-tools, humanizer, llm, opencode, writing, writing-skill, writing-tool
- **GitHub 描述**：AI agent skill for Claude Code and opencode. Finds and removes AI, LLM and robotic writing patterns and rewrites text to sound like human. Works across design docs, READMEs, code comments, and emails.
- **本地描述**：AI agent skill for Claude Code and opencode. Finds and removes AI, LLM and robotic writing patterns and rewrites text to sound like human. Works across design docs, READMEs, code comments, and emails.
- **拉取时间**：2026-07-25 18:09:18

---

# humanizer

Removes AI writing patterns from text and rewrites it to sound human.

Works with Claude Code and opencode. Adjusts tone for design docs, READMEs, code comments,
Slack messages, and emails. Never changes technical terms.

---

## Before / After

**Before:**
> This document serves as a pivotal resource for understanding our event-driven architecture.
> Leveraging Kafka as our backbone, we have fostered a robust, scalable, and seamless data
> pipeline. The system boasts sub-50ms latency, ensuring real-time processing and highlighting
> our commitment to performance. Let's dive into the details.

**After:**
> This document covers our event-driven architecture. We use Kafka as the message backbone.
> The pipeline processes events with sub-50ms latency.

---

## What it catches

18 AI writing patterns:

| Pattern | Example |
|---------|---------|
| AI vocabulary | delve, leverage, utilize, pivotal, seamless, tapestry, testament, synergy |
| Copula avoidance | "serves as" → "is", "boasts" → "has" |
| Significance inflation | "marks a pivotal moment", "evolving landscape" |
| Filler phrases | "In order to", "It is important to note that", "Moving forward" |
| Superficial -ing phrases | "ensuring reliability", "fostering collaboration" |
| Em dash frequency | 3+ per page is a signal — one or two is fine |
| Boldface overuse | **Performance:** description → description |
| Passive voice | "errors are handled gracefully" → say what handles them |
| Persuasive authority tropes | "at its core", "the real question is", "fundamentally" |
| Signposting | "let's dive into" → start with the content |
| Fragmented headers | heading followed by a sentence restating the heading |
| Negative parallelisms | "it's not just X, it's Y" → say Y |
| Vague attributions | "experts argue", "observers have noted" → cite or delete |
| Promotional language | "groundbreaking", "cutting-edge" → say what's new |
| Generic conclusions | "exciting times ahead" → end on the last real point |
| Perfect parallel structure | every bullet same verb form, same length → break the symmetry |
| Neutralized opinion | "there are trade-offs" → restore the actual take |
| Over-spelled informal text | "environment" in Slack → "env", "Kubernetes" → "k8s" |

---

## Context-aware rewrites

| Context | Target tone |
|---------|-------------|
| LLD / HLD / Design doc | Formal, precise — technical accuracy first |
| README | Direct, scannable — developers skim |
| Code comments | Minimal — one purpose per comment |
| Email | Business casual — direct opener |
| Slack | Casual, short — skip warm-ups |

API names, product names, and version numbers are never changed.

---

## Install

**Claude Code**
```bash
git clone https://github.com/rbaddam/humanizer.git && cp humanizer/SKILL.md ~/.claude/skills/humanizer/SKILL.md
```

**opencode**
```bash
git clone https://github.com/rbaddam/humanizer.git && cp humanizer/SKILL.md ~/.agents/skills/humanizer/SKILL.md
```

## Uninstall

```bash
rm -rf ~/.claude/skills/humanizer        # Claude Code
rm -rf ~/.agents/skills/humanizer        # opencode
```

---

## Use

Once installed, use it in any conversation:

```
Humanize this: [paste text]
```

```
Humanize this design doc section: [paste text]
```

```
Humanize this Slack message: [paste text]
```

The skill detects context automatically. You can also be explicit:
`"Humanize this as a README"` or `"Humanize this as a code comment"`.

---

## Attribution

Pattern catalog based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
maintained by WikiProject AI Cleanup (CC BY-SA 4.0).

Skill framework derived from humanizer v2.5.1 (MIT license).

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

Apache 2.0 — see [LICENSE](https://github.com/rbaddam/humanizer/blob/main/LICENSE).
