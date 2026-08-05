---
id: tool-00907
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: alchemy
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/fernforge/alchemy
created: 2026-07-18
updated: 2026-07-18
no: 907
category: 二、网文 / 长篇 AI 写作系统 库
repo: fernforge/alchemy
stars: 0
url: https://github.com/fernforge/alchemy
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# fernforge/alchemy

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/fernforge/alchemy
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：ai-writing, claude, coding-agent, commit-messages, copilot, cursor, developer-tools, documentation, humanize-ai, llm, mcp, prose, readme, style-guide, technical-writing, writing-assistant
- **GitHub 描述**：Turn AI prose into human-quality writing. A drop-in ruleset that stops your coding agent from writing like an LLM.
- **本地描述**：Turn AI prose into human-quality writing. A drop-in ruleset that stops your coding agent from writing like an LLM.
- **拉取时间**：2026-07-23 23:05:30

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<p align="center">
  <img src="./cover.png" alt="Alchemy — write like a human, not an LLM" width="100%">
</p>

# Alchemy

Alchemy is a drop-in ruleset that stops your AI coding agent from writing like an LLM: no em-dash pile-ups, no "not just X, it's Y", no stray *delve*. You add it once, your agent reads it before it writes, and the READMEs, commits, and docs it produces start sounding like a person wrote them.

Turn lead into gold. It's one file, about 1000 tokens, that lives next to your agent's other instructions: [`ALCHEMY.md`](./ALCHEMY.md). Everything else here just gets it into your project.

## How do I stop my AI from writing like an LLM?

Install it in your project and point your agent at it. Pick whichever fits your stack:

```bash
# Node / npm
npx @fernforge/alchemy init

# Python / pip
pip install alchemy-writing
alchemy init
```

`init` writes `ALCHEMY.md` into your project and links it from whatever agent config you already have: `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, or Copilot instructions. From then on the agent reads the rules as part of its normal context. To print the ruleset to stdout without installing anything:

```bash
npx @fernforge/alchemy print   # or: alchemy print
```

Prefer to do it by hand? Copy [`ALCHEMY.md`](./ALCHEMY.md) into your repo and reference it from your agent's instruction file. That's the whole mechanism. No service, no API, no account.

## Before and after

Here's the kind of sentence Alchemy catches. Same fact, two ways of saying it:

**Before**

> Redis isn't just a database — it's a powerful, robust caching layer that unlocks the full potential of your entire stack.

**After**

> Redis is an in-memory store. Put your cache and sessions in it and your database stops being the bottleneck.

The "before" stacks four tells in one sentence: the "isn't just X, it's Y" non-contrast, the adjective pile (`powerful`, `robust`), the lone dramatic em-dash, and "unlocks the full potential". None of it says what Redis does. The "after" drops all of it and states one concrete thing you can act on. That's the whole move, applied everywhere the agent writes.

## Which LLM tells does it remove?

The concrete ones, by name:

- Empty contrasts: "not just X, it's Y", "it's not about A, it's about B".
- Staccato trios and rule-of-three padding: "fast, reliable, scalable", "No X. No Y. Just Z."
- Stacked adjectives standing in for facts: robust, seamless, powerful, comprehensive.
- Em-dash pile-ups. The real tell is density, so the rule is: use them rarely.
- Filler vocabulary: delve, leverage, harness, unlock, elevate, tapestry, realm, showcase.
- Throat-clearing openers ("In today's fast-paced world", "At its core") and recap closers ("In conclusion", "Ultimately").
- Restating the prompt before answering it.

The fix is never a synonym swap. It's replacing the vague word with a specific fact: not "robust" but "handles 10k req/sec". The rules push the agent toward the fact.

The principle underneath: no single word proves a machine wrote something. The signal is many of these clustered together over flat, evenly-weighted text. Alchemy targets the clustering, so it thins the tells without stripping a word that's genuinely the right one.

## Use it with Claude, Cursor, or Copilot

`init` detects the config files already in your project and links the ruleset from them, so the same `ALCHEMY.md` works across agents:

- Claude Code / Claude reads it via `CLAUDE.md`.
- Cursor reads it via `.cursorrules`.
- Copilot reads it via its instructions file.
- Any agent that supports `AGENTS.md` picks it up there.

One ruleset, whichever agent you're driving.

## Use it as an MCP server

To serve the rules on demand across every project instead of committing a file to each repo, run Alchemy as an MCP server. Add it to your client config (Claude Desktop, Cursor, Cline):

```json
{
  "mcpServers": {
    "alchemy": { "command": "npx", "args": ["-y", "@fernforge/alchemy-mcp"] }
  }
}
```

It exposes a `get_writing_rules` tool and an `alchemy://rules` resource, so any MCP-aware agent can pull the ruleset when it's about to write prose. See [`mcp/`](./mcp) for details.

## Three ways to install, one ruleset

All three ship the same rules from the same source, so pick by your toolchain and mix freely:

- npm: `@fernforge/alchemy` — `npx @fernforge/alchemy init`
- PyPI: `alchemy-writing` — `pip install alchemy-writing`
- MCP: `@fernforge/alchemy-mcp` — `npx @fernforge/alchemy-mcp`

## Where the rules come from

They're grounded in what people actually flag as AI writing, not guesses: Wikipedia's "Signs of AI writing", the Kobak et al. study measuring which words spiked in research papers after ChatGPT, Pangram's phrase-frequency data, and the long-running arguments on Reddit and in r/Professors about spotting it. It's kept short on purpose: concrete guidance an agent can hold in context, not an essay.

This README follows its own rules. If it reads fine, that's the pitch.

## Contributing

Found a tell it misses? Open an issue or a PR with a real before-and-after pair. Concrete examples are worth more than new abstract rules.

Edit the root [`ALCHEMY.md`](./ALCHEMY.md) only. The copies under `python/` and `mcp/` are generated from it by `node scripts/sync-rules.mjs`, and CI fails if they drift. The npm, PyPI, and MCP packages publish from GitHub Releases (see [`.github/workflows`](./.github/workflows)).

## License

MIT
