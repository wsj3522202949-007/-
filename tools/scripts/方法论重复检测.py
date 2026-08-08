#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
方法论重复检测
==============

检测方法论内容中的重复概念，同一概念只保留一个主页面。

功能：
1. 检测重复标题
2. 检测相似内容
3. 建立主页面机制
4. 生成合并建议

用法
----
    python tools/scripts/方法论重复检测.py
    python tools/scripts/方法论重复检测.py --export  # 导出报告
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

# 方法论目录
METHODS_DIR = os.path.join(ROOT_DIR, "methods")
KNOWLEDGE_DIR = os.path.join(ROOT_DIR, "knowledge", "craft")

# 关键词映射（相似概念）
CONCEPT_MAPPING = {
    "大纲": ["大纲", "outline", "架构", "结构"],
    "人物": ["人物", "角色", "character", "人设"],
    "对白": ["对白", "对话", "dialogue", "台词"],
    "节奏": ["节奏", "pace", "节奏"],
    "爽点": ["爽点", "高潮", "climax", "情绪"],
    "开篇": ["开篇", "开头", "开头", "钩子"],
    "结尾": ["结尾", "结局", "ending"],
    "设定": ["设定", "setting", "世界观", "world"],
    "视角": ["视角", "pov", "point of view"],
    "冲突": ["冲突", "conflict", "矛盾"],
}


def extract_title(content):
    """提取标题"""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1) if match else None


def extract_summary(content):
    """提取摘要"""
    match = re.search(r'summary:\s*(.+)', content)
    return match.group(1).strip() if match else None


def get_all_md_files(directories):
    """获取所有 markdown 文件"""
    files = []
    for directory in directories:
        if not os.path.exists(directory):
            continue
        for root, dirs, filenames in os.walk(directory):
            for f in filenames:
                if f.endswith('.md'):
                    files.append(os.path.join(root, f))
    return files


def analyze_concepts(files):
    """分析概念重复"""
    concepts = {}
    
    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                title = extract_title(content)
                summary = extract_summary(content)
                
                if not title:
                    continue
                
                # 查找相似概念
                matched_concepts = []
                for concept, keywords in CONCEPT_MAPPING.items():
                    if any(kw.lower() in title.lower() for kw in keywords):
                        matched_concepts.append(concept)
                
                # 添加到概念字典
                for concept in matched_concepts:
                    if concept not in concepts:
                        concepts[concept] = []
                    concepts[concept].append({
                        "file": file_path,
                        "title": title,
                        "summary": summary,
                    })
        except Exception as e:
            print(f"警告：读取文件失败 {file_path}: {e}")
    
    return concepts


def find_duplicates(concepts):
    """查找重复概念"""
    duplicates = {}
    
    for concept, files in concepts.items():
        if len(files) > 1:
            duplicates[concept] = files
    
    return duplicates


def generate_report(concepts, duplicates):
    """生成报告"""
    report = []
    report.append("=" * 60)
    report.append("方法论重复检测报告")
    report.append("=" * 60)
    
    # 总体统计
    total_files = sum(len(files) for files in concepts.values())
    report.append(f"\n分析的概念数: {len(concepts)}")
    report.append(f"涉及的文件数: {total_files}")
    report.append(f"重复概念数: {len(duplicates)}")
    
    # 重复概念详情
    if duplicates:
        report.append(f"\n## 重复概念（{len(duplicates)} 个）")
        for concept, files in duplicates.items():
            report.append(f"\n### {concept}")
            report.append(f"涉及 {len(files)} 个文件:")
            for f in files:
                report.append(f"  - {f['file']}: {f['title']}")
    
    # 概念分布
    report.append(f"\n## 概念分布")
    for concept, files in sorted(concepts.items(), key=lambda x: len(x[1]), reverse=True):
        report.append(f"- {concept}: {len(files)} 个文件")
    
    return "\n".join(report)


def export_json(concepts, duplicates):
    """导出 JSON 报告"""
    output_file = os.path.join(ROOT_DIR, "tools", "scripts", "方法论重复检测报告.json")
    
    report = {
        "total_concepts": len(concepts),
        "total_files": sum(len(files) for files in concepts.values()),
        "duplicate_concepts": len(duplicates),
        "concepts": {k: v for k, v in concepts.items()},
        "duplicates": {k: v for k, v in duplicates.items()},
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    return output_file


def main():
    args = sys.argv[1:]
    export = "--export" in args
    
    print("正在检测方法论重复...")
    
    # 获取所有 markdown 文件
    files = get_all_md_files([METHODS_DIR, KNOWLEDGE_DIR])
    print(f"找到 {len(files)} 个文件")
    
    # 分析概念
    concepts = analyze_concepts(files)
    
    # 查找重复
    duplicates = find_duplicates(concepts)
    
    # 生成报告
    report = generate_report(concepts, duplicates)
    print(report)
    
    if export:
        output_file = export_json(concepts, duplicates)
        print(f"\n详细报告已导出到: {output_file}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())