---
id: tool-01875
type: tool
area: 库
status: active
tags: [去AI味, 协议未明, 本地优先, 中文友好, 本地写作]
title: AI-taste-research
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/show940125/ai-taste-research
created: 2026-07-18
updated: 2026-07-18
no: 1875
category: 二、网文 / 长篇 AI 写作系统 库
repo: show940125/AI-taste-research
stars: 0
url: https://github.com/show940125/ai-taste-research
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# show940125/AI-taste-research

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/show940125/ai-taste-research
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Research on Chinese AI writing patterns, translationese, and anti-AI-taste prompt design
- **本地描述**：Research on Chinese AI writing patterns, translationese, and anti-AI-taste prompt design
- **拉取时间**：2026-07-23 23:33:39

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI-taste-research

一個「中文模板味／AI 味」研究案的工作底稿與執行框架。主場景鎖定 `OpenAI/Claude` 的中文論說／評論文輸出，核心問題有三個：

- 模型輸出的模板味，哪些是一般同質化，哪些帶有英譯中殘影。
- 這些症狀能不能拆成可診斷、可評分、可改寫的指標。
- 哪一種 prompt 介入法，最能穩定壓低 AI 味，又不把文本修成另一種「表演味」。

## 目前的執行口徑

第一輪正式結果採 `subagent-run`。原因很簡單：不想多花錢。

這代表兩件事：

