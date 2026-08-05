---
id: tool-05295
type: tool
area: 库
status: active
tags: [HTML, 协议宽松, 本地优先, 中文友好, 去AI味, 本地写作]
title: SlopScan
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/gitstq/slopscan
created: 2026-07-18
updated: 2026-07-18
no: 5295
category: 一、去 AI 味 / Humanizer 库
repo: gitstq/SlopScan
stars: 0
url: https://github.com/gitstq/slopscan
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# gitstq/SlopScan

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/gitstq/slopscan
- **Stars**：0
- **语言**：HTML
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：🔍 SlopScan — AI Slop Detector & Text Purifier | AI文风检测与净化工具 — Zero Dependencies, Bilingual EN/ZH, Real-time Scoring, One-click Purification, 100% Client-Side
- **本地描述**：🔍 SlopScan — AI Slop Detector & Text Purifier （ AI文风检测与净化工具 — Zero Dependencies, Bilingual EN/ZH, Real-time Scoring, One-click Purification, 100% Client-Side
- **拉取时间**：2026-07-25 18:13:18

---

<p align="center">
  <a href="#简体中文">简体中文</a> &nbsp;|&nbsp;
  <a href="#繁體中文">繁體中文</a> &nbsp;|&nbsp;
  <a href="#english">English</a>
</p>

---

<a id="简体中文"></a>

# 🎉 SlopScan — AI 文风检测与净化工具

> **一句话介绍**：粘贴文本，秒级识别 AI 套路表达，一键净化，让你的文字回归人类质感。

## 为什么做 SlopScan？

随着大语言模型的普及，AI 生成内容随处可见。但 AI 写出来的文字往往带着一种独特的"塑料味"——堆砌填充词、滥用比喻、千篇一律的句式结构。这些被称为 **"AI Slop"** 的表达，正在侵蚀我们日常阅读和写作的质量。

**SlopScan 的核心使命**：让每一行文字都经得起推敲。

### 自研差异化亮点

- 🔬 **中英文双语原生检测**：不是简单翻译规则，而是分别针对中英文语境独立构建的检测词库与匹配策略
- 🧠 **7 大检测类别**：覆盖填充词、陈词滥调、模糊措辞、夸张表达、冗余表达、滥用比喻、结构套路，远超同类工具
- ⚡ **零依赖、单文件运行**：纯 HTML/CSS/JS 实现，无需安装任何依赖，下载即用
- 🎯 **实时评分 + 可视化高亮**：边写边查，问题一目了然
- 🛡️ **100% 客户端运行**：你的文本永远不会离开你的浏览器

---

## ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🔍 **智能检测** | 基于自研词库引擎，精准识别 7 大类 AI 套路表达 |
| 🌐 **双语支持** | 原生支持中文和英文文本检测，自动识别语言 |
| 📊 **实时评分** | 0-10 分套路评分体系，量化文风"AI 味"浓度 |
| 🎨 **可视化高亮** | 不同类别用不同颜色标注，悬停即可查看详情与替换建议 |
| 🧹 **一键净化** | 自动移除检测到的套路表达，瞬间提升文本纯净度 |
| 📤 **多格式导出** | 支持 **TXT**、**JSON**、**Markdown** 三种格式导出检测结果 |
| 🌗 **暗色/亮色主题** | 内置双主题切换，适配不同使用场景与个人偏好 |
| 🔒 **隐私优先** | 纯客户端运算，**零数据上传**，你的文本只属于你 |
| 📱 **响应式设计** | 完美适配桌面端和移动端，随时随地检测 |
| 🚀 **零依赖部署** | 单个 HTML 文件，无需构建工具、无需服务器，下载即用 |

---

## 🚀 快速开始

### 环境要求

> 只需要一个现代浏览器。没有其他前置条件。

| 浏览器 | 最低版本 |
|--------|---------|
| Chrome | 80+ |
| Firefox | 78+ |
| Safari | 14+ |
| Edge | 80+ |

