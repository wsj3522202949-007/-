# Obsidian 使用指南（本知识库）

> ↩ **回总地图**：[🗺️ 知识库总地图](../README.md)（本页是子地图）

本工作区 `E:\小说` 已配置为可直接用 **Obsidian** 打开的知识库（vault）。这篇指南讲怎么把它用顺手。

---

## 一、快速开始

1. 打开 Obsidian → 左下角「打开其他仓库」→「打开文件夹作为仓库」→ 选择 **`E:\小说`**。
2. 首次打开会自动识别已有的 `.obsidian` 配置（已帮你设好链接/排除规则）。
3. 在左侧文件树找到根目录 **`README.md`**（🗺️ 知识库总地图），右键 → 「设为启动页」（或加书签）。以后每次打开直接进这里。

---

## 二、导航体系（三层）

```
库/知识库导航.md          ← 总入口（MOC），先看这里
   └─ 库/分类导航/01~21    ← 21 个分类页（其中 16 个有真实仓库）
        └─ 库/cards/xxxxx__owner__repo.md  ← 每个仓库一篇笔记（README 全文）
```

- **总入口** `./知识库导航.md`：列出全量索引、21 个分类导航。
- **分类页** `./分类导航/`：每个分类一篇，Top50（按星标）+ 全部列表，点仓库名即跳。
- **仓库笔记** `./cards/`：每个 GitHub 仓库一篇，含元数据头 + README 全文。

> 跳转全靠 `[[双向链接]]`，点一下就过去；按 `Ctrl/Cmd + 点击` 在新窗格打开。

---

## 三、核心玩法与查询示例

### 1. 反向链接（最有用）
打开任意仓库笔记，右侧「反向链接」面板会显示：**它属于哪个分类、在总索引第几行被引用**。这就是知识图谱的雏形——不用手动整理关系，点进去自然连成网。

### 2. 搜索（比图谱快）
按 `Ctrl/Cmd + P` 或左侧放大镜，搜中文仓库描述、工具名、分类名都能秒出。例如搜「去 AI 味」「humanizer」「网文」直接定位相关工具。

### 3. 属性视图（frontmatter）
每个仓库笔记顶部都加了 YAML 属性：

```yaml
---
no: 254
category: "二、网文 / 长篇 AI 写作系统 库"
repo: "linshenkx/prompt-optimizer"
stars: 32543
url: "https://github.com/linshenkx/prompt-optimizer"
---
```

在 Obsidian 里：
- 左侧「属性」面板可按 `stars` 排序、按 `category` 过滤；
- 右键任意属性值 →「在 Canvas/表格视图中显示」可批量看 Top 星标工具；
- 配合「Dataview」插件（自行安装）能写出 `TABLE stars, category FROM "tools/cards" SORT stars DESC LIMIT 50` 这种动态榜单。

### 4. 查询示例库（照抄即用）

下面都是直接可粘进 Obsidian 命令面板（`Ctrl/Cmd + P` → 搜 `Dataview`）或任意笔记代码块的查询。改 `contains(tags, "某标签")` 即可复用；标签名全部来自 [标签规范](标签规范.md) 受控词表。

**① 你的签约痛点：去 AI 味 + S/A 级**
```dataview
TABLE stars AS "⭐", use_case AS "用途" FROM "tools/cards"
WHERE contains(tags, "去AI味") AND tier IN ("S","A")
SORT stars DESC
```

**② 零门槛可商用：本地优先 ∩ 协议宽松（S/A）**
```dataview
TABLE stars AS "⭐", use_case AS "用途" FROM "tools/cards"
WHERE contains(tags,"本地优先") AND contains(tags,"协议宽松") AND tier IN ("S","A")
SORT stars DESC
```

**③ 中文友好 + 去 AI 味（中文降痕首选）**
```dataview
TABLE stars AS "⭐", use_case AS "用途" FROM "tools/cards"
WHERE contains(tags,"中文友好") AND contains(tags,"去AI味") AND tier IN ("S","A")
SORT stars DESC
```

