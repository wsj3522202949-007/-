---
id: index-methods-dataview
type: index
area: 索引
status: active
tags: [Dataview, 方法论, 查询, 导航]
title: 方法论 Dataview 索引
summary: 方法论 Dataview 动态视图——按类型、目录、关键词筛选方法论。所有查询基于真实 frontmatter。
source: 内部制定
created: 2026-08-02
updated: 2026-08-03
related:
  - methods/README.md
  - tools/Dataview索引.md
see_also:
  - methods/QUICK_START.md
  - methods/SKILL.md
---

# 方法论 Dataview 索引

> 方法论 frontmatter：`id`, `type`(=ref/guide/index), `area`(=方法/索引), `status`, `tags`, `title`, `summary`
> 注意：methods/ 下大部分文件 tags 为空，查询优先用 `type`、`area`、`title` 关键词。

---

## 一、按类型筛选

### 1.1 指南类（guide）
```dataview
TABLE title AS "文档", summary AS "摘要"
FROM "methods"
WHERE type = "guide" AND area = "方法"
SORT title ASC
```

### 1.2 参考类（ref）
```dataview
TABLE title AS "文档", summary AS "摘要"
FROM "methods"
WHERE type = "ref" AND area = "方法"
SORT title ASC
```

### 1.3 索引类（index）
```dataview
TABLE title AS "文档", summary AS "摘要"
FROM "methods"
WHERE type = "index"
SORT title ASC
```

---

## 二、按子目录筛选

### 2.1 SKILL 大纲（skill_parts/）
```dataview
TABLE title AS "章节", summary AS "摘要"
FROM "methods/skill_parts"
SORT file.name ASC
```

### 2.2 实战模板（templates/）
```dataview
TABLE title AS "模板", summary AS "摘要"
FROM "methods/templates"
SORT file.name ASC
```

### 2.3 项目骨架模板
```dataview
TABLE title AS "模板", summary AS "摘要"
FROM "methods/项目骨架模板"
SORT file.name ASC
```

---

## 三、按关键词筛选

> 改 `contains(title, "关键词")` 中的关键词即可。

### 3.1 去 AI 味相关
```dataview
TABLE title AS "文档", summary AS "摘要", file.mtime AS "更新时间"
FROM "methods"
WHERE contains(title, "去AI味")
SORT file.mtime DESC
```

### 3.2 大纲相关
```dataview
TABLE title AS "文档", summary AS "摘要"
FROM "methods"
WHERE contains(title, "大纲")
SORT title ASC
```

### 3.3 人物相关
```dataview
TABLE title AS "文档", summary AS "摘要"
FROM "methods"
WHERE contains(title, "人物")
SORT title ASC
```

### 3.4 签约相关
```dataview
TABLE title AS "文档", summary AS "摘要"
FROM "methods"
WHERE contains(title, "签约")
SORT title ASC
```

### 3.5 开篇 / 钩子相关
```dataview
TABLE title AS "文档", summary AS "摘要"
FROM "methods"
WHERE contains(title, "开篇") OR contains(title, "钩子")
SORT title ASC
```

### 3.6 节奏 / 节拍相关
```dataview
TABLE title AS "文档", summary AS "摘要"
FROM "methods"
WHERE contains(title, "节奏") OR contains(title, "节拍")
SORT title ASC
```

---

## 四、按更新时间筛选

### 4.1 最近更新
```dataview
TABLE title AS "文档", summary AS "摘要", file.mtime AS "更新时间"
FROM "methods"
SORT file.mtime DESC
LIMIT 10
```

### 4.2 最近创建
```dataview
TABLE title AS "文档", summary AS "摘要", file.ctime AS "创建时间"
FROM "methods"
SORT file.ctime DESC
LIMIT 10
```

---

## 五、自定义查询

```dataview
TABLE field1 AS "列名1", field2 AS "列名2"
FROM "methods"
WHERE type = "guide" AND contains(title, "关键词")
SORT file.mtime DESC
LIMIT 10
```

### 常用条件
- `type = "guide"`：指南类
- `type = "ref"`：参考类
- `area = "方法"`：方法论区域
- `contains(title, "关键词")`：标题包含关键词
- `file.mtime > date(today) - dur(7 days)`：最近 7 天更新

---

> 所有查询基于真实 frontmatter。完整方法论导航见 [导览](导览.md)，快速入口见 [QUICK_START](QUICK_START.md)。
