---
id: index-goals
type: index
area: 索引
status: active
tags: [索引, 级联, 管理, 导航]
title: 目标级联系统入口
summary: 目标级联系统导航——3年愿景、年度目标、月度目标、周回顾、日任务。提升目标管理效率。
source: 内部制定
created: 2026-08-02
updated: 2026-08-02
related:
  - README.md
  - CLAUDE.md
  - ai/workflows/目标回顾.md
see_also:
  - methods/QUICK_START.md
  - ai/README.md
---

# 🎯 目标级联系统

> 本目录是目标级联系统的**唯一入口**。从愿景到日任务，层层分解，步步落实。

---

## 一、级联结构

```
3年愿景 (vision.md)
    ↓
年度目标 (yearly/)
    ↓
月度目标 (monthly/)
    ↓
周回顾 (weekly/)
    ↓
日任务 (daily/)
```

**核心原则**：每个层级的目标都必须与上一层级对齐。

---

## 二、快速导航

| 我想做什么 | 直接去 |
|---|---|
| 设定长期愿景 | `vision.md` |
| 制定年度目标 | `yearly/YYYY.md` |
| 分解月度目标 | `monthly/YYYY-MM.md` |
| 执行周回顾 | `weekly/YYYY-Www.md` |
| 记录日任务 | `daily/YYYY-MM-DD.md` |
| 学习目标管理 | `GUIDE.md` |

---

## 三、目录结构

```
goals/
├── README.md           # 本文件（导航入口）
├── vision.md           # 3年愿景
├── GUIDE.md            # 目标管理指南
├── yearly/             # 年度目标
│   └── 2026.md
├── monthly/            # 月度目标
│   └── 2026-08.md
├── weekly/             # 周回顾
│   └── 2026-W31.md
└── daily/              # 日任务
    └── 2026-08-02.md
```

---

## 四、使用流程

### 4.1 设定愿景（每年一次）
1. 编辑 `vision.md`
2. 描述 3 年后的理想状态
3. 分解为年度目标

### 4.2 制定年度目标（每年一次）
1. 创建 `yearly/YYYY.md`
2. 从愿景分解出 3-5 个关键目标
3. 设定可衡量的里程碑

### 4.3 分解月度目标（每月一次）
1. 创建 `monthly/YYYY-MM.md`
2. 从年度目标分解出本月重点
3. 设定具体可执行的任务

### 4.4 执行周回顾（每周一次）
1. 创建 `weekly/YYYY-Www.md`
2. 回顾本周成果和挑战
3. 调整下周计划

### 4.5 记录日任务（每天一次）
1. 创建 `daily/YYYY-MM-DD.md`
2. 从月度目标分解今日任务
3. 晚间回顾完成情况

---

## 五、Dataview 查询

### 查看所有未完成目标
```dataview
TABLE status AS "状态", priority AS "优先级", deadline AS "截止日期"
FROM "goals"
WHERE status != "completed"
SORT deadline ASC
```

### 查看本月重点目标
```dataview
TABLE title AS "目标", progress AS "进度"
FROM "goals/monthly"
WHERE file.name = dateformat(date(now), "yyyy-MM")
```

---

## 六、最佳实践

1. **SMART 原则**：目标必须具体、可衡量、可实现、相关、有时限
2. **对齐原则**：每个目标都必须与上一层级对齐
3. **定期回顾**：每周回顾，每月调整
4. **可视化进度**：使用 Dataview 查询进度

---

## 七、常见问题

### Q: 目标太多怎么办？
A: 使用优先级筛选，聚焦最重要的 3 个目标。

### Q: 目标未完成怎么办？
A: 分析原因，调整计划，继续执行。

### Q: 如何保持动力？
A: 定期回顾愿景，庆祝小胜利。

---

> 本系统基于目标级联方法论，帮助你从愿景到行动，层层落实。
