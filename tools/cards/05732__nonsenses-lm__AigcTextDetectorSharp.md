---
id: tool-05732
type: tool
area: 库
status: active
tags: [C#, 协议宽松, 本地优先, 中文友好, 去AI味, 本地写作]
title: AigcTextDetectorSharp
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/nonsenses-lm/aigctextdetectorsharp
created: 2026-07-18
updated: 2026-07-18
no: 5732
category: 一、去 AI 味 / Humanizer 库
repo: nonsenses-lm/AigcTextDetectorSharp
stars: 1
url: https://github.com/nonsenses-lm/aigctextdetectorsharp
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# nonsenses-lm/AigcTextDetectorSharp

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/nonsenses-lm/aigctextdetectorsharp
- **Stars**：1
- **语言**：C#
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AIGC 文本识别器
- **本地描述**：AIGC 文本识别器
- **拉取时间**：2026-07-25 18:29:34

---

# Aigc Text Detector Sharp 
AIGC Text Detector Sharp 是一款检测文本是由人类撰写还是 AI 生成的工具，支持中文和英文。

本项目基于是 ICLR'24 Spotlight 论文 "Multiscale Positive-Unlabeled Detection of AI-Generated Texts" 的 C# + ONNX 非官方实现。

## 功能特性

- 支持中文和英文文本检测
- 本地运行，数据不外传
- 支持多种输入格式：纯文本、Markdown、DOCX、PDF
- 提供 CLI 和 Web API 两种使用方式
- 超过 512 tokens 的文本自动分块处理

## 项目结构

```
AIGC_detector_zhv3/
├── AigcDetectorSharp.Core/     # 核心库
├── AigcDetectorSharp.UI/       # 桌面 / WebUI
├── AigcDetectorSharp/          # CLI 工具
├── model_zhv3/                 # 中文模型 (v3)
├── model_env3/                 # 英文模型 (v3)
├── app.py                      # Python 推理脚本
├── convert_to_onnx.py          # ONNX 模型转换
```

## 安装

### 依赖要求

- .NET 10.0+
- Python 3.8+ (若使用 Python 推理和转换)

### Python 依赖（若使用）

```bash
pip install torch transformers onnxruntime
```

## 使用方法

### C# CLI 使用

```bash
# 检测中文文本
./publish/AigcDetectorSharp "待检测的中文文本"

# 检测英文文本
./publish/AigcDetectorSharp -m en "English text to detect"

# 从文件检测
./publish/AigcDetectorSharp -f /path/to/file.txt
```

### 服务器模式

```bash
# 启动 Web 服务器
./publish/AigcDetectorSharp.UI --server --port=5000
```

### API 调用

```bash
curl -X POST http://localhost:5000/api/detect \
  -H "Content-Type: application/json" \
  -d '{"text":"your text","model":"zh"}'
```

## 命令行选项

| 选项 | 说明 |
|------|------|
| `-m zh` | 中文模型 (默认) |
| `-m en` | 英文模型 |
| `-f <file>` | 从文件读取 (.txt, .md, .docx, .pdf) |
| `-p <dir>` | 自定义模型目录 |
| `--echo` | 输出原始文本 |
| `--server` | 启动 Web 服务器 |
| `--port=<n>` | 服务器端口 (默认: 5000) |

## 输出格式

```
<Label> <Probability>
```

- `Label`: `Human` 或 `AI`
- `Probability`: 置信度 (0.0–1.0)

## 模型版本

| 版本 | 中文模型 | 英文模型 | 说明 |
|------|----------|----------|---related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| v3 | AIGC_detector_zhv3 | AIGC_detector_env3 | 针对最新 LLMs |
| v2 | AIGC_detector_zhv2 | AIGC_detector_env2 | 增强版检测器 |
| v1 | AIGC_detector_zh | AIGC_detector_env | 基础版 |

## 许可证

MIT License

## 参考

- 论文: [Multiscale Positive-Unlabeled Detection of AI-Generated Texts](https://arxiv.org/abs/2305.18149)
- 原项目: [Github](https://github.com/YuchuanTian/AIGC_text_detector)
