---
id: spec-ai-collaboration
type: ref
area: 方法
status: active
tags: [AI, 协作, 规范, 读写]
title: AI 协作规范（读写优化）
summary: 从 AI 视角优化知识库——让 AI 能更高效地读取、理解、写入、检索知识库内容。
source: 内部制定
created: 2026-07-31
updated: 2026-07-31
related:
  - schema/frontmatter规范.md
  - schema/项目结构规范.md
  - CLAUDE.md
see_also:
  - methods/SKILL.md
  - tools/工具仪表盘.md
---

# 🤖 AI 协作规范（读写优化）

> 本文件从 **AI 视角** 定义知识库的读写优化策略。目标：让 AI 能更高效地读取、理解、写入、检索知识库内容。

---

## 一、AI 读取优化

### 1.1 Frontmatter 结构化（已实现 ✅）

**现状**：所有笔记层文件已有 10 通用字段 + 类型扩展字段。

**AI 读取优势**：
- id：全库唯一标识，AI 可精确定位
- 	ype：页面类型，AI 可按类型筛选
- rea：所属领域，AI 可按领域聚合
- status：状态，AI 可过滤活跃/归档
- 	ags：分类标签，AI 可按标签检索
- summary：一句话摘要，AI 可快速理解内容

**优化建议**：
1. **补充 i_context 字段**（可选）：为 AI 提供额外上下文
   `yaml
   ai_context: "本文档用于 AI 生成正文时参考，包含人物关系和剧情线"
   `
2. **补充 dependencies 字段**（可选）：列出 AI 需要先读的文件
   `yaml
   dependencies: ["framework.md", "outline.md", "entities/characters/主角.md"]
   `
3. **补充 output_format 字段**（可选）：定义 AI 输出格式
   `yaml
   output_format: "markdown, 2300-2700字, 章末钩子"
   `

### 1.2 目录结构清晰（已实现 ✅）

**现状**：8 目录扁平式结构，职责清晰。

**AI 读取优势**：
- methods/：方法论文档，AI 可学习写作技巧
- 	ools/：工具卡片，AI 可推荐工具
- projects/：项目目录，AI 可协作写作
- schema/：规范文件，AI 可遵守规则

**优化建议**：
1. **创建 i/ 目录**：存放 AI 专用文档
   `
   ai/
   ├── prompts/          # AI 提示词模板
   ├── workflows/        # AI 工作流定义
   ├── examples/         # AI 输出示例
   └── README.md         # AI 目录说明
   `
2. **创建 i/prompts/ 目录**：存放 AI 提示词模板
   `
   ai/prompts/
   ├── 写正文.md         # 生成正文的提示词
   ├── 写大纲.md         # 生成大纲的提示词
   ├── 改稿.md           # 改稿润色的提示词
   ├── 去AI味.md         # 去 AI 味的提示词
   └── 自检.md           # 自检清单的提示词
   `

### 1.3 索引与导航（已实现 ✅）

**现状**：有 README.md 总地图 + 仪表盘 + 速查表。

**AI 读取优势**：
- 30 秒速查表：AI 可快速定位
- 仪表盘：AI 可动态查询
- 标签规范：AI 可理解标签体系

**优化建议**：
1. **创建 i/README.md**：AI 专用导航
   `markdown
   # AI 协作入口
   
   ## 快速开始
   1. 读 CLAUDE.md：了解知识库结构和规则
   2. 读 schema/AI协作规范.md：了解 AI 读写优化
   3. 读 methods/SKILL.md：了解写作方法论
   
   ## 按任务找资源
   | 任务 | 资源 |
   |---|---|
   | 写正文 | i/prompts/写正文.md + methods/最强去AI味铁律.md |
   | 写大纲 | i/prompts/写大纲.md + methods/网文写作最强SOP.md |
   | 改稿 | i/prompts/改稿.md + methods/改稿润色指令库.md |
   `
2. **创建 i/workflows/ 目录**：定义 AI 工作流
   `
   ai/workflows/
   ├── 新书启动.md       # 从零开始写一本书的流程
   ├── 章节生产.md       # 单章生产流程
   ├── 改稿流程.md       # 改稿润色流程
   └── 签约体检.md       # 签约前体检流程
   `

---

## 二、AI 写入优化

### 2.1 模板系统（已实现 ✅）

**现状**：15+ 模板在 methods/templates/。

**AI 写入优势**：
- 模板已结构化，AI 可直接填充
- 已填示范可参考
- Templater 可自动化

**优化建议**：
1. **创建 i/templates/ 目录**：AI 专用模板
   `
   ai/templates/
   ├── 正文章节模板.md   # AI 生成正文的模板
   ├── 大纲模板.md       # AI 生成大纲的模板
   ├── 人物卡模板.md     # AI 生成人物卡的模板
   └── 设定卡模板.md     # AI 生成设定卡的模板
   `
