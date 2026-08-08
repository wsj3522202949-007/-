---
id: tool-01644
type: tool
area: 库
status: active
tags: [TTS, Claude插件, Shell, 协议未明, 本地优先, 英文文档, 本地写作]
title: my-voice-template
summary: 小说转语音/有声书
source: https://github.com/ekroon/my-voice-template
created: 2026-07-18
updated: 2026-07-18
no: 1644
category: 二、网文 / 长篇 AI 写作系统 库
repo: ekroon/my-voice-template
stars: 0
url: https://github.com/ekroon/my-voice-template
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
content_hash: b071d08e58ee3204
  - methods/最强写作方法论_全球最强综合版.md
---

# ekroon/my-voice-template

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ekroon/my-voice-template
- **Stars**：0
- **语言**：Shell
- **License**：None
- **Topics**：—
- **GitHub 描述**：Copilot CLI plugin template: capture your writing style and make AI-generated text sound like you
- **本地描述**：Copilot CLI plugin template: capture your writing style and make AI-generated text sound like you
- **拉取时间**：2026-07-23 23:26:59

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# my-voice

A Copilot CLI plugin that captures your personal writing style and transforms AI-generated text to sound like you wrote it.

## The Problem

AI-generated text is useful but sounds generic. If you are someone who writes documents, proposals, status updates, or discussion posts, you want the AI to help with the effort, but not lose your identity in the process. This plugin solves that.

## How It Works

1. **Capture your voice**: The agent guides you through writing 5-8 short pieces in your natural style
2. **Build your profile**: It analyzes your samples and generates a voice profile (tone, vocabulary, sentence patterns, things to avoid)
3. **Use it**: From then on, the skill transforms AI output to match your voice, or the agent helps you write full documents in your style

## Structure

```
plugin.json                         # Copilot CLI plugin manifest
agents/
└── my-voice.agent.md               # Full writing session agent
skills/my-voice/
├── SKILL.md                        # Quick voice transformation skill
├── references/
│   └── voice-profile.md            # Your generated style guide
└── writing-samples/                # Your real writing samples
    └── .gitkeep
```

## Installation

### As a Copilot CLI plugin

```bash
copilot plugin install ./my-voice
```

After forking/cloning, install the plugin from your local directory. Then:
- `/agent` → select `my-voice` for dedicated writing sessions
- `/skills list` → verify the `my-voice` skill is loaded

### First run

When you start the agent for the first time, it will detect that the voice profile is empty and switch to capture mode. It will guide you through writing short pieces and then generate your profile.

## Usage

### Dedicated writing session (agent)

```
/agent my-voice
> I need to write a discussion post about improving our deployment process
```

The agent will ask for your rough content, draft it in your voice, and iterate section by section.

### Quick transform (skill)

In any conversation:

```
> Rewrite this in my voice: [paste AI-generated text]
```

The skill activates automatically and transforms the text.

### Adding more samples

Drop new `.md` files into `skills/my-voice/writing-samples/` and ask the agent to re-analyze:

```
/agent my-voice
> I added new writing samples, please re-analyze and update my voice profile
```

## Privacy

After capturing your voice, this repository will contain personal writing samples and a style profile. **Keep your fork/copy private** if you do not want others to replicate your writing style.

## License

MIT
