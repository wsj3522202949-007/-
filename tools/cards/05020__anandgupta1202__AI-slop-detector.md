---
id: tool-05020
type: tool
area: 库
status: active
tags: [协议未明, 需API密钥, 英文文档, 去AI味]
title: AI-slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/anandgupta1202/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5020
category: 一、去 AI 味 / Humanizer 库
repo: anandgupta1202/AI-slop-detector
stars: 1
url: https://github.com/anandgupta1202/ai-slop-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 35873a0eb151dfcc
  - methods/改稿润色指令库.md
---

# anandgupta1202/AI-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/anandgupta1202/ai-slop-detector
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：anandgupta1202/AI-slop-detector
- **拉取时间**：2026-07-25 18:03:10

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI-slop-detector

Comprehensive AI writing pattern detector and rewriter. 

Use when drafting, editing, or reviewing any prose to catch and eliminate the 18 most common AI writing tells across:
- sentence structure
- tone
- word choice
- paragraph structure
- formatting

Covers negative parallelism, dramatic countdowns, false ranges, stakes inflation, rhetorical self-answers, filler transitions, invented labels, ornate nouns, tricolon/anaphora abuse, punchy fragments, false suspense, patronizing analogies, simplicity assertions, disguised listicles, superficial analyses, vague attributions, and unicode decoration.

## Usage with Claude

### As a Project Instruction

1. Open your Claude project (or create a new one) at [claude.ai](https://claude.ai)
2. Go to **Project Settings** → **Custom Instructions**
3. Copy the contents of `ai-slop-detector.md` and paste it into the custom instructions field
4. Claude will now automatically detect and flag AI writing patterns in any text you share

### In a Single Conversation

Paste the contents of `ai-slop-detector.md` at the start of your conversation, then ask Claude to review or rewrite your text. For example:

```
[paste ai-slop-detector.md contents]

Review the following draft and flag any AI slop patterns:

[your text here]
```

### With the Claude API

Include the contents of `ai-slop-detector.md` as a system prompt:

```python
import anthropic

client = anthropic.Anthropic()

with open("ai-slop-detector.md") as f:
    slop_detector = f.read()

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system=slop_detector,
    messages=[
        {"role": "user", "content": "Review this text for AI writing patterns:\n\n[your text]"}
    ],
)
```
