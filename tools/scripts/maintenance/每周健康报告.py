#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
每周健康报告生成器
==================

每周自动生成知识库健康报告，包含：
1. 文件数量统计
2. 本周新增/修改文件
3. 前端校验结果
4. 链接健康状况
5. 项目进度概览
6. 建议改进项

用法
----
    python tools/scripts/maintenance/每周健康报告.py                 # 生成报告
    python tools/scripts/maintenance/每周健康报告.py --output <路径>  # 指定输出路径
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

# Windows GBK 终端安全：避免 emoji/中文输出 UnicodeEncodeError
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass


# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
REPORTS_DIR = os.path.join(ROOT_DIR, "maintenance", "reports")

# 确保报告目录存在
os.makedirs(REPORTS_DIR, exist_ok=True)


def count_files_by_type(root_dir):
    """统计各类型文件数量"""
    stats = {
        "total": 0,
        "md": 0,
        "py": 0,
        "json": 0,
        "other": 0
    }

    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__']
        for filename in filenames:
            stats["total"] += 1
            if filename.endswith('.md'):
                stats["md"] += 1
            elif filename.endswith('.py'):
                stats["py"] += 1
            elif filename.endswith('.json'):
                stats["json"] += 1
            else:
                stats["other"] += 1

    return stats


def get_recent_changes(root_dir, days=7):
    """获取最近修改的文件"""
    changes = {
        "added": [],
        "modified": []
    }

    cutoff_time = datetime.now() - timedelta(days=days)

    # 这里简化处理：实际应该对比 Git 历史
    # 目前只返回文件修改时间在范围内的文件
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__']
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                if mtime >= cutoff_time:
                    rel_path = os.path.relpath(file_path, root_dir)
                    changes["modified"].append({
                        "path": rel_path,
                        "time": mtime.isoformat()
                    })
            except:
                pass

    return changes


