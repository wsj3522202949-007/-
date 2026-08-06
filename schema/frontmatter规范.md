---
id: spec-frontmatter
type: ref
area: 方法
status: active
tags: [frontmatter, schema, 规范]
title: Frontmatter Schema 规范
summary: 全库 frontmatter 统一标准——平键为主，通用字段 + 各类型扩展字段 + 受控词表 + 旧格式迁移映射。
source: 内部制定
created: 2026-07-30
updated: 2026-07-31
related:
  - schema/维护标准.md
  - schema/链接规范.md
  - 库/标签规范.md
see_also:
  - tools/scripts/validation/校验脚本.py
  - ../methods/工具/链接体检与修复.py
---

> ↩ **回总地图**：[🗺️ 知识库总地图](../README.md) · [🛡️ 维护标准](维护标准.md)
> 本文件是全库 frontmatter 的**权威 schema 规范**。`维护标准.md` §1.2 标签合规以本文件为准。
> 配套机检：`tools/scripts/validation/校验脚本.py` 的 `[B]` `[C]` `[F]` `[G]` 检查项。

---

## 一、设计原则

1. **平键为主**：`type` `area` `status` 写成独立 YAML 键（`type: ref`），不塞进 `tags`。
2. **tags 回归纯分类**：`tags` 只放关键词标签（如 `去AI味` `大纲`），不再承担命名空间职责。
3. **通用字段全覆盖**：所有带 frontmatter 的文件至少包含 §二 的 10 个通用字段。
4. **按类型扩展**：chapter/character/setting/project/tool 各有专有扩展字段（§三）。
5. **受控词表**：`type` `area` `status` 取值受控，不在词表内的值触发 ERROR。

---

## 二、通用字段（所有带 frontmatter 的文件必须包含）

| 字段 | 类型 | 必填 | 说明 | 示例 |
|---|---|---|---|---|
| `id` | string | ✅ | 全库唯一标识，格式 `<type>-<slug>` | `ref-结构学` |
| `type` | string | ✅ | 页面类型，受控词（§四） | `ref` |
| `area` | string | ✅ | 所属领域，受控词（§四） | `方法` |
| `status` | string | ✅ | 状态，受控词（§四） | `active` |
| `tags` | string[] | ❌ | 分类标签（纯关键词，非命名空间） | `[去AI味, 大纲]` |
| `title` | string | ✅ | 页面标题（显示名） | `结构学` |
| `summary` | string | ✅ | 一句话摘要（≤80字） | `三幕/节拍表/Scene-Sequel…` |
| `source` | string | ❌ | 来源（URL / 书名 / 作者） | `Reedsy Prologues` |
| `created` | date | ✅ | 创建日期 `YYYY-MM-DD` | `2026-07-30` |
| `updated` | date | ✅ | 更新日期 `YYYY-MM-DD` | `2026-07-30` |
| `related` | string[] | ❌ | 结构性关联文件（vault 根相对路径，知识图谱边） | `[craft/结构学.md, craft/大纲工程.md]` |
| `see_also` | string[] | ❌ | 扩展阅读推荐（vault 根相对路径，弱关联） | `[craft/卡文急救.md]` |
| `historical` | bool | ❌ | 历史记录标记：`true` 时校验器豁免内容级检查（旧路径/断链/重复ID/编码等），仅统计计数 | `true` |

> `source` 非必填——原创内容可不填；外部资料必填。
> `related`/`see_also` 路径为 **vault 根相对路径**（含 `.md`），区别于 markdown 链接的文件相对路径。详见 [链接规范.md](链接规范.md) §四。

### 2.1 `historical` 字段语义

`historical: true` 用于**历史报告 / 归档记录**：声明该文件为历史记录后，统一门禁
（`run_all.py` 与 `链接检查器-修复版.py`）不再对其内容做质量检查（frontmatter
严格字段、旧路径残留、重复 ID、编码、断链均豁免），只在报告中单独统计
`historical_files`。判定以 frontmatter 为准，**优先于目录排除与文本标记**
（如 `[历史路径]`）——历史文档可放在任何目录而不会被门禁误报。

- 适用对象：一次性报告（`maintenance/reports/`）、归档记录（`archive/`）等不再维护的文件。
- 不适用：现行参考文档（如 `references/` 摘要、排错手册）——它们仍须遵守全部规范。
- 注意：声明 `historical: true` 的前提是文件**有 frontmatter**；无 frontmatter 的文件
  无法声明，仍按原规则处理（严格区缺 frontmatter = ERROR）。

---

## 三、各类型扩展字段

### 3.1 chapter（正文章节）

