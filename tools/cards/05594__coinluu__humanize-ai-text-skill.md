---
id: tool-05594
type: tool
area: 库
status: active
tags: [去AI味, 协议宽松, 本地优先, 中文友好, 本地写作]
title: humanize-ai-text-skill
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/coinluu/humanize-ai-text-skill
created: 2026-07-18
updated: 2026-07-18
no: 5594
category: 一、去 AI 味 / Humanizer 库
repo: coinluu/humanize-ai-text-skill
stars: 0
url: https://github.com/coinluu/humanize-ai-text-skill
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# coinluu/humanize-ai-text-skill

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/coinluu/humanize-ai-text-skill
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：agent-skill, agents, ai, ai-writing, chinese, content-editing, copywriting, humanize-ai, llm, prompt-engineering, text-rewrite, wechat, xiaohongshu
- **GitHub 描述**：Agent-ready skill for humanizing AI-generated Chinese text with platform adaptation, protected facts, and safety checks.
- **本地描述**：Agent-ready skill for humanizing AI-generated Chinese text with platform adaptation, protected facts, and safety checks.
- **拉取时间**：2026-07-25 18:24:29

---

# Humanize AI Text Skill｜AI 初稿真人化编辑 Skill

> 一个 Agent 可调用的中文文本真人化编辑 Skill。  
> 用于把 AI 生成的文章、文案、口播稿、小红书笔记、公众号文章、朋友圈内容、销售文案、商务文档等，改写成更自然、更像真人表达、更符合平台场景的版本。

