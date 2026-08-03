---
id: tool-01309
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: paper-copilot
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/youxuels/paper-copilot
created: 2026-07-18
updated: 2026-07-18
no: 1309
category: 二、网文 / 长篇 AI 写作系统 库
repo: youxuels/paper-copilot
stars: 0
url: https://github.com/youxuels/paper-copilot
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# youxuels/paper-copilot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/youxuels/paper-copilot
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Paper Copilot - AI驱动的交互式学术论文构建技能 | Interactive academic paper writing guide based on 9-module research integrity framework
- **本地描述**：Paper Copilot - AI驱动的交互式学术论文构建技能 （ Interactive academic paper writing guide based on 9-module research integrity framework
- **拉取时间**：2026-07-23 23:17:17

---

# Paper Copilot 🤖

**AI驱动的交互式学术论文构建技能**

基于学术论文九大模块研究完整性自评框架，通过"意图驱动+三选一"的交互方式，一步一步引导写作者构建论文。

## 核心理念

论文写作不是填模板，而是做决策。每一个写作环节都存在多种策略选择，而选择应该由写作者——而非AI——来做。

## 工作流程

| 步骤 | 模块 | 三个备选策略 |
|------|------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| 第0步 | 研究定位 | 自由描述研究领域、问题、阶段 |
| 第1步 | 摘要 | 问题驱动 / 缺口驱动 / 发现驱动 |
| 第2步 | 引言 | 数据冲击 / 事件叙事 / 悖论提问 |
| 第3步 | 文献综述 | 理论-方法-实证 / 主题递进 / 对比论证 |
| 第4步 | 理论框架 | 经典理论映射 / 多理论整合 / 机制推演 |
| 第5步 | 研究设计 | 实验设计详述 / 数据论证 / 方法-数据双线 |
| 第6步 | 计量模型 | 基准→放松假设 / 基准→异质性 / 基准→因果识别 |
| 第7步 | 结果分析 | 假设逐条验证 / 模型递进对比 / 核心发现优先 |
| 第8步 | 讨论 | 机制深挖 / 文献对话 / 局限前瞻 |
| 第9步 | 结论 | 政策建议导向 / 学术贡献提炼 / 未来研究路线图 |

## 文件说明

- `.trae/skills/paper-copilot/SKILL.md` — Skill定义文件，包含完整的交互流程、执行规范和协作说明
- `wechat-article-PaperCopilot-2026-05-24.docx` — 微信公众号文章，介绍Paper Copilot技能及AI辅助经济学实证研究的未来讨论

## 使用方式

1. 将 `.trae/skills/paper-copilot/` 目录复制到你的 Trae IDE 项目的 `.trae/skills/` 下
2. 在对话中输入"帮我写论文"或"我要写一篇关于XX的论文"
3. Paper Copilot 自动激活，引导你逐步构建论文

## 设计特点

- **意图驱动**：每步先解释"为什么要这样写"，再给选项
- **三选一决策**：每个决策点3个差异化策略，覆盖不同研究情境
- **前后连贯**：后续步骤引用前序选择，确保论文逻辑链不断裂
- **自检清单**：每步生成内容后附带自检项，对标26个核心问题
- **协作扩展**：可与 stata-analysis、chinese-econ-rewrite、academic-intro-checker 等skill无缝衔接

## 许可

MIT License
