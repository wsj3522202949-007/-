---
id: tool-05204
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 需API密钥, 中文友好, 去AI味]
title: ai-slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/liuxiaobai8868/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5204
category: 一、去 AI 味 / Humanizer 库
repo: liuxiaobai8868/ai-slop-detector
stars: 4
url: https://github.com/liuxiaobai8868/ai-slop-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 805b32ca8ac14183
  - methods/改稿润色指令库.md
---

# liuxiaobai8868/ai-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/liuxiaobai8868/ai-slop-detector
- **Stars**：4
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：多语言 AI 味检测与去 AI 化工具集 · Multilingual AI-slop detector & de-slopping toolkit (zh/en/es/ar/hi)
- **本地描述**：多语言 AI 味检测与去 AI 化工具集 · Multilingual AI-slop detector & de-slopping toolkit (zh/en/es/ar/hi)
- **拉取时间**：2026-07-25 18:09:57

---

# AI Slop Detector

> 多语言「AI 味」检测与去 AI 化工具集 · Multilingual AI-slop detector & de-slopping toolkit

检测文本里的 AI 写作痕迹（套话、滥用词、结构反模式），给出量化评分，并可调用 Claude API 自动重写润色。支持**中文、英文、西班牙语、阿拉伯语、印地语** 5 个语言区。

A zero-dependency toolkit to **detect** telltale signs of AI-generated writing (cliché phrases, overused words, structural anti-patterns), **score** them, and optionally **rewrite** the text via the Claude API to sound human. Supports Chinese, English, Spanish, Arabic, and Hindi.

---

## 为什么需要它 · Why

大模型写出来的文字有指纹：爱用「值得注意的是」「在当今时代」、排比三连、每段都升华、形容词堆砌。这些「AI 味」会被平台检测、被读者反感。本工具把这些模式做成可检索的词表 + 结构规则，扫一遍就知道一段文字有多「AI」，并能自动改写。

LLM output has a fingerprint: hedge phrases, rule-of-three parallelism, relentless summarizing, adjective stacking. This tool turns those patterns into searchable word lists + structural heuristics, scores any text, and can rewrite it.

## 安装 · Install

无需任何 npm 依赖，只要 **Node.js 18+**（用到内置 `fetch`）。

```bash
git clone https://github.com/liuxiaobai8868/ai-slop-detector.git
cd ai-slop-detector
node scan.js examples/sample-zh.md
```

## 三个工具 · The three tools

| 脚本 | 作用 | 需要 API |
|------|------|:related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---:|
| `scan.js` | 扫描文本，统计禁词 + 结构反模式，输出评分 | ❌ |
| `deai.js` | 调用 Claude 深度重写整篇，去 AI 化后自动复扫 | ✅ |
| `mix-rewrite.js` | 调用 Claude 做轻量「混改」，保留原意微调语感 | ✅ |

### 1. 扫描评分 `scan.js`（离线，零成本）

```bash
node scan.js <文件路径> [语言]
# 语言: zh(默认) | en | es | ar | hi，不指定则自动检测

node scan.js draft.md          # 自动检测语言
node scan.js draft.md en       # 强制按英文规则
```

输出：命中的 AI 套话清单 + 出现次数、结构反模式（如三连排比、千篇一律的段落收尾）、以及一个总评分。分数越高说明 AI 味越重，建议过一遍 `deai.js`。

### 2. 深度去 AI 化 `deai.js`（调 Claude）

按段切分整篇文本，逐段发给 Claude 重写，改完自动用 `scan.js` 复扫对比。

```bash
export ANTHROPIC_API_KEY=sk-ant-...        # 直连官方
node deai.js input.md output.md
```

中转 / 代理也支持：

```bash
export CLAUDE_API_KEY=your-key
export CLAUDE_API_BASE=https://your-proxy.example.com   # 可选，默认 api.anthropic.com
export CLAUDE_MODEL=claude-sonnet-4-20250514            # 可选
export PROXY_URL=http://127.0.0.1:7890                  # 可选，走本地代理
node deai.js input.md output.md
```

### 3. 轻量混改 `mix-rewrite.js`（调 Claude）

比 `deai.js` 更克制，适合已经不错、只想微调语感的稿子。环境变量同上。

```bash
node mix-rewrite.js input.md output.md
```

## 词表与 Prompt · Lists & prompts

- `*-slop-list.json` — 5 语种的 AI 套话/滥用词词表，**可直接编辑增删**，调教成你自己的标准。
- `*-deai-prompt.md` — 各语种的去 AI 化改写指令模板，给 `deai.js` 用，也可单独拿去喂任何 LLM。

想加一门新语言：复制一份 `*-slop-list.json` 填词，在 `scan.js` 的 `LANG_FILES` 里登记即可。

## 典型工作流 · Workflow

```bash
node scan.js draft.md              # 1. 先扫，看 AI 味多重
node deai.js draft.md clean.md     # 2. 高了就去 AI 化
node scan.js clean.md              # 3. 复扫确认（deai.js 已自动做一次）
```

## 注意 · Notes

- `scan.js` 完全离线、零成本，随便跑。
- `deai.js` / `mix-rewrite.js` 会消耗 Claude API 额度，按文本长度分段计费。
- 词表是主观的，第一次用建议先按自己的口味改 `*-slop-list.json`。
- `examples/sample-zh.md` 是一篇公版民间故事，仅作演示输入。

## License

MIT — 自由使用、修改、分发。
