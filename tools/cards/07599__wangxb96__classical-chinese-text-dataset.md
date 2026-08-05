---
id: tool-07599
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 中文友好, 本地写作]
title: classical-chinese-text-dataset
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/wangxb96/classical-chinese-text-dataset
created: 2026-07-18
updated: 2026-07-18
no: 7599
category: 画龙补充 / 扩容入库 — 补充源
repo: wangxb96/classical-chinese-text-dataset
stars: 0
url: https://github.com/wangxb96/classical-chinese-text-dataset
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# wangxb96/classical-chinese-text-dataset

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/wangxb96/classical-chinese-text-dataset
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：这是一个包含《道德经》、《易经》等经典古文的标注数据集，适用于自然语言处理、机器学习及文化研究，欢迎贡献和使用！This repository hosts a labeled dataset of classical Chinese texts, including the Dao De Jing and I Ching, suitable for NLP, machine learning, and cultural research. Contributions are welcome!
- **本地描述**：classical-chinese-text-dataset
- **拉取时间**：2026-07-25 19:26:50

---

# Classical Chinese Text Dataset

这是一个用于存储标注好的古文数据集的 GitHub 仓库。数据集包含《道德经》、《易经》及其他经典古文，经过详细的标签分类和注释，适用于自然语言处理（NLP）和机器学习任务。

---

## 数据集概述

### 数据集结构
数据集以 JSON 格式存储，包含以下内容：
- **id**：唯一标识符。
- **name**：古文名称或章节名称。
- **content**：古文原文。
- **tagged_content**：标注内容，包含标签和解释。
- **explanation**：对古文的详细解释和注释。

### 数据集名单
目前包含的古文数据集如下：
1. **道德经**：老子所著，涵盖道家哲学的核心思想。
2. **易经**：中国古代经典，涵盖六十四卦及其解释。
3. **论语**：孔子及其弟子的言行录，儒家经典之一。
4. **孟子**：孟子所著，儒家思想的重要文献。
5. **庄子**：庄子所著，道家哲学的代表作。
6. **诗经**：中国古代最早的诗歌总集。
7. **楚辞**：屈原等楚国诗人的作品集。

更多古文数据集正在持续添加中，欢迎贡献！

---

## 数据集示例

以下是一个 JSON 格式的数据集示例（以《易经》为例）：

