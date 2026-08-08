---
id: tool-09585
type: tool
area: 库
status: active
tags: [Claude Skill, Python, MIT, 英文文档, RAG]
title: recursive-research
summary: 递归式深度研究 Skill，支持 PhD 级多领域调研，含来源分级和磁盘检查点
source: https://github.com/Anjos2/recursive-research
created: 2026-07-31
updated: 2026-07-31
no: 9585
category: 一、网文 / Claude Skill 生态 写作辅助
repo: Anjos2/recursive-research
stars: 200
url: https://github.com/Anjos2/recursive-research
tier: "B"
use_case: "写硬科幻/悬疑/历史等需要深度考证的网文时，做递归式多轮调研"
pitfalls:
  - "面向学术研究设计，写作场景需调优查询策略"
  - "递归深度过高会消耗大量 token，建议限制深度 2-3 层"
  - "英文资料为主，中文调研需配合专门的搜索策略"
related:
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-31
content_hash: 4388474bbc9b6e12
  - methods/QUICK_START.md
---

# Anjos2/recursive-research

- **分类**：一、网文 / Claude Skill 生态 写作辅助
- **链接**：https://github.com/Anjos2/recursive-research
- **Stars**：~200
- **语言**：Python + Markdown
- **License**：MIT
- **Topics**：claude, skill, research, recursive, agent
- **GitHub 描述**：Recursive research up to PhD level across any domain with source tiering, WDM + Munger inversion for autonomous decisions, and disk checkpointing
- **本地描述**：递归式深度研究 Skill，支持多领域调研，含来源分级、自主决策和磁盘检查点
- **拉取时间**：2026-07-31

---

## 核心价值

不是简单搜一下就结束，而是像做学术研究一样**递归深挖**：搜索→发现新线索→追搜新线索→再发现→再追搜，直到满足深度要求。支持来源分级（学术>官方>媒体>博客），并在磁盘上保存检查点以防上下文压缩丢失数据。

### 写作场景应用

1. **硬科幻世界观构建**：写造芯片/航天/量子计算等硬科技内容时，递归调研技术原理→应用案例→最新进展→可行性边界
2. **悬疑推理逻辑链**：设计复杂诡计时，递归调研法医/刑侦/法律程序，确保每个推理环节经得起推敲
3. **历史年代文考证**：递归调研特定年代的物价/事件/风俗/语言/建筑/服饰，层层深入到生活细节
4. **商业文行业逻辑**：写商战/创业文时，递归调研行业运作模式→利益链条→常见套路→真实案例

### 递归研究流程

```
第0层：初始搜索（如"芯片制造流程"）
  ↓ 发现线索："光刻机""EDA软件""晶圆代工"
第1层：追搜每个线索
  ↓ "光刻机"→"ASML垄断""EUV vs DUV""国产替代"
第2层：继续追搜关键子线索
  ↓ "国产替代"→"上海微电子""28nm vs 7nm""技术差距"
第3层：最终输出结构化报告
  → 含来源分级 + 交叉验证 + 可信度评估
```

### 来源分级机制

| 级别 | 来源类型 | 可信度 |
|---|---|related:
  - methods/QUICK_START.md
---|
| Tier 1 | 学术论文、官方报告 | ★★★★★ |
| Tier 2 | 政府网站、权威机构 | ★★★★ |
| Tier 3 | 主流媒体、行业报告 | ★★★ |
| Tier 4 | 博客、论坛、自媒体 | ★★ |

### 磁盘检查点

研究过程中的中间结果会保存到磁盘，即使上下文被压缩也不会丢失已收集的数据，适合长时间深度调研。
