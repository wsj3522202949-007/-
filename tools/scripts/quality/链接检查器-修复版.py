#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
链接检查器-修复版
==================
本次修复内容：

1. 修正 JSON 输出错误
   - 原版 safe_json_output(data, errors, warnings) 定义 3 个参数，却被以
     safe_json_output(errors, warnings) 调用（少 1 个参数）→ 必崩。
   - 现统一为 json.dump(result, fh) 写文件 / json.dumps(result) 写 stdout，
     全程异常安全，任何情况下都输出合法 JSON，绝不崩溃。

2. 排除目录（完全不扫描）
   - .tools/、archive/、references/原始来源包/（以路径组件匹配）

3. 单独识别以下链接类型（计入统计、不计入错误）
   - 模板占位符：含 <...> / {{...}} / <<...>> 或「中文链接」式命名
   - 目录链接：以 / 结尾，或 目录 / TOC / toc
   - Obsidian 动作链接：obsidian:// 或 app:// 协议链接
   （另含 示例 / 外部 / 锚点 链接，同样不计入错误）

4. 输出两份结果
   - core_errors        ：严格区断链，必须为 0
   - external_warnings  ：外部区断链，仅供参考

5. 范围划分不再由本文件自定义
   历史上本文件与 run_all.py 各写了一份 CORE_DIRS（都只有
   schema/methods/knowledge/projects），导致 README/CLAUDE/ai//goals//
   maintenance//tools 导航层的断链被降级成 external_warnings，门禁因此
   报「总体通过」——假绿灯。现统一从 tools/scripts/gate_scope.py 引入，
   本文件不得再自行定义范围。

用法
----
    python 链接检查器-修复版.py
    python 链接检查器-修复版.py --json
    python 链接检查器-修复版.py --json-file=report.json
    python 链接检查器-修复版.py --root <路径>

