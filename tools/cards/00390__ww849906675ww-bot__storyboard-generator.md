---
id: tool-00390
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: storyboard-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ww849906675ww-bot/storyboard-generator
created: 2026-07-18
updated: 2026-07-18
no: 390
category: 二、网文 / 长篇 AI 写作系统 库
repo: ww849906675ww-bot/storyboard-generator
stars: 1
url: https://github.com/ww849906675ww-bot/storyboard-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: a6999a691b2100b1
  - methods/最强写作方法论_全球最强综合版.md
---

# ww849906675ww-bot/storyboard-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ww849906675ww-bot/storyboard-generator
- **Stars**：1
- **语言**：None
- **License**：MIT
- **Topics**：ai-film, chinese, film-preproduction, gpt-image-2, hermes-agent, storyboard
- **GitHub 描述**：AI导演版故事板生成工具 - Hermes Agent 技能，通过 gpt-image-2 生成专业影视分镜预演图像
- **本地描述**：AI导演版故事板生成工具 - Hermes Agent 技能，通过 gpt-image-2 生成专业影视分镜预演图像
- **拉取时间**：2026-07-23 22:50:31

---

# 🎬 Storyboard Generator

> AI 驱动的电影级导演故事板生成工具 —— 从角色圣经图到 8 格分镜，全流程预演。

## 有什么用？

用 AI（gpt-image-2）一键生成专业影视预演物料：

- **角色圣经图** — 正面/侧面/背面/特写，锁定角色造型，后续所有图以此为锚点
- **导演版故事板** — 项目信息栏 + 角色参考区 + 场景设计区 + 8 格分镜 + 技术注释
- **配合 Seedance 视频生成** — 故事板 → 15 秒视频 → 首尾帧衔接 → 剪映拼接成片

## 模板说明

### Template A：完整导演版故事板
五区布局（16:9）：项目栏 → 角色参考区 → 场景设计区 → 8 格分镜 → 技术注释。

### Template C：角色圣经图
4 格水平排列（正面/侧面/背面/特写），中性姿势，纯参考工具。用于 reference_images 锁定角色造型。

## 成本参考

| 物料 | 单价 |
|------|------|
| 角色圣经图 | ~¥0.2/张 |
| 导演版故事板 | ~¥0.2/张 |
| 15 秒视频 | ~¥35/条 |
| 1 分钟成片 | ~¥140 |

## 依赖

- gpt-image-2（图像生成）
- doubao-seedance-2-0（视频生成，可选）
- 剪映 / CapCut（剪辑，可选）

## 开源协议

MIT License

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*从抖音上学来的导演模板，用 AI 跑通了全流程。*
