---
id: tool-05202
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Reliability-of-AI-text-detectors
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/vinusankars/reliability-of-ai-text-detectors
created: 2026-07-18
updated: 2026-07-18
no: 5202
category: 一、去 AI 味 / Humanizer 库
repo: vinusankars/Reliability-of-AI-text-detectors
stars: 92
url: https://github.com/vinusankars/reliability-of-ai-text-detectors
tier: "A"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# vinusankars/Reliability-of-AI-text-detectors

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/vinusankars/reliability-of-ai-text-detectors
- **Stars**：92
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Can AI-Generated Text be Reliably Detected?
- **本地描述**：Can AI-Generated Text be Reliably Detected?
- **拉取时间**：2026-07-25 18:09:52

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
see_also:
  - 07480__oubigfa__de-ai-prompt-enhancer-writer-booster-skill.md
  - 07171__brandonwise__humanizer.md
  - 07166__blader__humanizer.md
---

# Can AI-Generated Text be Reliably Detected?
### Paper: https://arxiv.org/abs/2303.11156

This repository contains codes for reproducing our results on paraphrasing attacks, impossibility results, and spoofing attacks. Please see requirements.txt for Python libraries that are needed. To reproduce our attacks on text watermarks, clone the repository from https://github.com/jwkirchenbauer/lm-watermarking.git to this folder. Clone https://github.com/martiansideofthemoon/ai-detection-paraphrases/ to perform experiments using DIPPER paraphraser.

rephrase/ contains the paraphrasing attacks.<br/>
impossibilty/ contains codes for visualizing our theoretical results.<br/>
pair-distribution/ contains codes for spoofing atttacks.<br/>

![](https://github.com/vinusankars/Reliability-of-AI-text-detectors/blob/main/title.png)

<p/>
====================================================================


COPYRIGHT AND PERMISSION NOTICE <br/>
UMD Software [Can AI-Generated Text be Reliably Detected?] Copyright (C) 2022 University of Maryland<br/>
All rights reserved.<br/>
The University of Maryland (“UMD”) and the developers of [Can AI-Generated Text be Reliably Detected?] software (“Software”) give recipient (“Recipient”) permission to download a single copy of the Software in source code form and use by university, non-profit, or research institution users only, provided that the following conditions are met:<br/>
1)	Recipient may use the Software for any purpose, EXCEPT for commercial benefit.<br/>
2)	Recipient will not copy the Software.<br/>
3)	Recipient will not sell the Software.<br/>
4)	Recipient will not give the Software to any third party.<br/>
5)	Any party desiring a license to use the Software for commercial purposes shall contact:<br/>
UM Ventures, College Park at UMD at otc@umd.edu.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS, CONTRIBUTORS, AND THE UNIVERSITY OF MARYLAND "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO  EVENT SHALL THE COPYRIGHT OWNER, CONTRIBUTORS OR THE UNIVERSITY OF MARYLAND BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.<br/>

