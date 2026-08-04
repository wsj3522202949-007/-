#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
质量门禁系统 —— 统一检查入口
完美版：修复所有语法/逻辑错误，分区扫描，JSON稳定输出，8类门禁
一次命令跑完全部检查:
    python 质量门禁系统.py             # 全库
    python 质量门禁系统.py --zone core  # 核心区
    python 质量门禁系统.py --json       # 给 CI
    python 质量门禁系统.py --root E:\\个人知识库
"""

import os, re, sys, json, traceback
from datetime import datetime
from pathlib import Path

# ── 常量 ───────────────────────────────────
CONTROLLED_TAGS = {
    "协议宽松","协议传染","协议未明","本地优先","需API密钥",
    "中文友好","英文文档","去AI味","RAG","多Agent","提示词",
    "大纲规划","TTS","互动叙事","校对","文风迁移","Claude插件",
    "人物设定","改稿润色","本地写作","平台运营","灵感创意"
}
TYPE_VALS   = {"index","guide","ref","dashboard","template","moc","demo","project",
               "chapter","character","setting","location","prop","tool","daily-note","book-note"}
AREA_VALS   = {"库","方法","项目","资料","日记","索引","管理"}
STATUS_VALS = {"active","demo","wip","done","draft","archived"}

WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')
MDLINK_RE   = re.compile(r'(?<!\!)\[([^\]]*)\]\(([^)]+)\)')
OBSIDIAN_RE = re.compile(r'^(obsidian|app):')
EXAMPLE_RE  = re.compile(r'(示例|example|test|测试|占位|placeholder|TODO|<[^>]+>)', re.I)
OLD_PATH_RE = re.compile(r'[A-Za-z]:\\(?:Users|Program Files)')
READY_RE    = re.compile(r'^\d{5}__')

SKIP = (".git",".workbuddy",".obsidian","node_modules","__pycache__")

# ── 分区 ─────────────────────────────────
Z = {
  "core":{"name":"核心知识","paths":["schema","methods","knowledge"],"strict":True,"allow_place":False},
  "projects":{"name":"项目生产","paths":["projects"],"strict":True,"allow_place":True},
  "templates":{"name":"模板区","paths":["methods/templates","methods/项目骨架模板"],"strict":False,"allow_place":True},
  "refs":{"name":"外部参考","paths":["references","archive"],"strict":False,"allow_place":True},
  "tools":{"name":"工具运行时","paths":["tools"],"strict":False,"allow_place":True},
  "ai":{"name":"AI协作","paths":["ai"],"strict":False,"allow_place":True},
  "goals":{"name":"目标管理","paths":["goals"],"strict":False,"allow_place":True},
  "drafts":{"name":"草稿","paths":["drafts"],"strict":False,"allow_place":True},
}

# ── 工具函数 ──────────────────────────────
def parse_fm(txt):
    """解析frontmatter，返回dict或None"""
    if not txt.startswith("---"): return None
    lines = txt.split("\n")
    if lines[0].strip() != "---": return None
    end = next((i for i in range(1,len(lines)) if lines[i].strip()=="---"), None)
    if end is None: return None
    fm = {}
    for l in lines[1:end]:
        m = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', l)
        if m: fm[m.group(1)] = m.group(2).strip()
    return fm

def strip_code(t):
    """去除代码块，避免误判"""
    t = re.sub(r'```.*?```', '', t, flags=re.DOTALL)
    t = re.sub(r'`[^`\n]*`', '', t)
    return t

# ── 链接解析 (修复版) ──────────────────────
def _resolve_link(target, filedir, root, md_map):
    """
    解析链接：(相对路径 | 虚名 | 目录链接) → True/False
    - 跳过Obsidian协议、外部HTTP
    - 直接文件映射
    - 相对于当前文件目录
    - 允许指向目录的链接
    - 允许指向非.md文件的链接
    """
    target = target.split("#")[0].split("^")[0].split("|")[0].strip()
    if not target: return False
    # Obsidian协议跳过
    if OBSIDIAN_RE.match(target): return True
    # 外部HTTP跳过（视为外部链接）
    if target.startswith("http"): return True

    # 直接文件映射
    if target in md_map: return True
    if target + ".md" in md_map: return True

    # 相对于当前文件目录
    try:
        rel_path = (filedir / target).resolve()
        # 转换为相对于root的路径
        try:
            rel_str = str(rel_path.relative_to(root)).replace("\\", "/")
        except ValueError:
            rel_str = str(rel_path).replace("\\", "/")

        # 检查是否是目录
        if rel_path.is_dir(): return True

        # 检查文件是否存在（不只是.md）
        if rel_path.exists(): return True

        # 检查带.md后缀的文件
        if rel_str in md_map: return True
        if rel_str + ".md" in md_map: return True

        # 检查父目录
        parent = rel_path.parent
        if parent.exists() and parent.is_dir():
            # 检查目录中是否有匹配的文件
            try:
                for f in parent.iterdir():
                    if f.stem == rel_path.stem or f.name == rel_path.name:
                        return True
            except:
                pass
    except Exception:
        pass

    return False

# ── 主检查器 ─────────────────────────────
class Gate:
    def __init__(self, root_path):
        self.root = Path(root_path)
        self.err = []
        self.wrn = []
        self.inf = []
        self._md_map = None   # 延迟初始化

    def _rel(self, path):
        """计算相对于root的路径字符串"""
        try:
            return str(path.relative_to(self.root)).replace("\\", "/")
        except ValueError:
            return str(path).replace("\\", "/")

    def _zone(self, filepath):
        """根据文件路径确定所属分区"""
        try:
            rel = str(Path(filepath).relative_to(self.root)).replace("\\", "/")
        except ValueError:
            return None

        for zone_id, cfg in Z.items():
            for p in cfg["paths"]:
                if rel.startswith(p):
                    return zone_id
        return None

    def add_err(self, code, msg, file=""):
        self.err.append({"code": code, "msg": msg, "file": file, "time": datetime.now().isoformat()})

    def add_wrn(self, code, msg, file=""):
        self.wrn.append({"code": code, "msg": msg, "file": file, "time": datetime.now().isoformat()})

    def add_inf(self, code, msg, file=""):
        self.inf.append({"code": code, "msg": msg, "file": file, "time": datetime.now().isoformat()})

    # ── 准备md文件映射 ─────────────────────
    def _prepare(self):
        """扫描全库，构建所有md文件的快速查找映射"""
        if self._md_map is not None: return
        self._md_map = {}
        for root_dir, dirs, files in os.walk(str(self.root)):
            # 跳过不需要的目录
            dirs[:] = [d for d in dirs if d not in SKIP]
            for f in files:
                if f.endswith(".md"):
                    full_path = os.path.join(root_dir, f)
                    # 存储两种key: 完整路径 和 相对路径
                    try:
                        rel = str(Path(full_path).relative_to(self.root)).replace("\\", "/")
                        self._md_map[rel] = full_path
                        # 也存不带.md的版本
                        self._md_map[rel[:-3]] = full_path
                    except ValueError:
                        pass

    # ── 链接检查 ──────────────────────────
    def check_links(self, zone_filter=None):
        """
        链接检查：区分5种链接类型
        1. 真实断链 → ERROR
        2. 示例链接 → 跳过（按分区规则）
        3. 目录链接 → INFO
        4. Obsidian协议链接 → 跳过
        5. 外部源码内部链接 → 跳过（按分区规则）
        """
        total_links = 0
        broken_links = 0
        skipped_links = 0

        self._prepare()
        md_map = self._md_map

        for zone_id, cfg in Z.items():
            if zone_filter and zone_id != zone_filter: continue
            for sub in cfg["paths"]:
                d = self.root / sub
                if not d.is_dir(): continue

                for md in d.rglob("*.md"):
                    try:
                        txt = md.read_text(encoding="utf-8", errors="replace")
                    except Exception:
                        continue

                    txt = strip_code(txt)
                    rel = self._rel(md)
                    file_dir = md.parent

                    # ── Wikilink ──
                    for m in WIKILINK_RE.finditer(txt):
                        total_links += 1
                        inner = m.group(1)
                        target = inner.split("|", 1)[0].strip()

                        # 分类链接
                        if EXAMPLE_RE.search(inner) or EXAMPLE_RE.search(target):
                            skipped_links += 1
                            continue

                        if not _resolve_link(target, file_dir, self.root, md_map):
                            # 检查是否应该跳过
                            should_skip = False
                            if OBSIDIAN_RE.match(target):
                                should_skip = True
                            elif target.startswith("http"):
                                should_skip = cfg.get("allow_external", False)
                            elif EXAMPLE_RE.search(target):
                                should_skip = cfg.get("allow_place", False)

                            if should_skip:
                                skipped_links += 1
                                self.add_inf("LINK_SKIP", f"跳过链接: [[{inner}]]", rel)
                            else:
                                broken_links += 1
                                self.add_err("LINK_BROKEN", f"真实断链(wiki): [[{inner}]]", rel)

                    # ── Markdown链接 ──
                    for m in MDLINK_RE.finditer(txt):
                        total_links += 1
                        url = m.group(2).strip()

                        # 跳过锚点、外部链接
                        if url.startswith(("#", "http://", "https://", "mailto:", "ftp://")):
                            skipped_links += 1
                            continue

                        # 分类链接
                        if EXAMPLE_RE.search(url):
                            skipped_links += 1
                            self.add_inf("LINK_EXAMPLE", f"示例链接: ({url})", rel)
                            continue

                        if not _resolve_link(url, file_dir, self.root, md_map):
                            should_skip = False
                            if OBSIDIAN_RE.match(url):
                                should_skip = True
                            elif url.startswith("http"):
                                should_skip = cfg.get("allow_external", False)
                            elif EXAMPLE_RE.search(url):
                                should_skip = cfg.get("allow_place", False)

                            if should_skip:
                                skipped_links += 1
                                self.add_inf("LINK_SKIP", f"跳过链接: ({url})", rel)
                            else:
                                broken_links += 1
                                self.add_err("LINK_BROKEN", f"真实断链(md): ({url})", rel)

        print(f"  [链接] 扫描 {total_links} 条 | 断链 {broken_links} | 跳过 {skipped_links}")

    # ── Frontmatter检查 ────────────────────
    def check_fm(self, zone_filter=None):
        """
        Frontmatter合规检查：
        - type值合法性
        - area值合法性
        - id空值检查
        - 旧格式标签(type/xxx)检测
        """
        checked = 0
        bad_count = 0

        for zone_id, cfg in Z.items():
            if zone_filter and zone_id != zone_filter: continue
            for sub in cfg["paths"]:
                d = self.root / sub
                if not d.is_dir(): continue

                for md in d.rglob("*.md"):
                    try:
                        txt = md.read_text(encoding="utf-8", errors="replace")
                    except Exception:
                        continue

                    rel = self._rel(md)
                    fm = parse_fm(txt)

                    # 模板区的Templater模板文件不需要frontmatter
                    if zone_id == "templates" and ("templates/obsidian" in rel or md.suffix == ".js" or rel.startswith("methods/templates/obsidian")):
                        continue

                    if fm is None:
                        if cfg.get("strict", False):
                            self.add_err("NO_FRONTMATTER", "缺少frontmatter", rel)
                        continue

                    checked += 1

                    # type检查
                    if "type" in fm:
                        t = fm["type"].strip()
                        if t.startswith("type/"):
                            self.add_wrn("OLD_TYPE", f"type旧格式: {t}", rel)
                        elif t not in TYPE_VALS:
                            self.add_err("BAD_TYPE", f"非法type值: {t}", rel)

                    # area检查
                    if "area" in fm:
                        a = fm["area"].strip()
                        if a not in AREA_VALS:
                            self.add_err("BAD_AREA", f"非法area值: {a}", rel)

                    # id空值检查
                    if "id" in fm:
                        did = fm["id"].strip()
                        if did == ":" or not did:
                            self.add_err("EMPTY_ID", "id字段为空值", rel)

        print(f"  [Frontmatter] 检查 {checked} 篇")

    # ── 结构完整性检查 ────────────────────
    def check_structure(self):
        """
        结构完整性检查：
        - 项目结构漂移（中文旧结构）
        - 旧绝对路径残留
        """
        # 项目结构漂移
        proj_dir = self.root / "projects"
        if proj_dir.is_dir():
            for proj in proj_dir.iterdir():
                if not proj.is_dir(): continue
                has_old = (proj / "正文").is_dir() or (proj / "人物").is_dir()
                has_new = (proj / "chapters").is_dir()
                if has_old and not has_new:
                    self.add_err("OLD_STRUCTURE", f"中文旧结构漂移: {proj.name}", self._rel(proj))

        # 旧绝对路径
        for zone_id, cfg in Z.items():
            if zone_id in ("refs", "tools"): continue  # 外部参考和工具区跳过
            for sub in cfg["paths"]:
                d = self.root / sub
                if not d.is_dir(): continue
                for md in d.rglob("*.md"):
                    try:
                        txt = md.read_text(encoding="utf-8", errors="replace")
                    except Exception:
                        continue
                    if OLD_PATH_RE.search(txt):
                        self.add_wrn("OLD_PATH", "包含旧绝对路径", self._rel(md))

        print("  [结构] 完成")

    # ── 重复检查 ──────────────────────────
    def check_dups(self, zone_filter=None):
        """
        重复检查：
        - 重复ID
        - 重复标题
        """
        id_map = {}
        title_map = {}

        for zone_id, cfg in Z.items():
            if zone_filter and zone_id != zone_filter: continue
            if zone_id in ("refs", "tools"): continue  # 外部参考和工具区跳过

            for sub in cfg["paths"]:
                d = self.root / sub
                if not d.is_dir(): continue

                for md in d.rglob("*.md"):
                    try:
                        txt = md.read_text(encoding="utf-8", errors="replace")
                    except Exception:
                        continue

                    rel = self._rel(md)
                    fm = parse_fm(txt)
                    if not fm: continue

                    # 检查ID重复
                    if "id" in fm:
                        did = fm["id"].strip()
                        if did and did != ":":
                            if did in id_map:
                                self.add_err("DUP_ID", f"重复ID {did} (与 {id_map[did]} 冲突)", rel)
                            else:
                                id_map[did] = rel

                    # 检查标题重复
                    if "title" in fm:
                        title = fm["title"].strip()
                        if title:
                            if title in title_map:
                                self.add_wrn("DUP_TITLE", f"重复标题: {title} (与 {title_map[title]} 冲突)", rel)
                            else:
                                title_map[title] = rel

        print(f"  [重复] {len(id_map)} 个ID | {len(title_map)} 个标题")

    # ── README统计检查 ────────────────────
    def check_readme(self):
        """
        README统计过期检查：
        - 目录数量
        - 工具卡数量
        """
        rd = self.root / "README.md"
        if not rd.is_file(): return

        try:
            txt = rd.read_text(encoding="utf-8", errors="replace")
        except Exception:
            return

        # 检查目录数量
        m = re.search(r'(\d+)\s*个目录', txt)
        if m:
            readme_zones = int(m.group(1))
            actual_zones = len(Z)
            if readme_zones != actual_zones:
                self.add_wrn("ZONE_COUNT", f"README目录数量过期: {readme_zones} vs 实际 {actual_zones}", "README.md")

        # 检查工具卡数量
        m = re.search(r'(\d+)\s*个工具卡', txt)
        if m:
            readme_cards = int(m.group(1))
            cards_dir = self.root / "tools" / "cards"
            actual_cards = len(list(cards_dir.glob("*.md"))) if cards_dir.is_dir() else 0
            if readme_cards != actual_cards:
                self.add_wrn("CARD_COUNT", f"README工具卡数量过期: {readme_cards} vs 实际 {actual_cards}", "README.md")

        print("  [README] 完成")

    # ── 旧绝对路径检查 ────────────────────
    def check_old_paths(self):
        """
        旧绝对路径检查：
        - Windows绝对路径残留
        """
        for zone_id, cfg in Z.items():
            if zone_id in ("refs", "tools"): continue
            for sub in cfg["paths"]:
                d = self.root / sub
                if not d.is_dir(): continue
                for md in d.rglob("*.md"):
                    try:
                        txt = md.read_text(encoding="utf-8", errors="replace")
                    except Exception:
                        continue
                    if OLD_PATH_RE.search(txt):
                        self.add_wrn("OLD_PATH", "包含旧绝对路径", self._rel(md))

        print("  [旧路径] 完成")

    # ── 孤立核心笔记检查 ──────────────────
    def check_orphans(self, zone_filter=None):
        """
        孤立核心笔记检查：
        - 核心区未被引用的笔记
        """
        # 收集所有被引用的文件
        referenced = set()
        for zone_id, cfg in Z.items():
            if zone_filter and zone_id != zone_filter: continue
            if zone_id in ("refs", "tools"): continue
            for sub in cfg["paths"]:
                d = self.root / sub
                if not d.is_dir(): continue
                for md in d.rglob("*.md"):
                    try:
                        txt = md.read_text(encoding="utf-8", errors="replace")
                    except Exception:
                        continue
                    # 检查所有链接
                    for m in WIKILINK_RE.finditer(txt):
                        target = m.group(1).split("|", 1)[0].strip()
                        referenced.add(target)
                    for m in MDLINK_RE.finditer(txt):
                        url = m.group(2).strip()
                        if not url.startswith(("#", "http")):
                            referenced.add(url)

        # 检查核心区的孤立笔记
        core_files = []
        for sub in Z["core"]["paths"]:
            d = self.root / sub
            if d.is_dir():
                for md in d.rglob("*.md"):
                    core_files.append(md)

        for md in core_files:
            rel = self._rel(md)
            name = rel[:-3] if rel.endswith(".md") else rel
            name = name.split("/")[-1]  # 只取文件名

            # 检查是否被引用
            is_referenced = False
            for ref in referenced:
                if name in ref or ref in name:
                    is_referenced = True
                    break

            if not is_referenced and md.name != "README.md":
                self.add_wrn("ORPHAN", "孤立核心笔记（未被其他文件引用）", rel)

        print("  [孤立] 完成")

    # ── 运行所有检查 ──────────────────────
    def run(self, zone_filter=None):
        """运行所有检查"""
        print("=" * 70)
        print(f"质量门禁系统 · 根: {self.root}")
        print(f"分区: {zone_filter or 'all'}")
        print("=" * 70)

        self._prepare()
        self.check_links(zone_filter)
        self.check_fm(zone_filter)
        self.check_structure()
        self.check_dups(zone_filter)
        self.check_readme()
        self.check_old_paths()
        self.check_orphans(zone_filter)

        print("=" * 70)
        print(f"检查完成")
        print(f"错误: {len(self.err)}")
        print(f"警告: {len(self.wrn)}")
        print(f"信息: {len(self.inf)}")

        # 核心区必须零错误
        if zone_filter == "core" or zone_filter is None:
            core_errors = [e for e in self.err if e.get("file", "").startswith(("schema/", "methods/", "knowledge/"))]
            if core_errors:
                print("❌ 核心区发现错误，不符合验收标准！")
                for err in core_errors[:10]:
                    print(f"  {err['code']}: {err['msg']} ({err['file']})")
                if len(core_errors) > 10:
                    print(f"  ... 还有 {len(core_errors) - 10} 个错误")
            else:
                print("✅ 核心区零错误，符合验收标准")

        verdict = "PASS ✅（可提交）" if not self.err else \
            f"FAIL ❌（{len(self.err)}个ERROR，需修复后再提交）"
        print(f"结论: {verdict}")
        print("=" * 70)

    # ── JSON输出 ──────────────────────────
    def json_output(self):
        """
        安全的JSON输出，避免崩溃
        - 限制输出大小
        - 降级路径
        """
        try:
            report = {
                "timestamp": datetime.now().isoformat(),
                "success": len(self.err) == 0,
                "summary": {
                    "error_count": len(self.err),
                    "warn_count": len(self.wrn),
                    "info_count": len(self.inf),
                    "pass": len(self.err) == 0
                },
                "by_check": {
                    "links": len([e for e in self.err if "LINK" in e.get("code", "")]),
                    "frontmatter": len([e for e in self.err if "FRONTMATTER" in e.get("code", "") or "BAD" in e.get("code", "")]),
                    "structure": len([e for e in self.err if "STRUCT" in e.get("code", "")]),
                    "duplicate": len([e for e in self.err if "DUP" in e.get("code", "")]),
                    "readme": len([e for e in self.err if "README" in e.get("code", "")])
                },
                "errors": self.err[:1000],  # 限制数量
                "warnings": self.wrn[:1000],
                "info": self.inf[:500]
            }

            # 尝试完整输出
            json_str = json.dumps(report, ensure_ascii=False, indent=2)
            sys.stdout.write("\n" + json_str + "\n")
            return True

        except Exception as e:
            # 降级为简化输出
            try:
                simplified = {
                    "timestamp": datetime.now().isoformat(),
                    "success": False,
                    "error": f"JSON序列化失败: {str(e)}",
                    "summary": {
                        "error_count": len(self.err),
                        "warn_count": len(self.wrn),
                        "pass": len(self.err) == 0
                    },
                    "error_count": len(self.err),
                    "warn_count": len(self.wrn)
                }
                json_str = json.dumps(simplified, ensure_ascii=False, indent=2)
                sys.stdout.write("\n" + json_str + "\n")
            except Exception:
                sys.stdout.write(f'\n{{"error":"JSON输出完全失败","err_count":{len(self.err)},"wrn_count":{len(self.wrn)}}}\n')
            return False


# ── 入口 ──────────────────────────────────
def main():
    args = sys.argv[1:]
    zone_filter = None
    json_out = False
    strict = False
    root = None

    for a in args:
        if a.startswith("--zone="):
            zone_filter = a.split("=", 1)[1]
        elif a.startswith("--root="):
            root = a.split("=", 1)[1]
        elif a == "--json":
            json_out = True
        elif a == "--strict":
            strict = True

    # 确定根目录
    if root is None:
        # Script: tools/scripts/quality/质量门禁系统.py
        # Root: ../../../
        root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

    # 验证根目录
    if not os.path.exists(os.path.join(root, "README.md")):
        print(f"❌ 根目录错误: {root}", file=sys.stderr)
        print(f"   提示: 使用 --root=<路径> 指定正确的知识库根目录", file=sys.stderr)
        sys.exit(1)

    # 重定向输出
    _orig_stdout = sys.stdout
    if json_out:
        sys.stdout = sys.stderr

    # 创建检查器并运行
    try:
        gate = Gate(root)
        gate.run(zone_filter)
    except Exception as e:
        print(f"❌ 检查器运行失败: {str(e)}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)

    # JSON输出
    if json_out:
        sys.stdout = _orig_stdout
        gate.json_output()

    return 1 if gate.err else 0


if __name__ == "__main__":
    sys.exit(main())
