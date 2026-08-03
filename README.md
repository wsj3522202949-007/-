---
id: idx-vault-root
type: index
area: 索引
status: active
tags: [vault, 总入口, 目录冻结]
title: 知识库总说明书（vault 唯一前门）
summary: vault 根级机器可读说明书——长期主题、活跃项目、8 目录冻结职责、30 秒速查、迁移状态。
source: 内部制定
created: 2026-07-31
updated: 2026-08-02
related:
  - schema/维护标准.md
  - schema/正文生命周期规范.md
  - schema/项目结构规范.md
see_also:
  - schema/frontmatter规范.md
  - schema/链接规范.md
---

# 知识库总说明书（vault 唯一前门）

> 本文件是 vault 根级的**机器可读说明书**。回答三个问题：**我在长期做什么、现在在写哪本书、卡住时去哪查**。
> 顶层目录职责已**冻结**（见 [冻结书](archive/迁移计划-顶层目录职责冻结.md)），新增内容只能进对应目录。

---

## 一、长期主题

**一句话**：用一套可复用的「方法论 + AI 工具 + 合规骨架」工程化地持续生产长篇网文（目标 300 万字 / 单本）。

三条长期主线，互为支撑：

| 主线 | 是什么 | 入口 |
|---|---|---|
| ✍️ **创作主线** | 每本一个合规项目目录（当前无活跃项目） | [项目目录](projects/README.md) |
| 📚 **方法论主线** | 从 50 份作家方法论 + 外部 Skill 蒸馏成的"照着做"网文创作系统（约 41 万字 / 115 文件） | [方法论导览](methods/导览.md) |
| 🛠️ **工具主线** | 3574 篇 AI 写作工具情报卡，可检索可筛选，按任务/约束选型 | [工具情报网](tools/README.md) |

---

## 二、活跃项目

| 书名 | 角色 | 题材 / 平台 | 当前阶段 | 进度 | 入口 |
|---|---|---|---|---|---|

> 当前无活跃项目

---

## 三、冻结的顶层目录结构

> 以下 8 个目录 + 本文件一经冻结，**不得新增、不得拆分、不得合并**。新增内容只能进对应目录。

| 目录 | 职责（一句话） | 当前内容 | 禁止放入 |
|---|---|---|---|
| `schema/` | 规范与契约 | 10 个规范文件 | 脚本、正文、工具卡 |
| `projects/` | 所有项目 | 当前无项目 | 方法论、工具卡、草稿（→drafts/） |
| `knowledge/` | 结构化知识实体 | craft/ 20篇 · genres/ 29篇 · platforms/ 8篇 · 中国网文/ 4篇 | 可执行 SOP、模板、工具卡 |
| `drafts/` | 写作中草稿 | inbox/ journal/ projects/ scratch/ | 已校验最终稿、归档 |
| `archive/` | 归档 | 项目骨架模板-旧版/ | 活跃项目内容、常用参考资料 |
| `references/` | 参考资料与外部素材 | 49 篇指南 + Skill 蒸馏 + 原始调研 + 原始来源包 | 自创的方法论、项目正文 |
| `methods/` | 可复用的方法论 | 18 篇 + templates/ 15 篇 + 项目骨架模板/ | 知识实体、工具卡 |
| `tools/` | 工具说明、选型与脚本 | cards/ 3574 卡 + 分类导航/ 21 MOC + scripts/ | 方法论正文、项目正文 |

**正文生命周期**：`drafts/`（写作中）→ `projects/*/chapters/`（已校验生产）→ `archive/`（归档保留）。详见 [正文生命周期规范](schema/正文生命周期规范.md)。

**项目标准结构**：每个项目根级只有 4 文件 + 2 目录（README / STATUS / framework / outline + chapters/ + entities/）。详见 [项目结构规范](schema/项目结构规范.md)。

---

## 四、30 秒速查（想做 X → 去 Y）

| 我现在想… | 直接去 |
|---|---|
| 按症状找方法论武器 | [QUICK_START](methods/QUICK_START.md) |
| 学去 AI 味 / 改稿 | [最强去AI味铁律](methods/最强去AI味铁律.md) |
| 搭大纲 / 人物 / 开篇 | [网文写作最强SOP](methods/网文写作最强SOP.md) + [模板库](methods/模板库.md) |
| 看平台红线 | [平台差异手册](methods/平台差异手册.md) |
| 找 / 对比 AI 写作工具 | [工具选型指南](tools/工具选型指南.md) · [任务选型速查](tools/任务选型速查.md) |
| 深读实战指南 / 溯源 | [参考素材入口](references/README.md) |
| 把 Word / 原稿入库成项目 | [原稿转创作知识库-SOP](methods/原稿转创作知识库-SOP.md) |
| 新建一本书 | [项目骨架模板](methods/项目骨架模板/README.md) |
| 防知识库变乱 / 跑门禁 | [维护标准](schema/维护标准.md) → [校验脚本](tools/scripts/validation/校验脚本.py) |

---

## 五、迁移状态

> vault 已从「`小说/` 包裹式」迁移到「8 目录扁平式」。`小说/` 目录已删除，内容全部进入 8 目录。

