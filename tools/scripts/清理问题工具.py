#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
清理问题工具
============

清理失效工具、低相关工具和重复工具。

功能：
1. 移动失效工具到 archive
2. 移动低相关工具到 archive
3. 合并重复工具
4. 生成清理报告

用法
----
    python tools/scripts/清理问题工具.py --dry-run    # 预览模式
    python tools/scripts/清理问题工具.py --execute     # 执行清理
    python tools/scripts/清理问题工具.py --export      # 导出报告
"""

import os
import re
import sys
import json
import shutil
from pathlib import Path
from collections import Counter

# Windows GBK 终端安全：避免 emoji/中文输出 UnicodeEncodeError
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass


# 脚本目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))

# 工具卡目录
TOOLS_DIR = os.path.join(ROOT_DIR, "tools", "cards")
ARCHIVE_DIR = os.path.join(ROOT_DIR, "archive", "问题工具")

# 失效关键词
INVALID_KEYWORDS = ["失效", "停止", "关闭", "停止服务", "已停止", "下线", "下架", "停止维护", "不再维护"]

# 低相关关键词
LOW_RELEVANCE_KEYWORDS = ["通用", "通用工具", "开发工具", "编程", "代码", "数据库", "服务器", "运维"]


def extract_tier(content):
    """提取 tier 字段"""
    match = re.search(r'tier:\s*"?([SABC])"?', content)
    return match.group(1) if match else None


def extract_title(content):
    """提取标题"""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1) if match else None


def extract_tags(content):
    """提取标签"""
    match = re.search(r'tags:\s*\[([^\]]+)\]', content)
    if match:
        tags_str = match.group(1)
        return [t.strip().strip('"').strip("'") for t in tags_str.split(",") if t.strip()]
    return []


def check_invalid(content):
    """检查是否失效"""
    return any(kw in content for kw in INVALID_KEYWORDS)


def check_low_relevance(content, tags):
    """检查是否低相关"""
    text = content.lower()
    tag_text = " ".join(tags).lower()
    
    for kw in LOW_RELEVANCE_KEYWORDS:
        if kw.lower() in tag_text or kw.lower() in text:
            return True
    
    return False


def analyze_tools():
    """分析工具卡"""
    if not os.path.exists(TOOLS_DIR):
        print(f"错误：工具卡目录不存在: {TOOLS_DIR}")
        return None
    
    tools = []
    for f in os.listdir(TOOLS_DIR):
        if not f.endswith('.md'):
            continue
        
        file_path = os.path.join(TOOLS_DIR, f)
        try:
            with open(file_path, 'r', encoding='utf-8') as fh:
                content = fh.read()
                
                tier = extract_tier(content)
                title = extract_title(content)
                tags = extract_tags(content)
                is_invalid = check_invalid(content)
                is_low_relevance = check_low_relevance(content, tags)
                
                tools.append({
                    "file": f,
                    "path": file_path,
                    "tier": tier,
                    "title": title,
                    "tags": tags,
                    "is_invalid": is_invalid,
                    "is_low_relevance": is_low_relevance,
                })
        except Exception as e:
            print(f"警告：读取文件失败 {f}: {e}")
    
    return tools


def mark_duplicates(tools):
    """标记重复工具"""
    title_counter = Counter(t["title"] for t in tools if t["title"])
    duplicates = {title: count for title, count in title_counter.items() if count > 1}
    
    marked = []
    for tool in tools:
        if tool["title"] in duplicates:
            tool["is_duplicate"] = True
            tool["duplicate_count"] = duplicates[tool["title"]]
        else:
            tool["is_duplicate"] = False
        marked.append(tool)
    
    return marked


def move_to_archive(tool, category):
    """移动工具到 archive"""
    # 创建目标目录
    target_dir = os.path.join(ARCHIVE_DIR, category)
    os.makedirs(target_dir, exist_ok=True)
    
    # 移动文件
    target_path = os.path.join(target_dir, tool["file"])
    shutil.move(tool["path"], target_path)
    
    return target_path


def clean_invalid_tools(tools, dry_run=True):
    """清理失效工具"""
    invalid_tools = [t for t in tools if t["is_invalid"]]
    
    if not invalid_tools:
        print("没有失效工具需要清理")
        return []
    
    print(f"\n{'[预览]' if dry_run else '[执行]'} 清理失效工具（{len(invalid_tools)} 篇）")
    
    moved = []
    for tool in invalid_tools:
        if dry_run:
            print(f"  将移动: {tool['file']}")
        else:
            target = move_to_archive(tool, "失效工具")
            print(f"  已移动: {tool['file']} -> {target}")
            moved.append(target)
    
    return moved


def clean_low_relevance_tools(tools, dry_run=True):
    """清理低相关工具"""
    low_relevance_tools = [t for t in tools if t["is_low_relevance"]]
    
    if not low_relevance_tools:
        print("没有低相关工具需要清理")
        return []
    
    print(f"\n{'[预览]' if dry_run else '[执行]'} 清理低相关工具（{len(low_relevance_tools)} 篇）")
    
    moved = []
    for tool in low_relevance_tools:
        if dry_run:
            print(f"  将移动: {tool['file']}")
        else:
            target = move_to_archive(tool, "低相关工具")
            print(f"  已移动: {tool['file']} -> {target}")
            moved.append(target)
    
    return moved


def clean_duplicate_tools(tools, dry_run=True):
    """清理重复工具"""
    duplicate_tools = [t for t in tools if t.get("is_duplicate", False)]
    
    if not duplicate_tools:
        print("没有重复工具需要清理")
        return []
    
    print(f"\n{'[预览]' if dry_run else '[执行]'} 清理重复工具（{len(duplicate_tools)} 篇）")
    
    moved = []
    for tool in duplicate_tools:
        if dry_run:
            print(f"  将移动: {tool['file']}（重复 {tool.get('duplicate_count', 2)} 次）")
        else:
            target = move_to_archive(tool, "重复工具")
            print(f"  已移动: {tool['file']} -> {target}")
            moved.append(target)
    
    return moved


def generate_report(tools, invalid_moved, low_relevance_moved, duplicate_moved):
    """生成清理报告"""
    report = []
    report.append("=" * 60)
    report.append("问题工具清理报告")
    report.append("=" * 60)
    
    report.append(f"\n总工具卡数量: {len(tools)}")
    report.append(f"失效工具清理: {len(invalid_moved)} 篇")
    report.append(f"低相关工具清理: {len(low_relevance_moved)} 篇")
    report.append(f"重复工具清理: {len(duplicate_moved)} 篇")
    report.append(f"总计清理: {len(invalid_moved) + len(low_relevance_moved) + len(duplicate_moved)} 篇")
    
    report.append(f"\n清理后剩余: {len(tools) - len(invalid_moved) - len(low_relevance_moved) - len(duplicate_moved)} 篇")
    
    return "\n".join(report)


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args or "--execute" not in args
    export = "--export" in args
    
    print("正在分析问题工具...")
    tools = analyze_tools()
    
    if not tools:
        print("错误：没有找到工具卡")
        return 1
    
    tools = mark_duplicates(tools)
    
    print(f"\n找到 {len(tools)} 个工具卡")
    print(f"失效工具: {len([t for t in tools if t['is_invalid']])} 篇")
    print(f"低相关工具: {len([t for t in tools if t['is_low_relevance']])} 篇")
    print(f"重复工具: {len([t for t in tools if t.get('is_duplicate', False)])} 篇")
    
    if dry_run:
        print("\n" + "=" * 60)
        print("预览模式（不会实际移动文件）")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("执行模式（将实际移动文件）")
        print("=" * 60)
    
    # 清理失效工具
    invalid_moved = clean_invalid_tools(tools, dry_run)
    
    # 清理低相关工具
    low_relevance_moved = clean_low_relevance_tools(tools, dry_run)
    
    # 清理重复工具
    duplicate_moved = clean_duplicate_tools(tools, dry_run)
    
    # 生成报告
    report = generate_report(tools, invalid_moved, low_relevance_moved, duplicate_moved)
    print("\n" + report)
    
    if export and not dry_run:
        output_file = os.path.join(ROOT_DIR, "tools", "scripts", "清理报告.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                "invalid_moved": len(invalid_moved),
                "low_relevance_moved": len(low_relevance_moved),
                "duplicate_moved": len(duplicate_moved),
            }, f, ensure_ascii=False, indent=2)
        print(f"\n报告已导出到: {output_file}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())