### 安装与启动

**方式一：直接打开（推荐）**

```bash
# 克隆仓库
git clone https://github.com/gitstq/SlopScan.git

# 用浏览器打开 index.html
# macOS
open SlopScan/index.html

# Linux
xdg-open SlopScan/index.html

# Windows
start SlopScan/index.html
```

**方式二：本地服务器**

```bash
# 克隆仓库
git clone https://github.com/gitstq/SlopScan.git
cd SlopScan

# 使用任意静态服务器（可选，直接打开 HTML 也完全可以）
python3 -m http.server 8080
# 然后访问 http://localhost:8080
```

**方式三：在线使用**

直接访问 GitHub Pages（如果已启用），或下载 `index.html` 后双击打开。

---

## 📖 详细使用指南

### 基本流程

1. **粘贴或输入文本**：将待检测的文本粘贴到输入区域
2. **自动检测**：SlopScan 会实时分析文本并高亮标注问题表达
3. **查看评分**：顶部仪表盘显示套路评分（0-10 分）和纯净度百分比
4. **浏览详情**：悬停在高亮文本上，查看所属类别和替换建议
5. **筛选类别**：使用类别过滤器，聚焦你关心的特定问题类型
6. **一键净化**：点击净化按钮，自动移除所有检测到的套路表达
7. **导出结果**：选择 TXT / JSON / Markdown 格式导出

### 进阶技巧

- **对比检测**：先检测原文，净化后再检测一次，对比评分变化
- **针对性优化**：关闭不需要的类别过滤器，集中处理某一类问题
- **写作辅助**：边写边检测，实时避免 AI 套路表达

### 典型使用场景

| 场景 | 说明 |
|------|------|
| ✍️ **内容创作** | 润色 AI 辅助生成的初稿，去除机器味 |
| 📝 **学术写作** | 确保论文语言精炼、表达准确 |
| 📧 **商务沟通** | 让邮件和报告更专业、更有说服力 |
| 📱 **社交媒体** | 提升文案质量，告别千篇一律 |
| 🎓 **教学评估** | 检测学生作业是否存在过度依赖 AI 的痕迹 |

---

## 📊 检测类别

SlopScan 内置 **7 大检测类别**，全面覆盖 AI 生成文本中的常见问题：

| # | 类别 | 图标 | 说明 | 示例 |
|---|------|------|------|------|
| 1 | **填充词** | 🟡 | 不增加任何意义的填充短语，徒增篇幅 | "值得注意的是"、"需要指出的是"、"It's important to note that" |
| 2 | **陈词滥调** | 🔴 | 被过度使用的流行语和陈旧表达 | "至关重要"、"携手共进"、"In today's rapidly evolving landscape" |
| 3 | **模糊措辞** | 🟣 | 模糊、不明确的语言，削弱表达的力度 | "在一定程度上"、"某种意义上"、"to some extent" |
| 4 | **夸张表达** | 🩷 | 极端的夸张，过度夸大陈述 | "前所未有"、"颠覆性"、"revolutionary"、"game-changing" |
| 5 | **冗余表达** | 🔵 | 包含不必要重复的表达 | "未来前景"、"免费赠送"、"future prospects" |
| 6 | **滥用比喻** | 🟠 | 被用滥了的比喻和类比 | "如同打开了潘多拉魔盒"、"编织了一张大网"、"tapestry of" |
| 7 | **结构套路** | 🟢 | AI 输出中典型的公式化句式结构 | "总而言之...综上所述..."、"Let's dive in..." |

> 💡 每个类别都配备了中英文双语词库，并持续更新迭代。

---

## 💡 评分系统

### Slop Score（套路评分）

SlopScan 采用 **0-10 分**的评分体系，分数越高表示文本中 AI 套路表达越多：

