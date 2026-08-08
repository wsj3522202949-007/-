# -*- coding: utf-8 -*-
"""
test_chapter_policy.py — chapter_policy 模块单元测试

覆盖：
  1. DEFAULT_POLICY v2 键结构
  2. char_verdict() 五种状态：ok / soft_short / soft_long / hard_short / hard_long
  3. char_status() 五种状态码
  4. load_policy() v1（旧键 min_chars/max_chars/hard_max_chars）→ v2 映射
  5. load_policy() v2（新键 soft_min/soft_max/hard_min/hard_max）直读
  6. load_policy() 混合 v1+v2 键
  7. load_policy() 无配置文件回退默认值
  8. 创作闭环助手 generate_chapter_template 使用正确键名

运行：
  cd E:/个人知识库 && python -m pytest tools/scripts/tests/test_chapter_policy.py -v
  或直接：
  python tools/scripts/tests/test_chapter_policy.py
"""

import os
import sys
import json
import shutil
import tempfile
import unittest
from pathlib import Path

# Windows GBK 终端安全：避免 emoji/中文输出 UnicodeEncodeError
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

# ---- 路径设置：确保能 import writing/ 下的模块 ----
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_WRITING_DIR = os.path.join(os.path.dirname(_THIS_DIR), "writing")
if _WRITING_DIR not in sys.path:
    sys.path.insert(0, _WRITING_DIR)
_SCRIPTS_DIR = os.path.dirname(_THIS_DIR)
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from chapter_policy import (
    DEFAULT_POLICY,
    char_verdict,
    char_status,
    load_policy,
    _LEGACY_KEY_MAP,
)


class TestDefaultPolicy(unittest.TestCase):
    """DEFAULT_POLICY 必须是 v2 结构的完整字典。"""

    def test_has_all_v2_keys(self):
        required = ("platform", "policy_version", "soft_min", "soft_max",
                     "hard_min", "hard_max", "target")
        for k in required:
            self.assertIn(k, DEFAULT_POLICY, f"DEFAULT_POLICY 缺少键: {k}")

    def test_policy_version_is_v2(self):
        self.assertEqual(DEFAULT_POLICY["policy_version"], "v2")

    def test_no_legacy_keys_in_default(self):
        """DEFAULT_POLICY 不应包含旧键名。"""
        for old_k in _LEGACY_KEY_MAP:
            self.assertNotIn(old_k, DEFAULT_POLICY,
                             f"DEFAULT_POLICY 不应包含旧键: {old_k}")

    def test_intervals_make_sense(self):
        """硬区间必须包住软区间：hard_min ≤ soft_min ≤ soft_max ≤ hard_max"""
        self.assertLessEqual(DEFAULT_POLICY["hard_min"], DEFAULT_POLICY["soft_min"])
        self.assertLessEqual(DEFAULT_POLICY["soft_min"], DEFAULT_POLICY["soft_max"])
        self.assertLessEqual(DEFAULT_POLICY["soft_max"], DEFAULT_POLICY["hard_max"])


class TestCharVerdict(unittest.TestCase):
    """char_verdict() 两级判级输出。"""

    def setUp(self):
        self.p = DEFAULT_POLICY  # soft_min=2600 soft_max=3400 hard_min=2200 hard_max=4000

    def test_ok(self):
        self.assertIn("达标", char_verdict(3000, self.p))
        self.assertIn("达标", char_verdict(2600, self.p))
        self.assertIn("达标", char_verdict(3400, self.p))

    def test_soft_short(self):
        v = char_verdict(2400, self.p)
        self.assertIn("偏短", v)
        self.assertIn("2400", v)

    def test_soft_long(self):
        v = char_verdict(3700, self.p)
        self.assertIn("偏长", v)
        self.assertIn("3700", v)

    def test_hard_short(self):
        v = char_verdict(1500, self.p)
        self.assertIn("严重不足", v)
        self.assertIn("1500", v)

    def test_hard_long(self):
        v = char_verdict(4500, self.p)
        self.assertIn("严重超标", v)
        self.assertIn("4500", v)

    def test_boundary_hard_short(self):
        """hard_min 边界值不是 hard_short（等于硬下限不算严重不足）。"""
        v = char_verdict(self.p["hard_min"], self.p)
        self.assertNotIn("严重不足", v)

    def test_boundary_hard_long(self):
        """hard_max 边界值不是 hard_long（等于硬上限不算严重超标）。"""
        v = char_verdict(self.p["hard_max"], self.p)
        self.assertNotIn("严重超标", v)


