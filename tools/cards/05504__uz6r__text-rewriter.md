---
id: tool-05504
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: text-rewriter
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/uz6r/text-rewriter
created: 2026-07-18
updated: 2026-07-18
no: 5504
category: 一、去 AI 味 / Humanizer 库
repo: uz6r/text-rewriter
stars: 0
url: https://github.com/uz6r/text-rewriter
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 36f017dbede3ebb7
  - methods/改稿润色指令库.md
---

# uz6r/text-rewriter

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/uz6r/text-rewriter
- **Stars**：0
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：this is the text-rewriter-python repository, an open-source project that provides a python script to "humanize" ai-generated text. the script makes text more natural and readable by performing operations such as sentence and word-level processing, part-of-speech tagging, synonym replacement, symbol preservation, and formatting improvements.
- **本地描述**：this is the text-rewriter-python repository, an open-source project that provides a python script to "humanize" ai-generated text. the script makes text more natural and readable by performing operations such as sentence and word-level processing, part-of-speech tagging, synonym replacement, symbol preservation, and formatting improvements.
- **拉取时间**：2026-07-25 18:21:09

---

# 📚 **text-rewriter-python**

> ⚠️ **this repository is archived and no longer maintained.**  
> no further updates will be made. feel free to fork and build upon it.

---

## 🔍 overview

`text-rewriter-python` is a simple python tool that rewrites ai-generated text into more human-like language. it uses [`nltk`](https://www.nltk.org/) and [`textblob`](https://textblob.readthedocs.io/en/dev/) for natural language processing.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🛠️ getting started

1. make sure you have python 3 installed.
2. clone or download this repo.
3. install the required libraries:

   ```bash
   pip install nltk textblob
   ```

4. open `text_rewriter.py` in your editor.
5. use the `humanize_text` function to rewrite ai-generated text.

## example

```pgsql
$ python3 text_rewriter.py  
enter ai-generated text: the quick brown fox jumped over the lazy dog.  
the amazing brown fox really jumped over the lazy dog.
```

## 🧠 how it works

the core function `humanize_text` leverages basic nlp techniques to rephrase input text, aiming for more natural phrasing. it’s an experimental tool built as a starting point for further enhancements.

## 🤝 contributions

this repo is no longer maintained, but contributions via forks are always welcome. if you’d like to build on this, go ahead and fork the project.

## 📂 repo structure

```plain
.
├── readme.md  
└── text_rewriter.py
```

## 📄 license

licensed under the MIT license.
