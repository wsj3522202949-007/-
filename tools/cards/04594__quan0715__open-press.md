---
id: tool-04594
type: tool
area: 库
status: active
tags: [TypeScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 本地写作]
title: open-press
summary: 搭大纲/分卷/节拍
source: https://github.com/quan0715/open-press
created: 2026-07-18
updated: 2026-07-18
no: 4594
category: 五、写作 IDE / 本地优先工作台 库
repo: quan0715/open-press
stars: 10
url: https://github.com/quan0715/open-press
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 911b7c989e19e759
  - methods/QUICK_START.md
---

# quan0715/open-press

- **分类**：五、写作 IDE / 本地优先工作台 库
- **链接**：https://github.com/quan0715/open-press
- **Stars**：10
- **语言**：TypeScript
- **License**：MIT
- **Topics**：a4, agent-skills, ai-agents, ai-first, astro, claude-code, cli, codex, copilot, cursor, documents, editorial, mdx, monorepo, pdf, react, typescript, writing
- **GitHub 描述**：AI-first fixed-layout document workspaces. Your AI agent writes proposals, whitepapers, theses, books — A4, PDF, web reader.
- **本地描述**：AI-first fixed-layout document workspaces. Your AI agent writes proposals, whitepapers, theses, books — A4, PDF, web reader.
- **拉取时间**：2026-07-25 17:49:43

---

# open-press

> AI-first fixed-layout document framework. Creative skills decide what to make; OpenPress handles the workbench, inline editing, comment markers, rendering, PDF/image/Word export, and deploy plumbing.

[![npm](https://img.shields.io/npm/v/@open-press/cli?label=%40open-press%2Fcli&color=black)](https://www.npmjs.com/package/@open-press/cli)
[![cli downloads](https://img.shields.io/npm/dm/%40open-press%2Fcli?label=cli%20downloads&color=black)](https://www.npmjs.com/package/@open-press/cli)
[![core downloads](https://img.shields.io/npm/dm/%40open-press%2Fcore?label=core%20downloads&color=black)](https://www.npmjs.com/package/@open-press/core)
[![Landing](https://img.shields.io/badge/site-open--press.dev-black)](https://open-press.dev)
[![License](https://img.shields.io/badge/license-MIT-black)](LICENSE)

![OpenPress workbench showing a fixed-layout document page with outline navigation](https://github.com/quan0715/open-press/blob/main/docs/assets/openpress-readme-hero-screenshot-wide.png)

OpenPress is for artifacts where **content keeps changing but the output format must stay stable**: proposals, whitepapers, reports, course notes, books, social cards, and slide decks.

## Start

Prerequisite: Node.js 20 or newer. Use Node.js 24 for framework development and Cloudflare Pages builds.

```bash
npm create @open-press my-deck -- --type slides
cd my-deck
npm run dev
```

The create package installs the framework packages and OpenPress skills. Open the local Vite URL, usually `http://127.0.0.1:5173/workspace`.

## Create With AI

Open the workspace in a skill-aware agent such as Claude Code or Codex CLI:

```bash
claude
# or
codex
```

Then ask naturally:

```txt
我想寫一份投資人提案，幫我起手。
```

Creation is split by artifact type:

- `openpress-create-pages` creates page-based documents.
- `openpress-create-slide` creates slide decks.
- `openpress` owns CLI lifecycle, validation, rendering, export, and routing.
- `openpress-upgrade` owns package upgrades and workspace migration QA.

For Copilot Chat or other tools that do not auto-discover `SKILL.md`, see [manual agent setup](https://github.com/quan0715/open-press/blob/main/docs/skills.md#manual-agent-setup).

### Skills

`npm create @open-press` installs skills automatically. To install or update them separately:

```bash
# Install
npx skills add quan0715/open-press

# Update to latest
npm run openpress:skills
# or, in core-only workspaces:
node node_modules/@open-press/core/engine/cli.mjs skills:sync .
```

Skills land in `.agents/skills/` (universal) and `.claude/skills/` (Claude Code). They are read automatically by Claude Code, Cursor, Codex, Gemini CLI, Cline, Warp, and most other skill-aware agents — no manual loading required.

### Bootstrap Prompts

Use these when the agent does not yet have the OpenPress skills installed.

**Create a new workspace (empty folder, no skills):**

```txt
Run `npx skills add quan0715/open-press` to install the OpenPress skills.
Once installed, use the openpress-create-pages or openpress-create-slide skill
to set up a new workspace or add a Press to this folder.
```

**Upgrade an existing workspace:**

```txt
Use the openpress-upgrade skill.
It updates framework packages and skills, reads applicable migration docs,
scans press/ source, applies confirmed migrations, and loops through Migration QA.
```

## What You Get

- Fixed-layout pages: A4, social formats, slide 16:9, or custom presets.
- Press Tree rendering from folder entries such as `press/slide/press.tsx`.
- Multi-Press workspaces: documents, cards, and slides in one project.
- Tailwind-first authoring with OpenPress semantic slide classes and protocol layouts.
- Local workbench with preview, comments, mentions, and image export.
- PDF/Word export and Cloudflare Pages deploy workflow.
- Portable skills under `.agents/skills/` and `.claude/skills/`.

## Framework Development

This repo includes a tracked dogfood workspace in `press/`.

```bash
pnpm run dev:workspace  # dogfood press / workbench
pnpm run dev:web        # open-press.dev landing site
pnpm run build          # render every Press
pnpm run openpress:pdf  # export PDF
pnpm run openpress:word # export Word DOCX
```

## More

| Want to | See |
| --- | related:
  - methods/QUICK_START.md
--- |
| CLI commands | [docs/cli.md](https://github.com/quan0715/open-press/blob/main/docs/cli.md) |
| Press Tree model | [docs/press-tree.md](https://github.com/quan0715/open-press/blob/main/docs/press-tree.md) |
| Workbench UI | [docs/workbench.md](https://github.com/quan0715/open-press/blob/main/docs/workbench.md) |
| Skills and routing | [docs/skills.md](https://github.com/quan0715/open-press/blob/main/docs/skills.md) |
| Release / deploy | [docs/release-and-deploy.md](https://github.com/quan0715/open-press/blob/main/docs/release-and-deploy.md) |
| Contribute | [CONTRIBUTING.md](https://github.com/quan0715/open-press/blob/main/CONTRIBUTING.md) and [AGENTS.md](https://github.com/quan0715/open-press/blob/main/AGENTS.md) |
| Changelog | [CHANGELOG.md](https://github.com/quan0715/open-press/blob/main/CHANGELOG.md) |

## License

MIT - see [LICENSE](https://github.com/quan0715/open-press/blob/main/LICENSE).
