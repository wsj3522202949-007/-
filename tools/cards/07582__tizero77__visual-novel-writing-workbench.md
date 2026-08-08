---
id: tool-07582
type: tool
area: 库
status: active
tags: [提示词, JavaScript, 协议宽松, 本地优先, 中文友好, 多Agent, 本地写作]
title: visual-novel-writing-workbench
summary: 提示词/写作工作流
source: https://github.com/tizero77/visual-novel-writing-workbench
created: 2026-07-18
updated: 2026-07-18
no: 7582
category: 画龙补充 / 扩容入库 — 补充源
repo: tizero77/visual-novel-writing-workbench
stars: 0
url: https://github.com/tizero77/visual-novel-writing-workbench
tier: "C"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 50bc6f62a6e061ac
  - methods/QUICK_START.md
---

# tizero77/visual-novel-writing-workbench

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/tizero77/visual-novel-writing-workbench
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：一个“视觉小说辅助生成器”单页创作工作台，核心解决的是视觉小说创作者在灵感收集、剧情结构整理、场景写作和 AI 辅助之间频繁切换工具、上下文断裂的问题
- **本地描述**：visual-novel-writing-workbench
- **拉取时间**：2026-07-25 19:26:18

related:
  - methods/QUICK_START.md
---

# 视觉小说辅助生成器

一个以"当前场景写作"为中心的单页创作工作台。在同一页面内完成设定管理、章节结构、正文写作和 AI 辅助——不需要在多个页面间跳转。

## 特性

- **单页三栏工作台**：左侧设定库+灵感录入 / 中间章节→场景→正文编辑 / 右侧 AI 建议队列+快捷写作
- **空白项目启动**：新建项目从空白模板开始，无伪装 demo 内容；样例项目独立打开
- **场景写作主轴**：章节切换、场景切换、正文编辑在同一屏联动，设定引用和 AI 建议共享当前上下文
- **AI 辅助写作**：基于当前场景、关联节点、关联设定生成扩写/润色/对白/摘要，结果进入待确认队列
- **结构图覆盖层**：节点画布降级为全屏覆盖层，点「结构图」打开，关闭后回到原写作位置
- **AI 设置弹层**：API 配置移到独立弹窗，不打断正文编辑
- **项目管理弹层**：项目切换/复制/删除/导入导出集中在弹窗中
- **流式生成**：SSE 打字机效果，实时看到 AI 输出
- **本地优先**：所有数据存储在浏览器 localStorage，Python 代理转发 AI 请求
- **零前端依赖**：纯 Vanilla JS ES Modules，克隆即跑

## 快速启动

```bash
# 1. 克隆仓库
git clone <repo-url>
cd 视觉小说辅助生成器

# 2. 启动开发服务器（需要 Python 3）
npm run dev
# 或: python3 server.py 4174

# 3. 打开浏览器
open http://127.0.0.1:4174

# 4. 运行测试
npm test
```

## AI 设置

1. 点击顶栏 `AI 设置`
2. 填写 OpenAI 兼容接口地址，例如 `https://api.openai.com/v1/chat/completions`
3. 填写模型名和 API Key
4. 点击 `测试连接`
5. 成功后回到正文区使用 `扩写当前场景 / 润色正文 / 补全对白 / 生成摘要`

在弹层中可配置：

- **Endpoint**：OpenAI 兼容的 Chat Completions API 地址，也可以直接填写 base URL（例如 `https://api.deepseek.com` 或 `https://api.openai.com/v1`），程序会自动补成 `.../chat/completions`
- **Model**：模型名称（如 `gpt-5.5`）
- **API Key**：你的 API 密钥
- **系统提示词**：自定义 AI 行为指令
- **启用流式输出**：开关 SSE 打字机效果

填写后点击「测试连接」确认配置有效。所有配置保存在浏览器本地，通过本地 `/api/generate` 代理请求，不会上传至第三方。

### 本地联调 AI

用内置 mock 服务可以在不上线的情况下测试完整 AI 流程：

```bash
# 终端 1：启动项目
npm run dev

# 终端 2：启动 mock AI
python3 mock-ai-server.py
```

然后在 AI 设置中填入：

- **Endpoint**：`http://127.0.0.1:8787/v1/chat/completions`
- **Model**：`mock-model`
- **API Key**：任意非空字符串（如 `sk-test`）

mock 服务会根据你触发的动作（扩写/润色/对白/摘要）返回对应类型的模拟文本。

### AI 结果入稿

AI 生成结果会进入右侧「AI 待确认」队列，支持三种入稿方式：

- **追加**：将 AI 内容追加到当前场景正文末尾
- **替换**：用 AI 内容完全替换当前场景正文
- **仅存建议**：标记为已接受但不修改正文

### 安全提示

API Key 存储在浏览器 localStorage 中，不会上传至第三方服务器。请勿在公共设备上保存密钥。

## 导入/导出

- **导出项目**：点击顶栏「导出」按钮，下载单项目 JSON
- **导出工作区**：在项目管理弹层中导出全部项目
- **导入**：在项目管理弹层中导入 JSON 文件恢复项目
- 导出文件包含版本元数据（`exportedAt`），支持向后兼容

## 项目结构

```
src/
├── main.js                       # 入口，事件路由，状态管理
├── lib/
│   ├── workspace-state.js        # 工作区状态（项目 CRUD、导入导出）
│   ├── workbench-state.js        # 工作台状态（设定库、大纲、正文、AI 队列、场景-节点关联）
│   ├── workflow-state.js         # 画布工作流状态（节点、连线、素材池）
│   ├── ai-generation.js          # AI 生成（场景优先的 action 注册和 prompt 构建）
│   ├── stream-client.js          # SSE 流式客户端
│   ├── component.js              # 组件注册/挂载/patch
│   ├── storage.js                # localStorage 封装
│   ├── gap-detector.js           # 结构缺口检测
│   ├── intake-analysis.js        # 碎片分析
│   └── outline-sync.js           # 大纲同步
├── components/
│   ├── app-shell.js              # 顶层壳（品牌、状态条、操作栏）
│   ├── workspace-view.js         # 单页三栏工作台主视图
│   ├── canvas-overlay.js         # 结构图全屏覆盖层
│   ├── canvas.js                 # 画布渲染
│   ├── inspector.js              # 节点详情
│   ├── node-card.js              # 节点卡片
│   └── render-connector.js       # 连线渲染
├── data/
│   ├── empty-project.js          # 空白项目模板
│   ├── sample-project.js         # 样例项目
│   └── workflow-data.js          # 旧版种子数据
└── styles/
    └── app.css                   # 样式（含 dark mode）
```

## 技术栈

- **前端**：Vanilla JS (ES Modules)，零构建工具依赖
- **后端代理**：Python 3 标准库 (`http.server`)
- **测试**：Node.js 内置 test runner (`node --test`)
- **存储**：浏览器 localStorage

## License

MIT
