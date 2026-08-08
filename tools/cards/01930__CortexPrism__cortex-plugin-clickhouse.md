---
id: tool-01930
type: tool
area: 库
status: active
tags: [Claude插件, TypeScript, 协议宽松, 本地优先, 英文文档, 本地写作]
title: cortex-plugin-clickhouse
summary: Claude Code 插件式写作流
source: https://github.com/cortexprism/cortex-plugin-clickhouse
created: 2026-07-18
updated: 2026-07-18
no: 1930
category: 二、网文 / 长篇 AI 写作系统 库
repo: CortexPrism/cortex-plugin-clickhouse
stars: 0
url: https://github.com/cortexprism/cortex-plugin-clickhouse
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 932cf643e31bca4a
  - methods/最强写作方法论_全球最强综合版.md
---

# CortexPrism/cortex-plugin-clickhouse

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/cortexprism/cortex-plugin-clickhouse
- **Stars**：0
- **语言**：TypeScript
- **License**：MIT
- **Topics**：analytics, cortex-plugin, cortexprism, database, deno, plugin
- **GitHub 描述**：ClickHouse / Trino Analytical Query Agent — petabyte-scale OLAP analytics. Direct read-only access to ClickHouse and Trino for exploring massive datasets, writing optimized queries, and generating dashboards.
- **本地描述**：ClickHouse / Trino Analytical Query Agent — petabyte-scale OLAP analytics. Direct read-only access to ClickHouse and Trino for exploring massive datasets, writing optimized queries, and generating dashboards.
- **拉取时间**：2026-07-23 23:35:15

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Example Plugin

Brief one-line description of what this plugin does.

## Installation

```bash
# From marketplace
cortex plugin install marketplace:example-plugin

# From GitHub (for development)
cortex plugin install github:CortexPrism/cortex-plugin-example

# Local installation (for development)
cortex plugin install ./manifest.json
```

## Quick Start

After installation, list available tools:

```bash
cortex tools list
```

Use a tool in an agent session:

```bash
cortex chat --plugin example-plugin
```

## Tools

### hello

Greet a person by name.

**Parameters:**

- `name` (string, required) — Person's name

**Example:**

```bash
cortex tool call hello --name Alice
# Output: Hello, Alice! Welcome to Cortex.
```

### add

Add two numbers together.

**Parameters:**

- `a` (number, required) — First number
- `b` (number, required) — Second number

**Example:**

```bash
cortex tool call add --a 5 --b 3
# Output: 8
```

### fetch_data

Fetch data from an external API (HTTPS only).

**Parameters:**

- `url` (string, required) — URL to fetch from

**Example:**

```bash
cortex tool call fetch_data --url https://api.example.com/data
```

## Configuration

Configure this plugin in `~/.cortex/config.json`:

```json
{
  "plugins": {
    "example-plugin": {
      "enabled": true,
      "config": {}
    }
  }
}
```

## Permissions

This plugin declares:

- `network:fetch` — Makes HTTPS requests to external APIs

## Development

### Setup

```bash
# Install dependencies
deno cache mod.ts

# Run tests
deno task test

# Format code
deno fmt

# Lint
deno lint
```

### Building

```bash
# Validate the plugin
deno task validate

# Test locally
cortex plugin install ./manifest.json
cortex tool call hello --name Test

# Use in chat
cortex chat --plugin example-plugin
```

### Testing

Tests are located in `test/` directory:

```bash
# Run all tests
deno task test

# Run specific test
deno test --allow-all test/unit/mod.test.ts --filter "hello tool"

# Run with coverage
deno test --coverage=.coverage --allow-all test/
```

## Marketplace Publishing

When ready to publish:

1. Update version in `manifest.json`
2. Update `CHANGELOG.md` with changes
3. Commit and tag: `git tag v1.0.0`
4. Push to GitHub: `git push origin main --tags`
5. GitHub Actions automatically publishes to marketplace

For detailed publishing instructions, see [Publishing Plugins](https://github.com/CortexPrism/cortex-plugin-clickhouse/blob/main/../docs/publishing.md).

## Troubleshooting

### Plugin fails to load

**Error:** `Plugin failed to load: Invalid manifest`

**Solution:** Validate your `manifest.json`:

```bash
deno task validate
```

### Tool doesn't appear

**Error:** `Tool not found`

**Solution:** Ensure the tool is:

1. Exported in the `tools` array in `mod.ts`
2. Declared in `manifest.json` under `tools`
3. Plugin is enabled: `cortex plugin enable example-plugin`

### Permission denied

**Error:** `Permission denied: network:fetch`

**Solution:** The `network:fetch` capability must be in the manifest and approved by the user.

## Best Practices

See [Best Practices](https://github.com/CortexPrism/cortex-plugin-clickhouse/blob/main/../docs/best-practices.md) for complete guidelines:

✅ **Do:**

- Validate all tool parameters
- Handle errors gracefully
- Return ToolResult with `success` and `output`/`error`
- Respect timeouts
- Declare minimal permissions
- Write comprehensive tests

❌ **Don't:**

- Hardcode API keys or secrets
- Request overly broad permissions
- Ignore errors
- Leave console.log in code
- Skip input validation

## License

MIT — See [LICENSE](https://github.com/CortexPrism/cortex-plugin-clickhouse/blob/main/LICENSE) file

## Contributing

See [CONTRIBUTING.md](https://github.com/CortexPrism/cortex-plugin-clickhouse/blob/main/../CONTRIBUTING.md) for development standards.

## Support

- 📖 [Developing Plugins](https://github.com/CortexPrism/cortex-plugin-clickhouse/blob/main/../docs/developing.md)
- 📖 [Plugin Best Practices](https://github.com/CortexPrism/cortex-plugin-clickhouse/blob/main/../docs/best-practices.md)
- 📖 [Manifest Reference](https://github.com/CortexPrism/cortex-plugin-clickhouse/blob/main/../docs/manifest-reference.md)
- 💬 [Discord Community](https://discord.gg/y7DkaEbPQC)
- 🐛 [Report Issues](https://github.com/CortexPrism/cortex/issues)
