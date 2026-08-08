---
id: tool-05581
type: tool
area: 库
status: active
tags: [去AI味, TTS, 协议宽松, 本地优先, 英文文档, 本地写作]
title: humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/apoapostolov/humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5581
category: 一、去 AI 味 / Humanizer 库
repo: apoapostolov/humanizer
stars: 3
url: https://github.com/apoapostolov/humanizer
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 33a55da393af45a8
  - methods/改稿润色指令库.md
---

# apoapostolov/humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/apoapostolov/humanizer
- **Stars**：3
- **语言**：None
- **License**：MIT
- **Topics**：agents, ai-skill, ai-writing, claude, codex, editing, humanizer, llm, openclaw, prompt, prompt-engineering, style-guide, text-rewrite, vscode, writing
- **GitHub 描述**：Humanizer is an AI writing skill that detects and rewrites common signs of AI-generated prose. It helps agents preserve meaning, match audience and tone, reduce hype and filler, and produce writing that sounds natural, specific, and human across drafts, posts, docs, and messages.
- **本地描述**：Humanizer is an AI writing skill that detects and rewrites common signs of AI-generated prose. It helps agents preserve meaning, match audience and tone, reduce hype and filler, and produce writing that sounds natural, specific, and human across drafts, posts, docs, and messages.
- **拉取时间**：2026-07-25 18:24:00

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Humanizer

Humanizer is a reusable writing skill for turning generated-sounding prose into
clear, specific writing that preserves the author's meaning and voice.

It supports light cleanup, full rewrites, voice-sensitive editing, tone shifts,
fiction and dialogue revision, and systematic editorial audits. One humanization
workflow connects meaning, audience, specificity, voice, structure, and delivery;
a 55-pattern catalog supports deeper diagnosis when needed.

## Capabilities

- remove inflated, generic, promotional, or robotic phrasing
- preserve factual claims, uncertainty, terminology, and deliberate style
- adapt prose to a target audience, platform, and tone
- edit vocabulary, syntax, paragraphs, point of view, dialogue, setting, and
  delivery as one connected system
- repair flat lists, adjective piles, causal piles, pseudo-inventories, and
  false completeness
- identify placeholders, assistant chatter, vague attribution, cutoffs, and
  abrupt voice shifts
- remove prompt and reasoning echoes, generic endorsement closers, leaked
  citation tokens, and AI-tool URL parameters
- critique a draft without rewriting it

The goal is better writing, not AI-detector evasion or artificial imperfection.

## Repository layout

```text
humanizer/
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
├── README.md
└── skills/
    └── humanizer/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        └── references/
            ├── humanizing-text.md
            ├── pattern-catalog.md
            └── examples.md
```

`skills/humanizer/` is the installable skill package. Repository documentation,
release notes, and maintenance guidance remain at the root.

## Installation

Copy the complete `skills/humanizer/` directory so the core skill, UI metadata,
and references remain together.

### OpenClaw

Install as a shared skill:

```bash
mkdir -p ~/.openclaw/skills
cp -R skills/humanizer ~/.openclaw/skills/
```

Install for one workspace:

```bash
mkdir -p ~/.openclaw/workspace/skills
cp -R skills/humanizer ~/.openclaw/workspace/skills/
```

Restart the relevant OpenClaw session if the skill does not appear immediately.

### Claude

```bash
mkdir -p ~/.claude/skills
cp -R skills/humanizer ~/.claude/skills/
```

Start a new Claude session after installation.

### Codex

Default installation:

```bash
mkdir -p ~/.codex/skills
cp -R skills/humanizer ~/.codex/skills/
```

Portable installation when `CODEX_HOME` is set:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/humanizer "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Start a new Codex session if the skill is not discovered automatically.

### skills.sh CLI

Install Humanizer for the current project with the skills.sh CLI. The command
runs through `npx`, so no global CLI installation is required:

```bash
npx skills add apoapostolov/humanizer --skill humanizer
```

Add `--global` to make the skill available across projects. The CLI detects
supported agents and prompts you to choose the installation targets.

### VS Code agents

VS Code does not define one universal skill directory. Copy
`skills/humanizer/` into the skill directory used by the installed agent.

Examples:

```bash
mkdir -p ~/.copilot/skills
cp -R skills/humanizer ~/.copilot/skills/

mkdir -p ~/.continue/skills
cp -R skills/humanizer ~/.continue/skills/
```

Other extensions may use `~/.cline/skills/` or `~/.roo/skills/`.

## Verify installation

Ask the agent:

> Use $humanizer to rewrite this text naturally while preserving my voice.

If the agent supports skill discovery, confirm that `Humanizer` appears in its
skill list. OpenAI-compatible interfaces read the display metadata from
`skills/humanizer/agents/openai.yaml`.

## Usage examples

- “Humanize this for LinkedIn. Keep it thoughtful, not corporate.”
- “Make this sound natural but keep my blunt style.”
- “Critique what makes this sound generated without rewriting it.”
- “Rewrite this internal memo so the decision and owner are clear.”
- “Audit this scene's dialogue and point of view.”

Humanizer works best when the request includes the original text, intended
audience, desired tone, and any phrases or facts that must remain unchanged.

## Version

Current version: `1.2.0`

See [CHANGELOG.md](https://github.com/apoapostolov/humanizer/blob/main/CHANGELOG.md) for release notes.

## License

MIT. See [LICENSE](https://github.com/apoapostolov/humanizer/blob/main/LICENSE).
