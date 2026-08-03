---
id: tool-09583
type: tool
area: 库
status: active
tags: [Claude Skill, Python, MIT, 英文文档, RAG]
title: Skill-Seekers
summary: 将文档网站/GitHub仓库/PDF/视频等转为结构化知识资产，一次预处理导出 21 个 AI 平台
source: https://github.com/yusufkaraaslan/Skill_Seekers
created: 2026-07-31
updated: 2026-07-31
no: 9583
category: 一、网文 / Claude Skill 生态 写作辅助
repo: yusufkaraaslan/Skill_Seekers
stars: 800
url: https://github.com/yusufkaraaslan/Skill_Seekers
tier: "A"
use_case: "将写作参考网站/作者博客/创作指南批量转为可查询的 Skill 或 RAG 知识库"
pitfalls:
  - "部署较重（Python + 可选 Docker + MCP Server），非轻量工具"
  - "主要面向技术文档，文学/创意内容的分块策略可能需要调优"
  - "多语言支持有中文 README，但核心文档为英文"
related:
  - methods/QUICK_START.md
---

# yusufkaraaslan/Skill_Seekers

- **分类**：一、网文 / Claude Skill 生态 写作辅助
- **链接**：https://github.com/yusufkaraaslan/Skill_Seekers
- **Stars**：~800
- **语言**：Python
- **License**：MIT
- **Topics**：claude, skill, rag, documentation, ai, knowledge
- **GitHub 描述**：The data layer for AI systems — turns documentation sites, repos, PDFs, videos into structured knowledge assets
- **本地描述**：将文档网站/仓库/PDF/视频转为结构化知识资产，支持导出到 Claude/Gemini/OpenAI/LangChain 等 21 个平台
- **拉取时间**：2026-07-31

---

## 核心价值

不同于 book-to-skill 专注于"一本书转一个 Skill"，Skill Seekers 是**通用预处理层**：能抓取整个文档网站、GitHub 仓库、PDF 集合、甚至 YouTube 视频，统一转为结构化知识资产，然后一次预处理导出到 21 个 AI 平台。

### 写作场景应用

1. **平台创作指南抓取**：将番茄/起点/晋江官方创作指南网站整体抓取转为 Skill，随时查询规则
2. **作者博客聚合**：将多个网文作者的方法论博客合并为一个知识资产
3. **竞品拆文素材**：将起点/番茄排行榜页面的小说信息批量抓取，用于竞品分析
4. **视频教程转文字**：将 YouTube 上的写作教程视频转为可搜索的文字知识库
5. **多平台导出**：一次抓取，同时导出为 Claude Skill + LangChain RAG + Cursor 规则

### 支持的源类型（18+）

| 源类型 | 示例 |
|---|---|
| 文档网站 | docs.react.dev, 番茄创作者中心 |
| GitHub 仓库 | 任何公开仓库的 wiki/docs |
| PDF | 写作理论书、创作指南 |
| YouTube 视频 | 写作教程频道 |
| Jupyter Notebook | 数据分析笔记 |
| Wiki | Confluence/Notion 公开页面 |
| 本地文件夹 | 已有的写作参考资料集 |

### 导出目标（21 个平台）

| 输出格式 | 目标平台 |
|---|related:
  - methods/QUICK_START.md
---|
| Claude Skill (ZIP+YAML) | Claude Code, Claude API |
| Gemini Skill | Google Gemini |
| OpenAI Custom GPT (ZIP) | GPT-4o, 自定义助手 |
| LangChain Documents | QA 链/Agent/检索器 |
| LlamaIndex TextNodes | 查询引擎/聊天引擎 |
| Pinecone/ChromaDB/FAISS | 向量数据库 |
| Cursor .cursorrules | Cursor IDE |
| Windsurf/Cline/Continue | VS Code 插件 |

### 安装与使用

```bash
# 安装
pip install skill-seekers

# 抓取网站并转为 Claude Skill
skill-seekers create https://docs.example.com/
skill-seekers package output/example --target claude
```
