---
id: tool-00631
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 中文友好, 大纲规划, 多Agent, 灵感创意]
title: card-ocr-for-gws
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/masa-san-jp/card-ocr-for-gws
created: 2026-07-18
updated: 2026-07-18
no: 631
category: 二、网文 / 长篇 AI 写作系统 库
repo: masa-san-jp/card-ocr-for-gws
stars: 0
url: https://github.com/masa-san-jp/card-ocr-for-gws
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4498fbfc3de074df
  - methods/最强写作方法论_全球最强综合版.md
---

# masa-san-jp/card-ocr-for-gws

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/masa-san-jp/card-ocr-for-gws
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：automation, business-cards, google-sheets, google-workspace, ocr
- **GitHub 描述**：Google Workspace 上で名刺画像を OCR して Sheets に書き込むツール / A tool for OCR processing business card images and writing structured data to Google Sheets in Google Workspace workflows.
- **本地描述**：Google Workspace 上で名刺画像を OCR して Sheets に書き込むツール / A tool for OCR processing business card images and writing structured data to Google Sheets in Google Workspace workflows.
- **拉取时间**：2026-07-23 22:57:28

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 名刺スキャナーセットアップガイド

このガイドでは、Google Apps Script (GAS) と Gemini を使用して、名刺スキャナーをセットアップする方法を説明します。

## 前提条件

1.  **Googleアカウント**: GoogleドライブとGoogleスプレッドシートが利用できること。
2.  **Gemini APIキー**: [Google AI Studio](https://aistudio.google.com/) から取得してください。

## セットアップ手順

### 1. Googleドライブの準備
1.  Googleドライブに **"Business Cards Input"**（名刺入力用）という名前のフォルダを作成します。
2.  **"Business Cards Processed"**（処理済み名刺用）という名前のフォルダを作成します。
3.  両方の **フォルダID** を控えておきます。
    *   ブラウザでフォルダを開きます。
    *   URLの末尾がIDです: `https://drive.google.com/drive/folders/あなたのフォルダID`

### 2. Googleスプレッドシートとスクリプトの作成
1.  新しい **Googleスプレッドシート** を作成します。
2.  メニューから **拡張機能 > Apps Script** を選択します。
3.  Apps Scriptのエディタが開きます。

### 3. コードのコピー
Apps Scriptエディタで以下のファイルを作成し、提供されたコードをそれぞれコピー＆ペーストしてください：

*   `Config.gs`
*   `GeminiService.gs`
*   `SheetService.gs`
*   `main.gs`

**重要:** `Config.gs` 内の以下の項目を、実際ご自身の情報に書き換えてください：
*   `INPUT_FOLDER_ID`: 手順1で確認した入力用フォルダのID。
*   `PROCESSED_FOLDER_ID`: 手順1で確認した処理済み用フォルダのID。
*   `GEMINI_API_KEY`: 取得したAPIキー。

### 4. セットアップの実行
1.  Apps Scriptエディタの上部にある関数ドロップダウンから `setup` を選択します。
2.  **実行** ボタンをクリックします。
3.  **権限の承認**: 権限の確認を求められます。ご自身のドライブとスプレッドシートへのアクセスを許可してください。
    *   *注: ご自身で作成したスクリプトのため、「このアプリはGoogleによって確認されていません」という警告が表示される場合があります。「詳細」>「（プロジェクト名）に移動（安全ではない）」をクリックして進んでください。*
4.  スプレッドシートを確認し、ヘッダー行が作成されていれば成功です。

### 5. テスト実行
1.  名刺画像（JPG/PNG）を **"Business Cards Input"** フォルダにアップロードします。
2.  スクリプトエディタで `processNewCards` 関数を選択します。
3.  **実行** をクリックします。
4.  下部の **実行ログ** を確認します。"Successfully processed..." と表示されれば成功です。
5.  **スプレッドシート** を確認してください。データが抽出・入力されているはずです！

### 6. 自動化の設定（任意）
画像をアップロードしたら自動的に処理されるようにするには：
1.  左サイドバーの **トリガー** アイコン（時計のマーク）をクリックします。
2.  右下の **+ トリガーを追加** をクリックします。
3.  実行する関数: `processNewCards`
4.  イベントのソース: **時間主導型**
5.  時間ベースのトリガーのタイプ: **分ベースのタイマー**
6.  時間の間隔: **5分おき**（またはお好みの間隔）
7.  保存します。

これで、フォルダに画像を入れると5分以内に自動的に処理されるようになります。
