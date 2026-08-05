---
id: tool-07184
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 中文友好, 本地写作]
title: hyacinth-writer
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/charllote99/hyacinth-writer
created: 2026-07-18
updated: 2026-07-18
no: 7184
category: 画龙补充 / 扩容入库 — 补充源
repo: charllote99/hyacinth-writer
stars: 2
url: https://github.com/charllote99/hyacinth-writer
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# charllote99/hyacinth-writer

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/charllote99/hyacinth-writer
- **Stars**：2
- **语言**：HTML
- **License**：NOASSERTION
- **Topics**：ai-assistant, creative-writing, local-first, novel-writing, rag, single-file, vue3, wangwen, writing-tool, xiaoshuo, xiezuo
- **GitHub 描述**：A Zero-Gravity, Local-First AI Writing Workstation. (极简、零重力、本地优先的 AI 写作工作站)(小说助手 / 网文工具）
- **本地描述**：hyacinth-writer
- **拉取时间**：2026-07-25 19:13:24

---

# ● Hyacinth Writer 使用手册
**版本：v30.0 | 架构：Dual-Core Agentic (双核代理) 驱动**

---

### 🏗️ 核心架构：双核驱动 (The Architect & The Builder)

**1. 逻辑架构师 (DeepSeek-V3) [冷脑]**
这是系统的大脑。它负责**构思**。
* **职责**：当你开启“⚡ DeepSeek 构思”或使用工具时，它不直接写作，而是负责解构你的意图、规避审查、补全逻辑漏洞，并生成一份精密详尽的“施工图纸”（Prompt）。
* **特性**：永远保持 **0.7** 的冷静温度，确保逻辑严密，不胡编乱造。

**2. 审美执行官 (Claude/Main Model) [热手]**
这是系统的手。它负责**表达**。
* **职责**：它接收来自架构师的“图纸”，专注于文笔的渲染、辞藻的修饰和情感的注入。
* **特性**：跟随你设定的“创作温度”滑块（推荐 1.0+），可狂野可克制，确保文采飞扬。

**3. 智能温控分离 (Temperature Separation)**
系统实现了“冷脑热手”机制。逻辑层保持绝对理性，防止幻觉；表现层保持高度感性，确保文学性。

---

### 🤖 AI 深度赋能 (Agentic Workflow)

* **⚡ 智能构思开关**
    * 位于输入框上方的紫色开关。
    * **开启后**：你的任何简短指令（如“写个打架”）都会先经过架构师的深度拆解和脱敏处理，转化为高张力的文学指令，再交给主模型执行。

* **🧠 大师级技法 (Master Class Tools)**
    新增的高阶工具组，让网文写手也能轻松驾驭文学性技法：
    * **🧊 冰山对话 (Subtext)**：设计“话里有话”的潜台词张力，拒绝直白。
    * **🎬 蒙太奇剪辑 (Montage)**：处理双线叙事与转场，营造电影感。
    * **🕸️ 蝴蝶效应 (Logic)**：利用 DeepSeek 的推理能力进行剧情分支推演。
    * **🕯️ 氛围锚点 (Anchor)**：通过微小客观对应物（如烛火、尘埃）侧写环境。

* **🔗 动态世界观挂载 (Context Link)**
    工具面板新增“关联/断开”开关。
    * **关联模式**：工具会自动读取本书的“力量体系”和“世界基调”，生成贴合原著的内容。
    * **独立模式**：取消勾选后，DeepSeek 会暂时“失忆”，为你提供纯净的、跨题材的独立灵感（适合开新书或跑团）。

* **🃏 命运分叉 2.0**
    现在的“命运卡牌”不再是随机生成。点击卡牌后，架构师会阅读前文 **2500字**，根据剧情逻辑精准计算出最合理的“冲突点”或“悬疑点”。

---

### 📝 写作交互黑科技

* **全知视野扩容**
    * 架构师拥有 **2500 Token** 的超长视野以把握剧情大局。
    * 主写手拥有 **2000 Token** 视野以确保文风连贯（告别“前言不搭后语”）。

* **RAG 逻辑穿透**
    * 本地向量数据库（设定集）现在不仅服务于写手，也服务于架构师。
    * DeepSeek 在构思情节时，会自动检索你的设定，避免产生违背世界观的“幻觉”。

* **自然语言任务书**
    * 所有灵感工具不再生成僵硬的 `关键词: 数值`。
    * 升级为生成一段带有“导演说戏”感的**自然语言任务简报**，最大化激发 AI 的联想能力。

---

### ⌨️ 快捷键速查

| 快捷键 | 功能说明 |
| :--- | :--- |
| `Ctrl + S` | **[硬盘直连]** 无感同步保存到本地 .txt (推荐常驻) |
| `Ctrl + E` | **[沉浸模式]** 隐藏所有 UI，只留纸张 (Zen Mode) |
| `Ctrl + P` | **[排版输出]** 调用浏览器打印 / 导出 PDF |
| `Ctrl + Z` | **[撤销]** 撤销上一次 AI 生成或编辑操作 |

---

### 🌟 设计哲学

> **"Logic acts as the Architect, while Aesthetics serves as the Builder."**
>
> 让逻辑归于逻辑，让艺术归于艺术。
> Hyacinth Writer v30.0 —— 为追求极致的创作者而生。

## ✨ 核心特性 (Features)

- **🚀 零重力部署 (Zero-Gravity)**：单文件 HTML，无需安装，双击即用，可存入 U 盘随身携带。
- **🔒 数据绝对主权 (Local-First)**：基于 IndexedDB + File System Access API。文章只存浏览器和本地硬盘，绝无云端上传。
- **🤖 RAG 记忆引擎 (Archivist)**：内置向量检索，AI 能“读懂”你的前文伏笔和设定，而非仅仅通过上下文窗口。
- **✒️ 墨灵助手 (Ink Spirit)**：沉浸式悬浮交互，支持润色、续写、扩写。
- **🔌 全模型兼容 (Universal API)**：支持 DeepSeek, Claude, Gemini 以及 **本地 Ollama** (支持 OpenAI 兼容接口配置)。

## 📦 如何使用 (Usage)

### 方式一：在线体验 (推荐)
👉 [点击这里直接使用 Hyacinth Writer](https://Charllote99.github.io/hyacinth-writer/)
*(数据依然只保存在你的本地浏览器中)*

### 方式二：离线使用 (极客推荐)
1. 点击右上角绿色 `Code` 按钮 -> `Download ZIP`。
2. 解压后，双击 `index.html` 即可运行。

## 🛠️ 配置指南

1. 点击右上角 **⚙️ 设置**。
2. 在 **模型 (Model)** 选项卡中，选择厂商或点击 **Custom (自定义)**。
3. 填入你的 API Key 和 Base URL (例如本地 Ollama填 `http://localhost:11434/v1/chat/completions`)。
4. 点击检查连通性。

## 🔍 关键词 (Keywords)
AI写作, 小说创作, 网文工具, 码字软件, 写作助手, 创意写作, DeepSeek, Claude, 本地存储, 隐私保护, 单文件应用, 离线写作.

## ☕ 支持作者 (Sponsor)

Hyacinth Writer 是一个完全免费的开源项目。
我是一名独立开发者，如果你喜欢这个工具，或者它帮助你写出了精彩的故事，欢迎请我喝一杯咖啡，这将是我继续更新的最大动力！❤️

![Sponsor Me](./sponsor.png)

## 📄 版权说明 (License)

本项目采用 **[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)** 协议进行许可。

- ✅ **您可以**：自由下载、使用、修改源码、分享给朋友。
- ❌ **严禁商用**：禁止将本项目打包售卖、植入广告或用于商业收费服务。
- 📢 **转载请注明**：原作者 [Charllote99]。

related:
  - methods/QUICK_START.md
---
*Made with ❤️ by [Charllote99] & AI Assistant*
