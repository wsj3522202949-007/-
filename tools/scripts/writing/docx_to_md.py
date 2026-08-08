#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
docx_to_md.py — 批量把 .docx 转成清洗后的 Markdown（小说正文入库用）

转换策略（两级）
  1) pandoc 优先（质量最好）：pandoc -s -t gfm --wrap=none in.docx -o out.md
  2) pandoc 未装 -> 回退 python-docx 解析（需 python-docx: pip install python-docx）

两条路径产出后都过同一套「清洗管线」，保证结果一致：
  ✂ 删页眉 / 页脚 / 页码（PAGE / NUMPAGES 域、第 N 页、独立页码行）
  ✂ 删分页符（\\newpage / \\pagebreak / \\x0c / 段落级分页）
  ✂ 合并软回车（w:br 非 page）-> 同一段内用空格连接
  ✂ 连续空行压成一行（>=3 个换行 -> 1 个空行）
  ✂ 统一标题格式（Heading N -> #...#；pandoc 已统一则保持；--smart-headings 可选启发式）

用法
  python docx_to_md.py <输入.docx | 目录> [-o 输出目录] [-r] [-f] [--smart-headings]
依赖
  pandoc（可选，优先） 或  python-docx（pip install python-docx）
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

# Windows GBK 终端安全：避免 emoji/中文输出 UnicodeEncodeError
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass


# ----------------------------------------------------------------------------
def log(msg):
    print(f"[docx_to_md] {msg}", file=sys.stderr)

def have_pandoc():
    return shutil.which("pandoc") is not None

# ----------------------------------------------------------------------------
# pandoc 路径
def convert_pandoc(src, dst):
    subprocess.run(
        ["pandoc", "-s", "-t", "gfm", "--wrap=none", src, "-o", dst],
        check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )

# ----------------------------------------------------------------------------
# python-docx 路径
def _paragraph_runs_xml(p):
    """按 XML 顺序拼出段落文本，处理好软/硬分页、tab、域。"""
    from docx.oxml.ns import qn
    out = []
    page_break = False
    for child in p._p.iter():
        tag = child.tag
        if tag == qn("w:t"):
            out.append(child.text or "")
        elif tag == qn("w:tab"):
            out.append("\t")
        elif tag == qn("w:br"):
            btype = child.get(qn("w:type"))
            if btype == "page":
                page_break = True
            else:
                out.append(" ")  # 软回车 -> 空格（合并进同段）
    return "".join(out), page_break

def _style_level(style):
    if style is None:
        return None
    name = style.name
    if name == "Title":
        return 1
    m = re.match(r"Heading\s+(\d+)", name)
    if m:
        return int(m.group(1))
    return None

def _max_font_size(p):
    sizes = []
    for r in p.runs:
        if r.font.size:
            sizes.append(r.font.size.pt)
    return max(sizes) if sizes else None

def _save_image(d, p, img_name, media_dir):
    try:
        from docx.oxml.ns import qn
        blips = p._p.findall(".//" + qn("a:blip"))
        for blip in blips:
            rId = blip.get(qn("r:embed"))
            if not rId:
                continue
            part = d.part.related_parts[rId]
            with open(os.path.join(media_dir, img_name), "wb") as f:
                f.write(part.blob)
            return
    except Exception as e:  # noqa: BLE001
        log(f"  图片提取失败: {e}")

def convert_docx(src, dst, smart_headings=False):
    try:
        import docx
        from docx.oxml.ns import qn
    except ImportError:
        sys.exit("ERROR: 回退路径需要 python-docx。请运行: python -m pip install python-docx")
    d = docx.Document(src)
    lines = []
    media_dir = os.path.join(os.path.dirname(dst), "media")
    os.makedirs(media_dir, exist_ok=True)
    img_idx = 0
    for p in d.paragraphs:
        text, page_break = _paragraph_runs_xml(p)
        # page_break 只作标记：分页符本身不输出任何字符，正文照常保留
        # 图片检测（尽力而为，按段落为单位插入）
        drawings = p._p.findall(".//" + qn("w:drawing"))
        if drawings:
            for _ in drawings:
                img_idx += 1
                img_name = f"image{img_idx:03d}.png"
                _save_image(d, p, img_name, media_dir)
                rel = os.path.relpath(
                    os.path.join(media_dir, img_name), os.path.dirname(dst)
                ).replace(os.sep, "/")
                lines.append(f"![]({rel})")
        level = _style_level(p.style)
        # 启发式标题（默认关闭，避免误伤）
        if level is None and smart_headings and text.strip():
            sz = _max_font_size(p)
            if sz and sz >= 22 and len(text.strip()) <= 40:
                level = 1
            elif sz and sz >= 16 and len(text.strip()) <= 40:
                level = 2
        if level is not None:
            lines.append(("#" * level) + " " + text.strip())
        else:
            lines.append(text)
    md = "\n".join(lines)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(md)
    if img_idx:
        log(f"  提取 {img_idx} 张图片 -> media/")

