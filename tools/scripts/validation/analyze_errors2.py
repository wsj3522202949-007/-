#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析链接检查错误类型
"""

import os
import re
import json
import subprocess

# 运行链接检查脚本
result = subprocess.run(
    ['python', r'e:\个人知识库\tools\scripts\validation\_run_link_fixed.py', '--zone', 'core', '--json'],
    capture_output=True,
    text=True,
    encoding='utf-8',
    cwd=r'e:\个人知识库'
)

# 解析 JSON 输出
try:
    # 从输出中提取 JSON（可能在最后）
    output = result.stdout
    json_start = output.find('{')
    if json_start != -1:
        json_str = output[json_start:]
        report = json.loads(json_str)
        
        print("=" * 60)
        print("链接检查错误分析")
        print("=" * 60)
        
        # 分析错误类型
        error_types = {}
        for error in report['zones']['core']['errors']:
            match = re.match(r'\[(\d+)\]', error)
            if match:
                error_type = match.group(1)
                error_types[error_type] = error_types.get(error_type, 0) + 1
        
        print("\n错误类型统计：")
        for error_type, count in sorted(error_types.items(), key=lambda x: x[1], reverse=True):
            print(f"  [{error_type}]: {count} 个")
        
        print(f"\n总计 ERROR: {report['summary']['total_errors']}")
        print(f"总计 WARN: {report['summary']['total_warns']}")
        print(f"通过: {report['summary']['pass']}")
        
        # 显示前 20 个 ERROR 示例
        print("\n前 20 个 ERROR 示例：")
        for i, error in enumerate(report['zones']['core']['errors'][:20]):
            print(f"  {i+1}. {error}")
        
        # 显示前 10 个 WARN 示例
        print("\n前 10 个 WARN 示例：")
        for i, warn in enumerate(report['zones']['core']['warns'][:10]):
            print(f"  {i+1}. {warn}")
    else:
        print("未找到 JSON 输出")
        print("stdout:", output[:2000])
        print("stderr:", result.stderr[:2000])
except Exception as e:
    print(f"解析失败: {e}")
    print("stdout:", result.stdout[:2000])
    print("stderr:", result.stderr[:2000])
