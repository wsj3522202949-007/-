#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
分析工具卡数据层
================

分析当前工具卡的分布、分类和内容质量。

功能：
1. 统计各分类工具卡数量
2. 分析 S/A 级工具卡特点
3. 识别重复仓库、失效项目、无许可项目、低相关项目
4. 建立工具卡质量评估标准

用法
----
    python tools/scripts/分析工具卡数据层.py
    python tools/scripts/分析工具卡数据层.py --export  # 导出报告
"""

import os
import re
import sys
import json
from pathlib import Path
from collections import Counter, defaultdict

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

# 分类关键词
CATEGORY_KEYWORDS = {
    "写作辅助": ["写作", "write", "writing", "生成", "generate", "创作", "创作"],
    "改稿润色": ["改稿", "润色", "revise", "polish", "润色", "去AI味", "AI味"],
    "研究调研": ["研究", "research", "调研", "调查", "搜索", "search"],
    "出版发布": ["出版", "publish", "发布", "发布", "排版", "layout"],
    "大纲规划": ["大纲", "outline", "规划", "plan", "结构", "structure"],
    "人物设定": ["人物", "character", "角色", "角色", "人物"],
    "世界观": ["世界观", "world", "设定", "setting", "设定"],
    "对话": ["对话", "dialogue", "对白", "对白"],
    "节奏": ["节奏", "pace", "节奏", "节奏"],
    "爽点": ["爽点", "climax", "高潮", "情绪", "emotion"],
}

# 平台关键词
PLATFORM_KEYWORDS = {
    "番茄": ["番茄", "fanqie", "tomato"],
    "起点": ["起点", "qidian"],
    "晋江": ["晋江", "jjwxc"],
    "短剧": ["短剧", "short drama", "短剧"],
    "纵横": ["纵横", "zongheng"],
    "17K": ["17K", "17k"],
}

# 失效关键词
INVALID_KEYWORDS = ["失效", "停止", "关闭", "停止服务", "已停止", "下线", "下架"]

# 许可关键词
LICENSE_KEYWORDS = ["无许可", "版权", "copyright", "授权", "license", "许可"]


def extract_tier(content):
    """提取 tier 字段"""
    match = re.search(r'tier:\s*"?([SABC])"?', content)
    return match.group(1) if match else None


def extract_title(content):
    """提取标题"""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1) if match else None


def extract_summary(content):
    """提取摘要"""
    match = re.search(r'summary:\s*(.+)', content)
    return match.group(1).strip() if match else None


def extract_tags(content):
    """提取标签"""
    match = re.search(r'tags:\s*\[([^\]]+)\]', content)
    if match:
        tags_str = match.group(1)
        return [t.strip().strip('"').strip("'") for t in tags_str.split(",") if t.strip()]
    return []


def extract_platform(content):
    """提取平台"""
    tags = extract_tags(content)
    platforms = []
    for tag in tags:
        for platform, keywords in PLATFORM_KEYWORDS.items():
            if any(kw in tag for kw in keywords):
                platforms.append(platform)
    return platforms


def check_invalid(content):
    """检查是否失效"""
    return any(kw in content for kw in INVALID_KEYWORDS)


def check_license(content):
    """检查许可状态"""
    return any(kw in content for kw in LICENSE_KEYWORDS)


def categorize_tool(content, title, tags):
    """分类工具"""
    text = (title + " " + " ".join(tags)).lower()
    
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(kw.lower() in text for kw in keywords):
            return category
    
    return "其他"


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
                summary = extract_summary(content)
                tags = extract_tags(content)
                platform = extract_platform(content)
                is_invalid = check_invalid(content)
                has_license_issue = check_license(content)
                category = categorize_tool(content, title, tags)
                
                tools.append({
                    "file": f,
                    "path": file_path,
                    "tier": tier,
                    "title": title,
                    "summary": summary,
                    "tags": tags,
                    "platform": platform,
                    "category": category,
                    "is_invalid": is_invalid,
                    "has_license_issue": has_license_issue,
                })
        except Exception as e:
            print(f"警告：读取文件失败 {f}: {e}")
    
    return tools


def generate_report(tools):
    """生成分析报告"""
    if not tools:
        return "没有找到工具卡"
    
    report = []
    report.append("=" * 60)
    report.append("工具卡数据层分析报告")
    report.append("=" * 60)
    
    # 总体统计
    report.append(f"\n总工具卡数量: {len(tools)}")
    
    # Tier 分布
    tier_counter = Counter(t["tier"] for t in tools if t["tier"])
    report.append("\n## Tier 分布")
    report.append(f"- S级: {tier_counter.get('S', 0)} 篇")
    report.append(f"- A级: {tier_counter.get('A', 0)} 篇")
    report.append(f"- B级: {tier_counter.get('B', 0)} 篇")
    report.append(f"- C级: {tier_counter.get('C', 0)} 篇")
    report.append(f"- 未分级: {len(tools) - sum(tier_counter.values())} 篇")
    
    # 分类分布
    category_counter = Counter(t["category"] for t in tools)
    report.append("\n## 分类分布")
    for category, count in category_counter.most_common():
        report.append(f"- {category}: {count} 篇")
    
    # 平台分布
    platform_counter = Counter()
    for t in tools:
        for p in t["platform"]:
            platform_counter[p] += 1
    report.append("\n## 平台分布")
    for platform, count in platform_counter.most_common():
        report.append(f"- {platform}: {count} 篇")
    
    # 问题工具
    invalid_tools = [t for t in tools if t["is_invalid"]]
    license_issues = [t for t in tools if t["has_license_issue"]]
    
    report.append(f"\n## 问题工具")
    report.append(f"- 失效工具: {len(invalid_tools)} 篇")
    report.append(f"- 许可问题: {len(license_issues)} 篇")
    
    if invalid_tools:
        report.append("\n### 失效工具列表")
        for t in invalid_tools[:10]:
            report.append(f"- {t['file']}: {t['title']}")
    
    if license_issues:
        report.append("\n### 许可问题列表")
        for t in license_issues[:10]:
            report.append(f"- {t['file']}: {t['title']}")
    
    # S/A 级工具
    sa_tools = [t for t in tools if t["tier"] in ["S", "A"]]
    report.append(f"\n## S/A 级工具（推荐层候选）")
    report.append(f"总计: {len(sa_tools)} 篇")
    
    sa_categories = Counter(t["category"] for t in sa_tools)
    report.append("\n### S/A 级工具分类")
    for category, count in sa_categories.most_common():
        report.append(f"- {category}: {count} 篇")
    
    # 重复检测
    report.append("\n## 重复检测")
    title_counter = Counter(t["title"] for t in tools if t["title"])
    duplicates = {title: count for title, count in title_counter.items() if count > 1}
    if duplicates:
        report.append(f"发现 {len(duplicates)} 个重复标题:")
        for title, count in list(duplicates.items())[:10]:
            report.append(f"- '{title}': {count} 篇")
    else:
        report.append("未发现重复标题")
    
    return "\n".join(report)


def export_json(tools):
    """导出 JSON 报告"""
    output_file = os.path.join(ROOT_DIR, "tools", "scripts", "工具卡分析报告.json")
    
    report = {
        "total": len(tools),
        "tier_distribution": dict(Counter(t["tier"] for t in tools if t["tier"])),
        "category_distribution": dict(Counter(t["category"] for t in tools)),
        "platform_distribution": dict(Counter(p for t in tools for p in t["platform"])),
        "invalid_tools": len([t for t in tools if t["is_invalid"]]),
        "license_issues": len([t for t in tools if t["has_license_issue"]]),
        "sa_tools": len([t for t in tools if t["tier"] in ["S", "A"]]),
        "duplicates": len({t["title"] for t in tools if t["title"] and Counter(t["title"] for t in tools)[t["title"]] > 1}),
        "tools": tools,
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    return output_file


def main():
    args = sys.argv[1:]
    export = "--export" in args
    
    print("正在分析工具卡数据层...")
    tools = analyze_tools()
    
    if not tools:
        print("错误：没有找到工具卡")
        return 1
    
    report = generate_report(tools)
    print(report)
    
    if export:
        output_file = export_json(tools)
        print(f"\n详细报告已导出到: {output_file}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())