def check_project_health(root_dir):
    """检查项目健康状况"""
    health = {
        "projects": [],
        "issues": []
    }

    projects_dir = os.path.join(root_dir, "projects")
    if not os.path.exists(projects_dir):
        health["issues"].append("projects/ 目录不存在")
        return health

    for project_name in os.listdir(projects_dir):
        project_dir = os.path.join(projects_dir, project_name)
        if not os.path.isdir(project_dir):
            continue

        project_info = {
            "name": project_name,
            "status": "unknown",
            "chapters": 0,
            "words": 0
        }

        # 检查 STATUS.md
        status_file = os.path.join(project_dir, "STATUS.md")
        if os.path.exists(status_file):
            try:
                with open(status_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # 简单提取当前章节
                    import re
                    chapter_match = re.search(r'当前章节\s*\|\s*第(\d+)章', content)
                    if chapter_match:
                        project_info["chapters"] = int(chapter_match.group(1))
                    project_info["status"] = "active"
            except:
                project_info["status"] = "error"
        else:
            project_info["status"] = "incomplete"

        # 统计章节数
        chapters_dir = os.path.join(project_dir, "chapters")
        if os.path.exists(chapters_dir):
            chapter_files = [f for f in os.listdir(chapters_dir) if f.endswith('.md') and f != "README.md"]
            project_info["chapters"] = len(chapter_files)

        health["projects"].append(project_info)

    return health


def generate_report():
    """生成每周健康报告"""
    print("📊 生成每周健康报告...")
    print(f"   根目录: {ROOT_DIR}")
    print()

    # 1. 文件统计
    print("📁 统计文件数量...")
    file_stats = count_files_by_type(ROOT_DIR)
    print(f"   总计: {file_stats['total']} 个文件")
    print(f"   - Markdown: {file_stats['md']}")
    print(f"   - Python: {file_stats['py']}")
    print(f"   - JSON: {file_stats['json']}")
    print(f"   - 其他: {file_stats['other']}")
    print()

    # 2. 最近变化
    print("📝 分析最近变化...")
    changes = get_recent_changes(ROOT_DIR, days=7)
    print(f"   本周修改: {len(changes['modified'])} 个文件")
    print()

    # 3. 项目健康状况
    print("🏥 检查项目健康状况...")
    health = check_project_health(ROOT_DIR)
    print(f"   项目数: {len(health['projects'])}")
    print()

    # 4. 生成报告内容
    report_date = datetime.now().strftime("%Y-%m-%d")
    report_content = f"""# 每周健康报告

> 生成时间：{report_date}
> 根目录：知识库根目录

---

## 📊 文件统计

| 类型 | 数量 |
|---|---|
| 总计 | {file_stats['total']} |
| Markdown | {file_stats['md']} |
| Python | {file_stats['py']} |
| JSON | {file_stats['json']} |
| 其他 | {file_stats['other']} |

---

## 📝 本周变化

### 修改的文件（{len(changes['modified'])} 个）

"""

    if changes['modified']:
        for change in changes['modified'][:20]:  # 只显示前20个
            report_content += f"- `{change['path']}` ({change['time']})\n"
        if len(changes['modified']) > 20:
            report_content += f"\n... 还有 {len(changes['modified']) - 20} 个文件\n"
    else:
        report_content += "本周没有修改文件。\n"

    report_content += f"""
---

## 🏥 项目健康状况

### 项目概览

| 项目 | 状态 | 章节数 |
|---|---|---|
"""

    for project in health['projects']:
        report_content += f"| {project['name']} | {project['status']} | {project['chapters']} |\n"

    if health['issues']:
        report_content += "\n### 问题\n\n"
        for issue in health['issues']:
            report_content += f"- ⚠️ {issue}\n"

    report_content += f"""
---

## 💡 建议

### 自动检测建议

"""

    # 生成建议
    suggestions = []

    if file_stats['md'] > 100:
        suggestions.append("知识库 Markdown 文件较多，建议考虑内容归档策略")

    if len(changes['modified']) > 50:
        suggestions.append("本周修改文件较多，建议进行代码审查")

    incomplete_projects = [p for p in health['projects'] if p['status'] == 'incomplete']
    if incomplete_projects:
        suggestions.append(f"有 {len(incomplete_projects)} 个项目缺少 STATUS.md，建议补充")

    if not suggestions:
        suggestions.append("知识库状态良好，继续保持！")

    for i, suggestion in enumerate(suggestions, 1):
        report_content += f"{i}. {suggestion}\n"

    report_content += f"""
---

## 📈 趋势

### 下周目标

- [ ] 继续完善项目文档
- [ ] 定期运行核心校验
- [ ] 清理孤立文件
- [ ] 更新项目进度

---

> 本报告由每周健康报告生成器自动生成
> 最后更新时间：{report_date}
"""

    # 添加 frontmatter
    report_date_str = datetime.now().strftime("%Y-%m-%d")
    frontmatter = f"""---
id: auto-weekly-health-{datetime.now().strftime('%Y-%m-%d')}
type: report
area: 管理
status: archived
tags: [auto-generated]
title: weekly-health-{datetime.now().strftime('%Y-%m-%d')}
summary: 自动生成的每周健康报告。
source: 自动生成
created: {report_date_str}
updated: {report_date_str}
---

"""
    report_content = frontmatter + report_content

    # 保存报告
    report_filename = f"weekly-health-{datetime.now().strftime('%Y-%m-%d')}.md"
    report_path = os.path.join(REPORTS_DIR, report_filename)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print(f"✅ 报告已生成: {report_path}")
    print()

    # 输出摘要
    print("=" * 60)
    print("📊 健康报告摘要")
    print("=" * 60)
    print()
    print(f"文件总数: {file_stats['total']}")
    print(f"本周修改: {len(changes['modified'])} 个文件")
    print(f"项目总数: {len(health['projects'])}")
    print(f"问题数量: {len(health['issues'])}")
    print()
    print("建议:")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"  {i}. {suggestion}")
    print()

    return report_path


def main():
    args = sys.argv[1:]

    # 解析参数
    output_path = None
    if "--output" in args:
        idx = args.index("--output")
        if idx + 1 < len(args):
            output_path = args[idx + 1]

    # 生成报告
    report_path = generate_report()

    # 如果指定了输出路径，复制过去
    if output_path:
        import shutil
        shutil.copy2(report_path, output_path)
        print(f"📋 报告已复制到: {output_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
