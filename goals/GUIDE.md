---
id: guide-goal-management
type: guide
area: 方法
status: active
tags: [索引, 管理, 指南, 级联]
title: 目标管理指南
summary: 如何使用目标级联系统，从愿景到行动，层层落实。
source: 内部制定
created: 2026-08-02
updated: 2026-08-02
related:
  - goals/README.md
  - goals/vision.md
see_also:
  - methods/QUICK_START.md
---

# 📚 目标管理指南

> 本指南介绍如何使用目标级联系统，从愿景到行动，层层落实。

---

## 一、核心理念

### 1.1 级联原则
- **从上到下**：愿景 → 年度 → 月度 → 周 → 日
- **对齐原则**：每个目标都必须与上一层级对齐
- **分解原则**：大目标分解为小目标，小目标分解为行动

### 1.2 SMART 原则
- **S**pecific（具体）：目标要明确
- **M**easurable（可衡量）：有量化指标
- **A**chievable（可实现）：在能力范围内
- **R**elevant（相关）：与愿景相关
- **T**ime-bound（有时限）：有截止日期

---

## 二、操作流程

### 2.1 设定愿景（每年一次）
1. 打开 `vision.md`
2. 描述 3 年后的理想状态
3. 分解为年度目标
4. 设定核心价值和成功标准

### 2.2 制定年度目标（每年一次）
1. 创建 `yearly/YYYY.md`
2. 从愿景分解出 3-5 个关键目标
3. 设定可衡量的里程碑
4. 分解为季度重点

### 2.3 分解月度目标（每月一次）
1. 创建 `monthly/YYYY-MM.md`
2. 从年度目标分解出本月重点
3. 设定具体可执行的任务
4. 分配优先级

### 2.4 执行周回顾（每周一次）
1. 创建 `weekly/YYYY-Www.md`
2. 回顾本周成果和挑战
3. 分析未完成原因
4. 调整下周计划

### 2.5 记录日任务（每天一次）
1. 创建 `daily/YYYY-MM-DD.md`
2. 从月度目标分解今日任务
3. 设定优先级和时间块
4. 晚间回顾完成情况

---

## 三、模板使用

### 3.1 年度目标模板
使用 `yearly/TEMPLATE.md` 创建年度目标。

### 3.2 月度目标模板
使用 `monthly/TEMPLATE.md` 创建月度目标。

### 3.3 周回顾模板
使用 `weekly/TEMPLATE.md` 创建周回顾。

### 3.4 日任务模板
使用 `daily/TEMPLATE.md` 创建日任务。

---

## 四、Dataview 查询

### 4.1 查看所有未完成目标
```dataview
TABLE status AS "状态", priority AS "优先级", deadline AS "截止日期"
FROM "goals"
WHERE status != "completed"
SORT deadline ASC
```

### 4.2 查看本月重点目标
```dataview
TABLE title AS "目标", progress AS "进度"
FROM "goals/monthly"
WHERE file.name = dateformat(date(now), "yyyy-MM")
```

### 4.3 查看本周回顾
```dataview
TABLE title AS "回顾", achievements AS "成果", challenges AS "挑战"
FROM "goals/weekly"
SORT file.name DESC
LIMIT 4
```

---

## 五、常见问题

### Q: 目标太多怎么办？
A: 使用优先级筛选，聚焦最重要的 3 个目标。

### Q: 目标未完成怎么办？
A: 分析原因，调整计划，继续执行。

### Q: 如何保持动力？
A: 定期回顾愿景，庆祝小胜利。

### Q: 目标冲突怎么办？
A: 与愿景对齐，选择更相关的目标。

---

## 六、最佳实践

1. **定期回顾**：每周回顾，每月调整
2. **可视化进度**：使用 Dataview 查询进度
3. **保持灵活**：根据实际情况调整目标
4. **庆祝胜利**：完成目标后庆祝

---

## 七、工具支持

| 工具 | 用途 |
|---|---|
| Dataview | 查询和筛选目标 |
| Templater | 创建目标模板 |
| QuickAdd | 快速创建目标 |
| Obsidian Git | 版本控制 |

---

> 本指南帮助你使用目标级联系统，从愿景到行动，层层落实。
