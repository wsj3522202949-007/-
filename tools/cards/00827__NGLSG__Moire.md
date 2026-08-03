---
id: tool-00827
type: tool
area: 库
status: active
tags: [Dart, 协议宽松, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Moire
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/nglsg/moire
created: 2026-07-18
updated: 2026-07-18
no: 827
category: 二、网文 / 长篇 AI 写作系统 库
repo: NGLSG/Moire
stars: 1
url: https://github.com/nglsg/moire
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# NGLSG/Moire

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nglsg/moire
- **Stars**：1
- **语言**：Dart
- **License**：MIT
- **Topics**：android, desktop-app, editor, flutter, knowledge-base, linux, local-first, macos, markdown, windows
- **GitHub 描述**：Local-first novel writing editor with chapter management and knowledge-base references.
- **本地描述**：Local-first novel writing editor with chapter management and knowledge-base references.
- **拉取时间**：2026-07-23 23:03:09

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<p align="center">
  <img src="icon.png" alt="墨鸢" width="128">
</p>

# 墨鸢 / Moire

一个 Flutter 写的小说编辑器。

目前主要解决几件事：

- 长篇小说按项目管理，不把正文锁进数据库里。
- 正文、章节、知识库都直接落在本地文件夹。
- 写小说时能把人物、地点、组织、物品这类设定做成条目，然后在正文里引用。
- 尽量让几百万字项目也能打开、搜索、翻章节，不至于一章塞多了就卡死。

它还在开发中，不是成熟产品。

## 现在有的东西

### 项目和章节

- 打开一个文件夹作为项目。
- 扫描 `.txt` / `.md` 文件作为章节。
- 新建章节会写到 `chapters/` 目录。
- 章节文件保持普通文本格式。
- 文件树支持搜索、重命名、删除、批量删除、排序。

### 编辑器

- 编辑 / 预览两种视图。
- 切换视图时尽量保持滚动位置一致。
- 搜索会高亮所有匹配项。
- 上一个 / 下一个搜索结果会滚到选区附近。
- 大文本会关闭一部分重型渲染，避免拖死界面。

### 知识库

- 可以建人物、地点、组织、物品、设定等条目。
- 正文里用条目索引引用知识库。
- 可以扫描当前章节，把匹配到的普通文本替换成条目索引。
- 选中文本可以快速创建知识条目。
- 点击正文里的条目可以直接编辑条目内容。

### 阅读 / 预览

- 长文本分块渲染。
- 章节索引按真实章节位置跳转。
- 目标是能处理百万字级项目，而不是只适合小段 Markdown。

## 项目目录

大概长这样：

```text
my_novel/
  project.json
  knowledge.json
  chapters/
    001_第一章.md
    002_第二章.md
```

外部已有的 `.txt`、`.md` 也可以直接导入。

## 构建

```bash
flutter pub get
flutter run
```

Android：

```bash
flutter build apk --release
```

Windows：

```bash
flutter build windows --release
```

Linux / macOS 也保留了 Flutter 桌面工程配置，但我主要在 Windows 和 Android 上测试。

## 名字

- 中文名：墨鸢
- 英文名：Moire

## License

MIT