| 阶段 | 状态 | 说明 |
|---|---|---|
| Phase 0：创建骨架 | ✅ 完成 | 8 目录 + 本文件 |
| Phase 1：移动空目录 | ✅ 完成 | 收件箱/日记/资料 → drafts/ |
| Phase 2：archive → references | ✅ 完成 | 49 篇指南 + Skill 蒸馏 → references/ |
| Phase 3：库/ → tools/ | ✅ 完成 | 3604 工具卡 → tools/cards/ |
| Phase 4：projects/ 重构 | ✅ 完成 | 项目移至根级 projects/ |
| Phase 5：methods/ 拆分 | ✅ 完成 | craft/genres/platforms → knowledge/；SOP/模板 → methods/ |
| Phase 6：维护/ → schema/ + tools/ | ✅ 完成 | 规范文件 → schema/；脚本 → tools/scripts/validation/ |
| Phase 7：合并 README | ✅ 完成 | 三合一 → 本文件 |
| Phase 8：全库链接重写 | ✅ 完成 | 59 文件 127 处路径更新 |
| Phase 9：验证 | ✅ 通过 | ERROR=0 + WARN=0（校验脚本 PASS） |

完整迁移计划见 [迁移计划-顶层目录职责冻结](archive/迁移计划-顶层目录职责冻结.md)。

---

## 六、维护说明

- **编码**：全库 `.md` 统一 UTF-8 without BOM（已校验）。
- **frontmatter**：所有笔记层文件已补齐 10 通用字段（id/type/area/status/tags/title/summary/source/created/updated），工具卡 3604 篇全部补齐，0 缺失。规范见 [frontmatter 规范](schema/frontmatter规范.md)。
- **链接**：已废除 `[[wikilink]]` 作为唯一引用方式，改用标准 markdown 链接 + `related`/`see_also` 字段，规范见 [链接规范](schema/链接规范.md)。
- **提交前门禁**：动到带 frontmatter 的笔记后，跑 [校验脚本](tools/scripts/validation/校验脚本.py)，ERROR=0 再提交。当前状态：**PASS ✅（0 ERROR, 0 WARN）**。

---

## 七、新增系统（2026-08-02 优化）

### 7.1 目标级联系统

**目录**：`goals/`

**级联结构**：
```
3年愿景 (vision.md)
    ↓
年度目标 (yearly/)
    ↓
月度目标 (monthly/)
    ↓
周回顾 (weekly/)
    ↓
日任务 (daily/)
```

**快速导航**：
| 我想做什么 | 直接去 |
|---|---|
| 设定长期愿景 | `goals/vision.md` |
| 制定年度目标 | `goals/yearly/YYYY.md` |
| 分解月度目标 | `goals/monthly/YYYY-MM.md` |
| 执行周回顾 | `goals/weekly/YYYY-Www.md` |
| 记录日任务 | `goals/daily/YYYY-MM-DD.md` |
| 学习目标管理 | `goals/GUIDE.md` |

### 7.2 技能系统

**目录**：`ai/skills/`

**技能列表**：
| 技能 | 调用方式 | 用途 |
|---|---|---|
| `/daily` | 创建日记 | 每日写作进度跟踪 |
| `/weekly` | 周回顾 | 回顾本周成果 |
| `/write` | 写正文 | 生成正文内容 |
| `/revise` | 改稿 | 改稿润色 |
| `/check` | 自检 | 自动检查内容 |
| `/project` | 新建项目 | 一键生成项目骨架 |

**使用方法**：在 AI 对话中直接输入技能名称。

### 7.3 代理系统

**目录**：`ai/agents/`

**代理列表**：
| 代理 | 用途 | 触发方式 |
|---|---|---|
| note-organizer | 整理笔记、修复链接 | 手动/定期 |
| weekly-reviewer | 引导周回顾 | 每周一次 |
| goal-aligner | 检查目标对齐 | 每月一次 |
| inbox-processor | GTD 式收件箱处理 | 每日一次 |

**使用方法**：在 AI 对话中输入代理名称。

### 7.4 定期维护工作流

**目录**：`ai/maintenance/`

**维护任务**：
| 任务 | 用途 | 执行时间 |
|---|---|---|
| 收件箱处理 | 整理未分类内容 | 每日晚上 |
| 周回顾 | 回顾本周成果 | 每周日晚上 |
| 笔记整理 | 整理笔记、修复链接 | 每周六上午 |
| 月回顾 | 回顾本月成果 | 每月最后一天 |

**使用方法**：在 AI 对话中输入维护任务名称。

### 7.5 Dataview 动态视图

**目录**：`tools/Dataview索引.md`、`methods/Dataview索引.md`

**视图列表**：
| 视图 | 用途 |
|---|---|
| 工具选型矩阵 | 按评级筛选工具 |
| 按任务找工具 | 按任务筛选工具 |
| 方法论速查 | 查询方法论 |
| 目标进度 | 查询目标进度 |

**使用方法**：在 Obsidian 中打开索引文件，直接查看动态视图。

---

> 本文件是 vault 根级的机器可读说明书。详细规范见对应链接。
#   -  
 