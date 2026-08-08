---
id: tool-01494
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 中文友好, 大纲规划, 多Agent, 灵感创意]
title: SmartCommuter-MCP-Agent
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/chuwen-eilleen-zhong/smartcommuter-mcp-agent
created: 2026-07-18
updated: 2026-07-18
no: 1494
category: 二、网文 / 长篇 AI 写作系统 库
repo: Chuwen-Eilleen-ZHONG/SmartCommuter-MCP-Agent
stars: 1
url: https://github.com/chuwen-eilleen-zhong/smartcommuter-mcp-agent
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d6305909231b47ab
  - methods/最强写作方法论_全球最强综合版.md
---

# Chuwen-Eilleen-ZHONG/SmartCommuter-MCP-Agent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/chuwen-eilleen-zhong/smartcommuter-mcp-agent
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A multi-tool AI assistant for smart commuting that uses MCP to connect a LangGraph ReAct agent with weather, navigation, hotel search, and file-writing tools.
- **本地描述**：A multi-tool AI assistant for smart commuting that uses MCP to connect a LangGraph ReAct agent with weather, navigation, hotel search, and file-writing tools.
- **拉取时间**：2026-07-23 23:22:39

---

# SmartCommuter MCP Agent

一个基于 **Model Context Protocol (MCP)** 的多工具智能通勤助手。通过 LangGraph ReAct Agent 统一调度天气查询、高德地图导航、酒店搜索、本地文件写入等多种能力，支持 CLI 对话与 HTTP API 两种交互方式。

---

## 功能特性

| 工具 | 传输方式 | 能力说明 |
|------|----------|----------|
| **天气查询** (`weather`) | stdio | 接入 OpenWeather API，查询全球任意城市的实时天气 |
| **文件写入** (`write`) | stdio | 将 Agent 生成的内容保存为本地带时间戳的文本文件 |
| **高德地图** (`amap-maps`) | streamable_http | 地点搜索、路线规划、周边查询（通过 ModelScope 托管 MCP） |
| **酒店搜索** (`aigohotel`) | streamable_http | 通过 AigoHotel API 搜索全球酒店，支持星级、距离等多维筛选 |

---

## 技术栈

- **Python 3.12**
- **MCP / FastMCP** — Model Context Protocol，本地 MCP Server 框架
- **langchain-mcp-adapters** — 将 MCP 工具适配为 LangChain Tool
- **LangGraph** (`create_react_agent`) — ReAct 循环推理与多轮记忆
- **LangChain + ChatOpenAI** — 调用 OpenAI GPT-4o-mini
- **FastAPI + Uvicorn** — 提供 HTTP API 接口（`api_server.py`）
- **OpenWeather API** — 天气数据
- **AigoHotel API** — 酒店搜索数据

---

## 项目结构

```
Mini_ProjectII_SmartCommuter_MCP/
├── mcp_agent/                    # 核心 Agent 代码
│   ├── client.py                 # 方式①：直接 CLI 对话（无需 API Server）
│   ├── api_server.py             # 方式②：FastAPI HTTP 服务
│   ├── cli_chat.py               # 方式②的配套命令行客户端
│   ├── weather_server.py         # 本地 MCP Server：天气查询
│   ├── write_server.py           # 本地 MCP Server：文件写入
│   ├── agent_prompts.txt         # Agent 系统提示词
│   ├── servers_config.json       # MCP 服务器连接配置（本地，不上传）
│   ├── servers_config.json.example  # 配置模板（上传示例）
│   ├── .env                      # API 密钥（本地，不上传）
│   ├── .env.example              # 环境变量模板
│   └── requirements.txt
├── aigohotel-mcp/                # AigoHotel MCP Server（子项目）
│   ├── server.py
│   ├── requirements.txt
│   └── .env.example
├── .gitignore
└── README.md
```

---

## 快速开始

### 1. 克隆项目并创建虚拟环境

```bash
git clone <your-repo-url>
cd Mini_ProjectII_SmartCommuter_MCP

python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

### 2. 安装依赖

```bash
pip install -r mcp_agent/requirements.txt
```

### 3. 配置 API 密钥

```bash
cd mcp_agent
cp .env.example .env
```

编辑 `.env`，填入你的密钥：

```env
MODEL=gpt-4o-mini
OPENAI_API_KEY=sk-proj-你的OpenAI密钥
OPENWEATHER_API_KEY=你的OpenWeather密钥
AIGOHOTEL_API_KEY=mcp_你的AigoHotel密钥
```

> **如何获取各 API Key**
> - OpenAI：https://platform.openai.com/api-keys
> - OpenWeather：https://openweathermap.org/api（免费注册）
> - AigoHotel：https://mcp.agentichotel.cn/apply
> - 高德地图（ModelScope）：https://modelscope.cn（注册后获取推理端点）

### 4. 配置 MCP 服务器

```bash
cp servers_config.json.example servers_config.json
```

编辑 `servers_config.json`，将路径和密钥替换为本地真实值：

```json
{
  "mcpServers": {
    "weather": {
      "transport": "stdio",
      "command": "C:/你的路径/.venv/Scripts/python.exe",
      "args": ["C:/你的路径/mcp_agent/weather_server.py"]
    },
    "amap-maps": {
      "transport": "streamable_http",
      "url": "https://mcp.api-inference.modelscope.net/你的ModelScope推理ID/mcp"
    },
    "aigohotel": {
      "transport": "streamable_http",
      "url": "http://127.0.0.1:8000/mcp",
      "headers": {
        "Authorization": "Bearer mcp_你的AigoHotel密钥",
        "Content-Type": "application/json"
      }
    }
  }
}
```

---

## 运行方式

### 方式一：直接 CLI 对话（单进程）

```bash
cd mcp_agent
python client.py
```

Agent 启动后直接在终端输入问题，输入 `quit` 退出。

### 方式二：HTTP API + CLI 客户端（推荐）

**步骤 1**：先启动 AigoHotel MCP Server（提供酒店搜索服务）

```bash
cd aigohotel-mcp
pip install -r requirements.txt
python server.py
# 监听 http://127.0.0.1:8000/mcp
```

**步骤 2**：另开一个终端，启动 FastAPI Agent 服务

```bash
cd mcp_agent
python api_server.py
# 监听 http://0.0.0.0:8000/chat
```

**步骤 3**：再开一个终端，启动命令行客户端

```bash
cd mcp_agent
python cli_chat.py
```

也可以直接通过 HTTP 请求调用：

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "北京今天天气怎么样？", "thread_id": "1"}'
```

---

## 示例对话

```
你: 上海今天天气怎么样？
AI: 上海，CN
    温度: 22°C
    湿度: 68%
    风速: 3.5 m/s
    天气: 多云

你: 帮我查一下故宫附近5公里内的五星级酒店
AI: 为您找到故宫附近的高星级酒店...（返回酒店列表）

你: 把这个结果保存到文件里
AI: 已成功写入文件: ./output/note_20260416_103025.txt
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 注意事项

- `servers_config.json` 和 `.env` 已加入 `.gitignore`，**不会上传到 GitHub**，请妥善保管
- `servers_config.json` 中的 `command` 路径必须使用**绝对路径**指向本机 Python 解释器
- AigoHotel MCP Server 需要在 Agent 启动前单独运行，默认端口 `8000`