| 分数区间 | 等级 | 颜色 | 含义 |
|----------|------|------|------|
| **0 - 3** | 🟢 优良 | 绿色 | 文本自然流畅，几乎无 AI 套路痕迹 |
| **4 - 6** | 🟡 一般 | 黄色 | 存在一定数量的套路表达，建议优化 |
| **7 - 10** | 🔴 严重 | 红色 | AI 味浓厚，强烈建议净化处理 |

### 评分算法

评分基于以下因素综合计算：

- **检测命中数量**：命中的套路表达越多，分数越高
- **文本长度标准化**：按每 1000 字符标准化，避免长文本天然得分偏高
- **对数缩放**：采用对数函数映射，使评分分布更加合理和细腻

---

## 📦 导出功能

SlopScan 支持三种格式导出检测结果：

### TXT 格式

纯文本格式，适合快速查阅和分享：

```
SlopScan 检测报告
==================
评分: 6.5/10
纯净度: 72%
字数: 1,234

检测结果:
- [填充词] "值得注意的是" → 建议删除
- [陈词滥调] "至关重要" → 建议替换为"重要"
...
```

### JSON 格式

结构化数据格式，适合程序化处理和二次分析：

```json
{
  "score": 6.5,
  "purity": 72,
  "wordCount": 1234,
  "language": "zh",
  "findings": [
    {
      "text": "值得注意的是",
      "category": "filler",
      "suggestion": "建议删除",
      "position": [12, 19]
    }
  ]
}
```

### Markdown 格式

Markdown 格式，适合文档归档和知识管理：

```markdown
# SlopScan 检测报告

| 项目 | 数值 |
|------|------|
| 评分 | 6.5/10 |
| 纯净度 | 72% |
| 字数 | 1,234 |

## 检测结果
- **[填充词]** "值得注意的是" → 建议删除
- **[陈词滥调]** "至关重要" → 建议替换为"重要"
```

---

## 🔒 隐私说明

> **你的文本，只属于你。**

SlopScan 的所有检测、评分、净化逻辑 **100% 在浏览器客户端完成**：

- ❌ **不发送任何数据到服务器** — 没有后端 API 调用
- ❌ **不使用任何第三方追踪服务** — 无 Analytics、无 Cookie 追踪
- ❌ **不存储任何文本数据** — 关闭页面即清空，不留痕迹
- ✅ **完全离线可用** — 下载 HTML 文件后，断网也能正常使用

---

## 🤝 贡献指南

我们欢迎并感谢所有形式的贡献！

### 提交 PR

1. **Fork** 本仓库
2. 创建特性分支：`git checkout -b feature/your-feature-name`
3. 提交改动：`git commit -m 'feat: 添加某功能'`
4. 推送分支：`git push origin feature/your-feature-name`
5. 提交 **Pull Request**

**Commit 规范**：

| 前缀 | 用途 |
|------|------|
| `feat:` | 新功能 |
| `fix:` | 修复 Bug |
| `docs:` | 文档更新 |
| `style:` | 代码格式调整 |
| `refactor:` | 代码重构 |
| `test:` | 测试相关 |
| `chore:` | 构建/工具链相关 |

### 提交 Issue

- 🐛 **Bug 反馈**：请附上浏览器版本、操作系统和复现步骤
- 💡 **功能建议**：描述你的使用场景和期望行为
- 📝 **词库补充**：欢迎提交新的 AI 套路表达样本，帮助我们完善检测词库

---

## 📄 开源协议

本项目基于 `[MIT License](LICENSE)` 开源。

