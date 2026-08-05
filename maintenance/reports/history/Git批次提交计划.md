# Git批次提交计划

## 批次提交策略
按照清理优先级和风险等级，将整个清理过程分为多个批次，每个批次独立提交，确保可追溯性和可回滚性。

---

## 批次总览

| 批次 | 名称 | 优先级 | 预计时间 | 风险等级 | 影响范围 |
|------|------|--------|----------|----------|----------|
| Batch-01 | 紧急目录清理 | 高 | 30分钟 | 高 | 大文件移除 |
| Batch-02 | 重复文件清理 | 高 | 15分钟 | 低 | 系统文件 |
| Batch-03 | 大型文件处理 | 中 | 45分钟 | 中 | 媒体文件 |
| Batch-04 | 生成产物整理 | 中 | 1小时 | 低 | 导出文件 |
| Batch-05 | Obsidian优化 | 低 | 30分钟 | 低 | 配置文件 |
| Batch-06 | 工具卡规范 | 低 | 2小时 | 低 | 内容文件 |

---

## Batch-01: 紧急目录清理

### 提交信息
```
chore: 移除大型工具链目录

移除以下不应进入主库的目录：
- .tools/ (6,492个文件, 412MB)
- git/ (6,491个文件, 约400MB) 
- usr/ (4,534个文件, 约150MB)

总计移除: 17,517个文件, 约962MB
```

### 操作步骤
1. **备份当前状态**
   ```bash
   git add .
   git commit -m "backup: 清理前完整状态"
   ```

2. **移除目录**
   ```bash
   rm -rf .tools/
   rm -rf git/
   rm -rf usr/
   ```

3. **提交更改**
   ```bash
   git add .
   git commit -m "chore: 移除大型工具链目录
   
   移除以下不应进入主库的目录：
   - .tools/ (6,492个文件, 412MB)
   - git/ (6,491个文件, 约400MB)
   - usr/ (4,534个文件, 约150MB)
   
   总计移除: 17,517个文件, 约962MB"
   ```

### 验证标准
- [ ] 目录已完全移除
- [ ] Git状态干净
- [ ] 核心文件不受影响
- [ ] 提交信息清晰

---

## Batch-02: 重复文件清理

### 提交信息
```
chore: 清理重复的二进制文件

清理以下重复文件：
- scalar.exe (14MB, 重复2次)
- libSkiaSharp.dll (8MB, 重复2次)
- libcrypto-3-x64.dll (5MB, 重复2次)

总计节省: 27MB
```

### 操作步骤
1. **查找重复文件**
   ```bash
   find . -name "scalar.exe" -exec ls -lh {} \;
   find . -name "libSkiaSharp.dll" -exec ls -lh {} \;
   find . -name "libcrypto-3-x64.dll" -exec ls -lh {} \;
   ```

2. **保留一个副本，删除重复**
   ```bash
   # 保留根目录的文件，删除其他位置的重复文件
   rm -f ./git/bin/scalar.exe
   rm -f ./tools/scalar.exe
   rm -f ./usr/bin/libSkiaSharp.dll
   rm -f ./tools/libSkiaSharp.dll
   rm -f ./usr/bin/libcrypto-3-x64.dll
   rm -f ./tools/libcrypto-3-x64.dll
   ```

3. **提交更改**
   ```bash
   git add .
   git commit -m "chore: 清理重复的二进制文件
   
   清理以下重复文件：
   - scalar.exe (14MB, 重复2次)
   - libSkiaSharp.dll (8MB, 重复2次)
   - libcrypto-3-x64.dll (5MB, 重复2次)
   
   总计节省: 27MB"
   ```

### 验证标准
- [ ] 重复文件已清理
- [ ] 功能文件保留
- [ ] 提交信息准确

---

## Batch-03: 大型文件处理

### 提交信息
```
refactor: 移除过大的媒体文件

移除以下大型文件（>1MB）：
- cover-distill-minds.png (6.4MB)
- advisory-board.png (5.4MB)
- 6-agents-parallel.png (4.9MB)
- hero.gif (4.6MB)
- nuwa-hero-alchemy.mp4 (4.5MB)
- 封面-剑道独尊.png (3.0MB)
- nuwa-hero-alchemy.gif (1.8MB)
- 女娲landing-编辑长文.pdf (1.3MB)
- 女娲deck-粗野编辑.pdf (1.1MB)

总计节省: 33MB
```

