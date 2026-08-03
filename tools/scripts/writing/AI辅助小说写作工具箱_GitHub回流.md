# AI 辅助小说写作工具箱 · GitHub 项目回流

> 本文件是 `E:\小说\GitHub_相关项目清单.md`（79 批续搜、累计去重唯一仓库约 **1845** 个）的**方法库回流版**。
> 原始清单按批次平铺、重在「全」。本文件按**小说创作实际工作流 + 你的签约病灶**重排，只保留高价值 canonical 项，每条给「干什么 + 对流派写作的对口点」。
> 长尾与镜像/非代码仓请回原始清单查（各批章节含完整跳过理由）。
> 生成日期：2026-07-22。

## 怎么用这份工具箱

你的投稿被拒主因（番茄拒信原话）：**「开篇切入点吸引力不足、爽点不够、看点不足、AI味」**。
对应到工具，优先级最高的是：

| 病灶 | 直接对口工具类别 | 必看条目 |
|---|---|---|
| **AI 味重** | ① 去 AI 味（检测+改写）、② 鲁棒/对抗反向教材 | `harshaneel/humanize`、`ahans30/Binoculars`、`Moonlight-Syntax/LUNA` |
| **长篇崩、前后矛盾** | ③ 长篇不崩/多 Agent 框架、④ 长文本评测基准 | `unitagain/WenShape`、`THU-KEG/StoryWriter`、`Cuinnchen/saga` |
| **爽点不够、看点不足** | ⑥ 语料/爽点信号/读者反应、⑦ 写作质量评测 | `GOLEM-lab/Qidian_Webnovel_DataCollection`、`EQ-bench/creative-writing-bench` |
| **切入点弱（前 3 章）** | ③ 框架里的「大纲/钩子」、⑪ 平台抓取竞品 | `Clusm/AI_novel`（含爽点设计）、`HYL-Dave/WebNovelCrawler` |

> 引用约定：每条 `[owner/repo](链接)` 即原始 GitHub 仓。标注「HF/Modelscope」者为数据集卡，非代码仓但有训练价值。

---

## ① 去 AI 味（检测 + 改写）—— 直接对症被拒主因

