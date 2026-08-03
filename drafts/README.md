---
id: idx-drafts
type: index
area: 索引
status: active
tags: [目录冻结, drafts, 草稿]
title: drafts/ — 写作中
summary: 正在写、未校验、可能冲突的内容。含 inbox/journal/scratch/projects 子目录。禁止放已校验最终稿。
source: 内部制定
created: 2026-07-31
updated: 2026-07-31
related:
  - README.md
  - knowledge/README.md
  - methods/README.md
  - projects/README.md
---

# drafts/ — 写作中

> **冻结职责**：正在写、未校验、可能冲突的内容。
> **禁止放入**：已校验最终稿（→projects/*/chapters/）、归档内容（→archive/）。

## 子目录结构

| 子目录 | 来源 | 用途 |
|---|---|---|
| `inbox/` | 原 `收件箱/` | 临时待整理（随手记/截图/链接） |
| `journal/` | 原 `日记/` | 每日时间流 |
| `scratch/` | 原 `drafts/scratch/` | 临时草稿/实验片段 |
| `projects/` | 按项目隔离 | 项目未定稿章节 |

## 生命周期

```
drafts/  →（通过自检 + 校验后）→  projects/*/chapters/
drafts/  →（不再迭代后）→  archive/
```

## 规则

- frontmatter `status: draft`
- **不参与 ERROR 级机检**（草稿可以缺字段、可以脏）
- 允许死链（目标可能尚未创建）
- 任何人随时改，不需走流程

## 迁移状态

⏳ 待执行（Phase 1）：移动空目录 + 低风险内容。
