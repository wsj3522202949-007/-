import subprocess, json, re
base = r'E:/个人知识库/小说'
PY = r'C:/Users/wsj/.workbuddy/binaries/python/versions/3.13.12/python.exe'

r1 = subprocess.run([PY, '维护/校验脚本.py', '--json'], cwd=base, capture_output=True, text=True, encoding='utf-8')
try:
    j1 = json.loads(r1.stdout or '')
    e1, w1 = len(j1.get('errors', [])), len(j1.get('warns', []))
    v1 = 'PASS' if e1 == 0 else 'FAIL'
except Exception:
    e1, w1, v1 = -1, -1, 'PARSE_FAIL'

r2 = subprocess.run([PY, '通用小说创作流程/工具/链接体检与修复.py', '--fix'], cwd=base, capture_output=True, text=True, encoding='utf-8')
out2 = (r2.stdout or '') + (r2.stderr or '')
open(base + r'/维护/_link_clean.txt', 'w', encoding='utf-8').write(out2)
e2, w2, v2 = 0, 0, 'UNKNOWN'
for line in out2.splitlines():
    if '结论' in line:
        v2 = 'PASS' if 'PASS' in line else 'FAIL'
        m = re.search(r'WARN\(含未转义_\):\s*(\d+)', line)
        if m:
            w2 = int(m.group(1))
        break

print('GATE1 check | exit', r1.returncode, '| errors', e1, '| warns', w1, '| verdict', v1)
print('GATE2 link  | exit', r2.returncode, '| errors', e2, '| warns', w2, '| verdict', v2)
print('BOTH_GREEN' if (r1.returncode == 0 and e1 == 0 and r2.returncode == 0 and 'PASS' in v2) else 'NOT_GREEN')
