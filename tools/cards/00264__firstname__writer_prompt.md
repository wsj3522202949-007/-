---
id: tool-00264
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: writer_prompt
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/firstname/writer_prompt
created: 2026-07-18
updated: 2026-07-18
no: 264
category: 二、网文 / 长篇 AI 写作系统 库
repo: firstname/writer_prompt
stars: 0
url: https://github.com/firstname/writer_prompt
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 2429af14cb1c196f
  - methods/最强写作方法论_全球最强综合版.md
---

# firstname/writer_prompt

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/firstname/writer_prompt
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：ai prompts for writing novels
- **本地描述**：ai prompts for writing novels
- **拉取时间**：2026-07-23 22:46:46

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Writer Prompt

一个基于 Flask 的写作辅助工具，帮助作者管理写作项目、创作内容和组织思路。AI驱动的写作提示系统，帮助创作小说和其他文学作品。

## 功能特点

- 项目管理：创建和管理多个写作项目
- 全文设定：管理项目的世界观、人物和背景设定
- 纲要生成：规划和组织故事结构
- 正文生成：基于设定和纲要进行创作
- 数据互通：各个模块之间的数据关联和共享
- AI 辅助：智能提示和创作建议

## 技术栈

- Backend: Flask + SQLAlchemy
- Frontend: HTML + CSS + JavaScript
- Database: SQLite
- AI: 集成各类AI模型提供写作建议

## 开始使用

1. 克隆项目
```bash
git clone https://github.com/firstname/writer_prompt.git
cd writer_prompt
```

2. 创建虚拟环境
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 运行应用
```bash
python run.py
```

访问 http://127.0.0.1:5000 开始使用。

## 项目结构

```
writer_prompt/
├── app/
│   ├── models/        # 数据模型
│   ├── routes/        # 路由处理
│   ├── static/        # 静态文件
│   └── templates/     # 页面模板
├── config.py          # 配置文件
├── requirements.txt   # 依赖列表
└── run.py            # 启动脚本
```

## License

MIT License
