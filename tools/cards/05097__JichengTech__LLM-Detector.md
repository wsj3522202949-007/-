---
id: tool-05097
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: LLM-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/jichengtech/llm-detector
created: 2026-07-18
updated: 2026-07-18
no: 5097
category: 一、去 AI 味 / Humanizer 库
repo: JichengTech/LLM-Detector
stars: 25
url: https://github.com/jichengtech/llm-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 61e59f5b84c5b17d
  - methods/改稿润色指令库.md
---

# JichengTech/LLM-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/jichengtech/llm-detector
- **Stars**：25
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：This is an official implementation of paper "LLM-Detector: Improving AI-Generated Chinese Text Detection with Open-Source LLM Instruction Tuning"
- **本地描述**：This is an official implementation of paper "LLM-Detector: Improving AI-Generated Chinese Text Detection with Open-Source LLM Instruction Tuning"
- **拉取时间**：2026-07-25 18:05:59

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---


## <img src="assets/logo.png" style="vertical-align: middle; width: 45px;"> LLM-Detector: Improving AI-Generated Chinese Text Detection with Open-Source LLM Instruction Tuning

## Timeline

<!-- - 📢 *Feb. 2, 2024* We published a technical report on LLM-Detector at [arxiv](https://arxiv.org/abs/2402.01158)! -->
- 📢 *Jan. 25, 2024* We have released the small version of the LLM-Detector.
- 📢 *Nov. 9, 2023* We are starting the design and construction of the LLM-Detector!
<!--
## Contributions


||   |   ||
|:-:|:-:|:-:|:-|
|<img src="https://avatars.githubusercontent.com/u/55651568?v=4" alt="" width="40"/>|<img src="https://avatars.githubusercontent.com/u/44778029?v=4" alt="" width="40"/>|<img src="https://avatars.githubusercontent.com/u/42091637?v=4" alt="" width="40"/>|<img src="https://avatars.githubusercontent.com/u/38195038?v=4" alt="" width="40"/>|
| [Rongsheng Wang](https://github.com/WangRongsheng) </br>@MPU & QiYuan-Tech | [Haoming Chen](https://github.com/uxfion) </br>@MPU & QiYuan-Tech | [Ruizhe Zhou](https://github.com/RetroZhou) </br>@MPU & QiYuan-Tech |[Jing Tang](https://github.com/vaew) </br>@HUST |

<table>
  <tr>
    <td width= "165"><img src="https://avatars.githubusercontent.com/u/55651568?v=4" alt="Chat_haruhi" width="160"></td>
    <td>
      <h2><a href="https://github.com/WangRongsheng"> Rongsheng Wang </a> @MPU & QiYuan-Tech </h2>
      <p> 项目发起者, 数据采集 </p>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td width= "165"><img src="https://avatars.githubusercontent.com/u/44778029?v=4" alt="Chat_haruhi" width="160"></td>
    <td>
      <h2><a href="https://github.com/uxfion"> Haoming Chen </a> @MPU & QiYuan-Tech </h2>
      <p> 数据采集 </p>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td width= "165"><img src="https://avatars.githubusercontent.com/u/42091637?v=4" alt="Chat_haruhi" width="160"></td>
    <td>
      <h2><a href="https://github.com/RetroZhou"> Ruizhe Zhou </a> @MPU & QiYuan-Tech </h2>
      <p> 数据采集 </p>
    </td>
  </tr>
</table>


**Institutions**
||||
|:-:|:-:|:-:|
|[QiYuan](https://github.com/QiYuan-tech)|[MPU](https://www.mpu.edu.mo/zh/index.php)|[HUST](https://www.hust.edu.cn/)|
|<img src="https://avatars.githubusercontent.com/u/149642553?s=200&v=4" alt="" width="40"/>|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Macao_Polytechnic_University_logo.svg/150px-Macao_Polytechnic_University_logo.svg.png" alt="" width="40"/>|<img src="https://upload.wikimedia.org/wikipedia/zh/thumb/a/ab/Huazhong_University_of_Science_%26_Technology_logo.svg/230px-Huazhong_University_of_Science_%26_Technology_logo.svg.png" alt="" width="40"/>|

> *The above rankings are not in any particular order.*


## References

1. https://github.com/cardiffnlp/xlm-t
2. https://github.com/Hello-SimpleAI/chatgpt-comparison-detection
3. https://github.com/blmoistawinde/HarvestText
4. https://github.com/BLKSerene/Wordless
5. https://github.com/hankcs/HanLP
6. https://github.com/yafuly/DeepfakeTextDetect

-->

## Model

|Model|Download|
|:-|:-|
|LLM-Detector-Small-en|[![Static Badge](https://img.shields.io/badge/-gery?style=social&label=🤗%20Huggingface)](https://huggingface.co/QiYuan-tech/LLM-Detector-Small-en) [![Static Badge](https://img.shields.io/badge/-gery?style=social&label=🤖%20ModelScope)](https://modelscope.cn/models/QiYuan-tech/LLM-Detector-Small-en)|
|LLM-Detector-Small-zh|[![Static Badge](https://img.shields.io/badge/-gery?style=social&label=🤗%20Huggingface)](https://huggingface.co/QiYuan-tech/LLM-Detector-Small-zh) [![Static Badge](https://img.shields.io/badge/-gery?style=social&label=🤖%20ModelScope)](https://modelscope.cn/models/QiYuan-tech/LLM-Detector-Small-zh)|



## Citation

If you find our work helpful, feel free to give us a cite.

```bibtex
@article{wang2024llm,
  title={LLM-Detector: Improving AI-Generated Chinese Text Detection with Open-Source LLM Instruction Tuning},
  author={Wang, Rongsheng and Chen, Haoming and Zhou, Ruizhe and Ma, Han and Duan, Yaofei and Kang, Yanlan and Yang, Songhua and Fan, Baoyu and Tan, Tao},
  journal={arXiv preprint arXiv:2402.01158},
  year={2024}
}
```

<!--
```bibtex
@misc{wang2024llmdetector,
      title={LLM-Detector: Improving AI-Generated Chinese Text Detection with Open-Source LLM Instruction Tuning}, 
      author={Rongsheng Wang and Haoming Chen and Ruizhe Zhou and Han Ma and Yaofei Duan and Yanlan Kang and Songhua Yang and Baoyu Fan and Tao Tan},
      year={2024},
      eprint={2402.01158},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
-->
## License