```yaml
---
id: chapter-书名-001
type: chapter
area: 项目
status: draft
title: 汇报会上的新甲方
summary: 林晚星在汇报会上遭遇甲方突变，被迫用超脑能力化解危机。
source: ""
created: 2026-07-30
updated: 2026-07-30
chapter: 1
pov: 林晚星
location: 科技园会议室
characters: [林晚星, 陆远, 陈守义]
word_count: 2600
---
```

| 扩展字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `chapter` | int | ✅ | 章节序号（与文件名 `第NNN章` 一致） |
| `pov` | string | ❌ | 视点人物 |
| `location` | string | ❌ | 场景地点 |
| `characters` | string[] | ❌ | 出场人物列表 |
| `word_count` | int | ❌ | 本章字数 |

### 3.2 character（人物单页）

```yaml
---
id: character-书名-人名
type: character
area: 项目
status: active
title: 林晚星
summary: 女主，重生者，科技创业者，冷静理性但有情感软肋。
source: ""
created: 2026-07-30
updated: 2026-07-30
kind: 女主
related: 陆远|林傲|陈守义
---
```

| 扩展字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `kind` | string | ❌ | 角色类型（主角/女主/反派/配角/NPC） |
| `related` | string | ❌ | 关联人物（`\|` 分隔） |

### 3.3 setting / location / prop（设定 / 地点 / 道具）

```yaml
---
id: setting-书名-设定名
type: setting
area: 项目
status: active
title: 超脑能力
summary: 主角核心金手指，信息处理能力增强，有冷却期和边界。
source: ""
created: 2026-07-30
updated: 2026-07-30
related: 林晚星
---
```

| 扩展字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `related` | string | ❌ | 关联实体（`\|` 分隔） |

### 3.4 project（项目 README）

```yaml
---
id: project-书名
type: project
area: 项目
status: active
title: 书名
summary: 男频重生科技流，主角重回1999年利用未来记忆造芯片。
source: ""
created: 2026-07-19
updated: 2026-07-30
genre: 重生
platform: 番茄
chapters_planned: 300
chapters_written: 0
---
```

| 扩展字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `genre` | string | ❌ | 题材（重生/都市/玄幻…） |
| `platform` | string | ❌ | 投稿平台（番茄/起点/晋江…） |
| `chapters_planned` | int | ❌ | 计划总章数 |
| `chapters_written` | int | ❌ | 已写章数 |
| `word_count` | int | ❌ | 已写总字数 |
| `volumes_planned` | int | ❌ | 计划总卷数 |
| `volumes_outlined` | int | ❌ | 已完成细纲的卷数 |

### 3.5 tool（工具卡）

```yaml
---
id: tool-00001
type: tool
area: 库
status: active
title: storyteller
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）。
source: https://github.com/facedeer/storyteller
created: 2026-07-18
updated: 2026-07-18
no: 1
repo: facedeer/storyteller
stars: 23
language: Python
license: MIT
url: https://github.com/facedeer/storyteller
tier: B
tags: [协议未明, 本地优先, 英文文档]
use_case: 从灵感→大纲→正文的全流程写作辅助
pitfalls:
  - 协议未声明，商用前需确认授权
category: 二、网文 / 长篇 AI 写作系统 库
---
```

| 扩展字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `no` | int | ✅ | 工具卡序号 |
| `repo` | string | ✅ | GitHub 仓 `owner/repo` |
| `stars` | int | ✅ | GitHub stars |
| `language` | string | ❌ | 主语言 |
| `license` | string | ❌ | 许可证 |
| `url` | string | ✅ | 仓库 URL |
| `tier` | string | ✅ | 分层 S/A/B/C |
| `use_case` | string | ✅ | 使用场景 |
| `pitfalls` | string[] | ❌ | 避坑提示 |
| `category` | string | ❌ | 分类路径 |

> 工具卡由 `_enrich_readmes.py` 自动生成，通用字段（id/title/summary/source/created/updated）需在脚本中补齐。

### 3.6 其他类型（index / guide / ref / dashboard / template / moc / demo）

只用通用字段，无专有扩展。`tags` 可放领域关键词。

---

## 四、受控词表

### 4.1 `type` 取值

| 值 | 用途 | 层级 |
|---|---|---|
| `index` | 导航入口/总地图 | 全库 |
| `guide` | 指南/速查 | 全库 |
| `ref` | 参考资料/方法论 | 全库 |
| `dashboard` | 仪表盘 | 全库 |
| `template` | 模板 | 全库 |
| `moc` | 分类导航 MOC | 库/ |
| `demo` | 示范骨架 | projects/ |
| `project` | 项目 README | projects/ |
| `chapter` | 正文章节 | projects/正文/ |
| `character` | 人物单页 | projects/人物/ |
| `setting` | 设定单页 | projects/设定/ |
| `location` | 地点单页 | projects/地点/ |
| `prop` | 道具单页 | projects/道具/ |
| `tool` | 工具卡 | 库/enriched/readmes/ |
| `daily-note` | 每日笔记 | 日记/ |
| `book-note` | 读书笔记 | 资料/ |
| `plan` | 计划文档 | maintenance/ |
| `report` | 报告文档 | maintenance/reports/ |

