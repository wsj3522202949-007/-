---
id: ref-原稿转创作知识库-SOP
type: ref
area: 方法
status: active
tags: []
title: 原稿 → 创作知识库 · 优化版 SOP（已对齐五层蓝图）
summary: ---
source: ""
created: 2026-07-30
updated: 2026-07-30
---

# 原稿 → 创作知识库 · 优化版 SOP（已对齐五层蓝图）

> 基于你给的 8 步方案，结合本 vault 现有「五大区」架构 + `tools/scripts/validation/校验脚本.py`（契约门禁）+ `链接体检与修复.py`（链接门禁）的**实际行为**做了修订。
> 本 SOP 是 **L0–L4 五层结构蓝图**在「原稿入库」场景的落地步骤；架构总纲与契约见 [维护标准 §五层结构蓝图](../../schema/维护标准.md)，新建书直接复制 [项目骨架模板](../README.md)。
> 先读「〇、关键差异」做审核，再看「一～九」执行。
> 审核通过后，我可照此执行转换，或先补做附 A 里的工具。

---

## 〇、和你原方案的关键差异（先读这段）

| # | 你的原方案                                                | 优化后（为什么改）                                                                                                                                                          |                       |
| - | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- |
| 1 | 复制示范项目，只保留 6 个文件（README/SKILL/人物设定卡/分卷细纲/伏笔管理表/写作进度） | 复制**整个** `项目骨架模板/` 目录（还含 `AGENTS.md` / `STATUS.md` / `TODO.md` / `全书创作手册` / `大纲编写规则` / `框架` / `风格校准文档` / `模板应用/` / `正文/`）。这些是系统跑通"前 5 章真实正文"的骨架与证据，删了要重造。        |                       |
| 2 | 正文只放最终稿，命名 `第001章-标题.md`                             | 保留 ✅。补一条：正文文件**必须带 frontmatter**（见第六点），否则会被 `tools/scripts/validation/校验脚本.py` 的标签契约误伤成 ERROR。                                                                                           |                       |
| 3 | Word/WPS 导出 Markdown，去残留                             | 保留 ✅，并补**推荐转换器 + 清理清单**（见附 A）。                                                                                                                                     |                       |
| 4 | 拆 `人物/林晚星.md`、`设定/…`、`地点/…`、`道具/…`                   | 三处修订：(a) **位置下沉到本书目录内** `projects/你的书名/人物/…`，不要放 vault 根（多书混放会乱）；(b) 用 `人物设定卡.md` 作 MOC 汇总，单页作深链；(c) **链接用标准 markdown 链接**（见第一点），否则 AI/RAG 管道无法稳定消费。                          |                       |
| 5 | 写项目首页 `正文/README.md`                                 | 改成写**项目根** `README.md`（你示范里首页就是项目根 README，不是 `正文/README`）。`正文/README.md` 只放命名规范 + 章节清单。另：首页 `↩ 回总地图` 链接现网有 bug，要修成 `[🗺️ 知识库总地图](../../README.md)`（见第一点）。 |
| 6 | frontmatter 加 title/tags/status/platform/genre       | **重大修订**：`tags` 被两个脚本强制要求"命名空间化"——只能是 `type/`、`area/`、`status/` 且取值受限。`platform`/`genre` 不能直接进 `tags`，否则 ERROR 暴增。正确写法见第六点。                                        |                       |
| 7 | 跑 `链接体检与修复.py` 查断链                          | 两处修订：(a) **先跑 `tools/scripts/validation/校验脚本.py`**（守标签契约），再跑 `tools/scripts/writing/链接体检与修复.py --fix`（守 markdown 链接 + 残留 wikilink + 顺手转义 `_`）；(b) 仪表盘路径已修复，不再有绝对路径断链噪声。 |                       |
| 8 | 素材进 `archive/`                                       | 保留 ✅，补：archive 在链接体检 `SKIP_DIRS` 内被跳过，内部死链不报；进 archive 前自己核对一次出处链接。                                                                                                |                       |

---

## 一、链接写法铁律（最重要，先记住）

