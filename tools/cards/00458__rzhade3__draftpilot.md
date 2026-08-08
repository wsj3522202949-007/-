---
id: tool-00458
type: tool
area: 库
status: active
tags: [校对, JavaScript, 协议宽松, 本地优先, 英文文档, 改稿润色, 本地写作]
title: draftpilot
summary: 错别字/语法/风格校对
source: https://github.com/rzhade3/draftpilot
created: 2026-07-18
updated: 2026-07-18
no: 458
category: 二、网文 / 长篇 AI 写作系统 库
repo: rzhade3/draftpilot
stars: 0
url: https://github.com/rzhade3/draftpilot
tier: "C"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: ea3b5f992394cc82
  - methods/最强写作方法论_全球最强综合版.md
---

# rzhade3/draftpilot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rzhade3/draftpilot
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI-powered writing assistant for Google Docs, powered by GitHub Copilot SDK
- **本地描述**：AI-powered writing assistant for Google Docs, powered by GitHub Copilot SDK
- **拉取时间**：2026-07-23 22:52:26

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# DraftPilot

AI-powered writing assistant for Google Docs — grammar, tone, style, fact-checking, and more. Powered by [GitHub Copilot SDK](https://github.com/github/copilot-sdk).

## Features

- **Grammar & style suggestions** — inline accept/dismiss with one-click apply to your document
- **Target tone** — set a per-document target tone; analysis flags deviations
- **Writing Quality score** — hybrid score (0–100) based on suggestions, readability, vocabulary diversity, and sentence variety
- **Flesch Reading Ease** — instant readability calculation
- **AI Detection** — estimates how much of the text appears AI-generated _(stubbed in the Go backend; returns a placeholder pending reimplementation)_
- **Publish readiness** — tells you when your doc is ready to ship
- **Fact-check research** — extracts verifiable claims, then lets you verify each one via web search
- **SEO coverage** — suggests semantically relevant keywords and shows how well they're placed (title, headings, body) with actionable, non-stuffing recommendations
- **Chat interface** — ask the AI to rephrase, expand, summarize, or edit your text
- **Memory** — learns your writing preferences over time
- **Multi-tab support** — works with Google Docs that have multiple tabs

## Prerequisites

- [Go](https://go.dev/dl/) 1.25+
- [GitHub Copilot CLI](https://docs.github.com/en/copilot) installed and authenticated (`gh auth login`)
- A Google Cloud project with the **Google Docs API** enabled and an OAuth 2.0 client ID (Chrome app type)

## Setup

### 1. Configure the extension

```bash
cp extension/manifest.example.json extension/manifest.json
```

Edit `extension/manifest.json` and replace `YOUR_GOOGLE_OAUTH_CLIENT_ID` with your Google OAuth client ID.

### 2. Start the backend (native messaging host)

The backend is a single, statically-compiled **Go** binary that runs as a
**Chrome Native Messaging host** — Chrome launches it on demand over
stdin/stdout, so there is **no server to start manually and no open network
port**. You only register it once:

```bash
make install
# equivalently: cd server-go && go run ./cmd/installhost
```

This compiles the host binary and registers a native messaging manifest for the
current user (Chrome/Chromium/Edge). It pins DraftPilot's extension ID, so only
this extension can connect. Re-run it after pulling changes that affect the host.

The installer also scaffolds `~/.draftpilot/config.json`, auto-detecting model
IDs your Copilot account can actually use (it prefers `gpt-4.1` / `gpt-4.1-mini`
and falls back to whatever is available). Edit that file to change models:

```json
{
  "models": {
    "analyze": "gpt-4.1",
    "chat": "gpt-4.1",
    "extract": "gpt-4.1-mini",
    "verify": "gpt-4.1",
    "seo": "gpt-4.1"
  }
}
```

> **Why a config file and not env vars?** Chrome launches the host with a minimal
> environment (GUI apps on macOS don't inherit your shell), so `DRAFTPILOT_MODEL_*`
> env vars won't reach it. The config file is the reliable mechanism; env vars
> still work for local dev/testing and take precedence when set.

> The SQLite database lives at `~/.draftpilot/draftpilot.db` by default; override
> the location with `DRAFTPILOT_DB`. Override the config file path with
> `DRAFTPILOT_CONFIG`.

### 3. Load the Chrome extension

1. Open Chrome → `chrome://extensions/`
2. Enable **Developer mode** (top right)
3. Click **Load unpacked** → select the `extension/` folder
4. Navigate to a Google Doc and click the DraftPilot icon

## Usage

1. Click **Analyze** to get suggestions, scores, and tone analysis
2. **Accept** or **Dismiss** suggestions (applied directly to your doc)
3. **Double-click the tone pill** to set a target tone for this document
4. Use **🔍 Extract Claims** to pull out factual assertions, then **Verify** individually
5. Use the **Chat** tab to ask questions or request edits

## Development

```bash
# Backend (native messaging host) — rebuild + reinstall after changes
make install

# Other convenience targets (run `make help` for the full list)
make build   # compile the host binary to server-go/bin/
make test    # run the Go test suite
make fmt     # gofmt all sources
make vet     # go vet

# Extension — plain JS, no build step
# Edit files in extension/ and reload in Chrome (re-register the host if it changed)
```

After changing the host, reload the extension in `chrome://extensions` so Chrome
relaunches the host with the new code.