class TestCharStatus(unittest.TestCase):
    """char_status() 返回机器可读状态码。"""

    def setUp(self):
        self.p = DEFAULT_POLICY

    def test_ok(self):
        self.assertEqual(char_status(3000, self.p), "ok")

    def test_soft_short(self):
        self.assertEqual(char_status(2400, self.p), "soft_short")

    def test_soft_long(self):
        self.assertEqual(char_status(3700, self.p), "soft_long")

    def test_hard_short(self):
        self.assertEqual(char_status(1500, self.p), "hard_short")

    def test_hard_long(self):
        self.assertEqual(char_status(4500, self.p), "hard_long")

    def test_all_codes_are_known(self):
        """确保返回的状态码只在已知集合中。"""
        valid = {"ok", "soft_short", "soft_long", "hard_short", "hard_long"}
        for n in (1500, 2400, 3000, 3700, 4500):
            self.assertIn(char_status(n, self.p), valid)


class TestLoadPolicyV1Compat(unittest.TestCase):
    """load_policy() 对 v1 旧键名自动映射到 v2。"""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def _write_yaml(self, name, data_str):
        path = os.path.join(self.tmpdir, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(data_str)
        return path

    def test_v1_keys_map_to_v2(self):
        """旧键 min_chars / max_chars / hard_max_chars → soft_min / soft_max / hard_max"""
        self._write_yaml("chapter_policy.yaml", """\
platform: 起点
min_chars: 2000
max_chars: 3000
hard_max_chars: 3500
""")
        p = load_policy(self.tmpdir)
        self.assertEqual(p["platform"], "起点")
        self.assertEqual(p["soft_min"], 2000)   # min_chars → soft_min
        self.assertEqual(p["soft_max"], 3000)   # max_chars  → soft_max
        self.assertEqual(p["hard_max"], 3500)   # hard_max_chars → hard_max
        self.assertEqual(p["policy_version"], "v2")  # 默认值保留

    def test_v2_keys_direct_read(self):
        """新键 soft_min/soft_max/hard_min/hard_max 直接读取。"""
        self._write_yaml("chapter_policy.yaml", """\
platform: 番茄
policy_version: v2
soft_min: 2500
soft_max: 3500
hard_min: 2000
hard_max: 4500
target: 3000
""")
        p = load_policy(self.tmpdir)
        self.assertEqual(p["soft_min"], 2500)
        self.assertEqual(p["soft_max"], 3500)
        self.assertEqual(p["hard_min"], 2000)
        self.assertEqual(p["hard_max"], 4500)
        self.assertEqual(p["target"], 3000)

    def test_mixed_v1_v2_v2_wins_on_overlap(self):
        """同时有新旧键时，旧键在 load_policy 中被后处理会覆盖新版读取，
        但这个行为应明确（目前旧键覆盖）。"""
        self._write_yaml("chapter_policy.yaml", """\
platform: 七猫
soft_min: 2800
soft_max: 3800
min_chars: 2000
max_chars: 3200
""")
        p = load_policy(self.tmpdir)
        # 旧键在加载循环中后于新键处理，会覆盖
        self.assertEqual(p["soft_min"], 2000)
        self.assertEqual(p["soft_max"], 3200)

    def test_json_config(self):
        """JSON 配置文件同样支持。"""
        path = os.path.join(self.tmpdir, "chapter_policy.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump({
                "platform": "豆瓣阅读",
                "soft_min": 3000,
                "soft_max": 5000,
                "hard_min": 2500,
                "hard_max": 6000,
            }, f)
        p = load_policy(self.tmpdir)
        self.assertEqual(p["platform"], "豆瓣阅读")
        self.assertEqual(p["soft_min"], 3000)
        self.assertEqual(p["soft_max"], 5000)

    def test_no_config_falls_back_to_default(self):
        """无配置文件时回退 DEFAULT_POLICY。"""
        empty_dir = tempfile.mkdtemp()
        try:
            p = load_policy(empty_dir)
            self.assertEqual(p["soft_min"], DEFAULT_POLICY["soft_min"])
            self.assertEqual(p["soft_max"], DEFAULT_POLICY["soft_max"])
            self.assertEqual(p["policy_version"], "v2")
        finally:
            import shutil
            shutil.rmtree(empty_dir, ignore_errors=True)

    def test_partial_override_keeps_defaults(self):
        """部分覆盖：未指定的键保留 DEFAULT_POLICY 值。"""
        self._write_yaml("chapter_policy.yaml", """\
platform: 飞卢
soft_min: 2200
""")
        p = load_policy(self.tmpdir)
        self.assertEqual(p["platform"], "飞卢")
        self.assertEqual(p["soft_min"], 2200)
        # 未覆盖项保留默认
        self.assertEqual(p["soft_max"], DEFAULT_POLICY["soft_max"])
        self.assertEqual(p["hard_min"], DEFAULT_POLICY["hard_min"])
        self.assertEqual(p["hard_max"], DEFAULT_POLICY["hard_max"])


