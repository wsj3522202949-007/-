---
id: tool-00671
type: tool
area: 库
status: active
tags: [校对, C#, 协议传染, 本地优先, 英文文档, 改稿润色, 本地写作]
title: WritingTool
summary: 错别字/语法/风格校对
source: https://github.com/viorelghiurca/writingtool
created: 2026-07-18
updated: 2026-07-18
no: 671
category: 二、网文 / 长篇 AI 写作系统 库
repo: viorelghiurca/WritingTool
stars: 0
url: https://github.com/viorelghiurca/writingtool
tier: "C"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# viorelghiurca/WritingTool

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/viorelghiurca/writingtool
- **Stars**：0
- **语言**：C#
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：Privacy-friendly Windows writing assistant: bring your own API key or use local Ollama. Fast actions via hotkey.
- **本地描述**：Privacy-friendly Windows writing assistant: bring your own API key or use local Ollama. Fast actions via hotkey.
- **拉取时间**：2026-07-23 22:58:35

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# WritingTool

System-wide writing assistance for Windows — activate anywhere with a hotkey, pick an action, and get clean, paste-ready output.

Built by **Viorel Ghiurca** (Software Developer).  
Support the project: `https://buymeacoffee.com/viorelghiurca`

## Highlights

- **System-wide hotkey**: bring up the UI while you work (default: `Ctrl+Space`)
- **Fast writing actions**: proofread, rewrite, adjust tone, summarize, extract key points, translate, convert to tables
- **Multiple providers**: Google Gemini, OpenAI-compatible APIs, and **Ollama (local)**
- **Modern WinUI 3 UI**: Mica backdrop, smooth animations
- **Configurable buttons**: edit action buttons and prompts in `options.json`
- **Bring your own key**: you control which provider you use and what it costs

## Quick start

### Option A: Download a release

- Go to GitHub **Releases** and download the latest build for your architecture.

### Option B: Build from source

**Requirements**
- Windows 10/11
- Visual Studio 2022 (Desktop development with C++) or `dotnet` SDK
- .NET 8 SDK

**Build / run**
- Open `WritingTool.sln` in Visual Studio and run.
- Or build via CLI:

```powershell
dotnet restore
dotnet build -c Release
dotnet run -c Release
```

## Setup (providers)

Open **Settings** in the tray menu and select a provider:

- **Gemini (Recommended)**: add your API key and (optionally) model name.
- **OpenAI Compatible**: set API base URL + API key + model name.
- **Ollama (Local)**: install Ollama, run a model, and point WritingTool at `http://localhost:11434`.

See detailed guides:
- `docs/getting-started.md`
- `docs/providers.md`

## Configuration files

- **`settings.json`**: user-specific settings (provider choice, keys, theme, hotkey).  
  This file is **ignored by git** on purpose.
- **`settings.example.json`**: safe template you can copy to `settings.json`.
- **`options.json`**: action buttons (names, icons, prompts, "open in window" behavior).

## Privacy

WritingTool sends text only to the provider you select.

- If you use **Ollama**, text stays on your machine.
- If you use a cloud provider, text is sent to that provider's API endpoint.

See [`PRIVACY.md`](PRIVACY.md) for the full privacy policy.

## Code Signing Policy

Free code signing provided by [SignPath.io](https://signpath.io), certificate by [SignPath Foundation](https://signpath.org).

**Team roles:**
- Owner / Approver / Reviewer: [Viorel Ghiurca](https://github.com/viorelghiurca)

## Windows SmartScreen

When you first run WritingTool, Windows SmartScreen may show a warning because the application is new. This is normal for new software.

**To run the application:**
1. Click **"More info"** in the SmartScreen dialog
2. Click **"Run anyway"**

The application is open source — you can inspect the code and build it yourself if you prefer.

## Documentation

- `docs/getting-started.md` — first run, hotkey, basic workflow
- `docs/buttons-and-prompts.md` — customizing `options.json` (buttons, icons, windows)
- `docs/providers.md` — Gemini / OpenAI-compatible / Ollama setup
- `docs/troubleshooting.md` — common issues and fixes

## Contributing

PRs and issues are welcome. Please read `CONTRIBUTING.md` first.

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

See `LICENSE` for details.
