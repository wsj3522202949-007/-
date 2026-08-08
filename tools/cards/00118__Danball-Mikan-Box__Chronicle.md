---
id: tool-00118
type: tool
area: 库
status: active
tags: [Rust, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Chronicle
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/danball-mikan-box/chronicle
created: 2026-07-18
updated: 2026-07-18
no: 118
category: 二、网文 / 长篇 AI 写作系统 库
repo: Danball-Mikan-Box/Chronicle
stars: 1
url: https://github.com/danball-mikan-box/chronicle
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: fdc92d62d339c397
  - methods/最强写作方法论_全球最强综合版.md
---

# Danball-Mikan-Box/Chronicle

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/danball-mikan-box/chronicle
- **Stars**：1
- **语言**：Rust
- **License**：None
- **Topics**：—
- **GitHub 描述**：Markdown Novel Editor
- **本地描述**：Markdown Novel Editor
- **拉取时间**：2026-07-23 22:42:25

---

# Chronicle — 小説執筆支援アプリケーション

**Chronicle** は、小説家のためのデスクトップ / Android 対応執筆環境です。
Markdown エディタとライブプレビュー、プロジェクト管理、各種出力機能を備えています。

---

## 機能

### エディタ
- **Markdown 記法** — 書式ツールバー（太字、斜体、見出し、引用、箇条書き、番号リスト、リンク、区切り線）とショートカット（Ctrl+B / Ctrl+I）で即時挿入
- **ルビ** — `{漢字|かんじ}` 記法でルビ付きテキストを記述可能
- **ライブプレビュー** — 右ペインまたは下ペインに即時反映。縦書き / 横書き切替対応
- **集中モード** — サイドバー・プレビューを隠してエディタに没頭
- **パネルカスタマイズ** — サイドバー・エディタ・プレビューの表示/非表示とドラッグリサイズ
- **フォント設定** — フォント種類、サイズ、行間、最大幅をアプリ全体で設定可能
- **段落字下げ** — 段落先頭の字下げをオン/オフ

### プロジェクト管理
- **章・話ツリー** — 作品ごとにプロジェクトを作成し、章・話をツリー構造で管理
- **設定資料** — キャラクター、世界観、用語集、年表などのカテゴリ別に資料を保存・編集
- **タブ編集** — 複数の話や資料をタブで切り替え

### 執筆支援
- **自動保存** — 3秒無入力後に自動保存。手動保存（Ctrl+S）も可能
- **文字数カウント** — リアルタイムカウント、今日の執筆進捗バー、読了時間目安
- **1日目標** — 目標文字数を設定し進捗をパーセント表示
- **ダークモード** — ワンタッチで切替

### エクスポート

| 形式 | 説明 |
|------|------|
| プロジェクトバックアップ (ZIP) | 全ファイルを圧縮 |
| サイト出力 (ZIP) | HTML サイト形式。目次付き、モバイル対応 |
| 原稿分割 (ZIP) | 章フォルダごとに .txt または .html で出力 |
| 投稿サイト用 (ZIP) | ルビ記法を各サイト書式に変換 |

#### 対応投稿サイトとルビ記法変換

| サイト | 変換後ルビ記法 |
|--------|---------------|
| 小説家になろう | `｜漢字《かんじ》` |
| カクヨム | `漢字《かんじ》` |
| ハーメルン | `\|漢字《かんじ》` |

## 技術スタック

| 層 | 技術 |
|---|------|
| 言語 | Rust (edition 2024) |
| UI フレームワーク | Dioxus 0.6 (Desktop / Mobile) |
| Markdown 処理 | 自作パーサ + pulldown-cmark |
| ファイルダイアログ | rfd (Rust File Dialog) |
| WebView | wry / WebKitGTK |
| ストレージ | JSON (プロジェクト設定) + Markdown (本文) |
| パッケージング | .deb / .rpm / AppImage / .wix / .apk |

## セットアップ

### ビルドと実行

```bash
# デスクトップ（Linux / Windows）
cargo run --release

# Android（要 dioxus-cli + Android SDK）
rustup target add aarch64-linux-android
cargo install dioxus-cli
dx build --platform android --release
```

### Linux 依存パッケージ

```bash
sudo apt install libgtk-3-dev libwebkit2gtk-4.1-dev libjavascriptcoregtk-4.1-dev \
  libcairo2-dev libpango1.0-dev libgdk-pixbuf-2.0-dev libglib2.0-dev librsvg2-dev
```

## 使い方

1. **「新規」** でプロジェクトを作成（作品名・作者名を入力）
2. サイドバーの **「+ 章を追加」** で章、**「+ 話を追加」** で話を追加
3. エディタに執筆し、書式ツールバーで装飾
4. **「保存」** または Ctrl+S で手動保存（3秒無入力で自動保存）
5. **「出力」** から ZIP で書き出し
6. 章名・話名・資料名は **✎** ボタンまたはダブルクリックで変更

### ショートカット

| キー | 機能 |
|------|------|
| Ctrl+S | 保存 |
| Ctrl+B | 太字 |
| Ctrl+I | 斜体 |
| Escape | エディタからフォーカスを外す |

## プロジェクト構成

```
my-novel/
├── chronicle.json         # プロジェクト設定
├── chapters/
│   ├── 01-第一章/
│   │   ├── 01-第一話.md
│   │   └── 02-第二話.md
│   └── 02-第二章/
│       └── 01-第一話.md
└── materials/
    ├── 01-主人公.md
    └── 02-年表.md
```

## CI / リリース

タグ `v*` をプッシュすると GitHub Actions が自動ビルドし、Release にアップロードします。

| プラットフォーム | 成果物 |
|----------------|-----related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Linux | `.deb` / `.rpm` / `.tar.gz` / `.AppImage` |
| Windows | `.zip`（ポータブル） |
| Android | `.apk` |

## ライセンス

MIT
