#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
生成首页统计数据
================

自动生成 README.md 中的统计数据：
1. 各目录文件数统计
2. 工具卡数量统计
3. 当前项目表

用法
----
    python tools/scripts/生成首页统计.py
    python tools/scripts/生成首页统计.py --update-readme  # 自动更新 README.md
"""

import os
import re
import sys
import json
from pathlib import Path
from datetime import datetime

# 脚本目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))

# 目录定义
DIRECTORIES = {
    "schema": "规范文件",
    "projects": "项目",
    "knowledge": "结构化知识",
    "drafts": "草稿",
    "archive": "归档",
    "references": "参考资料",
    "methods": "方法论",
    "tools": "工具卡 + 脚本",
    "goals": "目标管理",
}

# 排除的目录
EXCLUDE_DIRS = {".git", ".workbuddy", ".tools", "__pycache__", "node_modules"}


def count_files(directory):
    """统计目录中的文件数"""
    count = 0
    if not os.path.exists(directory):
        return 0
    for root, dirs, files in os.walk(directory):
        # 排除指定目录
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            if f.endswith('.md'):
                count += 1
    return count


def count_tool_cards():
    """统计工具卡数量"""
    tools_dir = os.path.join(ROOT_DIR, "tools", "cards")
    if not os.path.exists(tools_dir):
        return 0
    count = 0
    for f in os.listdir(tools_dir):
        if f.endswith('.md'):
            count += 1
    return count


def get_tool_card_stats():
    """获取工具卡统计数据"""
    tools_dir = os.path.join(ROOT_DIR, "tools", "cards")
    if not os.path.exists(tools_dir):
        return {"S": 0, "A": 0, "B": 0, "C": 0, "total": 0}
    
    stats = {"S": 0, "A": 0, "B": 0, "C": 0, "total": 0}
    
    for f in os.listdir(tools_dir):
        if not f.endswith('.md'):
            continue
        file_path = os.path.join(tools_dir, f)
        try:
            with open(file_path, 'r', encoding='utf-8') as fh:
                content = fh.read()
                # 提取 tier 字段（支持带引号和不带引号）
                match = re.search(r'tier:\s*"?([SABC])"?', content)
                if match:
                    tier = match.group(1)
                    stats[tier] += 1
                    stats["total"] += 1
        except:
            pass
    
    return stats


def get_projects():
    """获取项目列表"""
    projects_dir = os.path.join(ROOT_DIR, "projects")
    if not os.path.exists(projects_dir):
        return []
    
    projects = []
    for project_name in os.listdir(projects_dir):
        project_dir = os.path.join(projects_dir, project_name)
        if not os.path.isdir(project_dir):
            continue
        
        # 读取 README.md
        readme_path = os.path.join(project_dir, "README.md")
        if os.path.exists(readme_path):
            try:
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # 提取标题
                    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                    title = title_match.group(1) if title_match else project_name
                    projects.append({
                        "name": project_name,
                        "title": title,
                        "path": f"projects/{project_name}/README.md"
                    })
            except:
                pass
    
    return projects


def generate_stats():
    """生成统计数据"""
    stats = {
        "timestamp": datetime.now().strftime("%Y-%m-%d"),
        "directories": {},
        "total_files": 0,
        "projects": [],
        "tool_cards": {},
    }
    
    # 统计各目录文件数
    for dir_name, description in DIRECTORIES.items():
        dir_path = os.path.join(ROOT_DIR, dir_name)
        count = count_files(dir_path)
        stats["directories"][dir_name] = {
            "count": count,
            "description": description
        }
        stats["total_files"] += count
    
    # 统计工具卡
    tool_stats = get_tool_card_stats()
    stats["tool_cards"] = tool_stats
    
    # 获取项目列表
    stats["projects"] = get_projects()
    
    return stats


def generate_markdown(stats):
    """生成 Markdown 格式的统计数据"""
    md = ""
    
    # 目录统计
    md += "### 目录统计\n"
    md += "| 目录 | 文件数 | 说明 |\n"
    md += "|---|---|---|\n"
    for dir_name, dir_info in stats["directories"].items():
        md += f"| `{dir_name}/` | {dir_info['count']} | {dir_info['description']} |\n"
    md += f"\n**总计**：约 {stats['total_files']}+ 个文件\n"
    
    # 项目统计
    md += "\n### 项目统计\n"
    md += f"- 活跃项目：{len(stats['projects'])} 个\n"
    md += "- 草稿项目：0 个\n"
    md += "- 归档项目：1 个\n"
    
    # 工具卡统计
    md += "\n### 工具卡统计\n"
    tool_cards = stats["tool_cards"]
    md += f"- 总数量：{tool_cards['total']} 篇\n"
    md += f"- S级：{tool_cards['S']} 篇\n"
    md += f"- A级：{tool_cards['A']} 篇\n"
    md += f"- B级：{tool_cards['B']} 篇\n"
    md += f"- C级：{tool_cards['C']} 篇\n"
    
    return md


def update_readme(stats):
    """更新 README.md 中的统计数据"""
    readme_path = os.path.join(ROOT_DIR, "README.md")
    if not os.path.exists(readme_path):
        print("错误：README.md 不存在")
        return False
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 生成新的统计数据
    new_stats = generate_markdown(stats)
    
    # 替换统计数据部分
    # 查找 "## 📊 快速统计" 到下一个 "## " 之间的内容
    pattern = r'(## 📊 快速统计\s*\n)(.*?)(\n## )'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        # 替换统计数据
        new_content = content[:match.start(2)] + new_stats + content[match.end(2):]
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"README.md 已更新（{stats['timestamp']}）")
        return True
    else:
        print("错误：未找到统计数据部分")
        print("README.md 中查找 '## 📊 快速统计'...")
        # 调试：查找所有 ## 标题
        headers = re.findall(r'^## .+$', content, re.MULTILINE)
        print(f"找到的标题: {headers[:10]}")
        return False


def main():
    args = sys.argv[1:]
    update_readme_flag = "--update-readme" in args
    
    # 生成统计数据
    stats = generate_stats()
    
    # 输出 JSON
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    
    # 更新 README.md
    if update_readme_flag:
        update_readme(stats)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())