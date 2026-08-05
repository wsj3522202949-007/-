---
id: tool-05703
type: tool
area: 库
status: active
tags: [Claude插件, TypeScript, 协议宽松, 本地优先, 英文文档, 本地写作]
title: agent-dx
summary: Claude Code 插件式写作流
source: https://github.com/lannguyensi/agent-dx
created: 2026-07-18
updated: 2026-07-18
no: 5703
category: 一、去 AI 味 / Humanizer 库
repo: LanNguyenSi/agent-dx
stars: 2
url: https://github.com/lannguyensi/agent-dx
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# LanNguyenSi/agent-dx

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/lannguyensi/agent-dx
- **Stars**：2
- **语言**：TypeScript
- **License**：MIT
- **Topics**：agent-tools, ai-linting, ast, code-quality, dx, pr-review, pre-commit, slop-detector, typescript
- **GitHub 描述**：Monorepo workshop for agent-development tooling: orchestrator-workflow and okf-kit ship on npm; slop-detector is the AI-slop linter for PRs.
- **本地描述**：Monorepo workshop for agent-development tooling: orchestrator-workflow and okf-kit ship on npm; slop-detector is the AI-slop linter for PRs.
- **拉取时间**：2026-07-25 18:28:29

---

# agent-dx

A monorepo workshop for agent-development tooling: CLIs, linters, and playbooks built while shipping AI-agent coding workflows in practice. Two packages ship on npm; the rest are working tools used inside this workshop and its sibling repos.

## Shipping on npm

### orchestrator-workflow

Installer for an orchestrator-led agent workflow: a `.ai/` directory for run state, a marker-fenced policy section in `AGENTS.md`, and subagent definitions with preselected models for Claude Code, OpenAI Codex, and opencode.

```bash
npx orchestrator-workflow init
```

See `[packages/orchestrator-workflow](packages/orchestrator-workflow)` for the full install and usage guide.

### okf-kit

Validates knowledge bundles against the Open Knowledge Format (OKF) v0.1 spec: frontmatter shape, reserved files, link resolution, absolute-link warnings, `sources` shape.

```bash
npx okf-kit check path/to/bundle
```

See `[packages/okf-kit](packages/okf-kit)` for the full install and usage guide.

## slop-detector

`[`slop-detector`](packages/slop-detector)` is the AI-slop linter for PRs: it catches leaked tool-call XML, doubled `## Summary` headings, hedging openers, marketing adjectives, JSDoc on trivial getters, and other agent-generated tells across five rule packs (`agent-tics`, `prose-slop`, `comment-slop`, `code-slop`, `ui-slop`; some packs are opt-in). It runs in pre-commit, in CI as a status check, or ad-hoc against a path.

Not yet published to npm (the bare `slop-detector` name belongs to an unrelated third-party package), so it runs from a local build:

```bash
cd packages/slop-detector && npm install && npm run build && cd ../..
node packages/slop-detector/dist/cli.js check examples/slop-sample.md --explain
```

Full pack reference, sample output, the scan pipeline, and the rationale (including a data point from running it against 20 recently merged PRs): `[packages/slop-detector/README.md](packages/slop-detector/README.md)`.

## Packages

| Package | What it does | npm |
|---------|--------------|--related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| `[orchestrator-workflow](packages/orchestrator-workflow)` | Installer for an orchestrator-led agent workflow: `.ai/` run state, an `AGENTS.md` policy section, and subagent definitions with preselected models for Claude Code, Codex, and opencode. | published |
| `[okf-kit](packages/okf-kit)` | CLI that validates OKF v0.1 knowledge bundles: frontmatter shape, reserved files, link resolution, absolute-link warnings, `sources` shape. | published |
| `[slop-detector](packages/slop-detector)` | AI-slop linter for PRs: leaked tool-call XML, doubled Summary headings, hedging openers, marketing adjectives, and more across five rule packs. | not published (name taken; run from a local build) |
| `[agent-dev-kit](packages/agent-dev-kit)` | CLI scaffolding for AI agent projects: file layout, hooks, entrypoints. | not published |
| `[friction-log](packages/friction-log)` | Capture, query, and infer agent-workflow frictions. SQLite-backed, sink-pluggable, zero-config default. | not published |
| `[github-api-tool](packages/github-api-tool)` | TypeScript CLI for GitHub API operations (issues, PRs, commits, standup digests), JSON output for agents calling via `exec`. | private |
| `[git-batch-cli](packages/git-batch-cli)` | Run safe batch git operations across all repos under a folder: sync, status, dirty checks, fetch, with `--strict` for automation. | not published |
| `[agent-engineering-playbook](packages/agent-engineering-playbook)` | Guide for building production-ready AI agent systems. | doc package |
| `[agentic-coding-playbook](packages/agentic-coding-playbook)` | Practical playbook for teams using AI agents in coding. | doc package |

## Repo layout

`agent-dx` is a folder of independent packages, not an npm workspaces / pnpm / lerna monorepo. There is no root `package.json`, no workspace manifest, and no shared root `node_modules`. Each package under `packages/` carries its own `package.json`, install, build, test, and version, so the install pattern for any local-build package is the same one shown above for `slop-detector`:

```bash
cd packages/<name> && npm install && npm run build
```

If you only care about one package, work in its directory; nothing at the root needs to be set up first.

## Status

Experimental: each package has its own version, README, and CI. APIs may evolve at minor-version bumps. `orchestrator-workflow` and `okf-kit` are published to npm with tagged releases. `slop-detector` is deliberately unpublished (the bare name on npm belongs to an unrelated package) and ships an MCP server alongside the CLI. `agent-dev-kit`, `friction-log`, and `git-batch-cli` are functional CLIs, not yet on npm. `github-api-tool` is marked private in its own `package.json`. `agent-engineering-playbook` and `agentic-coding-playbook` are documentation packages, not code.

## Where this fits

`slop-detector` and the workshop around it contribute the authoring-side tooling to the [Project OS](https://github.com/LanNguyenSi/project-pilot) human-agent dev lifecycle. It sits alongside:

- [agent-planforge](https://github.com/LanNguyenSi/agent-planforge) plans
- [agent-tasks](https://github.com/LanNguyenSi/agent-tasks) coordinates
- [agent-grounding](https://github.com/LanNguyenSi/agent-grounding) verifies (evidence ledger, claim gate, hypothesis tracker)
- [agent-preflight](https://github.com/LanNguyenSi/agent-preflight) gates pushes
- [harness](https://github.com/LanNguyenSi/harness) declares + enforces the policy boundary that calls into all of the above

[scaffoldkit](https://github.com/LanNguyenSi/scaffoldkit) and [agent-planforge](https://github.com/LanNguyenSi/agent-planforge) are standalone tools used by [project-forge](https://github.com/LanNguyenSi/project-forge).
