---
id: idx-projects
type: index
area: 索引
status: active
tags: [目录冻结, projects, 项目]
title: projects/ — 所有项目
summary: 每本书一个子目录，含 README + STATUS + framework + outline + chapters/ + entities/。禁止放方法论、工具卡、草稿。
source: 内部制定
created: 2026-07-31
updated: 2026-07-31
related:
  - README.md
  - drafts/README.md
  - knowledge/README.md
  - methods/README.md
---

# projects/ — 所有项目（小说/非小说统一）

> **冻结职责**：每本书一个合规项目目录。
> **禁止放入**：方法论、工具卡、外部素材、草稿（→drafts/）、归档（→archive/）。

## 标准结构（每个项目）

```
projects/作品名/
├── README.md          # 项目级 frontmatter + 摘要
├── STATUS.md          # 进度数字（章节数/字数/完成率）
├── framework.md       # 核心设定/一句话总纲
├── outline.md         # 总纲/分卷细纲/伏笔管理
├── chapters/          # 已校验正文（第NNN章-标题.md）
└── entities/          # 知识实体
    ├── characters/    # 人物
    ├── settings/      # 设定
    ├── locations/     # 地点
    └── items/         # 道具
```

## 当前项目

| 书名 | 说明 |
|---|---|
| [小说创作](小说创作/README.md) | 日常写作项目 |

## 迁移状态

⏳ 待执行（Phase 4）：物理移动 + 按项目结构规范重构内部结构。
