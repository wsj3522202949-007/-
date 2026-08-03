---
id: tool-01760
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: wechat-ai-content-agent
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/3168685397/wechat-ai-content-agent
created: 2026-07-18
updated: 2026-07-18
no: 1760
category: 二、网文 / 长篇 AI 写作系统 库
repo: 3168685397/wechat-ai-content-agent
stars: 0
url: https://github.com/3168685397/wechat-ai-content-agent
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 3168685397/wechat-ai-content-agent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/3168685397/wechat-ai-content-agent
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI workflow for WeChat Official Account content strategy, writing, visuals, layout, and draft-box automation
- **本地描述**：AI workflow for WeChat Official Account content strategy, writing, visuals, layout, and draft-box automation
- **拉取时间**：2026-07-23 23:30:20

---

# 微信公众号 AI 内容策略 Agent

这是一个面向「50+ 女性穿搭」公众号的本地 AI 内容运营工作流。项目目标不是无脑群发，而是把选题、标题、正文、真实穿搭配图、黄黑标题字封面、排版、草稿箱写入和 Excel 工作台记录串成一条可复用流程。

当前主线：

```text
历史数据学习
-> 周/日策略判断
-> 标题实验与评分
-> 正文初稿
-> 真实穿搭配图
-> 黄黑标题字封面
-> 精修排版
-> 图片门禁
-> 写入公众号草稿箱
-> 写回 Excel 工作台
-> 人工预览后再决定是否发布
```

## 当前能力

- 自动读取本地自有文章数据和竞品标题库，生成质量学习结果。
- 自动生成每日文章任务、标题候选、标题评分和正文初稿。
- 自动生成适合 50+ 女性读者的真实穿搭配图。
- 自动生成封面底图，并叠加黄色粗体、黑色粗描边的三行标题字。
- 自动检查图片门禁：正文图数量、封面是否有黄黑标题字、是否存在 placeholder。
- 自动生成精修排版稿：`article_refined.md`、`article_refined.html`、`article_layout_preview.html`。
- 自动写入微信公众号草稿箱。
- 自动写回桌面 Excel 工作台：`C:\Users\86177\Desktop\公众号AI内容工作台.xlsx`。
- 每天早上 6 点通过 Codex automation 自动运行。

## 安全边界

项目默认只写入公众号草稿箱，不自动发布，不自动群发。

发布前仍需要人工检查：

- 标题是否准确、有吸引力；
- 摘要是否自然；
- 封面是否清楚、有点击欲；
- 正文是否有明显 AI 腔；
- 配图是否讲清穿搭知识；
- 图片版权与平台合规；
- 是否适合当天发布。

关键保护：

- `WECHAT_DRAFT_ONLY=true` 时才允许写入草稿箱。
- 上传脚本不会调用 `freepublish/submit`、`message/mass/sendall`、`message/mass/send`。
- `visual_quality_gate.json` 未通过时停止写入草稿箱。
- 封面必须有 `cover-final-base.png` 和 `cover_text_passed=true`。

## 主要文件

| 文件 | 作用 |
|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `daily_article_pipeline_v1.py` | 每日文章生成主流程 |
| `daily_quality_learning_v1.py` | 读取历史表现，生成质量学习结果 |
| `strategy_agent.py` | 周策略报告和任务卡生成 |
| `content_production_v1.py` | 标题实验器、提纲生成器、CSV/XLSX 导出 |
| `layout_refiner_v1.py` | 精修排版稿生成 |
| `scripts/visual_outfit_pipeline_v1.py` | 真实穿搭图、黄黑标题字封面、图片门禁 |
| `scripts/wechat_api_draft_upload.py` | 微信公众号草稿箱写入 |
| `scripts/workbench_sync.mjs` | 标题/内容生产数据写回 Excel |
| `scripts/daily_article_workbench_sync.mjs` | 每日文章状态写回 Excel |
| `scripts/workflow_health_check.py` | 一键体检整套流程 |
| `data/latest_daily_article.json` | 最新每日文章记录 |
| `data/latest_wechat_api_draft_result.json` | 最新草稿箱写入结果 |
| `reports/workflow_health_check_latest.json` | 最新流程体检报告 |

