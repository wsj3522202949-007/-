---
id: index-dataview
type: index
area: 索引
status: active
tags: [Dataview, 动态视图, 查询, 导航]
title: Dataview 动态视图入口
summary: Dataview 动态视图导航——可视化筛选，告别肉眼翻卡。所有查询基于真实 frontmatter 字段。
source: 内部制定
created: 2026-08-02
updated: 2026-08-03
related:
  - tools/README.md
  - tools/仪表盘.md
see_also:
  - methods/Dataview索引.md
  - goals/GUIDE.md
---

# Dataview 动态视图

> 本文件是 Dataview 动态视图的**核心入口**。所有查询基于实际 frontmatter 字段，Obsidian 打开即可实时渲染。
> **前置**：需安装 [Dataview 社区插件](obsidian://show-plugin?id=dataview)。

---

## 一、工具视图（tools/cards/）

> 工具卡 frontmatter：`id`, `type`(=tool), `area`(=库), `status`, `tags`, `title`, `summary`, `category`, `repo`, `stars`, `tier`, `use_case`, `pitfalls`, `url`, `language`, `license`

### 1.1 S/A 级工具总览
```dataview
TABLE tier AS "评级", category AS "类别", stars AS "Stars", use_case AS "用途"
FROM "tools/cards"
WHERE tier = "S" OR tier = "A"
SORT tier ASC, stars DESC
```

### 1.2 按任务找工具（示例：去AI味）
> 改 `contains(tags, "去AI味")` 中的标签名即可切换任务。可用标签见 [标签规范](标签规范.md)。
```dataview
TABLE tier AS "评级", stars AS "Stars", use_case AS "用途"
FROM "tools/cards"
WHERE contains(tags, "去AI味") AND tier IN ("S", "A")
SORT stars DESC
```

### 1.3 按编程语言找工具
> 改 `language = "Python"` 为 `TypeScript` / `JavaScript` / `C#` / `Go` 等。
```dataview
TABLE tier AS "评级", stars AS "Stars", use_case AS "用途", license AS "协议"
FROM "tools/cards"
WHERE language = "Python" AND tier IN ("S", "A")
SORT stars DESC
```

### 1.4 本地优先 S/A（零成本可用）
```dataview
TABLE stars AS "Stars", use_case AS "用途", category AS "类别"
FROM "tools/cards"
WHERE contains(tags, "本地优先") AND tier IN ("S", "A")
SORT stars DESC
```

### 1.5 可商用 S/A（协议宽松）
```dataview
TABLE stars AS "Stars", use_case AS "用途", tags AS "标签"
FROM "tools/cards"
WHERE contains(tags, "协议宽松") AND tier IN ("S", "A")
SORT stars DESC
```

### 1.6 最近入库
```dataview
TABLE file.mtime AS "入库时间", tier AS "评级", stars AS "Stars", use_case AS "用途"
FROM "tools/cards"
SORT file.mtime DESC
LIMIT 15
```

### 1.7 按分类计数
```dataview
TABLE WITHOUT ID category AS "分类", length(rows) AS "工具数"
FROM "tools/cards"
GROUP BY category
SORT length(rows) DESC
```

---

## 二、方法论视图（methods/）

> 方法论 frontmatter：`id`, `type`(=ref/guide/index), `area`(=方法/索引), `status`, `tags`, `title`, `summary`
> 注意：methods/ 下大部分文件 tags 为空，查询优先用 `type` 和 `title` 关键词匹配。

### 2.1 指南类方法论
```dataview
TABLE title AS "文档", summary AS "摘要"
FROM "methods"
WHERE type = "guide" AND area = "方法"
SORT title ASC
```

### 2.2 参考类方法论
```dataview
TABLE title AS "文档", summary AS "摘要"
FROM "methods"
WHERE type = "ref" AND area = "方法"
SORT title ASC
```

### 2.3 按关键词找方法论
> 改 `contains(title, "去AI味")` 中的关键词即可。
```dataview
TABLE title AS "文档", summary AS "摘要", file.mtime AS "更新时间"
FROM "methods"
WHERE contains(title, "去AI味")
SORT file.mtime DESC
```

### 2.4 方法论 SKILL 大纲（skill_parts/）
```dataview
TABLE title AS "章节", summary AS "摘要"
FROM "methods/skill_parts"
SORT file.name ASC
```

### 2.5 最近更新的方法论
```dataview
TABLE title AS "文档", summary AS "摘要", file.mtime AS "更新时间"
FROM "methods"
SORT file.mtime DESC
LIMIT 10
```

---

## 三、目标视图（goals/）

> 目标 frontmatter：`id`, `type`(=index), `area`(=索引), `status`, `tags`, `title`, `summary`
> 注意：goals/ 下无 `progress`、`deadline`、`priority` 字段，用 `status` + `title` 关键词筛选。

### 3.1 年度目标
```dataview
TABLE title AS "目标", status AS "状态", summary AS "摘要"
FROM "goals/yearly"
SORT file.name DESC
```

### 3.2 月度目标
```dataview
TABLE title AS "目标", status AS "状态", summary AS "摘要"
FROM "goals/monthly"
SORT file.name DESC
```

### 3.3 本周任务
```dataview
TABLE title AS "任务", status AS "状态", summary AS "摘要"
FROM "goals/weekly"
SORT file.name DESC
```

### 3.4 近期日任务
```dataview
TABLE title AS "任务", status AS "状态"
FROM "goals/daily"
SORT file.name DESC
LIMIT 7
```

---

## 四、项目视图（projects/）

> 项目 frontmatter：`id`, `type`(=project/ref), `area`(=项目), `status`, `tags`, `title`, `summary`
> 项目 README 扩展字段：`platform`, `genre`, `target`, `word_target`

### 4.1 全部项目状态
```dataview
TABLE title AS "项目", status AS "状态", genre AS "题材", platform AS "平台", word_target AS "目标字数"
FROM "projects"
WHERE type = "project"
SORT file.mtime DESC
```

### 4.2 活跃项目
```dataview
TABLE title AS "项目", status AS "状态", tags AS "标签", summary AS "摘要"
FROM "projects"
WHERE status = "wip" OR status = "active"
SORT file.mtime DESC
```

### 4.3 项目进度文件
```dataview
TABLE title AS "项目", status AS "状态", tags AS "标签"
FROM "projects"
WHERE type = "ref" AND area = "项目"
SORT file.mtime DESC
```

---

## 五、全局视图

### 5.1 最近修改的文件
```dataview
TABLE type AS "类型", area AS "区域", file.mtime AS "修改时间"
FROM ""
WHERE area AND type
SORT file.mtime DESC
LIMIT 20
```

### 5.2 按区域统计
```dataview
TABLE WITHOUT ID area AS "区域", length(rows) AS "文件数"
FROM ""
WHERE area
GROUP BY area
SORT length(rows) DESC
```

### 5.3 按类型统计
```dataview
TABLE WITHOUT ID type AS "类型", length(rows) AS "文件数"
FROM ""
WHERE type
GROUP BY type
SORT length(rows) DESC
```

---

## 六、自定义查询模板

```dataview
TABLE field1 AS "列名1", field2 AS "列名2"
FROM "目录路径"
WHERE field = "value"
SORT field ASC
LIMIT 10
```

### 常用条件
- `tier = "S"`：评级等于 S
- `contains(tags, "标签名")`：标签包含
- `contains(title, "关键词")`：标题包含
- `tier IN ("S", "A")`：评级在范围内
- `file.mtime > date(today) - dur(7 days)`：最近 7 天更新

---

> 所有查询基于真实 frontmatter 字段。标签规范见 [标签规范](标签规范.md)，工具选型见 [工具选型指南](工具选型指南.md)。
