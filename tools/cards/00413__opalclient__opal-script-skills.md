---
id: tool-00413
type: tool
area: 库
status: active
tags: [Claude插件, JavaScript, 协议宽松, 本地优先, 英文文档, 本地写作]
title: opal-script-skills
summary: Claude Code 插件式写作流
source: https://github.com/opalclient/opal-script-skills
created: 2026-07-18
updated: 2026-07-18
no: 413
category: 二、网文 / 长篇 AI 写作系统 库
repo: opalclient/opal-script-skills
stars: 0
url: https://github.com/opalclient/opal-script-skills
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# opalclient/opal-script-skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/opalclient/opal-script-skills
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A portable AI assistant skill for writing Opal scripts, with a cross-AI installer for Claude Code, Codex, Copilot, and Gemini.
- **本地描述**：A portable AI assistant skill for writing Opal scripts, with a cross-AI installer for Claude Code, Codex, Copilot, and Gemini.
- **拉取时间**：2026-07-23 22:51:10

---

# opal-script-skills

Portable AI-assistant **skills** for writing [Opal](https://opal.wtf) (Minecraft
utility client) JavaScript scripts, plus a cross-AI installer that drops the
skill into whatever assistant your project uses.

Opal ships a GraalVM-JS scripting system: scripts are `.js` files in the
client's `opal/scripts` folder. This repo teaches an AI assistant the real
scripting API (`registerScript` / modules / settings / events, the `renderer`
canvas, the `palette` command-palette views, dynamic islands, and the
default-deny sandbox model) so it stops inventing methods and writes scripts
that run.