本 vault 的链接体检脚本**按文件路径**解析 markdown 链接和残留 wikilink（先按当前文件相对路径，再按 vault 根）。**标准 markdown 链接是首选格式**，AI/RAG 管道可稳定消费。

- ❌ `[[林晚星]]`（Obsidian 短名 wikilink）——多数解析器不识别，脚本判**断链**。
- ❌ `[[E:/projects/…/林晚星]]`（绝对路径）——脚本判断链，Obsidian 也不认。
- ✅ `[林晚星](projects/你的书名/人物/林晚星.md)`（标准 markdown 链接，相对路径）——AI/RAG/Obsidian 都认。

> **规则：文档间引用一律用标准 markdown 链接 `[显示文本](相对路径.md)`。结构性关联用 frontmatter `related`/`see_also` 字段。** 详见 [链接规范](schema/链接规范.md)。

**现网 bug（顺手修）**：示范项目 `README.md` 里的回总地图链接实际指向**自己**（同目录 README），应改为 `[🗺️ 知识库总地图](../../README.md)` 才回得到总地图（从 `projects/你的书名/` 上跳两级到 vault 根）。

---

## 二、复制并改名示范项目（对应你第 1 步）

```bash
cd E:/个人知识库/projects
cp -r "../methods/项目骨架模板" "你的书名"
```

保留全部文件，之后逐个文件：

- 把书名、人物、梗概、平台等 demo 占位替换成你的真内容；
- 删掉 `模板应用/` 里已填的示范作战卡（或留作空白模板参考）；
- `README.md` 顶部 `tags` 改 `status/demo` → `status/active`、`type/demo` → `type/project`。

并在 **`README.md`** 的「我的小说项目」表里加一行（vault 唯一前门纪律，新增书必须登记）：

```
| ✍️ **你的书名** | projects/你的书名/README.md |
```

---

## 三、正文只放最终稿（对应你第 2 步）

- 新建 `projects/你的书名/正文/`（示范里已有）。
- 每章 `第NNN章-章节标题.md`，三位零填充，一章一文件，不合并。
- **每个正文文件加 frontmatter**（见第六点），否则触发校验 ERROR。

---

## 四、原稿转 Markdown（对应你第 3 步）

**推荐转换器**（按源格式选）：

- 源是 `.docx`：优先 `pandoc 原稿.docx -o 第001章.md`（若已装 pandoc）；没装就让我写一个 `python-docx → md` 批量转换器（带清理清单，我可现做）。
- 源是 `.txt`/剪贴板：直接粘进 md 文件。

**清理清单（转完必做）**：

- 删页眉 / 页脚 / 页码（如 `第 3 页 / 共 12 页`）；
- 删分页符残留（`\pagebreak`、`===` 之类导出垃圾）；
- 合并被分段落（Word 自动换行造成的软回车 → 真换行）；
- 连续 >1 空行压成 1 个；
- 去掉自动编号列表，改纯段落；
- 标题统一 `# 第 001 章 · 章节标题`（与示范一致）。

---

## 五、知识化结构（对应你第 4 步，修订版）

位置**下沉到本书目录内**，并用 MOC 汇总：

```
projects/你的书名/
├─ 人物设定卡.md          # MOC：人物总表，链到各单页
├─ 人物/
│  ├─ 林晚星.md           # 单页，frontmatter: tags:[area/项目,status/active]
│  └─ 顾延舟.md
├─ 设定/
│  └─ 雪松调查组.md
├─ 地点/
│  └─ 滨海市.md
└─ 道具/
   └─ 旧钢笔.md
```

- `人物设定卡.md` 里用 `[林晚星](人物/林晚星.md)` 串起来；
- 正文里出现人物 / 设定处，用同格式 `[别名](相对路径.md)` 串；
- 单页彼此也可互链（如 林晚星 链 顾延舟），形成知识网；
- 单页 frontmatter 模板见第六点。

> **为什么下沉到本书**：你是多书 vault，vault 根放 `人物/` 会把多本书角色混在一起，检索和重名都是灾难。

---

## 六、frontmatter 写法（对应你第 6 步，修订版）

