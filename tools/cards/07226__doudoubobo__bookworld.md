---
id: tool-07226
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: bookworld
summary: 多 Agent 协作自动产文
source: https://github.com/doudoubobo/bookworld
created: 2026-07-18
updated: 2026-07-18
no: 7226
category: 画龙补充 / 扩容入库 — 补充源
repo: doudoubobo/bookworld
stars: 0
url: https://github.com/doudoubobo/bookworld
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/QUICK_START.md
---

# doudoubobo/bookworld

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/doudoubobo/bookworld
- **Stars**：0
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：Official repo for BOOKWORLD: From Novels to Interactive Agent Societies for Story Creation
- **本地描述**：bookworld
- **拉取时间**：2026-07-25 19:14:45

related:
  - methods/QUICK_START.md
---

# BookWorld: Interactive Multi-Agent Story Creation System

<div align="center">

🖥️ [Project Page](https://bookworld2025.github.io/) | 📃 [Paper](https://arxiv.org/abs/2406.18921) | 🤗 [Demo](https://huggingface.co/spaces/alienet/BookWorld)

</div>




This is the official implementation of the paper "BOOKWORLD: From Novels to Interactive Agent Societies for Story Creation".

![Preview.png](<https://media-hosting.imagekit.io/14ce589aed514385/Preview.png?Expires=1840513142&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=oH~h5cUOwe3DjyDa86z40LBKpVanA81kQcGWubqjAa7SdiRWbYq2GIIF27urVYi4JK6u20IcmbRmoIxqkIQ1D-IBc9aMKcyVLJrjtlsvbaePOzgi-GtivxWIFuJvSzzuOfYmWF89KxzQ~EFsximhKJqtuw-WCZYRhpEFMUSuy42z-Lhv4ou6mWM58PIwzvsdc~rJxtMEXdaoxA9BGKKfcWD8mrhN8TI~mQzeRP-WE6KxHS9ib3MKES1BN9n5jLa4vEI5I2OwnzBFnc2iJ2vcyYgYRUY~1JF-ucYubMt85H2aWo9PUBYy38BYzodDdI0X8sKesL~evjstY5RH0buyCw__>)

## Introduction

BookWorld is a comprehensive system for social simulation in fictional worlds through multi-agent interactions. The system features:

- Scene-based story progression with multiple character agents
- Continuous updating of agent memories, status, and goals
- World agent orchestration of the simulation
- Support for human intervention and control
- LLM-based story generation and refinement

## Setup

### Step 1. Clone the repository
```bash
git clone https://github.com/your-repo/bookworld.git
cd bookworld
```

### Step 2. Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3. Configure Simulation Settings
- Update the configuration parameters in `config.json`:
  - `role_llm_name`: LLM model for character roles
  - `world_llm_name`: LLM model for world simulation
  - `config_path`: The path to the experiment
  - `if_save`: Enable/disable saving (1/0)
  - `scene_mode`: Scene progression mode
  - `rounds`: Number of simulation rounds
  - `mode`: Simulation mode ("free" or "script")

## Usage

### Step 1. Start the server
```bash
python server.py
```
or
```bash
uvicorn server:app --host 127.0.0.1 --port 8000  
```

### Step 2. Access the web interface
Open a browser and navigate to http://localhost:8000.

### Step 3. Interact with the system
- Start/pause/stop story generation
- View character information and map details
- Monitor story progression and agent interactions
- Edit generated content if needed

### Step 4. Continue from previous simulation
Locate the directory of the previous simulation within `/experiment_saves/`, and set its path to the `save_dir` field in `config.json`.

## Customization
### Construct Your Virtual World
1. Create the roles, map, worldbuilding following the examples given in `/data/`. You can improve the simulation quality by providing background settings about the world in `world_details/` or put character dialogue lines in `role_lines.jsonl`. Additionally, you can place an image named `icon.(png/jpg)` inside the character's folder — this will be used as the avatar displayed in the interface.
3. Enter the preset path to `preset_path` in `config.json`.

### Convert SillyTavern Character Cards to Role Data
1. Put your character cards in `/data/sillytavern_cards/`.
2. Run the script. It will convert all the cards into the role data that BookWorld needs.
```bash
python convert_sillytavern_cards_to_data.py
```
3. Input role codes of all the characters participating in this simulation to `role_agent_codes` in the preset file.

## Directory Structure

```
.
├── data/
├── frontend/
│   ├── assets/
│   ├── css/
│   └── js/
├── modules/
│   ├── db/
│   ├── llm/
│   ├── prompt/
│   ├── main_role_agent.py
│   └── world_agent.py
├── experiment_configs/
├── BookWorld.py
├── server.py
├── config.json
└── index.html
```


## Authors and Citation
**Authors:** Yiting Ran, Xintao Wang, Tian Qiu,
Jiaqing Liang, Yanghua Xiao, Deqing Yang.

```bibtex
@misc{ran2025bookworldnovelsinteractiveagent,
      title={BookWorld: From Novels to Interactive Agent Societies for Creative Story Generation}, 
      author={Yiting Ran and Xintao Wang and Tian Qiu and Jiaqing Liang and Yanghua Xiao and Deqing Yang},
      year={2025},
      eprint={2504.14538},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2504.14538}, 
}
```
## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).


##  Acknowledgements

- Fantasy Map: The background of map panel used in the frontend is from [Free Fantasy Maps](https://freefantasymaps.org/epic-world-cinematic-landscapes/), created by Fantasy Map Maker. This map is free for non-commercial use.

## Contact

BookWorld is a foundational framework that we aim to continuously optimize and enrich with custom modules. We welcome and greatly appreciate your suggestions and contributions!

If you have any suggestions or would like to contribute, please contact us at: ytran23@m.fudan.edu.cn

