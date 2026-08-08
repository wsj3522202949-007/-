---
id: tool-05279
type: tool
area: 库
status: active
tags: [Claude插件, Shell, 协议宽松, 本地优先, 英文文档, 本地写作]
title: humanizer
summary: Claude Code 插件式写作流
source: https://github.com/voiscko/humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5279
category: 一、去 AI 味 / Humanizer 库
repo: voiscko/humanizer
stars: 1
url: https://github.com/voiscko/humanizer
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1e98e94da41155f6
  - methods/改稿润色指令库.md
---

# voiscko/humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/voiscko/humanizer
- **Stars**：1
- **语言**：Shell
- **License**：MIT
- **Topics**：ai, ai-writing, antigravity-ide, claude-code, humanizer, llm, opencode, skill, writing
- **GitHub 描述**：A skill for Claude Code, OpenCode, and Antigravity IDE that removes signs of AI-generated writing from text.
- **本地描述**：A skill for Claude Code, OpenCode, and Antigravity IDE that removes signs of AI-generated writing from text.
- **拉取时间**：2026-07-25 18:12:42

---

# Humanizer

> A writing editor skill that removes AI-generated patterns from text — making it sound like it was written by a real person.

**Available in English and German.** Works with Claude Code, OpenCode, and Antigravity IDE.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.7.0-green.svg)](SKILL.md)
[![Patterns](https://img.shields.io/badge/patterns-30-orange.svg)](SKILL.md)

---

## What it does

Humanizer scans text for the most common signs of AI-generated writing and rewrites them into natural, human-sounding prose. It is based on Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, maintained by WikiProject AI Cleanup — a collection of patterns observed across thousands of AI-generated texts.

The skill runs a **draft → audit → final rewrite** loop: it rewrites, then explicitly asks itself what still sounds like AI, then fixes those remaining tells.

### 30 patterns detected

Grouped into five categories:

| Category | Examples |
|---|---|
| **Content** | Significance inflation, notability name-dropping, promotional language, vague attributions, formulaic challenge sections |
| **Language** | AI vocabulary overuse, copula avoidance, rule of three, synonym cycling, false ranges, passive voice |
| **Style** | Em dashes (hard cut), boldface overuse, inline-header lists, title-case headings, emojis, curly quotes |
| **Communication** | Chatbot artifacts, knowledge-cutoff disclaimers, speculative gap-filling, sycophantic tone |
| **Filler & hedging** | Filler phrases, excessive hedging, generic conclusions, hyphenated word pairs, persuasive authority tropes, signposting, fragmented headers, diff-anchored writing |

---

## Installation

### Automatic (recommended)

```bash
git clone https://github.com/blader/humanizer.git
cd humanizer
chmod +x install.sh
./install.sh
```

Or install directly without cloning:

```bash
curl -sSL https://raw.githubusercontent.com/blader/humanizer/main/install.sh | bash
```

The installer will ask where to install:

```
╔══════════════════════════════════════╗
║       🤖  Humanizer Installer        ║
╚══════════════════════════════════════╝

Wohin soll Humanizer installiert werden?

  1) Claude Code      (~/.claude/skills/humanizer)
  2) OpenCode         (~/.config/opencode/skills/humanizer)
  3) Antigravity IDE  (~/.gemini/config/skills/humanizer)
  4) Alle drei
```

### Manual

#### Claude Code

```bash
mkdir -p ~/.claude/skills/humanizer
cp SKILL.md ~/.claude/skills/humanizer/
cp SKILL_DE.md ~/.claude/skills/humanizer/   # optional: German version
```

#### OpenCode

```bash
mkdir -p ~/.config/opencode/skills/humanizer
cp SKILL.md ~/.config/opencode/skills/humanizer/
cp SKILL_DE.md ~/.config/opencode/skills/humanizer/   # optional: German version
```

> **Note:** OpenCode also scans `~/.claude/skills/` for compatibility, so if you use both tools, a single clone into `~/.claude/skills/humanizer/` is enough.

#### Antigravity IDE

```bash
mkdir -p ~/.gemini/config/skills/humanizer
cp SKILL.md ~/.gemini/config/skills/humanizer/
cp SKILL_DE.md ~/.gemini/config/skills/humanizer/   # optional: German version
```

---

## Usage

### English

```
/humanizer

[paste your text here]
```

### German

```
/humanizer-de

[füge deinen Text hier ein]
```

Or ask the model directly:

```
Please humanize this text: [your text]
```

```
Humanisiere diesen Text: [dein Text]
```

### Voice calibration

Provide a sample of your own writing and the skill will match your personal style — sentence rhythm, word choices, quirks — instead of producing generic "clean" output:

```
/humanizer

Here's a sample of my writing for voice matching:
[paste 2-3 paragraphs of your own writing]

Now humanize this text:
[paste AI text to humanize]
```

The German version supports the same:

```
/humanizer-de

Hier ist eine Schreibprobe zur Stilanpassung:
[eigene 2-3 Absätze]

Jetzt humanisiere das:
[KI-Text zum Überarbeiten]
```

---

## Example

**Before (AI-sounding):**
> Great question! Here is an essay on this topic. I hope this helps!
>
> AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development. In today's rapidly evolving technological landscape, these groundbreaking tools—nestled at the intersection of research and practice—are reshaping how engineers ideate, iterate, and deliver, underscoring their vital role in modern workflows.
>
> At its core, the value proposition is clear: streamlining processes, enhancing collaboration, and fostering alignment. It's not just about autocomplete; it's about unlocking creativity at scale, ensuring that organizations can remain agile while delivering seamless, intuitive, and powerful experiences to users. The tool serves as a catalyst. The assistant functions as a partner. The system stands as a foundation for innovation.

**After (humanized):**
> AI coding assistants can make you faster at the boring parts. Not everything. Definitely not architecture.
>
> They're great at boilerplate: config files, test scaffolding, repetitive refactors. They're also great at sounding right while being wrong. I've accepted suggestions that compiled, passed lint, and still missed the point because I stopped paying attention.
>
> The productivity metrics are slippery. GitHub can say Copilot users "accept 30% of suggestions," but acceptance isn't correctness, and correctness isn't value. If you don't have tests, you're basically guessing.

---

## Files

| File | Description |
|------|-------------|
| `SKILL.md` | English skill — 30 patterns |
| `SKILL_DE.md` | German skill — `humanizer-de`, 30 Muster auf Deutsch |
| `install.sh` | Interactive installer for Claude Code, OpenCode, and Antigravity IDE |
| `AGENTS.md` | Guidance for AI coding agents working in this repo |

---

## References

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — primary source
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) — the community maintaining the guide

---

## Version history

- **2.7.0** — Added `SKILL_DE.md` (German, 30 patterns); added `install.sh` with support for Claude Code, OpenCode, and Antigravity IDE; added pattern #30 (diff-anchored writing); made em/en dashes a hard cut rather than "use sparingly"; expanded #21 to cover speculative gap-filling ("maintains a low profile"). 30 patterns total.
- **2.6.0** — Cleanup pass: consolidated the duplicated workflow sections, gated the personality guidance to content where voice is wanted, removed the model-fingerprinting subsection, and condensed the worked example. No change to the 29 patterns.
- **2.5.1** — Added a passive-voice / subjectless-fragment rule, raising the total to 29 patterns.
- **2.5.0** — Added patterns for persuasive framing, signposting, and fragmented headers; expanded negative parallelisms to cover tailing negations; tightened wording around em dash overuse; fixed frontmatter wording to use "filler phrases".
- **2.4.0** — Added voice calibration: match the user's personal writing style from samples.
- **2.3.0** — Added pattern #25: hyphenated word pair overuse.
- **2.2.0** — Added a final "obviously AI generated" audit + second-pass rewrite prompts.
- **2.1.1** — Fixed pattern #18 example (curly quotes vs straight quotes).
- **2.1.0** — Added before/after examples for all 24 patterns.
- **2.0.0** — Complete rewrite based on raw Wikipedia article content.
- **1.0.0** — Initial release.

---

## Author

Made by [@voiscko](https://github.com/voiscko).

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

MIT