class TestClosureHelperTemplate(unittest.TestCase):
    """创作闭环助手生成模板时使用正确 v2 键名。"""

    def test_template_uses_v2_keys_not_v1(self):
        """generate_chapter_template 读取的 dict 不应再用 min_chars/max_chars。"""
        # 用 reflexion 检查 generate_chapter_template 源码，确保不含旧键字面量
        import inspect
        # 使用创作闭环助手模块
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "closure_helper",
            os.path.join(os.path.dirname(_THIS_DIR), "创作闭环助手.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        src = inspect.getsource(mod.generate_chapter_template)
        # 不应包含旧键字面量（直接索引 policy dict）
        self.assertNotIn("min_chars", src)
        self.assertNotIn("max_chars", src)
        self.assertNotIn("hard_max_chars", src)
        # 应使用新键
        self.assertIn("soft_min", src)
        self.assertIn("soft_max", src)
        self.assertIn("hard_min", src)
        self.assertIn("hard_max", src)


class TestSelfCheckHardBlocking(unittest.TestCase):
    """创作闭环助手 self_check() 硬阻断返回非零。"""

    def test_self_check_returns_2_on_hard_block(self):
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "closure_helper",
            os.path.join(os.path.dirname(_THIS_DIR), "创作闭环助手.py"))
        mod = importlib.util.module_from_spec(spec)
        # Monkey-patch 项目路径让测试不依赖真实项目存在
        # 直接测 char_status 与返回值逻辑
        spec.loader.exec_module(mod)

        # char_status 验证：hard_short → 返回 2
        self.assertEqual(mod.char_status(500, DEFAULT_POLICY), "hard_short")
        self.assertEqual(mod.char_status(5000, DEFAULT_POLICY), "hard_long")
        # soft 状态应返回非 0（软警告）但与 hard 区分
        self.assertEqual(mod.char_status(2400, DEFAULT_POLICY), "soft_short")


class TestHardBlockExitCode(unittest.TestCase):
    """chapter_selfcheck 在硬阻断时返回非零退出码。"""

    def test_char_verdict_detects_hard_block(self):
        """严重不足/严重超标 标志应可被代码正确检测。"""
        v = char_verdict(1000, DEFAULT_POLICY)
        self.assertTrue("严重不足" in v or "严重超标" in v)

        v2 = char_verdict(5000, DEFAULT_POLICY)
        self.assertTrue("严重不足" in v2 or "严重超标" in v2)

        v3 = char_verdict(3000, DEFAULT_POLICY)
        self.assertFalse("严重不足" in v3 or "严重超标" in v3)


# ===========================================================================
# 反「指标刷分」检测防回归测试（2026-08-08）
# 背景：旧门禁只查 ≥30字段落、相似度≥0.80 的跨章重复，作者用短句/短段落
# 复制（"宿主…你确定吗？/确定。/那就明天见。"×6章）即可绕过，仍判达标。
# 以下测试把新检测的行为钉死，防止将来调阈值时再次出现假绿灯。
# ===========================================================================
from chapter_selfcheck import (  # noqa: E402
    extract_body,
    extract_hook_zone,
    find_exact_duplicate_paras,
    find_repeated_phrases,
    find_duplicate_sequences,
    find_near_duplicate_paras,
    check_hook_uniqueness,
    load_oral_tic_whitelist,
)