```json
{
  "id": "111111",
  "name": "乾",
  "gua_ci": "乾：元亨，利贞。",
  "tuan_ci": "大哉乾元，万物资始，乃统天。云行雨施，品物流形。大明始终，六位时成，时乘六龙以御天。乾道变化，各正性命，保合大和，乃利贞。首出庶物，万国咸宁。",
  "da_xiang": "天行健，君子以自强不息。",
  "yao_ci": [
    "初九：潜龙，勿用。",
    "九二：见龙在田，利见大人。",
    "九三：君子终日乾乾，夕惕若，厉，无咎。",
    "九四：或跃在渊，无咎。",
    "九五：飞龙在天，利见大人。",
    "上九：亢龙有悔。",
    "用九：见群龙无首，吉。"
  ],
  "xiao_xiang": [
    "潜龙勿用，阳在下也。",
    "见龙在田，德施普也。",
    "终日乾乾，反复道也。",
    "或跃在渊，进无咎也。",
    "飞龙在天，大人造也。",
    "亢龙有悔，盈不可久也。",
    "用九，天德不可为首也。"
  ],
  "symbol": "䷀",
  "tagged_gua_ci": {
    "content": "乾：元亨，利贞。",
    "tag": "元吉",
    "explanation": "乾卦的卦辞为“元亨，利贞”，意味着至善无缺，最好的结果。这里的“元亨”表示大为亨通，是最为吉祥的状态；“利贞”则表示在这样的状态下，保持正直和坚定是非常有利的。因此，乾卦的卦辞属于“元吉”类别，象征着至高无上的吉祥和成功。"
  },
  "tagged_tuan_ci": {
    "content": "大哉乾元，万物资始，乃统天。云行雨施，品物流形。大明始终，六位时成，时乘六龙以御天。乾道变化，各正性命，保合大和，乃利贞。首出庶物，万国咸宁。",
    "tag": "元吉",
    "explanation": "这段彖辞描述了乾卦的至高无上、创造力、滋养力、秩序性、和谐性和领导力，这些都是至善无缺的特质，因此标签为“元吉”。"
  },
  "tagged_da_xiang": {
    "content": "天行健，君子以自强不息。",
    "tag": "其他",
    "explanation": "这句大象辞强调君子应当效法天道，不断自我提升和努力，永不停息。它不属于吉凶悔吝的具体结果，归类为“其他”。"
  },
  "tagged_yao": [
    {
      "content": "初九：潜龙，勿用。",
      "tag": "其他",
      "explanation": "初九爻辞建议保持低调、不急于行动，没有明确的吉凶之分，归类为“其他”。"
    },
    {
      "content": "九二：见龙在田，利见大人。",
      "tag": "吉",
      "explanation": "九二爻辞表达了吉祥、有利的含义，归类为“吉”。"
    },
    {
      "content": "九三：君子终日乾乾，夕惕若，厉，无咎。",
      "tag": "无咎",
      "explanation": "九三爻辞描述了君子通过努力和谨慎避免过失，归类为“无咎”。"
    },
    {
      "content": "九四：或跃在渊，无咎。",
      "tag": "无咎",
      "explanation": "九四爻辞表示在当前情境下，行动或不行动都不会有过失，归类为“无咎”。"
    },
    {
      "content": "九五：飞龙在天，利见大人。",
      "tag": "吉",
      "explanation": "九五爻辞描述了一种非常吉祥的情境，归类为“吉”。"
    },
    {
      "content": "上九：亢龙有悔。",
      "tag": "悔",
      "explanation": "上九爻辞表示事物发展到了极点，容易产生过失，归类为“悔”。"
    },
    {
      "content": "用九：见群龙无首，吉。",
      "tag": "吉",
      "explanation": "用九爻辞表示一种平等、和谐的状态，归类为“吉”。"
    }
  ],
  "tagged_xiao": [
    {
      "content": "潜龙勿用，阳在下也。",
      "tag": "无咎",
      "explanation": "初九小象辞建议保持低调、积蓄力量，归类为“无咎”。"
    },
    {
      "content": "见龙在田，德施普也。",
      "tag": "吉",
      "explanation": "九二小象辞描述了君子的德行广泛施予，归类为“吉”。"
    },
    {
      "content": "终日乾乾，反复道也。",
      "tag": "无咎",
      "explanation": "九三小象辞强调了勤奋和遵循正道的重要性，归类为“无咎”。"
    },
    {
      "content": "或跃在渊，进无咎也。",
      "tag": "无咎",
      "explanation": "九四小象辞表示在谨慎行事的前提下可以避免过失，归类为“无咎”。"
    },
    {
      "content": "飞龙在天，大人造也。",
      "tag": "大吉",
      "explanation": "九五小象辞描述了极高的成就和吉祥，归类为“大吉”。"
    },
    {
      "content": "亢龙有悔，盈不可久也。",
      "tag": "悔",
      "explanation": "上九小象辞提醒人们不要过于自满或过度扩张，归类为“悔”。"
    },
    {
      "content": "用九，天德不可为首也。",
      "tag": "其他",
      "explanation": "用九小象辞表达了哲学思想，归类为“其他”。"
    }
  ]
}
```

---

## 数据集用途

- **自然语言处理**：用于训练古文分类、文本生成、语义分析等模型。
- **机器学习**：用于研究古文中的主题分类、情感分析、知识图谱构建等任务。
- **教育与研究**：为古文研究者提供结构化的数据支持。
- **文化传承**：通过数字化和标注，促进经典文化的传播与学习。

---

## 数据集下载

您可以通过以下方式获取数据集：
1. **直接下载**：点击 [这里](https://github.com/wangxb96/Classical-Chinese-Text-Dataset/archive/main.zip) 下载完整的 JSON 文件。
2. **Git 克隆**：使用以下命令克隆仓库：
   ```bash
   git clone https://github.com/wangxb96/Classical-Chinese-Text-Dataset.git
   ```

---

### 仓库结构

```
Classical-Chinese-Text-Dataset/
├── data/
│   ├── daodejing.json          # 《道德经》数据集
│   ├── yijing.json             # 《易经》数据集
│   ├── lunyu.json              # 《论语》数据集
│   ├── mengzi.json             # 《孟子》数据集
│   ├── zhuangzi.json           # 《庄子》数据集
│   ├── shijing.json            # 《诗经》数据集
│   └── chuci.json              # 《楚辞》数据集
├── LICENSE                     # 开源许可证
├── README.md                   # 项目说明文件
└── .gitignore                  # Git 忽略文件
```

---

## 贡献指南

欢迎贡献更多标注好的古文数据集！请遵循以下步骤：
1. **Fork 仓库**：点击右上角的“Fork”按钮，创建您的副本。
2. **添加数据**：在 `data` 目录下添加新的 JSON 文件，或修改现有文件。
3. **提交 Pull Request**：将您的更改提交到主仓库。

### 贡献要求
- 确保数据格式与现有数据集一致。
- 提供详细的注释和标签分类。
- 注明数据来源和版权信息。

---

## 许可证

本项目采用 `[MIT 许可证](LICENSE)`。您可以自由使用、修改和分发数据集，但请注明出处。

---

## 联系方式

如有任何问题或建议，请通过以下方式联系：
- **邮箱**：wangxubin at kindlab.site
- **GitHub Issues**：在仓库中提交 Issue。

related:
  - methods/QUICK_START.md
---

**Happy Coding!** 🚀


