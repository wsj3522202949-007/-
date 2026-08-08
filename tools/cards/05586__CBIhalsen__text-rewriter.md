---
id: tool-05586
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: text-rewriter
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/cbihalsen/text-rewriter
created: 2026-07-18
updated: 2026-07-18
no: 5586
category: 一、去 AI 味 / Humanizer 库
repo: CBIhalsen/text-rewriter
stars: 29
url: https://github.com/cbihalsen/text-rewriter
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8746dca5e7f51e39
  - methods/改稿润色指令库.md
---

# CBIhalsen/text-rewriter

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/cbihalsen/text-rewriter
- **Stars**：29
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：this is the text-rewriter-python repository, an open-source project that provides a python script to "humanize" ai-generated text. the script makes text more natural and readable by performing operations such as sentence and word-level processing, part-of-speech tagging, synonym replacement, symbol preservation, and formatting improvements.
- **本地描述**：this is the text-rewriter-python repository, an open-source project that provides a python script to "humanize" ai-generated text. the script makes text more natural and readable by performing operations such as sentence and word-level processing, part-of-speech tagging, synonym replacement, symbol preservation, and formatting improvements.
- **拉取时间**：2026-07-25 18:24:11

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# 📚 **text-rewriter-python**

welcome to the text-rewriter-python repository! this open-source collaboration is designed for anyone to fork and improve.

**description:**
the `text-rewriter-python` repository is a python project that provides a text rewriting functionality. it aims to create a python tool that can rewrite ai-generated text. by following the provided steps, you can install the tool, import the necessary libraries (`nltk` and `textblob`), and utilize the `humanize_text` function to rewrite the ai-generated text into a more human-like version.

**contributions:**
we encourage developers and enthusiasts to contribute to this project in any way they can. whether it's improving the text rewriting algorithms, enhancing the user interface, or adding new features, your contributions are highly appreciated! to contribute, you can fork the repository and submit a pull request with your changes.

**license:**
this project is licensed under the mit license. see the license file for details.

this tool utilizes the natural language toolkit (nltk) and textblob libraries, which make natural language processing in python accessible to everyone. we extend our gratitude to the developers of these libraries for their valuable contributions.

repository structure:
- readme.md
- text_rewriter.py

to get started with the tool, follow these steps:

1. install python 3 on your computer if it's not already installed.
2. download or clone the repository.
3. install the required libraries by running `pip install nltk textblob` in your terminal.
4. open the python file (`text_rewriter.py`) in your preferred code editor.
5. import the `nltk` and `textblob` libraries at the beginning of the file.
6. copy and paste the `humanize_text` function from the code snippet into your file.
7. call the `humanize_text` function with the ai-generated text as the argument.
8. the function will return the humanized text.

here's an example of how to use the tool:

```
$ python3 text_rewriter.py
enter ai-generated text: the quick brown fox jumped over the lazy dog.
the amazing brown fox really jumped over the lazy dog.
```

we appreciate your interest and contributions to the `text-rewriter-python` project. feel free to reach out if you have any questions or need further assistance.