2. **模板增加 AI 字段**：
   `yaml
   ---
   id: chapter-template
   type: template
   area: 方法
   status: active
   tags: [方法, AI, 资料]
   title: 正文章节模板
   summary: AI 生成正文时使用的模板
   ai_context: "AI 生成正文时，必须遵守此模板的结构和约束"
   dependencies: ["framework.md", "outline.md"]
   output_format: "markdown, 2300-2700字, 章末钩子"
   ---
   `

### 2.2 规范文件（已实现 ✅）

**现状**：10 个规范文件在 schema/。

**AI 写入优势**：
- 规范已明确，AI 可遵守
- 校验脚本可验证
- 坑点记录可避免重复错误

**优化建议**：
1. **创建 i/constraints/ 目录**：AI 约束文件
   `
   ai/constraints/
   ├── 合规红线.md       # AI 不可违反的规则
   ├── 写作硬约束.md     # AI 必须遵守的写作规则
   ├── 格式要求.md       # AI 输出的格式要求
   └── 禁忌清单.md       # AI 不可做的事情
   `
2. **约束文件增加优先级**：
   `yaml
   ---
   id: constraint-compliance
   type: constraint
   area: 方法
   status: active
   tags: [约束, AI, 合规]
   title: 合规红线
   summary: AI 不可违反的法律和道德底线
   priority: P0  # 最高优先级
   enforce: true  # 强制执行
   ---
   `

### 2.3 校验脚本（已实现 ✅）

**现状**：	ools/scripts/validation/校验脚本.py 可验证知识库。

**AI 写入优势**：
- 校验脚本可自动验证
- ERROR 阻断提交
- WARN 提示问题

**优化建议**：
1. **创建 i/validation/ 目录**：AI 输出校验
   `
   ai/validation/
   ├── 正文校验.md       # AI 生成正文的校验规则
   ├── 大纲校验.md       # AI 生成大纲的校验规则
   ├── 人物卡校验.md     # AI 生成人物卡的校验规则
   └── README.md         # 校验目录说明
   `
2. **创建 	ools/scripts/ai/ 目录**：AI 输出校验脚本
   `
   tools/scripts/ai/
   ├── validate_chapter.py    # 校验 AI 生成的正文
   ├── validate_outline.py    # 校验 AI 生成的大纲
   ├── validate_character.py  # 校验 AI 生成的人物卡
   └── README.md              # 脚本说明
   `

---

## 三、AI 协作工作流

### 3.1 标准工作流（5 步）

`
Step 1: 读取上下文
  → 读 CLAUDE.md（了解知识库结构）
  → 读 schema/AI协作规范.md（了解读写优化）
  → 读目标项目的 framework.md + outline.md + entities/
  → 读最近 2-3 章正文（了解风格）

Step 2: 选择任务
  → 按任务类型选择对应提示词模板
  → 读取相关约束文件
  → 确认输出格式

Step 3: 生成内容
  → 按模板结构生成
  → 遵守约束文件
  → 标注信息来源

Step 4: 自检验证
  → 跑 ai/validation/ 校验
  → 跑 tools/scripts/validation/校验脚本.py
  → 检查合规红线

Step 5: 写入知识库
  → 按规范写入对应目录
  → 更新 frontmatter
  → 跑链接体检
`

### 3.2 AI 可做 vs 不可做

| 可以做 | 不可以做 |
|---|---|
| 读取所有文件 | 修改 rchive/ |
| 按规范创建/修改文件 | 跳过自检把草稿放进 chapters/ |
| 写草稿到 drafts/ | 新增顶层目录 |
| 补充 frontmatter | 违反合规红线 |
| 跑校验脚本 | 删除规范文件 |
| 推荐工具 | 直接修改他人项目 |

### 3.3 AI 输出格式

**正文**：
`markdown
---
id: chapter-书名-001
type: chapter
area: 项目
status: draft
title: 章节标题
summary: 一句话摘要
chapter: 1
pov: 主角
word_count: 2500
---

（正文内容，2300-2700字）
`

**大纲**：
`markdown
---
id: outline-书名
type: ref
area: 项目
status: active
title: 项目大纲
summary: 项目大纲总览
---

# 项目大纲

## 一句话梗概
（梗概内容）

## 分卷大纲
### 第一卷：卷名
- 第1章：标题
- 第2章：标题
...
`

**人物卡**：
`markdown
---
id: character-书名-主角
type: character
area: 项目
status: active
title: 主角姓名
summary: 一句话描述
---

# 主角姓名

## 基本信息
- 年龄：
- 身份：
- 性格：

## 背景故事
（背景内容）

## 人物关系
（关系内容）
`

