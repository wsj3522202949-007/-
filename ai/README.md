---
id: index-ai
type: index
area: 索引
status: active
tags: [AI, 协作, 导航, 读写优化]
title: AI 协作入口（读写优化版）
summary: AI 读写知识库的专用导航——提示词、工作流、模板、约束、校验、检索。专为 AI 高效读写优化。
source: 内部制定
created: 2026-07-31
updated: 2026-08-02
related:
  - schema/AI协作规范.md
  - CLAUDE.md
  - methods/QUICK_START.md
see_also:
  - methods/SKILL.md
  - tools/工具仪表盘.md
---

# 🤖 AI 协作入口（读写优化版）

> 本目录是 AI 读写知识库的**专用入口**。读完即可：定位资源、遵守约束、高效输出。

---

## 🚀 快速开始（30 秒）

**第一次进入？按顺序读这 3 个文件：**

1. **[CLAUDE.md](../CLAUDE.md)** — 导航 + 红线 + 规则
2. **本文件**（ai/README.md）— AI 专用资源总览
3. **[methods/QUICK_START.md](../methods/QUICK_START.md)** — 按症状找方法论

**关键路径速查：**

| 我想做什么 | 直接去 |
|---|---|
| 写正文 | `ai/prompts/写正文.md` + `ai/templates/正文章节模板.md` |
| 写大纲 | `ai/prompts/写大纲.md` + `ai/templates/大纲模板.md` |
| 改稿/去AI味 | `ai/prompts/改稿.md` + `ai/prompts/去AI味.md` |
| 自检 | `ai/prompts/自检.md` + `ai/validation/正文校验.md` |
| 新书启动 | `ai/workflows/新书启动.md` |
| 章节生产 | `ai/workflows/章节生产.md` |
| 查方法论 | `methods/QUICK_START.md`（按症状查） |
| 查工具 | `tools/README.md` + `tools/任务选型速查.md` |
| 查规范 | `schema/` 目录（frontmatter/链接/结构） |

---

## 一、目录结构

```
ai/
├── README.md           # 本文件（AI 协作入口）
├── prompts/            # AI 提示词模板
│   ├── 写正文.md       # 生成正文的提示词
│   ├── 写大纲.md       # 生成大纲的提示词
│   ├── 改稿.md         # 改稿润色的提示词
│   ├── 去AI味.md       # 去 AI 味的提示词
│   └── 自检.md         # 自检的提示词
├── workflows/          # AI 工作流定义
│   ├── 新书启动.md     # 新书启动工作流
│   ├── 章节生产.md     # 章节生产工作流
│   ├── 改稿流程.md     # 改稿流程工作流
│   ├── 签约体检.md     # 签约体检工作流
│   ├── 全平台签约指南.md # 全平台签约指南
│   └── 番茄签约完全指南.md # 番茄签约完全指南
├── templates/          # AI 输出模板
│   ├── 正文章节模板.md # 正文章节模板
│   ├── 大纲模板.md     # 大纲模板
│   ├── 人物卡模板.md   # 人物卡模板
│   └── 设定卡模板.md   # 设定卡模板
├── constraints/        # AI 约束文件
│   ├── 合规红线.md     # 合规红线（不可违反）
│   ├── 写作硬约束.md   # 写作硬约束
│   ├── 格式要求.md     # 格式要求
│   └── 禁忌清单.md     # 禁忌清单
├── validation/         # AI 输出校验
│   ├── 正文校验.md     # 正文校验规则
│   ├── 大纲校验.md     # 大纲校验规则
│   └── 人物卡校验.md   # 人物卡校验规则
└── search/             # AI 检索索引
    ├── 按任务索引.md   # 按任务检索
    ├── 按工具索引.md   # 按工具检索
    └── 按平台索引.md   # 按平台检索
```

---

## 二、按任务找资源

### 2.1 写正文

| 资源 | 路径 | 用途 |
|---|---|---|
| 提示词 | `ai/prompts/写正文.md` | 生成正文的提示词 |
| 工作流 | `ai/workflows/章节生产.md` | 章节生产工作流 |
| 模板 | `ai/templates/正文章节模板.md` | 正文章节模板 |
| 约束 | `ai/constraints/写作硬约束.md` | 写作硬约束 |
| 校验 | `ai/validation/正文校验.md` | 正文校验规则 |

