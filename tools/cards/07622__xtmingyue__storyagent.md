---
id: tool-07622
type: tool
area: 库
status: active
tags: [大纲规划, 校对, Python, 协议传染, 需API密钥, 中文友好, 改稿润色]
title: storyagent
summary: 搭大纲/分卷/节拍
source: https://github.com/xtmingyue/storyagent
created: 2026-07-18
updated: 2026-07-18
no: 7622
category: 画龙补充 / 扩容入库 — 补充源
repo: xtmingyue/storyagent
stars: 3
url: https://github.com/xtmingyue/storyagent
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/QUICK_START.md
---

# xtmingyue/storyagent

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/xtmingyue/storyagent
- **Stars**：3
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：agent, ai, ai-writing, chinese-novel, chinese-novels, novel, novel-writing
- **GitHub 描述**：一键拆解网文连续章节为剧情片段、逐章节奏表和 Excel 拆书表
- **本地描述**：storyagent
- **拉取时间**：2026-07-25 19:28:00

---

<p align="center">
  <img src="docs/storyagent-logo.svg" width="96" alt="StoryAgent logo">
</p>

<h1 align="center">StoryAgent</h1>

<p align="center">长篇网文结构化拆书 CLI</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.7%2B-blue.svg" alt="Python 3.7+"></a>
  <a href="https://github.com/XTmingyue/StoryAgent"><img src="https://img.shields.io/badge/CLI-storyagent-1f6feb.svg" alt="StoryAgent CLI"></a>
</p>

<p align="center">
  将长篇小说拆成可阅读、可编辑、可复用的章节节奏与故事片段，导出为结构化 Markdown 和 Excel。
</p>

---

StoryAgent 面向网文拆书场景：先逐章提取章纲、节奏、故事线和亮点，再从已完成的章节拆解中滚动归纳故事片段、整体大纲与叙事循环。拆解结果可用于研究节奏、复盘爽点设计，或作为后续新小说构思的参考资料。

## 核心能力

- **单章拆解**：并行分析每一章的约 600 字章纲、章节节奏、故事线和金句/梗/爆点。
- **滚动片段提取**：按故事情节将连续章节归为片段；一个片段最多 10 章，不必等待全书拆解完成。
- **整体结构梳理**：基于故事片段生成主线、支线、剧情爽点、阶段推进和底层循环公式。
- **Excel 导出**：将多章节奏合并为单元格，和逐章分析一起输出为可阅读、可二次编辑的拆书表。
- **断点续跑**：自动跳过已完成内容；`extract --num` 可分批拆书，后续命令会接着处理尚未完成的章节。

## 拆书成果

`exports/analysis.xlsx` 包含两个工作表：

1. `拆书表`：章节序号、章节名称、多章节奏、单章节奏、单章简介、`story_line` 与 `highlights`。
2. `片段汇总`：每个故事片段的章节范围、核心事件、读者观感、情绪节奏、高潮章节和概括。

其中“多章节奏”会按同一故事片段合并单元格；“单章节奏”会突出章节核心和情绪基调，方便快速观察节奏变化。

<p align="center">
  <img src="docs/analysis-example.png" alt="StoryAgent 导出的小说拆书 Excel 示例" width="100%">
</p>
<p align="center">
  <img src="docs/analysis-example2.png" alt="StoryAgent 导出的小说拆书 Excel 示例" width="100%">
</p>

同时会导出：

- `exports/analysis.md`：可直接人工校对和编辑的拆书 Markdown。
- `exports/story_outline.md`：故事主线、支线、剧情与爽点、阶段大纲和底层循环公式。

## 工作流程

1. **章节切分**：从小说 TXT 识别并保存章节。
2. **单章拆解**：每章生成章纲、章节节奏、故事线、文章亮点。
3. **故事片段**：读取已完成的章节拆解，按情节边界归纳不超过 10 章的片段。
4. **整体大纲**：从故事片段提炼主线、支线、爽点与循环公式。
5. **导出**：生成 Markdown 与 Excel 拆书表。

## 环境要求

- Python 3.7+
- 支持 OpenAI 兼容接口的 LLM 服务，例如 DeepSeek、智谱 GLM、Kimi 等

## 安装

### 直接通过 pip 安装

```bash
pip install storyagent
```

安装完成后，`storyagent` 命令即可使用：

```bash
storyagent --help
```

### 本地开发安装

```bash
git clone https://github.com/XTmingyue/StoryAgent.git
cd StoryAgent
python -m pip install -e .
```

## 配置模型

```bash
storyagent config
```

编辑 `~/.storyagent/.env`：

```ini
STORYAGENT_MODEL=deepseek-v4-flash
STORYAGENT_BASE_URL=https://api.deepseek.com
STORYAGENT_API_KEY=your-api-key
```

