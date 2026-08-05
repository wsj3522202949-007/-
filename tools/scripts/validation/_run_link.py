#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OBSOLETE: 此脚本仅适用于旧目录结构（E:\小说\通用小说创作流程/）。
当前知识库已迁移至 e:\个人知识库，原路径与文件均已不存在。
保留仅作历史参考，勿再执行。
"""
import subprocess
# 旧路径已废弃
base = r'E:/个人知识库/小说'
py = r'C:/Users/wsj/.workbuddy/binaries/python/versions/3.13.12/python.exe'
r = subprocess.run([py, r'通用小说创作流程/工具/链接体检与修复.py'], cwd=base, capture_output=True, text=True, encoding='utf-8')
out = (r.stdout or '') + (r.stderr or '')
open(base + r'/维护/_link_report.txt', 'w', encoding='utf-8').write(out)
print('exit', r.returncode, 'chars', len(out))
