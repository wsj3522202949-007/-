---
id: tool-07435
type: tool
area: 库
status: active
tags: [大纲规划, Claude插件, TypeScript, 协议未明, 本地优先, 中文友好, 本地写作]
title: obsidian-writer-suite
summary: 搭大纲/分卷/节拍
source: https://github.com/morick66/obsidian-writer-suite
created: 2026-07-18
updated: 2026-07-18
no: 7435
category: 画龙补充 / 扩容入库 — 补充源
repo: morick66/obsidian-writer-suite
stars: 19
url: https://github.com/morick66/obsidian-writer-suite
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# morick66/obsidian-writer-suite

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/morick66/obsidian-writer-suite
- **Stars**：19
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：An obsidian plug-in that is more convenient for writing novels
- **本地描述**：obsidian-writer-suite
- **拉取时间**：2026-07-25 19:21:47

related:
  - methods/QUICK_START.md
---

# Obsidian Writer Suite
obsidian小说创作插件

> ⚠ **警告**
> 1. 插件目前还存在一些小bug，但是基本使用并无大碍
> 2. 插件目前只有中文，后续可能会支持英文
> 3. 诸如文件夹结构暂时无法自定义，目前只能使用我设定的这种文件夹结构
> 4. 需要单独创建一个obsidian仓库使用
> 5. 所有都是基于obsidian的文件和文件夹重新渲染展示，所以当使用同步插件时，插件不同步空文件夹就会导致创建的分类消失，所以创建了分类建议在分类下创建一个文件

## 特色

1. 涵盖长篇小说和短篇小说
2. 侧边栏显示大纲，创作时方便参考
3. 更舒服的目录，不用一层层的在树状文件结构中寻找章节
4. 全局灵感
5. 长篇小说的书籍设定部分包含大纲、角色、设定、灵感四大类，可自己创建分类
6. 基于obsidian的文件结构，零迁移成本。
7. 每一章节的字数统计以及全书的字数统计。
8. 以及其他

## 文件夹结构

仓库根目录中，除一个“@附件”的文件夹之外，一篇小说（无论长篇短篇）一个文件夹。

### @附件

这个文件夹存放可能的一些附件图片之类，目前有一个`灵感`文件夹，用于存放全局灵感。

### 长篇小说
- 信息.md
  - 存储小说基本信息
- 小说文稿
  - 存放小说文稿，可以分卷
- 设定
  - 存放小说设定、大纲等
  - 目前存在大纲、设定、角色、灵感四个大分类
  - 大分类下可以自定义小分类

### 短篇小说

短篇小说文件夹下有三个文件

- 信息.md
  - 小说基本信息
- 小说正文.md
  - 短篇小说的正文
- 大纲.md
  - 小说的大纲文件

## 插件功能

### 书架视图

书架视图，可以显示你创建的所有小说，包含长篇小说和短篇小说。

#### 新建书籍

点击书架视图中右下角的“+”按钮，出现新建书籍对话框。

可以定义书籍名称，小说的类型，和简介。

### 个人信息

可以在插件设置中设置头像（暂时只支持图床链接）和昵称。

简单显示创建的短篇小说和长篇小说的数量

### 全局灵感

显示全局灵感的快捷添加和删除，点击进入文件修改。

## 插件截图

### 书架视图

!`[alt text](images/image.png)`

### 短篇小说

!`[alt text](images/image-1.png)`

### 长篇小说

!`[alt text](images/image-2.png)`

## 使用

从`Releases`下载示例库压缩包，或者下载插件文件添加到自己的插件文件夹中。
