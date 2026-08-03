---
id: index-agents
type: index
area: 索引
status: active
tags: [方法, AI, 自动化, 导航, AI可执行]
title: 代理系统入口
summary: AI可执行的代理系统导航。每个代理都有明确的触发条件、执行步骤和输出格式。
source: 内部制定
created: 2026-08-02
updated: 2026-08-03
related:
  - ai/README.md
  - CLAUDE.md
see_also:
  - ai/skills/README.md
  - schema/维护标准.md
ai_instructions:
  purpose: "代理系统导航，AI可快速定位和调用代理"
  usage: "读取本文件了解所有可用代理，根据用户输入或定期任务调用对应代理"
---

# 代理系统

> 本目录是代理系统的唯一入口。每个代理文件包含结构化的 ai_instructions。

---

## 代理列表

### 维护代理

| 代理 | 触发条件 | 执行步骤 | 输出 |
|---|---|---|---|
| `inbox-processor` | 用户输入 `inbox-processor` 或每日执行 | 扫描→分类→处理→报告 | 处理报告 |
| `note-organizer` | 用户输入 `note-organizer` 或每周六执行 | 扫描→分析→整理→报告 | 整理报告 |
| `weekly-reviewer` | 用户输入 `weekly-reviewer` 或每周日执行 | 收集→分析→回顾→规划 | 周回顾报告 |
| `goal-aligner` | 用户输入 `goal-aligner` 或每月执行 | 扫描→分析→检查→报告 | 对齐报告 |

---

## 使用流程

1. **识别触发条件**：分析用户输入或定期任务，确定需要的代理
2. **读取代理文件**：读取 `ai/agents/代理名.md`，了解执行步骤
3. **执行代理**：按照代理文件的步骤执行
4. **生成报告**：按照代理文件的报告模板生成报告

---

## 定期执行时间表

| 代理 | 执行频率 | 执行时间 |
|---|---|---|
| `inbox-processor` | 每日 | 晚上 |
| `weekly-reviewer` | 每周 | 周日晚上 |
| `note-organizer` | 每周 | 周六上午 |
| `goal-aligner` | 每月 | 月初第一天 |
