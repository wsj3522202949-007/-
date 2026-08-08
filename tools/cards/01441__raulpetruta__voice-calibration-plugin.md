---
id: tool-01441
type: tool
area: 库
status: active
tags: [TTS, Claude插件, 协议宽松, 本地优先, 英文文档, 本地写作]
title: voice-calibration-plugin
summary: 小说转语音/有声书
source: https://github.com/raulpetruta/voice-calibration-plugin
created: 2026-07-18
updated: 2026-07-18
no: 1441
category: 二、网文 / 长篇 AI 写作系统 库
repo: raulpetruta/voice-calibration-plugin
stars: 10
url: https://github.com/raulpetruta/voice-calibration-plugin
tier: "B"
use_case: "小说转语音/有声书"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4d4e123e3af717a9
  - methods/最强写作方法论_全球最强综合版.md
---

# raulpetruta/voice-calibration-plugin

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/raulpetruta/voice-calibration-plugin
- **Stars**：10
- **语言**：None
- **License**：MIT
- **Topics**：claude-code, claude-code-plugin, claude-skills, codex, codex-cli, codex-skills
- **GitHub 描述**：AI voice calibration plugin that learns your writing style through guided prompts and generates a reusable voice profile so agents can write more like you across tools and workflows.
- **本地描述**：AI voice calibration plugin that learns your writing style through guided prompts and generates a reusable voice profile so agents can write more like you across tools and workflows.
- **拉取时间**：2026-07-23 23:21:06

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Voice Calibration Plugin

Teach AI to write and talk like you.

This Claude Code plugin learns your personal writing style through a series of interactive writing prompts — micro-stories, opinions, casual messages, descriptions — then generates a reusable **voice profile** that AI can use to match your tone, vocabulary, and personality.

## Installation (Claude Code)

### 1. Add the marketplace

```
/plugin marketplace add raulpetruta/voice-calibration-plugin
```

### 2. Install the plugin

```
/plugin install voice-calibration-plugin@voice-calibration-marketplace
```

### 3. Restart Claude Code

This ensures the plugin loads correctly.

## Usage

### Calibrate your voice

Run the skill:

```
/voice-calibration-plugin:voice-calibration
```

Or just tell Claude:

> "Learn my writing style"

Claude will guide you through 6-12 writing prompts, analyze your responses, and generate a voice profile saved as `.voice-profile.md`.

### Write in your voice

Once your profile exists, just ask:

> "Write an email to my team about the new feature — use my voice"

Claude reads your profile and matches your style automatically.

### Update your profile

Run calibration again anytime. You can start fresh or add more samples to refine your existing profile.

## How it works

1. **Prompts** — Claude presents diverse writing exercises (stories, opinions, rants, explanations) to capture your style across different registers
2. **Analysis** — Your samples are analyzed across 7 dimensions: sentence structure, vocabulary, tone, punctuation, narrative style, conversational markers, and cultural markers
3. **Profile** — A structured voice profile is generated with specific observations, sample phrases, and anti-patterns to avoid
4. **Review** — You review and refine the profile before it's saved

## Cross-platform compatibility

The skill inside this plugin follows the open [Agent Skills specification](https://agentskills.io), so the `skills/voice-calibration/` directory can also be used standalone with any agentskills.io-compatible tool (Cursor, VS Code Copilot, Gemini CLI, Goose, and others).

## License

MIT — see [LICENSE](https://github.com/raulpetruta/voice-calibration-plugin/blob/main/LICENSE) for details.