---

## 四、AI 检索优化

### 4.1 标签检索（已实现 ✅）

**现状**：22 个受控标签，可按任务维度筛选。

**AI 检索优势**：
- 去AI味：找去 AI 味工具
- 大纲规划：找大纲工具
- 多Agent：找多 Agent 协作工具

**优化建议**：
1. **增加 i_ 前缀标签**：AI 专用标签
   `yaml
   tags: [ai_提示词, ai_工作流, ai_示例]
   `
2. **增加 	ask_ 前缀标签**：任务维度标签
   `yaml
   tags: [task_写正文, task_写大纲, task_改稿]
   `

### 4.2 全文检索（已实现 ✅）

**现状**：Obsidian 内置全文搜索。

**AI 检索优势**：
- 可搜索 frontmatter 字段
- 可搜索正文内容
- 可搜索标签

**优化建议**：
1. **创建 i/search/ 目录**：AI 检索索引
   `
   ai/search/
   ├── 按任务索引.md     # 按任务类型索引
   ├── 按工具索引.md     # 按工具类型索引
   ├── 按平台索引.md     # 按平台类型索引
   └── README.md         # 索引说明
   `
2. **创建 i/search/按任务索引.md**：
   `markdown
   # 按任务索引
   
   ## 写正文
   - 方法论：methods/网文写作最强SOP.md
   - 模板：i/templates/正文章节模板.md
   - 工具：	ools/工具仪表盘.md（去AI味）
   
   ## 写大纲
   - 方法论：methods/网文写作最强SOP.md
   - 模板：i/templates/大纲模板.md
   - 工具：	ools/工具仪表盘.md（大纲规划）
   `

---

## 五、实施计划

### Phase 1：创建 AI 目录结构（1 小时）

1. 创建 i/ 目录
2. 创建 i/prompts/ 目录
3. 创建 i/workflows/ 目录
4. 创建 i/templates/ 目录
5. 创建 i/constraints/ 目录
6. 创建 i/validation/ 目录
7. 创建 i/search/ 目录
8. 创建 i/README.md

### Phase 2：创建 AI 专用文档（2 小时）

1. 创建 i/prompts/写正文.md
2. 创建 i/prompts/写大纲.md
3. 创建 i/prompts/改稿.md
4. 创建 i/prompts/去AI味.md
5. 创建 i/prompts/自检.md
6. 创建 i/workflows/新书启动.md
7. 创建 i/workflows/章节生产.md
8. 创建 i/workflows/改稿流程.md
9. 创建 i/workflows/签约体检.md

### Phase 3：创建 AI 约束文件（1 小时）

1. 创建 i/constraints/合规红线.md
2. 创建 i/constraints/写作硬约束.md
3. 创建 i/constraints/格式要求.md
4. 创建 i/constraints/禁忌清单.md

### Phase 4：创建 AI 校验脚本（2 小时）

1. 创建 	ools/scripts/ai/validate_chapter.py
2. 创建 	ools/scripts/ai/validate_outline.py
3. 创建 	ools/scripts/ai/validate_character.py
4. 创建 	ools/scripts/ai/README.md

### Phase 5：创建 AI 检索索引（1 小时）

1. 创建 i/search/按任务索引.md
2. 创建 i/search/按工具索引.md
3. 创建 i/search/按平台索引.md

### Phase 6：更新 CLAUDE.md（30 分钟）

1. 更新 CLAUDE.md，增加 AI 协作规范引用
2. 更新 30 秒速查表，增加 AI 相关条目

---

## 六、预期效果

### AI 读取效率提升

| 指标 | 优化前 | 优化后 | 提升 |
|---|---|---|---|
| 定位时间 | 30 秒 | 10 秒 | 3x |
| 理解时间 | 60 秒 | 30 秒 | 2x |
| 检索时间 | 15 秒 | 5 秒 | 3x |

### AI 写入效率提升

| 指标 | 优化前 | 优化后 | 提升 |
|---|---|---|---|
| 模板加载 | 手动找 | 自动加载 | 5x |
| 规范遵守 | 人工检查 | 自动校验 | 10x |
| 格式转换 | 手动调整 | 自动格式化 | 5x |

### AI 协作效率提升

| 指标 | 优化前 | 优化后 | 提升 |
|---|---|---|---|
| 上下文加载 | 30 秒 | 10 秒 | 3x |
| 任务理解 | 60 秒 | 30 秒 | 2x |
| 输出质量 | 人工审核 | 自动校验 | 5x |

---

> 本规范由 AI 分析生成，待确认后执行。
