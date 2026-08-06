---
id: tool-01416
type: tool
area: 库
status: active
tags: [Vue, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: novel-writing-tool-starter
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/siev0000/novel-writing-tool-starter
created: 2026-07-18
updated: 2026-07-18
no: 1416
category: 二、网文 / 长篇 AI 写作系统 库
repo: siev0000/novel-writing-tool-starter
stars: 0
url: https://github.com/siev0000/novel-writing-tool-starter
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# siev0000/novel-writing-tool-starter

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/siev0000/novel-writing-tool-starter
- **Stars**：0
- **语言**：Vue
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：siev0000/novel-writing-tool-starter
- **拉取时间**：2026-07-23 23:20:23

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 小説書き出しアプリ スターター

MD仕様をもとにした、Web/PWA/アプリ化前提のVue版スターターです。

## 仕様メモ

- [小説書き出しアプリ_仕様まとめ.md](https://github.com/siev0000/novel-writing-tool-starter/blob/main/docs/%E5%B0%8F%E8%AA%AC%E6%9B%B8%E3%81%8D%E5%87%BA%E3%81%97%E3%82%A2%E3%83%97%E3%83%AA_%E4%BB%95%E6%A7%98%E3%81%BE%E3%81%A8%E3%82%81.md)

## 方針

- Web本体: Vue + Vite
- 保存: まずは localStorage
- 後から拡張: APIサーバー、SQLite、PWA、Capacitor、Tauri などに移行可能

## 現在入っている機能

- 作品作成・作品編集
- 登場人物管理
- 自由プロフィール項目追加
- 用語まとめ
- 話プロット・シーン管理
- 書き出し候補保存、採用/保留/ボツ
- VSCode風の本文エディタ
- 行番号表示
- 行間メモ
- 文字数、行数、空行数、会話文数、メモ数
- 本文のみtxt出力
- メモ付きtxt出力
- JSONバックアップ

## 起動方法

```bash
npm install
npm run dev
```

ブラウザで表示されたURLを開きます。

ブラウザも自動で開きたい場合は、次を使います。

```bash
npm run dev:open
```

開発中の変更はViteが自動でブラウザへ反映します。

## アプリ化する場合

このコードはまずWebとして動かし、後から次のどれかでアプリ化する想定です。

- スマホアプリ: Capacitorでラップ
- PCアプリ: TauriまたはElectronでラップ
- インストール可能Webアプリ: PWA化

## 次に追加しやすいもの

- 作品ごとのタグ編集画面
- キャラクターと話・シーンの登場紐づけ
- 用語の表記ゆれチェック
- 本文内検索
- メモ一覧
- 投稿場所別プレビュー
- 投稿サイト別エクスポート
- AI API連携
