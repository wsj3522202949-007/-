---
id: tool-07392
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 中文友好, 本地写作]
title: novel-kg
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/liuyuzhangolvz/novel-kg
created: 2026-07-18
updated: 2026-07-18
no: 7392
category: 画龙补充 / 扩容入库 — 补充源
repo: liuyuzhangolvz/novel-kg
stars: 64
url: https://github.com/liuyuzhangolvz/novel-kg
tier: "A"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 3fee7ceecbbcd0a6
  - methods/QUICK_START.md
---

# liuyuzhangolvz/novel-kg

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/liuyuzhangolvz/novel-kg
- **Stars**：64
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：金庸小说人物关系图谱构建
- **本地描述**：novel-kg
- **拉取时间**：2026-07-25 19:20:31

---

# novel-kg
金庸小说人物关系图谱构建

related:
  - methods/QUICK_START.md
---

# 环境

```
Python 3.6+
MongoDB
Neo4j
```

⚠️ 请先启动 MongoDB 和 Neo4j 

# 目录结构
```
|- 
  |- crawl-baike  爬取百度百科
  |- crawl-novel  爬取小说
  |- kgqa  知识图谱文档
  |- mongo2neo  mongo 数据导入 neo4j
```

# 操作说明

**1.爬取金庸小说数据**

启动 MongoDB 进程，执行爬虫文件 xiaoshuo_spider.py ，得到小说文本存入MongoDB。
```
cd crawl-baike
scrapy crawl spider_xiaoshuo
```
**2.爬取小说人物关系**

- 执行转换脚本  convert.py，将 MongoDB 中的小说数据转成文本存到本地。
```
cd crawl-novel
python convert.py
```

- 执行 extract_persons.py ，对小说文本进行词法分析，提取出人名
```
python extract_persons.py
```

- 执行爬虫，根据人名爬取百度百科相关的属下和关系，存入MongoDB。
```
scrapy crawl person_spider
```
**3.MongoDB 转 Neo4j**

执行转换脚本 mongo2neo.py，将 MongoDB 中数据导入 Neo4j 。
```
cd mongo2neo
python mongo2neo.py
```


# 效果
## 人物关系知识图谱
全部人物关系图
![persons relations](https://github.com/liuyuzhangolvz/novel-kg/blob/master/docs/graph.png)

“张无忌”的人物关系图
![张无忌](https://github.com/liuyuzhangolvz/novel-kg/blob/master/docs/%E5%BC%A0%E6%97%A0%E5%BF%8C.png)

# 图谱问答系统
```
cd kgqa
python app.py
```

系统架构
![wenda index](https://github.com/liuyuzhangolvz/novel-kg/blob/master/docs/kgqa.png)

关于张无忌的问答
![wenda zhangwuji](https://github.com/liuyuzhangolvz/novel-kg/blob/master/docs/wenda-zhangwuji.png)

关于周芷若的问答
![wenda zhouzhiruo](https://github.com/liuyuzhangolvz/novel-kg/blob/master/docs/wenda-zhouzhiruo.png)
