---
id: tool-01450
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ai-novel-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/yangqi1309134997-coder/ai-novel-generator
created: 2026-07-18
updated: 2026-07-18
no: 1450
category: 二、网文 / 长篇 AI 写作系统 库
repo: yangqi1309134997-coder/ai-novel-generator
stars: 239
url: https://github.com/yangqi1309134997-coder/ai-novel-generator
tier: "S"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# yangqi1309134997-coder/ai-novel-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/yangqi1309134997-coder/ai-novel-generator
- **Stars**：239
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：An AI-powered tool to automatically generate long-form novels and stories. ai小说生成工具（一个利用 AI 自动生成长篇小说和故事的工具。）
- **本地描述**：An AI-powered tool to automatically generate long-form novels and stories. ai小说生成工具（一个利用 AI 自动生成长篇小说和故事的工具。）
- **拉取时间**：2026-07-23 23:21:21

---

# AI 小说工坊 4.5

> 基于大语言模型的智能小说生成平台，支持本地单机使用和商业多租户部署。

**版权所有 &copy; 2026 新疆幻城网安科技有限责任公司（幻城科技）**

---

## 产品形态

### 本地版（Gradio）

适合个人作者在本机直接使用，开箱即用。

```bash
python run.py
# 访问 http://127.0.0.1:7860
```

### 商业版（Vue 3 + FastAPI）

面向多用户、管理员后台、会员体系和后台任务场景。

```bash
# Windows
start-commercial.bat

# Linux / macOS
chmod +x start-commercial.sh && ./start-commercial.sh
```

默认地址：前端 `http://127.0.0.1:4173` | 后端 `http://127.0.0.1:8000` | API文档 `http://127.0.0.1:8000/docs`

---

## 核心功能

### 创作引擎

| 功能 | 说明 |
|------|------|
| 雪花法规划 | 从核心创意到完整大纲的分层展开 |
| 章节蓝图 | 每章的情节节点、角色弧线和场景设定 |
| 单章生成 | 基于上下文的章节内容生成 |
| 整本生成 | 后台任务自动生成完整小说 |
| 润色优化 | 风格化改写，去AI味 |
| 续写扩展 | 基于现有内容继续创作 |
| 连贯性分析 | 跨章节的剧情、角色、设定一致性检测 |

### 商业版特性

| 功能 | 说明 |
|------|------|
| 用户系统 | 注册、登录、JWT认证 |
| 角色权限 | 管理员 / 运营 / 客服 / 客户分层 |
| 会员体系 | 等级管理、配额控制、卡密兑换 |
| 支付系统 | 订单、账单、支付网关（含人工转账通道） |
| 管理后台 | 用户管理、卡密管理、订单管理、系统配置、提示词管理、审计日志 |
| 项目隔离 | 按用户隔离项目数据 |

### 模型支持

支持 20+ 主流 API 提供商（OpenAI、Claude、Gemini、通义千问、文心一言、DeepSeek 等），管理员统一配置，客户端开箱即用。

---

## 快速开始

### 环境要求

- Python 3.10+
- Node.js 18+（商业版前端）
- pip 包管理器

### 安装

```bash
# 克隆项目
git clone https://github.com/yangqi1309134997-coder/ai-novel-generator.git
cd ai-novel-generator

# 安装依赖
pip install -r requirements.txt

# 商业版额外安装前端
cd frontend-web
npm install
```

### 启动

| 版本 | 命令 | 地址 |
|------|------|------|
| 本地版 | `python run.py` | http://127.0.0.1:7860 |
| 商业版 | `start-commercial.bat` | http://127.0.0.1:4173 |

### 环境变量

复制 `.env.example` 为 `.env`，按需配置：

```bash
cp .env.example .env
```

主要配置项：后端端口、CORS、支付密钥、人工转账账户信息、数据库路径等。

---

## 项目结构

```
ai-novel-generator/
├── backend/              # FastAPI 后端（商业版）
│   ├── core/             # 安全、配置、设置
│   ├── models/           # ORM 模型
│   ├── routers/          # API 路由
│   ├── schemas/          # Pydantic 模型
│   ├── services/         # 业务逻辑
│   └── utils/            # 工具函数
├── frontend-web/         # Vue 3 前端（商业版）
│   └── src/
│       ├── views/        # 页面视图
│       ├── components/   # 通用组件
│       └── api/          # API 客户端
├── src/                  # 核心引擎（本地版 + 共用）
│   ├── api/              # API 客户端
│   ├── config/           # 配置管理
│   ├── core/             # 生成引擎、评估器、提示词
│   └── ui/               # Gradio 界面
├── config/               # 配置文件
│   ├── generation_config.json
│   ├── custom_prompts.json
│   └── style_prompts/    # 风格提示词模板
├── templates/            # 基础模板
├── docs/                 # 文档
└── scripts/              # 工具脚本
```

---

## 文档

| 文档 | 说明 |
|------|------|
| [更新日志](https://github.com/yangqi1309134997-coder/ai-novel-generator/blob/main/docs/CHANGELOG.md) | 版本更新记录 |
| [用户手册](https://github.com/yangqi1309134997-coder/ai-novel-generator/blob/main/docs/USER_MANUAL.md) | 完整使用指南 |
| [API 参考](https://github.com/yangqi1309134997-coder/ai-novel-generator/blob/main/docs/API_REFERENCE.md) | 后端 API 文档 |
| [依赖说明](https://github.com/yangqi1309134997-coder/ai-novel-generator/blob/main/docs/DEPENDENCIES.md) | 项目依赖清单 |
| [提示词优化指南](https://github.com/yangqi1309134997-coder/ai-novel-generator/blob/main/docs/PROMPT_OPTIMIZATION_GUIDE.md) | 提示词调优方法 |
| [优化速查](https://github.com/yangqi1309134997-coder/ai-novel-generator/blob/main/docs/OPTIMIZATION_QUICKSTART.md) | 常用优化配置 |
| [完整提示词参考](https://github.com/yangqi1309134997-coder/ai-novel-generator/blob/main/docs/COMPLETE_PROMPT_REFERENCE.md) | 所有内置提示词模板 |

---

## 测试

```bash
# 后端单元测试
pytest tests/backend/

# 商业版 API 回归
python scripts/commercial_api_regression.py
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 许可证

MIT License，详见 [LICENSE](https://github.com/yangqi1309134997-coder/ai-novel-generator/blob/main/LICENSE)。
