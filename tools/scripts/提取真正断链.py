#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""提取核心区真正的断链（非示例性质）"""

import json
import subprocess

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
json_start = output.find('{')
json_str = output[json_start:]
data = json.loads(json_str)
errors = data.get('errors', [])

# 只保留 BROKEN_LINK
broken_links = [e for e in errors if e.get('type') == 'BROKEN_LINK']

# 排除明显的示例/示意链接
exclude_patterns = [
    'schema/aliases.md',  # 别名示例
    'schema/链接规范.md',  # 链接规范示例
    'schema/项目结构规范.md',  # 项目结构示例
]

real_broken_links = []
for link in broken_links:
    file_path = link.get('file', '')
    if any(file_path.endswith(p) for p in exclude_patterns):
        continue
    real_broken_links.append(link)

print(f"核心区总断链数: {len(broken_links)}")
print(f"示例性质断链数: {len(broken_links) - len(real_broken_links)}")
print(f"真正需要修复的断链数: {len(real_broken_links)}")
print()

print("=" * 80)
print("真正需要修复的断链清单：")
print("=" * 80)
for i, link in enumerate(real_broken_links, 1):
    print(f"\n{i}. 文件: {link['file']}")
    print(f"   问题: {link['message']}")
    
# 保存到文件
with open(r'e:\个人知识库\tools\scripts\真正断链清单.json', 'w', encoding='utf-8') as f:
    json.dump(real_broken_links, f, ensure_ascii=False, indent=2)
print(f"\n清单已保存到: tools/scripts/真正断链清单.json")
