---
id: tool-05039
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, 协议宽松, 本地优先, 中文友好, 本地写作]
title: humanizer-zh
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/deedeekong07-alt/humanizer-zh
created: 2026-07-18
updated: 2026-07-18
no: 5039
category: 一、去 AI 味 / Humanizer 库
repo: deedeekong07-alt/humanizer-zh
stars: 1
url: https://github.com/deedeekong07-alt/humanizer-zh
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# deedeekong07-alt/humanizer-zh

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/deedeekong07-alt/humanizer-zh
- **Stars**：1
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：去AI味写作助手 — Claude Code Skill for Chinese fiction
- **本地描述**：去AI味写作助手 — Claude Code Skill for Chinese fiction
- **拉取时间**：2026-07-25 18:03:51

---

# 去AI味写作助手 (Humanizer-zh Enhanced for Fiction)

基于 [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)（⭐11.7k）和 [OUBIGFA/De-AI-Prompt-Enhancer](https://github.com/OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL) 的增强版本，专门针对中文小说和创意写作场景优化。

---

## 这是什么

一个 Claude Code Skill，用于检测和消除中文文本中的 AI 生成痕迹。与原始 Humanizer-zh 相比，本版本额外追加了：

- **小说/叙事类文本专用规则**（展示而非告知、对白呼吸感、冲突代价、环境克制）
- **50 分量化评分体系**（改写后自动打分）
- **双模式系统**（good-writing 正向创作 / de-AI-writing 反向消除）

## 快速开始

```bash
# 安装到 Claude Code
npx skills add https://github.com/deedeekong07-alt/humanizer-zh.git

# 或手动克隆
git clone https://github.com/deedeekong07-alt/humanizer-zh.git ~/.claude/skills/humanizer-zh
```

安装后在 Claude Code 中输入 `/humanizer-zh` 或直接说"去AI味"即可触发。

## 核心能力

**24 项 AI 痕迹检测**，覆盖四大维度：

| 维度 | 检测项 |
|------|-----related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 内容模式 | 过度强调意义、宣传语言、肤浅分析、模糊归因、公式化展望、强行上价值 |
| 语言语法 | AI高频词（赋能/抓手/闭环）、高频连接词（此外/与此同时）、排比句式、三段式法则 |
| 风格模式 | 破折号滥用、列表化写作、教科书式段落控制、平均句长 |
| 交流模式 | 机器人式让步、谄媚附和、过度限定、通用积极结论 |

**小说专用规则**：
- 展示而非告知——把"他很愤怒"改成一个动作
- 对白要有呼吸——删掉互相汇报信息的废话
- 冲突必须有代价——不能主角永远秒杀
- 环境描写服务场景——超过100字纯风景即警告
- 情绪不要标签化——删除"震惊""愤怒""五味杂陈"
- 章末钩子要具体——禁用"更大的危机即将到来"

**50 分评分体系**：内容真实性 + 语言自然度 + 风格个性化 + 结构有机性 + 交流温度，≥40 分通过。

## 使用示例

```
用户：这段开头帮我改改，去AI味

AI生成原文：
> 在这座繁华的都市中，陈默每天骑着电动车穿梭于大街小巷，
> 为生计奔波。他深知生活不易，但他始终保持着乐观的心态。
> 然而他不知道的是，命运即将给他开一个巨大的玩笑。

改后：
> 陈默把电动车停在天桥底下，雨正下得最大的时候。
> 保温箱里压着三单没送，麻辣烫超时了四分钟。
> 手机震了——不是催单，是一条群消息，三个字：阿辉没了。
```

## 评分示例

```
【改写前评分：18/50】
内容真实性 2/10 —— 全是概括，没有一个具体细节
语言自然度 4/10 —— "穿梭于""为生计奔波""保持乐观心态"
风格个性化 3/10 —— 无观点、无节奏变化
结构有机性 5/10 —— 模板化叙事
交流温度 4/10 —— 机器在讲故事，不是人在讲

【改写后评分：42/50】
内容真实性 9/10 —— 保温箱、麻辣烫、群消息、三个字
语言自然度 8/10 —— "雨正下得最大的时候"口语化节奏
风格个性化 8/10 —— 短句切入，有压迫感
结构有机性 8/10 —— 从具体场景自然展开
交流温度 9/10 —— 人在讲，有情绪，不解释
```

## 与原始版本的关系

本 Skill 构建于 op7418/Humanizer-zh 的 24 项检测体系之上，追加了 OUBIGFA 的双模式系统和原创的 50 分评分体系 + 小说专用规则。适用于 Claude Code 的 Skill 系统。

## 许可

MIT License