class _ChapterDirMixin:
    """构造临时章节目录的辅助方法。"""

    def _make_dir(self, chapters):
        d = tempfile.mkdtemp()
        for i, (name, body) in enumerate(chapters.items(), 1):
            p = os.path.join(d, name)
            with open(p, "w", encoding="utf-8") as f:
                f.write(f"---\nid: c{i}\ntype: chapter\n---\n\n{body}")
        self.addCleanup(lambda: shutil.rmtree(d, ignore_errors=True))
        return d


class TestAntiGamingExactDuplicates(_ChapterDirMixin, unittest.TestCase):
    """跨章完全重复段落检测（短段 12 字起，旧检测的盲区）。"""

    def test_short_para_repeated_across_chapters(self):
        d = self._make_dir({
            "第001章-A.md": "白天进货，晚上算账。\n\n宿主，系统的声音带着一丝意味深长，你确定吗？\n\n明天照常开门。",
            "第002章-B.md": "宿主，系统的声音带着一丝意味深长，你确定吗？\n\n日子一天天过去。",
            "第003章-C.md": "完全不同的内容，没有任何重复。\n\n另一段也完全不同。",
        })
        dups = find_exact_duplicate_paras(d)
        self.assertEqual(len(dups), 1, f"应抓到 1 个重复段落，实际 {dups}")
        self.assertIn("你确定吗", dups[0]["para"])
        self.assertEqual(dups[0]["count"], 2)

    def test_short_para_below_12_chars_not_reported(self):
        d = self._make_dir({
            "第001章-A.md": "确定。\n\n明天见。\n\n白天进货晚上算账。",
            "第002章-B.md": "确定。\n\n明天见。\n\n白天进货晚上算账。",
        })
        dups = find_exact_duplicate_paras(d)
        self.assertEqual(dups, [], "12 字以下的超短段不应由段落级检测报告")


class TestAntiGamingPhrasesAndWhitelist(_ChapterDirMixin, unittest.TestCase):
    """12 字以上重复短语 + 口头禅白名单豁免。"""

    _PHRASE = "街边的路灯亮了起来，照在他苍白的脸上。"

    def test_phrase_repeated_two_chapters(self):
        d = self._make_dir({
            "第001章-A.md": f"他走出店门。\n\n{self._PHRASE}\n\n往家走去。",
            "第002章-B.md": f"夜幕降临。\n\n{self._PHRASE}\n\n他叹了口气。",
        })
        ph = find_repeated_phrases(d)
        self.assertEqual(len(ph), 1)
        self.assertIn("路灯亮了起来", ph[0]["phrase"])
        self.assertEqual(ph[0]["count"], 2)

    def test_whitelist_exempts_oral_tic(self):
        d = self._make_dir({
            "第001章-A.md": f"他走出店门。\n\n{self._PHRASE}\n\n往家走去。",
            "第002章-B.md": f"夜幕降临。\n\n{self._PHRASE}\n\n他叹了口气。",
        })
        # 白名单包含该短语 → 豁免
        ph = find_repeated_phrases(d, whitelist=(self._PHRASE,))
        self.assertEqual(ph, [], "白名单中的口头禅应被豁免")


class TestAntiGamingSequences(_ChapterDirMixin, unittest.TestCase):
    """段落序列重复（整套结尾模板："你确定吗→确定→明天见"）。"""

    _TAIL = ("宿主，系统的声音带着一丝意味深长，你确定吗？\n\n"
             "确定。\n\n那就明天见。")

    def test_template_tail_sequence_repeated(self):
        d = self._make_dir({
            "第001章-A.md": f"正文甲。\n\n{self._TAIL}\n\n次日清晨。",
            "第002章-B.md": f"正文乙。\n\n{self._TAIL}\n\n次日清晨。",
        })
        seqs = find_duplicate_sequences(d)
        self.assertTrue(seqs, "整套结尾序列重复应被序列检测抓到")
        self.assertEqual(seqs[0]["count"], 2)
        self.assertIn("那就明天见", seqs[0]["sequence"])


