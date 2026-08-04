---
id: tools-reports-index
type: index
area: 库
status: active
tags: [工具, 报告, 维护, 最近变更]
title: 维护报告索引（最近变更）
summary: 自动生成的校验 / 健康 / 清理报告索引，是「最近变更」的稳定入口。
source: 内部生成
created: 2026-08-04
updated: 2026-08-04
related:
  - README.md
  - tools/scripts/validation/run_all.py
  - maintenance/入口.md
---

# 维护报告索引（最近变更）

> 本目录由维护脚本**自动生成**，记录知识库最近的状态、健康与清理情况。
> 这是「维护入口 → 最近变更」的稳定落点（文件名会随日期滚动，请以本索引为准）。

---

## 📋 当前报告

| 报告 | 说明 | 生成时间 |
|---|---|---|
| [周度健康报告 2026-08-04](weekly-health-2026-08-04.md) | 每周健康检查 | 2026-08-04 |
| [月度清理 2026-08](monthly-cleanup-2026-08.md) | 每月清理检查 | 2026-08 |
| [季度清理 2026-Q3](quarterly-cleanup-2026-Q3.md) | 季度深度清理 | 2026-Q3 |

---

## 🔧 如何刷新

```bash
# 每周健康报告
python tools/scripts/maintenance/每周健康报告.py

# 每月清理检查
python tools/scripts/maintenance/每月清理检查.py

# 季度清理
python tools/scripts/maintenance/季度清理.py

# 全库校验（门禁）
python tools/scripts/validation/run_all.py
```

---

## 📊 最近校验结果

- **状态**：PASS（0 ERROR / 0 WARN，2026-08-04）
- 全库校验入口：[run_all.py](../scripts/validation/run_all.py)

---

> 报告为自动产物，请勿手改；如需调整检查项，改对应脚本。
