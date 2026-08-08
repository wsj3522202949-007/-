---
id: tool-05661
type: tool
area: 库
status: active
tags: [去AI味, 协议宽松, 本地优先, 中文友好, 本地写作]
title: fiction-humanizer-zh
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/deedeekong07-alt/fiction-humanizer-zh
created: 2026-07-18
updated: 2026-07-18
no: 5661
category: 一、去 AI 味 / Humanizer 库
repo: deedeekong07-alt/fiction-humanizer-zh
stars: 1
url: https://github.com/deedeekong07-alt/fiction-humanizer-zh
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 6ce22005925daac3
  - methods/改稿润色指令库.md
---

# deedeekong07-alt/fiction-humanizer-zh

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/deedeekong07-alt/fiction-humanizer-zh
- **Stars**：1
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Chinese fiction de-AI writing skill for AI-assisted novel creation
- **本地描述**：Chinese fiction de-AI writing skill for AI-assisted novel creation
- **拉取时间**：2026-07-25 18:26:59

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# fiction-humanizer-zh

`fiction-humanizer-zh` 是一个面向 AI 小说创作流程的中文去 AI 味技能。它用于重写、润色、审阅和续写中文小说章节，重点修复 AI 初稿里常见的剧情梗概感、人物扁平、对白生硬、情绪标签化、冲突无代价、场景无余波和章末钩子空泛。

它适合：

- 中文网文章节精修
- AI 小说初稿去 AI 味
- 短篇小说重写
- 番茄、七猫、起点等平台向章节增强
- 人物弧线、对白、节奏、场景和章末钩子修复
- 小说创作应用中的 AI 写作后处理

## 能力范围

- 保留原主线和设定，修复情节跳步
- 按「铺垫、过程、余波」重写核心情节
- 给人物补目标、阻碍、选择、代价和后续反应
- 把情绪标签改成动作、对白、停顿和环境压力
- 修复对白中的信息汇报感和模型腔
- 强化前 300 字吸引力和章末钩子
- 根据题材区分强情绪网文、升级流、女频情感、悬疑、历史权谋、现实职场和文学短篇

## 安装

发布到 GitHub 后，可通过 skills CLI 安装：

```bash
npx skills add <owner>/fiction-humanizer-zh
```

个人全局安装：

```bash
npx skills add <owner>/fiction-humanizer-zh -g
```

也可以把整个目录复制到 Codex 的个人技能目录：

```bash
~/.codex/skills/fiction-humanizer-zh
```

## 使用示例

```text
请用 $fiction-humanizer-zh 把这一章改得更像真人作者写的，保留主线，补足铺垫、过程、余波和章末钩子。
```

```text
用 $fiction-humanizer-zh 审一下这段 AI 小说为什么有 AI 味，并给我一个精修版。
```

```text
用 $fiction-humanizer-zh 改这个番茄开头，前 300 字要抓人，但不要水文。
```

## 仓库结构

```text
fiction-humanizer-zh/
├── SKILL.md
├── README.md
├── VERSION
├── CHANGELOG.md
├── LICENSE
├── agents/
│   └── openai.yaml
└── references/
    ├── ai-fiction-patterns.md
    ├── scene-rewrite.md
    ├── genre-notes.md
    └── chapter-checklist.md
```

## 许可证

MIT License
