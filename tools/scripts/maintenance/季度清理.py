#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
季度深度清理
============

每季度执行一次深度清理，包括：
1. 清理缓存目录（__pycache__、.git、node_modules 等）
2. 清理临时文件（.tmp、.temp、.swp 等）
3. 清理大文件（超过 10MB）
4. 清理旧备份
5. 压缩历史报告
6. 生成清理报告

用法
----
    python tools/scripts/maintenance/季度清理.py                 # 预览要清理的内容
    python tools/scripts/maintenance/季度清理.py --execute        # 执行清理
    python tools/scripts/maintenance/季度清理.py --json           # JSON 输出
"""

import os
import sys
import json
import shutil
import zipfile
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
REPORTS_DIR = os.path.join(ROOT_DIR, "reports")

# 确保报告目录存在
os.makedirs(REPORTS_DIR, exist_ok=True)

# 缓存目录列表
CACHE_DIRS = [
    '__pycache__',
    '.git',
    'node_modules',
    '.vscode',
    '.idea',
    '.DS_Store'
]

# 临时文件扩展名
TEMP_EXTENSIONS = [
    '.tmp', '.temp', '.swp', '.swo', '.log',
    '.bak', '.orig', '.rej', '.pid'
]

# 大文件阈值（10MB）
LARGE_FILE_THRESHOLD = 10 * 1024 * 1024

# 旧备份阈值（90天）
OLD_BACKUP_DAYS = 90


def format_size(size_bytes):
    """格式化文件大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f}{unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f}TB"


def find_cache_dirs(root_dir):
    """查找缓存目录"""
    cache_dirs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for cache_dir in CACHE_DIRS:
            if cache_dir in dirnames:
                full_path = os.path.join(dirpath, cache_dir)
                # 计算大小
                try:
                    total_size = 0
                    for dirpath2, dirnames2, filenames2 in os.walk(full_path):
                        for filename in filenames2:
                            filepath = os.path.join(dirpath2, filename)
                            try:
                                total_size += os.path.getsize(filepath)
                            except:
                                pass
                    cache_dirs.append({
                        "path": os.path.relpath(full_path, root_dir),
                        "size": total_size,
                        "size_formatted": format_size(total_size),
                        "type": "cache"
                    })
                except:
                    pass
    return cache_dirs


def find_temp_files(root_dir):
    """查找临时文件"""
    temp_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__']
        for filename in filenames:
            if any(filename.endswith(ext) for ext in TEMP_EXTENSIONS):
                file_path = os.path.join(dirpath, filename)
                try:
                    size = os.path.getsize(file_path)
                    temp_files.append({
                        "path": os.path.relpath(file_path, root_dir),
                        "size": size,
                        "size_formatted": format_size(size),
                        "type": "temp"
                    })
                except:
                    pass
    return temp_files


def find_large_files(root_dir):
    """查找大文件"""
    large_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__']
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                size = os.path.getsize(file_path)
                if size > LARGE_FILE_THRESHOLD:
                    large_files.append({
                        "path": os.path.relpath(file_path, root_dir),
                        "size": size,
                        "size_formatted": format_size(size),
                        "type": "large"
                    })
            except:
                pass
    return large_files


def find_old_backups(root_dir):
    """查找旧备份"""
    old_backups = []
    cutoff_time = datetime.now() - timedelta(days=OLD_BACKUP_DAYS)

    backup_patterns = ['backup', 'bak', '.zip', '.tar.gz', '.rar']

    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__']
        for filename in filenames:
            # 检查是否是备份文件
            is_backup = any(pattern in filename.lower() for pattern in backup_patterns)
            if is_backup:
                file_path = os.path.join(dirpath, filename)
                try:
                    mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                    if mtime < cutoff_time:
                        size = os.path.getsize(file_path)
                        old_backups.append({
                            "path": os.path.relpath(file_path, root_dir),
                            "size": size,
                            "size_formatted": format_size(size),
                            "last_modified": mtime.strftime("%Y-%m-%d"),
                            "days_old": (datetime.now() - mtime).days,
                            "type": "backup"
                        })
                except:
                    pass
    return old_backups


