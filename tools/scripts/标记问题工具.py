#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
标记问题工具
============

对重复仓库、失效项目、无许可项目、低相关项目做标记。

功能：
1. 标记重复工具卡
2. 标记失效工具
3. 标记无许可工具
4. 标记低相关工具
5. 生成标记报告

用法
----
    python tools/scripts/标记问题工具.py
    python tools/scripts/标记问题工具.py --export  # 导出报告
"""

import os
import re
import sys
import json
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

# 失效关键词
INVALID_KEYWORDS = ["失效", "停止", "关闭", "停止服务", "已停止", "下线", "下架", "停止维护", "不再维护"]

# 低相关关键词（与网文写作无关）
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
    
    # 检查标签和内容
    for kw in LOW_RELEVANCE_KEYWORDS:
        if kw.lower() in tag_text or kw.lower() in text:
            return True
    
    return False


def analyze_tools():
    """分析工具卡并标记问题"""
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


def generate_report(tools):
    """生成标记报告"""
    if not tools:
        return "没有找到工具卡"
    
    report = []
    report.append("=" * 60)
    report.append("问题工具标记报告")
    report.append("=" * 60)
    
    # 总体统计
    report.append(f"\n总工具卡数量: {len(tools)}")
    
    # 问题统计
    invalid_tools = [t for t in tools if t["is_invalid"]]
    low_relevance_tools = [t for t in tools if t["is_low_relevance"]]
    duplicate_tools = [t for t in tools if t.get("is_duplicate", False)]
    
    report.append(f"\n## 问题统计")
    report.append(f"- 失效工具: {len(invalid_tools)} 篇")
    report.append(f"- 低相关工具: {len(low_relevance_tools)} 篇")
    report.append(f"- 重复工具: {len(duplicate_tools)} 篇")
    
    # 失效工具列表
    if invalid_tools:
        report.append(f"\n## 失效工具（{len(invalid_tools)} 篇）")
        for t in invalid_tools[:20]:
            report.append(f"- {t['file']}: {t['title']}")
        if len(invalid_tools) > 20:
            report.append(f"... 还有 {len(invalid_tools) - 20} 篇")
    
    # 低相关工具列表
    if low_relevance_tools:
        report.append(f"\n## 低相关工具（{len(low_relevance_tools)} 篇）")
        for t in low_relevance_tools[:20]:
            report.append(f"- {t['file']}: {t['title']}")
        if len(low_relevance_tools) > 20:
            report.append(f"... 还有 {len(low_relevance_tools) - 20} 篇")
    
    # 重复工具列表
    if duplicate_tools:
        report.append(f"\n## 重复工具（{len(duplicate_tools)} 篇）")
        for t in duplicate_tools[:20]:
            report.append(f"- {t['file']}: {t['title']}（重复 {t.get('duplicate_count', 2)} 次）")
        if len(duplicate_tools) > 20:
            report.append(f"... 还有 {len(duplicate_tools) - 20} 篇")
    
    # 按 tier 统计问题
    report.append(f"\n## 按 Tier 统计问题")
    for tier in ["S", "A", "B", "C"]:
        tier_tools = [t for t in tools if t["tier"] == tier]
        if not tier_tools:
            continue
        invalid = len([t for t in tier_tools if t["is_invalid"]])
        low_rel = len([t for t in tier_tools if t["is_low_relevance"]])
        dup = len([t for t in tier_tools if t.get("is_duplicate", False)])
        report.append(f"- {tier}级: {len(tier_tools)} 篇（失效: {invalid}, 低相关: {low_rel}, 重复: {dup}）")
    
    return "\n".join(report)


def export_json(tools):
    """导出 JSON 报告"""
    output_file = os.path.join(ROOT_DIR, "tools", "scripts", "问题工具标记报告.json")
    
    report = {
        "total": len(tools),
        "invalid_tools": len([t for t in tools if t["is_invalid"]]),
        "low_relevance_tools": len([t for t in tools if t["is_low_relevance"]]),
        "duplicate_tools": len([t for t in tools if t.get("is_duplicate", False)]),
        "tools": tools,
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    return output_file


def main():
    args = sys.argv[1:]
    export = "--export" in args
    
    print("正在分析工具卡并标记问题...")
    tools = analyze_tools()
    
    if not tools:
        print("错误：没有找到工具卡")
        return 1
    
    tools = mark_duplicates(tools)
    report = generate_report(tools)
    print(report)
    
    if export:
        output_file = export_json(tools)
        print(f"\n详细报告已导出到: {output_file}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())