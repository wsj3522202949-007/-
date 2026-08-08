---
id: tool-07387
type: tool
area: 库
status: active
tags: [HTML, 协议宽松, 本地优先, 中文友好, 大纲规划, 本地写作]
title: tao-kb
summary: 搭大纲/分卷/节拍
source: https://github.com/lingtian/tao-kb
created: 2026-07-18
updated: 2026-07-18
no: 7387
category: 画龙补充 / 扩容入库 — 补充源
repo: lingtian/tao-kb
stars: 5
url: https://github.com/lingtian/tao-kb
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: a0b9bd9d1477054a
  - methods/QUICK_START.md
---

# lingtian/tao-kb

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/lingtian/tao-kb
- **Stars**：5
- **语言**：HTML
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：tao-kb (道教知识库) 项目简介：AI助力探索千年道统。 tao-kb 是一个由 AI Agent 驱动的开源知识工程项目，致力于系统性地搜集、归纳、整理与标注“道”的相关典籍与思想体系，并将其转化为可交互、可推理、可视化的结构化知识库，为现代修行者提供一套面向未来的 “科学修仙” 数字化工具体系。
- **本地描述**：tao-kb
- **拉取时间**：2026-07-25 19:20:23

---

# tao-kb 道教知识库

tao-kb 是一个由 AI Agent 协作构建的道教典籍知识工程项目。它把道家、道教、内丹、符箓、科仪、劝善、神仙传记等文本收集为 Markdown 原文，再通过规则和语义词表生成 tagged 章节、知识图谱、二层关系和可交互阅读器。

当前项目重点不是做静态文档库，而是建立一套可持续扩展的古籍处理流水线：

1. 抓取或导入典籍原文到 `texts/`
2. 自动/半自动标注为 `chapters/**/*.tagged.md`
3. 聚合统一实体索引 `entities/index.json`
4. 生成单书知识图谱到 `graphs/classics/*_kg.json` / `graphs/classics/*_kg.mmd`
5. 生成跨章节二层关系 `relations/secondary_relations.json`
6. 渲染可点击实体卡片的网页阅读器 `docs/index.html`
7. 通过审计报告检查空文件、坏标签和标签体系漂移

## 当前状态

更新时间：2026-06-16

| 指标 | 当前值 |
| --- | ---: |
| 原文 Markdown | 53 部/份 `*full.md` |
| 全仓库 Markdown | 226 个 |
| 活跃 tagged 文件 | 128 个 |
| 活跃标签数 | 103,064 |
| 统一实体数 | 845 |
| 唯一标签名 | 811 |
| 阅读器章节 | 135 |
| 二层关系 | 62,628 |
| 空 Markdown | 0 |
| 空 tagged 文件 | 0 |
| 零标签 active 文件 | 0 |
| 畸形标签 | 0 |

审计入口：