- 第一輪比較仍然有效，因為 prompt 條件、題組、評分欄位都固定。
- 第一輪結果是基於「subagent writer backend」(使用GPT-5.4 mini 模型)下的正式比較結果。
- 目前已完成一個正式子集：8 題、24 份正式輸出、24 份盲評版；範圍見 [第一輪正式結果說明.md](https://github.com/show940125/AI-taste-research/blob/main/03-%E9%A1%8C%E7%B5%84%E8%88%87%E8%A9%95%E4%BC%B0/%E7%AC%AC%E4%B8%80%E8%BC%AA%E6%AD%A3%E5%BC%8F%E7%B5%90%E6%9E%9C%E8%AA%AA%E6%98%8E.md)。

## 先看哪裡

- 主報告：[01-報告/AI模板味研究總報告.md](https://github.com/show940125/AI-taste-research/blob/main/01-%E5%A0%B1%E5%91%8A/AI%E6%A8%A1%E6%9D%BF%E5%91%B3%E7%A0%94%E7%A9%B6%E7%B8%BD%E5%A0%B1%E5%91%8A.md)
- 特徵表：[02-框架/AI味特徵表.md](https://github.com/show940125/AI-taste-research/blob/main/02-%E6%A1%86%E6%9E%B6/AI%E5%91%B3%E7%89%B9%E5%BE%B5%E8%A1%A8.md)
- Prompt 模型：[02-框架/anti-AI-prompt模型規格.md](https://github.com/show940125/AI-taste-research/blob/main/02-%E6%A1%86%E6%9E%B6/anti-AI-prompt%E6%A8%A1%E5%9E%8B%E8%A6%8F%E6%A0%BC.md)
- 正式 prompt 入口：[02-框架/正式anti-AI味prompt模板.md](https://github.com/show940125/AI-taste-research/blob/main/02-%E6%A1%86%E6%9E%B6/%E6%AD%A3%E5%BC%8Fanti-AI%E5%91%B3prompt%E6%A8%A1%E6%9D%BF.md)
- 融合穩健版模板：[02-框架/融合穩健版anti-AI味prompt模板.md](https://github.com/show940125/AI-taste-research/blob/main/02-%E6%A1%86%E6%9E%B6/%E8%9E%8D%E5%90%88%E7%A9%A9%E5%81%A5%E7%89%88anti-AI%E5%91%B3prompt%E6%A8%A1%E6%9D%BF.md)
- 強力 pivot 版模板：[02-框架/強力pivot版anti-AI味prompt模板.md](https://github.com/show940125/AI-taste-research/blob/main/02-%E6%A1%86%E6%9E%B6/%E5%BC%B7%E5%8A%9Bpivot%E7%89%88anti-AI%E5%91%B3prompt%E6%A8%A1%E6%9D%BF.md)
- 第一輪模板包：[02-框架/第一輪Prompt模板包.md](https://github.com/show940125/AI-taste-research/blob/main/02-%E6%A1%86%E6%9E%B6/%E7%AC%AC%E4%B8%80%E8%BC%AAPrompt%E6%A8%A1%E6%9D%BF%E5%8C%85.md)
- 題組與評估：[03-題組與評估/題組與評估框架.md](https://github.com/show940125/AI-taste-research/blob/main/03-%E9%A1%8C%E7%B5%84%E8%88%87%E8%A9%95%E4%BC%B0/%E9%A1%8C%E7%B5%84%E8%88%87%E8%A9%95%E4%BC%B0%E6%A1%86%E6%9E%B6.md)
- 第一輪題組：[03-題組與評估/第一輪探索題組.md](https://github.com/show940125/AI-taste-research/blob/main/03-%E9%A1%8C%E7%B5%84%E8%88%87%E8%A9%95%E4%BC%B0/%E7%AC%AC%E4%B8%80%E8%BC%AA%E6%8E%A2%E7%B4%A2%E9%A1%8C%E7%B5%84.md)
- 第一輪 runbook：[03-題組與評估/第一輪執行runbook.md](https://github.com/show940125/AI-taste-research/blob/main/03-%E9%A1%8C%E7%B5%84%E8%88%87%E8%A9%95%E4%BC%B0/%E7%AC%AC%E4%B8%80%E8%BC%AA%E5%9F%B7%E8%A1%8Crunbook.md)
- 第一輪 manifest：[03-題組與評估/第一輪最小矩陣_manifest.csv](https://github.com/show940125/AI-taste-research/blob/main/03-%E9%A1%8C%E7%B5%84%E8%88%87%E8%A9%95%E4%BC%B0/%E7%AC%AC%E4%B8%80%E8%BC%AA%E6%9C%80%E5%B0%8F%E7%9F%A9%E9%99%A3_manifest.csv)
- 第一輪正式結果說明：[03-題組與評估/第一輪正式結果說明.md](https://github.com/show940125/AI-taste-research/blob/main/03-%E9%A1%8C%E7%B5%84%E8%88%87%E8%A9%95%E4%BC%B0/%E7%AC%AC%E4%B8%80%E8%BC%AA%E6%AD%A3%E5%BC%8F%E7%B5%90%E6%9E%9C%E8%AA%AA%E6%98%8E.md)
- 第一輪正式結果 manifest：[03-題組與評估/第一輪正式結果_manifest.csv](https://github.com/show940125/AI-taste-research/blob/main/03-%E9%A1%8C%E7%B5%84%E8%88%87%E8%A9%95%E4%BC%B0/%E7%AC%AC%E4%B8%80%E8%BC%AA%E6%AD%A3%E5%BC%8F%E7%B5%90%E6%9E%9C_manifest.csv)
- 第一輪結果初步分析：[03-題組與評估/第一輪結果初步分析.md](https://github.com/show940125/AI-taste-research/blob/main/03-%E9%A1%8C%E7%B5%84%E8%88%87%E8%A9%95%E4%BC%B0/%E7%AC%AC%E4%B8%80%E8%BC%AA%E7%B5%90%E6%9E%9C%E5%88%9D%E6%AD%A5%E5%88%86%E6%9E%90.md)
- 評分模板：[03-題組與評估/評分記錄模板.csv](https://github.com/show940125/AI-taste-research/blob/main/03-%E9%A1%8C%E7%B5%84%E8%88%87%E8%A9%95%E4%BC%B0/%E8%A9%95%E5%88%86%E8%A8%98%E9%8C%84%E6%A8%A1%E6%9D%BF.csv)
- Heuristics 附錄：[04-附錄/humanizer與維基heuristics附錄.md](https://github.com/show940125/AI-taste-research/blob/main/04-%E9%99%84%E9%8C%84/humanizer%E8%88%87%E7%B6%AD%E5%9F%BAheuristics%E9%99%84%E9%8C%84.md)

## 建議使用順序

1. 先讀主報告，抓研究判斷與文獻脈絡。
2. 再讀特徵表，知道診斷欄位怎麼分層。
3. 接著看 prompt 模型規格，理解五組條件與研究設計。
4. 真要拿去寫，先用正式 prompt 入口；一般場景優先用融合穩健版，英譯中與抽象說理題再用強力 pivot 版。
5. 若要直接開跑測試，再看第一輪模板包、第一輪題組與 runbook。
6. 最後用題組與評估框架，加上 `評分記錄模板.csv` 開始做 A/B 測試。

## 目前研究包包含什麼

- 一份整合文獻、翻譯學脈絡、維基觀察與 `humanizer` 規則的主研究報告。
- 一份六層 AI 味特徵表：詞彙、句法、篇章、翻譯腔、互動殘影、樣式。
- 一套 prompt 介入法：`baseline`、`persona-only`、`few-shot-only`、`rewrite-pipeline`、`classical/vernacular pivot pipeline`。
- 一組可直接投入實作的正式 prompt 模板，另拆成融合穩健版與強力 pivot 版。
- 一份可直接執行的題組與三軌評估框架。
- 一套第一輪探索版測試材料：18 題題組、可直接貼用的 prompt 模板、實作 runbook。
- 一份第一輪最小矩陣 manifest，供正式記錄輸出狀態與盲評路徑。
- 一份 heuristics 附錄，把 `humanizer` 與維基特徵頁整理成研究用檢查清單。

## 現階段結論

- 中文 AI 味的主問題不在幾個高頻壞詞，主戰場在句法骨架、篇章節奏與整體分布過窄；只禁詞，效果有限。
- translationese 在中文場景不是旁支，且常和模板味纏在一起，尤其在英譯中與抽象說理題裡最明顯；若不處理源語骨架，很多去味只停在表層美容。
- 第一輪正式結果顯示，`rewrite-pipeline` 較穩，適合內容保真壓力高的題目；`pivot-pipeline` 更能切斷英語骨架，但代價是篇幅容易縮、語勢容易變緊。
- 較可靠的對抗路徑，是先分層診斷，再選改寫主幹，最後用有邊界的 heuristics 清理殘影；「文言中轉 -> 新文化白話」目前是這套方法裡最值得保留的一支。

## 原始材料

- [賈寶適翻譯.txt](https://github.com/show940125/AI-taste-research/blob/main/%E8%B3%88%E5%AF%B6%E9%81%A9%E7%BF%BB%E8%AD%AF.txt)
- [翻译理论要点及提示词优化指南.md](https://github.com/show940125/AI-taste-research/blob/main/%E7%BF%BB%E8%AF%91%E7%90%86%E8%AE%BA%E8%A6%81%E7%82%B9%E5%8F%8A%E6%8F%90%E7%A4%BA%E8%AF%8D%E4%BC%98%E5%8C%96%E6%8C%87%E5%8D%97.md)
