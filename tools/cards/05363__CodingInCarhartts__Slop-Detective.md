---
id: tool-05363
type: tool
area: 库
status: active
tags: [多Agent, TypeScript, 协议宽松, 本地优先, 英文文档, 本地写作]
title: Slop-Detective
summary: 多 Agent 协作自动产文
source: https://github.com/codingincarhartts/slop-detective
created: 2026-07-18
updated: 2026-07-18
no: 5363
category: 一、去 AI 味 / Humanizer 库
repo: CodingInCarhartts/Slop-Detective
stars: 0
url: https://github.com/codingincarhartts/slop-detective
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4fd5fc9ad623b041
  - methods/改稿润色指令库.md
---

# CodingInCarhartts/Slop-Detective

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/codingincarhartts/slop-detective
- **Stars**：0
- **语言**：TypeScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：An AI Slop Detector for Github
- **本地描述**：An AI Slop Detector for Github
- **拉取时间**：2026-07-25 18:15:48

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Slop Meter (Slop Detective) 🕵️‍♂️

**AI Slop Meter** is a Chrome extension designed to detect potential AI-generated code ("slop") in GitHub repositories. It analyzes commit patterns, code comments, directory structures, and file uniformity to provide a "Slop Score."

## Features

- **Neural Pattern Detection**: Scans for common LLM-generated boilerplate and "helpful" comment patterns.
- **Commit Analysis**: Analyzes commit messages and frequencies for signs of automated or agentic behavior.
- **Structural Uniformity**: Detects highly repetitive or perfectly scaffolded directory structures typical of AI generators.
- **Noir Detective UI**: A unique, retro-themed interface for your investigation.
- **Cache Support**: Saves analysis results to stay within GitHub API limits.

## Installation

### From Source
1. Clone this repository.
2. Run `npm install` to install dependencies.
3. Run `npm run build` to generate the production build in the `dist` directory.
4. Open Chrome and navigate to `chrome://extensions/`.
5. Enable "Developer mode" (top right).
6. Click "Load unpacked" and select the `dist` folder.

## Usage
1. Navigate to any GitHub repository root (e.g., `https://github.com/owner/repo`).
2. Click the **Slop Detective** icon in your browser toolbar.
3. Click **Scan Target**.
4. (Optional) Add a GitHub Personal Access Token in the **Files** (settings) tab to avoid rate limits on private or large repos.

## Tech Stack
- **React 19** + **TypeScript**
- **Vite** + **CRXJS**
- **Tailwind CSS v4**
- **Radix UI** primitives
- **Lucide React** icons

## License
MIT
