---
id: tool-07352
type: tool
area: 库
status: active
tags: [校对, TypeScript, 协议未明, 本地优先, 中文友好, 改稿润色, 本地写作]
title: scrutario
summary: 错别字/语法/风格校对
source: https://github.com/kakahuote1/scrutario
created: 2026-07-18
updated: 2026-07-18
no: 7352
category: 画龙补充 / 扩容入库 — 补充源
repo: kakahuote1/scrutario
stars: 2
url: https://github.com/kakahuote1/scrutario
tier: "B"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# kakahuote1/scrutario

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/kakahuote1/scrutario
- **Stars**：2
- **语言**：TypeScript
- **License**：None
- **Topics**：classical-chinese, desktop-app, digital-humanities, document-management, electron, full-text-search, historical-documents, local-first, ocr, pdf
- **GitHub 描述**：Local-first desktop OCR, proofreading and full-text search for classical Chinese documents
- **本地描述**：scrutario
- **拉取时间**：2026-07-25 19:19:15

---

<div align="center">

# 📖 Scrutario

**面向古籍、地方志、影印书和个人文献库的本地化桌面检索与管理平台**

[![Platform](https://img.shields.io/badge/Platform-Windows-blue.svg)]()
[![Electron](https://img.shields.io/badge/Electron-31.7.7-47848f.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

</div>

---

**Scrutario** 是一款专为古籍、地方志、影印书及个人文献库打造的高性能桌面端检索与管理工具；核心目标是将**资料导入、OCR 识别、校对、全文检索、书签管理、目录生成、沉浸式阅读及模型训练数据采集**整合入单一工作流，为研究人员和文献爱好者提供本地化数字文献处理体验
<p style="font-size: 10px;">....嗯，也许用来读论文也是不错的？</p>
<div align="center">
  <img src="media/reader.png" alt="Scrutario 阅读与校对界面" width="100%" />
</div>

## ✨ 核心特性

- 📚 **统一的本地资料库**：无缝导入 PDF、图片、Word、EPUB、TXT 等常见格式；所有文献、索引、模型和日志均在本地应用数据目录集中管理
- ⚡ **毫秒级高速全文检索**：正文、书名、作者及元数据统一构建索引入库；支持精确匹配、模糊检索和跨页连续文本搜索
- 🔍 **双栏对读与高精度 OCR 校对**：支持 PDF 原页与识别文本并排比对；提供阅读、校对、识别块等多种视图模式
- 📐 **灵活的 OCR 扫描规则引擎**：支持按页码、范围、规律或自定义框选设定 OCR 区域；适配竖排古籍、多栏、折痕及侧边批注等复杂版式
- 🧩 **模块化能力包管理架构**：OCR 引擎、文档转换器和训练模块均封装为独立离线包；支持 GitHub Release 更新和纯离线安装
- 🤖 **训练数据采集闭环**：校对过程中可随时截图保存字形样本；训练控制台用于整理数据集、备份模型并生成本地模型
- 📖 **无干扰沉浸阅读体验**：支持单页阅读或双文献同屏对读；提供滚轮缩放、拖拽平移、方向键翻页和书签跳转

---

## 📸 界面纵览

### 1. 资料库、阅读与校对
左侧集成目录、搜索和书签；中栏保留宽敞的文献预览与校对空间；核心操作全局可见，低频操作收纳于上下文菜单
<div align="center">
  <img src="media/reader.png" alt="阅读与校对" width="100%" />
</div>

### 2. OCR 方案动态调度
遵循“单一模型对应单一能力”原则；启动 OCR 时按需选择模型与运行模式，可用性校验、下载和离线导入均在当前工作流内完成
<div align="center">
  <img src="media/ocr-profile-dialog.png" alt="OCR 方案选择" width="100%" />
</div>

### 3. 高级扫描规则配置
专为复杂文献设计；支持翻页预览、滚轮缩放、精准框选识别区与排除区，适配竖排古籍、多栏混排、页眉页脚干扰及旁批
<div align="center">
  <img src="media/scan-rules-dialog.png" alt="扫描规则" width="100%" />
</div>

### 4. 沉浸式阅读与分屏对读
屏蔽所有非阅读相关的 UI 元素；支持拖入第二份文献形成左右或上下分屏，适合文本查校、版本对读和长篇阅读
<div align="center">
  <img src="media/immersive-reader.png" alt="沉浸阅读" width="100%" />
</div>

### 5. 全局设置与暗黑模式
配置项按 OCR、转换、训练、模型、资料包、存储、日志和热键结构化组织；侧边栏支持一键切换日间和暗黑模式
<div align="center">
  <img src="media/settings.png" alt="设置页" width="49%" />
  <img src="media/settings-dark.png" alt="夜间模式" width="49%" />
</div>

### 6. 模型训练数据控制台
支持独立浮动窗口；提供截图粘贴、手动归档、发起训练、模型备份及本地模型管理功能
<div align="center">
  <img src="media/training-dialog.png" alt="训练控制台" width="100%" />
</div>

---

## 🚀 快速开始

### 标准使用流程

1. **导入资料**：将 PDF、图片或其他类型文档直接拖入应用窗口
2. **完善元数据**：录入书名、作者、版本、分类等结构化档案信息
3. **配置规则**：选择预设模板，或针对特殊页面自定义识别/排除范围及文字走向
4. **执行 OCR**：选择已加载的模型包，可按需切换“效率”、“平衡”或“精确”模式
5. **即扫即看**：后台 OCR 任务支持暂停、恢复与取消；已识别页面可立即进入校对与检索环节
6. **检索与阅读**：借助目录、全局搜索、书签网络或沉浸模式深度阅读文献
7. **数据流转**：资料库与能力包支持全量导出/导入，实现多端设备间的无缝迁移与完全离线分发

### 安装与能力包部署

- `Scrutario_Setup.exe`：Windows 平台一体化安装器
- `paddle_ppocrv5.socr`：清晰扫描书和普通地方志识别包
- `kraken_htr.socr`：旧刻本、竖排页和同一字形训练识别包
- `cnocr_doc.socr`：单字单行截图数据集和小样本验证识别包
- `tesseract5.socr`：无网络、低配电脑和规整横排资料识别包
- `doc_converter.sconv`：格式解析与文档转换能力包
- `ocr_train.strain`：模型训练与本地模型管理能力包

**离线环境部署**：用户可手动下载上述能力包，并在应用的“设置页”或导入向导中选择“导入离线能力包”进行离线部署

---

## 📂 存储与升级机制

- **数据隔离与安全**：默认情况下，Scrutario 将文献、索引数据库、模型权重、训练集、日志及缓存统一部署在安装目录下的 `data` 文件夹内
- **平滑更新机制**：自 `v0.1` 起，应用接入 GitHub Release 作为官方更新信道系统在后台静默轮询安装器及能力包更新，发现新版本后将通过非阻塞式弹窗通知用户，由用户自主决定**更新**、**取消**或**跳过该版本**

related:
  - methods/QUICK_START.md
---

## 📜 许可与第三方鸣谢

本项目在架构与实现过程中，使用了诸多优秀的开源组件：
- [Electron](https://github.com/electron/electron) 
- [PDF.js](https://github.com/mozilla/pdf.js) 
- [sql.js](https://github.com/sql-js/sql.js) 
- [7-Zip](https://www.7-zip.org/)

详细的第三方开源许可声明，请参阅源码库中的 `third-party-licenses/` 目录

<p style="font-size: 5px;">以及感谢一位神秘人的赞助</p>
