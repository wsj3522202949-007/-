---
id: tool-07521
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 中文友好, 本地写作]
title: classical-modern
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/rockets-cn/classical-modern
created: 2026-07-18
updated: 2026-07-18
no: 7521
category: 画龙补充 / 扩容入库 — 补充源
repo: rockets-cn/classical-modern
stars: 0
url: https://github.com/rockets-cn/classical-modern
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1a128c23d4260482
  - methods/QUICK_START.md
---

# rockets-cn/classical-modern

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/rockets-cn/classical-modern
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：非常全的文言文（古文）-现代文平行语料
- **本地描述**：classical-modern
- **拉取时间**：2026-07-25 19:24:26

related:
  - methods/QUICK_START.md
---

# 文言文（古文）- 现代文平行语料

## 一、语料简介

这是一个非常全的文言文（古文）- 现代文平行语料，基本涵盖了大部分经典古籍著作。从文学角度出发，本项目将所有古文原文整理至文件夹 `古文原文` 中，并对每本古籍，按篇章/章节进行划分与展示，正文部分存于各章节下的 `text.txt` 中，例如 `论语/学而篇/text.txt` ，`孟子/梁惠王章句上/第一节/text.txt` 。对于平行数据，本项目整理至文件夹 `双语数据` 中，这些双语数据是以句子级别为单位进行划分，本项目提供了原文、译文、双语三种数据格式，例如：`论语/学而篇/source.txt` 、 `论语/学而篇/target.txt` 、 `论语/学而篇/bitext.txt` 。注：所有数据均按行保留了古文原文的相对顺序，即数据非打乱。

本语料数据来源于互联网<sup>1</sup>，所爬取到的原始数据是篇章级对齐的双语数据，经过脚本进行分句、对齐，处理成了句子级别对齐的双语（平行）数据，共计 *972467* 句。核心对齐思路采用归一化编辑距离算法与长度比指标。

需要注意 `双语数据` 文件夹中古文数据量少于 `古文原文` 文件夹中的古文数据，这是因为数据来源中部分古文没有译文，也有部分古文的译文残缺，故 `双语数据` 文件夹中仅收录了包含双语句对的数据。

## 二、复现过程

本项目提供了本语料的处理过程及相关脚本，具体过程详见[复现](https://github.com/NiuTrans/Classical-Modern/tree/main/%E5%A4%8D%E7%8E%B0)。

## 三、统计信息

古文原文共包含327本书籍。双语数据共包含97本书籍，其中包含句子级别对齐句子共计 972467 个句对。详细统计信息可查看[统计信息](https://github.com/NiuTrans/Classical-Modern/blob/main/statistic.md)。


## 四、声明

本语料数据均来自互联网。所有数据均注明了出处，可详见各书目下文件 `数据来源.txt` 。原始数据的最终解释权归相关数据来源方所有。

感谢为该语料库做出贡献的成员：谈修泽、罗应峰。

## 五、更新历史

v2.0 2023年3月 重新整理数据，保留更加详尽的原始数据信息，并注明出处

v1.0 2022年2月 数据的初始整理
