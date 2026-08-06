---
id: auto-Git仓库整理第三阶段重建质量门禁计划
type: report
area: 管理
status: archived
tags: [auto-generated]
title: Git仓库整理第三阶段重建质量门禁计划
summary: 自动生成报告，无需人工维护。
source: 自动生成
created: 2026-08-05
updated: 2026-08-05
---

# Git仓库整理第三阶段重建质量门禁计划

## 阶段概述

### 第三阶段目标
**重建质量门禁**
- 预计时间：2～3天
- 优先级：P0
- 目标：修复检查器不一致问题，建立统一、可靠的质量门禁系统

### 当前问题
1. **校验脚本.py**：完全通过
2. **链接体检与修复.py**：8,459 个错误，并在 JSON 输出阶段崩溃
3. 两个检查器结果不一致
4. 缺乏统一入口

---

## 修复计划

### 1. 分析检查器差异

#### 校验脚本.py 特点
- 检查项：A-G 共 7 类
- 扫描范围：全库（排除 archive/、references/、原始来源包/、在线调研/）
- JSON 输出：正常
- 结果：完全通过

#### 链接体检与修复.py 特点
- 检查项：1-3 类（未转义 _、断链、tag 规范）
- 扫描范围：全库（排除 .git、.workbuddy、archive）
- JSON 输出：崩溃
- 结果：8,459 个错误

#### 差异分析
1. **扫描范围不同**：
   - 校验脚本排除：archive/、references/、原始来源包/、在线调研/
   - 链接体检排除：.git、.workbuddy、archive

2. **检查规则不同**：
   - 校验脚本：检查 frontmatter、结构、wiki 链接
   - 链接体检：检查链接文本、断链、tag 规范

3. **JSON 输出问题**：
   - 链接体检在大量错误时可能内存不足或输出格式问题

### 2. 统一扫描范围策略

#### 分区检查策略

| 区域 | 路径 | 检查级别 | 说明 |
|------|------|----------|------|
| **核心知识区** | schema/、methods/、tools/cards/ | 零错误 | 必须完全合规 |
| **项目生产区** | projects/ | 严格检查 | 必须合规，允许少量 WARN |
| **模板区** | methods/templates/ | 允许占位 | 允许明确标记的占位链接 |
| **外部参考区** | references/、archive/ | 只读 | 不要求遵守本库 frontmatter |
| **缓存/工具运行时** | .git/、.workbuddy/、.tools/ | 完全排除 | 不检查 |

#### 扫描范围统一
```python
SCAN_ZONES = {
    "core": {
        "paths": ["schema", "methods", "tools/cards"],
        "level": "strict",
        "allow_placeholder": False,
    },
    "production": {
        "paths": ["projects"],
        "level": "strict",
        "allow_placeholder": False,
    },
    "template": {
        "paths": ["methods/templates"],
        "level": "normal",
        "allow_placeholder": True,
    },
    "reference": {
        "paths": ["references", "archive"],
        "level": "readonly",
        "allow_placeholder": True,
        "skip_frontmatter": True,
    },
    "excluded": {
        "paths": [".git", ".workbuddy", ".tools", "__pycache__"],
        "level": "none",
    },
}
```

### 3. 修复链接检查脚本

#### 问题定位
1. **JSON 输出崩溃**：可能是大量错误导致内存不足或格式错误
2. **误报过多**：8,459 个错误可能有大量误报
3. **链接分类不清**：未区分真实断链、示例链接、目录链接等

#### 修复方案
1. **分批输出**：将错误分批输出，避免内存溢出
2. **链接分类**：
   - 真实断链：ERROR
   - 示例链接：WARN（如 `(链接)`、`(参见)`）
   - 目录链接：WARN（如 `目录/`）
   - Obsidian 协议链接：WARN（如 `obsidian://`）
   - 外部源码内部链接：WARN（如 GitHub 内部链接）
3. **JSON 格式统一**：与校验脚本保持一致

