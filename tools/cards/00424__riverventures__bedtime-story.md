---
id: tool-00424
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: bedtime-story
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/riverventures/bedtime-story
created: 2026-07-18
updated: 2026-07-18
no: 424
category: 二、网文 / 长篇 AI 写作系统 库
repo: riverventures/bedtime-story
stars: 1
url: https://github.com/riverventures/bedtime-story
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: e7b8e97532c64edc
  - methods/最强写作方法论_全球最强综合版.md
---

# riverventures/bedtime-story

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/riverventures/bedtime-story
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI bedtime story generator. Your kid is the hero. Personalized, illustrated, printable. OpenClaw skill.
- **本地描述**：AI bedtime story generator. Your kid is the hero. Personalized, illustrated, printable. OpenClaw skill.
- **拉取时间**：2026-07-23 22:51:28

---

# 🌙 bedtime-story

Personalized bedtime stories where your kid is the hero. An [OpenClaw](https://github.com/openclaw/openclaw) skill.

## What it does

Your kid picks who they want to be tonight. The AI writes a story with them as the main character, generates character-consistent watercolor illustrations, and gives you a printable landscape picture book. Over time, you build a physical storybook together.

```
"Nina wants to be friends with a flamingo tonight"
```

→ 9-page landscape picture book where Nina meets a flamingo by the pool, with her Nani tucking her in at the end. Full-bleed watercolor illustrations, one line of story per page.

## Install

```bash
openclaw skill add riverventures/bedtime-story
```

## Features

- **Your kid is the hero.** Every story uses their real name and puts them at the center.
- **Character-consistent illustrations.** Describe your child once — hair, skin, eyes, outfit. The skill generates a hero reference image and passes it to every page so your kid looks the same throughout.
- **Age-calibrated.** Under 2: simple sensory stories, 8-10 pages, one line each. Ages 3-5: problem-solution arcs. Ages 6+: real narrative with twists.
- **Landscape picture book format.** Full-bleed illustration fills 90% of each page. One line of story at the bottom. Looks like a real children's book.
- **Family members included.** Describe grandma, grandpa, siblings, pets — they appear as recurring characters.
- **Printable.** Landscape A4 PDF. Print, staple, done.
- **Anti-duplication guardrails.** Built-in prompt engineering to prevent the AI from cloning your child in the same illustration.
- **Voice narration.** Optional audio version via ElevenLabs.
- **Always ends with sleep.** Engineered to make kids want to close their eyes.

## First Time Setup

Tell me about your child:

```
Name: Nina
Age: 19 months
Hair: straight, short, dark brown
Skin: light olive
Eyes: big, dark brown
Features: tiny gold stud earrings
Default outfit: light pink dress with white flowers
Favorites: birds, flamingos, cats, pool, tomatoes
Family:
  - Nani (grandmother): Indian, early 50s, dark brown hair, blue cardigan and jeans
  - Nanu (grandfather): [description]
  - Masie (aunt): [description]
Avoid: nothing scary, no loud noises
```

After that, every night just say who they want to be.

## Output

| Feature | Detail |
|---|---|
| Orientation | Landscape (11 x 8.5 in) |
| Illustration | 90% of page, full-bleed, watercolor |
| Text | 10% bottom strip, Georgia 42pt, black on white |
| Pages | 8-10 (under 2), 10-15 (older) |
| Format | Multi-page PDF |
| Character consistency | Hero reference image + anchor string on every page |

## How Character Consistency Works

1. You describe your child's appearance once
2. The skill generates a **hero reference image** — a front-facing portrait in the story's art style
3. That reference image is passed as input to **every page generation** alongside the scene prompt
4. An identical character description (anchor string) is included in every prompt
5. Anti-duplication guardrails prevent the model from rendering the child twice

This isn't perfect — AI image generation still has drift. But it's significantly better than generating each page independently.

## Examples

| Request | Output |
|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| "Nina wants to be friends with a flamingo" (19mo) | 9 pages, pool party, Nani tucks her in |
| "Liam wants to be an astronaut" (4yr) | 12 pages, discovers Planet Banana, silly aliens |
| "Maya wants to be a detective" (7yr) | 15 pages, solves mystery at school, plot twist |

## Requirements

- Google API key (Gemini for illustrations)
- Python 3.9+ with Pillow (for PDF assembly)
- Optional: ElevenLabs API key (voice narration)
- Optional: printer for nightly printouts

## Why this exists

A dad on Reddit has his kids pick heroes each night. His daughter picks a princess, his son picks a superhero. AI generates a story where they ARE those characters. He prints each story with an illustration, and the kids build their own physical storybooks.

I thought every parent should be able to do this. Now they can.

## License

MIT
