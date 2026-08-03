---
id: tool-00294
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Novel-writing-tools
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/wgwtest/novel-writing-tools
created: 2026-07-18
updated: 2026-07-18
no: 294
category: 二、网文 / 长篇 AI 写作系统 库
repo: wgwtest/Novel-writing-tools
stars: 0
url: https://github.com/wgwtest/novel-writing-tools
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# wgwtest/Novel-writing-tools

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/wgwtest/novel-writing-tools
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：wgwtest/Novel-writing-tools
- **拉取时间**：2026-07-23 22:47:38

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 小说叙事验证工具

本目录是小说结构管理工具的验证仓库，用于沉淀原型、需求说明和后续实验代码。当前仓库只管理 `验证工具` 内部内容，不直接污染外层小说正文和支撑材料。

## 当前基准

当前基准原型：

`原型包/2026-06-20-叙事验证工具-章节选区高亮原型-v6/`

当前实验原型：

`原型包/2026-06-20-叙事验证工具-故事线展开人物子线原型-v7/`

这一版作为后续继续绘制和迭代的基础。它已经较好地表达了以下方向：

- 以时间轴作为对齐底盘。
- 以章节作为基础单元。
- 用多轨事件块表达不同事件线。
- 点击章节或事件只选中，不自动跳转。
- 章节选中时突出整列背景框，不使用当前指针线。

v6 不是最终版本，v7 已开始验证“故事线展开后的人物子线”和“同一人物跨多条故事线出现”的结构。后续仍需继续讨论事件拖拽、章节函数界面、数据结构、导入导出和正式材料接入。

## 当前文件结构

```text
验证工具/
  README.md
  .gitignore
  小说叙事验证工具-策划案.md
  叙事验证工具-需求规格说明-v0.1.md
  原型包/
    2026-06-20-叙事验证工具-章节选区高亮原型-v6/
      README.md
      REVIEW_RESPONSE.md
      source/index.html
      *.png
```

## 查看原型

直接打开：

```text
原型包/2026-06-20-叙事验证工具-章节选区高亮原型-v6/source/index.html
```

## 迭代规则

- 新方向或重要评审修正，继续创建新的版本包，不覆盖当前基准。
- 临时测试、脚本和缓存必须留在本仓库内部。
- 外层小说正文、设定、章节文件不属于本仓库的默认改动范围。