退出码：核心区无错误 → 0；核心区有错误 → 1（外部 warnings 不阻断）。
"""

import os
import re
import sys
import json
import traceback
import importlib.util
from datetime import datetime


# ---------------------------------------------------------------------------
# 范围定义：唯一权威来源 tools/scripts/gate_scope.py
# 禁止在本文件重复定义 CORE_DIRS —— 历史上就是因为这里和 run_all.py 各写一份
# （都只有 schema/methods/knowledge/projects），才让 README/CLAUDE/ai//goals//
# maintenance//tools 导航层的断链被降级成 external_warnings，产生假绿灯。
# ---------------------------------------------------------------------------
def _load_gate_scope():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.normpath(os.path.join(here, "..", "gate_scope.py"))
    if not os.path.isfile(path):
        raise RuntimeError(
            f"缺少范围定义模块 gate_scope.py（期望位置: {path}）。"
            "门禁范围必须由该模块统一定义，不提供局部回退，以免再次出现假绿灯。")
    spec = importlib.util.spec_from_file_location("gate_scope", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


scope = _load_gate_scope()
is_core = scope.is_strict            # 严格区判定（沿用旧函数名，语义已扩大）
should_skip_dir = scope.should_skip_dir

WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')
MD_LINK_RE = re.compile(r'(?<!\!)\[([^\]]*)\]\((?!https?://|mailto:|ftp://)([^)]+)\)')

PLACEHOLDER_RE = re.compile(r'(<\s*[^<>]+\s*>|{{[^}]+}}|<<[^>]+>>)')
# 待填/待补充类占位词（常见于索引骨架）
PLACEHOLDER_KW_RE = re.compile(r'(待补充|待定|待完善|待填|待写|待补|占位|占位符|TBD|TODO|XXX|见下文|详见|略)')
# 元变量占位符：模板文件里代表「以后填进去」的形式参数，而非真实文件名。
#   YYYY-01.md（goals/*/TEMPLATE.md）· 第NNN章-标题.md（命名契约示例）
#   projects/书名/...（文档里的示意路径）· [文本](路径.md)（格式演示）
# 注意：这是「链接分类」的修正，不是范围豁免——它不会让任何目录逃出严格区，
# 只是不再把形式参数当成真实文件去解析。
METAVAR_RE = re.compile(
    r'(?:^|[/\-_])(?:YYYY|MM-DD|NNN|书名|路径|文本|标题|你的书名|某某)(?:$|[/\-_.])')
OBSIDIAN_RE = re.compile(r'^(obsidian|app)://')
EXTERNAL_RE = re.compile(r'(github|gitlab|bitbucket)\.com', re.I)
EXAMPLE_KW_RE = re.compile(r'(示例|example|placeholder|测试|test)', re.I)
CHINESE_LINK_RE = re.compile(r'^[一-鿿]+链接$')
# 仅由 . 与 / 组成的相对目录路径（如 . / .. / ../..），指向目录而非文件
DOTPATH_RE = re.compile(r'^(\.\.?/?)+$')

# 单独识别的类型（计入 recognized，不计入错误）
RECOGNIZED = ("placeholder", "directory", "obsidian", "example", "external", "anchor")


def classify_link(target):
    """分类链接类型；返回 'real' 时才需要解析文件存在性。"""
    t = (target or "").strip()
    if not t or t == "#":
        return "empty"
    if OBSIDIAN_RE.match(t):
        return "obsidian"        # Obsidian 动作/协议链接
    if t.startswith(("http://", "https://", "mailto:", "ftp://")):
        return "external"
    if t.startswith("#"):
        return "anchor"
    if PLACEHOLDER_RE.search(t):
        return "placeholder"     # 模板占位符 <...> / {{...}} / <<...>>
    if PLACEHOLDER_KW_RE.search(t):
        return "placeholder"     # 待补充 / 占位 / TBD / 详见 … 等待填标记
    if METAVAR_RE.search(t):
        return "placeholder"     # 元变量：YYYY / NNN / 书名 / 路径 / 文本
    if EXAMPLE_KW_RE.search(t):
        return "example"
    if EXTERNAL_RE.search(t):
        return "external"
    if CHINESE_LINK_RE.match(t):
        return "placeholder"     # 如「中文链接」「项目链接」
    if DOTPATH_RE.match(t):
        return "directory"       # 仅由 . 与 / 组成的相对目录路径（如 ../..）
    if t.endswith("/") or t in ("目录", "TOC", "toc", "index"):
        return "directory"       # 目录链接
    return "real"


def resolve(root, filedir, target):
    """解析相对/绝对链接目标是否存在对应文件。"""
    target = target.split("#")[0].split("^")[0].strip()
    if not target:
        return False
    base = target[:-3] if target.endswith(".md") else target
    cands = [
        os.path.normpath(os.path.join(filedir, base)),
        os.path.normpath(os.path.join(filedir, base + ".md")),
        os.path.normpath(os.path.join(root, base)),
        os.path.normpath(os.path.join(root, base + ".md")),
    ]
    for c in cands:
        if os.path.isfile(c) or os.path.isfile(c + ".md"):
            return True
    return False


def strip_code(text):
    """去除 fenced / inline 代码块，避免代码里的字面 [[...]]/(...) 被当成链接。"""
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # 支持单反引号和双反引号（markdown 中 `` `code` `` 表示含单反引号的代码）
    text = re.sub(r'`+[^`]*?`+', '', text)
    return text


def find_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "schema")) or \
           os.path.isdir(os.path.join(d, "tools")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def safe_json(data):
    """异常安全的 JSON 序列化（兜底）。"""
    try:
        return json.dumps(data, ensure_ascii=False, indent=2)
    except Exception as e:  # noqa: BLE001
        return json.dumps({
            "success": False,
            "error": f"JSON 序列化失败: {e}",
            "core_errors": data.get("core_errors", []),
            "external_warnings": data.get("external_warnings", []),
        }, ensure_ascii=False, indent=2)


def run_link_check(root):
    """扫描全库链接，返回 严格区断链 / 外部区警告 / 识别统计。
    供统一门禁 run_all.py 直接导入调用，避免重复实现链接解析逻辑。

    返回字段中 core_errors 沿用旧键名，实际语义为「严格区断链」，
    范围由 gate_scope.is_strict 判定。"""
    core_errors = []
    external_warnings = []
    recognized = {k: 0 for k in RECOGNIZED}
    scanned = 0
    strict_files = 0
    external_files = 0

    for p, rel, zone in scope.iter_md_files(root):
        dp = os.path.dirname(p)
        try:
            with open(p, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        scanned += 1
        text = strip_code(text)
        core = (zone == "strict")
        if core:
            strict_files += 1
        else:
            external_files += 1

        # wikilinks
        for m in WIKILINK_RE.finditer(text):
            inner = m.group(1)
            tgt = inner.split("|", 1)[0].strip()
            lt = classify_link(tgt)
            if lt in recognized:
                recognized[lt] += 1
                continue
            if lt == "real" and not resolve(root, dp, tgt):
                msg = f"[wiki] 断链: {rel}  →  [[{inner}]]"
                (core_errors if core else external_warnings).append(msg)

        # markdown 链接（相对路径，非外链协议）
        for m in MD_LINK_RE.finditer(text):
            url = m.group(2).strip()
            lt = classify_link(url)
            if lt in recognized:
                recognized[lt] += 1
                continue
            if lt == "real" and not resolve(root, dp, url):
                msg = f"[md] 断链: {rel}  →  ({url})"
                (core_errors if core else external_warnings).append(msg)

    return {
        "core_errors": core_errors,
        "external_warnings": external_warnings,
        "recognized": recognized,
        "scanned": scanned,
        "strict_files": strict_files,
        "external_files": external_files,
    }


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    json_file = None
    root = None
    for a in args:
        if a.startswith("--json-file="):
            json_file = a.split("=", 1)[1]
            as_json = True
        elif a.startswith("--root="):
            root = a.split("=", 1)[1]

    if root is None:
        root = find_root()

    res = run_link_check(root)
    core_errors = res["core_errors"]
    external_warnings = res["external_warnings"]
    recognized = res["recognized"]
    scanned = res["scanned"]

    result = {
        "timestamp": datetime.now().isoformat(),
        "root": root,
        "summary": {
            "scanned_files": scanned,
            "core_errors": len(core_errors),
            "external_warnings": len(external_warnings),
            "core_pass": len(core_errors) == 0,
            "recognized": recognized,
        },
        "core_errors": core_errors,
        "external_warnings": external_warnings,
    }

    try:
        if as_json:
            js = safe_json(result)
            if json_file:
                try:
                    with open(json_file, "w", encoding="utf-8") as fh:
                        json.dump(result, fh, ensure_ascii=False, indent=2)
                        fh.write("\n")
                except Exception as e:  # noqa: BLE001
                    sys.stderr.write(f"[链接检查器] 写入 JSON 文件失败: {e}\n")
                    sys.stdout.write(js + "\n")
            else:
                sys.stdout.write(js + "\n")
        else:
            print("=" * 60)
            print(f"链接检查器-修复版 · 根: {root}")
            print("=" * 60)
            print(f"扫描文件数: {scanned}")
            print(f"单独识别 → 占位符:{recognized['placeholder']}  目录:{recognized['directory']}  "
                  f"Obsidian动作:{recognized['obsidian']}  示例:{recognized['example']}  "
                  f"外部:{recognized['external']}  锚点:{recognized['anchor']}")
            print("-" * 60)
            print(f"CORE_ERRORS（核心知识区，必须为 0）: {len(core_errors)}")
            for e in core_errors:
                print(f"  ❌ {e}")
            print(f"EXTERNAL_WARNINGS（外部资料，仅供参考）: {len(external_warnings)}")
            for w in external_warnings[:300]:
                print(f"  ⚠ {w}")
            if len(external_warnings) > 300:
                print(f"  … 其余 {len(external_warnings) - 300} 条已省略")
            print("=" * 60)
            verdict = "PASS ✅ 核心区无错误" if not core_errors else \
                f"FAIL ❌ 核心区有 {len(core_errors)} 处错误"
            print(f"结论: {verdict}")

        return 1 if core_errors else 0

    except Exception as e:  # noqa: BLE001
        sys.stderr.write(f"[链接检查器] 运行异常: {e}\n")
        traceback.print_exc()
        err_result = {
            "success": False,
            "timestamp": datetime.now().isoformat(),
            "error": str(e),
            "core_errors": core_errors,
            "external_warnings": external_warnings,
        }
        if as_json:
            sys.stdout.write(safe_json(err_result) + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
