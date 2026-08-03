---
id: tool-05332
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/epicsaber/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5332
category: 一、去 AI 味 / Humanizer 库
repo: EpicSaber/ai-text-detector
stars: 0
url: https://github.com/epicsaber/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# EpicSaber/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/epicsaber/ai-text-detector
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Apify actor: ai-text-detector
- **本地描述**：Apify actor: ai-text-detector
- **拉取时间**：2026-07-25 18:14:41

---

[AI Text Detector](https://apify.com/dadhalfdev/ai-text-detector?fpr=data)

# 🤖 AI Text Detector

Detect AI-generated writing signals in articles, social media posts, and other text formats. The actor classifies each input as `Social Media`, `Article`, or `Other`, then extracts structured evidence and ratings for common AI-writing tells.

## 💡 Perfect For

- 📱 **Social Media Audits:** Review comments, captions, and posts for AI-like phrasing.
- 📰 **Article Reviews:** Analyze articles, newsletters, and blog posts for formulaic AI writing.
- 🛡️ **Moderation & QA:** Build moderation, quality-control, or editorial workflows around AI-content risk.
- 📊 **Structured Exports:** Export AI-detection signals to CSV, JSON, Excel, or downstream dashboards.

## ✨ What It Detects

For every input text, the actor returns:

- 🏷️ `text_type`: `Social Media`, `Article`, or `Other`.
- 📏 `text_length_chars` and `text_length_words`.
- ➖ `em_dashes_num` and `em_dashes_rating`.
- 🧩 AI verb, adjective, noun, transition, and phrase counts, evidence lists, and ratings.
- 📝 `sentence_patterns_num`, `sentence_patterns_list`, and `sentence_patterns_rating`.
- 🎯 `overall_ai_rating`, a 0-100 estimate of how likely the text is AI-generated.

The detector looks for high-signal AI patterns such as em dash-heavy prose, phrases like `game-changer` or `in today's fast-paced world`, generic polished agreement, rhetorical contrast patterns, staccato triplets, vague buzzword stacking, and other formulaic structures.

## 🚀 How To Use

1. Add one or more texts to `input_text_list`.
2. Start the actor.
3. Export the dataset as JSON, CSV, Excel, or through the Apify API.

You can process up to 30 texts per run. Each text can contain up to 30,000 characters.

## 📥 Input Example

```
{
  "input_text_list": [
    "Flexible payment systems are essential, but true accessibility comes from supporting freelancers globally, regardless of location. Expanding payment options would make an even bigger impact.",
    "That’s not a feature. That’s the entire value proposition right there. Because without it, you’re just hoping your agents behave responsibly — and they won’t, because “responsible” isn’t a concept they have. They have goals. Goals and no ceiling is how you end up with a $50,000 cloud bill.\n\nBeyond budget enforcement, Paperclip handles task assignment through what it calls atomic checkout. Only one agent can hold a task at a time. That sounds obvious, but it’s genuinely hard to implement when you’re running a dozen concurrent agents, and most frameworks just… don’t do it. You end up with three agents researching the same competitor because nobody claimed the task. Paperclip treats that the way a database treats concurrent writes — with locks, guarantees, and no duplicates.\n\nEvery decision, every tool call, every status change gets logged to an..."
  ]
}
```

## 📤 Output Example

```
{
  "text": "That’s not a feature. That’s the entire value proposition right there. Because without it, you’re just hoping your agents behave responsibly — and they won’t, because “responsible” isn’t a concept they have. They have goals. Goals and no ceiling is how you end up with a $50,000 cloud bill.\n\nBeyond budget enforcement, Paperclip handles task assignment through what it calls atomic checkout. Only one agent can hold a task at a time. That sounds obvious, but it’s genuinely hard to implement when you’re running a dozen concurrent agents, and most frameworks just… don’t do it. You end up with three agents researching the same competitor because nobody claimed the task. Paperclip treats that the way a database treats concurrent writes — with locks, guarantees, and no duplicates.\n\nEvery decision, every tool call, every status change gets logged to an...",
  "text_type": "Article",
  "text_length_chars": 12032,
  "text_length_words": 1974,
  "em_dashes_num": 16,
  "em_dashes_rating": 78,
  "ai_verbs_num": 2,
  "ai_verbs_list": [
    "utilize",
    "unveil"
  ],
  "ai_verbs_rating": 10,
  "ai_adjectives_num": 0,
  "ai_adjectives_list": [],
  "ai_adjectives_rating": 0,
  "ai_nouns_num": 6,
  "ai_nouns_list": [
    "realm",
    "landscape",
    "tapestry",
    "testament",
    "beacon",
    "complexities"
  ],
  "ai_nouns_rating": 18,
  "ai_transitions_num": 2,
  "ai_transitions_list": [
    "Moreover",
    "In conclusion"
  ],
  "ai_transitions_rating": 14,
  "ai_phrases_num": 2,
  "ai_phrases_list": [
    "in today's fast-paced world",
    "game-changer"
  ],
  "ai_phrases_rating": 72,
  "sentence_patterns_num": 6,
  "sentence_patterns_list": [
    "That’s not just for debugging, though it’s excellent for debugging.",
    "That’s not a perfect solution.",
    "No software solution to alignment is.",
    "The “Bring Your Own Agent” Architecture (This Is Key)",
    "The only requirement for an agent to work with Paperclip: it must respond to an HTTP heartbeat signal.",
    "It’s not a perfect solution."
  ],
  "sentence_patterns_rating": 86,
  "overall_ai_rating": 84
}
```

## ⚙️ Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
--- |
| `input_text_list` | array of strings | Yes | List of texts to analyze for AI-generated writing signals. |