**④ 长篇一致性：RAG + S 级**
```dataview
TABLE stars AS "⭐", use_case AS "用途" FROM "tools/cards"
WHERE contains(tags,"RAG") AND tier="S"
SORT stars DESC
```

**⑤ 按 owner/repo 精确定位一张卡**（配合 [manifest.json](manifest说明.md) 的 key）
```dataview
TABLE stars, tier, use_case FROM "tools/cards"
WHERE repo = "op7418/humanizer-zh"
```

**⑥ 最近一周新入库**
```dataview
TABLE file.mtime AS "入库", stars AS "⭐" FROM "tools/cards"
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
```

> 字段名见 [标签体系说明](标签体系说明.md)（`no / category / repo / stars / url / tier / tags / use_case / pitfalls`）；更多约束组合见 [库·落地建议](落地建议.md) 与 [仪表盘](../仪表盘.md) 的「实用查询层」。

### 5. 最佳实践

1. **三件事别混**：找单一工具用**搜索**，找一类工具用 **Dataview 查询**，找关系用**反向链接**。全局图谱只在「探索未知关联」时开，平时关着——3572 节点全开图谱是噪音。
2. **属性视图排序/过滤比手翻快 10 倍**：左侧「属性」面板点 `stars` 表头即排序；按 `category` 过滤只看某分类。
3. **双向链接是骨架**：在仓库笔记里写 `[[库/分类导航/...]]`、在方法笔记里写 `[[库/cards/...]]`，右侧「反向链接」会自动织网，不用维护目录。
4. **程序化精确定位走 manifest**：脚本/外部工具要按 `owner/repo` 找卡，直接读 [manifest.json](manifest说明.md)，别正则扫目录（去重后每个 `owner/repo` 仅一条）。
5. **模板 + 单章作战卡是写作主循环**：开写前翻 `../methods/templates/00_开写启动器.md`，每章填 `01_单章作战卡.md`，前 3 章跑 `02_前3章签约体检表.md`——情报网（本库）只负责「找外部武器」，写作主循环在方法论里。
6. **每次提交前跑双检**：`python tools/scripts/validation/校验脚本.py` + `python ../methods/工具/链接体检与修复.py`，ERROR=0、断链=0 再提交（见 [维护标准](../../schema/维护标准.md)）。

---

## 四、已为你配好的规则（`.obsidian/app.json`）

| 规则 | 作用 |
|---|---|
| 忽略 `*.json`/`*.csv`/`*.pdf`、临时构建目录、`.git` 等 | 造库脚本与原始 json 数据**不进 Obsidian**，避免搜索/图谱被污染 |
| `useMarkdownLinks: false` + `newLinkFormat: wiki` | 新链接自动用 `[[ ]]` 双向链接格式 |
| `alwaysUpdateLinksOnNoteChange: true` | 改名/移动笔记时链接自动更新，不会断 |

---

## 五、图谱视图注意

仓库笔记共 **3572** 篇，加上素材/方法论约 4000+ 节点。图谱全开会比较密：

- 建议在左侧文件树**只展开 `./` 或一个分类文件夹**再开图谱，节点数可控；
- 或装「Graph Settings」限制到当前文件夹；
- 日常找工具，**搜索 + 分类导航**比全局图谱更高效。

---

## 六、数据说明

- 真实落盘 README：**3572** 篇（来自 GitHub 上真实存在的仓库）。
- 不存在（gone）：**6432** 条，是源库里的 `library-lab/*` 等占位/虚构条目，GitHub 上无对应仓库，故无内容。
- 失败：**1** 条（`dtube`，源数据为单段组织名，无法解析）。

> 想补拉、重跑或加新仓库，需另行准备抓取脚本（造库中间数据已清理，保持 vault 干净）。

---

## 七、推荐插件（按需自装，非必需）

- **Dataview**：用属性做动态表格/榜单（上面第三节用到）。
- **OmniSearch** / **Text Snippets**：中文搜索体验更好。
- **Canvas**：把「去 AI 味 Top10 + 网文写作系统 Top10」拖成一张工具地图。
