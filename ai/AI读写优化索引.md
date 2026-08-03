---
id: idx-ai-optimization
type: index
area: 索引
status: active
tags: [AI, 优化, 读写, 索引]
title: AI 读写优化索引
summary: AI 读写知识库的优化索引——优化要点、关键路径、常见任务、快速参考。
source: 内部制定
created: 2026-08-02
updated: 2026-08-02
related:
  - CLAUDE.md
  - ai/README.md
  - schema/AI协作规范.md
see_also:
  - schema/frontmatter规范.md
  - schema/链接规范.md
---

# 🤖 AI 读写优化索引

> 本文件是 AI 读写知识库的**优化索引**。读完即可：了解优化要点、快速定位资源、高效完成任务。

---

## 一、优化要点速查

### 1.1 读取优化

| 优化项 | 说明 | 关键文件 |
|---|---|---|
| Frontmatter 结构化 | 所有笔记层文件有 10 通用字段 | `schema/frontmatter规范.md` |
| 类型系统 | 15 种类型（tool/ref/guide/index/moc/template/...） | `schema/frontmatter规范.md` |
| 标签系统 | 22 个受控标签，支持按任务/平台/约束筛选 | `schema/frontmatter规范.md` |
| 链接系统 | 标准 markdown 链接 + `related`/`see_also` 字段 | `schema/链接规范.md` |
| 目录结构 | 8 目录冻结，职责清晰 | `README.md` |
| 索引导航 | README.md + 仪表盘 + 速查表 | `README.md` + `CLAUDE.md` |

### 1.2 写入优化

| 优化项 | 说明 | 关键文件 |
|---|---|---|
| 模板系统 | 15+ 模板（正文、大纲、人物卡、设定卡） | `ai/templates/` |
| 规范文件 | 10 个规范（frontmatter/链接/结构/生命周期） | `schema/` |
| 校验脚本 | 自动验证（正文/大纲/人物卡校验） | `ai/validation/` |
| 提示词 | 5 个提示词（写正文/写大纲/改稿/去AI味/自检） | `ai/prompts/` |
| 工作流 | 6 个工作流（新书启动/章节生产/改稿流程/签约体检） | `ai/workflows/` |

### 1.3 检索优化

| 优化项 | 说明 | 关键文件 |
|---|---|---|
| 按任务检索 | 按任务类型快速定位 | `ai/search/按任务索引.md` |
| 按工具检索 | 按工具类型快速定位 | `ai/search/按工具索引.md` |
| 按平台检索 | 按平台类型快速定位 | `ai/search/按平台索引.md` |
| 标签检索 | 22 个受控标签，支持多维度筛选 | Obsidian 标签窗格 |
| 全文检索 | Obsidian 内置全文搜索 | Obsidian 搜索 |

---

## 二、关键路径速查

### 2.1 导航路径

| 我想做什么 | 直接去 |
|---|---|
| 了解知识库结构 | `README.md` |
| 了解 AI 协作规则 | `CLAUDE.md` |
| 了解 AI 专用资源 | `ai/README.md` |
| 了解 AI 读写优化 | `schema/AI协作规范.md` |
| 按症状找方法论 | `methods/QUICK_START.md` |

### 2.2 写作路径

| 我想做什么 | 直接去 |
|---|---|
| 写正文 | `ai/prompts/写正文.md` + `ai/templates/正文章节模板.md` |
| 写大纲 | `ai/prompts/写大纲.md` + `ai/templates/大纲模板.md` |
| 改稿/去AI味 | `ai/prompts/改稿.md` + `ai/prompts/去AI味.md` |
| 自检 | `ai/prompts/自检.md` + `ai/validation/正文校验.md` |
| 新书启动 | `ai/workflows/新书启动.md` |
| 章节生产 | `ai/workflows/章节生产.md` |

### 2.3 资源路径

| 我想做什么 | 直接去 |
|---|---|
| 查方法论 | `methods/QUICK_START.md`（按症状查） |
| 查工具 | `tools/README.md` + `tools/任务选型速查.md` |
| 查规范 | `schema/` 目录（frontmatter/链接/结构） |
| 查模板 | `ai/templates/` 目录 |
| 查提示词 | `ai/prompts/` 目录 |
| 查工作流 | `ai/workflows/` 目录 |
| 查约束 | `ai/constraints/` 目录 |
| 查校验 | `ai/validation/` 目录 |
| 查检索 | `ai/search/` 目录 |

---

## 三、常见 AI 任务流程

### 3.1 写一章正文

```
1. 读 ai/prompts/写正文.md（了解提示词）
2. 读 ai/templates/正文章节模板.md（了解格式）
3. 读目标项目的 framework.md + outline.md + entities/
4. 读最近 2-3 章正文（了解上下文）
5. 按模板生成正文
6. 跑 ai/validation/正文校验.md（自检）
7. 写入 projects/*/chapters/第NNN章-标题.md
```

### 3.2 写大纲

```
1. 读 ai/prompts/写大纲.md
2. 读 ai/templates/大纲模板.md
3. 读目标项目的 framework.md
4. 按模板生成大纲
5. 跑 ai/validation/大纲校验.md
6. 写入 projects/*/outline.md
```

### 3.3 改稿/去AI味

```
1. 读 ai/prompts/改稿.md 或 ai/prompts/去AI味.md
2. 读目标章节正文
3. 按提示词改稿
4. 跑 ai/validation/正文校验.md
5. 覆盖原文件
```

### 3.4 新建一本书

```
1. 读 ai/workflows/新书启动.md
2. 按工作流创建项目目录
3. 填写 framework.md + outline.md
4. 创建 entities/ 目录和设定卡
5. 开始章节生产
```

---

## 四、优化效果验证

### 4.1 当前状态

- **总文件数**：4517
- **有 frontmatter**：4003（88.6%）
- **无 frontmatter**：514（11.4%，主要是 references/原始来源包/）
- **类型分布**：3588 tool + 160 ref + 21 moc + 19 index + 12 guide + 11 template + ...
- **标签分布**：22 个受控标签，支持多维度筛选

### 4.2 优化效果

- **读取效率**：通过 frontmatter 结构化、类型系统、标签系统，AI 可快速定位目标文件
- **写入效率**：通过模板系统、规范文件、校验脚本，AI 可高效生成规范内容
- **检索效率**：通过按任务/工具/平台索引、标签检索、全文检索，AI 可快速找到所需资源

---

## 五、相关文档

- [CLAUDE.md](../CLAUDE.md)：AI 协作指令（导航 + 红线 + 规则）
- [ai/README.md](../ai/README.md)：AI 协作入口（专用资源总览）
- [schema/AI协作规范.md](../schema/AI协作规范.md)：AI 读写优化规范
- [schema/frontmatter规范.md](../schema/frontmatter规范.md)：Frontmatter Schema 规范
- [schema/链接规范.md](../schema/链接规范.md)：链接规范
- [methods/QUICK_START.md](../methods/QUICK_START.md)：按症状找方法论

---

> 本文件是 AI 读写知识库的优化索引。详细规范见对应链接。