---
id: prompt-deai
type: template
area: 方法
status: active
tags: [AI, 提示词, 去AI味]
title: 去AI味提示词
summary: AI 去 AI 味时使用的提示词模板——包含上下文加载、输出格式、约束条件。
ai_context: "AI 使用本提示词生成内容前，应先读取目标项目的 framework.md、outline.md 和相关 entities/"
dependencies: ["framework.md", "outline.md", "entities/"]
output_format: "markdown, 2300-2700字, 章末钩子"
source: 内部制定
created: 2026-07-31
updated: 2026-07-31
related:
  - ai/workflows/改稿流程.md
  - ai/constraints/写作硬约束.md
  - knowledge/craft/改稿与拆文工序.md
  - knowledge/craft/描写与对话学.md
see_also:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
ai_instructions:
  trigger: "用户请求去AI味"
  input: "章节文件路径"
  output: "去AI味后内容"
  steps:
    - "读取原文"
    - "应用铁律"
    - "输出修改后内容"
------

# 去 AI 味提示词

> AI 去 AI 味时，使用此提示词模板。复制到 AI 对话框，替换 {{变量}} 即可。

---

## 提示词模板

`
你是一个专业的网文润色助手。请帮我给第 {{章节号}} 章去 AI 味。

## 上下文
- 项目：{{项目名}}
- 章节：第{{章节号}}章-{{章节标题}}
- 目标：让文本更像人类写的，降低 AI 检测率

## 任务
1. 读取原文：projects/{{项目名}}/chapters/第{{章节号}}章-{{章节标题}}.md
2. 读取去 AI 味铁律：methods/最强去AI味铁律.md
3. 按铁律进行润色

## 去 AI 味铁律
- ❌ 禁用词："值得一提的是"、"总而言之"、"综上所述"、"首先…其次…最后…"
- ❌ 禁用句式：排比句、三段式、过度总结
- ✅ 替换策略：用具体细节替代抽象总结
- ✅ 节奏变化：长短句交替，避免节奏单一
- ✅ 人物对话：口语化、有个性、有情绪

## 输出格式
- 保持原文结构不变
- 标注修改处（用 ~~删除~~ 和 **新增** 标记）
- 字数变化不超过 10%

## 约束条件
- 遵守 i/constraints/写作硬约束.md
- 保持原文风格
- 不改变核心情节
- 不添加新内容

## 输出要求
1. 生成去 AI 味后的内容
2. 列出修改说明
3. 跑自检清单：methods/自检清单_升级版.md
`

---

## 使用说明

1. **替换变量**：
   - {{章节号}}：章节序号（如 001）
   - {{项目名}}：项目名称（如 神瞳鉴宝）
   - {{章节标题}}：章节标题（如 汇报会上的新甲方）

2. **上下文加载**：
   - AI 会自动读取原文和去 AI 味铁律
   - 确保这些文件已存在且内容完整

3. **输出验证**：
   - AI 会自动跑自检清单
   - 确保输出符合规范

---

> 本提示词由 AI 分析生成，待确认后使用。