也可以用同名环境变量覆盖文件配置。

## 快速开始

```bash
storyagent run 小说拆书 --txt /path/to/小说.txt --max-chapters-per-segment 10
```

命令会在当前目录创建 `workspaces/小说拆书/`，依次完成章节切分、单章拆解、故事片段、整体大纲和 Excel 导出。

```text
workspaces/小说拆书/
├── data/
│   ├── chapters.json
│   ├── chapter_extracts/
│   ├── chapter_extracts.json
│   ├── segment_plan.json
│   ├── segment_state.json
│   └── story_outline.json
└── exports/
    ├── analysis.md
    ├── analysis.xlsx
    └── story_outline.md
```

## 分步执行

```bash
# 1. 解析原始小说，不调用模型
storyagent split 小说拆书 --txt /path/to/小说.txt

# 2. 首次只拆解最靠前的 100 个未完成章节。再执行一次，会继续拆解后续 100 个未完成章节
storyagent extract 小说拆书 --num 100

# 4. 基于当前已拆解的章节，滚动提取故事片段
storyagent segments 小说拆书 --max-chapters-per-segment 10

# 5. 提取整体大纲与细纲循环
storyagent outline 小说拆书

# 6. 导出 Markdown 和 Excel
storyagent export 小说拆书
```

## 注意

需要注意要拆解的小说文件的格式是utf8编码的txt文件，如果不是可以采用命令进行转换：

```bash
iconv -f GBK -t UTF-8 小说名字.txt > 小说名字-utf8.txt
```

## 常用参数

| 参数 | 说明 |
| --- | --- |
| `--num N` | 本次拆解最靠前的 `N` 个尚未完成章节；适用于 `extract`。 |
| `--extract-batch-size N` | 每批提交给模型拆解的章节数，默认 10。 |
| `--max-workers N` | 单章拆解阶段的最大并发请求数。 |
| `--chapter-char-limit N` | 单章输入给模型的最大字符数。 |
| `--segment-load-size N` | 每轮故事片段提取新加载的章节数。 |
| `--max-chapters-per-segment N` | 单个故事片段最大章节数，默认 10。 |
| `--force` | 强制重跑当前命令对应的已有结果。 |
| `--force-extract` / `--force-segments` / `--force-outline` | 在 `run` 中只重做指定阶段。 |

## 拆解维度

### 单章内容

每章会提取四部分内容：

1. **章纲**：约 600 字的章节故事简述。
2. **章节节奏**：章节核心内容与情绪基调，例如“危机加重 + 金手指使用成功 + 战斗 + 情绪”。
3. **章节故事线**：短语链式事件流，例如“主角穿越 + 初遇危机 + 配角登场 + 世界观铺垫 + 结尾悬念”。
4. **文章亮点**：可能引发读者评论的金句、梗和爆点。

### 故事片段与大纲

- **故事片段**：归纳核心事件、读者观感、情绪节奏、高潮章节与片段概括。
- **整体大纲**：梳理故事主线、支线和“剧情 + 爽点”的阶段推进。
- **细纲循环**：提炼可重复的叙事机制，例如“危机发现 + 调查试探 + 修炼加点 + 暴力验证 + 资源收获 + 更高层威胁”。

## 命令参考

| 命令 | 说明 |
| --- | related:
  - methods/QUICK_START.md
--- |
| `storyagent config` | 创建全局模型配置文件。 |
| `storyagent list` | 列出当前工作区。 |
| `storyagent split <工作区> --txt <小说路径>` | 将 TXT 解析为章节。 |
| `storyagent extract <工作区> [--num N]` | 并行拆解单章内容。 |
| `storyagent segments <工作区>` | 基于已完成的单章拆解滚动提取故事片段。 |
| `storyagent outline <工作区>` | 生成整体大纲与细纲循环。 |
| `storyagent export <工作区>` | 导出 `analysis.md` 与 `analysis.xlsx`。 |
| `storyagent md2xlsx <工作区>` | 将已编辑的 `analysis.md` 重新转换为 Excel。 |
| `storyagent run <工作区> --txt <小说路径>` | 一键执行完整拆书流程。 |

## 关于作者

飞鸟 one the way — 探索者

<p align="left">
  <img src="docs/qrcode.png" width="400" alt="公众号二维码">
</p>

**微信公众号** · [飞鸟onTheWay](https://mp.weixin.qq.com/s/_GIBLfxKKc6VyMdx9oWhwA) 

**社交平台** · [小红书 潮声明月](https://www.xiaohongshu.com/user/profile/5668486ae4251d644618986d)· [知乎 飞鸟在路上](https://www.zhihu.com/people/05124ba329947f0f0b705c0fce66b069)

## License

`[GPL-3.0](LICENSE)`
