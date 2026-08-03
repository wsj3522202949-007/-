---
id: tool-09582
type: tool
area: 库
status: active
tags: [Claude Skill, MIT, 英文文档, 大纲规划]
title: superpowers-writing-plans
summary: 将复杂设计拆解为 2-5 分钟粒度的可执行任务清单，每步含精确路径和验证标准
source: https://github.com/obra/superpowers/tree/main/skills/writing-plans
created: 2026-07-31
updated: 2026-07-31
no: 9582
category: 一、网文 / Claude Skill 生态 写作辅助
repo: obra/superpowers
stars: 171000
url: https://github.com/obra/superpowers
tier: "A"
use_case: "将大纲/卷纲拆解为逐章可执行清单，每章含写前准备/核心场景/验证标准"
pitfalls:
  - "原为软件开发设计，'文件路径'需替换为'章节文件'，'测试'需替换为'自检清单'"
  - "粒度偏细（2-5分钟/任务），写作场景建议放大到 30-60分钟/章"
  - "需配合 brainstorming 先完成设计后再使用"
related:
  - methods/QUICK_START.md
---

# obra/superpowers — writing-plans skill

- **分类**：一、网文 / Claude Skill 生态 写作辅助
- **链接**：https://github.com/obra/superpowers/tree/main/skills/writing-plans
- **Stars**：~171,000（整个 Superpowers 仓库）
- **语言**：Markdown（Skill 文件）
- **License**：MIT
- **Topics**：claude-code, skill, planning, agent, productivity
- **GitHub 描述**：Breaks work into bite-sized tasks with exact file paths, complete code, and verification steps
- **本地描述**：将设计拆解为粒度可执行的任务清单，每步含精确路径和验证标准
- **拉取时间**：2026-07-31

related:
  - methods/QUICK_START.md
---

## 核心价值

在设计和执行之间加一层"计划"：把已确认的大纲拆解为每一步都有明确目标、文件路径和验证标准的任务清单。确保 AI（或人类）在逐章写作时不会偏离主线。

### 写作场景应用

1. **卷纲→逐章清单**：将一卷的卷纲拆解为每章的写作任务卡（写前准备/核心场景/爽点位置/章末钩子/自检标准）
2. **改稿排期**：将改稿意见拆解为按优先级排序的修改任务（先改结构硬伤→再改节奏→最后润色）
3. **多线并行**：将多条故事线的写作任务拆解为可并行执行的批次（主线/副线/伏笔埋设各自独立排期）
4. **签约准备**：将投稿前准备拆解为清单（简介/书名/前3章/大纲/平台自查）

### 计划格式示例（适配写作后）

```markdown
## Task 1: 第15章 — 主角第一次被反派算计

**文件**: 正文/第015章_暗流.md
**预计字数**: 2500-2700 字
**写前准备**:
  - 重读第14章末尾，确认场景衔接点
  - 检查伏笔表：第8章埋的"手机"需在本章触发
  - 确认主角当前情绪状态（刚升职→放松警惕）

**核心场景**:
  1. 开场：主角在办公室收到看似好消息（铺垫）
  2. 发展：反派通过第三方传递错误信息（暗线推进）
  3. 转折：主角做出基于错误信息的决策（冲突升级）
  4. 章末钩子：暗示决策后果将在下章爆发

**验证标准**:
  - [ ] 字数 2300-2700
  - [ ] 章末有钩子
  - [ ] 无 AI 味（五感/微表情/口语化/生活碎片/情绪波动）
  - [ ] 伏笔"手机"已触发
  - [ ] 主角行为符合人设
```

### 与 brainstorming 的配合

```
brainstorming（发想→设计文档）
       ↓ 用户确认
writing-plans（设计→任务清单）
       ↓ 用户说"开始"
逐章执行（按清单写，每章完成后打勾）
```
