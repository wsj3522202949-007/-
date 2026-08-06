---
id: tool-04810
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/hope0719/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
$18
category: 一、去 AI 味 / Humanizer 库
repo: hope0719/ai-text-detector
stars: 0
language: JavaScript
license: null
url: https://github.com/hope0719/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI 文本检测（人工智能检测）· 开源合集

一款用于判断「文本是否由 AI 生成」的开源工具合集，同时提供**网页版**与**微信小程序版**两种形态，全部开源、免费使用。

> 本仓库由原 `ai-text-detector-web`（网页版）与 `ai-text-detector-miniprogram`（小程序版）合并而来，统一维护。

## 📂 仓库结构

```
ai-text-detector/
├── web/                # 网页版（单文件 HTML，开箱即用）
│   ├── index.html      #   浏览器直接打开即可使用，零依赖、无需打包
│   └── README.md       #   网页版说明
└── miniprogram/        # 微信小程序版（明鉴文本检测）
    ├── pages/          #   检测 / 结果 / 我的 / 分享 四个页面
    ├── utils/          #   检测算法与词频数据集
    ├── app.js / app.json / app.wxss
    └── project.config.json
```

## 🌐 网页版（web/）

纯单文件 `index.html`，**不需要任何构建步骤**：

- 用浏览器直接打开 `web/index.html` 即可使用。
- 样式通过 Tailwind CSS CDN 加载，字体使用 Google Fonts；⚠️ 需联网才能加载上述 CDN 资源。
- 零依赖、无需打包，适合快速体验与二次开发。

详细用法见 [web/README.md](https://github.com/hope0719/ai-text-detector/blob/main/web/README.md)。

## 🟢 微信小程序版（miniprogram/）

名为「明鉴文本检测」的微信小程序，AI 检测神器：

- 功能：文本检测、结果展示、我的、分享等页面。
- 算法：基于 n-gram 词频统计 + 黄金数据集比对（`utils/` 下）。
- 使用：用微信开发者工具打开 `miniprogram/` 目录即可预览与编译。

详细用法见 [miniprogram/README.md](https://github.com/hope0719/ai-text-detector/blob/main/miniprogram/README.md)。

## 🤝 开源协议

欢迎 Star / Fork / PR。如需使用代码，请遵循仓库 LICENSE（如有）。