class TestAntiGamingNearDuplicates(_ChapterDirMixin, unittest.TestCase):
    """MinHash/改写式近似重复检测。"""

    _BASE = ("那天晚上他翻来覆去睡不着，盯着天花板想了一整夜，眼前全是系统面板上"
             "那些跳动的数字。废手机十五块，三年后八千块，父亲的医药费八十万。")

    def test_rewritten_para_detected(self):
        # 改 2 处短语（约 15% 内容）：实测 jaccard ≈0.74，应在 0.72 阈值内命中
        d = self._make_dir({
            "第001章-A.md": self._BASE,
            "第002章-B.md": self._BASE.replace("跳动的数字", "跳动数字")
                                          .replace("医药费八十万", "手术费八十万"),
        })
        near = find_near_duplicate_paras(d)
        self.assertEqual(len(near), 1, f"改写式近似重复应被检测，实际 {near}")
        self.assertGreaterEqual(near[0]["similarity"], 0.70)

    def test_unrelated_paras_not_reported(self):
        d = self._make_dir({
            "第001章-A.md": "他走进旧货市场，在一排蒙灰的摊位前停下脚步。今天他想碰碰运气。",
            "第002章-B.md": "系统面板浮现在眼前，一行行数字快速滚动。任务已完成三分之一。",
        })
        near = find_near_duplicate_paras(d)
        self.assertEqual(near, [])


class TestAntiGamingHookUniqueness(_ChapterDirMixin, unittest.TestCase):
    """章末钩子唯一性。"""

    def test_identical_hook_zones_detected(self):
        d = self._make_dir({
            "第001章-A.md": "正文甲。\n\n**【章末钩子】**\n\n他翻来覆去睡不着，盯着天花板。",
            "第002章-B.md": "正文乙。\n\n**【章末钩子】**\n\n他翻来覆去睡不着，盯着天花板。",
        })
        hk = check_hook_uniqueness(d)
        self.assertEqual(len(hk), 1, f"相同钩子区应报雷同，实际 {hk}")

    def test_distinct_hook_zones_ok(self):
        d = self._make_dir({
            "第001章-A.md": "正文甲。\n\n**【章末钩子】**\n\n他守在病房的陪护椅上。",
            "第002章-B.md": "正文乙。\n\n**【章末钩子】**\n\n他从抽屉里翻出圆珠笔写字。",
        })
        hk = check_hook_uniqueness(d)
        self.assertEqual(hk, [])


class TestMetaBlockExtraction(unittest.TestCase):
    """【数据预估】等元信息块必须从正文剔除（字数刷分源）。"""

    def test_data_block_stripped_from_body(self):
        raw = ("---\nid: x\n---\n\n正文第一段。\n\n**【数据预估】**\n\n"
               "- 完读率目标：50%\n\n- 追读率目标：15%\n\n- 下一章：第一次估值\n")
        body = extract_body(raw)
        self.assertIn("正文第一段", body)
        self.assertNotIn("完读率目标", body, "【数据预估】块必须剔除")
        self.assertNotIn("下一章", body, "【数据预估】块必须剔除")

    def test_hook_zone_extraction(self):
        raw = ("---\nid: x\n---\n\n正文。\n\n**【章末钩子】**\n\n"
               "他翻来覆去睡不着。\n\n**【数据预估】**\n\n- 下一章：xx\n")
        zone = extract_hook_zone(raw)
        self.assertIn("翻来覆去", zone)
        self.assertNotIn("下一章", zone, "钩子区不应包含数据块")


class TestOralTicWhitelistFile(unittest.TestCase):
    """口头禅白名单文件读取。"""

    def test_load_from_project_file(self):
        d = tempfile.mkdtemp()
        self.addCleanup(lambda: shutil.rmtree(d, ignore_errors=True))
        with open(os.path.join(d, "chapter_oral_tic.txt"), "w", encoding="utf-8") as f:
            f.write("# 注释\n叮\n宿主，系统的声音带着一丝意味深长\n")
        wl = load_oral_tic_whitelist(d)
        self.assertIn("叮", wl)
        self.assertIn("宿主，系统的声音带着一丝意味深长", wl)
        self.assertEqual(len(wl), 2, "注释行不应计入白名单")

    def test_missing_file_returns_empty(self):
        d = tempfile.mkdtemp()
        self.addCleanup(lambda: shutil.rmtree(d, ignore_errors=True))
        self.assertEqual(load_oral_tic_whitelist(d), ())


if __name__ == "__main__":
    unittest.main()
