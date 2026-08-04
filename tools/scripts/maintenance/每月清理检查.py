#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
每月清理检查
============

每月自动检查并报告以下内容：
1. 孤立笔记（无反向链接）
2. 重复内容检测
3. 陈旧状态文档（长期未更新）
4. 低价值资料识别
5. 清理建议生成

用法
----
    python tools/scripts/maintenance/每月清理检查.py                 # 运行检查
    python tools/scripts/maintenance/每月清理检查.py --json          # JSON 输出
    python tools/scripts/maintenance/每月清理检查.py --clean         # 自动清理可安全删除的文件
"""

import os
import sys
import json
import re
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

# 陈旧阈值：180 天未更新视为陈旧
STALE_DAYS = 180

# 低价值关键词（用于识别低价值资料）
LOW_VALUE_KEYWORDS = [
    "tmp", "temp", "test", "draft", "scratch",
    "未命名", "临时", "测试", "草稿"
]


def find_markdown_files(root_dir):
    """查找所有 Markdown 文件"""
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__']
        for filename in filenames:
            if filename.endswith('.md'):
                md_files.append(os.path.join(dirpath, filename))
    return md_files


def build_link_index(files):
    """构建链接索引（谁链接到了谁）"""
    link_index = defaultdict(set)  # target -> set of sources
    file_index = {}  # rel_path -> abs_path

    for file_path in files:
        rel_path = os.path.relpath(file_path, ROOT_DIR)
        file_index[rel_path] = file_path

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue

        # 查找所有内部链接
        link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        for match in link_pattern.finditer(content):
            link_target = match.group(2)
            if not link_target.startswith('http') and not link_target.startswith('#'):
                # 规范化目标路径
                file_dir = os.path.dirname(file_path)
                target_path = os.path.normpath(os.path.join(file_dir, link_target))
                target_rel = os.path.relpath(target_path, ROOT_DIR)
                link_index[target_rel].add(rel_path)

    return link_index, file_index


def find_orphan_notes(files, link_index, file_index):
    """查找孤立笔记（无反向链接）"""
    orphans = []

    for file_path in files:
        rel_path = os.path.relpath(file_path, ROOT_DIR)

        # 跳过特定目录
        if any(rel_path.startswith(d) for d in ['tools/cards/', 'archive/', '.git/']):
            continue

        # 检查是否有反向链接
        backlinks = link_index.get(rel_path, set())
        if not backlinks:
            # 检查是否是索引文件
            if rel_path.endswith('README.md') or rel_path.endswith('INDEX.md'):
                continue

            orphans.append({
                "path": rel_path,
                "reason": "无反向链接",
                "action": "考虑归档或删除"
            })

    return orphans


def find_duplicates(files):
    """查找重复内容"""
    duplicates = []

    # 按文件名分组
    filename_groups = defaultdict(list)
    for file_path in files:
        filename = os.path.basename(file_path)
        filename_groups[filename].append(file_path)

    # 检查同名文件
    for filename, paths in filename_groups.items():
        if len(paths) > 1:
            # 检查内容是否相似
            contents = []
            for path in paths:
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        contents.append(f.read())
                except:
                    contents.append("")

            # 简单检查：如果内容完全相同
            if len(set(contents)) == 1:
                duplicates.append({
                    "files": [os.path.relpath(p, ROOT_DIR) for p in paths],
                    "similarity": "100%",
                    "action": "删除重复副本"
                })

    return duplicates


def find_stale_docs(files):
    """查找陈旧文档"""
    stale_docs = []
    cutoff_time = datetime.now() - timedelta(days=STALE_DAYS)

    for file_path in files:
        try:
            mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            if mtime < cutoff_time:
                rel_path = os.path.relpath(file_path, ROOT_DIR)

                # 跳过归档目录
                if 'archive' in rel_path.lower():
                    continue

                stale_docs.append({
                    "path": rel_path,
                    "last_modified": mtime.strftime("%Y-%m-%d"),
                    "days_old": (datetime.now() - mtime).days,
                    "action": "考虑归档或更新"
                })
        except:
            pass

    # 按陈旧程度排序
    stale_docs.sort(key=lambda x: x['days_old'], reverse=True)

    return stale_docs


def find_low_value_content(files):
    """查找低价值内容"""
    low_value = []

    for file_path in files:
        filename = os.path.basename(file_path).lower()
        rel_path = os.path.relpath(file_path, ROOT_DIR)

        # 检查文件名是否包含低价值关键词
        for keyword in LOW_VALUE_KEYWORDS:
            if keyword in filename:
                low_value.append({
                    "path": rel_path,
                    "reason": f"文件名包含关键词: {keyword}",
                    "action": "考虑删除或重命名"
                })
                break

        # 检查文件大小（小于 100 字节可能是空文件）
        try:
            size = os.path.getsize(file_path)
            if size < 100 and not rel_path.endswith('README.md'):
                low_value.append({
                    "path": rel_path,
                    "reason": f"文件过小 ({size} 字节)",
                    "action": "考虑删除"
                })
        except:
            pass

    return low_value


def generate_report():
    """生成清理检查报告"""
    print("🧹 每月清理检查...")
    print(f"   根目录: {ROOT_DIR}")
    print()

    # 查找所有 Markdown 文件
    print("📁 扫描 Markdown 文件...")
    files = find_markdown_files(ROOT_DIR)
    print(f"   找到 {len(files)} 个文件")
    print()

    # 构建链接索引
    print("🔗 构建链接索引...")
    link_index, file_index = build_link_index(files)
    print(f"   索引完成")
    print()

    # 1. 查找孤立笔记
    print("🔍 查找孤立笔记...")
    orphans = find_orphan_notes(files, link_index, file_index)
    print(f"   找到 {len(orphans)} 个孤立笔记")
    print()

    # 2. 查找重复内容
    print("🔁 查找重复内容...")
    duplicates = find_duplicates(files)
    print(f"   找到 {len(duplicates)} 组重复文件")
    print()

    # 3. 查找陈旧文档
    print("📅 查找陈旧文档...")
    stale_docs = find_stale_docs(files)
    print(f"   找到 {len(stale_docs)} 个陈旧文档（>{STALE_DAYS}天未更新）")
    print()

    # 4. 查找低价值内容
    print("🗑️  查找低价值内容...")
    low_value = find_low_value_content(files)
    print(f"   找到 {len(low_value)} 个低价值文件")
    print()

    # 生成报告
    report_date = datetime.now().strftime("%Y-%m-%d")
    report_content = f"""# 每月清理检查报告