### 检测（白盒，写作中实时把关）
| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [HendrikStrobelt/detecting-fake-text](https://github.com/HendrikStrobelt/detecting-fake-text) | GLTR：GPT-2 词概率排名颜色可视化，人类辨识 AI 准确率 54%→72% | 投稿前先跑一遍，定位「AI 腔」句子 |
| [baoguangsheng/fast-detect-gpt](https://github.com/baoguangsheng/fast-detect-gpt) | Fast-DetectGPT（ICLR'24 官方）：条件概率曲率零样本检测，比 DetectGPT 快 340× | 去 AI 味白盒检测首选，无需训练 |
| [Dylan-Harden3/PyDetectGPT](https://github.com/Dylan-Harden3/PyDetectGPT) | 开箱即用检测库：封装 FastDetectGPT/DetectLLM/LogRank/LogLikelihood 四法+CLI | 批量扫整本文稿 |
| [ahans30/Binoculars](https://github.com/ahans30/Binoculars) | Binoculars 官方 canonical（ICML'24 零样本，无需训练/阈值） | 去 AI 味检测基座 |
| [weberBen/Binoculars-CPU](https://github.com/weberBen/Binoculars-CPU) | Binoculars CPU 版：无 GPU 也能跑 | 本地低成本把关 |
| [cags9607/Binoculars-T4-gpu](https://github.com/cags9607/Binoculars-T4-gpu) | Binoculars T4 GPU 部署版：加速推理 | 大批量扫描 |
| [openai/gpt-2-output-dataset](https://github.com/openai/gpt-2-output-dataset) | OpenAI 官方 GPT-2 检测数据集 + roberta-base-openai-detector 源码 | 白盒溯源鼻祖/基准 |
| [SuwaidAslam/AI_Generated_Text_Checker_App](https://github.com/SuwaidAslam/AI_Generated_Text_Checker_App) | RoBERTa-base 检测器实战 App（Dash/Plotly），一键判 AI/人工 | 非技术向落地 |
| [RUI-LONG/ChatGPT-detector](https://github.com/RUI-LONG/ChatGPT-detector) | 中文 AI 文本检测器（perplexity+Streamlit） | 中文稿专用 |
| [johnsonwangzs/MGT-Mini](https://github.com/johnsonwangzs/MGT-Mini) | NLPCC'25 中文检测冠军（EnsemJudge），含前端可直接部署 | 中文检测最强方案 |
| [qy-guo/ai-detect](https://github.com/qy-guo/ai-detect) | 基于 Qwen1.5-7B 的 LoRA/QLoRA 中文检测 + GPT-5 拟人化对抗测试 | 中文+对抗鲁棒 |
| [candycca/aiotHW5](https://github.com/candycca/aiotHW5) | 深度诊断面板：RoBERTa + GPT-2 困惑度 + 突发度/TTR/齐夫律可视化 | 看「为什么像 AI」 |
| [yiqingzhang/gpt-detector](https://github.com/yiqingzhang/gpt-detector) | 微调 RoBERTa 检测器 + Flask REST API + 训练管线 | 可服务化接入写作流 |
| [MichaelShpyl/AI-Text-Detection-Tool](https://github.com/MichaelShpyl/AI-Text-Detection-Tool) | 上传文本即给 AI/人类概率的 Web 工具 | 轻量零样本把关 |
| [Moonlight-Syntax/LUNA](https://github.com/Moonlight-Syntax/LUNA) | LUNA（Language Understanding & Naturalness Assessment）：评估文本自然度/AI 痕迹 | 去 AI 味「自然度」新维度 |

### 改写 / 降 AI 率
| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [harshaneel/humanize](https://github.com/harshaneel/humanize) | 九杠杆去 AI 味：ai-check 文体学评分(0–27)+humanize 改写，50+ 文献，25 语域全过 | **最系统去 AI 味技能**，直接套用 |
| [brandonwise/humanizer](https://github.com/brandonwise/humanizer) | 29 种 AI 写作模式(500+ 词库)+突发度/TTR 统计，整库扫描排名 | 工程化批量把关 |
| [jiakecong0724/humanizer](https://github.com/jiakecong0724/humanizer) | 双语去 AI 味 Claude Code Skill，融合 blader/hardikpandya+Wikipedia 指南 | 中文稿改写 |
| [haibarazz/academic-humanize](https://github.com/haibarazz/academic-humanize) | 学术文本降 AI 率改写 | 议论文/解说向降味 |

### 鲁棒 / 对抗（反向教材：学「检测器怕什么」）
| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [GYK-CASIC/DAP](https://github.com/GYK-CASIC/DAP) | 动态对抗释义提升检测：检测器与生成器协同进化 | 理解对抗样本→别踩雷 |
| [Subangkar/cs577-project](https://github.com/Subangkar/cs577-project) | RADAR 鲁棒检测：混合回译+神经释义 vs PPO 释义器 | 释义攻击原理 |
| [CarlanLark/Robust-AIGC-Detector](https://github.com/CarlanLark/Robust-AIGC-Detector) | ACL'24 鲁棒检测器，含训练/攻击脚本 | 评测自己改写是否过关 |
| [ffhibnese/CoPA_Contrastive_Paraphrase_Attacks](https://github.com/ffhibnese/CoPA_Contrastive_Paraphrase_Attacks) | CoPA 对比释义攻击（EMNLP'25）：免训练绕过 Fast-DetectGPT | 「过度 paraphrasing」反而可疑 |
| [junchaoIU/DetectEval](https://github.com/junchaoIU/DetectEval) | DetectRL（NeurIPS'24）：多提示/人类修订/拼写扰动/混合攻击基准 | 改写鲁棒性自测 |
| [D-Diaa/MarkLLM](https://github.com/D-Diaa/MarkLLM) | 水印工具包+自适应攻击（释义规避>96%） | 水印机制认知 |
| [abehou/SemStamp](https://github.com/abehou/SemStamp) | 语义水印：抗释义攻击的 AI 文本检测 | 深层检测原理 |
| [multimodal-art-projection/COIG-P](https://github.com/multimodal-art-projection/COIG-P) | 中文偏好数据集 100 万对，DPO 对齐去 AI 味 | 训练自家自然度模型 |

---

## ② 长篇不崩 / 一致性 / 多 Agent 写作框架

| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [THU-KEG/StoryWriter](https://github.com/THU-KEG/StoryWriter) | 清华多智能体长篇框架（ICLR'25）：事件级大纲+章节规划+动态压缩历史，配 LONGSTORY 数据集 | **长篇不崩范本** |
| [MarioSigal/PLN-StoryWriter-](https://github.com/MarioSigal/PLN-StoryWriter-) | StoryWriter 开源实现，可训自己模型 | 落地复刻 |
| [unitagain/WenShape](https://github.com/unitagain/WenShape) | 文枢：多 Agent+动态事实表 Canon+BM25 上下文引擎+Token 预算+Git 存储 | **十万字级长篇不崩范本，最贴国产** |
| [Cuinnchen/saga](https://github.com/Cuinnchen/saga) | SAGA 知识图谱写作（LangGraph+Neo4j）：角色/地点/关系/事件图谱保一致 | 人物关系不崩 |
| [maplesugano/graphrag-narratology](https://github.com/maplesugano/graphrag-narratology) | GraphRAG 叙事增强：知识图谱组织情节/角色 | 长篇检索质量 |
| [kevinchcn/million-word-novel-ai-creator](https://github.com/kevinchcn/million-word-novel-ai-creator) | LangChain+DeepSeek 百万字系统：分层记忆+实时一致性检查 | 专治前后矛盾 |
| [ylc3000/AI-Novel-Writing-Assistant](https://github.com/ylc3000/AI-Novel-Writing-Assistant) | AI Native 长篇系统：Agent/世界观/写法引擎/RAG/反 AI 规则 | **最完整中文长篇生产链**，拆学「写法引擎」 |
| [ronghuaxueleng/Long-Novel-GPT](https://github.com/ronghuaxueleng/Long-Novel-GPT) | Long-Novel-GPT 增强版 v3.0：多 API/本地/动态配置/拆书 | 分层大纲生产 |
| [bodinggg/LangGraph-based-Novel-by-Agents](https://github.com/bodinggg/LangGraph-based-Novel-by-Agents) | LangGraph 多 Agent 小说生成 | 图编排写作 |
| [newyngwieslash-ops/novel_outline_with_langgraph](https://github.com/newyngwieslash-ops/novel_outline_with_langgraph) | LangGraph 大纲辅助：混合检索+知识图谱+版本快照 | 大纲+RAG |
| [xulingran/novel_outline_generator](https://github.com/xulingran/novel_outline_generator) | LLM 为文本生成大纲：WebUI/CLI/GUI，支持 OpenAI/Gemini/智谱 | 开书大纲 |
| [doudoubobo/BookWorld](https://github.com/doudoubobo/BookWorld) | 复旦 ICLR'25：从小说到可交互 Agent 社会（角色/地点/事件实例化） | 群像/世界构建 |
| [Clusm/AI_novel](https://github.com/Clusm/AI_novel) | 四 Agent（大纲优化师含爽点设计/人设守护/主写手/审校）+剧情圣经+番茄模式锚点 | **专治 OOC 与开篇拖沓** |
| [narcooo/inkos](https://github.com/narcooo/inkos) | Story Creation Agent 工作台：长篇/剧本/互动影游/多语翻译+可视化叙事画布 | 一站式创作台 |
| [llm-believer/wriagent](https://github.com/llm-believer/wriagent) | LangChain 写作助手：长期记忆+中英文流式协作 | 轻量助手 |
| [ARMANDSnow/make-ur-Agent-writer](https://github.com/ARMANDSnow/make-ur-Agent-writer) | 多 Agent 长篇续写 19 轮迭代，跑通《龙族》《冰火》风格 | 风格续写 |
| [MinYounZhang/MetaGPT_novels](https://github.com/MinYounZhang/MetaGPT_novels) | 基于 MetaGPT 中文小说 Agent：多角色协作自动产出标题/人设/大纲/章节 | 中文自动化流水线 |
| [GrannyProgramming/multi-agent-llm-novel-creation](https://github.com/GrannyProgramming/multi-agent-llm-novel-creation) | 单实例 Mistral-7B 多 Agent+Chroma 向量记忆 | 低成本本地 Agent |
| [raghvendra5688/Harry-Potter-Book-Writing-via-Multi-Agents](https://github.com/raghvendra5688/Harry-Potter-Book-Writing-via-Multi-Agents) | CrewAI 写书实例：OutlineCrew+每章 WriteBookChapterCrew | 模块化扩写模板 |
| [QSPBU-LONG/novel-multi-agents](https://github.com/QSPBU-LONG/novel-multi-agents) | OpenAI-Agent-SDK 五专家+Ollama 本地 qwen2.5:14b | 本地多 Agent |
| [sabeel111/Novatale](https://github.com/sabeel111/Novatale) | NovaTale：Gemini+LangGraph，概念→圣经→大纲→逐场 | 协作引擎 |
| [CuSO41108/flashnovel](https://github.com/CuSO41108/flashnovel) | flashNovel 章节级 Agent Runtime：context/plan/draft/.../checkpoint 结构化记忆 | 章节连续性 |
| [yh633/novel-agent](https://github.com/yh633/novel-agent) | 一键生成 10w 字+，多轮章节，作家风格模仿，状态保存 | 国产 LLM 方案 |
| [datacrystals/AIStoryWriter](https://github.com/datacrystals/AIStoryWriter) | AI 故事写作器 | 通用写作 |

---

## ③ 长文本一致性 / 写作质量评测基准

| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [google-deepmind/narrativeqa](https://github.com/google-deepmind/narrativeqa) | NarrativeQA 长篇阅读理解（4 万词+问答） | 长篇事实记忆基座 |
| [Azawp/DramaBench](https://github.com/Azawp/DramaBench) | 剧本续写六维评测：格式/叙事效率/人设一致/情感深度/逻辑/冲突 | 长篇剧情延续评测 |
| [cylnlp/booksum](https://github.com/cylnlp/booksum) | BookSum 书籍章节级摘要数据集+对齐 | 长篇结构化理解 |
| [tau-nlp/scrolls](https://github.com/tau-nlp/scrolls) | SCROLLS 长文本理解基准（7 任务统一） | 长篇推理/摘要基座 |
| [mingdachen/SummScreen](https://github.com/mingdachen/SummScreen) | SummScreen 剧本→recap 摘要 | 对话级情节抽取 |
| [nyu-mll/quality](https://github.com/nyu-mll/quality) | QuALITY+SQuALITY 长文多选 QA（须通读全文） | 长篇事实一致性 |
| [stanfordnlp/contract-nli-bert](https://github.com/stanfordnlp/contract-nli-bert) | ContractNLI 文档级 NLI+证据抽取 | 长文档推理参考 |
| [Yale-LILY/QMSum](https://github.com/Yale-LILY/QMSum) | QMSum 查询式会议摘要 | 长篇内容抽取 |
| [luyang-huang96/LongDocSum](https://github.com/luyang-huang96/LongDocSum) | GovReport 官方代码+高效注意力 | 万字级理解基座 |
| [lzhou1998/scrolls-for-longtext-models](https://github.com/lzhou1998/scrolls-for-longtext-models) | SCROLLS 基准实验代码（官方复刻） | 长篇模型实战 |
| [google/storybench](https://github.com/google/storybench) | 连续故事可视化基准：自动生成多帧故事图 | 漫画分镜参考 |
| [vistorybench/vistorybench](https://github.com/vistorybench/vistorybench) | ViStoryBench 角色跨/自相似性+风格相似+提示对齐 | 漫画/绘本角色一致性 |
| [HiWorld2024/ConStory-Bench](https://github.com/HiWorld2024/ConStory-Bench) | 长篇生成一致性基准：ConStory-Checker 检测 19 类矛盾 | 长篇矛盾自检 |
| [clchinkc/story-bench](https://github.com/clchinkc/story-bench) | Story Theory Benchmark：Hero's Journey/Save the Cat 评测 | 故事理论合规 |
| [EQ-bench/creative-writing-bench](https://github.com/EQ-bench/creative-writing-bench) | 创意写作评测 v3：32 提示×3 迭代，rubric+Elo | **写作质量打分榜** |
| [NousResearch/longform-writing-bench](https://github.com/NousResearch/longform-writing-bench) | 长篇小说写作评测：极简提示→8 章中篇 | 长文连贯评测 |

---

## ④ 角色立绘 / 漫画改编（IP 衍生变现）

| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [TencentARC/PhotoMaker](https://github.com/TencentARC/PhotoMaker) | PhotoMaker V2：堆叠 ID 嵌入秒级定制真人/角色，写实/漫画/动画风 | 封面/角色立绘固定 |
| [bytedance/InfiniteYou](https://github.com/bytedance/InfiniteYou) | 字节 InfiniteYou：FLUX ID 保持生成（InfuseNet） | 角色一致出图 |
| [Tencent/InstantCharacter](https://github.com/Tencent/InstantCharacter) | 腾讯混元 InstantCharacter：FLUX 单图免训练一致角色 | 连环画创作 |
| [showlab/OmniConsistency](https://github.com/showlab/OmniConsistency) | OmniConsistency：DiT 风格一致性 LoRA 插件 | 封面立绘固定 |
| [ali-vilab/ACE_plus](https://github.com/ali-vilab/ACE_plus) | ACE++（通义官方）：FLUX 指令式生成/编辑，免训练保角色一致 | 封面/分镜工程化 |
| [keyvez/ACE_plus](https://github.com/keyvez/ACE_plus) | ACE++ 社区镜像（同上） | 备用 |
| [tencent-ailab/IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) | IP-Adapter 官方：22M 轻量图像提示适配 | 角色固定底层 |
| [NVlabs/consistory](https://github.com/NVlabs/consistory) | 英伟达免训练角色/物品一致性文生图 | 故事书/漫画一致 |
| [ToTheBeginning/PuLID](https://github.com/ToTheBeginning/PuLID) | 字节 PuLID：对比对齐 ID 定制，高保真 | 角色立绘 |
| [InstantID/InstantID](https://github.com/InstantID/InstantID) | 单张人脸照秒级多风格人物 | IP 替代方案 |
| [smthemex/ComfyUI_StoryDiffusion](https://github.com/smthemex/ComfyUI_StoryDiffusion) | ComfyUI 故事一致性节点：集成 StoryMaker/PhotoMaker/PuLID/Consistory/IP-Adapter | 一键多角色叙事图 |
| [jianzongwu/DiffSensei](https://github.com/jianzongwu/DiffSensei) | 定制漫画生成：MLLM+扩散，掩码控多角色一致 | 漫画改编 |
| [jbilcke-hf/ai-comic-factory](https://github.com/jbilcke-hf/ai-comic-factory) | AI 漫画工厂：LLM+SDXL 一句话生成分镜 | 文本→漫画 |
| [Yutarop/comic-generator](https://github.com/Yutarop/comic-generator) | 一句话生成完整漫画：LLM 剧情+角色参考图保一致 | 几分钟出漫画 |
| [tiemka14/comic-gen](https://github.com/tiemka14/comic-gen) | 漫画生成训练管线：SD1.5+LoRA→Gradio | 自训漫画模型 |
| [Ramsi-K/agentic-comic-generator](https://github.com/Ramsi-K/agentic-comic-generator) | 多 Agent 漫画：分镜+对话+图像生成 | 小说转漫画工程化 |
| [PragyaVijay1222/Comicfy](https://github.com/PragyaVijay1222/Comicfy) | AI 漫画生成器：NLP 分镜+SD 逐场景出图 | 分镜落地 |
| [lambui/mangadex-dl](https://github.com/lambui/mangadex-dl) | MangaDex 下载器（Python 脚本） | 漫画素材抓取 |
| [mansuf/mangadex-downloader](https://github.com/mansuf/mangadex-downloader) | MangaDex 最完整下载器（PyPI 包） | 漫画素材抓取 |
| [L0g0rhythm/MDex](https://github.com/L0g0rhythm/MDex) | MangaDex 下载器（API→PDF） | 漫画素材抓取 |
| [Sydiepus/mangadex-py](https://github.com/Sydiepus/mangadex-py) | mangadex-py：v5 API 多线程下载 | 漫画素材抓取 |
| [Yui007/mangadex-extension](https://github.com/Yui007/mangadex-extension) | MangaDex 浏览器扩展 | 阅读/下载增强 |

---

## ⑤ 有声化（变现链路：有声书/播客）

| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [swivid/f5-tts](https://github.com/swivid/f5-tts) | ACL'25 流匹配零样本语音克隆，RTF≈0.15 | **有声书首选** |
| [hexgrad/kokoro](https://github.com/hexgrad/kokoro) | Kokoro 82M 轻量 TTS，多语免费商用，无需 GPU | 低门槛有声化 |
| [zai-org/GLM-TTS](https://github.com/zai-org/GLM-TTS) | 智谱全开源中文情感语音克隆（零样本/流式） | 中文有声书 |
| [xlzhen-940218/BookToAudiobook](https://github.com/xlzhen-940218/BookToAudiobook) | 小说转有声书：DeepSeek 分章+CosyVoice 多角色配音 | 整本有声小说 |
| [cosin2077/easyVoice](https://github.com/cosin2077/easyVoice) | 开源 TTS 超长文本多角色配音 | 小说级长文切分 |
| [shangyuok/alexandria-audiobook-gg](https://github.com/shangyuok/alexandria-audiobook-gg) | alexandria 有声书生成：文本→多角色 TTS | 整本有声书 |
| [cestella/tts_helper](https://github.com/cestella/tts_helper) | TTS 辅助：小说/长文转语音流水线 | 角色音色分配 |
| [garciadias/audify](https://github.com/garciadias/audify) | 文本转有声书（audify） | 自动可听内容 |
| [erlint1212/ai-transealtion-novel-to-anki-tts](https://github.com/erlint1212/ai-transealtion-novel-to-anki-tts) | AI 小说翻译+Anki 卡片+TTS | 译作+记忆卡+朗读 |
| [robert-clayton/audiobook](https://github.com/robert-clayton/audiobook) | 网文→有声书流水线：爬 RoyalRoad/ScribbleHub+Qwen3 TTS | 批量有声化 |
| [moc67331/EasyNovelAssistant](https://github.com/moc67331/EasyNovelAssistant) | 日语本地 LLM 生成+Style-BERT-VITS2 朗读 | 端到端离线写作+有声 |

---

## ⑥ 语料 / 爽点信号 / 读者反应（数据驱动写作）

| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [GOLEM-lab/Qidian_Webnovel_DataCollection](https://github.com/GOLEM-lab/Qidian_Webnovel_DataCollection) | 起点-Webnovel 语料：110 本+279 万中文/23 万英文评论，段落级读者反馈 | **爽点/追读预测数据** |
| [RUCAIBox/RecSysDatasets](https://github.com/RUCAIBox/RecSysDatasets) | 推荐系统数据集大全（GoodReads/Book-Crossing/Douban） | 小说推荐/爽点建模 |
| [acanois/ProjectWattpad](https://github.com/acanois/ProjectWattpad) | Wattpad 官方 API 数据分析：阅读量/投票/评论/情感趋势 | 跨文化读者偏好 |
| [jerry-chee/Navigating-Sensitivity](https://github.com/jerry-chee/Navigating-Sensitivity) | AO3 80 万+ works 的 kudos/预警标签 | 读者偏好/爽点信号 |
| [SimoneRebora/Wattpad_analysis](https://github.com/SimoneRebora/Wattpad_analysis) | Wattpad syuzhet 情感弧+评论网络分析 | 量化读者反应 |
| [shaido987/novel-dataset](https://github.com/shaido987/novel-dataset) | NovelUpdates 爬虫→24k+ 译作跨 8 语种元数据 | 网文语料+推荐信号 |
| [dragneel2074/Dataset](https://github.com/dragneel2074/Dataset) | Web-Novels-Dataset：NovelUpdates/Webnovel/Dreame/RoyalRoad 元数据 | 跨站题材/热度 |
| [tencent-ailab/GuoFeng-Webnovel](https://github.com/tencent-ailab/GuoFeng-Webnovel) | 腾讯×阅文多语言网文语料 14 类 | 中文预训练语料 |
| [hjzhao73/GenWebNovel](https://github.com/hjzhao73/GenWebNovel) | 中文网文实体识别语料（玄幻/历史 400 章） | 实体/世界观抽取 |
| [hjzhao73/MultiGenre-ChineseNovel](https://github.com/hjzhao73/MultiGenre-ChineseNovel) | 多类型中文小说 NER 语料库（260 部） | 多题材语料 |

---

## ⑦ 小语种 / 跨语 / 出海

| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [mmlong818/lightnovel-studio](https://github.com/mmlong818/lightnovel-studio) | 中日双语轻小说生成器（纯前端） | 双语草稿 |
| [parkwoo/gensou-ai](https://github.com/parkwoo/gensou-ai) | 日式小说助手：思维导图+设定一致 PWA | 日轻创作 |
| [kokardy/kakuyomu-cli](https://github.com/kokardy/kakuyomu-cli) | Kakuyomu（日本平台）命令行发布/下载 | 日站发布 |
| [MintoTsukino/claude-novel-workflow](https://github.com/MintoTsukino/claude-novel-workflow) | 日文轻小说 Canon 驱动多 Agent 工作流（70 章样例） | 日轻一致性 |
| [sail-sg/sailor-llm](https://github.com/sail-sg/sailor-llm) | Sailor 东南亚开源 LLM（印尼/泰/越/马来/老挝） | 小语种底座 |
| [OpenThaiGPT/openthaigpt](https://github.com/OpenThaiGPT/openthaigpt) | 泰语 13B LLaMA 续训+指令微调 | 泰语创作 |
| [soundstarrain/ko-lightnovels-clean](https://huggingface.co/datasets/soundstarrain/ko-lightnovels-clean) | 韩文轻小说清洗数据集（HF） | 韩文语料 |
| [soundstarrain/vi-lightnovels-clean](https://huggingface.co/datasets/soundstarrain/vi-lightnovels-clean) | 越南语轻小说清洗数据集（HF） | 越语语料 |
| [huseinzol05/malay-dataset](https://github.com/huseinzol05/malay-dataset) | 马来语语料大全（含 Wattpad 爬虫） | 马来语网文 |

---

## ⑧ 互动小说 / 游戏化叙事（支线 IP / 影游改编）

| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [inkle/ink](https://github.com/inkle/ink) | ink 叙事脚本引擎（80 Days/Heaven's Vault） | 分支叙事基座 |
| [inkle/inky](https://github.com/inkle/inky) | ink 官方可视化编辑器 | 写互动小说 |
| [inkle/ink-library](https://github.com/inkle/ink-library) | ink 资源总汇（引擎移植/编辑器/模板） | 生态入口 |
| [bemisguided/vscode-ink-language-tools](https://github.com/bemisguided/vscode-ink-language-tools) | VS Code Ink 扩展：高亮+大纲+实时编译+预览 | 编辑器内写作 |
| [wildwinter/ink-explorer](https://github.com/wildwinter/ink-explorer) | Ink Explorer：节点图+变量检视+试玩快照 | 调试利器 |
| [h3y6e/atom-ink](https://github.com/h3y6e/atom-ink) | atom-ink：Atom IDE Inky 替代 | 老牌环境 |
| [elliotherriman/catmint](https://github.com/elliotherriman/catmint) | Catmint：inkjs 实时测试器 | Web 开发调试 |
| [chromy/ink-proof](https://github.com/chromy/ink-proof) | ink-proof：编译器/运行时一致性测试套件 | 质量保障 |
| [dringz/inky-plus](https://github.com/dringz/inky-plus) | 增强版 Inky：多文件导航/跳转定义 | 可视化编写 |
| [furkleindustries/inklecate-node](https://github.com/furkleindustries/inklecate-node) | inklecate 的 Node.js 封装 | 工程化集成 |
| [KibaOfficial/Inky](https://github.com/KibaOfficial/Inky) | TypeScript 视觉小说引擎（Inky TS 移植） | 网页端互动落地 |
| [klembot/twine2](https://github.com/klembot/twine2) | Twine 2 互动小说引擎（节点连箭头，直出 HTML） | 零代码分支剧情 |
| [videlais/extwee](https://github.com/videlais/extwee) | Twee 解析/编译工具集 | 工程化流水线 |
| [HiEv/UInv](https://github.com/HiEv/UInv) | Twine/SugarCube 通用物品栏系统 | 游戏化道具 |
| [LockeBirdsey/TwET](https://github.com/LockeBirdsey/TwET) | Twine HTML→itch.io/GameJolt/Steam 可执行 | 互动小说分发 |
| [tweecode/twine](https://github.com/tweecode/twine) | Twine 1 原版源码 | 现代版见 klembot/twinejs |

---

## ⑨ 古籍 OCR / 标点 / 版面 / 古文 NLP（历史·年代文考据）

| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [Polo-Marco/HanDoc-OrderOCR](https://github.com/Polo-Marco/HanDoc-OrderOCR) | 中文文献 OCR+阅读顺序（竖排古文，AAAI'24） | 史料数字化 |
| [2287185537/Chinese-Ancient-OCR](https://github.com/2287185537/Chinese-Ancient-OCR) | 基于 PaddleOCR 的古籍识别（竖排+右到左排序） | PDF→TXT 批量 |
| [kakahuote1/Scrutario](https://github.com/kakahuote1/Scrutario) | 本地优先文言文 OCR/校对/全文检索桌面应用 | 多引擎包 |
| [Bignerdee/Jiayan](https://github.com/Bignerdee/Jiayan) | 甲言：古汉语 NLP（分词/词性/断句/标点） | 古文预处理 |
| [raynardj/yuan](https://github.com/raynardj/yuan) | 渊：古文自动断句+标点（BERT，附文白翻译） | 加标点 |
| [huangbo2024/XunziAP](https://github.com/huangbo2024/XunziAP) | 荀子大模型古籍自动断句标点 | 一键加标点 |
| [CiCistar/SBD](https://github.com/CiCistar/SBD) | 古文句读检测（BERT-CRF） | 句界切分 |
| [phyboy/LayoutSegmentation](https://github.com/phyboy/LayoutSegmentation) | 藏经版面划分与字切分 | 复杂版面 |
| [alephpi/24histories](https://github.com/alephpi/24histories) | 二十四史 OCR 全流程（YOLOv8+单字识别） | 古籍数字化范例 |
| [DaiHaoguang3151/ocr_fusion](https://github.com/DaiHaoguang3151/ocr_fusion) | 多 OCR 引擎融合工具箱 | 多场景比对 |
| [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | 智谱轻量 OCR(0.9B)，OmniDocBench 第一 | 边缘部署 |
| [Yuliang-Liu/MonkeyOCR](https://github.com/Yuliang-Liu/MonkeyOCR) | 轻量多模态文档解析(3B)，超 MinerU | 古书批量数字化 |
| [bensonchow123/ppocr-fine-tune](https://github.com/bensonchow123/ppocr-fine-tune) | PP-OCRv5 微调实操（3 卡训练） | 古籍识别落地 |
| [ftnfurina/giaa-train](https://github.com/ftnfurina/giaa-train) | GIAA OCR 炼丹（PP-OCRv5 det/rec 双阶段） | 古文字实战 |
| [NUC-Hong/DanQing](https://github.com/NUC-Hong/DanQing) | 丹青：古画修复/超分/上色 | 插图复原 |
| [qiaott/AncientPainitng2NaturalImage](https://github.com/qiaott/AncientPainitng2NaturalImage) | 古画转自然图像（CycleGAN） | 风格迁移 |

---

## ⑩ 写作 SFT / DPO 训练数据（自建风格模型）

| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [lemon07r/vellumforge2](https://github.com/lemon07r/vellumforge2) | VellumForge2 小说写作数据生成工具 | DPO 数据集流水线 |
| [lemon07r/VellumK2-Fantasy-DPO-Small-01](https://huggingface.co/datasets/lemon07r/VellumK2-Fantasy-DPO-Small-01) | 奇幻小说 DPO 数据集 1038 对（HF） | 风格对齐 |
| [lemon07r/VellumK2T-Fiction-DPO-Small-01](https://huggingface.co/datasets/lemon07r/VellumK2T-Fiction-DPO-Small-01) | 虚构 DPO 小数据集 333 对（HF） | 连贯叙事 |
| [crownelius/Creative_Writing_Multiturn_Enhanced](https://modelscope.cn/datasets/crownelius/Creative_Writing_Multiturn_Enhanced) | 中文创意写作多轮集 4312 对话（反 AI 陈词过滤） | 中文 SFT |
| [telecomadm1145/creative_writing](https://huggingface.co/datasets/telecomadm1145/creative_writing) | 中文轻小说指令集（CoT，HF） | 小说章节 SFT |
| [NousResearch/autonovel](https://github.com/NousResearch/autonovel) | 自主小说管线：种子→PDF/有声书/封面 | 全自动出版级 |
| [Zhao-yangyang/autonovel](https://github.com/Zhao-yangyang/autonovel) | 自主小说管线（modify-eval-keep 循环） | 同上镜像 |
| [Alex-Gurung/ReasoningNCP](https://github.com/Alex-Gurung/ReasoningNCP) | VR-CLI 可验证奖励训练长文推理 | 长文逻辑 |
| [PrimeIntellect-ai/creative_writing](https://github.com/PrimeIntellect-ai/creative_writing) | RL 创意写作环境：rubric 评分+奖励函数 | 偏好对齐 |
| [mozhu621/SuperWriter](https://github.com/mozhu621/SuperWriter) | 长文框架+7B 模型：Plan→Write→Refine+分层 DPO | WritingBench 8.51 |

---

## ⑪ 平台抓取与备份（自己的稿 / 竞品分析）

| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [HYL-Dave/WebNovelCrawler](https://github.com/HYL-Dave/WebNovelCrawler) | 网文爬虫（Selenium/Playwright stealth/HTTP 反爬） | 竞品/备份 |
| [Takishima/webnovel2epub](https://github.com/Takishima/webnovel2epub) | webnovel.com→EPUB（登录解锁+增量合并） | WebNovel 素材 |
| [DarkNacho/WebNovel-Scraper-Downloader](https://github.com/DarkNacho/WebNovel-Scraper-Downloader) | www.webnovel.com 小说 EPUB/漫画 PDF | 下载备份 |
| [ImagineBrkr/web-novel-scraper](https://github.com/ImagineBrkr/web-novel-scraper) | 网文爬虫（多平台 Webnovel/Wuxiaworld） | 多源抓取 |
| [felixApps/WattpadConnect-Python](https://github.com/felixApps/WattpadConnect-Python) | Wattpad 取正文/作者/元数据（免 API） | Wattpad 语料 |
| [TheOnlyWayUp/Wattpad-Py](https://github.com/TheOnlyWayUp/Wattpad-Py) | Wattpad 异步 API 封装（全类型标注） | 结构化采集 |
| [nianeyna/ao3downloader](https://github.com/nianeyna/ao3downloader) | AO3 批量下载（书签/元数据/正文/评论） | 同人备份 |
| [tertiary-stars/ao3-bulk-downloader](https://github.com/tertiary-stars/ao3-bulk-downloader) | AO3 批量下载+调度 | 多格式 |
| [fluteds/ao3-kindle](https://github.com/fluteds/ao3-kindle) | AO3 转 Kindle | 移动阅读 |
| [DreamCobbler/fiction-dl](https://github.com/DreamCobbler/fiction-dl) | 多平台 fiction 抓取→本地/EPUB | 离线文库 |
| [gochezkerrth/bulk-downloader](https://github.com/gochezkerrth/bulk-downloader) | FanFiction/AO3 类同人站批量下载 | 同人抓取 |

---

## ⑫ 完整流水线（端到端，一键出书）

| 仓库 | 一句话用途 | 对流派写作的对口 |
|---|---|---|
| [InitialXKO/dog-Engine](https://github.com/InitialXKO/dog-Engine) | 网文创作引擎：内置 AI 率检测，写作中实时提示 AI 痕迹 | **去 AI 味闭环** |
| [NousResearch/autonovel](https://github.com/NousResearch/autonovel) | 自主小说管线：世界/角色/大纲/声音→初稿→修订→导出 | 全自动出版 |
| [Zhao-yangyang/autonovel](https://github.com/Zhao-yangyang/autonovel) | 自主小说管线（modify-eval-keep 循环） | 同上 |

---

## 回流说明

- **来源**：`E:\小说\GitHub_相关项目清单.md`（79 批续搜，累计去重唯一仓库约 1845 个）。本文件为「按功能重排的高价值 canonical 子集」，非全量。
- **筛选原则**：跳过镜像/fork/非代码仓（HF 数据集卡、PyPI、arxiv、CSDN 博客），只留可直接服务于小说创作链的 canonical 项。
- **与签约病灶对应**：①去 AI 味、②长篇不崩、③爽点/读者信号、④角色漫改、⑤有声化、⑥语料——均直接指向你被拒的三类原因（AI味/爽点不足/切入点弱）。
- **维护**：原始清单每批续搜后，本文件的高价值项可随之增补；长尾请回原始清单按批次查。
