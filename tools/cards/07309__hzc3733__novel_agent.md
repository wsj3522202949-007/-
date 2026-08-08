---
id: tool-07309
type: tool
area: 库
status: active
tags: [大纲规划, 协议未明, 本地优先, 中文友好, 本地写作]
title: novel_agent
summary: 搭大纲/分卷/节拍
source: https://github.com/hzc3733/novel_agent
created: 2026-07-18
updated: 2026-07-18
no: 7309
category: 画龙补充 / 扩容入库 — 补充源
repo: hzc3733/novel_agent
stars: 0
url: https://github.com/hzc3733/novel_agent
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: dfb3d3c3aaa635d3
  - methods/QUICK_START.md
---

# hzc3733/novel_agent

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/hzc3733/novel_agent
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Git-native AI novel writing workbench with Dify agents
- **本地描述**：novel_agent
- **拉取时间**：2026-07-25 19:17:22

related:
  - methods/QUICK_START.md
---

# Novel Agent

面向长篇网文作者的本地 AI 创作工作台：把小说导入、世界观蒸馏、大纲协作、续写草稿、审核归档和剧情分支管理做成一套可维护的创作 IDE。

它不是普通聊天框应用：人类作者和 Agent 共同维护同一套 Markdown 创作资产，Dify 负责语义决策和工作流编排，Flask / LoreGit 提供确定性的文件、上下文与 Git 工具层，让章节草稿、审核意见、回退历史和剧情分支都可以被检查、回滚和继续推进。

## 工程证据

- 公网体验：<http://47.237.191.43:15173/>
- 演示视频：<https://www.bilibili.com/video/BV12eVA69EGV/>
- GitHub Pages 技术档案：<https://blackzhanzhan.github.io/novel_agent/>
- 测试规模：`novel_git_server/tests` 当前包含 **50 个核心测试文件、426 个测试函数**，覆盖 Flask API、Git 分支 / diff / 回退、Markdown 区块写入、Dify ToolProvider 边界、运行时配置、公开体验会话隔离和章节审核归档等核心链路。
- 部署路径：仓库提供 Release ZIP、本地源码运行、Docker Compose 本地构建、GHCR 预构建镜像和半公开体验版服务器部署说明；`deploy/demo/deploy_doctor.py` 区分本地 demo 与 public-demo 画像做部署体检。

完整介绍、截图、架构说明、部署教程和 FAQ 都放在 GitHub Pages：

## [打开 GitHub Pages 技术档案](https://blackzhanzhan.github.io/novel_agent/)

备用入口：

- [仓库内 HTML 技术档案](https://github.com/hzc3733/novel_agent/blob/main/docs/technical-dossier.html)
- [Markdown 技术档案](https://github.com/hzc3733/novel_agent/blob/main/docs/TECHNICAL_DOSSIER.md)
- [完整部署说明](https://github.com/hzc3733/novel_agent/blob/main/docs/DEPLOYMENT.md)

![Novel Agent 工作台](https://github.com/hzc3733/novel_agent/blob/main/docs/assets/screenshots/02-workbench-main.jpg)
