---
id: guide-claude
type: guide
area: 索引
status: active
tags: [AI指令, CLAUDE, 导航, 读写优化, AI可执行]
title: AI 协作指令（CLAUDE.md）— AI 可执行版本
summary: AI 进入此知识库的唯一导航——目录结构、速查表、合规红线、写作驱动规则、AI可执行系统、校验流程。
source: 内部制定
created: 2026-07-30
updated: 2026-08-03
related:
  - README.md
  - schema/frontmatter规范.md
  - schema/链接规范.md
  - schema/正文生命周期规范.md
  - schema/项目结构规范.md
  - schema/坑点记录.md
  - schema/AI协作规范.md
  - ai/README.md
see_also:
  - schema/维护标准.md
  - methods/QUICK_START.md
ai_instructions:
  purpose: "AI 进入知识库的唯一导航，包含所有AI可执行的系统和指令"
  usage: "读取本文件了解知识库结构和AI可执行系统，然后根据用户需求调用对应系统"
---

# AI 协作指令（AI 读写优化版）

> 本文件是 AI 进入此知识库的**唯一导航**。读完即可：定位内容、遵守红线、正确建/改文件、跑校验。

---

## 🚀 AI 快速启动（30 秒）

**第一次进入知识库？按顺序读这 3 个文件：**

1. **本文件**（CLAUDE.md）— 导航 + 红线 + 规则
2. **[ai/README.md](ai/README.md)** — AI 专用资源总览
3. **[methods/QUICK_START.md](methods/QUICK_START.md)** — 按症状找方法论

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
| 跑校验 | `python tools/scripts/validation/校验脚本.py` |

---

## 一、这是什么

工程化生产长篇网文的知识库（目标：单本 300 万字）。8 目录冻结，职责见 README.md。

**AI 专用目录**：`ai/`（提示词、工作流、模板、约束、校验、检索）。

**目录结构：**

```
E:\个人知识库\
├── README.md              # 知识库总说明书
├── CLAUDE.md              # 本文件（AI 导航）
├── schema/                # 规范与契约（13 文件）
├── methods/               # 可复用方法论（79 文件）
├── knowledge/             # 结构化知识实体（63 文件）
├── ai/                    # AI 专用资源（26 文件）
├── tools/                 # 工具说明与脚本（3641 文件）
├── projects/              # 项目目录（当前无活跃项目）
├── drafts/                # 写作中草稿
├── references/            # 参考资料（916 文件）
└── archive/               # 归档
```

---

## 二、AI 读写优化要点

### 2.1 读取优化

- **Frontmatter 结构化**：所有笔记层文件有 10 通用字段（id/type/area/status/tags/title/summary/source/created/updated）
- **类型系统**：15 种类型（tool/ref/guide/index/moc/template/setting/character/chapter/project/...）
- **标签系统**：22 个受控标签，支持按任务/平台/约束筛选
- **链接系统**：标准 markdown 链接 + `related`/`see_also` 字段，禁用 `[[wikilink]]`

### 2.2 写入优化

- **模板系统**：`ai/templates/` 下有正文章节、大纲、人物卡、设定卡模板
- **规范文件**：`schema/` 下有 frontmatter/链接/结构/生命周期等规范
- **校验脚本**：`tools/scripts/validation/校验脚本.py` 自动验证

### 2.3 检索优化

- **按任务检索**：`ai/search/按任务索引.md`
- **按工具检索**：`ai/search/按工具索引.md`
- **按平台检索**：`ai/search/按平台索引.md`
- **全文检索**：Obsidian 内置搜索

---

## 三、合规红线（不可违反）

- 所有内容遵守 PRC 法律法规——不可协商的底线
- 邪不压正——违法行为最终面临法律制裁，犯罪不得美化
- 主角复仇走合法渠道（取证→举报→司法），绝非私刑
- 打斗仅限正当防卫（对方先动手→主角在必要限度内反击），主角绝不先动手

---

## 四、正文写作硬约束

- 每章 2300–2700 字，文件名 `第NNN章-标题.md`
- 章末钩子：5 种强钩子之一，禁"下章预告"括号
- 正文生命周期：`drafts/` → `projects/*/chapters/` → `archive/`
- 项目结构：每项目 4 文件 + 2 目录（README / STATUS / framework / outline + chapters/ + entities/）

---

## 五、写作驱动规则（知识库→正文）

> **核心原则：不让 AI 从零写正文，而是让 AI 从已有设定和方法论中组织内容。**

1. **写正文前必读**：目标项目的 `framework.md` + `outline.md` + 相关 `entities/` + 最近 2-3 章正文
2. **卡住时查方法论**：按 `methods/QUICK_START.md` 的"症状→武器"表定位
3. **大纲生成**：基于已有 framework/outline 扩展，不凭空编造；每节标注信息来源
4. **正文生成**：基于细纲 + 设定卡片写，不添加设定中没有的内容；需补充时标注【待补充】
5. **每章完成后**：跑 `ai/validation/正文校验.md` + 更新 `STATUS.md` 进度

---

## 六、AI 协作边界

- **可以**：读取所有文件、按规范创建/修改文件、写草稿到 `drafts/`、补充 frontmatter
- **不能**：修改 `archive/`、跳过自检把草稿放进 `chapters/`、新增顶层目录、违反合规红线
- **每次犯错**：记录到 `schema/坑点记录.md`（问题/表现/修复/预防四要素）
- **修改后必做**：跑校验脚本，ERROR=0 才算完成

