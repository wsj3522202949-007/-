---
id: tool-04802
type: tool
area: 库
status: active
tags: [Claude插件, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: mysterycode-skill
summary: Claude Code 插件式写作流
source: https://github.com/the-time-forever/mysterycode-skill
created: 2026-07-18
updated: 2026-07-18
no: 4802
category: 一、去 AI 味 / Humanizer 库
repo: The-time-forever/mysterycode-skill
stars: 1
url: https://github.com/the-time-forever/mysterycode-skill
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 627f60df62a60101
  - methods/改稿润色指令库.md
---

# The-time-forever/mysterycode-skill

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/the-time-forever/mysterycode-skill
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Evidence-based Claude Code skill for analyzing mystery novels and detective fiction. Extracts EPUB text, tracks clues   and anomalies, checks consistency across chapters, separates annotation notes from narrative evidence, and generates   Obsidian-ready vault notes, character pages, and investigation templates.
- **本地描述**：Evidence-based Claude Code skill for analyzing mystery novels and detective fiction. Extracts EPUB text, tracks clues   and anomalies, checks consistency across chapters, separates annotation notes from narrative evidence, and generates   Obsidian-ready vault notes, character pages, and investigation templates.
- **拉取时间**：2026-07-25 17:54:50

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Mystery Analysis Skill for Claude Code

Evidence-based mystery and detective fiction analysis for Claude Code.

This skill is built for readers who want more than a plot summary. It helps an agent read extracted book text, analyze chapters for clues and anomalies, and maintain an Obsidian vault with structured notes for characters, locations, objects, and timeline tracking.

## Highlights

- Works well for mystery novels and detective fiction
- Supports EPUB-based workflows through agent-run extraction
- Produces Obsidian-ready vaults instead of one-off answers
- Tracks clues, anomalies, foreshadowing, and cross-chapter consistency
- Organizes entities into `Characters/`, `Locations/`, `Objects/`, and `Timeline/`

## Install

Install from this repository:

```bash
git clone https://github.com/The-time-forever/mysterycode-skill.git
/plugin add /path/to/mysterycode-skill
```

Or copy it into the Claude skills directory:

```bash
cp -r mysterycode-skill ~/.claude/skills/
```

On Windows, copy the folder to `C:\Users\<you>\.claude\skills\`.

### Verify

```bash
claude list-skills
```

Look for `mystery-analysis`.

## What It Does

- Read mystery novels from EPUB-derived text and other text formats
- Analyze chapters for details, anomalies, foreshadowing, and insights
- Check consistency across chapters and timelines
- Generate relationship-oriented reading notes
- Build and maintain an Obsidian vault with structured folders and linked pages

## Typical Use

You do not need to run the Python scripts manually in normal use. The agent should call them when needed.

Example prompts:

```text
Read this EPUB, analyze chapter 1, and create an Obsidian vault in ./mystery-vault-book

Continue analyzing chapter 2 and update the existing Obsidian vault

Check this mystery vault for missing links, empty pages, and stale indexes
```

## Obsidian Output

This skill is designed to produce and maintain an Obsidian vault, not just isolated chapter summaries.

Typical vault structure:

```text
vault/
├── Books/[书名]/
│   ├── 00-书籍信息.md
│   ├── 01-第一章分析.md
│   └── ...
├── Analysis/
├── Characters/
├── Locations/
├── Objects/
├── Timeline/
└── Home.md
```

The vault is meant to stay navigable as it grows:

- `Books/` stores chapter analysis
- `Analysis/` stores cross-chapter clue tracking
- `Characters/`, `Locations/`, and `Objects/` store entity pages
- `Timeline/` stores chronology and flow notes
- `Home.md` acts as the vault entry page

## How It Works

1. The agent extracts readable chapter text from EPUB when needed.
2. The agent analyzes selected chapters using evidence-first close reading.
3. The agent writes or updates the Obsidian vault.
4. The agent synchronizes chapter indexes, clue tracking, and entity pages.
5. The agent validates the vault to catch missing links, empty pages, and stale navigation.

## Behavior Notes

- EPUB use is intentionally two-step: extract first, then analyze.
- EPUB extraction supports `zh`, `en`, and `--language auto`.
- Extracted `notes` are reference context, not primary plot evidence.
- Vault output location is user-controlled.
- If extraction fails, the skill should stop instead of guessing from prior knowledge.
- Failed extraction should be retried through controlled parameters such as `--language`, `--include-item`, `--exclude-item`, or `--disable-frontmatter-filter`.
- Chapter updates should also update book info, clue tracking, recent-analysis links, and minimal entity pages.

## Repository Layout

```text
mysterycode-skill/
├── SKILL.md
├── skill.json
├── scripts/
│   ├── extract_epub.py
│   └── validate_vault.py
├── templates/
│   ├── chapter-analysis-template.md
│   ├── character-card-template.md
│   ├── location-card-template.md
│   ├── object-card-template.md
│   ├── timeline-note-template.md
│   └── clue-tracking-template.md
└── docs/
    ├── README_CN.md
    ├── USAGE.md
    ├── prompt.md
    ├── examples.md
    ├── PROJECT_OVERVIEW.md
    └── CHANGELOG.md
```

## More Docs

- Chinese overview: `docs/README_CN.md`
- Usage guide: `docs/USAGE.md`
- Prompt rules: `docs/prompt.md`
- Project overview: `docs/PROJECT_OVERVIEW.md`
- Examples: `docs/examples.md`
- Changelog: `docs/CHANGELOG.md`

## License

MIT
