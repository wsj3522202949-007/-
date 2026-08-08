---
id: tool-01247
type: tool
area: 库
status: active
tags: [互动叙事, Python, 协议未明, 本地优先, 中文友好, 本地写作]
title: ai-curio-cabinet-journey
summary: 互动叙事/聊天写故事
source: https://github.com/xiajinqing29-byte/ai-curio-cabinet-journey
created: 2026-07-18
updated: 2026-07-18
no: 1247
category: 二、网文 / 长篇 AI 写作系统 库
repo: xiajinqing29-byte/ai-curio-cabinet-journey
stars: 2
url: https://github.com/xiajinqing29-byte/ai-curio-cabinet-journey
tier: "B"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 01b722cba2c5f27c
  - methods/最强写作方法论_全球最强综合版.md
---

# xiajinqing29-byte/ai-curio-cabinet-journey

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/xiajinqing29-byte/ai-curio-cabinet-journey
- **Stars**：2
- **语言**：Python
- **License**：None
- **Topics**：ai-game, chinese-game, collection-game, interactive-fiction, python-game, single-file, text-game
- **GitHub 描述**：AI-hosted Chinese interactive fiction and curio-collecting game｜AI主持的中文旅行收藏游戏
- **本地描述**：AI-hosted Chinese interactive fiction and curio-collecting game｜AI主持的中文旅行收藏游戏
- **拉取时间**：2026-07-23 23:15:27

---

# 🗄️ 珍奇柜 · 给 AI 主持的旅行收藏游戏

一款**单文件、零依赖、可存档、适合盲玩**的中文文字游戏。

选择一只珍奇柜，从它所在地区的第一座小镇出发。沿途遭遇事件、作出选择、收集散落的奇物，让空着的柜格一件件亮起来；走完六座小镇后抵达主城，五角星世界地图也将随之展开。

> 当前版本：**v0.1.0 公开测试版**  
> 推荐玩法：把盲玩文件 `curio.py` 交给支持运行 Python 的 AI，让它在不读取隐藏收藏与事件答案的前提下主持游戏。

---

## 这是什么

《珍奇柜》的核心循环很简单：

**选择柜子 → 踏上旅途 → 遭遇事件 → 作出选择 → 收藏物品 → 抵达城镇 → 点亮主城**

与普通的随机收集小游戏相比，它更重视三种感受：

- **不知道下一件是什么**：未获得的收藏不会提前显示名称与说明。
- **收藏有来历**：珍贵物品往往藏在需要选择的事件里，不只是随机掉落。
- **旅行正在前进**：每只柜子都有自己的故事、故乡路线与最终称号。

## 五种珍奇柜

| 珍奇柜 | 收藏方向 | 故乡与起点 |
|---|---|---|
| **绘彩柜** | 收藏世间未被留住的颜色 | 伊芮珐周边 · 薄暮镇 |
| **奇想柜** | 收藏奇异生灵留下的痕迹 | 弥拉维周边 · 鹿角镇 |
| **撷卷柜** | 收藏故事、寓言、歌剧与失落文字 | 维洛恩周边 · 晨钟镇 |
| **圣木柜** | 收藏古老植物与森林奇物 | 瑟尔凡周边 · 榛谷镇 |
| **长石柜** | 收藏岩层、矿石与大地隐秘 | 佩拉贡周边 · 白崖镇 |

选择后，该柜子的第一章故事会立即开始。后续章节随旅程逐步展开；错误选择不会造成永久损失，错过的事件会在之后重新回到路上。

---

## 为什么适合交给 AI 主持

- **盲玩**：`curio.py` 将物品表、事件结果与概率藏在打包内容中，只公开游戏入口。
- **独立存档**：进度保存在脚本同目录的 JSON 文件里，不依赖聊天上下文。
- **可复现**：随机状态会写入存档；相同种子与相同指令序列会得到相同结果。
- **省对话轮次**：支持 `travel 4` 连续赶路，也支持用分号一次执行多条指令。
- **对错误输入友好**：无法理解的指令只会返回提示，不会让整局游戏中断。

> 盲玩打包是为了避免普通游玩时被剧透，并不是真正的加密。刻意解包仍然能够看到隐藏内容。

---

## 仓库里有什么

| 文件 | 用途 |
|---|---|
| **`curio.py`** | 推荐下载的盲玩版。把它交给 AI，只使用 `cmd()` 与 `new_game()`。 |
| **`engine.py`** | 可读源码，包含完整事件和收藏数据，适合修改与二次开发；打开即会剧透。 |
| `build_blind.py` | 修改 `engine.py` 后，重新生成 `curio.py`。 |
| `tool-schema.json` | 将游戏接入函数调用 / Tool use 时可使用的 JSON Schema。 |
| `examples/play_with_ai.md` | 两种玩法：让 AI 主持给你玩，或让 AI 自己做旅行者。 |
| `CHANGELOG.md` | 版本更新记录。 |

`engine.py` 与 `curio.py` 是同一款游戏。前者便于阅读和修改，后者用于不剧透地游玩。

---

## 快速开始

需要 Python 3.8 或更高版本，不需要安装第三方依赖。

