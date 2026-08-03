import os, re

VAULT = r'E:/个人知识库'
# 修改 PROJECT_NAME 和 PROJ 来指定目标项目
PROJECT_NAME = ''  # TODO: 运行前手动设置目标项目名，如 '【你的书名】'
PROJ = os.path.join(VAULT, 'projects', PROJECT_NAME)
TOTAL = os.path.join(VAULT, 'README.md')
PROJREADME = os.path.join(PROJ, 'README.md')

def rel_link(target, d):
    return os.path.relpath(target, d).replace('\\', '/')

changed = []
for root, dirs, files in os.walk(PROJ):
    for fn in sorted(files):
        if not fn.endswith('.md'):
            continue
        path = os.path.join(root, fn)
        d = os.path.dirname(path)
        tot = rel_link(TOTAL, d).removesuffix('.md')
        proj = rel_link(PROJREADME, d).removesuffix('.md')
        nav_line = f'> ↩ 回总地图：[[{tot}|🗺️ 知识库总地图]] · 回项目：[[{proj}|《{PROJECT_NAME}》]]'
        txt = open(path, encoding='utf-8').read()
        m = re.search(r'^> ↩ 回总地图：.*$', txt, re.M)
        if m:
            line = m.group(0)
            parts = line.split(' · ')
            new_parts = []
            for p in parts:
                if p.startswith('↩ 回总地图：'):
                    new_parts.append('↩ 回总地图：[[%s|🗺️ 知识库总地图]]' % tot)
                elif p.startswith('回项目：'):
                    new_parts.append('回项目：[[%s|《%s》]]' % (proj, PROJECT_NAME))
                else:
                    new_parts.append(p)
            new_line = '> ' + ' · '.join(new_parts)
            if new_line != line:
                txt = txt[:m.start()] + new_line + txt[m.end():]
                open(path, 'w', encoding='utf-8').write(txt)
                changed.append(('fix', fn, tot))
        else:
            if txt.startswith('---'):
                idx = txt.find('\n---', 3)
                if idx != -1:
                    end = txt.find('\n', idx + 1)
                    txt = txt[:end+1] + '\n' + nav_line + '\n' + txt[end+1:]
                else:
                    txt = nav_line + '\n\n' + txt
            else:
                txt = nav_line + '\n\n' + txt
            open(path, 'w', encoding='utf-8').write(txt)
            changed.append(('add', fn, tot))

for act, fn, tot in changed:
    print(f'{act:3} {fn:28} 回总地图=[[{tot}|🗺️ 知识库总地图]]')
print('TOTAL changed:', len(changed))
