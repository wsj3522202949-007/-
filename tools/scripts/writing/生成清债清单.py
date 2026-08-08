#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
生成清债清单.py —— 把门禁 ERROR 转成逐章逐段可执行的清债清单
================================================================

背景
----
run_all.py 门禁现在如实报告正文质量债（跨章重复 / 模板句 / 硬短章等），
但报的是「全局统计」（如"精确重复段落 81 个"），作者不知道**具体该改
哪一章的哪一段**。本脚本把统计还原成逐章逐段的任务清单：

  · 每章：需要重写的重复段落（含**文件行号**、重复次数、涉及章节）
  · 硬短章 / 硬超章：直接列出当前字数与硬区间
  · 近似重复对：列出两侧段落预览与相似度
  · 模板句 / 重复短语：列出该章命中的句子

用法
----
  python 生成清债清单.py                    # 扫描全部 projects/*/chapters
  python 生成清债清单.py --root <仓库根>
  python 生成清债清单.py --out <输出路径>   # 默认 tools/reports/正文质量清债清单.html

输出
----
  HTML 清单（浅色主题，可按章 / 按项目浏览）+ 同名 .json（供后续流程机器读取）。
  本脚本只读，不修改任何章节正文。
"""

import os
import re
import sys
import json
import argparse
import importlib.util
from datetime import datetime

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

_HERE = os.path.dirname(os.path.abspath(__file__))
_SC_PATH = os.path.join(_HERE, "chapter_selfcheck.py")
_spec = importlib.util.spec_from_file_location("chapter_selfcheck", _SC_PATH)
_cs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cs)

_FRONT = re.compile(r'^---\r?\n.*?\r?\n---\r?\n', re.DOTALL)
_SENT = re.compile(r'(?<=[。！？…])')


def find_root():
    d = _HERE
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "schema")) or \
           os.path.isdir(os.path.join(d, "projects")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(_HERE)


def find_chapter_dirs(root):
    """projects/*/{chapters,正文} 且含章节 .md 的目录。"""
    out = []
    proj = os.path.join(root, "projects")
    if os.path.isdir(proj):
        for dp, _dn, fn in os.walk(proj):
            if os.path.basename(dp) in ("chapters", "正文"):
                if [f for f in fn if f.endswith(".md") and f != "README.md"]:
                    out.append(dp)
    return sorted(out)


def locate_norm_para_lines(path, target_norm):
    """在原始文件（含 frontmatter）中定位 norm 后等于 target_norm 的段落起始行号。"""
    with open(path, "rb") as f:
        raw = f.read().decode("utf-8", errors="replace")
    hits = []
    start = 0
    for m in re.finditer(r'\n[ \t]*\n', raw):
        seg = raw[start:m.start()]
        if _cs._norm(seg) == target_norm:
            hits.append(raw[:start].count("\n") + 1)
        start = m.end()
    seg = raw[start:]
    if _cs._norm(seg) == target_norm:
        hits.append(raw[:start].count("\n") + 1)
    return hits


def locate_seq_lines(path, seq_norm, window=3):
    """定位连续 window 段归一拼接等于 seq_norm 的序列起始行号。"""
    with open(path, "rb") as f:
        raw = f.read().decode("utf-8", errors="replace")
    segs = []  # (norm, start_line)
    start = 0
    for m in re.finditer(r'\n[ \t]*\n', raw):
        seg = raw[start:m.start()]
        segs.append((_cs._norm(seg), raw[:start].count("\n") + 1))
        start = m.end()
    segs.append((_cs._norm(raw[start:]), raw[:start].count("\n") + 1))
    hits = []
    for i in range(0, max(1, len(segs) - window + 1)):
        joined = "".join(s[0] for s in segs[i:i + window])
        if joined == seq_norm:
            hits.append(segs[i][1])
    return hits


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def collect_debt(cdir):
    """收集一个章节目录的全部清债条目。

    返回 dict:
      project: 项目名
      chapters: [ {name, rel, path, chars, char_verdict, hard_short/long,
                   exact: [...], sequences: [...], phrases: [...],
                   near: [...], templates: [...]} ]
    """
    whitelist = _cs.load_oral_tic_whitelist(cdir)
    exact = _cs.find_exact_duplicate_paras(cdir)
    phrases = _cs.find_repeated_phrases(cdir, whitelist=whitelist)
    seqs = _cs.find_duplicate_sequences(cdir)
    near = _cs.find_near_duplicate_paras(cdir)
    tpl, tpl_hits = _cs.find_cross_chapter_template_sentences(cdir)
    policy = _cs.load_policy(cdir)

    chapters = []
    for fname in _cs._chapter_files(cdir):
        path = os.path.join(cdir, fname)
        r = _cs.check_chapter(path, policy=policy)
        cv = r["char_verdict"]
        # 该章参与的精确重复段落
        ch_exact = [d for d in exact if fname in d["chapters"]]
        for d in ch_exact:
            d["lines"] = locate_norm_para_lines(path, d["para"])
        # 该章参与的序列重复
        ch_seq = []
        for d in seqs:
            if fname in d["chapters"]:
                d2 = dict(d)
                d2["lines"] = locate_seq_lines(path, d["sequence"])
                ch_seq.append(d2)
        # 该章参与的重复短语
        ch_ph = [d for d in phrases if fname in d["chapters"]]
        # 涉及该章的近似重复对
        ch_near = []
        for d in near:
            if d["chapter_a"] == fname:
                side = "a"
            elif d["chapter_b"] == fname:
                side = "b"
            else:
                continue
            other = d["chapter_b"] if side == "a" else d["chapter_a"]
            para = d["para_a"] if side == "a" else d["para_b"]
            ch_near.append({
                "other": other,
                "similarity": d["similarity"],
                "para": para,
                "lines": locate_norm_para_lines(path, d["para_a"] if side == "a" else d["para_b"]),
            })
        # 该章命中的模板句
        ch_tpl = [t for t in tpl if fname in t["chapters"]]
        chapters.append({
            "name": fname,
            "path": os.path.relpath(path, os.path.dirname(cdir)),
            "chars": r["chars"],
            "char_verdict": cv,
            "hard_short": cv.startswith("严重不足"),
            "hard_long": cv.startswith("严重超标"),
            "ai_verdict": r["ai_verdict"],
            "hook_verdict": r["hook_verdict"],
            "exact": ch_exact,
            "sequences": ch_seq,
            "phrases": ch_ph,
            "near": ch_near,
            "templates": ch_tpl,
        })

    chapters.sort(key=lambda c: (
        -(len(c["exact"]) + len(c["sequences"]) + len(c["phrases"])
          + len(c["near"]) + len(c["templates"])),
        c["name"]))
    return {
        "project": os.path.basename(os.path.dirname(cdir)),
        "dir": os.path.relpath(cdir, os.path.dirname(os.path.dirname(cdir))),
        "chapters": chapters,
    }


# ---------------------------------------------------------------------------
# HTML 渲染（浅色主题，与 IDE light 一致）
# ---------------------------------------------------------------------------
_CSS = """
body { font-family: "Microsoft YaHei", "PingFang SC", sans-serif;
       background:#f7f8fa; color:#24292f; margin:0; padding:24px; }
.wrap { max-width:1080px; margin:0 auto; }
h1 { font-size:22px; border-bottom:3px solid #d0d7de; padding-bottom:10px; }
h2 { font-size:18px; margin-top:32px; color:#1f2328;
     border-left:4px solid #0969da; padding-left:10px; }
h3 { font-size:15px; margin:18px 0 8px; color:#1f2328; }
table { border-collapse:collapse; width:100%; margin:8px 0 20px;
        background:#fff; font-size:13px; }
th,td { border:1px solid #d8dee4; padding:6px 10px; text-align:left;
        vertical-align:top; }
th { background:#f0f3f6; font-weight:600; white-space:nowrap; }
.badge { display:inline-block; padding:1px 8px; border-radius:10px;
         font-size:12px; font-weight:600; }
.bad-red { background:#ffebe9; color:#cf222e; }
.bad-orange { background:#fff1e5; color:#bc4c00; }
.bad-green { background:#dafbe1; color:#1a7f37; }
.mono { font-family:Consolas,Menlo,monospace; font-size:12px; color:#57606a; }
.para { background:#f6f8fa; border-left:3px solid #cf222e; padding:6px 10px;
        margin:4px 0; font-size:13px; white-space:pre-wrap; word-break:break-all; }
.summary-box { background:#fff; border:1px solid #d8dee4; border-radius:8px;
        padding:14px 18px; margin:16px 0; }
.kpi { display:inline-block; margin-right:24px; }
.kpi b { font-size:22px; color:#cf222e; }
.foot { margin-top:40px; color:#57606a; font-size:12px; }
"""


def render_html(projects, gen_time):
    total_exact = sum(len(p["chapters"]) and sum(len(c["exact"]) for c in p["chapters"]) for p in projects)
    rows = []
    for p in projects:
        rows.append(f"<h2>{esc(p['project'])} <span class='mono'>({esc(p['dir'])})</span></h2>")
        rows.append(_render_project(p))
    html = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>正文质量清债清单 · {gen_time[:10]}</title>
<style>{_CSS}</style></head><body><div class="wrap">
<h1>正文质量清债清单</h1>
<div class="summary-box">
<span class="kpi">生成时间 <b style="color:#0969da">{esc(gen_time)}</b></span>
<span class="kpi">涉及项目 <b>{len(projects)}</b></span>
<span class="kpi">涉及章节 <b>{sum(len(p['chapters']) for p in projects)}</b></span>
<span class="kpi">完全重复段落 <b>{sum(sum(len(c['exact']) for c in p['chapters']) for p in projects)}</b></span>
</div>
<div style="font-size:13px;color:#57606a;margin-bottom:8px">
使用说明：每个章节按「需要重写的段落」列出，<b>行号为该段落起始行</b>；
改写目标是<b>逐章差异化</b>（换场景/换动作/换对白），不是删句凑数；
若某短语属人物设定口头禅，可加入 <code>chapter_oral_tic.txt</code> 豁免（每行一条，<code>#</code> 注释）。
改完一章跑一次 <code>python tools/scripts/writing/chapter_selfcheck.py 章节目录</code> 自检。
</div>
{''.join(rows)}
<div class="foot">由 生成清债清单.py 生成 · 只读工具，未修改任何正文</div>
</div></body></html>"""
    return html


def _render_project(p):
    rows = [f"<p>章节 {len(p['chapters'])} 篇，按需改量排序。</p>"]
    for c in p["chapters"]:
        flags = []
        if c["hard_short"]:
            flags.append(f"<span class='badge bad-red'>硬短章 {c['chars']} 字</span>")
        if c["hard_long"]:
            flags.append(f"<span class='badge bad-red'>硬超章 {c['chars']} 字</span>")
        if c["ai_verdict"] == "重度":
            flags.append(f"<span class='badge bad-red'>重度AI味</span>")
        n_exact = len(c["exact"]); n_seq = len(c["sequences"])
        n_ph = len(c["phrases"]); n_near = len(c["near"]); n_tpl = len(c["templates"])
        rows.append(
            f"<h3>{esc(c['name'])} <span class='mono'>{esc(c['path'])}</span>"
            + (" " + "".join(flags) if flags else "")
            + f" <span class='badge {'bad-red' if n_exact+n_seq+n_near+n_tpl else 'bad-green'}'>"
              f"重复 {n_exact}+序列 {n_seq}+短语 {n_ph}+近似 {n_near}+模板句 {n_tpl}</span></h3>")
        if c["hard_short"] or c["hard_long"]:
            rows.append(
                f"<p><b>字数 {c['char_verdict']}</b> —— 需扩写/精简至硬区间 "
                f"[{policy_min(c)}-{policy_max(c)}] 内。</p>")
        if c["exact"]:
            rows.append("<table><tr><th>行号</th><th>重复次数</th><th>重复章节</th><th>段落内容（需差异化重写）</th></tr>")
            for d in c["exact"]:
                rows.append(
                    f"<tr><td class='mono'>{', '.join(map(str, d['lines'])) or '?'}</td>"
                    f"<td>{d['count']}</td>"
                    f"<td>{', '.join(esc(x[:12]) for x in d['chapters'])}</td>"
                    f"<td><div class='para'>{esc(d['para'])}</div></td></tr>")
            rows.append("</table>")
        if c["sequences"]:
            rows.append("<table><tr><th>行号</th><th>重复章节</th><th>整套结尾/桥段序列（需差异化重写）</th></tr>")
            for d in c["sequences"]:
                rows.append(
                    f"<tr><td class='mono'>{', '.join(map(str, d['lines'])) or '?'}</td>"
                    f"<td>{', '.join(esc(x[:12]) for x in d['chapters'])}</td>"
                    f"<td><div class='para'>{esc(d['sequence'])}</div></td></tr>")
            rows.append("</table>")
        if c["near"]:
            rows.append("<table><tr><th>行号</th><th>相似度</th><th>近似另一章</th><th>本段内容（需差异化重写）</th></tr>")
            for d in c["near"]:
                rows.append(
                    f"<tr><td class='mono'>{', '.join(map(str, d['lines'])) or '?'}</td>"
                    f"<td>{d['similarity']}</td><td>{esc(d['other'][:16])}</td>"
                    f"<td><div class='para'>{esc(d['para'])}</div></td></tr>")
            rows.append("</table>")
        if c["phrases"]:
            rows.append(f"<p><b>重复短语 {len(c['phrases'])} 个</b>（句子级，≥12字/≥2章）</p>")
            rows.append("<table><tr><th>重复章节</th><th>短语（需至少保留一章，其余差异化改写）</th></tr>")
            for d in c["phrases"][:15]:
                rows.append(f"<tr><td>{', '.join(esc(x[:12]) for x in d['chapters'])}</td>"
                            f"<td><div class='para'>{esc(d['phrase'])}</div></td></tr>")
            rows.append("</table>")
        if c["templates"]:
            rows.append(f"<p><b>模板句 {len(c['templates'])} 个</b>（≥3章重复，该章参与其中）</p>")
            rows.append("<table><tr><th>出现章数</th><th>句子（该章出现，需差异化）</th></tr>")
            for t in c["templates"][:15]:
                rows.append(f"<tr><td>{t['count']}</td><td>{esc(t['sentence'])}</td></tr>")
            rows.append("</table>")
        if not (c["exact"] or c["sequences"] or c["phrases"] or c["near"] or c["templates"]
                or c["hard_short"] or c["hard_long"]):
            rows.append("<p style='color:#1a7f37'>✅ 无已知内容债。</p>")
    return "".join(rows)


def policy_min(c):
    return _cs.load_policy().get("hard_min", 2200)


def policy_max(c):
    return _cs.load_policy().get("hard_max", 4000)


def main():
    ap = argparse.ArgumentParser(description="生成正文质量清债清单")
    ap.add_argument("--root", default=None)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    root = os.path.abspath(args.root) if args.root else find_root()
    out = os.path.abspath(args.out) if args.out else \
        os.path.join(root, "tools", "reports", "正文质量清债清单.html")

    projects = []
    for cdir in find_chapter_dirs(root):
        projects.append(collect_debt(cdir))

    gen_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = render_html(projects, gen_time)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    with open(out[:-5] + ".json", "w", encoding="utf-8") as f:
        json.dump(projects, f, ensure_ascii=False, indent=2)
    print(f"清债清单已生成: {out}")
    print(f"JSON 数据:      {out[:-5]}.json")
    for p in projects:
        n = sum(len(c["exact"]) + len(c["sequences"]) + len(c["near"])
                + len(c["templates"]) for c in p["chapters"])
        print(f"  {p['project']}: 章节 {len(p['chapters'])} | 需改条目 {n}")


if __name__ == "__main__":
    main()
