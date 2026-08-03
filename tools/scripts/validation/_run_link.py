import subprocess
base = r'E:/个人知识库/小说'
py = r'C:/Users/wsj/.workbuddy/binaries/python/versions/3.13.12/python.exe'
r = subprocess.run([py, r'通用小说创作流程/工具/链接体检与修复.py'], cwd=base, capture_output=True, text=True, encoding='utf-8')
out = (r.stdout or '') + (r.stderr or '')
open(base + r'/维护/_link_report.txt', 'w', encoding='utf-8').write(out)
print('exit', r.returncode, 'chars', len(out))