**流程：**
1. 读 `ai/prompts/写正文.md`（了解提示词）
2. 读 `ai/templates/正文章节模板.md`（了解格式）
3. 读目标项目的 `framework.md` + `outline.md` + `entities/`
4. 读最近 2-3 章正文（了解上下文）
5. 按模板生成正文
6. 跑 `ai/validation/正文校验.md`（自检）
7. 写入 `projects/*/chapters/第NNN章-标题.md`

### 2.2 写大纲

| 资源 | 路径 | 用途 |
|---|---|---|
| 提示词 | `ai/prompts/写大纲.md` | 生成大纲的提示词 |
| 工作流 | `ai/workflows/新书启动.md` | 新书启动工作流 |
| 模板 | `ai/templates/大纲模板.md` | 大纲模板 |
| 约束 | `ai/constraints/格式要求.md` | 格式要求 |
| 校验 | `ai/validation/大纲校验.md` | 大纲校验规则 |

**流程：**
1. 读 `ai/prompts/写大纲.md`
2. 读 `ai/templates/大纲模板.md`
3. 读目标项目的 `framework.md`
4. 按模板生成大纲
5. 跑 `ai/validation/大纲校验.md`
6. 写入 `projects/*/outline.md`

### 2.3 改稿/去AI味

| 资源 | 路径 | 用途 |
|---|---|---|
| 提示词 | `ai/prompts/改稿.md` | 改稿润色的提示词 |
| 提示词 | `ai/prompts/去AI味.md` | 去 AI 味的提示词 |
| 工作流 | `ai/workflows/改稿流程.md` | 改稿流程工作流 |
| 约束 | `ai/constraints/写作硬约束.md` | 写作硬约束 |

**流程：**
1. 读 `ai/prompts/改稿.md` 或 `ai/prompts/去AI味.md`
2. 读目标章节正文
3. 按提示词改稿
4. 跑 `ai/validation/正文校验.md`
5. 覆盖原文件

### 2.4 自检

| 资源 | 路径 | 用途 |
|---|---|---|
| 提示词 | `ai/prompts/自检.md` | 自检的提示词 |
| 工作流 | `ai/workflows/签约体检.md` | 签约体检工作流 |
| 约束 | `ai/constraints/禁忌清单.md` | 禁忌清单 |

### 2.5 新建一本书

| 资源 | 路径 | 用途 |
|---|---|---|
| 工作流 | `ai/workflows/新书启动.md` | 新书启动工作流 |
| 模板 | `ai/templates/大纲模板.md` | 大纲模板 |
| 模板 | `ai/templates/人物卡模板.md` | 人物卡模板 |
| 模板 | `ai/templates/设定卡模板.md` | 设定卡模板 |

**流程：**
1. 读 `ai/workflows/新书启动.md`
2. 按工作流创建项目目录
3. 填写 `framework.md` + `outline.md`
4. 创建 `entities/` 目录和设定卡
5. 开始章节生产

---

## 三、AI 协作原则

### 3.1 读取原则

1. **先读导航**：读 `CLAUDE.md` 和 `ai/README.md`，了解结构
2. **按需深入**：按任务类型读对应提示词、工作流、模板
3. **遵守规范**：读 `schema/` 目录下的规范文件

### 3.2 写入原则

1. **按模板输出**：使用 `ai/templates/` 下的模板
2. **遵守约束**：遵守 `ai/constraints/` 下的约束文件
3. **自动校验**：输出后跑 `ai/validation/` 下的校验规则

### 3.3 检索原则

1. **按任务检索**：用 `ai/search/按任务索引.md` 快速定位
2. **按标签检索**：用 Obsidian 标签窗格筛选
3. **全文检索**：用 Obsidian 全文搜索

---

## 四、相关文档

- [schema/AI协作规范.md](../schema/AI协作规范.md)：AI 读写优化规范
- [CLAUDE.md](../CLAUDE.md)：AI 协作指令
- [methods/QUICK_START.md](../methods/QUICK_START.md)：按症状找方法论
- [methods/SKILL.md](../methods/SKILL.md)：写作方法论
- [tools/工具仪表盘.md](../tools/工具仪表盘.md)：工具选型

---

> 本目录是 AI 读写知识库的专用入口。详细规范见对应链接。