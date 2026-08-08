#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ingest_chapters.py —— 正文入库流水线（配合 维护/校验脚本.py 的 [F] 强制 frontmatter）

把"清洗后的 Markdown 最终稿"变成符合本 vault 契约的正文章节：
  - 输入：单文件（多章合一）或目录（每章一文件）
  - 拆分：按章节标题（第NNN章 / Chapter N / 自定义）切成独立章
  - 命名：正文/第NNN章-标题.md（零填充 3 位，见 维护标准.md §1.5 ①）
  - 注入：每章强制 frontmatter（title/chapter/status/type:type/chapter/tags/pov）
  - 落库：写入 <project>/正文/

用法：
  python ingest_chapters.py <输入.md 或 输入目录> --project <projects/书名> [--pov 主角] [--status draft] [-f] [--dry-run]

依赖：仅标准库。建议配合 docx_to_md.py 先把 .docx 转成清洗后 Markdown，
      再把输出目录喂给本工具。
"""
import argparse
import os
import re
import sys

# Windows GBK 终端安全：避免 emoji/中文输出 UnicodeEncodeError
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass


# 章节标题识别：支持「第1章」「第001章」「第一章」「Chapter 3」及其带 # 的 markdown 标题
CHAPTER_RE = re.compile(
    r'^(?:\s{0,3}#{1,3}\s*)?'
    r'(?:第\s*(?P<cn>[〇零一二三四五六七八九十百千0-9]+)\s*章'
    r'|Chapter\s*(?P<en>[0-9]+))'
    r'[：:．.\s_-]*\s*(?P<title>.*?)\s*$',
    re.IGNORECASE,
)

CN_NUM = {
    '〇': 0, '零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5,
    '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, '百': 100, '千': 1000,
}


def cn_to_int(s):
    """把中文数字（含阿拉伯）转成整数。支持 1~9999 常见组合。"""
    s = s.strip()
    if s.isdigit():
        return int(s)
    if not s:
        return 0
    # 简单组合：处理 十/百/千 与个位的加法式与乘法式
    total, cur, prev_unit = 0, 0, 1
    for ch in s:
        if ch in CN_NUM:
            v = CN_NUM[ch]
            if v >= 10:  # 单位
                if v == 10 and cur == 0:
                    cur = 1
                prev_unit = v
                total += cur * v
                cur = 0
            else:
                cur = v
        else:
            # 含阿拉伯数字片段（如 1万2）不做复杂处理
            return None
    return total + cur


def sanitize_title(title):
    """把章节标题清洗成文件名安全片段。"""
    t = title.strip()
    # 去掉可能从标题行带出的 markdown 标记
    t = t.strip('#').strip()
    # 非法文件名字符
    for ch in ('\\', '/', ':', '*', '?', '"', '<', '>', '|'):
        t = t.replace(ch, '')
    t = t.strip().rstrip('.')
    # 限制长度，避免路径过长
    return t[:40] if t else '未命名'


def split_file(text):
    """把整篇 Markdown 按章节标题切成 [(chapter_no:int|None, title:str, body:str), ...]。"""
    lines = text.splitlines()
    chapters = []
    cur = None
    buf = []
    for ln in lines:
        m = CHAPTER_RE.match(ln)
        if m:
            # 落库上一章
            if cur is not None:
                chapters.append(cur)
            title = (m.group('title') or '').strip()
            if m.group('cn') is not None:
                no = cn_to_int(m.group('cn'))
            else:
                no = int(m.group('en'))
            cur = {'no': no, 'title': title, 'buf': []}
        else:
            if cur is None:
                # 章节前的 preamble（如书名/简介），归入第 0 章"前言/引子"
                if not chapters or chapters[0].get('no') != 0:
                    cur = {'no': 0, 'title': '引子', 'buf': []}
            if cur is not None:
                cur['buf'].append(ln)
    if cur is not None:
        chapters.append(cur)
    result = []
    for c in chapters:
        result.append((c['no'], c['title'], '\n'.join(c['buf']).strip('\n')))
    return result


def split_dir(d, files):
    """目录模式：每个 .md 文件即一章，按文件名或顺序编号。"""
    out = []
    order = 0
    for f in sorted(files):
        if not f.lower().endswith('.md') or f == 'README.md':
            continue
        order += 1
        base = f[:-3]
        m = re.match(r'第\s*0*(\d+)\s*章[_\-]?\s*(.*)', base)
        if m:
            no = int(m.group(1))
            title = sanitize_title(m.group(2) or '')
        else:
            no = order
            title = sanitize_title(base)
        with open(os.path.join(d, f), encoding='utf-8', errors='replace') as fh:
            body = fh.read().strip('\n')
        # 若文件内部已含 frontmatter，剥离（由本工具统一重写）
        if body.startswith('---'):
            body = re.sub(r'^---\n.*?\n---\n?', '', body, count=1, flags=re.DOTALL)
        out.append((no, title, body.strip('\n')))
    return out


def build_frontmatter(no, title, pov, status, tags):
    fm = ['---']
    fm.append(f'title: {title}')
    fm.append(f'chapter: {no}')
    fm.append(f'status: {status}')
    fm.append('type: type/chapter')
    fm.append(f'pov: {pov}')
    fm.append('tags: [' + ', '.join(tags) + ']')
    fm.append('---')
    return '\n'.join(fm)


def main():
    ap = argparse.ArgumentParser(description='正文入库：Markdown 最终稿 -> 正文/第NNN章-标题.md（带强制 frontmatter）')
    ap.add_argument('input', help='清洗后的 Markdown 文件，或每章一文件的目录')
    ap.add_argument('--project', required=True, help='目标项目目录，如 projects/你的书名')
    ap.add_argument('--pov', default='主角', help='默认叙事视角（写进 pov 键）')
    ap.add_argument('--status', default='wip', help='章节状态（须为 active/demo/wip/done 之一，默认 wip）')
    ap.add_argument('-f', '--force', action='store_true', help='覆盖已存在的同名章节文件')
    ap.add_argument('--dry-run', action='store_true', help='只预览，不写文件')
    args = ap.parse_args()

    # status 必须落在契约取值内（维护/校验脚本.py 的 STATUS_VALUES）
    VALID_STATUS = {'active', 'demo', 'wip', 'done'}
    if args.status not in VALID_STATUS:
        print(f'WARN: --status={args.status} 不在契约取值 {sorted(VALID_STATUS)}，回退为 wip', file=sys.stderr)
        args.status = 'wip'

    proj_root = os.path.abspath(args.project)
    body_dir = os.path.join(proj_root, '正文')
    if not os.path.isdir(proj_dir_check := body_dir):
        # 允许 --project 指向 projects/<书名> 即已含 正文/；若没有则创建
        if not os.path.isdir(proj_root):
            print(f'ERROR: 目标项目不存在: {proj_root}', file=sys.stderr)
            return 2
        os.makedirs(body_dir, exist_ok=True)

    # 解析输入
    if os.path.isdir(args.input):
        chapters = split_dir(args.input, os.listdir(args.input))
    elif os.path.isfile(args.input):
        with open(args.input, encoding='utf-8', errors='replace') as fh:
            chapters = split_file(fh.read())
    else:
        print(f'ERROR: 输入不存在: {args.input}', file=sys.stderr)
        return 2

    if not chapters:
        print('WARN: 未识别到任何章节，检查输入格式。', file=sys.stderr)
        return 1

    # 统一编号：引子(no=0) 单独成 引子.md；其余按原序号升序排为 001..NNN
    ordered = []
    for no, title, body in chapters:
        if no == 0:
            ordered.append(('第000章-引子.md', title or '引子', body))
    real = sorted(((no, t, b) for no, t, b in chapters if no and no > 0),
                  key=lambda x: x[0])
    for i, (no, title, body) in enumerate(real, start=1):
        safe = sanitize_title(title) if title else '未命名'
        ordered.append((f'第{i:03d}章-{safe}.md', title or '未命名', body))

    written = 0
    for fname, title, body in ordered:
        fpath = os.path.join(body_dir, fname)
        m = re.match(r'第(\d{3})章', fname)
        idx = int(m.group(1)) if m else 0
        tags = ['type/chapter', 'area/项目', f'status/{args.status}']
        fm = build_frontmatter(idx, title, args.pov, args.status, tags)
        content = f'{fm}\n\n{body}\n'
        if os.path.exists(fpath) and not args.force:
            print(f'SKIP (已存在, 用 -f 覆盖): {fpath}')
            continue
        if args.dry_run:
            print(f'[dry-run] 将写入 {fpath}\n{fm}\n  正文 {len(body)} 字\n')
            continue
        with open(fpath, 'w', encoding='utf-8') as fh:
            fh.write(content)
        written += 1
        print(f'OK -> {os.path.relpath(fpath, proj_root)}')

    print(f'\n完成：识别 {len(ordered)} 段，写入 {written} 个章节文件到 {body_dir}')
    if args.dry_run:
        print('（dry-run 模式，未写盘）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
