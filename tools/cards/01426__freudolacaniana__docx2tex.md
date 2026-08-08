---
id: tool-01426
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: docx2tex
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/freudolacaniana/docx2tex
created: 2026-07-18
updated: 2026-07-18
no: 1426
category: 二、网文 / 长篇 AI 写作系统 库
repo: freudolacaniana/docx2tex
stars: 0
url: https://github.com/freudolacaniana/docx2tex
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8bdff5cc8909ac1d
  - methods/最强写作方法论_全球最强综合版.md
---

# freudolacaniana/docx2tex

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/freudolacaniana/docx2tex
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：An online tool for converting Microsoft Word (.docx) files into LaTeX (.tex) format, specifically optimized for Japanese typesetting in humanities research and creative writing (novels).／Microsoft Word（.docx）ファイルを、人文科学系の論文や小説などの日本語組版に最適化された LaTeX（.tex）形式へ変換するオンラインツールです。
- **本地描述**：An online tool for converting Microsoft Word (.docx) files into LaTeX (.tex) format, specifically optimized for Japanese typesetting in humanities research and creative writing (novels).／Microsoft Word（.docx）ファイルを、人文科学系の論文や小説などの日本語組版に最適化された LaTeX（.tex）形式へ変換するオンラインツールです。
- **拉取时间**：2026-07-23 23:20:41

---

# docx2tex



Microsoft Word（.docx）ファイルを、日本語組版に最適化された LaTeX（.tex）形式に変換するオンラインツールです。

以下のリンクから使用できます。



https://freudolacaniana.github.io/docx2tex/docx2tex.html



## 🚀 これは何？



Microsoft Word 等で作成された原稿を、LaTeX で処理可能なソースファイルに変換します。



- **一括ダウンロード**: 変換後のファイルは、原稿内の画像ファイル等を含めた `.zip` 形式で取得できます。

- **日本語組版への最適化**: `lualatex` + `jlreq` 環境を前提としており、[日本語組版処理の要件](https://www.w3.org/TR/jlreq/?lang=ja)に即した高品質なPDF出力が可能です。

- **CloudLaTeX 対応**: 出力される `.zip` ファイルは、そのまま [CloudLaTeX](https://cloudlatex.io/) へインポートして使用できます。



### 💡 本ツールの特徴



Pandoc をはじめとする既存の変換ツールは多数ありますが、本ツールは特に **「日本語・縦書きの人文科学系論文、書籍、小説」** のために開発されています。



- **ルビ** や **縦中横** など、日本語文書特有の書式保持に強みがあります。

- ※ 数式や `.emf` ファイルの変換には限定的にしか対応していません。理系分野の用途には [Pandoc](https://pandoc.org/) 等の利用を推奨します。



---



## ⚠️ 注意事項



- **プライバシー・セキュリティ**: 本ツールはクライアントサイドの JavaScript のみで動作します。ファイルが外部サーバーにアップロードされることはなく、すべての処理はブラウザ内で完結します。

- **PDF出力について**: 本ツール自体は PDF を出力しません。PDF を得るには、変換後のファイルをローカルの [TeX Live](https://texwiki.texjp.org/?TeX%20Live) 環境や CloudLaTeX 等でコンパイル（タイプセット）する必要があります。

- **推奨環境**: `lualatex` + `jlreq` でのコンパイルを想定しています。その他の環境で使用する場合は、適宜 `.tex` ファイルのプリアンブルを編集してください。



---



## 📝 .docx ファイルの準備



変換精度を高めるため、元の `.docx` ファイルで以下の設定を行っておくことを推奨します。



- **スタイル機能の活用**:

- タイトルには「表題」スタイル

- サブタイトルには「副題」スタイル

- 各見出しには「見出し1」「見出し2」などのスタイルを適用してください。



- **著者名**: タイトル・サブタイトルの直下にある短い行は、自動的に著者名として認識されます。

- **見出しレベル**: 各スタイルを LaTeX のどのコマンド（`\section`, `\subsection` 等）に対応させるかは、ツール上の設定で調整可能です。



related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---



### 💡 Licenses



This project utilizes the following libraries under the MIT License:



- **UDOC.js**: Used for reading `.emf` files embedded within `.docx` documents.

- **JSZip**: Used for parsing `.docx` files and generating `.zip` output.

- **officemath2latex**: Used for parsing oMath formulas and generating their LaTex equivalents.







