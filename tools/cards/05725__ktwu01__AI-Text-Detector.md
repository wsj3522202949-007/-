---
id: tool-05725
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议未明, 本地优先, 中文友好, 本地写作]
title: AI-Text-Detector
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/ktwu01/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5725
category: 一、去 AI 味 / Humanizer 库
repo: ktwu01/AI-Text-Detector
stars: 3
url: https://github.com/ktwu01/ai-text-detector
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: f55fb7485273a503
  - methods/改稿润色指令库.md
---

# ktwu01/AI-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ktwu01/ai-text-detector
- **Stars**：3
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：ai, ai-agent, llm, llm-detector, llm-inspector
- **GitHub 描述**：Aiming to be not the best free LLM-Fingerprint-Detector, AIText-Analyst, GenAI-Content-Inspector, AI-Pattern-Highlighter, AIScript-Detector, LLM-Style-Analyzer, AIContent-Forensics, NLP-AIMarker-Detector, AIText-Signature-Finder, LLM-Prose-Scanner
- **本地描述**：Aiming to be not the best free LLM-Fingerprint-Detector, AIText-Analyst, GenAI-Content-Inspector, AI-Pattern-Highlighter, AIScript-Detector, LLM-Style-Analyzer, AIContent-Forensics, NLP-AIMarker-Detector, AIText-Signature-Finder, LLM-Prose-Scanner
- **拉取时间**：2026-07-25 18:29:18

---

# AI-Text-Highlighter
---
Author: Koutian Wu

Github, LinkedIn: ktwu01

Release date: Apr 20, 2025

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

The AI Word and Phrase Highlighter is designed to detect common words and phrases frequently used in AI-generated content.

为啥要做：，优势

免费开源。

本地部署，数据不上传，隐私保护。

可以根据需要自定义AI词库。

某种意义上也可以作为违禁词词库查询。。

捐赠选项，捐赠支持作者。


## How It Works

The tools work by scanning text for words and phrases commonly used by AI models like ChatGPT, Claude, and others. These words and phrases are ranked based on their frequency in AI-generated documents compared to human-written documents. The data is drawn from research by various detection tools like ZeroGPT and GPTZero.

When analyzing text, the tools identify common AI markers like:
- Overused transition phrases ("Furthermore", "On the other hand")
- Formal academic constructions ("It's important to note", "In conclusion")
- Verbose expressions ("When it comes to", "In the realm of")
- Distinctive vocabulary ("delve", "plethora", "harness", "tapestry")

## Using the Tools

You can use these tools in several ways:

1. **For Content Creation**: Identify and replace AI-like patterns in your writing
2. **For SEO**: Optimize content to reduce AI detection probability
3. **For Education**: Compare AI vs. human writing patterns
4. **For Research**: Analyze large text corpora for AI indicators

The HTML reports provide color-coded highlighting of AI indicators and suggest alternative words and phrases to make text appear more human-written.

## Installation & Setup

To use these tools:

1. Git Clone
   ```
   git clone https://github.com/ktwu01/AI-Text-Detector.git
   ```
2. Install required dependencies:
   ```
   pip install pandas matplotlib seaborn streamlit sqlite3
   ```
3. Run the tool
   ```
   streamlit run KW-ai_word_highlighter.py
   ```
 <!-- according to your needs:
   - For the Streamlit app:  -->
   
<!-- 
   - For command-line analysis: 
   ```
   python ai_seo_analyzer.py --file your_text.txt
   ```
   
   - For Python integration: Import SimpleAIWordHighlighter in your code -->

## Preview
![assets/preview.png](https://github.com/ktwu01/AI-Text-Detector/blob/main/assets/preview.png)

Example result:

![assets/result1.png](https://github.com/ktwu01/AI-Text-Detector/blob/main/assets/result1.png)
![assets/result2.png](https://github.com/ktwu01/AI-Text-Detector/blob/main/assets/result2.png)
