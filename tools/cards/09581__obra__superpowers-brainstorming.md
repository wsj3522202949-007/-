---
id: tool-09581
type: tool
area: 库
status: active
tags: [Claude Skill, MIT, 英文文档, 大纲规划, 灵感创意]
title: superpowers-brainstorming
summary: 苏格拉底式结构化发想，通过追问将模糊创意打磨为完整设计
source: https://github.com/obra/superpowers/tree/main/skills/brainstorming
created: 2026-07-31
updated: 2026-07-31
no: 9581
category: 一、网文 / Claude Skill 生态 写作辅助
repo: obra/superpowers
stars: 171000
url: https://github.com/obra/superpowers
tier: "S"
use_case: "开新书/卡文时用结构化追问打磨创意，从模糊灵感到可执行大纲"
pitfalls:
  - "原为软件开发设计，需适配写作场景（把'功能需求'替换为'故事设计'）"
  - "Superpowers 整体是开发方法论，brainstorming 是其中一个可独立使用的 skill"
  - "安装整个 Superpowers 插件会加载 14 个 skill，可能污染上下文；建议只提取 brainstorming 的 SKILL.md"
related:
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-31
content_hash: cd789b28464c558c
  - methods/QUICK_START.md
---

# obra/superpowers — brainstorming skill

- **分类**：一、网文 / Claude Skill 生态 写作辅助
- **链接**：https://github.com/obra/superpowers/tree/main/skills/brainstorming
- **Stars**：~171,000（整个 Superpowers 仓库）
- **语言**：Markdown（Skill 文件）
- **License**：MIT
- **Topics**：claude-code, skill, brainstorming, agent, productivity
- **GitHub 描述**：Transform rough ideas into fully-formed designs through structured questioning and alternative exploration
- **本地描述**：苏格拉底式结构化发想 Skill，通过追问将模糊创意打磨为完整设计
- **拉取时间**：2026-07-31

---

## 核心价值

在动手写之前，先通过结构化追问把模糊创意打磨成完整设计。不急于输出，而是逐步厘清：你到底想写什么故事、核心冲突是什么、人物动机是否自洽。

### 写作场景应用

1. **新书发想**：从一句话灵感出发，通过追问逐步建立故事核心（题材/主角/冲突/世界观/爽点线）
2. **卡文诊断**：卡住时不是直接跳过，而是追问"卡在哪里→为什么卡→有什么替代方案"
3. **大纲验证**：写好大纲后用 brainstorming 做一轮压力测试，找出逻辑漏洞和替代走向
4. **人物深化**：对扁平角色做苏格拉底式追问，挖出隐藏动机和弧光可能

### 工作流程

```
1. 你说一个模糊想法（如"想写一个重生造芯片的故事"）
2. AI 不急着写，而是问：
   - 核心冲突是什么？（复仇？技术报国？商业博弈？）
   - 主角的重生带来了什么具体优势？（知识？人脉？时机？）
   - 第一个爽点放在哪里？（第1章？第3章？）
   - 有什么替代设计？（如果重生到大学而不是高中会怎样？）
3. 分段展示设计，每段你确认后再继续
4. 最终保存为设计文档
```

### 安装方式

```bash
# 方式 A：安装整个 Superpowers（含 brainstorming + 13 个其他 skill）
/plugin install superpowers@claude-plugins-official

# 方式 B：只提取 brainstorming skill（推荐，避免上下文污染）
# 将 skills/brainstorming/SKILL.md 复制到 ~/.claude/skills/brainstorming/
```

### Superpowers 技能库全景

| 技能 | 用途 | 写作适用度 |
|---|---|related:
  - methods/QUICK_START.md
---|
| **brainstorming** | 结构化发想 | ★★★ 直接可用 |
| **writing-plans** | 拆解复杂任务为可执行步骤 | ★★★ 直接可用 |
| writing-skills | 创建新 Skill 的元技能 | ★★ 可用于自建写作 Skill |
| executing-plans | 分批执行+检查点 | ★★ 可用于逐章写作 |
| subagent-driven-development | 子 Agent 并行迭代 | ★ 可用于多线并行写作 |
| requesting-code-review | 代码审查 | ★ 可改为"章节互审" |
| systematic-debugging | 系统化调试 | ★ 可改为"卡文诊断" |
| test-driven-development | TDD | — 不适用 |
