#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
导航历史记录
============

记录用户的导航历史，提供快速访问常用入口的功能。

功能：
1. 记录最近访问的文档
2. 统计最常访问的入口
3. 生成导航热力图
4. 提供快速访问建议

用法
----
    python tools/scripts/导航历史.py              # 显示导航历史
    python tools/scripts/导航历史.py --stats       # 显示统计信息
    python tools/scripts/导航历史.py --clear       # 清除历史记录
    python tools/scripts/导航历史.py --export      # 导出历史记录
"""

import os
import sys
import json
import datetime
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
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))

# 历史记录文件
HISTORY_FILE = os.path.join(ROOT_DIR, "tools", "scripts", ".navigation_history.json")
MAX_HISTORY = 1000  # 最大历史记录数


def load_history():
    """加载导航历史"""
    if not os.path.exists(HISTORY_FILE):
        return []
    
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []


def save_history(history):
    """保存导航历史"""
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    
    # 只保留最近的 MAX_HISTORY 条记录
    history = history[-MAX_HISTORY:]
    
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def add_record(file_path, action="open"):
    """添加导航记录"""
    history = load_history()
    
    record = {
        "file": file_path,
        "action": action,
        "timestamp": datetime.datetime.now().isoformat(),
        "date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "hour": datetime.datetime.now().hour,
    }
    
    history.append(record)
    save_history(history)


def get_stats():
    """获取导航统计"""
    history = load_history()
    
    if not history:
        return {
            "total_visits": 0,
            "unique_files": 0,
            "top_files": [],
            "by_date": {},
            "by_hour": {},
            "by_action": {},
        }
    
    # 统计访问次数
    file_counter = Counter()
    date_counter = Counter()
    hour_counter = Counter()
    action_counter = Counter()
    
    for record in history:
        file_counter[record["file"]] += 1
        date_counter[record["date"]] += 1
        hour_counter[record["hour"]] += 1
        action_counter[record["action"]] += 1
    
    return {
        "total_visits": len(history),
        "unique_files": len(file_counter),
        "top_files": file_counter.most_common(20),
        "by_date": dict(date_counter.most_common(30)),
        "by_hour": dict(sorted(hour_counter.items())),
        "by_action": dict(action_counter),
    }


def get_recent_files(n=20):
    """获取最近访问的文件"""
    history = load_history()
    
    # 去重，保留最近的访问
    seen = set()
    recent = []
    for record in reversed(history):
        if record["file"] not in seen:
            seen.add(record["file"])
            recent.append(record["file"])
            if len(recent) >= n:
                break
    
    return recent


def get_frequent_files(n=20):
    """获取最常访问的文件"""
    stats = get_stats()
    return [f for f, _ in stats["top_files"][:n]]


def get_hotspots():
    """获取导航热点"""
    stats = get_stats()
    
    hotspots = {
        "entry": [],
        "methods": [],
        "tools": [],
        "projects": [],
        "knowledge": [],
    }
    
    for file_path, count in stats["top_files"]:
        if "README" in file_path or "入口" in file_path:
            hotspots["entry"].append((file_path, count))
        elif "methods/" in file_path:
            hotspots["methods"].append((file_path, count))
        elif "tools/" in file_path:
            hotspots["tools"].append((file_path, count))
        elif "projects/" in file_path:
            hotspots["projects"].append((file_path, count))
        elif "knowledge/" in file_path:
            hotspots["knowledge"].append((file_path, count))
    
    return hotspots


def clear_history():
    """清除历史记录"""
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        return True
    return False


def export_history(output_file=None):
    """导出历史记录"""
    if output_file is None:
        output_file = os.path.join(ROOT_DIR, "tools", "scripts", "navigation_history_export.json")
    
    history = load_history()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
    
    return output_file


def print_human_readable():
    """打印人类可读的报告"""
    stats = get_stats()
    recent = get_recent_files(10)
    hotspots = get_hotspots()
    
    print("=" * 60)
    print("导航历史报告")
    print("=" * 60)
    
    print(f"\n总访问次数: {stats['total_visits']}")
    print(f"独立文件数: {stats['unique_files']}")
    
    print("\n最近访问的文件（前10）:")
    for i, file_path in enumerate(recent, 1):
        print(f"  {i}. {file_path}")
    
    print("\n最常访问的文件（前10）:")
    for file_path, count in stats["top_files"][:10]:
        print(f"  {count}次 - {file_path}")
    
    print("\n导航热点:")
    for category, files in hotspots.items():
        if files:
            print(f"\n  {category}:")
            for file_path, count in files[:5]:
                print(f"    {count}次 - {file_path}")


def print_json():
    """打印 JSON 格式的报告"""
    stats = get_stats()
    recent = get_recent_files(20)
    hotspots = get_hotspots()
    
    output = {
        "stats": stats,
        "recent_files": recent,
        "hotspots": hotspots,
    }
    
    print(json.dumps(output, ensure_ascii=False, indent=2))


def main():
    args = sys.argv[1:]
    
    if "--stats" in args:
        print_json()
    elif "--clear" in args:
        if clear_history():
            print("历史记录已清除")
        else:
            print("没有历史记录需要清除")
    elif "--export" in args:
        output_file = export_history()
        print(f"历史记录已导出到: {output_file}")
    else:
        print_human_readable()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())