```
MIT License

Copyright (c) 2026 SlopScan Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a> &amp; Contributors
</p>

---

<a id="繁體中文"></a>

# 🎉 SlopScan — AI 文風偵測與淨化工具

> **一句話介紹**：貼上文字，秒級識別 AI 套路表達，一鍵淨化，讓你的文字回歸人類質感。

## 為什麼做 SlopScan？

隨著大型語言模型的普及，AI 生成內容隨處可見。但 AI 寫出來的文字往往帶著一種獨特的「塑膠味」——堆砌填充詞、濫用比喻、千篇一律的句式結構。這些被稱為 **「AI Slop」** 的表達，正在侵蝕我們日常閱讀和寫作的品質。

**SlopScan 的核心使命**：讓每一行文字都經得起推敲。

### 自研差異化亮點

- 🔬 **中英文雙語原生偵測**：不是簡單翻譯規則，而是分別針對中英文語境獨立構建的偵測詞庫與匹配策略
- 🧠 **7 大偵測類別**：覆蓋填充詞、陳詞濫調、模糊措辭、誇張表達、冗餘表達、濫用比喻、結構套路，遠超同類工具
- ⚡ **零依賴、單檔案運行**：純 HTML/CSS/JS 實現，無需安裝任何依賴，下載即用
- 🎯 **即時評分 + 視覺化標記**：邊寫邊查，問題一目了然
- 🛡️ **100% 客戶端運行**：你的文字永遠不會離開你的瀏覽器

---

## ✨ 核心特性

| 特性 | 說明 |
|------|------|
| 🔍 **智慧偵測** | 基於自研詞庫引擎，精準識別 7 大類 AI 套路表達 |
| 🌐 **雙語支援** | 原生支援中文和英文文字偵測，自動識別語言 |
| 📊 **即時評分** | 0-10 分套路評分體系，量化文風「AI 味」濃度 |
| 🎨 **視覺化標記** | 不同類別用不同顏色標註，懸停即可查看詳情與替換建議 |
| 🧹 **一鍵淨化** | 自動移除偵測到的套路表達，瞬間提升文字純淨度 |
| 📤 **多格式匯出** | 支援 **TXT**、**JSON**、**Markdown** 三種格式匯出偵測結果 |
| 🌗 **暗色/亮色主題** | 內建雙主題切換，適配不同使用場景與個人偏好 |
| 🔒 **隱私優先** | 純客戶端運算，**零資料上傳**，你的文字只屬於你 |
| 📱 **響應式設計** | 完美適配桌面端和行動端，隨時隨地偵測 |
| 🚀 **零依賴部署** | 單個 HTML 檔案，無需建置工具、無需伺服器，下載即用 |

---

## 🚀 快速開始

### 環境需求

> 只需要一個現代瀏覽器。沒有其他前置條件。

| 瀏覽器 | 最低版本 |
|--------|---------|
| Chrome | 80+ |
| Firefox | 78+ |
| Safari | 14+ |
| Edge | 80+ |

### 安裝與啟動

**方式一：直接開啟（推薦）**

```bash
# 複製倉庫
git clone https://github.com/gitstq/SlopScan.git

# 用瀏覽器開啟 index.html
# macOS
open SlopScan/index.html

# Linux
xdg-open SlopScan/index.html

# Windows
start SlopScan/index.html
```

**方式二：本地伺服器**

```bash
# 複製倉庫
git clone https://github.com/gitstq/SlopScan.git
cd SlopScan

