---
id: tool-00216
type: tool
area: 库
status: active
tags: [大纲规划, Python, 协议宽松, 本地优先, 中文友好, 本地写作]
title: novel_outline_generator
summary: 搭大纲/分卷/节拍
source: https://github.com/xulingran/novel_outline_generator
created: 2026-07-18
updated: 2026-07-18
no: 216
category: 二、网文 / 长篇 AI 写作系统 库
repo: xulingran/novel_outline_generator
stars: 0
url: https://github.com/xulingran/novel_outline_generator
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# xulingran/novel_outline_generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/xulingran/novel_outline_generator
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：使用LLM为文本文件生成大纲
- **本地描述**：使用LLM为文本文件生成大纲
- **拉取时间**：2026-07-23 22:45:21

---

## 小说大纲生成工具

支持三种运行模式：`WebUI`、`命令行`、`桌面 GUI`。  
本项目已统一为 **Python 官方 `venv + pip` 工作流**，不再使用 `uv`。

## 快速开始（推荐）

### 1. 创建并激活虚拟环境

macOS / Linux：

```bash
python3 -m venv venv_system
source venv_system/bin/activate
```

Windows（PowerShell）：

```powershell
py -3.12 -m venv venv_system
venv_system\Scripts\Activate.ps1
```

Windows（CMD）：

```bat
py -3.12 -m venv venv_system
venv_system\Scripts\activate.bat
```

### 2. 安装依赖

```bash
python -m pip install -U pip
python -m pip install -e ".[dev]"
```

### 3. 配置环境变量

```bash
cp .env.sample .env
```

Windows:

```bat
copy .env.sample .env
```

填写至少一个可用提供商的 API Key（`openai/gemini/zhipu/aihubmix`）。

---

## 启动方式

### 方式一：启动脚本（三选一菜单）

Windows:

```bat
run.bat
```

macOS / Linux:

```bash
./run.sh
```

菜单中可选：
1. WebUI
2. 命令行
3. GUI

### 方式二：手动命令

WebUI：

```bash
venv_system/bin/python -m uvicorn web_api:app --reload --host 0.0.0.0 --port 8000
```

命令行：

```bash
venv_system/bin/python main.py --mode process
```

GUI：

```bash
venv_system/bin/python gui_launcher.py
```

Windows（对应写法）：

```bat
venv_system\Scripts\python -m uvicorn web_api:app --reload --host 0.0.0.0 --port 8000
venv_system\Scripts\python -Xutf8 main.py --mode process
venv_system\Scripts\python gui_launcher.py
```

---

## 开发命令

```bash
venv_system/bin/python -m ruff check . --fix
venv_system/bin/python -m black .
venv_system/bin/python -m black . --check
venv_system/bin/python -m mypy .
venv_system/bin/python -m pytest tests/ -v
```

Windows：

```bat
venv_system\Scripts\python -m ruff check . --fix
venv_system\Scripts\python -m black .
venv_system\Scripts\python -m black . --check
venv_system\Scripts\python -m mypy .
venv_system\Scripts\python -m pytest tests/ -v
```

---

## 常见问题

### 1) GUI 启动失败（`_tkinter` / `init.tcl`）
- 请确认使用的是 `venv_system` 对应的 Python。
- macOS 建议使用 python.org 官方安装包或 pyenv 安装带 Tcl/Tk 的 Python。

### 2) 点开始处理没反应
- 先在处理页选择文件，按钮会启用。
- 看日志区是否有错误（配置/API Key/文件读取等）。

### 3) 修改 `.env` 后不生效
- 需要重启应用。

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 目录结构

```text
novel_outline_generator/
├── main.py
├── web_api.py
├── gui_launcher.py
├── run.bat
├── run.sh
├── gui/
├── services/
├── models/
├── tests/
└── ui/index.html
```

## 许可证

MIT
