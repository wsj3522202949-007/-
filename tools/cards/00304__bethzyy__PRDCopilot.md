---
id: tool-00304
type: tool
area: 库
status: active
tags: [提示词, HTML, 协议未明, 需API密钥, 中文友好, 多Agent]
title: PRDCopilot
summary: 提示词/写作工作流
source: https://github.com/bethzyy/prdcopilot
created: 2026-07-18
updated: 2026-07-18
no: 304
category: 二、网文 / 长篇 AI 写作系统 库
repo: bethzyy/PRDCopilot
stars: 0
url: https://github.com/bethzyy/prdcopilot
tier: "C"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 35c720f0f2fb2f6b
  - methods/最强写作方法论_全球最强综合版.md
---

# bethzyy/PRDCopilot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/bethzyy/prdcopilot
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：PRD Copilot - AI-driven PRD writing assistant
- **本地描述**：PRD Copilot - AI-driven PRD writing assistant
- **拉取时间**：2026-07-23 22:47:56

---

# PRD Copilot · 需求搭子

AI 驱动的 PRD（产品需求文档）写作助手，通过对话引导帮你从零构建完整的 13 板块 PRD。

## 功能

- **AI 对话引导** — "小搭"以 PM 老朋友的口吻，通过微信式聊天引导你填写每个板块
- **13 板块完整覆盖** — 项目概况、业务目标、用户画像、竞品分析、替代方案、核心场景、功能需求、非功能需求、约束条件、埋点分析、里程碑、风险、验收标准
- **实时评分** — 65 分制评分系统，实时反映 PRD 完整度
- **雷达图仪表盘** — 可视化展示各板块得分分布
- **智能板块聚焦** — 自动锁定最薄弱板块，引导深聊
- **一键 PRD 分解** — 输入产品描述，AI 自动生成完整 PRD 骨架
- **多版本管理** — 支持多个项目版本，独立存储和评分
- **导出** — 支持 Markdown、PDF、CSV、JSON 导出
- **数据自动保存** — IndexedDB + localStorage 双层存储，刷新不丢数据
- **可拖拽布局** — 内容区、聊天面板、仪表盘之间支持拖拽调整宽度

## 技术架构

```
PRDCopilot/
├── index.html              # React 18 + htm + Tailwind CSS（UI层）
├── js/
│   ├── core/
│   │   ├── schema.js       # PRD 结构定义（13 板块 schema）
│   │   └── scoring.js      # 评分引擎 + 模板检测
│   ├── ai/
│   │   ├── client.js       # ZhipuAI GLM API（流式 + 重试）
│   │   ├── prompts.js      # 对话提示词 + 提取提示词（双提示词架构）
│   │   └── parser.js       # AI 输出解析、JSON 容错、智能板块推断
│   ├── state/
│   │   ├── actions.js      # Action 类型常量
│   │   └── reducer.js      # 统一 Reducer（30+ action types）
│   └── storage/
│       └── repository.js   # IndexedDB + localStorage 双层存储
├── config.json             # API 配置（gitignore 排除）
└── start.bat               # 一键启动
```

### 双提示词架构

核心设计：每次用户消息触发两次独立的 API 调用。

1. **对话提示词**（轻量）— 只负责自然语言聊天，不知道 PRD 结构
   - 输入：用户消息 + 当前聚焦板块信息
   - 输出：3-5 句微信口吻回复

2. **提取提示词**（精确）— 只负责结构化数据提取
   - 输入：对话历史 + PRD 快照
   - 输出：纯 JSON（含智能板块推断）

优势：每个提示词都在弱模型（glm-4-airx）的能力范围内，对话质量和数据提取精度互不影响。

## 快速开始

### 1. 启动服务器

```bash
# 方式一：双击 start.bat（Windows）
start.bat

# 方式二：手动启动
python -m http.server 8090
```

浏览器访问 http://localhost:8090

### 2. 配置 API Key

首次使用需要在设置中配置 [ZhipuAI API Key](https://open.bigmodel.cn/)。

格式：`id.secret`（如 `8760a192a1da4bd3b7ccb4a2b3e29926.xxxxxxxxxxxxxxxx`）

也可直接编辑 `config.json`：
```json
{
  "apiKey": "你的API Key",
  "apiEndpoint": "https://open.bigmodel.cn/api/paas/v4/chat/completions",
  "apiModel": "glm-4-airx"
}
```

### 3. 开始使用

- **从零开始**：点击"新建项目"，在聊天中和"小搭"对话
- **快速生成**：在首页输入产品描述，点击"AI 智能分解"一键生成 PRD 骨架

## 技术栈

| 层 | 技术 |
|---|---related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| UI | React 18 + htm（模板字面量）+ Tailwind CSS（CDN） |
| 状态管理 | useReducer + Context（单向数据流） |
| AI | ZhipuAI GLM API（glm-4-airx） |
| 存储 | IndexedDB（项目数据）+ localStorage（元数据） |
| 模块化 | ES Modules（原生 import/export） |

## 安全说明

- `config.json` 包含 API Key，已在 `.gitignore` 中排除，不会提交到 GitHub
- API Key 仅保存在浏览器本地，不会发送到第三方服务
- 所有 AI 请求直接从浏览器发送到 ZhipuAI API
