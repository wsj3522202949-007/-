---
id: tool-00103
type: tool
area: 库
status: active
tags: [TTS, Claude插件, Rust, 协议未明, 本地优先, 英文文档, 本地写作]
title: comaster
summary: 小说转语音/有声书
source: https://github.com/denczh/comaster
created: 2026-07-18
updated: 2026-07-18
no: 103
category: 二、网文 / 长篇 AI 写作系统 库
repo: denczh/comaster
stars: 0
url: https://github.com/denczh/comaster
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
content_hash: 203cb729fb69bacf
  - methods/最强写作方法论_全球最强综合版.md
---

# denczh/comaster

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/denczh/comaster
- **Stars**：0
- **语言**：Rust
- **License**：None
- **Topics**：—
- **GitHub 描述**：Desktop GM assistant and fiction-world authoring environment (Rust + Slint)
- **本地描述**：Desktop GM assistant and fiction-world authoring environment (Rust + Slint)
- **拉取时间**：2026-07-23 22:41:58

---

# Comaster

Comaster is a desktop application written in Rust and Slint that assists a human game master (GM) during tabletop role-playing sessions, and serves as a fiction-world authoring environment. It hosts the GM workflow, a Claude-based AI co-pilot, authoring editors, and — in future iterations — an embedded Claude Code terminal.

## Components

| Crate | Description |
|-------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| **pharos** | Universe, geography, locations, connections, and nested levels of detail (LOD), inspired by OpenStreetMap extended for narrative. |
| **gens** | Creatures, objects, bonds, motivations, and NPC narrative voice. |
| **codex** | Adapter to Foundry VTT for querying table state, character sheets, and rolls; includes a Year Zero Engine (YZE) rule-doctrine layer. |
| **nexus** | Narrative structure: acts, scenes, open threads, beats, and tension clocks. |
| **vigil** | Knowledge and witnesses: who knows what, when, in an append-only register. |

Each component exposes a library crate for direct use by the Comaster application and a binary crate (`<component>-mcp`) that runs as an MCP server for the AI co-pilot.

Additional crates:

- **shared** — Cross-cutting identifiers and error types.
- **copilot** — Orchestration layer for the Claude AI co-pilot.
- **ui** — Reusable Slint UI components.

## Building

```sh
cargo build --workspace
cargo run -p comaster
```

Requires a stable Rust toolchain. Install via [rustup](https://rustup.rs/).

## Development

```sh
just fmt      # format
just clippy   # lint
just test     # test suite
just run-mcp pharos   # start the Pharos MCP server
```
