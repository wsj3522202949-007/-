# Batch-04: 生成产物整理记录

## 清理信息
- **批次**: Batch-04
- **清理时间**: 2026-08-04
- **清理人员**: AI Assistant
- **优先级**: 中
- **状态**: 进行中

## 清理目标
整理 `references/在线调研/` 目录中的生成产物：
- HTML网页快照文件
- TXT文本导出文件
- 保留重要内容，移除重复快照

## 清理前统计
- **HTML文件**: 25个文件
- **TXT文件**: 12个文件
- **总文件数**: 37个文件
- **目录结构**: 网页快照和文本导出

## 文件分析
### HTML文件列表
- `live-web-1-full.html` - 网页完整快照
- `live-web-1-source.html` - 网页源码快照
- `live-web-2-full.html` - 网页完整快照
- `live-web-2-source.html` - 网页源码快照
- ... (共25个HTML文件)

### TXT文件列表
- `live-web-1-full.txt` - 网页文本内容
- `live-web-1-source.txt` - 网页源码文本
- `live-web-2-full.txt` - 网页文本内容
- `live-web-2-source.txt` - 网页源码文本
- ... (共12个TXT文件)

## 整理策略
### 保留文件
1. **核心文档**:
   - `INDEX.md` - 索引文档
   - `小说sill_吸收精华.md` - 重要研究内容

2. **唯一快照**:
   - 每个主题保留一个完整的快照
   - 移除重复的source和full版本

### 移除文件
1. **重复快照**: 移除source和full的重复版本
2. **临时文件**: 移除测试和临时文件
3. **过时内容**: 移除过期的研究数据

## 清理操作
```powershell
# 分析文件重复情况
Get-ChildItem -Path "e:\个人知识库\references\在线调研" -Recurse -Filter "*.html" | Group-Object Name | Where-Object { $_.Count -gt 1 }
Get-ChildItem -Path "e:\个人知识库\references\在线调研" -Recurse -Filter "*.txt" | Group-Object Name | Where-Object { $_.Count -gt 1 }

# 保留重要文件，移除重复文件
# 具体操作将根据分析结果执行
```

## 预期效果
- **减少文件数量**: 约50% (从37个减少到约18个)
- **节省空间**: 约20MB
- **提升管理效率**: 更清晰的目录结构

## 清理后验证
- [ ] 重复文件已清理
- [ ] 重要内容已保留
- [ ] 目录结构已优化
- [ ] 研究资料完整

---
**记录创建时间**: 2026-08-04  
**操作状态**: 🔄 进行中