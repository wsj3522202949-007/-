---
id: tool-05597
type: tool
area: 库
status: active
tags: [Claude插件, 协议宽松, 本地优先, 中文友好, 本地写作]
title: design-deai
summary: Claude Code 插件式写作流
source: https://github.com/eruto-skills/design-deai
created: 2026-07-18
updated: 2026-07-18
no: 5597
category: 一、去 AI 味 / Humanizer 库
repo: eruto-skills/design-deai
stars: 0
url: https://github.com/eruto-skills/design-deai
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# eruto-skills/design-deai

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/eruto-skills/design-deai
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Claude Code skill — AI slop detector + DESIGN.md generator
- **本地描述**：Claude Code skill — AI slop detector + DESIGN.md generator
- **拉取时间**：2026-07-25 18:24:35

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# design-deai

> Claude Code skill — AI slop detector + DESIGN.md generator

AIコーディングツール（Claude Code・Cursor・v0・Lovable 等）が生成した UI コードの「AI 臭さ」をソースコード静的解析で診断し、脱スロップ化のための `DESIGN.md` を生成するスキル。

## What it does

1. **スロップパターン検出**: 紫グラデーション・Inter 固定・`rounded-2xl` 乱用・グラスモーフィズム・Empty/Error State 欠如・デザイントークン不在など 9 カテゴリを Grep で検出
2. **スロップスコア算出**: 0〜100 点で重症度を分類
3. **DESIGN.md 生成**: 検出されたアンチパターンを禁止事項として明記し、OKLCH カラーシステム・タイポグラフィ・スペーシング・コンポーネントルールを定義

## Installation

```
/plugin install design-deai@eruto-skills
```

## Usage

```
/design-deai [プロジェクトディレクトリパス]
```

引数省略時はカレントディレクトリを解析します。

## License

MIT
