---
id: tool-00813
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: story
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/escharm/story
created: 2026-07-18
updated: 2026-07-18
no: 813
category: 二、网文 / 长篇 AI 写作系统 库
repo: escharm/story
stars: 1
url: https://github.com/escharm/story
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: f26c3562bc3c9460
  - methods/最强写作方法论_全球最强综合版.md
---

# escharm/story

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/escharm/story
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Next generation story framework powered by Vite.
- **本地描述**：Next generation story framework powered by Vite.
- **拉取时间**：2026-07-23 23:02:45

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 编辑器工作流程

1. 访问 preview 地址
2. 通过开发服务器，加载代码
   - 读取原始代码，增加 data-id 到普通 tag
     - 使用正则处理
   - 编译代码为 ast
     - 解析组件 props
     - 创建 mock 数据
     - 生成组件层级数据
   - 拼装新的组件
     - 捕获器。
       - 代理点击事件，获取点击的对象。但不触发目标的点击事件
     - 展示正常的组件
     - 选择器
       - 从网页中获取元素大小
       - 标记用户选中的元素
     - 目录
       - 加载组件层级数据
     - 工具栏
       - 增加新的结构
