---
id: tool-09584
type: tool
area: 库
status: active
tags: [Claude Skill, MIT, 英文文档, 提示词]
title: content-research-writer
summary: 研究+写作一体化 Skill，自动调研、引用、优化钩子、分段反馈
source: https://github.com/ComposioHQ/awesome-claude-skills/tree/main/content-research-writer
created: 2026-07-31
updated: 2026-07-31
no: 9584
category: 一、网文 / Claude Skill 生态 写作辅助
repo: ComposioHQ/awesome-claude-skills
stars: 7000
url: https://github.com/ComposioHQ/awesome-claude-skills
tier: "B"
use_case: "写涉及专业领域知识（科技/历史/法律/医学）的网文时，自动调研+引用+分段优化"
pitfalls:
  - "面向内容营销写作设计，非小说创作；但研究+引用的工作流可迁移"
  - "需要配合 WebSearch/WebFetch 工具使用"
  - "引用质量依赖搜索结果，中文资料覆盖可能不足"
related:
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-31
content_hash: ca4cf825779198ed
  - methods/QUICK_START.md
---

# ComposioHQ/awesome-claude-skills — content-research-writer

- **分类**：一、网文 / Claude Skill 生态 写作辅助
- **链接**：https://github.com/ComposioHQ/awesome-claude-skills/tree/main/content-research-writer
- **Stars**：~7,000（整个 awesome-claude-skills 仓库）
- **语言**：Markdown（Skill 文件）
- **License**：Apache-2.0
- **Topics**：claude, skill, writing, research, content
- **GitHub 描述**：Assists in writing high-quality content by conducting research, adding citations, improving hooks, and providing section-by-section feedback
- **本地描述**：研究+写作一体化 Skill，自动调研、引用、优化钩子、分段反馈
- **拉取时间**：2026-07-31

related:
  - methods/QUICK_START.md
---

## 核心价值

将"调研→写作→优化"整合为一个工作流：先自动搜索相关资料，写作时插入引用，完成后分段给出改进建议。虽然面向内容营销，但研究+引用的工作流可直接迁移到网文写作中的"专业领域验证"环节。

### 写作场景应用

1. **专业知识验证**：写涉及芯片制造/法律诉讼/医学急救等专业场景时，自动搜索验证技术细节
2. **历史背景调研**：写年代文/历史文时，自动调研时代背景（物价/事件/风俗/语言习惯）
3. **平台规则查证**：投稿前自动搜索目标平台最新签约规则和稿费政策
4. **竞品分析写作**：写拆书笔记/书评时，自动搜索补充背景信息并引用

### 工作流程

```
1. 输入写作主题和目标读者
2. AI 自动搜索相关资料，整理为引用列表
3. 按大纲逐段写作，每段标注信息来源
4. 优化钩子：检查每段开头是否吸引人
5. 分段反馈：对每段给出改进建议（准确性/可读性/引用完整性）
```

### 安装

```bash
# 从 awesome-claude-skills 仓库复制 Skill 文件
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cp -r awesome-claude-skills/content-research-writer ~/.claude/skills/
```