### 操作步骤
1. **识别大型文件**
   ```bash
   find . -type f -size +1M
   ```

2. **评估文件重要性**
   - 保留重要文档
   - 移除重复或过时的媒体文件
   - 压缩可压缩的文件

3. **移除文件**
   ```bash
   rm -f "cover-distill-minds.png"
   rm -f "advisory-board.png"
   rm -f "6-agents-parallel.png"
   rm -f "hero.gif"
   rm -f "nuwa-hero-alchemy.mp4"
   rm -f "封面-剑道独尊.png"
   rm -f "nuwa-hero-alchemy.gif"
   rm -f "女娲landing-编辑长文.pdf"
   rm -f "女娲deck-粗野编辑.pdf"
   ```

4. **提交更改**
   ```bash
   git add .
   git commit -m "refactor: 移除过大的媒体文件
   
   移除以下大型文件（>1MB）：
   - cover-distill-minds.png (6.4MB)
   - advisory-board.png (5.4MB)
   - 6-agents-parallel.png (4.9MB)
   - hero.gif (4.6MB)
   - nuwa-hero-alchemy.mp4 (4.5MB)
   - 封面-剑道独尊.png (3.0MB)
   - nuwa-hero-alchemy.gif (1.8MB)
   - 女娲landing-编辑长文.pdf (1.3MB)
   - 女娲deck-粗野编辑.pdf (1.1MB)
   
   总计节省: 33MB"
   ```

### 验证标准
- [ ] 大型文件已移除
- [ ] 重要内容不受影响
- [ ] 提交信息详细

---

## Batch-04: 生成产物整理

### 提交信息
```
chore: 整理生成产物文件

整理以下目录的生成产物：
- references/online-research/ (HTML、TXT文件)
- 其他导出文件

保留标准：
1. 包含独特内容的文件
2. 近期的研究数据（2024年后）
3. 核心参考资料
```

### 操作步骤
1. **分析生成产物**
   ```bash
   find references/online-research/ -name "*.html" | wc -l
   find references/online-research/ -name "*.txt" | wc -l
   ```

2. **清理重复和过期文件**
   ```bash
   # 删除重复的HTML文件
   find references/online-research/ -name "*.html" -exec basename {} \; | sort | uniq -d | while read file; do
     find references/online-research/ -name "$file" | head -n -1 | xargs rm -f
   done
   
   # 删除过期的TXT文件（2024年前的）
   find references/online-research/ -name "*.txt" -mtime +730 -exec rm -f {} \;
   ```

3. **提交更改**
   ```bash
   git add .
   git commit -m "chore: 整理生成产物文件
   
   整理以下目录的生成产物：
   - references/online-research/ (HTML、TXT文件)
   - 其他导出文件
   
   保留标准：
   1. 包含独特内容的文件
   2. 近期的研究数据（2024年后）
   3. 核心参考资料"
   ```

### 验证标准
- [ ] 重复文件已清理
- [ ] 重要文件保留
- [ ] 目录结构清晰

---

## Batch-05: Obsidian优化

### 提交信息
```
config: 优化Obsidian配置

优化内容：
1. 精简插件配置
2. 清理缓存文件
3. 保留核心配置

保留的插件：
- dataview
- templater-obsidian
- obsidian-git
```

### 操作步骤
1. **分析当前配置**
   ```bash
   ls -la .obsidian/plugins/
   ```

2. **移除不必要的插件**
   ```bash
   # 禁用不必要的插件
   rm -rf .obsidian/plugins/periodic-notes
   rm -rf .obsidian/plugins/quickadd
   rm -rf .obsidian/plugins/tag-wrangler
   ```

3. **清理缓存文件**
   ```bash
   find .obsidian/ -name "*.cache" -delete
   find .obsidian/ -name "*.tmp" -delete
   ```

4. **提交更改**
   ```bash
   git add .
   git commit -m "config: 优化Obsidian配置
   
   优化内容：
   1. 精简插件配置
   2. 清理缓存文件
   3. 保留核心配置
   
   保留的插件：
   - dataview
   - templater-obsidian
   - obsidian-git"
   ```