```python
import curio

print(curio.cmd(""))                 # 播放公共开场并显示五种柜子
print(curio.cmd("begin 撷卷柜"))     # 选择柜子
print(curio.cmd("travel"))           # 前进一步
print(curio.cmd("travel 4"))         # 连续赶路，遇到选择或抵达地点会暂停
print(curio.cmd("choose C"))         # 为当前事件作出选择
print(curio.cmd("status"))           # 查看当前状态
```

想从头开始：

```python
print(curio.new_game())               # 回到选柜界面
print(curio.new_game("圣木柜", 2026)) # 以指定种子直接开始
```

Windows 终端若无法正常显示中文或 emoji，可先启用 UTF-8，例如设置环境变量 `PYTHONUTF8=1`。

---

## 旅途规则

### 路线

每片地区由六座小镇和一座主城组成。每两处地点之间有四段路程；抵达故乡主城后，玩家可以从五角星地图选择其他四片地区。

### 事件

- **A 类**：极少出现的幸运彩蛋，带来意外之喜。
- **B / C 类**：在固定旅程节点触发的地方旧事与柜子故事。
- **D 类**：当前柜子的专属选择事件，藏着专属收藏。
- **E 类**：所有路线都可能遇到的公共选择事件。
- **F 类**：旅途中直接发现的小物品；普通 F 类最多连续出现两次。

### 魔力

收藏物品会提高魔力。魔力越高，专属事件与高品质公共事件越容易出现；刚出发时则更常遇见普通小物件。

### 跨周目防重复

重新选择另一只柜子时，新柜仍然是空的，旧物品不会继承；游戏只记住哪些公共事件已经看过，并优先展示尚未见过的内容。

### 存档

- 每条指令结束后都会进行技术性自动保存。
- 抵达小镇或主城时会建立正式存档节点。
- `save` 可以在安全地点手动建立正式节点。
- `restore` 返回最近的正式节点。
- 存档文件名为 `珍奇柜_完整版存档.json`；请不要把个人存档提交到 GitHub。

---

## 指令清单

| 指令 | 作用 |
|---|---|
| `begin` | 显示五种珍奇柜 |
| `begin <柜名>` | 选择柜子并开始旅程 |
| `travel [次数]` | 向下一站前进，最多连续执行 20 次 |
| `explore` | 在当前小镇或主城附近探索，不推进路线 |
| `choose A/B/C` | 为当前 D/E 类事件作出选择 |
| `status` | 查看地点、魔力、故事与主城进度 |
| `map` | 查看五角星世界地图 |
| `depart <主城名>` | 从主城选择下一片地区 |
| `town` | 查看当地可用功能 |
| `rumor` | 打听尚未收藏的专属珍奇线索 |
| `repair` | 请当地手艺人修补一次柜子 |
| `cabinet` | 查看已经获得的收藏 |
| `look <名称>` | 查看某件已获得物品的说明 |
| `save` | 建立正式存档节点 |
| `restore` | 返回最近的正式存档节点 |
| `help` | 查看游戏内说明 |

可以用分号或换行一次执行最多八条指令：

```python
print(curio.cmd("status; map"))
```

每次返回末尾都会附带一行紧凑状态栏，便于 AI 判断当前进度：

```text
📊 {"柜":"撷卷柜","魔力":14,"地点":"鹭羽镇","回合":13,"收藏":12,"S":0,"A":0,"B":2,"C":3,"工具":7,"主城":0,"待选择":false}
```

---

## 接到 AI 上

### 方式一：AI 可以运行 Python

把 `curio.py` 上传给 AI，然后告诉它：

> 请把这个文件作为盲玩文字游戏运行。不要解码或搜索隐藏内容；只调用 `cmd()`。先调用 `cmd("")`，把游戏文字交给我，等我决定行动后再继续。遇到 A/B/C 选择时不要替我决定。

更完整的提示词见 [`examples/play_with_ai.md`](examples/play_with_ai.md)。

### 方式二：函数调用 / Tool use

注册 `tool-schema.json` 中的 `play_curio` 工具。处理函数只需把字符串指令交给引擎：

```python
import engine

def play_curio(command: str) -> str:
    return engine.cmd(command)
```

---

## 内容规模

- 5 种珍奇柜与 5 条专属故事线
- 5 片地区、30 座小镇、5 座主城
- 40 个柜子专属选择事件
- 20 个公共选择事件
- 16 个旅途直接发现事件
- 3 种极低概率幸运彩蛋
- 111 件跨五条路线编写的收藏与工具
- 五城点亮称号、地方旧事、柜子工具与终极收藏解锁

所有未获得物品的名称、事件答案和具体奖励均不会在盲玩版中提前展示。

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 当前测试重点

v0.1.0 最希望得到以下反馈：

1. 前期普通物品与选择事件的节奏是否舒服。
2. 第二、第三只柜子的重复游玩感是否足够低。
3. 玩家是否能自然理解地图、存档和跨地区旅行。
4. 哪类收藏最让人产生“还想再走一步”的感觉。

欢迎通过 Issues 留下不剧透的体验；涉及隐藏物品或事件答案时，请在标题中标注「剧透」。

## 致谢

本项目的单文件盲玩形式、可读源码与打包版并存的仓库结构，参考了 [tutusagi/ai-fishing-game](https://github.com/tutusagi/ai-fishing-game)。感谢它展示了“让 AI 真正参与游玩”的有趣方式。

## 版权与许可

© 2026 《珍奇柜》作者。当前测试版暂未附开源许可证；在作者明确选择许可证之前，默认保留全部权利。

