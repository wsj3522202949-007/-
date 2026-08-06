---
id: tool-04908
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议宽松, 本地优先, 中文友好, 本地写作]
title: realtext-zh
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/sevendataai/realtext-zh
created: 2026-07-18
updated: 2026-07-18
no: 4908
category: 一、去 AI 味 / Humanizer 库
repo: SevenDataAI/realtext-zh
stars: 0
url: https://github.com/sevendataai/realtext-zh
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# SevenDataAI/realtext-zh

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sevendataai/realtext-zh
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：ai-writing, chinese, cli, copywriting, humanizer, productivity, text-cleaner, writing-tools
- **GitHub 描述**：Chinese AI-style text cleaner and humanizer for articles, docs, social posts, resumes and sales copy.
- **本地描述**：Chinese AI-style text cleaner and humanizer for articles, docs, social posts, resumes and sales copy.
- **拉取时间**：2026-07-25 17:58:56

---

# RealText-ZH

把 AI 味很重的中文，改成更像真人写的中文。

这个项目不绑定任何行业。只要你用 AI 写过文章、朋友圈、简历、产品介绍、知识库、销售话术、公众号、小红书、B 站简介、飞书文档，都可能遇到同一个问题：

**内容看起来完整，但不像人写的。**

常见表现：

- 开头就“在当今时代”
- 动不动“赋能”“闭环”“抓手”“落地”
- 一段话里全是正确废话
- 每个标题都像咨询公司 PPT
- 句子很顺，但没有具体场景
- 看起来客观，其实没有观点
- 一眼能看出是 AI 生成

RealText-ZH 做三件事：

1. 扫描 AI 腔和空话。
2. 给出问题位置和原因。
3. 生成更自然、更具体、更像人写的版本。

## Quick Start

```bash
git clone https://github.com/SevenDataAI/realtext-zh.git
cd realtext-zh

python -m realtext_zh.cli examples/ai_style_article.txt
```

输出：

```text
AI-likeness score: 78/100

Issues:
- 使用泛化开头：在当今...
- 出现高频 AI 词：赋能、闭环、落地
- 缺少具体对象：用户、团队、业务都没有被具体化
- 句子过于均匀，缺少自然节奏

Rewrite:
...
```

## What It Detects

| 类型 | 示例 | 问题 |
| --- | --- | --- |
| 泛化开头 | 在当今数字化时代 | 太模板化 |
| 空洞动词 | 赋能、助力、打造、推动 | 没有具体动作 |
| 咨询腔 | 形成闭环、构建体系、打通链路 | 看起来高级，信息量低 |
| 假深度 | 本质上是认知升级 | 没有解释发生了什么 |
| 过度总结 | 综上所述、总而言之 | AI 常见收束 |
| 缺少主体 | 企业应该、团队需要 | 不知道谁、在哪、做什么 |
| 没有场景 | 只讲方法论 | 用户不知道怎么用 |

## Rewrite Principles

RealText-ZH 不追求“更华丽”。

它的改写原则是：

- 少用大词，多用具体动作
- 少讲趋势，多讲场景
- 少讲价值，多讲问题
- 少用排比，多保留自然节奏
- 少做总结，多给判断
- 不替作者编造事实

## Example

AI 味版本：

```text
在当今人工智能快速发展的时代，企业需要通过 AI 工具赋能业务流程，打造高效协同的工作闭环，从而实现降本增效和持续增长。
```

改写后：

```text
很多公司现在不是缺 AI 工具，而是缺一套能稳定执行的流程。

比如客户资料进来以后，谁来判断意图，谁来生成回复，谁来确认能不能发，结果写到哪里，这些步骤如果没有定下来，换再强的模型也只是临时帮你写几句话。
```

## Use Cases

### 内容创作

- 小红书笔记去 AI 味
- 公众号文章重写
- B 站简介优化
- 短视频口播稿润色

### 职场文档

- 飞书文档重排
- 周报改写
- 会议纪要改写
- 方案说明去空话

### 商业转化

- 私信话术优化
- 产品介绍重写
- 知识库试读页优化
- FAQ 改成更像真人回答

### 简历和面试

- 简历项目经历去模板化
- 面试项目表达优化
- 自我介绍改写

## CLI

```bash
python -m realtext_zh.cli input.txt
python -m realtext_zh.cli input.txt --mode strict
python -m realtext_zh.cli input.txt --output output.txt
```

模式：

| mode | 说明 |
| --- | related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
--- |
| light | 轻度清理，只替换明显 AI 腔 |
| standard | 默认模式，清理空话并调整句子 |
| strict | 严格模式，删除废话，补场景提示 |

## Python API

```python
from realtext_zh import analyze_text, rewrite_text

text = "在当今数字化时代，企业需要通过 AI 赋能业务流程。"

report = analyze_text(text)
print(report.score)
print(report.issues)

result = rewrite_text(text, mode="standard")
print(result.rewritten_text)
```

## Rules

规则文件在 [`rules/default_rules.yaml`](https://github.com/SevenDataAI/realtext-zh/blob/main/rules/default_rules.yaml)。

你可以加自己的行业词库，例如：

- 互联网黑话
- 咨询公司话术
- 公文腔
- 知识付费销售腔
- 过度营销词

## What This Is Not

这个项目不是：

- 自动爆款生成器
- AI 检测器
- 学术降重工具
- 洗稿工具
- 绕过平台检测的工具

它的目标很简单：**让中文表达更具体、更自然、更可信。**

## Roadmap

- [x] AI 腔词库
- [x] 空话扫描
- [x] CLI
- [x] 简单改写器
- [ ] Web UI
- [ ] VS Code 插件
- [ ] 浏览器插件
- [ ] 飞书文档清洗脚本
- [ ] 小红书/公众号/简历/周报专用规则包
- [ ] LLM rewrite adapter

## License

MIT

