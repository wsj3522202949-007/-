---
id: tool-01726
type: tool
area: 库
status: active
tags: [TTS, Claude插件, 协议宽松, 本地优先, 英文文档, 本地写作]
title: kling-3-prompting-skill
summary: 小说转语音/有声书
source: https://github.com/aedev-tools/kling-3-prompting-skill
created: 2026-07-18
updated: 2026-07-18
no: 1726
category: 二、网文 / 长篇 AI 写作系统 库
repo: aedev-tools/kling-3-prompting-skill
stars: 21
url: https://github.com/aedev-tools/kling-3-prompting-skill
tier: "B"
use_case: "小说转语音/有声书"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: ab41e2d304b25b0c
  - methods/最强写作方法论_全球最强综合版.md
---

# aedev-tools/kling-3-prompting-skill

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/aedev-tools/kling-3-prompting-skill
- **Stars**：21
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI agent skill for writing cinema-grade Kling 3.0 video prompts — interactive builder for text-to-video, image-to-video, multi-shot, and keyframes
- **本地描述**：AI agent skill for writing cinema-grade Kling 3.0 video prompts — interactive builder for text-to-video, image-to-video, multi-shot, and keyframes
- **拉取时间**：2026-07-23 23:29:21

---

# Kling 3.0 Prompt Skills

AI agent skill for writing better Kling 3.0 video generation prompts. Describe your scene in natural language, and the agent builds a polished, cinema-grade prompt for you.

```bash
npx skills add aedev-tools/kling-3-prompting-skill
```

---

## What it does

- **Interactive prompt builder** — walks you through scene, subject, camera, lighting, audio, and mood
- **Covers all generation modes** — text-to-video, image-to-video, multi-shot sequences, and keyframe transitions
- **Cinematic language** — translates your ideas into the director-style prompts Kling 3.0 responds best to
- **Quick reference tables** — camera movements, lens/film stock, lighting, color grading, dialogue rules

## Example prompts it generates

```
"Dense Indian forest canopy, dappled sunlight filtering through banyan trees.
A small rhesus macaque leaps between branches with effortless agility.
Handheld shoulder-cam tracks him closely from below, rushing through foliage
to keep up. Ambient jungle sounds — birds, rustling leaves, distant insects."
```

```
"A dim kitchen late at night. Only the refrigerator hum fills the silence.
[Character A: Exhausted Partner, trembling frustrated voice]: 'You never
listen to me.' Immediately, the other partner turns around, eyes wide.
[Character B: Defensive Partner, shouting loudly]: 'Because you never
stop blaming!'"
```

## Setup

1. **Install the skill:**

   ```bash
   npx skills add aedev-tools/kling-3-prompting-skill
   ```

2. **Start prompting.** Open your coding agent and describe the video you want to create.

## Requirements

- A coding agent that supports [Agent Skills](https://agentskills.io) (Claude Code, Cursor, etc.)

## What's inside

| Feature | Coverage |
|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Text-to-Video | Full prompt assembly from scratch |
| Image-to-Video | Motion, camera, and evolution from reference images |
| Multi-Shot | 2-6 shot storyboards with labeled scenes and durations |
| Keyframe Transitions | Start/end frame interpolation with motion control |
| Dialogue & Lip-Sync | Multi-character scenes with voice tone and timing |
| Camera Language | 12 movement types with example phrases |
| Lighting & Color | Specific source descriptors, color grade language |
| Negative Prompts | Default set to prevent common AI artifacts |

## Feedback & Issues

Found a bug? Have a feature request or idea?
[Open an issue](https://github.com/aedev-tools/kling-3-prompting-skill/issues)

## License

Apache 2.0 — see [LICENSE](https://github.com/aedev-tools/kling-3-prompting-skill/blob/main/LICENSE) for details.