# 使用任意靜態伺服器（可選，直接開啟 HTML 也完全可以）
python3 -m http.server 8080
# 然後造訪 http://localhost:8080
```

**方式三：線上使用**

直接造訪 GitHub Pages（若已啟用），或下載 `index.html` 後雙擊開啟。

---

## 📖 詳細使用指南

### 基本流程

1. **貼上或輸入文字**：將待偵測的文字貼到輸入區域
2. **自動偵測**：SlopScan 會即時分析文字並標記問題表達
3. **查看評分**：頂部儀表板顯示套路評分（0-10 分）和純淨度百分比
4. **瀏覽詳情**：懸停在標記文字上，查看所屬類別和替換建議
5. **篩選類別**：使用類別過濾器，聚焦你關心的特定問題類型
6. **一鍵淨化**：點擊淨化按鈕，自動移除所有偵測到的套路表達
7. **匯出結果**：選擇 TXT / JSON / Markdown 格式匯出

### 進階技巧

- **對比偵測**：先偵測原文，淨化後再偵測一次，對比評分變化
- **針對性優化**：關閉不需要的類別過濾器，集中處理某一類問題
- **寫作輔助**：邊寫邊偵測，即時避免 AI 套路表達

### 典型使用場景

| 場景 | 說明 |
|------|------|
| ✍️ **內容創作** | 潤飾 AI 輔助生成的初稿，去除機器味 |
| 📝 **學術寫作** | 確保論文語言精煉、表達準確 |
| 📧 **商務溝通** | 讓郵件和報告更專業、更有說服力 |
| 📱 **社群媒體** | 提升文案品質，告別千篇一律 |
| 🎓 **教學評估** | 偵測學生作業是否存在過度依賴 AI 的痕跡 |

---

## 📊 偵測類別

SlopScan 內建 **7 大偵測類別**，全面覆蓋 AI 生成文字中的常見問題：

| # | 類別 | 圖示 | 說明 | 範例 |
|---|------|------|------|------|
| 1 | **填充詞** | 🟡 | 不增加任何意義的填充短語，徒增篇幅 | 「值得注意的是」、「需要指出的是」、「It's important to note that」 |
| 2 | **陳詞濫調** | 🔴 | 被過度使用的流行語和陳舊表達 | 「至關重要」、「攜手共進」、「In today's rapidly evolving landscape」 |
| 3 | **模糊措辭** | 🟣 | 模糊、不明確的語言，削弱表達的力度 | 「在一定程度上」、「某種意義上」、「to some extent」 |
| 4 | **誇張表達** | 🩷 | 極端的誇張，過度誇大陳述 | 「前所未有」、「顛覆性」、「revolutionary」、「game-changing」 |
| 5 | **冗餘表達** | 🔵 | 包含不必要重複的表達 | 「未來前景」、「免費贈送」、「future prospects」 |
| 6 | **濫用比喻** | 🟠 | 被用濫了的比喻和類比 | 「如同打開了潘朵拉魔盒」、「編織了一張大網」、「tapestry of」 |
| 7 | **結構套路** | 🟢 | AI 輸出中典型的公式化句式結構 | 「總而言之...綜上所述...」、「Let's dive in...」 |

> 💡 每個類別都配備了中英文雙語詞庫，並持續更新迭代。

---

## 💡 評分系統

### Slop Score（套路評分）

SlopScan 採用 **0-10 分**的評分體系，分數越高表示文字中 AI 套路表達越多：

| 分數區間 | 等級 | 顏色 | 含義 |
|----------|------|------|------|
| **0 - 3** | 🟢 優良 | 綠色 | 文字自然流暢，幾乎無 AI 套路痕跡 |
| **4 - 6** | 🟡 一般 | 黃色 | 存在一定數量的套路表達，建議優化 |
| **7 - 10** | 🔴 嚴重 | 紅色 | AI 味濃厚，強烈建議淨化處理 |

### 評分演算法

評分基於以下因素綜合計算：

- **偵測命中數量**：命中的套路表達越多，分數越高
- **文字長度標準化**：按每 1000 字元標準化，避免長文字天然得分偏高
- **對數縮放**：採用對數函數映射，使評分分布更加合理和細膩

---

## 📦 匯出功能

SlopScan 支援三種格式匯出偵測結果：

### TXT 格式

純文字格式，適合快速查閱和分享：

```
SlopScan 偵測報告
==================
評分: 6.5/10
純淨度: 72%
字數: 1,234

偵測結果:
- [填充詞] 「值得注意的是」 → 建議刪除
- [陳詞濫調] 「至關重要」 → 建議替換為「重要」
...
```

### JSON 格式

結構化資料格式，適合程式化處理和二次分析：

```json
{
  "score": 6.5,
  "purity": 72,
  "wordCount": 1234,
  "language": "zh",
  "findings": [
    {
      "text": "值得注意的是",
      "category": "filler",
      "suggestion": "建議刪除",
      "position": [12, 19]
    }
  ]
}
```

### Markdown 格式

Markdown 格式，適合文件歸檔和知識管理：

```markdown
# SlopScan 偵測報告