# ----------------------------------------------------------------------------
# 清洗管线（两条路径共用）
def clean_pipeline(md):
    # 1) 分页符残留
    md = md.replace("\x0c", "")
    md = re.sub(r"\\newpage", "", md)
    md = re.sub(r"\\pagebreak", "", md)
    md = re.sub(r"\n*\\newpage\n*", "\n", md)
    # 2) 页码 / 页眉页脚残留文本
    md = re.sub(r"第\s*[0-9]+\s*页", "", md)            # 第 12 页
    md = re.sub(r"-\s*[0-9]+\s*-", "", md)              # - 12 -
    md = re.sub(r"\bPAGE\b", "", md, flags=re.I)        # PAGE 域
    md = re.sub(r"\bNUMPAGES?\b", "", md, flags=re.I)   # NUMPAGES
    # 3) 行尾空白
    md = re.sub(r"[ \t]+\n", "\n", md)
    # 4) 连续空行压成一行（>=3 换行 -> 2 换行 = 一个空行）
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"

# ----------------------------------------------------------------------------
def one_file(src, base_root, out_dir, force, smart_headings):
    if not src.lower().endswith(".docx") or src.lower().endswith(".docm"):
        return
    if os.path.basename(src).startswith("~$"):
        return
    if out_dir:
        if base_root:
            rel = os.path.relpath(src, base_root)
        else:
            rel = os.path.basename(src)
        relmd = os.path.splitext(rel)[0] + ".md"
        dst = os.path.join(out_dir, relmd)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
    else:
        dst = os.path.splitext(src)[0] + ".md"
    if os.path.exists(dst) and not force:
        log(f"跳过(已存在, -f 覆盖): {dst}")
        return
    log(f"转换: {src}")
    if have_pandoc():
        convert_pandoc(src, dst)
    else:
        convert_docx(src, dst, smart_headings)
    md = open(dst, encoding="utf-8").read()
    md = clean_pipeline(md)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(md)
    log(f"完成: {dst}")

def main():
    ap = argparse.ArgumentParser(description="docx -> 清洗后 Markdown 批量转换")
    ap.add_argument("path", help=".docx 文件或目录")
    ap.add_argument("-o", "--out", default=None, help="输出目录（默认与源同目录）")
    ap.add_argument("-r", "--recursive", action="store_true", help="递归处理目录")
    ap.add_argument("-f", "--force", action="store_true", help="覆盖已存在输出")
    ap.add_argument("--smart-headings", action="store_true",
                    help="启发式把大字号短段落当标题（默认关）")
    args = ap.parse_args()

    if have_pandoc():
        log("检测到 pandoc，优先使用 pandoc 路径")
    else:
        log("未检测到 pandoc，使用 python-docx 回退路径（需 python-docx）")

    if os.path.isfile(args.path):
        one_file(args.path, None, args.out, args.force, args.smart_headings)
    elif os.path.isdir(args.path):
        srcs = []
        if args.recursive:
            for root, _, fs in os.walk(args.path):
                for fn in fs:
                    if fn.lower().endswith(".docx") and not fn.startswith("~$"):
                        srcs.append(os.path.join(root, fn))
        else:
            for fn in os.listdir(args.path):
                if fn.lower().endswith(".docx") and not fn.startswith("~$"):
                    srcs.append(os.path.join(args.path, fn))
        if not srcs:
            log(f"目录内无 .docx 文件: {args.path}")
            return
        for s in sorted(srcs):
            one_file(s, args.path, args.out, args.force, args.smart_headings)
    else:
        sys.exit(f"ERROR: 路径不存在: {args.path}")

if __name__ == "__main__":
    main()
