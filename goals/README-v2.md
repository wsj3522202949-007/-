---
id: index-goals-v2
type: index
area: 索引
status: active
tags: [索引, 级联, 管理, 导航, AI可执行]
title: 目标级联系统入口 - AI 可执行版本
summary: AI可执行的目标级联系统导航。从愿景到日任务，层层分解，步步落实。
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
ai_instructions:
  purpose: "目标级联系统导航，AI可快速定位和管理目标"
  usage: "读取本文件了解目标级联结构，根据用户需求创建或查询目标"
---

# 目标级联系统 - AI 可执行版本

## AI 指令

**用途**：目标级联系统导航，AI可快速定位和管理目标

**使用方法**：
1. 读取本文件了解目标级联结构
2. 根据用户需求创建或查询目标
3. 每个层级都有明确的文件格式和查询方法

---

## 级联结构

```
3年愿景 (vision.md)
    ↓
年度目标 (yearly/YYYY.md)
    ↓
月度目标 (monthly/YYYY-MM.md)
    ↓
周回顾 (weekly/YYYY-Www.md)
    ↓
日任务 (daily/YYYY-MM-DD.md)
```

---

## 目标管理

### 创建目标

| 操作 | 触发条件 | 执行步骤 | 输出 |
|---|---|---|---|
| 创建愿景 | 用户输入 `create-vision` | 设定愿景→分解目标→创建文件 | vision.md |
| 创建年度目标 | 用户输入 `create-yearly` | 从愿景分解→设定目标→创建文件 | yearly/YYYY.md |
| 创建月度目标 | 用户输入 `create-monthly` | 从年度分解→设定任务→创建文件 | monthly/YYYY-MM.md |
| 创建周回顾 | 用户输入 `create-weekly` | 收集成果→分析挑战→创建文件 | weekly/YYYY-Www.md |
| 创建日任务 | 用户输入 `/daily` | 从月度分解→设定任务→创建文件 | daily/YYYY-MM-DD.md |

### 查询目标

| 操作 | 触发条件 | 执行步骤 | 输出 |
|---|---|---|---|
| 查询愿景 | 用户输入 `query-vision` | 读取文件→返回内容 | 愿景内容 |
| 查询年度目标 | 用户输入 `query-yearly` | 读取文件→返回内容 | 年度目标内容 |
| 查询月度目标 | 用户输入 `query-monthly` | 读取文件→返回内容 | 月度目标内容 |
| 查询周回顾 | 用户输入 `query-weekly` | 读取文件→返回内容 | 周回顾内容 |
| 查询日任务 | 用户输入 `query-daily` | 读取文件→返回内容 | 日任务内容 |
| 查询进度 | 用户输入 `query-progress` | 扫描目标→计算进度→返回报告 | 进度报告 |

---

## 文件格式

### 愿景文件 (vision.md)

```yaml
---
id: goal-vision
type: index
area: 索引
status: active
tags: [愿景, 3年, 长期]
title: 3年愿景
summary: 3年后的理想状态描述，指导所有目标设定。
source: AI 生成
created: {{date}}
updated: {{date}}
related:
  - goals/README.md
see_also:
  - goals/yearly/{{year}}.md
---
```

### 年度目标文件 (yearly/YYYY.md)

```yaml
---
id: goal-yearly-{{year}}
type: index
area: 索引
status: active
tags: [索引, 年度, {{year}}]
title: {{year}}年目标
summary: {{year}}年度目标，从愿景分解，指导月度目标。
source: AI 生成
created: {{date}}
updated: {{date}}
related:
  - goals/vision.md
see_also:
  - goals/monthly/{{year}}-01.md
---
```

### 月度目标文件 (monthly/YYYY-MM.md)

```yaml
---
id: goal-monthly-{{year}}-{{month}}
type: index
area: 索引
status: active
tags: [索引, 月度, {{year}}-{{month}}]
title: {{year}}年{{month}}月目标
summary: {{year}}年{{month}}月目标，从年度目标分解，指导周任务。
source: AI 生成
created: {{date}}
updated: {{date}}
related:
  - goals/yearly/{{year}}.md
see_also:
  - goals/weekly/{{year}}-W{{week}}.md
---
```

### 周回顾文件 (weekly/YYYY-Www.md)

```yaml
---
id: goal-weekly-{{year}}-W{{week}}
type: index
area: 索引
status: active
tags: [索引, 周回顾, {{year}}-W{{week}}]
title: {{year}}年第{{week}}周回顾
summary: {{year}}年第{{week}}周回顾，回顾本周成果，规划下周任务。
source: AI 生成
created: {{date}}
updated: {{date}}
related:
  - goals/monthly/{{year}}-{{month}}.md
see_also:
  - goals/daily/{{date}}.md
---
```

### 日任务文件 (daily/YYYY-MM-DD.md)

```yaml
---
id: goal-daily-{{date}}
type: index
area: 索引
status: active
tags: [索引, 日任务, {{date}}]
title: {{date}} 任务
summary: {{date}} 任务，从月度目标分解，指导今日行动。
source: AI 生成
created: {{date}}
updated: {{date}}
related:
  - goals/weekly/{{year}}-W{{week}}.md
see_also:
  - goals/monthly/{{year}}-{{month}}.md
---
```

---

## 查询语法

### Dataview 查询

```dataview
TABLE title AS "目标", status AS "状态", progress AS "进度", deadline AS "截止日期"
FROM "goals"
WHERE status != "completed"
SORT deadline ASC
```

### 按层级查询

```dataview
TABLE title AS "目标", status AS "状态"
FROM "goals/yearly"
SORT file.name DESC
```

### 按状态查询

```dataview
TABLE title AS "目标", status AS "状态", priority AS "优先级"
FROM "goals"
WHERE status = "active"
SORT priority ASC
```

---

## 使用流程

1. **识别用户意图**：分析用户输入，确定需要的操作
2. **读取目标文件**：读取对应的目标文件，了解内容
3. **执行操作**：按照操作步骤执行
4. **返回结果**：返回查询结果或创建文件

---

## 注意事项

1. **级联原则**：每个目标都必须与上一层级对齐
2. **SMART原则**：目标必须具体、可衡量、可实现、相关、有时限
3. **定期回顾**：每周回顾，每月调整
4. **可视化进度**：使用 Dataview 查询进度
