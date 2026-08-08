---
id: tool-01453
type: tool
area: 库
status: active
tags: [Claude插件, JavaScript, 协议未明, 本地优先, 中文友好, 本地写作]
title: anki-story-generator
summary: Claude Code 插件式写作流
source: https://github.com/kobe050/anki-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1453
category: 二、网文 / 长篇 AI 写作系统 库
repo: kobe050/anki-story-generator
stars: 2
url: https://github.com/kobe050/anki-story-generator
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 0d1394b6cf424188
  - methods/最强写作方法论_全球最强综合版.md
---

# kobe050/anki-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/kobe050/anki-story-generator
- **Stars**：2
- **语言**：JavaScript
- **License**：None
- **Topics**：ai, ai-education, anki, english-learning, gemini, gemini-api, js, language-learning, story-generation, study-tool
- **GitHub 描述**：—
- **本地描述**：kobe050/anki-story-generator
- **拉取时间**：2026-07-23 23:21:27

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 📚 Anki 单词短文生成器 (2026 版)

这是一个利用 **Google Gemini 2.5 Flash** AI 驱动的英语学习辅助工具。它可以将你背诵的单词自动编织成一篇有趣的短文，并提供全文本交互式翻译。

## ✨ 核心功能
- **智能故事生成**：输入单词列表，AI 自动生成主题故事。
- **Anki 笔记导入**：支持直接上传从 Anki 导出的 `.txt` 笔记文件提取单词。
- **中英双语对照**：支持段落点击即看翻译，全篇一键翻译切换。
- **分词级悬停翻译**：鼠标悬停在文中任何单词上 1 秒，自动显现中文释义。
- **极致 Token 优化**：采用前端分词与免费翻译 API，大幅节省 AI 消耗。

## 🚀 如何使用
1.  **准备 API Key**：前往 [Google AI Studio](https://aistudio.google.com/) 免费申请一个 Gemini API Key。
2.  **运行项目**：由于涉及跨域请求，请使用本地服务器（如 VS Code 的 **Live Server** 插件）打开 `autoMakeStoryByEn.html`。
3.  **输入单词**：手动输入或导入 Anki 笔记。
4.  **生成短文**：点击生成按钮，开始你的浸入式复习。

## 🛠️ 技术栈
- HTML5 / Vanilla CSS
- JavaScript (ES6+)
- Google Gemini API
- Google Translate API (gtx)

## 🔒 安全说明
本项目完全在本地浏览器运行，API Key 仅存在于内存中，不会上传至任何第三方服务器。
