---
id: tool-07132
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 中文友好, 本地写作]
title: novel-to-script
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/ai-practical-lab/novel-to-script
created: 2026-07-18
updated: 2026-07-18
no: 7132
category: 画龙补充 / 扩容入库 — 补充源
repo: ai-practical-lab/novel-to-script
stars: 0
url: https://github.com/ai-practical-lab/novel-to-script
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# ai-practical-lab/novel-to-script

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/ai-practical-lab/novel-to-script
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：novel-to-script
- **拉取时间**：2026-07-25 19:11:49

---

# Novel to Script - 小说转短剧剧本（最终版）

## 版本说明

**V3 Final** - 基于参考剧本标准重写

## 主要改进

### 1. 台词改进
- ✅ 缩短到15字以内
- ✅ 增加命令句："给我滚！"、"闭嘴！"
- ✅ 增加反问句："你也配？"、"凭什么？"
- ✅ 口语化，接地气

### 2. 动作描写
- ✅ 可视化，演员能直接演
- ✅ 增加微表情："眼角微挑"、"手指轻颤"
- ✅ 增加细节："指甲掐进掌心"、"喉结滚动"

### 3. 情绪设计
- ✅ 每集3个情绪起伏点
- ✅ 压抑→反击→爽的曲线
- ✅ 打脸反派的爽感

### 4. 钩子设计
- ✅ 每集结尾强悬念
- ✅ 付费卡点标注清晰
- ✅ 黑屏字幕留悬念

### 5. 格式规范
- ✅ 场景头：X-Y 地点 时间 内外
- ✅ 动作：【】和△标记
- ✅ 台词：带情绪标注
- ✅ 内心独白：（OS）

## 使用方法

```bash
python3 scripts/convert_final.py \
  -i /path/to/novel.txt \
  -o /path/to/output.txt \
  -e 10 \
  -t warrior
```

参数：
- `-i`: 输入小说文件
- `-o`: 输出剧本文件
- `-e`: 集数（10/30/100）
- `-t`: 模板（sweet/revenge/warrior）

## 输出示例

桌面上的 `短剧剧本_最终版.txt` 是测试输出。

## 对比参考剧本

| 检查项 | 参考剧本 | 本版本 |
|-------|---------|-----related:
  - methods/QUICK_START.md
---|
| 格式规范 | ✅ | ✅ |
| 台词简短 | ✅ | ✅ |
| 动作可视化 | ✅ | ✅ |
| 情绪起伏 | ✅ | ✅ |
| 钩子设计 | ✅ | ✅ |
| 付费卡点 | ✅ | ✅ |

## 文件说明

- `scripts/convert_final.py` - 最终版本脚本
- `剧本标准.md` - 从参考剧本提取的标准
- `自我检查报告.md` - 改进过程记录

## 后续优化方向

1. 基于AI生成更个性化的台词
2. 自动识别小说中的具体剧情
3. 学习示例剧本的台词风格
4. 批量处理多个文件
