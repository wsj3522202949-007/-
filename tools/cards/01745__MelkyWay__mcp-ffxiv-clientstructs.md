---
id: tool-01745
type: tool
area: 库
status: active
tags: [Claude插件, TypeScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: mcp-ffxiv-clientstructs
summary: Claude Code 插件式写作流
source: https://github.com/melkyway/mcp-ffxiv-clientstructs
created: 2026-07-18
updated: 2026-07-18
no: 1745
category: 二、网文 / 长篇 AI 写作系统 库
repo: MelkyWay/mcp-ffxiv-clientstructs
stars: 0
url: https://github.com/melkyway/mcp-ffxiv-clientstructs
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1a9658a44f0edc66
  - methods/最强写作方法论_全球最强综合版.md
---

# MelkyWay/mcp-ffxiv-clientstructs

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/melkyway/mcp-ffxiv-clientstructs
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：An MCP server that indexes the FFXIVClientStructs C# library and exposes it as searchable tools for any MCP-compatible AI assistant. Useful when writing Dalamud plugins.
- **本地描述**：An MCP server that indexes the FFXIVClientStructs C# library and exposes it as searchable tools for any MCP-compatible AI assistant. Useful when writing Dalamud plugins.
- **拉取时间**：2026-07-23 23:29:54

---

# mcp-xiv-clientstructs

An MCP server that indexes the [FFXIVClientStructs](https://github.com/aers/FFXIVClientStructs) C# library and exposes it as searchable tools for any MCP-compatible AI assistant. Useful when writing [Dalamud](https://github.com/goatcorp/Dalamud) plugins.

## Tools

| Tool | Description |
|------|-------------|
| `search_types` | Search types by name or namespace — returns brief results (no fields/methods) |
| `get_type` | Full type definition: fields with offsets, methods, size, inheritance |
| `list_namespaces` | All available namespaces |
| `get_namespace` | All types in a namespace (brief) |
| `refresh` | Run `git pull` on the repo and rebuild the index if the SHA changed |

## Environment variables

| Variable | Description |
|----------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `FFXIV_STRUCTS_REPO` | Path to a local clone of [FFXIVClientStructs](https://github.com/aers/FFXIVClientStructs) |
| `FFXIV_STRUCTS_INDEX` | Path where the server writes its `index.json` cache (does not need to exist beforehand) |

Both are required. The server will exit on startup if either is missing.

## Setup

**1. Clone FFXIVClientStructs somewhere:**
```bash
git clone https://github.com/aers/FFXIVClientStructs.git /path/to/ffxiv_clientstructs_repo
```

**2. Install and build:**
```bash
npm install
npm run build
```

**3. Add to your MCP host's config:**
```json
{
  "mcpServers": {
    "ffxiv-structs": {
      "command": "node",
      "args": ["/path/to/mcp-xiv-clientstructs/dist/index.js"],
      "env": {
        "FFXIV_STRUCTS_REPO": "/path/to/ffxiv_clientstructs_repo",
        "FFXIV_STRUCTS_INDEX": "/path/to/mcp-xiv-clientstructs/index.json"
      }
    }
  }
}
```

On first start the index is built automatically (~2–5s). Subsequent starts load the cached index instantly unless the repo SHA has changed.

## Keeping up to date

On every start, the server compares the repo's current git SHA against the cached index. If they differ (e.g. because you pulled externally), it rebuilds automatically.

The `refresh` tool does this in one step without a restart: it runs `git pull` on the repo and rebuilds the index if the SHA changed. Useful to call after a game patch.