### 验证标准
- [ ] 插件配置精简
- [ ] 缓存文件清理
- [ ] 核心功能正常

---

## Batch-06: 工具卡规范

### 提交信息
```
refactor: 标准化工具卡格式

标准化内容：
1. 统一工具卡模板
2. 清理重复字段
3. 规范ID格式

影响文件：tools/cards/ (3,573个文件)
```

### 操作步骤
1. **创建工具卡模板**
   ```bash
   cat > tools/card-template.yaml << 'EOF'
   ---
   id: tool-XXXXX
   name: ""
   description: ""
   author: ""
   version: ""
   category: ""
   tags: []
   install: ""
   use_case: ""
   pitfalls: []
   related: []
   ---
   EOF
   ```

2. **批量处理工具卡**
   ```bash
   # 清理重复的related字段
   for file in tools/cards/*.md; do
     # 使用sed清理重复字段
     sed -i '/^related:$/,/^[^ ]/ { /^related:$/d; }' "$file"
   done
   ```

3. **提交更改**
   ```bash
   git add .
   git commit -m "refactor: 标准化工具卡格式
   
   标准化内容：
   1. 统一工具卡模板
   2. 清理重复字段
   3. 规范ID格式
   
   影响文件：tools/cards/ (3,573个文件)"
   ```

### 验证标准
- [ ] 格式统一
- [ ] 重复字段清理
- [ ] 模板建立

---

## 提交验证脚本

### 验证脚本
```bash
#!/bin/bash
# 验证批次提交的完整性

echo "=== Git仓库清理验证 ==="
echo "当前分支: $(git branch --show-current)"
echo "最新提交: $(git log --oneline -1)"

# 检查工作区状态
echo -e "\n=== 工作区状态 ==="
git status

# 检查文件数量变化
echo -e "\n=== 文件数量统计 ==="
echo "当前文件数量: $(git ls-files | wc -l)"
echo "删除的文件数量: $((11364 - $(git ls-files | wc -l)))"

# 检查存储空间
echo -e "\n=== 存储空间 ==="
echo "当前仓库大小: $(du -sh . | cut -f1)"
echo "节省空间: 约1GB"

# 检查关键文件
echo -e "\n=== 关键文件检查 ==="
echo "核心文档数量: $(find ai/ knowledge/ methods/ projects/ -name "*.md" | wc -l)"
echo "工具卡数量: $(find tools/cards/ -name "*.md" | wc -l)"
echo "配置文件状态: $(ls -la .obsidian/ | wc -l)"
```

---

## 回滚机制

### 基线标签
```bash
# 创建基线标签
git tag baseline-before-cleanup

# 回滚到基线
git reset --hard baseline-before-cleanup

# 查看标签
git tag
```

### 分批回滚
```bash
# 回滚到特定批次
git reset --hard Batch-01
git reset --hard Batch-02
# 以此类推
```

---

## 执行时间表

| 时间 | 批次 | 状态 | 预计耗时 |
|------|------|------|----------|
| 第1天 | Batch-01 | 进行中 | 30分钟 |
| 第1天 | Batch-02 | 待执行 | 15分钟 |
| 第1天 | Batch-03 | 待执行 | 45分钟 |
| 第2天 | Batch-04 | 待执行 | 1小时 |
| 第2天 | Batch-05 | 待执行 | 30分钟 |
| 第3天 | Batch-06 | 待执行 | 2小时 |

---

## 风险控制

### 每批次前检查
1. **备份当前状态**
   ```bash
   git add .
   git commit -m "backup: 批次前备份"
   ```

2. **验证文件完整性**
   ```bash
   git status
   git diff --cached
   ```

### 每批次后验证
1. **检查提交信息**
   ```bash
   git log --oneline -5
   ```

2. **验证功能正常**
   ```bash
   # 测试核心功能
   # 检查重要文件
   ```

### 应急处理
1. **立即回滚**
   ```bash
   git reset --hard HEAD~1
   ```

2. **恢复备份**
   ```bash
   git checkout HEAD -- <file>
   ```

---
**制定时间**: 2026-08-04  
**执行人员**: AI Assistant  
**预计完成**: 3天内