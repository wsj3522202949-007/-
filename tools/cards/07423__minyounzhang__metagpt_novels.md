---
id: tool-07423
type: tool
area: 库
status: active
tags: [大纲规划, Python, 协议宽松, 需API密钥, 中文友好]
title: metagpt_novels
summary: 搭大纲/分卷/节拍
source: https://github.com/minyounzhang/metagpt_novels
created: 2026-07-18
updated: 2026-07-18
no: 7423
category: 画龙补充 / 扩容入库 — 补充源
repo: minyounzhang/metagpt_novels
stars: 1
url: https://github.com/minyounzhang/metagpt_novels
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/QUICK_START.md
---

# minyounzhang/metagpt_novels

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/minyounzhang/metagpt_novels
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Agent for writing Chinese novels
- **本地描述**：metagpt_novels
- **拉取时间**：2026-07-25 19:21:26

related:
  - methods/QUICK_START.md
---

# 📖 AI 小说写作 Agent

一个基于 LLM 的自动小说创作 Agent，支持生成总纲纲、创作人物、生成章节大纲、内容扩写并自动保存。

## 🚀 快速开始

### 1. 克隆&安装
```bash
git clone [repo] 
cd [repo]
pip install -e . 
# requirements.txt里注释了zhipu和火山
```

### 2. 配置 API 密钥
在 config/config2.yaml 中填入LLM API 密钥：
```yaml
llm:
  api_key: "your_api_key_here" 
  # ps:测试时，dpsk和qwen往往需要多对话几轮
```

### 3. demo
```bash
python ./metagpt/test_novel.py
```

![示例图片](imgs/author.jpg)
