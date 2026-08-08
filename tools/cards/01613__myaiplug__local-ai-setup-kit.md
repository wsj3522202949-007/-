---
id: tool-04808
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: local-ai-setup-kit
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/myaiplug/local-ai-setup-kit
created: 2026-07-18
updated: 2026-07-18
$11613
category: 一、去 AI 味 / Humanizer 库
repo: myaiplug/local-ai-setup-kit
stars: 0
language: Python
license: null
url: https://github.com/myaiplug/local-ai-setup-kit
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d638d64ab75b76e1
  - methods/改稿润色指令库.md
---

# Local AI Setup Kit

Complete toolkit for installing and running local AI models + agent crews.

## What's Included

- `install_local_ai.py` — Cross-platform Python installer
- `install_local_ai.sh` — Mac/Linux shell installer
- `ai-spec-detector.html` — Hardware detection + model recommendations
- Ready-to-use CrewAI templates
- Beginner guides for Image Generation and Text-to-Speech

## Quick Start

### Run the Installer

**Mac/Linux:**
```bash
chmod +x install_local_ai.sh
./install_local_ai.sh
```

**Windows:**
Run `install_local_ai.bat`

### Detect Your Hardware
Open `ai-spec-detector.html` in your browser.

### Try a Pre-built Crew
```bash
cd templates
python faceless_content_crew.py
```
