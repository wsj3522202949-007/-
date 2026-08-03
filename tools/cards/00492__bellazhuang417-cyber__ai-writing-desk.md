---
id: tool-00492
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 需API密钥, 中文友好, 大纲规划, 多Agent, 灵感创意]
title: ai-writing-desk
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/bellazhuang417-cyber/ai-writing-desk
created: 2026-07-18
updated: 2026-07-18
no: 492
category: 二、网文 / 长篇 AI 写作系统 库
repo: bellazhuang417-cyber/ai-writing-desk
stars: 0
url: https://github.com/bellazhuang417-cyber/ai-writing-desk
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# bellazhuang417-cyber/ai-writing-desk

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/bellazhuang417-cyber/ai-writing-desk
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI 内容创作工作台 — 口述→润色→发布，9种模板+字数控制+配图Prompt
- **本地描述**：AI 内容创作工作台 — 口述→润色→发布，9种模板+字数控制+配图Prompt
- **拉取时间**：2026-07-23 22:53:25

---

# AI Writing Desk ✍️

一个自给自足的内容创作工作台 — 输入口述内容，AI 帮你润色，一键生成发布级文案。

**[👉 在线使用](https://bellazhuang417-cyber.github.io/ai-writing-desk/)**

---

## 功能

| 功能 | 说明 |
|------|---related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| 🎯 9 种模板 | 清单体（干货/数字/避坑）× 文学感（情感/叙事/哲理）× 实用技巧（教程/对比/指南） |
| 🪄 AI 润色 | 接入 DeepSeek，一键将口述内容整理成结构化文案 |
| 📏 字数控制 | 实时字数统计 + 平台适配（小红书 ≤1000 字 / 公众号 ≤1500 字）+ 超标一键精简 |
| 🎨 配图 Prompt | AI 分析文章结构，自动生成 Ian 小黑风格配图 Prompt，复制到任意平台生图 |
| 📝 实时预览 | 左侧编辑 + 右侧 Markdown 实时渲染 |
| 📤 导出 | 一键导出 .md 文件 / 复制到剪贴板 |

## 使用方法

1. **获取 API Key**：前往 [DeepSeek 开放平台](https://platform.deepseek.com/api_keys) 注册并创建 API Key
2. **打开工作台**：访问上面的在线链接，或下载 `index.html` 本地打开
3. **填入 Key**：页面顶部粘贴你的 DeepSeek API Key，点击保存（Key 仅保存在浏览器本地，不会上传）
4. **开始写作**：在编辑区写下你想发的内容，选择模板，点「润色」

## 技术说明

- **零后端**：纯静态 HTML 文件，无需服务器
- **直连 API**：浏览器直接调用 DeepSeek API（需联网）
- **隐私安全**：API Key 仅存储在浏览器 `localStorage`，不会发送到任何第三方
- **配图 Prompt**：基于 [Ian 小黑风格](https://github.com/ian-xiaohei) 的配图 Prompt 生成，可复制到任意 AI 生图平台使用

## 开发

```bash
# 本地运行（任意一种）
open index.html                # 直接打开
python3 -m http.server 8080    # 本地服务器
```

## License

MIT