| 項目 | 數值 |
|------|------|
| 評分 | 6.5/10 |
| 純淨度 | 72% |
| 字數 | 1,234 |

## 偵測結果
- **[填充詞]** 「值得注意的是」 → 建議刪除
- **[陳詞濫調]** 「至關重要」 → 建議替換為「重要」
```

---

## 🔒 隱私說明

> **你的文字，只屬於你。**

SlopScan 的所有偵測、評分、淨化邏輯 **100% 在瀏覽器客戶端完成**：

- ❌ **不發送任何資料到伺服器** — 沒有後端 API 呼叫
- ❌ **不使用任何第三方追蹤服務** — 無 Analytics、無 Cookie 追蹤
- ❌ **不儲存任何文字資料** — 關閉頁面即清空，不留痕跡
- ✅ **完全離線可用** — 下載 HTML 檔案後，斷網也能正常使用

---

## 🤝 貢獻指南

我們歡迎並感謝所有形式的貢獻！

### 提交 PR

1. **Fork** 本倉庫
2. 建立特性分支：`git checkout -b feature/your-feature-name`
3. 提交變更：`git commit -m 'feat: 新增某功能'`
4. 推送分支：`git push origin feature/your-feature-name`
5. 提交 **Pull Request**

**Commit 規範**：

| 前綴 | 用途 |
|------|------|
| `feat:` | 新功能 |
| `fix:` | 修復 Bug |
| `docs:` | 文件更新 |
| `style:` | 程式碼格式調整 |
| `refactor:` | 程式碼重構 |
| `test:` | 測試相關 |
| `chore:` | 建置/工具鏈相關 |

### 提交 Issue

- 🐛 **Bug 回報**：請附上瀏覽器版本、作業系統和重現步驟
- 💡 **功能建議**：描述你的使用場景和期望行為
- 📝 **詞庫補充**：歡迎提交新的 AI 套路表達樣本，幫助我們完善偵測詞庫

---

## 📄 開源協議

本專案基於 `[MIT License](LICENSE)` 開源。

```
MIT License

Copyright (c) 2026 SlopScan Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a> &amp; Contributors
</p>

---

<a id="english"></a>

# 🎉 SlopScan — AI Slop Detector & Text Purifier

> **One-liner**: Paste your text, detect AI-generated slop in seconds, purify with one click, and bring the human touch back to your writing.

## Why SlopScan?

With the rise of large language models, AI-generated content is everywhere. But AI-written text often carries a distinct "plastic flavor" — stuffed with filler words, overused metaphors, and formulaic sentence structures. These expressions, known as **"AI Slop"**, are degrading the quality of everything we read and write.

**SlopScan's core mission**: Make every line of text worth reading.

### What Sets Us Apart

- 🔬 **Native bilingual detection** — Independent detection lexicons and matching strategies built separately for Chinese and English contexts, not just translated rules
- 🧠 **7 detection categories** — Covering filler words, clichés, hedging, hyperbole, redundancy, overused metaphors, and structural slop — far beyond similar tools
- ⚡ **Zero dependencies, single-file deployment** — Pure HTML/CSS/JS, no build tools or server required, download and run
- 🎯 **Real-time scoring & visual highlighting** — Catch issues as you write, with problems visible at a glance
- 🛡️ **100% client-side operation** — Your text never leaves your browser

---

## ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🔍 **Smart Detection** | Custom-built lexicon engine for precise identification of 7 categories of AI slop |
| 🌐 **Bilingual Support** | Native Chinese and English text detection with automatic language identification |
| 📊 **Real-time Scoring** | 0-10 Slop Score system that quantifies the concentration of AI-generated patterns |
| 🎨 **Visual Highlighting** | Color-coded annotations by category; hover for details and replacement suggestions |
| 🧹 **One-Click Purify** | Automatically remove all detected slop expressions and boost text purity instantly |
| 📤 **Multi-format Export** | Export results in **TXT**, **JSON**, or **Markdown** format |
| 🌗 **Dark / Light Themes** | Built-in theme toggle to match your environment and preference |
| 🔒 **Privacy First** | All processing happens client-side — **zero data uploads** |
| 📱 **Responsive Design** | Works seamlessly on desktop and mobile devices |
| 🚀 **Zero-dependency Deployment** | A single HTML file — no build tools, no server, just open and go |

---

## 🚀 Quick Start

### Requirements

> All you need is a modern browser. Nothing else.

| Browser | Minimum Version |
|---------|----------------|
| Chrome | 80+ |
| Firefox | 78+ |
| Safari | 14+ |
| Edge | 80+ |

### Installation & Launch

**Option 1: Open directly (Recommended)**

```bash
# Clone the repository
git clone https://github.com/gitstq/SlopScan.git

# Open index.html in your browser
# macOS
open SlopScan/index.html

# Linux
xdg-open SlopScan/index.html

# Windows
start SlopScan/index.html
```

**Option 2: Local server**

```bash
# Clone the repository
git clone https://github.com/gitstq/SlopScan.git
cd SlopScan

# Use any static file server (optional — opening the HTML directly works fine too)
python3 -m http.server 8080
# Then visit http://localhost:8080
```

**Option 3: Use online**

Visit the GitHub Pages site (if enabled), or simply download `index.html` and double-click to open.

---

## 📖 Detailed Usage Guide

### Basic Workflow

1. **Paste or type text** — Drop the text you want to check into the input area
2. **Automatic detection** — SlopScan analyzes your text in real time and highlights problematic expressions
3. **Check your score** — The dashboard at the top shows your Slop Score (0-10) and purity percentage
4. **Inspect details** — Hover over highlighted text to see the category and replacement suggestions
5. **Filter by category** — Use the category filters to focus on specific types of issues
6. **One-click purify** — Click the purify button to automatically remove all detected slop
7. **Export results** — Choose from TXT / JSON / Markdown formats

### Pro Tips

- **Before & after comparison** — Detect the original text, purify it, then detect again to see the score improvement
- **Targeted optimization** — Disable categories you don't care about and focus on one issue type at a time
- **Writing assistant mode** — Detect as you write to avoid AI slop patterns in real time

### Common Use Cases

| Scenario | Description |
|----------|-------------|
| ✍️ **Content Creation** | Polish AI-assisted drafts and strip away the robotic feel |
| 📝 **Academic Writing** | Ensure your papers are concise and precisely worded |
| 📧 **Business Communication** | Make emails and reports more professional and persuasive |
| 📱 **Social Media** | Elevate your copy quality and stand out from the crowd |
| 🎓 **Education & Assessment** | Detect whether student submissions show signs of over-reliance on AI |

---

## 📊 Detection Categories

SlopScan includes **7 detection categories**, comprehensively covering common issues in AI-generated text:

| # | Category | Color | Description | Examples |
|---|----------|-------|-------------|----------|
| 1 | **Filler Words** | 🟡 | Unnecessary filler phrases that add no meaning | "It's important to note that", "It is worth mentioning", "值得注意的是" |
| 2 | **Clichés** | 🔴 | Overused buzzwords and tired expressions | "In today's rapidly evolving landscape", "Synergy", "至关重要" |
| 3 | **Hedging** | 🟣 | Vague, non-committal language that weakens statements | "To some extent", "In a certain sense", "在一定程度上" |
| 4 | **Hyperbole** | 🩷 | Extreme exaggerations that overstate claims | "Revolutionary", "Game-changing", "前所未有" |
| 5 | **Redundancy** | 🔵 | Expressions with unnecessary repetition | "Future prospects", "Free gift", "未来前景" |
| 6 | **Overused Metaphors** | 🟠 | Metaphors and analogies that have been used to death | "Tapestry of", "Unlocking potential", "编织了一张大网" |
| 7 | **Structural Slop** | 🟢 | Formulaic sentence structures typical of AI output | "Let's dive in...", "In conclusion...", "总而言之...综上所述..." |

