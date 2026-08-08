---
id: tool-05089
type: tool
area: 库
status: active
tags: [去AI味, 协议宽松, 本地优先, 英文文档, 本地写作]
title: ai-text-humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/code20/ai-text-humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5089
category: 一、去 AI 味 / Humanizer 库
repo: code20/ai-text-humanizer
stars: 0
url: https://github.com/code20/ai-text-humanizer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: dc8475bd0ba79f49
  - methods/改稿润色指令库.md
---

# code20/ai-text-humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/code20/ai-text-humanizer
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A prompt that rewrites AI-generated text to sound like a specific person wrote it. No clichés, no fluff, no formulaic structures.  And a slightly shorter alternative if character count is tight:  An LLM prompt that makes AI-generated text sound authentically human, from any persona you define.
- **本地描述**：A prompt that rewrites AI-generated text to sound like a specific person wrote it. No clichés, no fluff, no formulaic structures.  And a slightly shorter alternative if character count is tight:  An LLM prompt that makes AI-generated text sound authentically human, from any persona you define.
- **拉取时间**：2026-07-25 18:05:41

---

# Humanizer Rewrite Prompt

By [@code20](https://github.com/code20)

[License](https://github.com/code20/ai-text-humanizer/blob/main/LICENSE)

A detailed LLM prompt that rewrites any text to sound authentically human, from a specific persona's perspective. It strips away AI clichés, marketing fluff, and formulaic structures to produce prose that feels like a real person wrote it.

---

## 🚀 TL;DR

A prompt that takes AI-generated or overly polished text and rewrites it from a specific persona's perspective. You define who is writing, what tone they use, and how long the output should be. The prompt handles the rest: restructuring for natural flow, cutting empty filler, and enforcing plain, direct language. It works with Claude, ChatGPT, Gemini, or any capable LLM. Free. Public domain.

---

## 🧠 What It Does

This prompt takes AI-generated or overly polished text and rewrites it so it sounds like a specific person wrote it, not a content machine. You define the writer's background, the desired tone, and the output length. The prompt then restructures the content for natural flow, cuts empty filler, and enforces plain, direct language.

It works with any capable large language model (Claude, ChatGPT, Gemini, etc.).

## 🔍 The Problem It Solves

Most AI writing tools produce text that sounds impressive at first glance but feels hollow on closer inspection. Common giveaways include:

- Formulaic contrasts like "not only X, but also Y"
- Inflated adjectives like "groundbreaking," "renowned," or "pivotal"
- Forced synonym swapping to avoid repeating a subject's name
- Vague, motivational endings that say nothing specific

This prompt explicitly blocks those patterns and replaces them with prose that has texture, varied rhythm, and believable specificity.

## 🛠️ How to Use It

1. Copy the full content of `humanizer-rewrite-prompt.md`.
2. Paste it into your LLM of choice.
3. Fill in the three variables at the top:

- **Writer persona:** Who is writing this? (e.g., "A 50-year-old Accountant," "A tired graduate student," "A small-town mechanic")
- **Tone:** The emotional and stylistic register (e.g., "Casual and relaxed," "Professional and direct," "Academic but accessible")
- **Length:** How long should the output be? (e.g., "Similar length to the original," "Shorter and tighter," "More detailed but still concise")

1. Paste the text you want rewritten at the bottom, after "Text to rewrite."
2. Run the prompt. The output will be only the rewritten prose, with no introductory or concluding filler.

## ⚠️ Important: This Is an Aid, Not an Authority

This prompt is a readability and style tool. It makes text sound more natural, but it does not guarantee factual accuracy. Large language models can silently alter numbers, shift dates, drop qualifiers like "may" or "some," and subtly change claims in ways that are easy to miss on a quick read.

Always validate the output against your source material. Check that:

- Numbers, dates, statistics, and proper names match the original exactly
- Hedging language like "may," "might," "some users," or "in some cases" has not been hardened into definite claims
- Nothing has been added that was not in the original text, including implied context, examples, or background details
- The meaning of each sentence holds up when compared side by side with the source

Treat the output as a strong first draft for tone and readability. You are still responsible for the final accuracy of anything you publish or share.

## 📝 Example

**Input variables:**

- Writer persona: A 50-year-old accountant who explains things patiently
- Tone: Casual and relaxed
- Length: Shorter and tighter

**Text to rewrite (excerpt from generic product copy):**

> Our groundbreaking platform leverages cutting-edge AI technology to revolutionize your workflow. Not only does it streamline operations, but it also boosts productivity to unprecedented levels. Experts agree this is a pivotal moment for the industry, and our solution stands as a testament to what innovation can achieve.

**Output:**

> The software uses AI to handle repetitive tasks. It organizes your files, drafts responses to common questions, and flags things that look off so you can check them yourself. I have been using it for about a year, and the main difference is that I spend less time sorting through clutter and more time on work that actually needs my attention.

This illustrates the key difference: the original relies on inflated claims and anonymous authority, while the rewrite grounds the description in concrete, believable language from a specific person's point of view.

## 🤝 Who This Is For

- Bloggers cleaning up AI-generated drafts
- Marketers who want copy that doesn't sound like a landing page from 2018
- Developers writing documentation, changelogs, or READMEs
- Non-native speakers using AI for English prose who want natural-sounding output
- Anyone who has read AI-generated text and thought "this is fine but it has no texture"

## 🧩 Why This Prompt Is Detailed

Every rule in the prompt targets a specific failure pattern common in AI-generated prose. The length is intentional. Vague instructions like "make it sound human" produce inconsistent results. Explicit prohibitions on formulaic contrasts, empty grand claims, and forced synonym swapping give the model clear guardrails that dramatically improve output quality.

## 📁 Files in This Repo


| File                          | Purpose           |
| ----------------------------- | --------------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
--- |
| `humanizer-rewrite-prompt.md` | The full prompt   |
| `README.md`                   | You're reading it |
| `LICENSE`                     | MIT               |


## 📝 [License](https://github.com/code20/ai-text-humanizer/blob/main/LICENSE)

```
MIT — use it, modify it, share it. See [LICENSE](https://github.com/code20/ai-text-humanizer/blob/main/LICENSE) for details
```