### 4. 增加新的门禁检查

#### 新增检查项
1. **真实断链**：区分真实断链和示例/占位链接
2. **重复 ID**：检查 frontmatter id 是否重复
3. **重复标题**：检查标题是否重复
4. **非法 frontmatter**：检查 frontmatter 格式是否合法
5. **项目结构漂移**：检查项目结构是否符合规范
6. **README 统计过期**：检查 README 中的统计信息是否过期
7. **旧绝对路径**：检查是否使用旧绝对路径
8. **孤立核心笔记**：检查是否有孤立的核心笔记（无反向链接）

### 5. 统一入口

#### 统一检查命令
```bash
python tools/scripts/validation/run_all.py [--zone <zone>] [--fix] [--json]
```

#### 参数说明
- `--zone`：指定检查区域（core/production/template/reference/all）
- `--fix`：自动修复问题
- `--json`：输出 JSON 格式

#### 输出格式
```json
{
  "timestamp": "2026-08-04T12:00:00",
  "zones": {
    "core": {
      "errors": [],
      "warns": [],
      "pass": true
    },
    "production": {
      "errors": [],
      "warns": [],
      "pass": true
    }
  },
  "summary": {
    "total_errors": 0,
    "total_warns": 0,
    "pass": true
  }
}
```

---

## 实施步骤

### Step 1：修复链接检查脚本（1天）
1. 修复 JSON 输出崩溃问题
2. 区分真实断链和示例链接
3. 统一 JSON 输出格式

### Step 2：统一扫描范围（0.5天）
1. 定义分区检查策略
2. 更新两个检查器的扫描范围
3. 确保扫描范围一致

### Step 3：增加新门禁（1天）
1. 实现重复 ID 检查
2. 实现重复标题检查
3. 实现非法 frontmatter 检查
4. 实现项目结构漂移检查
5. 实现 README 统计过期检查
6. 实现旧绝对路径检查
7. 实现孤立核心笔记检查

### Step 4：统一入口（0.5天）
1. 创建 run_all.py
2. 整合所有检查器
3. 统一输出格式

### Step 5：测试验证（0.5天）
1. 测试核心区 ERROR=0
2. 验证报告没有大规模误报
3. 验证 JSON 可供 Dataview、CI 或 AI 稳定读取

---

## 验收标准

### 1. 核心区 ERROR=0
- [ ] schema/ 区域 ERROR=0
- [ ] methods/ 区域 ERROR=0
- [ ] tools/cards/ 区域 ERROR=0

### 2. 报告没有大规模误报
- [ ] 真实断链准确率 >95%
- [ ] 示例链接不报 ERROR
- [ ] 目录链接不报 ERROR
- [ ] Obsidian 协议链接不报 ERROR

### 3. JSON 可供稳定读取
- [ ] JSON 格式统一
- [ ] JSON 输出不崩溃
- [ ] JSON 包含所有必要信息
- [ ] JSON 可通过 Dataview 读取
- [ ] JSON 可通过 CI 读取
- [ ] JSON 可通过 AI 读取

---

## 风险评估

### 1. JSON 输出崩溃风险
- **风险**：大量错误导致内存不足
- **缓解**：分批输出，优化内存使用
- **应对**：增加错误数量限制，分批处理

### 2. 误报风险
- **风险**：大量误报导致无法使用
- **缓解**：仔细区分链接类型，增加白名单
- **应对**：建立误报反馈机制，持续优化

### 3. 性能风险
- **风险**：检查速度过慢
- **缓解**：优化扫描算法，增加缓存
- **应对**：分批检查，异步处理

---

## 下一步行动

1. **立即开始**：修复链接检查脚本的 JSON 输出问题
2. **今天完成**：统一扫描范围策略
3. **明天完成**：增加新门禁检查
4. **后天完成**：统一入口和测试验证

---
**计划时间**: 2026-08-04  
**计划人员**: AI Assistant  
**预计完成**: 2026-08-06