---

## 七、AI 专用资源

| 资源类型 | 路径 | 用途 |
|---|---|---|
| 提示词 | `ai/prompts/` | 写正文、写大纲、改稿、去AI味、自检 |
| 工作流 | `ai/workflows/` | 新书启动、章节生产、改稿流程、签约体检 |
| 模板 | `ai/templates/` | 正文章节、大纲、人物卡、设定卡 |
| 约束 | `ai/constraints/` | 合规红线、写作硬约束、格式要求、禁忌清单 |
| 校验 | `ai/validation/` | 正文校验、大纲校验、人物卡校验 |
| 检索 | `ai/search/` | 按任务、按工具、按平台 |

---

## 八、常见 AI 任务流程

### 8.1 写一章正文

```
1. 读 ai/prompts/写正文.md（了解提示词）
2. 读 ai/templates/正文章节模板.md（了解格式）
3. 读目标项目的 framework.md + outline.md + entities/
4. 读最近 2-3 章正文（了解上下文）
5. 按模板生成正文
6. 跑 ai/validation/正文校验.md（自检）
7. 写入 projects/*/chapters/第NNN章-标题.md
```

### 8.2 写大纲

```
1. 读 ai/prompts/写大纲.md
2. 读 ai/templates/大纲模板.md
3. 读目标项目的 framework.md
4. 按模板生成大纲
5. 跑 ai/validation/大纲校验.md
6. 写入 projects/*/outline.md
```

### 8.3 改稿/去AI味

```
1. 读 ai/prompts/改稿.md 或 ai/prompts/去AI味.md
2. 读目标章节正文
3. 按提示词改稿
4. 跑 ai/validation/正文校验.md
5. 覆盖原文件
```

### 8.4 新建一本书

```
1. 读 ai/workflows/新书启动.md
2. 按工作流创建项目目录
3. 填写 framework.md + outline.md
4. 创建 entities/ 目录和设定卡
5. 开始章节生产
```

---

## 九、AI 可执行系统（2026-08-02 优化）

### 9.1 目标级联系统

**目录**：`goals/`　**入口**：`goals/README.md`

**级联结构**：
```
3年愿景 (vision.md) → 年度 (yearly/) → 月度 (monthly/) → 周 (weekly/) → 日 (daily/)
```

**AI 指令**：`create-vision` / `create-yearly` / `create-monthly` / `create-weekly` / `/daily` / `query-progress`

### 9.2 技能系统

**目录**：`ai/skills/`　**入口**：`ai/skills/README.md`

| 技能 | 触发条件 | 输入 | 输出 |
|---|---|---|---|
| `/daily` | 用户输入 `/daily` | 日期（可选） | 创建日记文件 |
| `/weekly` | 用户输入 `/weekly` | 周数（可选） | 创建周回顾文件 |
| `/write` | 用户输入 `/write` | 章节名/大纲 | 生成正文内容 |
| `/revise` | 用户输入 `/revise` | 文件路径/内容 | 改稿后内容 |
| `/check` | 用户输入 `/check` | 文件路径/目录 | 检查报告 |
| `/project` | 用户输入 `/project` | 书名/类型 | 创建项目骨架 |

### 9.3 代理系统

**目录**：`ai/agents/`　**入口**：`ai/agents/README.md`

| 代理 | 触发条件 | 执行步骤 | 输出 |
|---|---|---|---|
| `note-organizer` | 输入 `note-organizer` | 扫描→分析→整理→报告 | 整理报告 |
| `weekly-reviewer` | 输入 `weekly-reviewer` | 收集→分析→回顾→规划 | 周回顾报告 |
| `goal-aligner` | 输入 `goal-aligner` | 扫描→分析→检查→报告 | 对齐报告 |
| `inbox-processor` | 输入 `inbox-processor` | 扫描→分类→处理→报告 | 处理报告 |

### 9.4 定期维护工作流

**目录**：`ai/maintenance/`　**入口**：`ai/maintenance/README.md`

| 任务 | 触发条件 | 输出 |
|---|---|---|
| 收件箱处理 | 每日晚上 | 处理报告 |
| 周回顾 | 每周日晚上 | 周回顾报告 |
| 笔记整理 | 每周六上午 | 整理报告 |
| 月回顾 | 每月最后一天 | 月回顾报告 |

### 9.5 Dataview 动态视图

**入口**：`tools/Dataview索引.md`、`methods/Dataview索引.md`

| 视图 | 用途 |
|---|---|
| 工具选型矩阵 | 按评级筛选工具 |
| 按任务找工具 | 按任务筛选工具 |
| 方法论速查 | 查询方法论 |
| 目标进度 | 查询目标进度 |

---

## 十、AI 执行流程

### 10.1 识别用户意图
1. 分析用户输入，确定需要的操作
2. 识别触发条件（技能/代理/工作流）
3. 确定需要读取的文件

### 10.2 读取相关文件
1. 读取对应的技能/代理/工作流文件
2. 了解执行步骤和输出格式
3. 读取相关的目标、项目、方法论文件

### 10.3 执行操作
1. 按照文件中的步骤执行
2. 创建或修改文件
3. 生成报告或返回结果

### 10.4 返回结果
1. 返回查询结果
2. 创建文件并返回路径
3. 生成报告并返回内容

---

> 本文件是 AI 进入知识库的唯一导航。详细规范见对应链接。