[English Version](https://github.com/coinluu/humanize-ai-text-skill/blob/main/README_EN.md)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status: v1.0.0](https://img.shields.io/badge/Status-v1.0.0-blue.svg)
![Agent Ready](https://img.shields.io/badge/Agent-Ready-purple.svg)
![Language: Chinese](https://img.shields.io/badge/Language-Chinese-red.svg)
![No Database Required](https://img.shields.io/badge/No%20Database-Required-lightgrey.svg)

## 这个 Skill 解决什么问题？

很多 AI 初稿并不是不能用，而是读起来有明显的“机器感”：

- 开头宏大空泛
- 结构模板化
- 语气过度中立
- 抽象词过多
- 缺少场景和判断
- 像报告，不像真人表达

`humanize-ai-text-skill` 的目标不是把文本改得更夸张，而是帮助 Agent 在保留事实和原意的前提下，把中文内容改得更自然、更清楚、更适合发布。

## Before / After

### Before

```text
在当今 AI 快速发展的时代，越来越多企业开始关注 AI 工作流。AI 工作流不仅能够帮助企业提升效率，而且能够优化业务流程，推动企业实现智能化升级。因此，企业应该积极拥抱 AI 工作流，以便在未来竞争中获得更大的发展空间。
```

### After

```text
企业开始关注 AI 工作流，通常不是因为它听起来新，而是因为很多重复工作确实需要被重新处理。

比如信息整理、内容初稿、客户问题归类、内部流程提醒，这些环节如果一直靠人工来回确认，很容易耗时间。AI 工作流的价值，是把这些固定动作先串起来，让人把精力放到判断、沟通和决策上。

所以它不是一个简单的“智能化升级”口号，更像是一种重新整理工作方式的工具。用得好，效率会更稳；用不好，也只是多了一套复杂流程。
```

## 快速开始

```text
请调用 humanize-ai-text-skill，把下面这段 AI 文本改得更自然，更像真人表达，适合小红书发布。

【原文】
AI 工作流可以帮助个人和团队提升效率，优化重复性工作流程，并更好地管理日常任务。
```

更多调用模板见：[examples/usage_examples.md](https://github.com/coinluu/humanize-ai-text-skill/blob/main/examples/usage_examples.md) 和 [docs/usage.md](https://github.com/coinluu/humanize-ai-text-skill/blob/main/docs/usage.md)。

## 核心能力

| 能力 | 说明 |
| --- | --- |
| AI 感诊断 | 找出宏大开头、模板结构、抽象词、机械连接词等问题 |
| 真人化改写 | 在保留原意的前提下，让文本更自然、更有节奏 |
| 平台适配 | 适配小红书、抖音口播、公众号、朋友圈、商务文档等 |
| 内容类型识别 | 自动识别文章、笔记、口播、标题、邮件、简历等类型 |
| Protected Facts 保真 | 保护数字、日期、名称、价格、合同条款和关键结论 |
| 参考样本风格提炼 | 只提炼结构、节奏、语气和表达方式等通用规律 |
| 高风险内容安全检查 | 医疗、法律、金融、教育、求职等内容降低改写强度 |
| 防过度真人化 | 避免口水化、油腻化、低质营销号化 |
| 多种输出模式 | 支持 `concise`、`standard`、`full`、`debug` |

## 三种调用模式

| 模式 | 用途 |
| --- | --- |
| `basic_humanize` | 普通去 AI 味，让通用文本更自然 |
| `platform_humanize` | 按平台改写，如小红书、抖音口播、公众号、商务文档 |
| `sample_guided_humanize` | 参考样本风格引导改写，只提炼通用表达规律 |

## 支持平台

| 平台/场景 | 改写目标 |
| --- | --- |
| 小红书 | 短段落、真实感、低官方感、不虚构体验 |
| 抖音口播 | 前三秒有钩子、短句、适合朗读 |
| 公众号 | 观点明确、逻辑清晰、有解释力 |
| 知乎 | 判断清楚、推理完整、保留边界 |
| 朋友圈 | 像真人分享，低营销感，不像广告 |
| 私域社群 | 清楚、友好、有行动指向，不过度催促 |
| 销售文案 | 增强信任，说明适合谁/不适合谁，不夸大效果 |
| 商务文档 | 自然但专业，克制、清楚、准确 |
| 通用文本 | 不指定平台时，默认做自然化编辑 |

## 支持文本类型

| 类型 | 说明 |
| --- | related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
--- |
| `article` | 文章、长文、公众号稿 |
| `social_note` | 小红书笔记、社交平台内容 |
| `short_video_script` | 抖音口播、短视频脚本、直播话术 |
| `sales_copy` | 销售文案、产品介绍、服务介绍 |
| `title` | 标题、主题行、视频标题 |
| `caption` | 图片/视频配文 |
| `comment_reply` | 评论回复、评价回复、异议回应 |
| `private_message` | 私信、私域消息、跟进话术 |
| `email` | 邮件、商务沟通 |
| `resume` | 简历、项目经历、求职材料 |
| `business_doc` | 商务报告、方案、纪要、SOP |
| `knowledge_explanation` | 知识解释、教程、科普 |
| `generic_text` | 通用文本 |

## 工作流

```text
输入文本
  ↓
解析输入
  ↓
识别内容类型
  ↓
抽取 Protected Facts
  ↓
AI 感诊断
  ↓
选择改写强度
  ↓
平台适配
  ↓
真人化改写
  ↓
事实一致性检查
  ↓
输出结果
```

完整流程说明见：[docs/integration.md](https://github.com/coinluu/humanize-ai-text-skill/blob/main/docs/integration.md)。

## 输出示例

默认 `standard` 模式会输出：

```markdown
## AI 感诊断

- 开头偏宏大，缺少具体问题。
- “不仅……而且……”结构模板化。
- “提升效率”“智能化升级”偏抽象。

## 改写策略

- 从具体工作场景切入。
- 保留原意，但减少口号化表达。
- 用长短句混合增强自然节奏。

## 真人化改写版

企业开始关注 AI 工作流，通常不是因为它听起来新，而是因为很多重复工作确实需要被重新处理。

## 修改说明

- 删除宏大背景开头。
- 将抽象表达改成更具体的工作动作。
- 保留 AI 工作流、效率和流程优化的核心意思。

## 风险提示

未发现需要特别提示的风险。
```

更多输出模式见：[docs/output_modes.md](https://github.com/coinluu/humanize-ai-text-skill/blob/main/docs/output_modes.md)。

## 参考样本模式

用户可以提供 1-3 篇参考样本。

Skill 只提炼通用表达规律，例如：

- 结构
- 节奏
- 语气
- 句式倾向
- 观点表达方式
- 内容组织方式

参考样本中的以下内容不作为可迁移素材：

- 具体故事
- 个人经历
- 案例
- 独特比喻
- 原句
- 标题
- 强识别性表达

最终改写必须基于用户原文重新组织表达，而不是复用样本具体内容。详见：[docs/reference_sample_mode.md](https://github.com/coinluu/humanize-ai-text-skill/blob/main/docs/reference_sample_mode.md)。

## 安全边界

- 不虚构事实、数据、案例、个人经历
- 不伪造权威背书
- 保留数字、日期、名称、价格、关键结论
- 高风险行业降低改写强度
- 避免过度口水化、油腻化、营销号化

更多安全说明见：[docs/safety.md](https://github.com/coinluu/humanize-ai-text-skill/blob/main/docs/safety.md) 和 [SECURITY.md](https://github.com/coinluu/humanize-ai-text-skill/blob/main/SECURITY.md)。

## 项目结构

```text
humanize-ai-text-skill/
├── README.md
├── README_EN.md
├── skill.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── prompts/
│   ├── main.md
│   ├── input_parser.md
│   ├── content_type_router.md
│   ├── protected_facts_extractor.md
│   ├── ai_tone_diagnosis.md
│   ├── rewrite_intensity_controller.md
│   ├── platform_adaptation.md
│   ├── sample_style_analysis.md
│   ├── sample_style_extraction.md
│   ├── rewrite_engine.md
│   ├── safety_check.md
│   ├── factual_consistency_check.md
│   ├── output_mode_selector.md
│   └── output_format.md
├── rules/
│   ├── ai_phrase_blacklist.md
│   ├── ai_structure_blacklist.md
│   ├── human_style_rules.md
│   ├── anti_overhumanize_rules.md
│   ├── platform_rules.md
│   ├── content_type_rules.md
│   ├── industry_safety_rules.md
│   ├── no_fabrication_rules.md
│   ├── protected_facts_rules.md
│   └── sample_style_rules.md
├── docs/
├── examples/
├── tests/
├── assets/
├── marketing/
└── .github/
```

## 示例

- [普通去 AI 味](https://github.com/coinluu/humanize-ai-text-skill/blob/main/examples/basic_humanize_example.md)
- [小红书改写](https://github.com/coinluu/humanize-ai-text-skill/blob/main/examples/xiaohongshu_example.md)
- [抖音口播](https://github.com/coinluu/humanize-ai-text-skill/blob/main/examples/douyin_script_example.md)
- [公众号文章](https://github.com/coinluu/humanize-ai-text-skill/blob/main/examples/wechat_article_example.md)
- [朋友圈内容](https://github.com/coinluu/humanize-ai-text-skill/blob/main/examples/moments_example.md)
- [销售文案](https://github.com/coinluu/humanize-ai-text-skill/blob/main/examples/sales_copy_example.md)
- [商务文档](https://github.com/coinluu/humanize-ai-text-skill/blob/main/examples/business_doc_example.md)
- [参考样本风格](https://github.com/coinluu/humanize-ai-text-skill/blob/main/examples/sample_guided_example.md)
- [Protected Facts 保真](https://github.com/coinluu/humanize-ai-text-skill/blob/main/examples/protected_facts_example.md)
- [防过度真人化](https://github.com/coinluu/humanize-ai-text-skill/blob/main/examples/anti_overhumanize_example.md)
- [调用模板合集](https://github.com/coinluu/humanize-ai-text-skill/blob/main/examples/usage_examples.md)

## 测试

`tests/` 覆盖：

- [基础改写](https://github.com/coinluu/humanize-ai-text-skill/blob/main/tests/basic_test.md)
- [平台适配](https://github.com/coinluu/humanize-ai-text-skill/blob/main/tests/platform_test.md)
- [内容类型识别](https://github.com/coinluu/humanize-ai-text-skill/blob/main/tests/content_type_test.md)
- [参考样本引导](https://github.com/coinluu/humanize-ai-text-skill/blob/main/tests/sample_guided_test.md)
- [安全检查](https://github.com/coinluu/humanize-ai-text-skill/blob/main/tests/safety_test.md)
- [Protected Facts 保真](https://github.com/coinluu/humanize-ai-text-skill/blob/main/tests/protected_facts_test.md)
- [禁止虚构](https://github.com/coinluu/humanize-ai-text-skill/blob/main/tests/no_fabrication_test.md)
- [防过度真人化](https://github.com/coinluu/humanize-ai-text-skill/blob/main/tests/anti_overhumanize_test.md)

## Roadmap｜路线图

- 更多平台风格规则
- 更多行业安全规则
- 英文支持
- 更多 Before/After 示例
- 评测 benchmark
- Agent 集成示例

详见：[docs/roadmap.md](https://github.com/coinluu/humanize-ai-text-skill/blob/main/docs/roadmap.md)。

## Contributing｜贡献

欢迎提交平台规则、内容类型规则、before/after 示例和测试样本。请先阅读 [CONTRIBUTING.md](https://github.com/coinluu/humanize-ai-text-skill/blob/main/CONTRIBUTING.md)。

## License｜许可证

MIT License. See [LICENSE](https://github.com/coinluu/humanize-ai-text-skill/blob/main/LICENSE).

## Citation｜引用

如果你在 Agent 工作流中使用本 Skill，欢迎引用：

```text
Humanize AI Text Skill：一个 Agent 可调用的中文 AI 初稿真人化编辑 Skill，用于把 AI 生成文本改写成更自然、更符合平台场景的版本。
```
