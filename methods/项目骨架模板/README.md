---
id: proj-template
type: project
area: 项目
status: demo
tags: []
title: 《书名》— 项目门面
summary: 可复制的项目骨架模板。整目录复制、改名后，改 frontmatter 的 status 为 active 即可开写。
source: 内部制定
created: 2026-07-31
updated: 2026-07-31
genre: 待填
platform: 待填
pov: 待填
chapters_planned: 0
chapters_written: 0
related:
  - projects/README.md
---

# 《书名》— 项目门面

> 复制本目录、改名成你的书名后，把 frontmatter 的 `status` 改为 `active`，再填下面内容。
> 结构规范见 [项目结构规范](../../schema/项目结构规范.md)。

## 一、一句话梗概

（一句话讲清"这是什么书、凭什么好看"）

## 二、核心信息

| 字段 | 内容 |
|---|---|
| 书名 | 《书名》 |
| 题材 / 频率 | 男频/女频 · 题材标签 |
| 目标平台 | 番茄/起点/晋江/盐言… |
| 预计总字数 | 万 |
| 卷数规划 | N 卷 |
| 一句话卖点 | … |

## 三、三大冲突

1. **生存冲突**：…
2. **行业冲突**：…
3. **身份冲突**：…

## 四、AI 协作边界

> 接手本书任何任务前先读此节。

**角色**：你是本书的写作协作者，不是代笔。最终判断权在作者。

**必须遵循**：
1. 先读 [framework.md](framework.md) 的项目铁律，再动手。
2. 任何成稿默认过去 AI 味铁律（`methods/最强去AI味铁律.md`）。
3. 改动设定/人名/金手指前，先查 [entities/](entities/) 下对应单页，保持一致性。
4. 引用方法论用相对路径 `../../methods/...`。

**不要做**：
- 不要擅自大改世界观/人设基调（先问作者）。
- 不要产出"下章预告"式章末。
- 不要把未通过自检的章节标记为完成。

## 五、文件导航

| 文件 | 用途 |
|---|---|
| [STATUS.md](STATUS.md) | 进度数字 + 章节推进表 + 下一步 |
| [framework.md](framework.md) | 核心设定 + 风格基线 + 项目铁律 |
| [outline.md](outline.md) | 分卷总览 + 各卷细纲 + 伏笔追踪 |
| [chapters/](chapters/README.md) | 正文（`第NNN章-标题.md`） |
| [entities/](entities/characters/示例-主角.md) | 知识实体（人物/设定/地点/道具） |
