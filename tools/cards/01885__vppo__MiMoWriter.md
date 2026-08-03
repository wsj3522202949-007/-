---
id: tool-01885
type: tool
area: 库
status: active
tags: [RAG, 多Agent, 大纲规划, TTS, Python, 协议未明, 本地优先, 中文友好, 人物设定, 本地写作]
title: MiMoWriter
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/vppo/mimowriter
created: 2026-07-18
updated: 2026-07-18
no: 1885
category: 二、网文 / 长篇 AI 写作系统 库
repo: vppo/MiMoWriter
stars: 0
url: https://github.com/vppo/mimowriter
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# vppo/MiMoWriter

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/vppo/mimowriter
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-assisted Chinese web novel writing tool built on Xiaomi MiMo-V2.5. Multi-agent pipeline: outline → character → writing → review with auto-fix.
- **本地描述**：AI-assisted Chinese web novel writing tool built on Xiaomi MiMo-V2.5. Multi-agent pipeline: outline → character → writing → review with auto-fix.
- **拉取时间**：2026-07-23 23:33:56

---

# MiMoWriter

> 基于 Xiaomi MiMo-V2.5-Pro 的网文创作 Agent 工具

## 项目简介

MiMoWriter 是一个专为中文网络小说创作者设计的 AI 辅助写作工具，基于小米 MiMo 大模型构建。

核心理念：**不是让 AI 替你写，而是让 AI 帮你从大纲到成稿全流程加速。**

## 架构概览

```
┌─────────────────────────────────────────────────┐
│                  MiMoWriter                      │
├──────────┬──────────┬──────────┬────────────────┤
│  Agent   │ Pipeline │   API    │   Frontend     │
│  Layer   │  Engine  │  Server  │   Editor       │
├──────────┴──────────┴──────────┴────────────────┤
│              MiMo API / Local Model              │
├─────────────────────────────────────────────────┤
│          RAG Store + Trend Analyzer              │
└─────────────────────────────────────────────────┘
```

### Agent 流水线

```
用户输入题材/设定
      │
      ▼
 ┌─────────┐    ┌──────────┐    ┌──────────┐
 │ 世界观   │───▶│ 人物设定  │───▶│ 大纲生成  │
 │ Generator │    │ Designer │    │ Planner  │
 └─────────┘    └──────────┘    └──────────┘
                                     │
      ┌──────────────────────────────┘
      ▼
 ┌──────────┐    ┌──────────┐    ┌──────────┐
 │ 章节拆分  │───▶│ 逐章撰写  │───▶│ 风格审查  │
 │ Splitter  │    │  Writer   │    │ Reviewer │
 └──────────┘    └──────────┘    └──────────┘
                                     │
                                     ▼
                              用户审阅 & 编辑
```

## 技术栈

| 层级 | 技术选型 |
|------|------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| **AI 模型** | MiMo-V2.5-Pro (长文生成) / MiMo-V2.5 (快速交互) / MiMo-V2.5-TTS (语音试读) |
| **后端** | Python 3.12+ / FastAPI |
| **Agent 框架** | 自研 Pipeline + Function Calling |
| **向量数据库** | ChromaDB (本地) / Qdrant (生产) |
| **前端** | React 18 + Tiptap Editor + TailwindCSS |
| **数据采集** | Scrapy + Playwright |
| **部署** | Docker / 阿里云 |

## 核心功能

### 已完成
- [x] 项目架构设计
- [x] MiMo API 对接层
- [x] Agent Pipeline 基础框架

### 开发中
- [ ] 大纲生成模块 (基于 MiMo-V2.5-Pro)
- [ ] 人物设定生成器
- [ ] 章节自动拆分
- [ ] RAG 风格迁移系统

### 计划中
- [ ] 前端编辑器
- [ ] 排行榜数据分析看板
- [ ] TTS 语音试读功能
- [ ] 多用户协作

## 快速开始

```bash
# 克隆项目
git clone https://github.com/yourname/MiMoWriter.git
cd MiMoWriter

# 安装依赖
pip install -e .

# 配置环境变量
cp .env.example .env
# 编辑 .env 填入你的 MiMo API Key

# 启动 API 服务
python -m src.api.server

# 启动前端 (开发模式)
cd src/frontend && npm run dev
```

## 使用示例

```python
from src.pipeline.novel_pipeline import NovelPipeline

pipeline = NovelPipeline(model="mimo-v2.5-pro")

# 从一句话生成完整大纲
outline = pipeline.generate_outline(
    genre="诡异游戏",
    premise="主角意外进入一个诡异游戏副本，需要完成各种任务才能存活",
    target_chapters=30,
    style="番茄小说热门风格"
)

# 生成人物设定
characters = pipeline.design_characters(
    outline=outline,
    protagonist={"type": "成长型男主", "traits": ["冷静", "善于观察"]},
    count=5
)

# 逐章生成
for chapter in outline.chapters:
    text = pipeline.write_chapter(
        chapter=chapter,
        characters=characters,
        context=outline,
        word_count=3000
    )
    # 自动风格审查
    review = pipeline.review_chapter(text, style_guide=outline.style)
    print(f"第{chapter.number}章: {review.score}/100")
```

## 为什么选择 MiMo

1. **1M 上下文窗口** — 整本书的上下文都能装进去，前后文一致性极强
2. **Agent 能力** — 支持多步骤工具调用，完美匹配创作流水线
3. **中文优化** — 对中文网文的理解和生成质量优于同级别模型
4. **Token 效率高** — ClawEval 同分下比竞品省 40-50% Token
5. **MIT 开源** — 可以本地部署和二次微调

## 贡献

欢迎提交 Issue 和 PR！

## License

MIT
