---
id: tool-00506
type: tool
area: 库
status: active
tags: [提示词, Python, 协议宽松, 本地优先, 中文友好, 多Agent, 本地写作]
title: ComfyUI_JoyAI_Echo
summary: 提示词/写作工作流
source: https://github.com/smthemex/comfyui_joyai_echo
created: 2026-07-18
updated: 2026-07-18
no: 506
category: 二、网文 / 长篇 AI 写作系统 库
repo: smthemex/ComfyUI_JoyAI_Echo
stars: 57
url: https://github.com/smthemex/comfyui_joyai_echo
tier: "A"
use_case: "提示词/写作工作流"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# smthemex/ComfyUI_JoyAI_Echo

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/smthemex/comfyui_joyai_echo
- **Stars**：57
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：Pushing the Frontier of Long Video Generation  Standalone, inference-only release for minute-level multi-shot audio-video generation with a distilled DMD generator, paired cross-modal memory, and story-level consistency.
- **本地描述**：Pushing the Frontier of Long Video Generation  Standalone, inference-only release for minute-level multi-shot audio-video generation with a distilled DMD generator, paired cross-modal memory, and story-level consistency.
- **拉取时间**：2026-07-23 22:53:49

---

# ComfyUI_JoyAI_Echo
[JoyAI_Echo](https://github.com/jd-opensource/JoyAI-Echo) ：Pushing the Frontier of Long Video Generation  Standalone, inference-only release for minute-level multi-shot audio-video generation with a distilled DMD generator, paired cross-modal memory, and story-level consistency.

Update
----
* 2023.6.23 支持v2v模式，在first video 连入视频，以达成v2v的效果(ID保持一般)，注意中间帧最好有人物，注意第一句提示词的描述尽量跟参考视频内容一致（反推）Support v2v mode, connect the video to the first video to achieve v2v effect(normal ID keep), pay attention to the presence of characters in the mid frame, and try to match the description of the first prompt with the reference video content (reverse inference);  
* 2026.6.21 add a button to easy seltct json files /加了个选文件的按钮,稍微改了下流式卸载的逻辑
* 2026.6.8 新增多个swap卸载模式,支持多个层的加卸载,修复tile无法使用的问题/add sawp unloading mode, support multiple layers of add and unload, fix the problem that tile cannot be used; 
* 2026.6.6 新增TE的safetesor 支持，目前只支持t2v，i2v需要官方的1.5版模型，在训练了，等等
* 复现官方代码， 3050 6G即可 跑5分钟 848*512 故事板长视频，无任何字幕，拼接自然
* just need 6G Vram to infer 5 minutes long video ，no word

1.Installation  
----
  In the ./ComfyUI/custom_nodes directory, run the following:   
```
git clone https://github.com/smthemex/ComfyUI_JoyAI_Echo
```
2.requirements  
----
```
pip install -r requirements.txt
```
3.checkpoints 
----
  
dit/gguf :[JoyAI-Echo gguf or dit or clip ](https://huggingface.co/smthem/JoyAI-Echo-gguf)  
text_encoder/vae :[ltx2 text encoder vae audio vae...](https://huggingface.co/smthem/LTX-2.3-test-gguf)  

```
├── ComfyUI/models/diffusion_models/
|     ├── JoyAI-Echo-transformer.safetensors #optional 可选
├── ComfyUI/models/vae/
|     ├── ltx-2.3-22b-distilled_video_vae.safetensors
|     ├── ltx-2.3-22b-distilled_audio_vae.safetensors
├── ComfyUI/models/gguf/
|     ├── gemma-3-12b-it-qat-Q4_0.gguf 
|     ├──JoyAI-Echo-Q8_0.gguf
|     ├──JoyAI-Echo-Q6_K.gguf
├── ComfyUI/models/clip/ 
|     ├── gemma-3-12b-it-qat.safetensors #optional 可选
|     ├── connector.safetensors  # or 11 version
```

4 Example
----
![](example_workflows/i2v.png)
![](example_workflows/example.png)

5 Citation
-related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

```
@techreport{echo2026longvideo,
  title        = {JoyAI-Echo: Pushing the Frontier of Long Video Generation},
  author       = {{Echo Team @ Joy Future Academy, JD}},
  institution  = {Joy Future Academy, JD},
  year         = {2026},
  month        = {May}
}
```