## 如何运行

进入项目目录：

```powershell
cd C:\Users\86177\Documents\Codex\2026-07-12\qin\outputs\公众号内容策略Agent_V0
```

只生成今日文章草稿包：

```powershell
python daily_article_pipeline_v1.py
```

生成精修排版：

```powershell
python layout_refiner_v1.py
```

生成真实穿搭配图和黄黑标题字封面：

```powershell
python scripts\visual_outfit_pipeline_v1.py --generate
```

写入微信公众号草稿箱：

```powershell
python scripts\wechat_api_draft_upload.py --yes
```

同步 Excel 工作台：

```powershell
node scripts\workbench_sync.mjs --mode sync --title-csv data\title_experiments_daily_YYYYMMDD.csv --outline-csv data\content_outlines_daily_YYYYMMDD.csv --qa-dir reports\daily_article_workbench_qa
node scripts\daily_article_workbench_sync.mjs
```

一键体检：

```powershell
python scripts\workflow_health_check.py
```

## 定时任务

当前 Codex automation：

- ID：`8`
- 名称：`微信公众号每日6点创作并自动写入草稿箱`
- 频率：每天早上 6 点
- 边界：自动创作并写入草稿箱，不自动发布，不自动群发。

每日任务执行顺序：

1. `python daily_article_pipeline_v1.py`
2. `python layout_refiner_v1.py`
3. `python scripts\visual_outfit_pipeline_v1.py --generate`
4. `python scripts\wechat_api_draft_upload.py --yes`
5. `node scripts\workbench_sync.mjs ...`
6. `node scripts\daily_article_workbench_sync.mjs`

## 本地配置

密钥只放在 `.env`，不要提交到 GitHub。

当前重要开关：

```env
WECHAT_DRAFT_ONLY=true
ENABLE_IMAGE_GENERATION=true
ENABLE_AUTO_WRITING=true
ENABLE_DEEPSEEK_ANALYSIS=true
ENABLE_VISION_ANALYSIS=false
```

说明：

- `ENABLE_IMAGE_GENERATION=true`：已启用阿里生图模型。
- `ENABLE_AUTO_WRITING=true`：每日正文主笔优先接入 DeepSeek，接口异常时回退到本地模板。
- `ENABLE_DEEPSEEK_ANALYSIS=true`：复盘和策略判断优先接入 DeepSeek，接口异常时回退到本地规则。
- `ENABLE_VISION_ANALYSIS=false`：视觉理解分析暂未开启；当前图片质量主要由生成规范和本地门禁控制。

如果要继续提升图片判断能力，下一步再开启 `ENABLE_VISION_ANALYSIS=true` 并接入封面/配图审美评分。

## 当前验收状态

最新体检重点：

- Python 核心脚本语法通过。
- Node 同步脚本语法通过。
- Excel 工作台存在并可写入。
- 最新文章 A008 已生成完整产物。
- 正文真实穿搭图数量：6 张。
- 封面黄黑标题字门禁：通过。
- 微信草稿箱写入：成功。
- 每日 6 点自动任务：已启用。

## 仍需优化

严格说，这套流程已经能跑通主线，但还不是“完美项目”。下一步建议补齐：

- 增加 DeepSeek 生成后的二次润色和人工语气校验，让正文更接近成熟编辑。
- 增加发布后 24h / 72h 数据回填和复盘判断。
- 做一个更完整的 GitHub 作品集包：截图、流程图、演示数据、脱敏说明、项目复盘。
- 给封面和正文配图增加人工评分字段，沉淀“哪种图片更能提高点击”。
- 减少 Excel 备份文件数量，避免桌面越来越乱。
