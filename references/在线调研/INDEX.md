# online_research 素材区 · 分类索引与吸收状态

> 用途：本目录是 `../../methods/` 的**原始抓取素材区**（2026-07-18 批量存档），不是日常用法。进方法库请从 `INDEX.md` / `导览.md` 走。本文件只负责：把 50 个原始文件分类、标注状态、给吸收结论，避免卡文时误进垃圾堆。
> 关联：[../外部Skill蒸馏/00_总索引_外部Skill蒸馏.md](../外部Skill蒸馏/00_总索引_外部Skill蒸馏.md)（Skill→方法库 吸收映射）

## 一、总判定（2026-07-19 复盘）

| 分组 | 文件数 | 状态 | 结论 |
|---|---|---|---|
| 已吸收产物 | 1 | ✅ 已归口 | `小说sill_吸收精华.md` 的 skill 精华已吸收进主库 |
| 英文写作指南（抓取失败） | 8 | 🗑️ 删除候选 | 仅有网站导航/404/空，无正文可吸收 |
| 实时搜索抓取堆 live-web-* | 41 | 🟡 待 triage | 原始搜索页 HTML 转储，大多低价值，批量删前需人工筛 |

**关键结论**：此前待办里写的"online_research 50 文件待吸收"实际已**基本闭环**——真正有价值的写作知识在 `小说sill_吸收精华.md`（oh-story / nuwa / humanizer 系列 README 合集），它早已通过 `../外部Skill蒸馏/00_总索引_外部Skill蒸馏.md` 归口到 `最强去AI味铁律.md`、`人物思维蒸馏法.md`、`自检清单_升级版.md`、`改稿润色指令库.md`。那 4 组"英文指南"本次核查为**抓取死链**，无可吸收内容，已删除。

---

## 二、分组明细

### A 组 · 已吸收产物（保留，已归口主库）

| 文件 | 内容 | 吸收去向 |
|---|---|---|
| `小说sill_吸收精华.md` | oh-story / nuwa-skill / humanizer / Humanizer-zh / ai-flavor-remover / chatgpt-comparison-detection 的 README 合集 | 见 `../外部Skill蒸馏/00_总索引_外部Skill蒸馏.md` 第一节 |

### B 组 · 英文写作指南（🗑️ 已删除，抓取失败）

原 8 个文件（4 篇 × html+txt）经核查内容仅为站点导航菜单 / 404 页 / 空文件（dictionary 仅 61 字符），无任何文章正文，无法吸收，已于 2026-07-19 删除：

- `20260718-102531-1-blog.reedsy.com_guide_plot-structure_` (html/txt) — 仅 reedsy 站点导航
- `20260718-102531-2-www.nownovel.com_blog_novel-outline_` (html/txt) — 仅 NowNovel 站点导航
- `20260718-102531-3-www.helpingwritersbecomeauthors.com_how-to-write-a-novel_` (html/txt) — 404 页
- `20260718-102531-4-blog.dictionary.com_25-best-english-novels-of-all-time_` (html/txt) — 空（61 字符）

> 若日后需要西方结构学原典，应重新定向抓取 Reedsy《Plot Structure》、K.M.Weiland《Structuring Your Novel》、NowNovel《Novel Outline》的**文章正文**（非站点首页），目标归口 `craft/西方理论原典溯源.md`。

### C 组 · 实时搜索抓取堆 live-web-*（🟡 待 triage / 删除候选）

均为 2026-07-18 实时搜索（bing/baidu）的 HTML 转储，属原始噪声素材，建议人工筛后批量删。重点标注：

| 文件 | 体积提示 | 建议 |
|---|---|---|
| `live-web-1-*` (full/source html+txt) | source 约 57K，最大 | 可能含正文，优先筛；有用则摘要点进 `craft/` |
| `live-web-2-*` (full/source html+txt) | source 约 54K | 同上 |
| `live-web-23.*` (html+txt) | 8K | 可筛 |
| `live-web-3/5/6/7/8/11/12/13-*` | 2–6K | 多为搜索结果页，低价值，删除候选 |
| `live-web-4/9/10/14/15/16/17/18/19/20-*` | 小 | 删除候选（working memory 已标 live-web-14 为删除候选） |
| `live-web-14-*` | 小 | 🗑️ 删除候选（明确） |

---

## 三、使用约定

1. 本目录是"仓库"，不是"武器库"。写稿卡文别来这翻，去 `INDEX.md` / `QUICK_START.md` / `导览.md`。
2. 任何新抓取素材，吸收完立即归档到主库对应 `craft/`（保留原始进 `../archive/`），别堆在 online_research 烂尾。
3. live-web-* 若长期不筛，整组可删——它们不进版本控制的核心价值。