⚠️ `type` / `area` / `status` 作为**独立 YAML 平键**，取值受限（见下表）。`platform` / `genre` / `pov` / `chapter` 等也**作为独立 YAML 键**，不要塞进 `tags`。`tags` 只放受控标签（工具卡）或留空（笔记层）。

**项目根 `README.md`：**

```yaml
---
id: project-你的书名
type: project
area: 项目
status: active
tags: []
title: 你的书名
summary: 一句话简介
created: 2026-07-31
updated: 2026-07-31
platform: 番茄/晋江
genre: 男频·重生科技
---
```

**章节 `第001章-xxx.md`：**

```yaml
---
id: chapter-你的书名-001
type: chapter
area: 项目
status: done
tags: []
title: 第001章 · 汇报会上的新甲方
chapter: 1
pov: 沈念
genre: 女频·都市言情
created: 2026-07-31
updated: 2026-07-31
---
```

**知识单页 `人物/林晚星.md`：**

```yaml
---
id: character-你的书名-林晚星
type: character
area: 项目
status: active
tags: []
title: 林晚星
summary: 一句话人物简介
created: 2026-07-31
updated: 2026-07-31
book: 你的书名
---
```

**命名空间取值速查（写错会被 `tools/scripts/validation/校验脚本.py` 报 ERROR）：**

- `type/` ∈ {index, guide, ref, dashboard, template, moc, demo, project}
- `area/` ∈ {库, 方法, 项目}
- `status/` ∈ {active, demo, wip, done}

> 章节没有专属 `type/`，所以用 `area/项目 + status/*` 即可满足"≥1 个 area/"的契约。

---

## 七、提交前门禁（对应你第 7 步，修订版）

按顺序跑两个脚本（都在 vault 根下执行）：

```bash
# 1) 契约门禁：标签命名空间 / 结构不变量
python tools/scripts/validation/校验脚本.py
# 2) 链接门禁：断链 + 转义 _（--fix 顺手把链接显示文本里的 _ 转义，安全可重入）
python tools/scripts/writing/链接体检与修复.py --fix
```

- 两者都 `ERROR=0` 再提交（git）。
- `--fix` 不会改断链本身，只自动转义链接文本里的 `_`（很多角色 / 工具名带 `_`），减少误排版。
我可一并修掉，让第 7 步报告只反映你新书的问题。

---

## 八、素材进 archive（对应你第 8 步）

- 灵感 / 截图 / 原始调研 / 早期版本 → `archive/`（可沿用现有 10_外部Skill… 等分类，或新建 `archive/你的书名_素材/`）。
- archive 在链接体检 `SKIP_DIRS` 内，内部死链不报；进 archive 前自己核对出处链接。
- **不要把素材塞进 `正文/` 或项目根**。

---

## 九、最简执行顺序（优化后）

1. `cp -r` 复制**整个**示范项目 → 改名
2. 在 `README.md` 项目表登记一行
3. 原稿 `.docx` → Markdown，按清理清单去残留
4. 按 `第NNN章-标题.md` 放进 `正文/`，每章加 frontmatter
5. 建 `人物/设定/地点/道具/` 单页 + `人物设定卡.md` 作 MOC，用标准 markdown 链接串
6. 补项目根 `README.md`（卷名 / 进度 / 核心人物 / 主线冲突 / 章节映射）+ 修 `↩ 回总地图` 链接
7. 跑 `tools/scripts/validation/校验脚本.py` → `链接体检与修复.py --fix`，ERROR=0 再提交
8. 素材进 `archive/`

---

## 附 A：要不要我顺手做这些（审核时勾选）

- [x] 写 `.docx → md` 批量转换器（带第四点的清理清单）
- [x] 修 `仪表盘-静态版.md` 的 55 条绝对路径断链（让门禁报告干净）
- [x] 修示范项目 `README.md` 的 `↩ 回总地图` 自链 bug（顺手让示范本身合规）
- [x] 把本 SOP 落成 vault 正式模板（`./模板/` 下）
- [ ] 直接用本 SOP 执行你某本书的入库（给我书名 + 原稿路径）
