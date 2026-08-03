---
id: tool-01056
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: novel-toolbox
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/gaozhi-ui/novel-toolbox
created: 2026-07-18
updated: 2026-07-18
no: 1056
category: 二、网文 / 长篇 AI 写作系统 库
repo: GaoZhi-ui/novel-toolbox
stars: 0
url: https://github.com/gaozhi-ui/novel-toolbox
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# GaoZhi-ui/novel-toolbox

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/gaozhi-ui/novel-toolbox
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Novel writing automation toolkit - chapter anchor compiler + delivery pipeline
- **本地描述**：Novel writing automation toolkit - chapter anchor compiler + delivery pipeline
- **拉取时间**：2026-07-23 23:09:48

---

# novel-toolbox 📚

> **小说写作自动化工具箱** — 两个工具链，管你小说的后半程

[![AI-Generated](https://img.shields.io/badge/%F0%9F%A4%96-AI%20Generated-blue)](https://github.com/xiaohong-ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)

---

长篇小说写到几十章以后，管理成本爆炸：
- 时间线搞混：谁在第几天干了什么
- 伏笔遗忘：埋了什么、什么时候回收
- 角色跑偏：OOC 了都没发现
- 交付繁琐：合并、转 docx、发邮件、同步备份

这两个工具把后半程自动化了。

## 工具一：toolbox_compile — 锚点→知识库编译器

每章写完后，从「章节锚点」文件自动提取结构化信息，编译到三个管理文件：

```
第22章_锚点.md  ---→  故事时间线.md  (时间线)
        |----→  伏笔追踪表.md  (伏笔管理)
        |----→  角色档案卡.md  (角色追踪)
```

### 用法

```bash
# 编译第22-24章的锚点到工具箱
python3 toolbox_compile.py 22-24
```

### 锚点文件格式

```markdown
**贯穿天数**：第47天

### 核心情节
1. 赫德雷抵达龙门，与老同事重逢
2. 回忆十年前并肩作战的日子

### 角色状态
- **赫德雷**（主要）：情绪低落→渐显坚毅，对龙门既熟悉又疏离

### 回收的伏笔
- ✅ F012 赫德雷的老同事就在龙门

### 新埋下的伏笔
- 🎯 赫德雷发现一份十年前的文件，里面提到一个他以为已经死去的人
```

## 工具二：chapter_delivery — 章节交付链

五步自动完成章节交付：

```
查找正文 → MD合并 → 转docx → 发邮件 → D盘同步
```

### 用法

```bash
# 交付第22-24章
python3 chapter_delivery.py 22-24
```

### 邮件配置

在 `~/.qclaw/workspace/email.env` 中设置 SMTP 凭证：

```
SMTP_HOST=smtp.qq.com
SMTP_PORT=465
SMTP_USER=your@email.com
SMTP_PASS=your_auth_code
TO_EMAIL=recipient@email.com
```

## 完整写作流水线

```
  每日8:00 cron触发
      │
      ├─→ 写3章（AI辅助）
      │      │
      │      └─→ 每章生成 章节锚点
      │
      ├─→ toolbox_compile 22-24  (更新知识库)
      │
      ├─→ pipeline-guard filter  (过滤正文)
      ├─→ pipeline-guard scan    (扫描禁用词)
      │
      ├─→ chapter_delivery 22-24 (合并→docx→邮件→同步)
      │
      └─→ pipeline-guard clean   (清理临时文件)
```

## 依赖

```bash
pip install pypandoc_binary  # docx 转换（推荐）
# 或用系统 pandoc：winget install pandoc
```

其余均为 Python 标准库。

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

🤖 **本工具由 AI（小红）辅助开发**，在为小说《泰拉拾遗录》搭建自动化写作流水线时打磨而成。
