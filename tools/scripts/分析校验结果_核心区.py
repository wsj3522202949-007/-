#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""分析校验结果分布（核心区）"""

import json
import subprocess
from collections import Counter

import sys
# Windows GBK 终端安全：避免 emoji/中文输出 UnicodeEncodeError
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass


result = subprocess.run(
    [r'python', r'e:\个人知识库\tools\scripts\maintenance\提交前校验.py', '--core-only', '--json'],
    capture_output=True,
    text=True,
    encoding='utf-8'
)

output = result.stdout

# 查找JSON开始位置
json_start = output.find('{')
if json_start == -1:
    print("未找到JSON输出")
    print("原始输出：")
    print(output[:2000])
    exit(1)

json_str = output[json_start:]
data = json.loads(json_str)
errors = data.get('errors', [])
warns = data.get('warns', [])

print("=" * 60)
print("📊 校验结果分析（核心区）")
print("=" * 60)
print()

print("【错误类型分布】")
error_types = Counter(e.get('type', 'UNKNOWN') for e in errors)
for t, c in error_types.most_common():
    print(f"  {t}: {c}")
print(f"\n总错误数: {len(errors)}")

print()
print("【警告类型分布】")
warn_types = Counter(w.get('type', 'UNKNOWN') for w in warns)
for t, c in warn_types.most_common():
    print(f"  {t}: {c}")
print(f"\n总警告数: {len(warns)}")

print()
print("【错误最多的前10个文件】")
file_errors = Counter(e.get('file', 'UNKNOWN') for e in errors)
for f, c in file_errors.most_common(10):
    print(f"  {c:4d} {f}")

print()
print("【警告最多的前10个文件】")
file_warns = Counter(w.get('file', 'UNKNOWN') for w in warns)
for f, c in file_warns.most_common(10):
    print(f"  {c:4d} {f}")

print()
print("=" * 60)