- [reports/tag_audit.md](https://github.com/lingtian/tao-kb/blob/main/reports/tag_audit.md)
- [reports/tag_audit.json](https://github.com/lingtian/tao-kb/blob/main/reports/tag_audit.json)

总纲入口：

- [docs/corpus_outline.md](https://github.com/lingtian/tao-kb/blob/main/docs/corpus_outline.md)
- [data/corpus_outline.json](https://github.com/lingtian/tao-kb/blob/main/data/corpus_outline.json)

阅读器入口：

- [docs/index.html](https://github.com/lingtian/tao-kb/blob/main/docs/index.html)

## 已收集典籍

### 哲学与道家经典

- 《道德经》
- 《庄子》
- 《列子》
- 《文子》
- 《关尹子》
- 《管子》
- 《鹖冠子》
- 《淮南子》
- 《老子想尔注》
- 《老子指歸》
- 《老子化胡經》
- 《化書》

目录：`texts/Philosophy(哲学)/`

### 丹道与相关经典

- 《抱朴子》
- 《周易参同契》
- 《黄帝阴符经》
- 《清静经》
- 《悟真篇》
- 《入藥鏡》
- 《鍾呂傳道集》
- 《靈寶畢法》
- 《上清大洞真经》
- 《黄庭经》
- 《灵宝度人经》
- 《太上灵宝五符序》
- 《正一法文》
- 《三五都功经箓》

目录：`texts/Alchemy(丹道体系)/`

### 身体图景与养生修持

- 《坐忘論》
- 《天隱子》
- 《洞玄靈寶定觀經》
- 《太上老君內觀經》
- 《養性延命錄》
- 《服氣精義論》

目录：`texts/Body System(身体图景)/`

### 宇宙观与早期道教

- 《太平經》

目录：`texts/Cosmology(宇宙观)/`

### 道教类书与总集

- 《雲笈七籤》
- 《無上秘要》
- 《道教義樞》
- 《三洞珠囊》

目录：`texts/Daoist Canon(道教类书)/`

### 神仙传记与洞天叙事

- 《真誥》
- 《神仙傳》
- 《列仙傳》
- 《海內十洲記》

目录：`texts/Hagiography(神仙传记)/`

### 伦理、劝善与功过格

- 《太上感應篇》
- 《文昌帝君陰騭文》
- 《關聖帝君覺世真經》
- 《太微仙君功過格》
- 《文昌帝君功過格》

目录：`texts/Ethics(伦理戒律)/`

### 符箓、神咒与科仪

- 《上清佩符文白券訣》
- 《太極左仙公說神符經》
- 《太上三洞神呪》
- 《太上洞淵三昧神呪齋清旦行道儀》
- 《太上洞淵神咒經》
- 《太上洞玄靈寶真文要解上經》
- 《高上玉皇本行集經》

目录：`texts/Ritual(科仪符箓)/`

符咒相关文本已额外补标到 `chapters/fulu/`，并对《雲笈七籤》《無上秘要》《三洞珠囊》《太上洞淵神咒經》《太上洞玄靈寶真文要解上經》《高上玉皇本行集經》等现有章节做了符箓/咒诀/科仪/法术/器物/神名/星宿/方位补标。

## 标签体系

标签格式统一为：

```text
全角左标记 + @标签类型:标签名 + 全角右标记
```

当前标签类型映射见 [tag_taxonomy.json](https://github.com/lingtian/tao-kb/blob/main/tag_taxonomy.json)。

主要层级：

- 实体：人物、地名、生物、神名、器物
- 思想：概念、主体
- 修行：境界、身神
- 宇宙：星宿、方位
- 科仪：符箓、咒诀、科仪、法术
- 伦理：德目、善行、恶行、过失、果报、戒律
- 修辞：隐喻、意象
- 关系：对立

## 关键目录

| 路径 | 用途 |
| --- | related:
  - methods/QUICK_START.md
--- |
| `texts/` | 原文 Markdown，按主题分类 |
| `chapters/` | tagged 章节，是阅读器和图谱的主要输入 |
| `chapters/fulu/` | 符箓/神咒/科仪专门 tagged 输出 |
| `graphs/classics/` | 单书知识图谱 JSON/Mermaid 产物 |
| `graphs/philosophy/` | 哲学层综合图谱和报告 |
| `data/` | 辅助索引数据，包括 `corpus_outline.json` |
| `relations/` | 二层关系数据 |
| `docs/index.html` | 静态网页阅读器 |
| `docs/corpus_outline.md` | 已收录道教书籍的总纲与分门别类导航 |
| `reports/` | 标签审计报告 |
| `skills/` | 项目内技能/标注说明 |
| `scripts/` | 抓取、拆分、标注、图谱、渲染、审计脚本 |

## 常用脚本

### 抓取原文

```bash
python3 scripts/crawl_expanded_taoist_sources.py
python3 scripts/crawl_expanded_taoist_sources.py --only 雲笈七籤 無上秘要
python3 scripts/crawl_alchemy_canons.py
python3 scripts/crawl_ritual_wikisource.py
```

### 自动标注

```bash
python3 scripts/auto_tag_batch.py
python3 scripts/auto_tag_batch.py --only 雲笈七籤 無上秘要
python3 scripts/auto_tag_fulu_terms.py
python3 scripts/auto_tag_ethics_terms.py
```

### 拆分已有大文本

```bash
python3 scripts/split_baopuzi.py
python3 scripts/split_wenzi.py
python3 scripts/split_liezi_wenzi.py
```

### 生成实体、图谱、关系和阅读器

```bash
python3 scripts/build_corpus_outline.py
python3 scripts/build_entity_index.py
python3 scripts/generate_kg_batch.py
python3 scripts/build_secondary_relations.py
python3 scripts/render_tao_html.py
```

### 审计质量

```bash
python3 scripts/audit_markdown_tags.py
```

## 推荐工作流

每次新增典籍或改标签词表后，建议按这个顺序执行：

```bash
python3 -m py_compile scripts/*.py
python3 scripts/auto_tag_batch.py --only <书名>
python3 scripts/auto_tag_fulu_terms.py
python3 scripts/auto_tag_ethics_terms.py
python3 scripts/audit_markdown_tags.py
python3 scripts/build_corpus_outline.py
python3 scripts/build_entity_index.py
python3 scripts/generate_kg_batch.py --only <相关章节目录>
python3 scripts/build_secondary_relations.py
python3 scripts/render_tao_html.py
```

如果只是修改符咒/科仪标签，优先运行：

```bash
python3 scripts/auto_tag_fulu_terms.py
python3 scripts/generate_kg_batch.py --only fulu 雲笈七籤 無上秘要 三洞珠囊 太上洞淵神咒經 太上洞玄靈寶真文要解上經 高上玉皇本行集經
python3 scripts/build_corpus_outline.py
python3 scripts/build_entity_index.py
python3 scripts/build_secondary_relations.py
python3 scripts/render_tao_html.py
python3 scripts/audit_markdown_tags.py
```

## 给后来 Agent 的快速接手说明

先读这几个文件：

1. [README.md](https://github.com/lingtian/tao-kb/blob/main/README.md)：项目地图和书目总览
2. [docs/corpus_outline.md](https://github.com/lingtian/tao-kb/blob/main/docs/corpus_outline.md)：全库书目总纲，按门类看哪些书已标注、哪些还没动
3. [reports/tag_audit.md](https://github.com/lingtian/tao-kb/blob/main/reports/tag_audit.md)：当前质量状态和标签统计
4. [tag_taxonomy.json](https://github.com/lingtian/tao-kb/blob/main/tag_taxonomy.json)：标签类型到一级分类的映射
5. [entities/index.json](https://github.com/lingtian/tao-kb/blob/main/entities/index.json)：由标签聚合出的统一实体索引
6. [scripts/build_corpus_outline.py](https://github.com/lingtian/tao-kb/blob/main/scripts/build_corpus_outline.py)：总纲生成逻辑
7. [scripts/build_entity_index.py](https://github.com/lingtian/tao-kb/blob/main/scripts/build_entity_index.py)：实体索引生成逻辑
8. [scripts/auto_tag_batch.py](https://github.com/lingtian/tao-kb/blob/main/scripts/auto_tag_batch.py)：通用批量标注
9. [scripts/auto_tag_fulu_terms.py](https://github.com/lingtian/tao-kb/blob/main/scripts/auto_tag_fulu_terms.py)：符箓/神咒/科仪专门标注
10. [scripts/auto_tag_ethics_terms.py](https://github.com/lingtian/tao-kb/blob/main/scripts/auto_tag_ethics_terms.py)：劝善/功过格专门标注
11. [scripts/render_tao_html.py](https://github.com/lingtian/tao-kb/blob/main/scripts/render_tao_html.py)：阅读器与实体卡片生成逻辑

接手时注意：

- 工作区可能有大量未提交生成文件，不要随手清理或回滚。
- `docs/corpus_outline.md` 是项目书目总纲，新增原文、补标章节或整理分类后要一并重建。
- `chapters/**/*.tagged.md` 是核心语料输入，修改后要重建实体索引、阅读器、图谱和二层关系。
- 阅读器里的高亮标签已经可点击，会从 `entities/index.json` 中读取出现次数、章节分布、样例上下文和关联实体。
- `relations/secondary_relations.json` 已包含初步道教语义关系，如 `invokes_deity`、`used_in_ritual`、`uses_object`、`commands_deity`、`has_directional_context` 等。
- 大部头如《雲笈七籤》《無上秘要》目前仍多以整部书一个 tagged 文件存在，后续最值得做的是按卷/篇拆分。
- `skills/SKILL_Tao_NER.md` 里有示例标签类型 `类型`，审计会把它列为 unknown，但它不是正文语料问题。
- 对符咒文本，优先维护 `scripts/auto_tag_fulu_terms.py` 的词表，再重新生成 `chapters/fulu/` 和相关章节补标。

## 下一步建议

- 将《雲笈七籤》《無上秘要》《真誥》按卷拆分，提升跨章节共现关系质量。
- 为符箓文本增加更细标签，如神将、雷法、章奏、坛仪、步罡、法器；目前这些仍合并在神名/法术/科仪/器物等类型下。
- 继续做实体归并，把“玉皇 / 玉皇上帝 / 昊天金阙至尊玉皇大帝”等别名合并到稳定实体 ID。
- 为每部原文补充来源元数据、版本说明和采集时间。
- 把 `docs/index.html` 发布到 GitHub Pages，方便在线阅读和人工校对。
