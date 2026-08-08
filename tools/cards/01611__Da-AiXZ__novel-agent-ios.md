---
id: tool-01611
type: tool
area: 库
status: active
tags: [Swift, 协议宽松, 需API密钥, 英文文档, 大纲规划]
title: novel-agent-ios
summary: 搭大纲/分卷/节拍
source: https://github.com/da-aixz/novel-agent-ios
created: 2026-07-18
updated: 2026-07-18
no: 1611
category: 二、网文 / 长篇 AI 写作系统 库
repo: Da-AiXZ/novel-agent-ios
stars: 0
url: https://github.com/da-aixz/novel-agent-ios
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: fa56175b064e3d46
  - methods/最强写作方法论_全球最强综合版.md
---

# Da-AiXZ/novel-agent-ios

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/da-aixz/novel-agent-ios
- **Stars**：0
- **语言**：Swift
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Native iOS AI agent for Chinese long-form web fiction
- **本地描述**：Native iOS AI agent for Chinese long-form web fiction
- **拉取时间**：2026-07-23 23:26:01

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# NovelAgent

NovelAgent is an iPhone-native AI agent for planning and writing Chinese
long-form web fiction. It guides a new writer from an initial idea to a
confirmed story brief, rolling outline, chapter draft, consistency review,
revision, and local backup.

## Product Boundaries

- iOS 16.0+, iPhone only
- Swift 6, SwiftUI, UIKit text editor bridge
- Direct BYOK access to OpenAI, Anthropic, and OpenAI-compatible APIs
- Local SQLite source of truth with Markdown/JSON/ZIP backup
- One chapter per resumable production run
- No account system, iCloud, arbitrary novel import, local LLM, or unattended
  background generation in V1

## Repository Layout

```text
Sources/NovelAgentCore/       Cross-platform domain and agent runtime
Sources/NovelAgentProviders/  URLSession/SSE provider adapters
NovelAgentApp/                SwiftUI app, GRDB storage, Keychain, export
Tests/                        Core, persistence, and UI tests
project.yml                   XcodeGen project definition
```

## Windows Core Tests

Install Swift 6 for Windows, then run:

```powershell
swift test
```

The iOS application itself requires Xcode. GitHub Actions generates the Xcode
project and runs iOS builds and simulator tests.

## Generate the Xcode Project

```bash
brew install xcodegen
xcodegen generate
open NovelAgent.xcodeproj
```

## Unsigned IPA

Run the `Build Unsigned IPA` workflow manually. It creates an ad-hoc signed
IPA intended for personal installation with TrollStore. No signing certificate
or provisioning profile is embedded.

## Security

API keys are stored in Keychain and are never written to SQLite, exported
backups, source files, or logs. Custom endpoints must use HTTPS.

## License

MIT. See `THIRD_PARTY_NOTICES.md` for attribution and clean-room boundaries.