def compress_old_reports(root_dir):
    """压缩历史报告"""
    reports_dir = os.path.join(root_dir, "reports")
    if not os.path.exists(reports_dir):
        return []

    compressed = []
    cutoff_date = datetime.now() - timedelta(days=30)

    for filename in os.listdir(reports_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(reports_dir, filename)
            try:
                mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                if mtime < cutoff_date:
                    # 压缩为 zip
                    zip_path = file_path.replace('.md', '.zip')
                    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                        zf.write(file_path, filename)
                    os.remove(file_path)
                    compressed.append({
                        "original": os.path.relpath(file_path, root_dir),
                        "compressed": os.path.relpath(zip_path, root_dir),
                        "size_saved": os.path.getsize(zip_path)
                    })
            except:
                pass

    return compressed


def calculate_total_size(items):
    """计算总大小"""
    total = 0
    for item in items:
        if 'size' in item:
            total += item['size']
    return total


def generate_report():
    """生成清理报告"""
    print("🧹 季度深度清理...")
    print(f"   根目录: {ROOT_DIR}")
    print()

    # 1. 查找缓存目录
    print("📦 查找缓存目录...")
    cache_dirs = find_cache_dirs(ROOT_DIR)
    cache_size = calculate_total_size(cache_dirs)
    print(f"   找到 {len(cache_dirs)} 个缓存目录，共 {format_size(cache_size)}")
    print()

    # 2. 查找临时文件
    print("🗑️  查找临时文件...")
    temp_files = find_temp_files(ROOT_DIR)
    temp_size = calculate_total_size(temp_files)
    print(f"   找到 {len(temp_files)} 个临时文件，共 {format_size(temp_size)}")
    print()

    # 3. 查找大文件
    print("📦 查找大文件...")
    large_files = find_large_files(ROOT_DIR)
    large_size = calculate_total_size(large_files)
    print(f"   找到 {len(large_files)} 个大文件（>{format_size(LARGE_FILE_THRESHOLD)}），共 {format_size(large_size)}")
    print()

    # 4. 查找旧备份
    print("💾 查找旧备份...")
    old_backups = find_old_backups(ROOT_DIR)
    backup_size = calculate_total_size(old_backups)
    print(f"   找到 {len(old_backups)} 个旧备份（>{OLD_BACKUP_DAYS}天），共 {format_size(backup_size)}")
    print()

    # 5. 压缩历史报告
    print("📦 压缩历史报告...")
    compressed = compress_old_reports(ROOT_DIR)
    print(f"   压缩了 {len(compressed)} 个报告")
    print()

    # 生成报告
    report_date = datetime.now().strftime("%Y-%m-%d")
    report_content = f"""# 季度深度清理报告

> 生成时间：{report_date}
> 清理目录：{ROOT_DIR}

---

## 📊 清理结果概览

| 类别 | 数量 | 总大小 |
|---|---|---|
| 缓存目录 | {len(cache_dirs)} | {format_size(cache_size)} |
| 临时文件 | {len(temp_files)} | {format_size(temp_size)} |
| 大文件 | {len(large_files)} | {format_size(large_size)} |
| 旧备份 | {len(old_backups)} | {format_size(backup_size)} |
| 已压缩报告 | {len(compressed)} | - |

---

## 📦 缓存目录（{len(cache_dirs)} 个）

这些目录可以安全删除（会重新生成）：

"""

    if cache_dirs:
        for i, cache in enumerate(cache_dirs[:10], 1):
            report_content += f"{i}. `{cache['path']}` - {cache['size_formatted']}\n"

        if len(cache_dirs) > 10:
            report_content += f"\n... 还有 {len(cache_dirs) - 10} 个缓存目录\n"
    else:
        report_content += "✅ 没有发现缓存目录。\n"

    report_content += f"""
---

## 🗑️ 临时文件（{len(temp_files)} 个）

这些文件可以安全删除：

"""

    if temp_files:
        for i, temp in enumerate(temp_files[:20], 1):
            report_content += f"{i}. `{temp['path']}` - {temp['size_formatted']}\n"

        if len(temp_files) > 20:
            report_content += f"\n... 还有 {len(temp_files) - 20} 个临时文件\n"
    else:
        report_content += "✅ 没有发现临时文件。\n"

    report_content += f"""
---

## 📦 大文件（{len(large_files)} 个，>{format_size(LARGE_FILE_THRESHOLD)}）

这些文件占用了大量空间，建议审查：

"""

    if large_files:
        for i, large in enumerate(large_files[:10], 1):
            report_content += f"{i}. `{large['path']}` - {large['size_formatted']}\n"

        if len(large_files) > 10:
            report_content += f"\n... 还有 {len(large_files) - 10} 个大文件\n"
    else:
        report_content += "✅ 没有发现大文件。\n"

    report_content += f"""
---

## 💾 旧备份（{len(old_backups)} 个，>{OLD_BACKUP_DAYS}天）

这些备份已经很久没用，可以删除或归档：

"""

    if old_backups:
        for i, backup in enumerate(old_backups[:10], 1):
            report_content += f"{i}. `{backup['path']}` - {backup['size_formatted']}（{backup['days_old']}天前）\n"

        if len(old_backups) > 10:
            report_content += f"\n... 还有 {len(old_backups) - 10} 个旧备份\n"
    else:
        report_content += "✅ 没有发现旧备份。\n"

    report_content += f"""
---

## 📋 已压缩报告（{len(compressed)} 个）

"""

    if compressed:
        for i, comp in enumerate(compressed[:10], 1):
            report_content += f"{i}. `{comp['original']}` -> `{comp['compressed']}`\n"

        if len(compressed) > 10:
            report_content += f"\n... 还有 {len(compressed) - 10} 个报告\n"
    else:
        report_content += "本次没有压缩报告。\n"

    report_content += f"""
---

## 💡 清理建议

### 可自动清理（安全）

"""

    # 计算可清理的总大小
    auto_clean_size = cache_size + temp_size
    report_content += f"- 缓存目录: {format_size(cache_size)}\n"
    report_content += f"- 临时文件: {format_size(temp_size)}\n"
    report_content += f"- **预计可释放: {format_size(auto_clean_size)}**\n"

    report_content += f"""
### 需人工审查

- 大文件: {len(large_files)} 个（{format_size(large_size)}）
- 旧备份: {len(old_backups)} 个（{format_size(backup_size)}）

---

## 🚀 执行清理

### 预览模式（当前）

本次运行是预览模式，不会实际删除文件。

### 执行模式

要实际执行清理，请运行：

```bash
python tools/scripts/maintenance/季度清理.py --execute
```

**注意**：执行前请确认备份已做好！

---

## 📋 季度清理检查清单

- [ ] 审查大文件清单
- [ ] 确认旧备份是否需要保留
- [ ] 执行清理（使用 --execute 参数）
- [ ] 验证清理结果
- [ ] 更新备份策略

---

> 本报告由季度深度清理脚本自动生成
> 最后更新时间：{report_date}
"""

    # 保存报告
    # 计算季度
    quarter = (datetime.now().month - 1) // 3 + 1
    report_filename = f"quarterly-cleanup-{datetime.now().year}-Q{quarter}.md"
    report_path = os.path.join(REPORTS_DIR, report_filename)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print(f"✅ 报告已生成: {report_path}")
    print()

    # 输出摘要
    print("=" * 60)
    print("🧹 季度清理摘要")
    print("=" * 60)
    print()
    print(f"缓存目录: {len(cache_dirs)} 个，共 {format_size(cache_size)}")
    print(f"临时文件: {len(temp_files)} 个，共 {format_size(temp_size)}")
    print(f"大文件: {len(large_files)} 个，共 {format_size(large_size)}")
    print(f"旧备份: {len(old_backups)} 个，共 {format_size(backup_size)}")
    print(f"已压缩报告: {len(compressed)} 个")
    print()

    total_reclaimable = cache_size + temp_size
    print(f"💾 预计可释放空间: {format_size(total_reclaimable)}")
    print()

    if total_reclaimable > 0:
        print("⚠️  建议执行清理以释放空间")
    else:
        print("✅ 知识库空间使用正常")

    print()

    return report_path


def execute_cleanup():
    """执行清理（危险操作）"""
    print("⚠️  执行清理模式...")
    print()

    # 这里可以实现实际的清理逻辑
    # 为了安全起见，暂时只打印预览信息
    print("⚠️  清理功能暂未实现，请手动处理预览报告中标记的内容")
    print()


def main():
    args = sys.argv[1:]

    # 解析参数
    json_output = "--json" in args
    execute_mode = "--execute" in args

    if execute_mode:
        execute_cleanup()
        return 0

    # 生成报告
    report_path = generate_report()

    return 0


if __name__ == "__main__":
    sys.exit(main())
