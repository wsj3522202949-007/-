---
id: ref-manifest说明
type: ref
area: 库
status: active
tags: []
title: 🗂️ manifest.json 用法说明（工具卡去重索引）
summary: ↩ **回总地图**：🗺️ 知识库总地图
created: 2026-07-31
updated: 2026-07-31
related:
  - tools/标签规范.md
  - tools/维护说明.md
---

> ↩ **回总地图**：[🗺️ 知识库总地图](../README.md)

# 🗂️ manifest.json 用法说明（工具卡去重索引）

> 本文件是 `./cards/manifest.json` 的**用法手册**，不是数据本身。它把「3572 张工具卡」按 `owner/repo` 收成一本**去重字典**，让你不用翻目录就能用「GitHub 仓库名」直接定位笔记。

---

## 一、它是什么

`./cards/` 下有 **3572** 篇工具卡，文件名形如 `NNNNN__owner__repo.md`（前 5 位是入库序号，后面是 `owner/repo`）。

同一对 `owner/repo` 可能因为「补全抓取 / 重分类」出现 **2 张卡**。manifest 把这种情况收口成一条：`owner/repo` → **序号最小**的那张卡文件名。

- 工具卡文件数：**3572**
- 唯一 `owner/repo` 数：**3572**
- 被折叠的冗余卡：**21**（21 对 `owner/repo` 各有 2 张，取低序号那张做代表）

> 想看冗余清单、或要把高序号的 21 张合并/删除，见 [库·维护说明](维护说明.md)。

---

## 二、文件格式

纯 JSON 对象，`key` = `"owner/repo"`，`value` = 卡文件名。按 key 字母序排序，UTF-8、缩进 2 空格。

```json
{
  "blader/humanizer": "07166__blader__humanizer.md",
  "linshenkx/prompt-optimizer": "00254__linshenkx__prompt-optimizer.md",
  "op7418/humanizer-zh": "07475__op7418__humanizer-zh.md"
}
```

- key：`owner/repo`（与卡 frontmatter 的 `repo:` 字段一致，但这里是「斜杠」格式，不是下划线）。
- value：`NNNNN__owner__repo.md`（注意 value 里的 `owner` 和 `repo` 用**双下划线**分隔，且保留了 `NNNNN__` 前缀）。

---

## 三、怎么用它（三种场景）

### 1. 人肉查：已知 GitHub 仓库，找笔记
例如想看 `op7418/humanizer-zh`，直接在 manifest 里搜 key，得到 `07475__op7418__humanizer-zh.md`，去 `./cards/` 打开即可。

### 2. 脚本查：批量/程序化定位
```python
import json, os
BASE = "tools/cards"
man = json.load(open(os.path.join(BASE, "manifest.json"), encoding="utf-8"))

def card_path(owner_repo: str) -> str | None:
    """返回该仓库代表卡的绝对路径；不存在返回 None。"""
    fn = man.get(owner_repo)
    return os.path.join(BASE, fn) if fn else None

print(card_path("linshenkx/prompt-optimizer"))
# -> 库/cards/00254__linshenkx__prompt-optimizer.md
```

### 3. 去重校验：确认某个 owner/repo 是不是「唯一」
```python
# 直接数 key 出现次数即可；manifest 天然每 key 仅一条。
# 若要列出全库所有「有重复」的 owner/repo，需直接扫目录：
import re, glob
pat = re.compile(r'^(\d+)__(.+)__(.+)\.md$')
buckets = {}
for f in glob.glob("库/cards/*.md"):
    m = pat.match(os.path.basename(f))
    if m:
        buckets.setdefault(f"{m.group(2)}/{m.group(3)}", []).append(int(m.group(1)))
dups = {k: v for k, v in buckets.items() if len(v) > 1}
print("重复 owner/repo 数:", len(dups))
```

---

## 四、它是怎么生成的

由一段扫描脚本生成（与 `_enrich_readmes.py` 的命名规则一致）：

1. 遍历 `./cards/*.md`，用正则 `^(\d+)__(.+)__(.+)\.md$` 拆出 `序号 / owner / repo`；
2. 以 `owner/repo` 为 key 聚合；
3. 每个 key 只保留**序号最小**的卡（最早入库、最稳定）；
4. 写成 `manifest.json`，key 排序。

> ⚠️ 全库文件名必须严格遵循 `NNNNN__owner__repo.md`（5 位序号 + 双下划线）。若某文件命名不符（如序号不是 5 位），会被正则跳过、不进 manifest——这类异常由 `tools/scripts/validation/校验脚本.py` 的「readme 命名规范」项告警。

---

## 五、重生成命令

工具库若发生增删/改名（跑过 `_enrich_readmes.py` 或手动整理后），重生成索引：

```bash
# 仓库根目录 e:\个人知识库 下执行
python - <<'PY'
import os, re, glob, json
BASE = "tools/cards"
pat = re.compile(r'^(\d+)__(.+)__(.+)\.md$')
best = {}
for f in glob.glob(os.path.join(BASE, "*.md")):
    m = pat.match(os.path.basename(f))
    if not m: continue
    no, owner, repo = int(m.group(1)), m.group(2), m.group(3)
    key = f"{owner}/{repo}"
    if key not in best or no < best[key][0]:
        best[key] = (no, os.path.basename(f))
manifest = {k: v[1] for k, v in sorted(best.items())}
with open(os.path.join(BASE, "manifest.json"), "w", encoding="utf-8") as fh:
    json.dump(manifest, fh, ensure_ascii=False, indent=2, sort_keys=True)
    fh.write("\n")
print("manifest 已重生成:", len(manifest), "条")
PY
```

生成后跑 `tools/scripts/validation/校验脚本.py` 与 `../methods/工具/链接体检与修复.py` 确认无断链。

---

## 六、和其他索引的关系

| 索引 | 用途 | 维度 |
|---|---|---|
| `manifest.json` | 程序化按 `owner/repo` 定位单卡 | 仓库名 → 文件 |
| `./知识库导航.md` | 人工总入口，全量 + 分类 | 分类 → 仓库 |
| `./分类导航/*.md` | 21 个分类页，Top50 + 全量 | 分类 → 仓库 |
| `仪表盘.md` / `仪表盘-静态版.md` | 按 tier / 标签 / 约束统计 | 维度 → 榜单 |

> manifest 是「精确查一张卡」的底层索引；上面那些是「浏览 / 统计」的上层视图。两者互不替代。
