---
id: tool-01937
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: github-ai
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/daesdev/github-ai
created: 2026-07-18
updated: 2026-07-18
no: 1937
category: 二、网文 / 长篇 AI 写作系统 库
repo: daesdev/github-ai
stars: 1
url: https://github.com/daesdev/github-ai
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 921cee66e40704cd
  - methods/最强写作方法论_全球最强综合版.md
---

# daesdev/github-ai

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/daesdev/github-ai
- **Stars**：1
- **语言**：HTML
- **License**：None
- **Topics**：vscode, vscode-settings
- **GitHub 描述**：Markdown configuration for GitHub Copilot — commit messages and PR descriptions using AI for writing assistance
- **本地描述**：Markdown configuration for GitHub Copilot — commit messages and PR descriptions using AI for writing assistance
- **拉取时间**：2026-07-23 23:35:27

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# VS Code AI Setup

A VS Code configuration tool that sets up GitHub Copilot with custom commit message and pull request instructions using AI.

## What is this?

This is a VS Code configuration tool that modifies your `.vscode/settings.json` to point GitHub Copilot to custom instructions. When you commit or create a PR, Copilot generates optimized messages following Conventional Commits format.

## Quick Install (One Command)

```bash
curl -sL https://raw.githubusercontent.com/daesdev/github-ai/main/install.sh | bash
```

## Features

- **AI-Powered Commit Messages**: GitHub Copilot generates commit messages using Conventional Commits format with AI
- **AI-Powered PR Descriptions**: Intelligent PR title and description generation with structured templates
- **Conventional Commits**: Standardized commit message format with type, scope, emoji, and subject
- **One-command install**: Works on any project with a single curl command
- **Safe & Secure**: Backup to `~/.daes/` before any modification, restores on failure
- **Version Tracking**: Shows current version during installation, auto-updates landing page on release

## Installation Methods

### Method 1: curl | bash (Recommended)

```bash
curl -sL https://raw.githubusercontent.com/daesdev/github-ai/main/install.sh | bash
```

### Method 2: Clone and run

```bash
git clone https://github.com/daesdev/github-ai.git
cd your-project
make install
# or
./install.sh
```

## What gets installed?

The installer creates these files in your project:

```
.github/
└── copilot-instructions.md    # AI instructions for commits and PRs

.vscode/settings.json           # Updated with Copilot configuration
```

## How It Works

1. Run the install command
2. The script creates `.github/copilot-instructions.md` with your custom AI instructions
3. It updates `.vscode/settings.json` to point GitHub Copilot to the instructions file
4. When you commit or create a PR, Copilot reads your instructions and generates optimized messages

## Requirements

### Software
- **VS Code** - Code editor
- **GitHub Copilot** - Subscription required (not the free tier)

### Tools
- Git
- Bash
- Python3 (required for JSON merge)

## Landing Page

The project includes a landing page at `web/index.html` that displays:

- Installation command
- Features overview
- Version badge (auto-updates on release via GitHub Actions)

### Deploy to Cloudflare Pages

```bash
# Install wrangler if needed
npm install -g wrangler

# Deploy to Cloudflare Pages
wrangler pages deploy web --project-name=github-ai
```

The landing page will be available at `vscode.daes.dev`

## Contributing

Feel free to submit issues and pull requests to improve the instructions or installer.

## License

MIT
