---
id: tool-09580
type: tool
area: 库
status: active
tags: [Claude Skill, Python, MIT, 英文文档, RAG]
title: book-to-skill
summary: 将技术书/文档/PDF 转为结构化 Claude Skill，按需加载省 24-51 倍 token
source: https://github.com/virgiliojr94/book-to-skill
created: 2026-07-31
updated: 2026-07-31
no: 9580
category: 一、网文 / Claude Skill 生态 写作辅助
repo: virgiliojr94/book-to-skill
stars: 12700
url: https://github.com/virgiliojr94/book-to-skill
tier: "S"
use_case: "将写作方法论书籍/文档批量转为可按需加载的 Skill，解决长文档反复查询的 token 爆炸问题"
pitfalls:
  - "需要 Python 环境和额外依赖（pdftotext/docling 等），非零配置"
  - "章节自动检测需要明确的 Chapter N 标题，纯标题或罗马数字命名的书可能无法自动分段"
  - "每本书转换成本约 $1（API 调用），但一次转换后可反复使用"
related:
  - methods/QUICK_START.md
---

# virgiliojr94/book-to-skill

- **分类**：一、网文 / Claude Skill 生态 写作辅助
- **链接**：https://github.com/virgiliojr94/book-to-skill
- **Stars**：~12,700
- **语言**：Python
- **License**：MIT
- **Topics**：claude-code, skill, book, pdf, epub, agent
- **GitHub 描述**：Turn any technical book, document folder, or collection of sources into a unified agent skill
- **本地描述**：将书籍/文档/PDF 转为结构化 Claude Skill，按需加载章节，省 24-51 倍 token
- **拉取时间**：2026-07-31

---

## 核心价值

将任何技术书、文档文件夹或资料集合转换为一个统一的 Agent Skill，让 AI 能按需加载章节内容回答问题，而非把整本书塞入上下文。

### 写作场景应用

1. **方法论书籍转 Skill**：将《故事》《救猫咪》《编剧的艺术》等写作理论书转为 Skill，写卡文时直接查询对应章节
2. **作家访谈集转 Skill**：将多份作家方法论（如知识库已有的 50 份番茄金番作家方法论）合并为一个 Skill
3. **平台规则转 Skill**：将番茄/起点/晋江的创作指南文档转为 Skill，投稿前快速查询规则
4. **竞品分析转 Skill**：将多本同类小说的拆文笔记合并，写作时按需参考

### 生成产物

| 文件 | 用途 | 大小 |
|---|---|---|
| `SKILL.md` | 核心心智模型 + 章节索引 | ~4,000 tokens |
| `chapters/ch01-*.md` | 每章一个文件，按需加载 | ~1,000 tokens/章 |
| `glossary.md` | 术语表（按字母排序+章节引用） | ~1,500 tokens |
| `patterns.md` | 所有技巧/算法/设计模式 | ~2,000 tokens |
| `cheatsheet.md` | 决策表和快速参考规则 | ~1,000 tokens |

### 支持格式

PDF, EPUB, DOCX, TXT, Markdown, reStructuredText, AsciiDoc, HTML, RTF, MOBI/AZW/AZW3

### 安装与使用

```bash
# 方案 A：作为 Claude Code Skill 安装
git clone https://github.com/virgiliojr94/book-to-skill.git ~/.claude/skills/book-to-skill

# 方案 B：独立 CLI
pip install "book-to-skill[pdf,epub,docx]"
```

```
# 转换单本书
/book-to-skill ~/books/writing-guide.pdf writing-guide

# 合并多个文件为一个 Skill
/book-to-skill ~/papers/paper1.pdf ~/notes/export.txt unified-research

# 转换整个文件夹
/book-to-skill ~/workspace/project-docs/ project-knowledge
```

### Token 节省对比

| 方式 | 回答单个问题的 token 消耗 |
|---|related:
  - methods/QUICK_START.md
---|
| 整本书塞入上下文 | 119K-256K |
| AI 自主导航 PDF | 12K-78K |
| **book-to-skill** | **~5,000** |

**节省倍数：24x-51x**（且整本书塞入上下文的成本每轮对话都会重复产生）
