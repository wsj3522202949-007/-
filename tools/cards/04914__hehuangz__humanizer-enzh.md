---
id: tool-04914
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, 互动叙事, 协议宽松, 本地优先, 中文友好, 本地写作]
title: humanizer-enzh
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/hehuangz/humanizer-enzh
created: 2026-07-18
updated: 2026-07-18
no: 4914
category: 一、去 AI 味 / Humanizer 库
repo: hehuangz/humanizer-enzh
stars: 0
url: https://github.com/hehuangz/humanizer-enzh
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# hehuangz/humanizer-enzh

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/hehuangz/humanizer-enzh
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Claude Code skill: remove AI writing patterns from English and Chinese text
- **本地描述**：Claude Code skill: remove AI writing patterns from English and Chinese text
- **拉取时间**：2026-07-25 17:59:10

---

# humanizer-enzh

A Claude Code skill that removes signs of AI-generated writing from text in both English and Chinese.

一个 Claude Code skill，用于去除英文和中文文本中的 AI 生成痕迹。英文检测基于 Wikipedia 的「[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)」指南（源自 [blader/humanizer](https://github.com/blader/humanizer)）；中文检测基于技术文档和商业写作中常见的 AI 写作模式分析。

English detection is based on Wikipedia's "[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)" guide (via [blader/humanizer](https://github.com/blader/humanizer)). Chinese detection is based on common AI patterns in technical and business writing.

## What it detects and fixes

**English patterns:**
- Inflated symbolism ("testament to", "beacon of", "tapestry of")
- Promotional language ("seamless", "robust", "cutting-edge")
- AI vocabulary (delve, embark, realm, nuanced, foster, leverage...)
- Copula avoidance ("serves as" instead of "is")
- Em dash overuse, rule of three, chatbot artifacts, and more

**Chinese patterns (中文):**
- 连接词滥用 (首先/其次/最后, 综上所述...)
- 强调词堆砌 (值得注意的是, 需要强调的是...)
- 过度正式化 (运行→跑, 完成→搞定)
- 节奏死板 (每段 3-4 行, 每句长度相似)
- 模板化结构, 虚假对比, 空洞修饰

## Installation

### Claude Code

Global install (available in all projects):

```bash
mkdir -p ~/.claude/skills/humanizer-enzh
cp SKILL.md ~/.claude/skills/humanizer-enzh/SKILL.md
```

Project-level install (only available in current project):

```bash
mkdir -p .claude/skills/humanizer-enzh
cp SKILL.md .claude/skills/humanizer-enzh/SKILL.md
```

### OpenCode

Copy `SKILL.md` to your OpenCode skills directory and register it in your configuration.

## Usage

### Default mode (rewrite)

```
/humanizer-enzh "Your text here"
/humanizer-enzh path/to/file.md
```

### Detect-only mode

```
/humanizer-enzh --detect "Your text here"
```

Returns a report of AI patterns found without rewriting.

### With voice sample

```
/humanizer-enzh --voice=path/to/sample.md "Your text here"
```

Matches the writing style from a sample of your own writing.

## Examples

### English

**Before:**
```
First and foremost, it's important to note that implementing this solution
requires a comprehensive understanding of the underlying architecture.
Moreover, one must delve into the nuanced aspects of the system to fully
leverage its robust capabilities.
```

**After:**
```
You'll need to understand how the system works before implementing this.
Dig into the details—especially the parts that aren't obvious.
```

### Chinese

**Before:**
```
首先，我们需要安装依赖。其次，配置环境变量。最后，启动服务。
值得注意的是，端口号需要设置为 8080。通过以上步骤，我们可以
成功部署应用。综上所述，该方案具有良好的可行性。
```

**After:**
```
装好依赖，配一下环境变量，然后跑起来就行。记得端口改成 8080。
这样就能把应用部署上去了。
```

## Comparison with similar projects

| Project | Language | Type | Description |
|---|---|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| [blader/humanizer](https://github.com/blader/humanizer) | English | Claude Code Skill | The original humanizer skill, 13k+ stars. English patterns only |
| [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | 简体中文 | Claude Code Skill | Most popular Chinese version, 6k+ stars. Chinese patterns only |
| [kevintsai1202/Humanizer-zh-TW](https://github.com/kevintsai1202/Humanizer-zh-TW) | 繁體中文 | Claude Code Skill | Traditional Chinese (Taiwan) version |
| [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | English | Claude Code Skill | English audit skill with rewrite |
| [voidborne-d/humanize-chinese](https://github.com/voidborne-d/humanize-chinese) | 中文 | Python Tool | Standalone tool with N-gram perplexity analysis |
| **humanizer-enzh** (this project) | **English + 中文** | **Claude Code Skill** | **Bilingual: auto-detects language and applies language-specific rules** |

Existing projects are split by language — English or Chinese, not both. This project combines both into a single skill with automatic language detection, so you don't need to install separate skills for each language.

## Credits

- English patterns based on [blader/humanizer](https://github.com/blader/humanizer) (MIT License) and [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Chinese patterns based on analysis of AI-generated Chinese content in technical and business contexts

## License

MIT
