---
id: tool-00988
type: tool
area: 库
status: active
tags: [提示词, 协议未明, 本地优先, 中文友好, 多Agent, 本地写作]
title: aimv-storyboard-skill-free
summary: 提示词/写作工作流
source: https://github.com/zzz1phyrf/aimv-storyboard-skill-free
created: 2026-07-18
updated: 2026-07-18
no: 988
category: 二、网文 / 长篇 AI 写作系统 库
repo: Zzz1phyrf/aimv-storyboard-skill-free
stars: 1
url: https://github.com/zzz1phyrf/aimv-storyboard-skill-free
tier: "B"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Zzz1phyrf/aimv-storyboard-skill-free

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/zzz1phyrf/aimv-storyboard-skill-free
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI video MV storyboard generator skill free version
- **本地描述**：AI video MV storyboard generator skill free version
- **拉取时间**：2026-07-23 23:07:51

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AIMV Storyboard Skill

AI 视频 / MV 分镜脚本生成器。

这个 skill 用于把歌词、LRC、歌曲时长或主题设定转成可执行的 MV 分镜方案，输出资产图、故事板、分镜执行表和视频制作清单。

## 内容

- `SKILL.md`：skill 主文件
- `references/storyboard-guide.md`：分镜与镜头语言参考
- `references/prompt-engineering.md`：Prompt 写作参考

## 适用场景

- 给歌曲生成 AIMV / MV 分镜脚本
- 按场景切分画面，而不是一句歌词一张图
- 先锁定角色、场景和道具资产
- 生成 GPT Image 2 多宫格 storyboard sheet
- 输出分镜执行表、关键尾帧和视频制作清单

## 使用方式

把本仓库目录放到支持 skill 的 Agent / Codex skills 目录中，然后在对话中提出类似需求：

```text
帮我根据这首歌生成一个 MV 分镜脚本
```
