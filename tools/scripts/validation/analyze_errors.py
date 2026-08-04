#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析链接检查错误类型
"""

import os
import re
import json

# 读取 JSON 报告
with open(r'e:\个人知识库\tools\scripts\validation\_link_report.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

# 分析错误类型
error_types = {}
for error in report['zones']['core']['errors']:
    # 提取错误类型
    match = re.match(r'\[(\d+)\]', error)
    if match:
        error_type = match.group(1)
        error_types[error_type] = error_types.get(error_type, 0) + 1

print("错误类型统计：")
for error_type, count in sorted(error_types.items(), key=lambda x: x[1], reverse=True):
    print(f"  [{error_type}]: {count} 个")

print(f"\n总计 ERROR: {report['summary']['total_errors']}")
print(f"总计 WARN: {report['summary']['total_warns']}")

# 显示前 20 个错误示例
print("\n前 20 个错误示例：")
for i, error in enumerate(report['zones']['core']['errors'][:20]):
    print(f"  {i+1}. {error}")
