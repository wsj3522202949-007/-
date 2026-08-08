---
id: tool-03149
type: tool
area: 库
status: active
tags: [Claude插件, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: portage
summary: Claude Code 插件式写作流
source: https://github.com/birdseyeglobal/portage
created: 2026-07-18
updated: 2026-07-18
no: 3149
category: 六、多 Agent 小说生产 / 叙事引擎 库
repo: birdseyeglobal/portage
stars: 0
url: https://github.com/birdseyeglobal/portage
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 9a72d9face2de86b
  - methods/网文写作最强SOP.md
---

# birdseyeglobal/portage

- **分类**：六、多 Agent 小说生产 / 叙事引擎 库
- **链接**：https://github.com/birdseyeglobal/portage
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：ai-assistant, ai-skills, claude-code, codex, content, cursor, marketplace, open-skills-standard, opencode, writing
- **GitHub 描述**：A marketplace for portable AI-assistant extensions. Skills work in any Open Skills Standard tool (Claude Code, Cursor, Codex, OpenCode, ...); Claude Code users also get plugins that bundle skills, commands, and agents.
- **本地描述**：A marketplace for portable AI-assistant extensions. Skills work in any Open Skills Standard tool (Claude Code, Cursor, Codex, OpenCode, ...); Claude Code users also get plugins that bundle skills, commands, and agents.
- **拉取时间**：2026-07-23 23:51:00

related:
  - methods/网文写作最强SOP.md
---

# Portage

[![CI](https://github.com/grootenberg/Portage/actions/workflows/ci.yml/badge.svg)](https://github.com/grootenberg/Portage/actions/workflows/ci.yml)

A marketplace for portable AI-assistant extensions.

Portage packages skills, commands, and agents as Claude Code plugins _and_ exposes the skills under `.agents/skills/` so tools that follow the Open Skills Standard — Cursor, Codex, OpenCode, and others — can use them without a separate install. Skills are the portable unit: they work anywhere the standard is supported. The plugin format is the richer unit: Claude Code users get skills bundled with commands and agents.

## What's inside

- **`plugins/`** — each plugin is a self-contained directory with its own `plugin.json`, agents, commands, and skills.
- **`.claude-plugin/marketplace.json`** — the registry Claude Code reads.
- **`.claude/skills/`** — symlinks to every skill across every plugin. Populated by the link script.
- **`.agents/skills/`** — a symlink to `.claude/skills/`. Point any Open Skills Standard tool here.

## Install a plugin in Claude Code

Add the marketplace, then install the plugin:

```text
/plugin marketplace add grootenberg/portage
/plugin install prose@portage
/plugin install styleguide@portage
```

## Use skills in other tools

The skills live as self-contained directories under `.agents/skills/`. Each directory has a `SKILL.md` plus any bundled files (`references/`, `scripts/`, `assets/`). Tools that read the Open Skills Standard format can load them directly.

Point your tool at `.agents/skills/` — no extra setup.

## Add a plugin or skill

1. Drop the plugin into `plugins/<plugin-name>/` following the existing structure.
2. Register it in `.claude-plugin/marketplace.json`.
3. Run the link script:

   ```sh
   ./scripts/link-marketplace-skills.sh
   ```

The script symlinks each skill directory into `.claude/skills/` and maintains the `.agents/skills` symlink. It detects collisions on skill names, cleans up stale symlinks, and flags duplicate frontmatter names.

Re-run the script only when skills are added or removed. Edits inside an existing skill directory propagate through the symlink automatically.

## Available plugins

- **[prose](https://github.com/birdseyeglobal/portage/tree/main/plugins/prose/)** — composable content quality toolkit. Seven skills for writing craft, citations, SEO, video scripts, social posts, transcript cleanup, and AI artifact removal, plus two commands that chain them into editorial workflows.
- **[styleguide](https://github.com/birdseyeglobal/portage/tree/main/plugins/styleguide/)** — standalone organization-wide style guide for internal updates, customer-facing notes, docs, GitHub work, stakeholder communication, and AI artifact cleanup.
- **[geo](https://github.com/birdseyeglobal/portage/tree/main/plugins/geo/)** — generative engine optimization workflows for AI-search prompt design, citation analysis, content briefs, sitemap strategy, SEO competitor research, and visibility reporting.

## License

MIT. See [LICENSE](https://github.com/birdseyeglobal/portage/blob/main/LICENSE).

## Contributing

See [CONTRIBUTING.md](https://github.com/birdseyeglobal/portage/blob/main/CONTRIBUTING.md). Portage is early; open an issue before starting significant work.