### 4.2 `area` 取值

| 值 | 覆盖范围 |
|---|---|
| `库` | 工具情报网（库/） |
| `方法` | 方法论主库（../methods/） |
| `项目` | 小说项目（projects/） |
| `资料` | 非小说参考资料（资料/） |
| `日记` | 每日时间流（日记/） |
| `索引` | vault 导航（索引/） |

### 4.3 `status` 取值

| 值 | 含义 |
|---|---|
| `active` | 活跃使用中 |
| `demo` | 示范/模板 |
| `wip` | 进行中 |
| `done` | 已完成 |
| `draft` | 草稿（正文专用） |
| `archived` | 已归档（不再活跃） |

---

## 五、旧格式 → 新格式迁移映射

| 旧写法（命名空间标签） | 新写法（平键） | 迁移动作 |
|---|---|---|
| `tags: [type/ref]` | `type: ref` | 从 tags 移除 `type/xxx`，加平键 |
| `tags: [area/方法]` | `area: 方法` | 从 tags 移除 `area/xxx`，加平键 |
| `tags: [status/active]` | `status: active` | 从 tags 移除 `status/xxx`，加平键 |
| `type: type/chapter`（[F] 正文） | `type: chapter` | 去掉 `type/` 前缀 |
| `type: type/moc`（[C] MOC） | `type: moc` | 去掉 `type/` 前缀 |
| 无 `id` | 补 `id: <type>-<slug>` | 按文件路径/标题生成 |
| 无 `title` | 补 `title: <标题>` | 取文件 H1 或文件名 |
| 无 `summary` | 补 `summary: <一句话>` | 人工或 AI 生成 |
| 无 `created`/`updated` | 补日期 | 取 git 首次/最后提交日期 |

> **迁移后 `tags` 只剩纯关键词**（如 `[去AI味, 大纲]`），不再有 `type/` `area/` `status/` 命名空间标签。

---

## 六、过渡期策略（迁移未完成时）

校验脚本采用**双轨检测**：

| 检测到 | 行为 | 级别 |
|---|---|---|
| 新格式（平键 `type:` 存在） | 严格校验取值，非法值 | **ERROR** |
| 旧格式（仅 `tags: [type/xxx]`） | 提示需迁移 | **WARN**（不阻断） |
| 新旧并存（平键 + 命名空间标签） | 提示冗余，建议清理 tags | **WARN** |
| 无 frontmatter | 放行（内容笔记不强求） | — |
| 有 frontmatter 但缺通用字段 | 提示缺失字段 | **WARN** |

> 迁移完成后，旧格式将升级为 ERROR。届时全库应已无 `tags: [type/xxx]` 命名空间标签。

---

## 七、与其他文档的关系

| 文档 | 关系 |
|---|---|
| `维护标准.md` §1.2 | 标签合规规则**以本文件为准**；旧版命名空间规则废止 |
| `维护标准.md` §1.5 ③ | `tags` 纯度规则保留——`platform`/`genre`/`pov`/`chapter`/`kind` 仍写独立 YAML 键 |
| `../tools/标签规范.md` | 工具卡受控标签（17词）保留，作为 `tags` 字段的取值参考 |
| `校验脚本.py` [B] | 检查平键 `type`/`area`/`status` 取值 |
| `校验脚本.py` [C] | MOC 检查 `type: moc` 平键 |
| `校验脚本.py` [F] | 正文检查 `type: chapter` 平键 |
| `校验脚本.py` [G]（新增） | 通用字段缺失检查（过渡期 WARN） |
| `_enrich_readmes.py` | 工具卡生成逻辑需补齐通用字段 |
| 仪表盘 Dataview 查询 | 从 `contains(tags, "type/xxx")` 改为 `type = "xxx"` |

---

## 八、id 生成规则

| 类型 | 格式 | 示例 |
|---|---|---|
| chapter | `chapter-<书名>-<NNN>` | `chapter-书名-001` |
| character | `character-<书名>-<人名>` | `character-书名-人名` |
| setting/location/prop | 同 character | `setting-书名-设定名` |
| project | `project-<书名>` | `project-书名` |
| tool | `tool-<NNNNN>` | `tool-00001` |
| ref/guide/index | `<type>-<slug>` | `ref-结构学` |
| moc | `moc-<分类名>` | `moc-去AI味` |
| daily-note | `daily-YYYY-MM-DD` | `daily-2026-07-30` |
| book-note | `book-<书名>` | `book-故事` |

> slug 规则：中文保留原字，空格转 `-`，去掉标点。
