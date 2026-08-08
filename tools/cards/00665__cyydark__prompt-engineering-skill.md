---
id: tool-00665
type: tool
area: 库
status: active
tags: [提示词, TTS, Claude插件, 协议未明, 本地优先, 英文文档, 本地写作]
title: prompt-engineering-skill
summary: 小说转语音/有声书
source: https://github.com/cyydark/prompt-engineering-skill
created: 2026-07-18
updated: 2026-07-18
no: 665
category: 二、网文 / 长篇 AI 写作系统 库
repo: cyydark/prompt-engineering-skill
stars: 0
url: https://github.com/cyydark/prompt-engineering-skill
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8ff791e77156cedc
  - methods/最强写作方法论_全球最强综合版.md
---

# cyydark/prompt-engineering-skill

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/cyydark/prompt-engineering-skill
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：A 6-layer prompt design framework for writing prompts that AI coding tools can execute correctly.
- **本地描述**：A 6-layer prompt design framework for writing prompts that AI coding tools can execute correctly.
- **拉取时间**：2026-07-23 22:58:26

---

# Prompt Engineering Skill for Claude Code

A Claude Code skill that teaches a **6-layer prompt design framework** for writing prompts that AI coding tools can execute correctly. Covers Claude Code, GitHub Copilot, Cursor, and any LLM-based coding assistant.

## Based On

This skill was built by applying the 6-layer prompt design framework to the development prompts of [voice-input-src](https://github.com/yetone/voice-input-src) — a menu-bar voice input app for macOS that intercepts the Fn key globally for recording, performs streaming speech recognition, and injects transcribed text into any app.

The real-world complexity of that project (CJK IME handling, audio pipeline, global event interception) made it the perfect proving ground for a rigorous prompt design methodology.

## The 6-Layer Framework

| Layer | Name | What It Does |
|-------|------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| 1 | Context & Goal | Who you are, what you're building, why it matters |
| 2 | Technical Specs | Numbers + units + specific APIs instead of vague descriptions |
| 3 | Algorithm & Logic | Pseudocode that externalizes your implicit knowledge |
| 4 | Edge Cases | All failure modes and how to handle them |
| 5 | Negative Constraints | What NOT to do — prevents AI "helpfulness" from breaking things |
| 6 | Output Format | Exact files, build commands, and quality gates |

## Quick Template

```
## Layer 1 — Context & Goal
[Who you are] + [What you're building] + [Why it matters]

## Layer 2 — Technical Specs
[Exact dimensions, colors, frameworks, APIs]

## Layer 3 — Algorithm / Logic
[Step-by-step in plain English or pseudocode]

## Layer 4 — Edge Cases
[List specific failure modes and handling]

## Layer 5 — Negative Constraints
[What NOT to do — be explicit]

## Layer 6 — Output Format
[Files, build commands, quality requirements]
```

## Worked Example

**Bad (vague):**
> Build a macOS voice input app that records when you hold a key and injects the text.

**Good (6 layers):**

> **Layer 1 — Context:** I am building a menu-bar voice input app for macOS 14+ (Swift). My target users are Chinese speakers who need to dictate into any app. This replaces manual typing for short-to-medium text inputs.
>
> **Layer 2 — Specs:** Hold Fn key to record, release to inject. Floating window: 56px tall, corner radius 28px, NSPanel nonactivatingPanel, NSVisualEffectView(.hudWindow). Waveform: 5 bars, weights [0.5, 0.8, 1.0, 0.75, 0.55], RMS-driven, attack 40%/release 15%, ±4% jitter.
>
> **Layer 3 — Logic:** Use CGEvent tap to intercept Fn key globally. On keyDown: start AVAudioEngine recording + SFSpeechRecognizer streaming. On keyUp: stop recording, send to LLM (if enabled), inject via clipboard swap. For CJK IME: switch to ASCII source before paste, restore after 200ms.
>
> **Layer 4 — Edge cases:** Mic permission denied → show settings deep-link. Empty transcription → show "No speech" for 1.5s. LLM timeout >10s → inject raw text. No internet → skip LLM entirely.
>
> **Layer 5 — Constraints:** Do NOT use hardcoded fake waveform animation. Do NOT paste without IME switching — CJK users will get broken output. Do NOT store API keys in code. Do NOT modify clipboard contents permanently.
>
> **Layer 6 — Output:** SPM project, Makefile (build/run/install/clean), LSUIElement app, Info.plist with NSMicrophoneUsageDescription, audio-input entitlement.

## Installation

Copy the `SKILL.md` file to your Claude Code skills directory:

```bash
# Claude Code default skills directory
cp SKILL.md ~/.claude/skills/prompt-engineering/SKILL.md
```

Or place it alongside your project-specific skills:

```
.your-project/
└── .claude/
    └── skills/
        └── prompt-engineering/
            └── SKILL.md
```

## When to Use

Activate this skill when:
- You want to write better prompts for AI coding tools
- You're starting a new project and need to structure your request
- A prompt produced poor code and you want to understand why
- Your task is complex enough that vague = wrong

## License

MIT