> 生成时间：{report_date}
> 检查目录：{ROOT_DIR}

---

## 📊 检查结果概览

| 检查项 | 数量 | 状态 |
|---|---|---|
| 孤立笔记 | {len(orphans)} | {'⚠️ 需要关注' if orphans else '✅ 正常'} |
| 重复文件 | {len(duplicates)} | {'⚠️ 需要处理' if duplicates else '✅ 正常'} |
| 陈旧文档 | {len(stale_docs)} | {'⚠️ 需要更新' if stale_docs else '✅ 正常'} |
| 低价值内容 | {len(low_value)} | {'⚠️ 需要清理' if low_value else '✅ 正常'} |

---

## 🔍 孤立笔记（{len(orphans)} 个）

这些文件没有其他文件链接到它们，可能是：

"""

    if orphans:
        for i, orphan in enumerate(orphans[:20], 1):
            report_content += f"{i}. `{orphan['path']}`\n"
            report_content += f"   - 原因: {orphan['reason']}\n"
            report_content += f"   - 建议: {orphan['action']}\n\n"

        if len(orphans) > 20:
            report_content += f"\n... 还有 {len(orphans) - 20} 个孤立笔记\n"
    else:
        report_content += "✅ 没有发现孤立笔记。\n"

    report_content += f"""
---

## 🔁 重复文件（{len(duplicates)} 组）

"""

    if duplicates:
        for i, dup in enumerate(duplicates[:10], 1):
            report_content += f"{i}. 相似度: {dup['similarity']}\n"
            report_content += f"   - 文件: {', '.join([f'`{f}`' for f in dup['files']])}\n"
            report_content += f"   - 建议: {dup['action']}\n\n"

        if len(duplicates) > 10:
            report_content += f"\n... 还有 {len(duplicates) - 10} 组重复文件\n"
    else:
        report_content += "✅ 没有发现重复文件。\n"

    report_content += f"""
