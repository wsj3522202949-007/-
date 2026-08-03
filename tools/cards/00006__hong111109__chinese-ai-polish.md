---
id: tool-04799
type: tool
area: 库
status: active
tags: [Claude插件, 协议未明, 需API密钥, 中文友好]
title: chinese-ai-polish
summary: Claude Code 插件式写作流
source: https://github.com/hong111109/chinese-ai-polish
created: 2026-07-18
updated: 2026-07-18
$16
category: 一、去 AI 味 / Humanizer 库
repo: hong111109/chinese-ai-polish
stars: 1
language: null
license: null
url: https://github.com/hong111109/chinese-ai-polish
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# 中文消痕 · AI 文本人性化

> 把 AI 写的中文，改回像人写的。

[![Claude Skill](https://img.shields.io/badge/Claude-Skill-blue)](https://www.anthropic.com/claude)
[![Chinese](https://img.shields.io/badge/Language-Chinese-red)]()

专门处理中文 AI 文本的 Claude Skill，去除"AI 味"，保留人写作的痕迹：犹豫、修正、停顿和自然语感。

---

## 解决什么问题

中文 AI 文本常见的"机器感"：

| 问题 | 表现 |
|------|------|
| **铺垫过多** | 迟迟不进入正题，先摆背景造气氛 |
| **连接词泛滥** | 首先、其次、此外、综上所述堆叠 |
| **翻译腔** | 语法没错，但读起来发卡、发硬 |
| **虚词粘连** | "是……的"、多个"的"连用 |
| **重复闭环** | 同一意思换皮说两三遍 |
| **修饰膨胀** | 非常、极其、高度、显著堆砌 |
| **假文采** | 比喻、类比过长，修辞抢戏 |
| **模板段落** | 每段都太完整、太像标准答案 |
| **强行升华** | 结尾硬拔高、上价值 |
| **信息过满** | 解释太全，没有留白 |

---

## 四大处理场景

根据文本用途，自动匹配改写策略：

| 场景 | 策略 | 特点 |
|------|------|------|
| **chat** | 轻改 + 自然化 | 保留对话感，去套话 |
| **status** | 轻改 + 保真优先 | 保留时间线、责任归属、风险 |
| **docs** | 保守减法式 | 保术语、命令、字段名、步骤 |
| **public-writing** | 按需启用全规则 | 去 AI 味，补节奏和思考痕迹 |

---

## 核心原则（8 条）

1. **先说事，再说态度** — 别铺垫半天才入题
2. **能短就别绕** — 一句说完，不补第二句
3. **能直说就别翻译腔** — 少支架，少名词化
4. **少让虚词拖句子** — 警惕"是、的、地、得"过密
5. **别把话说太满** — 信任读者，保留留白
6. **优先提高信息密度** — 删无增量内容
7. **保留人写作的痕迹** — 允许犹豫、修正、停顿
8. **先判场景，再判力度** — 不一刀切

---

## 14 条专项规则

1. 反铺垫：开门见山，不先搭台
2. 反连接词、填充词泛滥
3. 反翻译腔 / 欧化表达
4. 反虚词粘连（少"是"少"的地得"）
5. 反重复闭环
6. 反修饰词膨胀
7. 反假文采（比喻必须有信息增益）
8. 反模板段落
9. 反结尾升华
10. 反信息说满（留白）
11. 补中文语感（轻度口语化）
12. 补节奏（句长、停顿、标点）
13. 补思考痕迹（犹豫、不确定性）
14. 反结构模板（二元对比、价值拔高骨架）

---

## 执行流程

```
1. 判场景 → chat / status / docs / public-writing
2. 查禁改项 → 术语、命令、时间线、责任归属
3. 判问题强度 → Tier 1/2/3
4. 定改写力度 → 轻改 / 中改 / 重改
5. 执行规则 → 按 Top 14 处理
6. 回读检查 → 保真回读 + 残留味回读
7. 输出 → 单一推荐版本
```

---

## 输出模式

- **默认模式**：直接给改写后的单一版本
- **Annotation Mode**：只标注问题，不改写（用户明确要求时）

---

## 文件结构

```
.
├── SKILL.md                    # 主技能文件（14 条规则 + 执行流程）
├── references/
│   ├── chinese-rules-examples.md   # 中文前后对照例子
│   ├── scene-guardrails-zh.md      # 场景禁改表
│   ├── protected-spans-zh.md       # 保护项清单
│   ├── positive-style-zh.md        # 正向风格合同
│   ├── operation-manual-zh.md      # 微操作手册
│   ├── boundary-cases-zh.md        # 误杀边界案例
│   └── structures-zh.md            # 结构反模式
├── evals/
│   ├── benchmark.md              # 评测集
│   └── run-eval.md               # 评测方法
├── .gitignore
└── README.md
```

---

## 使用示例

**输入**：
```
在当今快速发展的市场环境中，企业需要更加高效地推进协作，
进行全面的流程优化。值得注意的是，这一举措不仅能显著提升工作效率，
更是为后续发展奠定了坚实基础。
```

**输出**：
```
市场变化快，协作流程得跟着提速。先把流程理顺，效率自然会上去。
```

---

## 适用场景

- ✓ 改写 AI 生成的中文文案
- ✓ 润色过于"书面"的文本
- ✓ 去除客服腔、协作残留
- ✓ 把文档改成口语化表达
- ✓ 诊断文本"AI 味"来源

**不适用**：
- ✗ 需要严格保留术语的技术文档（需人工核对）
- ✗ 法律、医学等高风险专业文本

---

## 更新日志

- **2026-04-21** — 初始版本，14 条专项规则 + 场景矩阵

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 关于

这是一个 [Claude Code](https://claude.ai/code) 的 Skill。

> **注意**：本 Skill 优先保真，不确定时会选择保守处理。涉及关键信息（命令、字段名、时间线、责任归属）时请人工复核。