> 💡 Each category is backed by a dedicated bilingual lexicon that is continuously updated and expanded.

---

## 💡 Scoring System

### Slop Score

SlopScan uses a **0-10 scale** — the higher the score, the more AI slop patterns detected in your text:

| Score Range | Grade | Color | Meaning |
|-------------|-------|-------|---------|
| **0 - 3** | 🟢 Excellent | Green | Text reads naturally with minimal AI slop detected |
| **4 - 6** | 🟡 Fair | Yellow | Some slop patterns present; optimization recommended |
| **7 - 10** | 🔴 Severe | Red | Heavy AI-generated patterns; purification strongly recommended |

### Scoring Algorithm

The score is calculated based on a combination of factors:

- **Hit count** — More detected slop expressions result in a higher score
- **Length normalization** — Standardized per 1,000 characters to prevent longer texts from scoring disproportionately higher
- **Logarithmic scaling** — A logarithmic function maps raw counts to scores for a more nuanced and balanced distribution

---

## 📦 Export

SlopScan supports three export formats for your detection results:

### TXT Format

Plain text format, ideal for quick review and sharing:

```
SlopScan Detection Report
==========================
Score: 6.5/10
Purity: 72%
Word Count: 1,234

Findings:
- [Filler Words] "It's important to note that" → Suggest removing
- [Clichés] "In today's rapidly evolving landscape" → Suggest replacing
...
```

### JSON Format

Structured data format, ideal for programmatic processing and further analysis:

```json
{
  "score": 6.5,
  "purity": 72,
  "wordCount": 1234,
  "language": "en",
  "findings": [
    {
      "text": "It's important to note that",
      "category": "filler",
      "suggestion": "Suggest removing",
      "position": [12, 40]
    }
  ]
}
```

### Markdown Format

Markdown format, ideal for documentation and knowledge management:

```markdown
# SlopScan Detection Report

| Metric | Value |
|--------|-------|
| Score | 6.5/10 |
| Purity | 72% |
| Word Count | 1,234 |

## Findings
- **[Filler Words]** "It's important to note that" → Suggest removing
- **[Clichés]** "In today's rapidly evolving landscape" → Suggest replacing
```

---

## 🔒 Privacy

> **Your text belongs to you. Period.**

All detection, scoring, and purification logic in SlopScan runs **100% on the client side in your browser**:

- ❌ **No data sent to any server** — There are no backend API calls
- ❌ **No third-party tracking** — No analytics, no cookie tracking
- ❌ **No text data stored** — Close the tab and everything is gone
- ✅ **Fully offline-capable** — Download the HTML file and use it without an internet connection

---

## 🤝 Contributing

We welcome and appreciate contributions of all kinds!

### Submitting a PR

1. **Fork** this repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'feat: add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a **Pull Request**

**Commit Convention**:

| Prefix | Purpose |
|--------|---------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation update |
| `style:` | Code formatting |
| `refactor:` | Code refactoring |
| `test:` | Test-related |
| `chore:` | Build / tooling |

### Opening an Issue

- 🐛 **Bug reports** — Please include your browser version, OS, and steps to reproduce
- 💡 **Feature requests** — Describe your use case and expected behavior
- 📝 **Lexicon contributions** — Submit new AI slop expression samples to help us improve detection coverage

---

## 📄 License

This project is released under the `[MIT License](LICENSE)`.

```
MIT License

Copyright (c) 2026 SlopScan Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

<p align="center">
  Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a> &amp; Contributors
</p>