The single **source of truth** is [`skills/opal-scripting/`](https://github.com/opalclient/opal-script-skills/tree/main/skills/opal-scripting/):

- [`SKILL.md`](https://github.com/opalclient/opal-script-skills/blob/main/skills/opal-scripting/SKILL.md): the skill (structure, settings,
  events, renderer + color rule, palette views, islands, the sandbox, common
  mistakes).
- [`reference.md`](https://github.com/opalclient/opal-script-skills/blob/main/skills/opal-scripting/reference.md): the module/settings/event
  model index, plus the `keys` table. Proxy globals are split by category:
  - [`reference/core.md`](https://github.com/opalclient/opal-script-skills/blob/main/skills/opal-scripting/reference/core.md): `client`,
    `notification`, `overlay`, `modules`, `mc`, `timer`, `ScriptList`.
  - [`reference/character.md`](https://github.com/opalclient/opal-script-skills/blob/main/skills/opal-scripting/reference/character.md):
    `player`, `movement`, `rotation`, `inventory`, `mc.interactionManager`.
  - [`reference/world.md`](https://github.com/opalclient/opal-script-skills/blob/main/skills/opal-scripting/reference/world.md): `world`,
    `esp`, the class globals (`BlockPos`, `Vec2f`, `Vec3d`, `Color`, hand
    constants), and the wrapper types the proxies return (`ScriptVec3`,
    `ScriptEntity`, `ScriptEffect`, `ScriptBox2D`, …).
  - [`reference/ui.md`](https://github.com/opalclient/opal-script-skills/blob/main/skills/opal-scripting/reference/ui.md): `renderer`,
    `palette`.
- [`palette-views.md`](https://github.com/opalclient/opal-script-skills/blob/main/skills/opal-scripting/palette-views.md): a complete
  palette-view example.

## Install

One command per assistant. Run it from your project root. No dependencies, no
network; it just renders the skill into the right place.

```bash
# Auto-detect which assistants this project uses and install for them:
npx @opalclient/opal-script-skills add

# Or target one explicitly:
npx @opalclient/opal-script-skills add --target claude-code
npx @opalclient/opal-script-skills add --target codex      # AGENTS.md
npx @opalclient/opal-script-skills add --target gemini      # GEMINI.md
npx @opalclient/opal-script-skills add --target copilot     # .github/copilot-instructions.md
npx @opalclient/opal-script-skills add --target cursor      # .cursor/rules/opal-scripting.md
npx @opalclient/opal-script-skills add --target windsurf    # .windsurfrules
npx @opalclient/opal-script-skills add --target generic     # OPAL_SCRIPTING.md

# Everything at once:
npx @opalclient/opal-script-skills add --all

# List supported targets:
npx @opalclient/opal-script-skills list
```

The `npx` short name `opal-skills` works too. Use `--dir <path>`
to install into a directory other than the current one.

### What each target writes

| Target | Path | Form |
| --- | --- | related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- |
| `claude-code` | `.claude/skills/opal-scripting/` | full skill files |
| `cursor` | `.cursor/rules/opal-scripting.md` | full skill (one file) |
| `generic` | `OPAL_SCRIPTING.md` | full skill (one file) |
| `codex` | `AGENTS.md` | delimited block |
| `gemini` | `GEMINI.md` | delimited block |
| `copilot` | `.github/copilot-instructions.md` | delimited block |
| `windsurf` | `.windsurfrules` | delimited block |

Block targets insert a `<!-- opal-scripting:start -->…<!-- opal-scripting:end -->`
region and leave the rest of your file untouched. Re-running is idempotent: the
block is replaced, never duplicated.

When you pass neither `--target` nor `--all`, the installer detects markers in
the directory (`.claude/`, `AGENTS.md`, `GEMINI.md`, `.github/`, `.cursor/`,
`.windsurfrules`) and installs the matching targets. If it finds none, it installs
`generic`.

## Manual adapters

Don't want to run the installer? Copy a ready-made surface from
[`adapters/`](https://github.com/opalclient/opal-script-skills/tree/main/adapters/):

- [`adapters/claude-code/`](https://github.com/opalclient/opal-script-skills/tree/main/adapters/claude-code/): Claude Code **plugin** form
  (`.claude-plugin/plugin.json` + `skills/opal-scripting/` + a
  `/new-opal-script` command that scaffolds a new script file).
- [`adapters/codex/AGENTS.md`](https://github.com/opalclient/opal-script-skills/blob/main/adapters/codex/AGENTS.md)
- [`adapters/gemini/GEMINI.md`](https://github.com/opalclient/opal-script-skills/blob/main/adapters/gemini/GEMINI.md)
- [`adapters/copilot/.github/copilot-instructions.md`](https://github.com/opalclient/opal-script-skills/blob/main/adapters/copilot/.github/copilot-instructions.md)

## In-client docs

The authoritative reference is the client itself. Reference scripts ship in the
Opal install under `opal/scripts` (`ScriptScaffold.js`, `Chomp.js`); read them
for idiomatic usage. Scripts run in a default-deny sandbox, and community
scripts are additionally quarantined to `opal/scripts/pending` behind an
explicit **"Trust & run"**; see [`SECURITY.md`](https://github.com/opalclient/opal-script-skills/blob/main/SECURITY.md).

Finished scripts go in the official
[`opalclient/scripts`](https://github.com/opalclient/scripts) repo:
folder-per-script, a `manifest.json`, a TS template bundled via esbuild, and a
PR flow with CI gates — releases are tagged `<id>@<version>`. Its flagship
example is **Chomp**, a roguelite arcade script that exercises `storage`.

## For AI agents

If you are an AI assistant working in this repo:

- [`CLAUDE.md`](https://github.com/opalclient/opal-script-skills/blob/main/CLAUDE.md): the mental model for this repo and how to change it.
- [`llms.txt`](https://github.com/opalclient/opal-script-skills/blob/main/llms.txt): a compact, link-first map of everything here.
- [`skills/opal-scripting/`](https://github.com/opalclient/opal-script-skills/tree/main/skills/opal-scripting/): the source of truth for
  the Opal scripting API. **Use only the API documented there**; do not invent
  methods.

## Development

```bash
npm test        # node --test
```

The installer is dependency-free ESM (`bin/install.mjs`). Edits to the skill
live in `skills/opal-scripting/`; the `adapters/` surfaces are regenerated from
it (see [`CONTRIBUTING.md`](https://github.com/opalclient/opal-script-skills/blob/main/CONTRIBUTING.md)).

## License

[MIT](https://github.com/opalclient/opal-script-skills/blob/main/LICENSE) © Opal.
