---
id: tool-05575
type: tool
area: 库
status: active
tags: [去AI味, TTS, Claude插件, 协议宽松, 需API密钥, 英文文档]
title: claude-skills-creativity
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/bislanb/claude-skills-creativity
created: 2026-07-18
updated: 2026-07-18
no: 5575
category: 一、去 AI 味 / Humanizer 库
repo: BislanB/claude-skills-creativity
stars: 1
url: https://github.com/bislanb/claude-skills-creativity
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# BislanB/claude-skills-creativity

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/bislanb/claude-skills-creativity
- **Stars**：1
- **语言**：None
- **License**：MIT
- **Topics**：agent-skills, ai, anthropic, claude, claude-code, claude-skills, copywriting, llm, russian
- **GitHub 描述**：Production-grade Claude skills: humanizer-ru (natural Russian text without AI markers) and creativity (a non-obvious solution engine)
- **本地描述**：Production-grade Claude skills: humanizer-ru (natural Russian text without AI markers) and creativity (a non-obvious solution engine)
- **拉取时间**：2026-07-25 18:23:47

---

# Claude Skills RU — living text & creative thinking for Claude

> A collection of production-grade [Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) for Claude Code and the Claude API. Not toy demos — tools I use every day.

<p align="center">
  <a href="https://github.com/BislanB/claude-skills-ru/stargazers"><img src="https://img.shields.io/github/stars/BislanB/claude-skills-ru?style=flat-square" alt="Stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="License"></a>
  <a href="https://github.com/sponsors/BislanB"><img src="https://img.shields.io/badge/sponsor-%E2%9D%A4-ff69b4?style=flat-square" alt="Sponsor"></a>
</p>

## Why

By default an LLM gives you the **statistical average of its training data** — sterile, recognizable, predictable. These skills break that default in two of the most common tasks:

| Skill | What it does | For whom |
|---|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 🖋 **`[humanizer-ru](skills/humanizer-ru/)`** | Turns robotic AI text into natural, living Russian: strips bureaucratese, fixes rhythm, adds an authorial voice. Good writing passes AI-detectors as a side effect, not as the goal. | copywriters, marketers, writers — anyone producing Russian text with AI |
| 💡 **`[creativity](skills/creativity/)`** | Forces Claude to find the non-obvious solution: bans the default, finds the contradiction (TRIZ), reframes the problem, collides distant domains. One best solution instead of "here are 5 options." | developers, PMs — anyone stuck on the "obvious" answer |

> **Note:** `humanizer-ru` works on **Russian-language** text and its internal instructions are written in Russian by design. `creativity` is language-agnostic.

## Installation

The skills work in **Claude Code** (CLI/IDE) and through the **Claude API / Agent SDK**.

### Quick install (recommended)

Using the [`skills`](https://skills.sh) CLI — no clone, no manual copying:

```bash
npx skills add BislanB/claude-skills-ru
```

It fetches both skills and drops them into the right folder for your agent automatically.

### Manual install

```bash
# 1. Clone the repository
git clone https://github.com/BislanB/claude-skills-ru.git

# 2. Copy the skills you want into your Claude Code skills folder
#    (global — available in every project)
cp -r claude-skills-ru/skills/humanizer-ru ~/.claude/skills/
cp -r claude-skills-ru/skills/creativity   ~/.claude/skills/
```

On Windows (PowerShell):

```powershell
Copy-Item -Recurse claude-skills-ru\skills\humanizer-ru $env:USERPROFILE\.claude\skills\
Copy-Item -Recurse claude-skills-ru\skills\creativity   $env:USERPROFILE\.claude\skills\
```

Or drop them into `.claude/skills/` inside a specific project to scope them to that project only.

Claude then picks the skill up automatically from its description, or you can invoke it explicitly: `/humanizer-ru` or `/creativity`.

## Usage

### 🖋 humanizer-ru

```
/humanizer-ru <paste your dry AI-generated Russian text here>
```

Three modes (`--mode` flag):
- **rewrite** *(default)* — rewrites the text while preserving meaning
- **write** — writes from scratch on a topic
- **audit** — surfaces problems and AI markers without rewriting

Plus tones (`--tone деловой|дружеский|экспертный|разговорный`) and formats (`--format статья|пост|письмо|лендинг`).

**Under the hood:** the principles of Nora Gal (*"The Word Living and Dead"*) and Maxim Ilyahov (*"Write, Cut"*) — two classics of Russian editorial style — combined with an understanding of the metrics AI-detectors actually use (perplexity, burstiness). Details in `[references/detection-science.md](skills/humanizer-ru/references/detection-science.md)`.

### 💡 creativity

```
/creativity our API responds in 3 seconds, we need it faster
```

Claude won't dump "add a cache and a CDN." It bans that default, finds the contradiction, reframes the problem, and proposes **one** non-obvious solution — with the insight and an honestly named trade-off.

## Support this project

If these skills save you time, drop a ⭐ and consider supporting:

- ❤️ **[GitHub Sponsors](https://github.com/sponsors/BislanB)** — for international supporters
- 🚀 **[Boosty](https://boosty.to/neuromisha)** — for supporters from Russia (works with Russian cards)

A star is free and tells me this is worth maintaining. Thanks 🙌

## Contributing

Found a bug, have an idea for a pattern, or want to add your own skill? Welcome. See `[CONTRIBUTING.md](CONTRIBUTING.md)`.

## License

`[MIT](LICENSE)` — take it, use it, modify it. Attribution is appreciated but not required.
