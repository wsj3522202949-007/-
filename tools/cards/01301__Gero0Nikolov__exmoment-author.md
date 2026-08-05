---
id: tool-01301
type: tool
area: 库
status: active
tags: [Claude插件, PHP, 协议宽松, 本地优先, 英文文档, 本地写作]
title: exmoment-author
summary: Claude Code 插件式写作流
source: https://github.com/gero0nikolov/exmoment-author
created: 2026-07-18
updated: 2026-07-18
no: 1301
category: 二、网文 / 长篇 AI 写作系统 库
repo: Gero0Nikolov/exmoment-author
stars: 0
url: https://github.com/gero0nikolov/exmoment-author
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Gero0Nikolov/exmoment-author

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/gero0nikolov/exmoment-author
- **Stars**：0
- **语言**：PHP
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：ExMoment Author is a WordPress AI writing plugin for SEO content creation. Generate drafts, optimize copy, and schedule publishing with OpenAI-powered workflows. Includes job scheduler, content library, and admin controls for fast, consistent content production and smarter editorial automation.
- **本地描述**：ExMoment Author is a WordPress AI writing plugin for SEO content creation. Generate drafts, optimize copy, and schedule publishing with OpenAI-powered workflows. Includes job scheduler, content library, and admin controls for fast, consistent content production and smarter editorial automation.
- **拉取时间**：2026-07-23 23:17:02

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ExMoment Author

ExMoment Author is a modular WordPress plugin for AI-assisted content authoring, scheduling, and operational editorial workflows.

## Documentation

Project documentation is organized under [`docs/index.md`](docs/index.md).

## What This Plugin Includes

- GPT-powered generation workflows.
- Jobs post type for single and repeating execution.
- Scheduler worker lifecycle and cron integrations.
- Library tooling for reusable content and used-articles tracking.
- Logging and operational diagnostics.
- Settings and admin support pages.

## Repository Layout

- `exmoment-author.php` - plugin bootstrap.
- `Core.php` - core runtime loader and module registration.
- `modules/` - feature modules (`gpt`, `jobs`, `library`, `settings`, and others).
- `resources/` - admin scripts/styles and assets.
- `docs/` - architecture, module guides, settings, operations, references, and archive docs.
- `readme.txt` - WordPress distribution metadata.

## Development Notes

- Runtime modules are autoloaded from `Core.php` configuration.
- Local Docker development targets WordPress `7.0`, PHP `8.4`, and MariaDB `10.6`.
- The `wpcli` service now mirrors the WordPress DB environment so `wp` commands work against `wp-config.php` without manual overrides.
- Keep docs updated whenever module behavior, hooks, or operational procedures change.

## Related Entrypoint

Contributor/agent orientation is documented in [`AGENTS.md`](AGENTS.md).
