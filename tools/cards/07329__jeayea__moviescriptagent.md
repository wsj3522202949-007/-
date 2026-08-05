---
id: tool-07329
type: tool
area: 库
status: active
tags: [大纲规划, Python, 协议未明, 本地优先, 中文友好, 本地写作]
title: moviescriptagent
summary: 搭大纲/分卷/节拍
source: https://github.com/jeayea/moviescriptagent
created: 2026-07-18
updated: 2026-07-18
no: 7329
category: 画龙补充 / 扩容入库 — 补充源
repo: jeayea/moviescriptagent
stars: 1
url: https://github.com/jeayea/moviescriptagent
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# jeayea/moviescriptagent

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/jeayea/moviescriptagent
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：moviescriptagent
- **拉取时间**：2026-07-25 19:18:01

related:
  - methods/QUICK_START.md
---

# 🎬 AI Serial Scriptwriter (AI 连续剧编剧)

这是一个基于 **LangGraph** 和 **Google Gemini** 的智能剧本创作 Agent。它不仅能从零开始创作基于真实背景的剧本，还支持读取本地历史存档，进行长篇连续剧的**续写**。

系统利用 **Playwright** 进行本地无头浏览器搜索（无需额外的搜索 API 费用），并通过 **Streamlit** 提供友好的可视化交互界面。

## ✨ 功能特性

  * **双模式创作**：
      * **🆕 新建剧本**：自动进行互联网搜索（DuckDuckGo），基于真实资料生成“三幕式”大纲并撰写第一集。
      * **🔄 续写模式**：自动读取 `output/` 目录下的旧剧本，生成前情摘要（Summary），并基于上下文保持剧情连贯性进行续写。
  * **本地互联网搜索**：内置自定义 Tool，使用 Playwright 模拟浏览器访问 DuckDuckGo，获取实时背景资料，无需 Tavily/SerpAPI 等付费 Key。
  * **智能长文本处理**：利用 Gemini-2.5-Flash 的长上下文窗口能力，处理复杂的剧情结构和多幕场景。
  * **可视化工作流**：通过 Streamlit 实时展示 Agent 的思考过程（搜索词、摘要内容、大纲草稿、最终剧本）。
  * **自动归档**：所有生成的大纲和剧本会自动保存为 Markdown 文件到 `output/` 目录。

## 📂 项目结构

```text
.
├── app.py              # Streamlit 前端界面与交互逻辑
├── writer_flow.py      # LangGraph 核心逻辑（节点定义、状态管理、文件读写）
├── search_tool.py      # Playwright 本地搜索工具实现
├── output/             # 自动生成的剧本存档目录 (自动创建)
└── README.md           # 项目说明文档
```

## 🛠️ 安装指南

本项目推荐使用 **uv** 进行极速环境管理，也可以使用标准的 pip。

### 1\. 克隆项目或准备文件

确保 `app.py`, `writer_flow.py`, `search_tool.py` 在同一文件夹下。

### 2\. 初始化环境与安装依赖

```bash
# 初始化 uv 项目 (如果尚未初始化)
uv init

# 安装所需依赖
uv add streamlit langchain-google-genai langgraph playwright beautifulsoup4
```

### 3\. 安装浏览器内核 (关键步骤)

Playwright 需要下载浏览器二进制文件才能运行搜索功能：

```bash
uv run playwright install chromium
```

## 🚀 运行方法

使用以下命令启动 Web 界面：

```bash
uv run streamlit run app.py
```

启动后，浏览器会自动打开 `http://localhost:8501`。

## 📖 使用说明

1.  **配置 Key**：在侧边栏输入你的 **Google API Key**（需支持 Gemini 模型）。
2.  **选择模式**：
      * **新建剧本**：输入一个创意（如“19世纪的蒸汽朋克侦探”），点击开始。Agent 会先去搜索相关历史背景，然后写大纲，最后写剧本。
      * **续写剧本**：从下拉菜单中选择一个之前生成的 `.md` 文件，输入续写指令（如“主角发现了凶手的藏身处”）。Agent 会总结前文，生成新大纲并撰写下一幕。
3.  **查看结果**：运行结束后，页面会展示完整剧本，文件也会自动保存到 `output/` 文件夹。

## 生成结果示例
UI
![UI](images/screenshot1.png)
结果示例（节选）
![结果示例](images/screenshot2.png)

## ⚠️ 常见问题

**Q: 运行搜索时报错 `Executable doesn't exist`？**
A: 请确保你执行了 `uv run playwright install chromium`。

**Q: 搜索返回“无结果”？**
A: 这可能是网络问题导致无法访问 DuckDuckGo，或者触发了反爬虫机制。可以在 `search_tool.py` 中将 `headless=True` 改为 `False` 来调试观察浏览器行为。

**Q: Gemini 报错 `404 Not Found` 或权限错误？**
A: 请检查 `logic.py` 中的 `MODEL_NAME`。确保你的 API Key 有权限访问 `gemini-2.5-flash`。如果不行，请尝试改回 `gemini-1.5-flash`。
