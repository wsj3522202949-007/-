---
id: tool-05648
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 中文友好, 去AI味, 本地写作]
title: ai-text-detector2
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/caryyang59/ai-text-detector2
created: 2026-07-18
updated: 2026-07-18
no: 5648
category: 一、去 AI 味 / Humanizer 库
repo: CaryYang59/ai-text-detector2
stars: 0
url: https://github.com/caryyang59/ai-text-detector2
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: f406ea6a64171368
  - methods/改稿润色指令库.md
---

# CaryYang59/ai-text-detector2

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/caryyang59/ai-text-detector2
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：CaryYang59/ai-text-detector2
- **拉取时间**：2026-07-25 18:26:31

---

# 产品功能命名生成器 (Feature Namer)

零依赖、纯Python标准库实现的产品功能命名工具。输入功能描述，自动生成10个多维度命名方案，附评分与可行性分析。

## 功能特性

- **4种命名维度**：直白型、隐喻型、情感型、动词型
- **可行性评估**：易发音、易记忆、商标注册友好性
- **多维评分**：记忆力、可发音性、商标潜力、品牌契合度
- **品牌调性适配**：支持5种调性（专业/活泼/极简/企业级/消费级）
- **双界面**：CLI命令行 + Web UI（端口8080）
- **零依赖**：仅使用Python标准库，无需pip install

## 命名评估框架

| 维度 | 说明 | 高分标准 |
|------|------|-------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 记忆力 | 名称长度与简洁度 | 5-8个字符为佳 |
| 可发音性 | 元音比例与辅音连缀 | 无连续辅音，元音≥30% |
| 商标潜力 | 是否含通用词 | 独特性强，不含hub/pro等通用词 |
| 品牌契合 | 符合现代产品命名规律 | 首字母大写，现代后缀加分 |

## 使用方法

### CLI

```bash
# 基础用法
python namer.py "帮助团队管理和追踪项目任务"

# 指定品牌调性和目标用户
python namer.py "智能客服自动回答用户问题" "professional" "企业用户"
```

### Web UI

```bash
python app.py        # 默认端口8080
python app.py 9090   # 自定义端口
```

然后浏览器访问 http://localhost:8080

### 3个场景示例

```bash
python test_cases.py
```

## 局限性

- 命名生成基于启发式规则，不依赖大语言模型
- 商标注册风险评估为启发式估算，不代表法律意见
- 当前仅支持英文命名（中文输入用于描述，命名输出为英文）
- 隐喻词库较小，可通过扩展 `METAPHOR_TEMPLATES` 丰富
