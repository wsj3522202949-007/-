---
id: tool-01367
type: tool
area: 库
status: active
tags: [Claude插件, Dart, 协议未明, 需API密钥, 中文友好]
title: novel-writer
summary: Claude Code 插件式写作流
source: https://github.com/maxlingg/novel-writer
created: 2026-07-18
updated: 2026-07-18
no: 1367
category: 二、网文 / 长篇 AI 写作系统 库
repo: maxlingg/novel-writer
stars: 0
url: https://github.com/maxlingg/novel-writer
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# maxlingg/novel-writer

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/maxlingg/novel-writer
- **Stars**：0
- **语言**：Dart
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered novel writing tool built with Flutter
- **本地描述**：AI-powered novel writing tool built with Flutter
- **拉取时间**：2026-07-23 23:19:00

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Novel Writer

一款 AI 驱动的小说创作工具，基于 Flutter 开发，仅支持 Android 平台。

## 功能特性

- **AI 辅助写作** - 支持 Claude、GPT、DeepSeek、GLM、Kimi 等多种 AI 模型
- **智能体体系** - Agent + Tool + Skill 三层架构，AI 可操作项目文件
- **技能系统** - 插件化技能架构，支持创建/分享/安装技能
- **项目管理** - 项目 > 卷 > 章节层级管理
- **富文本编辑器** - HTML 格式编辑，自动保存
- **DOCX 导入导出** - 完整的 Word 文档支持
- **WebDAV 云同步** - 支持与 NAS/云存储同步
- **搜索功能** - 本地文件搜索 + 网络搜索
- **主题系统** - 深色/浅色/跟随系统
- **备忘录** - 创作灵感记录

## 技术栈

- **框架**: Flutter 3.x (Dart)
- **状态管理**: Provider
- **平台**: Android (arm64-v8a)
- **数据存储**: 本地文件系统 + SharedPreferences

## 项目结构

```
lib/
├── main.dart              # 应用入口
├── app.dart               # 根组件（路由/主题）
├── models/                # 数据模型
├── services/              # 业务逻辑服务
│   ├── providers/         # AI 模型提供商
│   └── tools/             # Agent 工具
├── screens/               # 页面 UI
├── widgets/               # 自定义组件
└── utils/                 # 工具类
```

## 快速开始

```bash
# 获取依赖
flutter pub get

# 运行
flutter run

# 构建 APK
flutter build apk --release
```

## 配置 AI 模型

在设置页面配置对应模型的 API Key：
- Anthropic Claude: [console.anthropic.com](https://console.anthropic.com)
- OpenAI GPT: [platform.openai.com](https://platform.openai.com)
- DeepSeek: [platform.deepseek.com](https://platform.deepseek.com)
- 智谱 GLM: [open.bigmodel.cn](https://open.bigmodel.cn)
- Kimi: [platform.moonshot.cn](https://platform.moonshot.cn)

## 许可证

MIT License
