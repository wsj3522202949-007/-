import os

base = r'E:/个人知识库/小说'

# 通用小说创作流程/ 下的文档：从 通用小说创作流程/ 到 archive/原始调研_online_research/ 的相对路径
rel = '../archive/原始调研_online_research/'
gcf_files = [
    '通用小说创作流程/INDEX.md',
    '通用小说创作流程/FRAMEWORK.md',
    '通用小说创作流程/QUICK_START.md',
    '通用小说创作流程/导览.md',
    '通用小说创作流程/最强写作方法论_全球最强综合版.md',
]

for f in gcf_files:
    p = os.path.join(base, f)
    if not os.path.exists(p):
        print('SKIP (missing)', f)
        continue
    t = open(p, encoding='utf-8').read()
    new = t
    new = new.replace('online_research/', rel)
    new = new.replace('online_research\\', rel)
    # 绝对路径那一行（最强写作方法论）
    new = new.replace(r'E:\小说\通用小说创作流程\online_research\\',
                      'E:/个人知识库/小说/archive/原始调研_online_research/')
    if new != t:
        open(p, 'w', encoding='utf-8').write(new)
        print('UPDATED', f)
    else:
        print('no-change', f)

# archive/导览.md：已在 archive/ 内，相对路径直接用子目录名
ap = os.path.join(base, 'archive/导览.md')
if os.path.exists(ap):
    t = open(ap, encoding='utf-8').read()
    new = t.replace('online_research/', '原始调研_online_research/')
    if new != t:
        open(ap, 'w', encoding='utf-8').write(new)
        print('UPDATED archive/导览.md')
    else:
        print('no-change archive/导览.md')