---

## 📅 陈旧文档（{len(stale_docs)} 个，>{STALE_DAYS}天未更新）

"""

    if stale_docs:
        for i, doc in enumerate(stale_docs[:20], 1):
            report_content += f"{i}. `{doc['path']}`\n"
            report_content += f"   - 最后更新: {doc['last_modified']}（{doc['days_old']}天前）\n"
            report_content += f"   - 建议: {doc['action']}\n\n"

        if len(stale_docs) > 20:
            report_content += f"\n... 还有 {len(stale_docs) - 20} 个陈旧文档\n"
    else:
        report_content += "✅ 没有发现陈旧文档。\n"

    report_content += f"""
---

## 🗑️ 低价值内容（{len(low_value)} 个）

"""

    if low_value:
        for i, item in enumerate(low_value[:20], 1):
            report_content += f"{i}. `{item['path']}`\n"
            report_content += f"   - 原因: {item['reason']}\n"
            report_content += f"   - 建议: {item['action']}\n\n"

        if len(low_value) > 20:
            report_content += f"\n... 还有 {len(low_value) - 20} 个低价值文件\n"
    else:
        report_content += "✅ 没有发现低价值内容。\n"

    report_content += f"""
---

## 💡 清理建议

### 自动清理（安全）

以下文件可以安全删除：

"""

    # 生成清理建议
    safe_to_delete = []

    # 低价值临时文件
    for item in low_value:
        if 'tmp' in item['path'].lower() or 'temp' in item['path'].lower():
            safe_to_delete.append(item)

    # 完全重复的文件
    for dup in duplicates:
        if dup['similarity'] == '100%':
            # 保留第一个，删除其余
            for file_path in dup['files'][1:]:
                safe_to_delete.append({
                    "path": file_path,
                    "reason": "完全重复",
                    "action": "删除"
                })

    if safe_to_delete:
        for i, item in enumerate(safe_to_delete[:10], 1):
            report_content += f"{i}. `{item['path']}` - {item['reason']}\n"
    else:
        report_content += "没有可以安全自动清理的文件。\n"

    report_content += f"""
### 人工审查（需要确认）

以下文件需要人工审查后再决定：

1. **孤立笔记**：确认是否还有价值，无价值则归档
2. **陈旧文档**：确认是否过时，过时则更新或归档
3. **低价值内容**：确认是否有保留价值

---

## 📋 清理检查清单

- [ ] 审查孤立笔记清单
- [ ] 处理重复文件
- [ ] 更新或归档陈旧文档
- [ ] 清理低价值内容
- [ ] 更新相关索引

---

> 本报告由每月清理检查脚本自动生成
> 最后更新时间：{report_date}
"""

    # 保存报告
    report_filename = f"monthly-cleanup-{datetime.now().strftime('%Y-%m')}.md"
    report_path = os.path.join(REPORTS_DIR, report_filename)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print(f"✅ 报告已生成: {report_path}")
    print()

    # 输出摘要
    print("=" * 60)
    print("🧹 清理检查摘要")
    print("=" * 60)
    print()
    print(f"孤立笔记: {len(orphans)} 个")
    print(f"重复文件: {len(duplicates)} 组")
    print(f"陈旧文档: {len(stale_docs)} 个（>{STALE_DAYS}天）")
    print(f"低价值内容: {len(low_value)} 个")
    print()

    total_issues = len(orphans) + len(duplicates) + len(stale_docs) + len(low_value)
    if total_issues == 0:
        print("✅ 知识库状态良好，无需清理")
    else:
        print(f"⚠️  发现 {total_issues} 个问题，建议处理")

    print()

    return report_path


def main():
    args = sys.argv[1:]

    # 解析参数
    json_output = "--json" in args
    clean_mode = "--clean" in args

    # 生成报告
    report_path = generate_report()

    # 如果指定了清理模式，执行清理
    if clean_mode:
        print("🧹 自动清理模式（暂未实现，请手动处理）")
        # TODO: 实现自动清理逻辑

    return 0


if __name__ == "__main__":
    sys.exit(main())
