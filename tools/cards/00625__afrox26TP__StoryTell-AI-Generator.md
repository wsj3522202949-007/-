---
id: tool-00625
type: tool
area: 库
status: active
tags: [Claude插件, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: StoryTell-AI-Generator
summary: Claude Code 插件式写作流
source: https://github.com/afrox26tp/storytell-ai-generator
created: 2026-07-18
updated: 2026-07-18
no: 625
category: 二、网文 / 长篇 AI 写作系统 库
repo: afrox26TP/StoryTell-AI-Generator
stars: 0
url: https://github.com/afrox26tp/storytell-ai-generator
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
content_hash: f1eaa94846eefd20
  - methods/最强写作方法论_全球最强综合版.md
---

# afrox26TP/StoryTell-AI-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/afrox26tp/storytell-ai-generator
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：some simple script for creating your own ai telling story on perchance.org platform.
- **本地描述**：some simple script for creating your own ai telling story on perchance.org platform.
- **拉取时间**：2026-07-23 22:57:17

---

# 📖 StoryTell AI — Perchance Generator

Interactive AI story generator powered by Perchance AI text plugin.

## How to Deploy on Perchance.org

1. Go to **https://perchance.org** and register/login.
2. Click **➕ new** (top left) to create a new generator.
3. In the **Lists editor** (left), delete everything and paste the content from:
   ```
   storytell-lists.txt
   ```
4. In the **HTML editor** (right), delete everything and paste the content from:
   ```
   storytell-template.html
   ```
5. Click **💾 save** — enter a name (e.g., `storytell-ai`).
6. Done! Click **🛠️ edit → view** to run it.

## Features

| Button | Function |
|--------|-------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| ✨ **Start Story** | Begin a new story (with your prompt or without) |
| ▶ **Continue** | AI continues the story |
| 🗑 **New Story** | Clear the current story |
| 📋 **Copy** | Copy the entire story to clipboard |

**Keyboard shortcut:** `Ctrl + Enter` to start or continue the story.

## Settings

- **Genre** — Fantasy, Sci-Fi, Horror, Mystery, Romance, Adventure, Historical Fiction, Thriller, Fairy Tale, Age Regression
- **Perspective** — Third-person / First-person / Second-person
- **Length** — Short / Medium / Long / Extra Long
- **Language** — English / Czech / Slovak

Multi-chapter generation is temporarily disabled while the chapter flow is being stabilized.

## File Structure

```
storytell/
├── README.md                  ← this file
├── storytell-lists.txt        ← paste into Perchance Lists editor
└── storytell-template.html    ← paste into Perchance HTML editor
```

## Notes

- The plugin runs on Perchance servers — no local model or API key needed.
- Free tier shows ads (that's how Perchance funds the GPU servers).
- Log in to remove ads.

