---
id: idx-archive
type: index
area: 索引
status: active
tags: [目录冻结, archive, 归档]
title: archive/ — 归档
summary: 不再迭代、只保留不删除的内容。含旧版章节、废弃设定、过期方案、完结书存档。禁止放活跃内容。
source: 内部制定
created: 2026-07-31
updated: 2026-07-31
---

# archive/ — 归档保留

> **冻结职责**：不再迭代、只保留不删除。
> **禁止放入**：活跃项目内容、常用参考资料、正在写的内容。

## 子目录结构

| 子目录 | 用途 |
|---|---|
| `projects/` | 项目归档（旧版章节、废弃设定） |
| `drafts/` | 草稿归档（实验片段留底） |

## 规则

- frontmatter `status: archived` 或 `status: deprecated`
- 保留归档时的原始文件名，不重命名
- **豁免全部机检**（归档内容不要求 frontmatter 合规）
- 允许死链
- **只读**：归档后不再修改内容，除非有明确纠错理由

## 迁移状态

⏳ 待执行（Phase 2）：`archive/` 中已废弃部分移入此目录；未废弃的外部素材移入 `references/`。
