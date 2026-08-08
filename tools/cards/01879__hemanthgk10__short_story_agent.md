---
id: tool-01879
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议未明, 需API密钥, 英文文档]
title: short_story_agent
summary: 多 Agent 协作自动产文
source: https://github.com/hemanthgk10/short_story_agent
created: 2026-07-18
updated: 2026-07-18
no: 1879
category: 二、网文 / 长篇 AI 写作系统 库
repo: hemanthgk10/short_story_agent
stars: 1
url: https://github.com/hemanthgk10/short_story_agent
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: ffc8930e04700d0c
  - methods/最强写作方法论_全球最强综合版.md
---

# hemanthgk10/short_story_agent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/hemanthgk10/short_story_agent
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Generate 120s+ story scripts designed as AI video generator instructions. Each line includes narration, character details, and background context to help you produce scene-accurate video clips.
- **本地描述**：Generate 120s+ story scripts designed as AI video generator instructions. Each line includes narration, character details, and background context to help you produce scene-accurate video clips.
- **拉取时间**：2026-07-23 23:33:46

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# short_story_agent (CrewAI)

Generate 120s+ story scripts designed as AI video generator instructions. Each line
includes narration, character details, and background context to help you produce
scene-accurate video clips.

## Features
- 120s+ narration guaranteed via minimum word count
- Scene-by-scene JSON output
- Character look, expression, and clothing per line
- Background and context per line
- Simple CLI inputs for genre, theme, and setting

## Setup

1) Create a virtual environment (optional):
```bash
python -m venv .venv
source .venv/bin/activate
```

2) Install dependencies:
```bash
pip install -r requirements.txt
```

3) Provide your API key:
```bash
export OPENAI_API_KEY="your_key_here"
```

Optional:
```bash
export CREWAI_TESTING="true"
```

## Run

```bash
python -m src.main --genre "mystery" --theme "lost artifact" --setting "rainy coastal town"
```

The API base URL defaults to `https://api.openai.com/v1`. If you need to override it:
```bash
python -m src.main --openai-base-url "https://api.openai.com/v1"
```

You can also control duration and scene count:
```bash
python -m src.main --duration-min 120 --max-scenes 14
```

## Sample Output

Command:
```bash
python -m src.main --genre "mystery" --theme "lost artifact" --setting "rainy coastal town"
```

Example output (truncated for brevity):
```text
python -m src.main --genre "mystery" --theme "lost artifact" --setting "rainy coastal town"

2026-02-04 22:16:30,557 INFO short_story_agent [main.py:192] Starting story generation
2026-02-04 22:16:44,268 INFO httpx [_client.py:1025] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2026-02-04 22:16:44,279 INFO root [completion.py:1657] OpenAI API usage: {'prompt_tokens': 253, 'completion_tokens': 534, 'total_tokens': 787}
2026-02-04 22:17:25,326 INFO httpx [_client.py:1025] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2026-02-04 22:17:25,329 INFO root [completion.py:1657] OpenAI API usage: {'prompt_tokens': 832, 'completion_tokens': 1719, 'total_tokens': 2551}
2026-02-04 22:18:12,615 INFO httpx [_client.py:1025] HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2026-02-04 22:18:12,622 INFO root [completion.py:1657] OpenAI API usage: {'prompt_tokens': 4606, 'completion_tokens': 2216, 'total_tokens': 6822}
2026-02-04 22:18:12,633 INFO short_story_agent [main.py:217] Story generated successfully
2026-02-04 22:18:12,633 INFO short_story_agent [main.py:218] Output saved to outputs/story_20260204_221812.json
{
  "title": "Secrets of the Lighthouse",
  "duration_seconds_min": 120,
  "scenes": [
    {
      "line": 1,
      "narration": "In the small, rain-soaked town of Grayhaven, whispers of a lost artifact hung in the mist, intertwining with tales of long-forgotten sailors and mystical treasures.",
      "characters": [],
      "background": "A bleak town shrouded in mist with rain falling on cobblestone streets, flickering street lamps casting ghostly shadows.",
      "context": "Setting the atmospheric tone of Grayhaven, suggesting a rich, mysterious past intertwined with local lore.",
      "camera": "Wide shot capturing the misty streets, rain pelting down against the cobblestones."
    },
    {
      "line": 2,
      "narration": "Every evening, the old lighthouse shone its beam across the stormy waves, a relic of the past holding secrets within its weathered walls, casting long shadows on the rocky shore.",
      "characters": [],
      "background": "A rugged coastline with crashing waves and a luminous lighthouse standing defiantly against the dark sky.",
      "context": "Emphasizing the lighthouse as a pivotal visual element, a guardian of the town's mysteries.",
      "camera": "Medium shot focused on the lighthouse, illuminating the tumultuous waves at its base."
    },
    {
      "line": 3,
      "narration": "When local historian Clara stumbled upon a faded map in the town archives, her curiosity ignited a flame for adventure and the promise of uncovering hidden truths.",
      "characters": [
        {
          "name": "Clara",
          "appearance": "A woman in her late 30s with shoulder-length brown hair and round spectacles, exuding an air of intellect.",
          "expression": "A look of excitement and eager curiosity in her eyes.",
          "clothing": "Wearing a cozy, oversized sweater and worn jeans, with a satchel slung over her shoulder, hinting at her scholarly pursuits."
        }
      ],
      "background": "An old town archive filled with dusty books, ancient artifacts, and declining sunlight streaming through the windows.",
      "context": "Clara discovers an important clue about the lost artifact that could change everything.",
      "camera": "Close-up of Clara's face, then panning to the old, tattered map she's holding, revealing intricate details."
    },
    {
      "line": 4,
      "narration": "The map hinted at a treasure buried deep within the cliffs, said to be protected by the spirits of sailors long lost, their voices echoing through time.",
      "characters": [],
      "background": "The map spread out on a weathered wooden table, with sketches of cliffs, waves, and cryptic symbols hinting at danger.",
      "context": "Illustrating the treasure's location while deepening the legend that surrounds it, hinting at the supernatural.",
      "camera": "Overhead shot of the map, focusing on watercolor markings that indicate potential locations of the treasure."
    },
    {
      "line": 5,
      "narration": "Clara ventured out into the storm one fateful night, her determination unwavering as the rain lashed at her face, embodying the very spirit of adventure.",
      "characters": [
        {
          "name": "Clara",
          "appearance": "Clara with her hair plastered to her forehead, determined eyes reflecting the storm's fury.",
          "expression": "A fierce look of resolve, undeterred by the elements.",
          "clothing": "Wearing a waterproof raincoat and sturdy boots, water droplets glistening like jewels on her skin."
        }
      ],
      "background": "A dark, stormy night with heavy rain and wind whipping through the trees, lightning illuminating the sky in brief flashes.",
      "context": "Clara embarks on her perilous journey to find the artifact, the storm reflecting the turmoil she feels inside.",
      "camera": "Tracking shot following Clara as she walks determinedly against the wind and rain, illuminated by lightning."
    },
    {
      "line": 6,
      "narration": "With only the flickering light of the lighthouse to guide her, she navigated treacherous paths along the rocky coast, each step resonating with the weight of the legends.",
      "characters": [
        {
          "name": "Clara",
          "appearance": "Clara appears focused and sharpened by the elements, her eyes scanning for danger.",
          "expression": "A concentrated expression, bracing against the relentless wind and rain.",
          "clothing": "Still in her raincoat, with her map tightly clutched in her hands as she walks carefully."
        }
      ],
      "background": "Rocky coastline illuminated sporadically by the beam of the lighthouse sweeping across the tumultuous waves.",
      "context": "Clara carefully navigates the unstable terrain, grappling with the weight of the stones and her own anticipation.",
      "camera": "Wide shot showing Clara\u2019s small figure against the vast, rugged coast, with waves crashing fiercely."
    },
    {
      "line": 7,
      "narration": "As she reached the cliff\u2019s edge, an eerie hush fell over the landscape, and she sensed a shiver crawl down her spine as she realized she was not alone.",
      "characters": [
        {
          "name": "Clara",
          "appearance": "Clara standing at the cliff, her silhouette outlined against the dim light, looking around cautiously.",
          "expression": "A sudden look of apprehension, as if she can feel eyes watching her.",
          "clothing": "Her raincoat still on, water continuing to drip from her hair, mingling with the rain."
        }
      ],
      "background": "The edge of a cliff overlooking tumultuous waves below, fog rolling in ominously and enveloping the scenery.",
      "context": "Clara begins to sense supernatural elements in the air, making her feel vulnerable yet intrigued.",
      "camera": "Close-up of Clara's face, capturing her apprehension before shifting to the ominous cliff surroundings cloaked in mist."
    },
    {
      "line": 8,
      "narration": "A figure emerged from the shadows, cloaked in mystery, warning her to leave before the tide came in, their voice barely a whisper among the crashing waves.",
      "characters": [
        {
          "name": "Mysterious Figure",
          "appearance": "A tall figure draped in a dark, tattered cloak, features hidden within the shadows, exuding an aura of foreboding.",
          "expression": "A stern and warning look, eyes glinting with knowledge of the peril ahead.",
          "clothing": "Clothing is frayed, dark, and ethereal, blending seamlessly into the shadows of the night."
        }
      ],
      "background": "A shadowy area near the cliff, with swirling mist thickening the air and the sound of roaring waves echoing in the distance.",
      "context": "The mysterious figure tries to thwart Clara\u2019s quest, emphasizing the danger of the approaching tide.",
      "camera": "Medium shot of the figure emerging from the shadows, with Clara in the foreground looking shocked and wary."
    },
    {
      "line": 9,
      "narration": "But Clara's resolve was stronger than her fear, and she pressed on, driven by the lore of the rumored artifact that had drawn countless adventurers before her.",
      "characters": [
        {
          "name": "Clara",
          "appearance": "Clara standing resolute once more, her fists clenched and eyes ablaze with determination.",
          "expression": "Determined and courageous, embodying unyielding spirit.",
          "clothing": "Her raincoat worn, still protecting her as she stands firm against the gale."
        }
      ],
      "background": "Back at the cliff's edge, dark clouds gathering above, nature roaring in response to her defiance.",
      "context": "Clara chooses to face her fears head-on, resolving to continue her journey despite warnings.",
      "camera": "Close-up of Clara\u2019s face showing unrelenting determination, with the cliff's edge imprinted in the background."
    },
    {
      "line": 10,
      "narration": "Finally, she discovered a hidden cave, its entrance concealed by cascading waves and swirling fog, inviting yet foreboding.",
      "characters": [],
      "background": "A dark and mysterious cave entrance, partially hidden by jagged rocks and mist swirling like ghosts.",
      "context": "Clara finds the secret entrance to the cave, the culmination of her quest thus far, leaving her breathless.",
      "camera": "Wide shot capturing the cave entrance, waves crashing nearby, sending water splashing at its threshold."
    },
    {
      "line": 11,
      "narration": "Inside, amidst glimmering stones and ancient relics, the lost artifact shimmered with an almost magical brilliance, a beacon of history and power.",
      "characters": [],
      "background": "The dim interior of the cave, illuminated by sparkling stones scattered around, reflecting light and flickering shadows.",
      "context": "The cave reveals itself as a treasure trove of historical marvels, the artifact being the crowning jewel.",
      "camera": "Pan shot inside the cave, emphasizing the glimmering treasures, finally honing in on the artifact itself."
    },
    {
      "line": 12,
      "narration": "As she reached for it, the earth trembled beneath her, and the whispers of the past grew louder, revealing the true cost of uncovering the town's hidden secrets long buried.",
      "characters": [
        {
          "name": "Clara",
          "appearance": "Clara's hand outstretched toward the artifact, her eyes wide with a mix of awe and fear.",
          "expression": "A captivating blend of wonder and trepidation.",
          "clothing": "Her raincoat hanging open, exposing the determination that surged within her."
        }
      ],
      "background": "The cave illuminated now, shadows dancing chaotically with the shifting light, creating an eerie spectacle.",
      "context": "Clara faces the consequences of her discovery as the atmosphere grows thick with suspense and anticipation.",
      "camera": "Close-up of Clara\u2019s hand reaching toward the artifact, followed by a wide shot revealing the trembling cave around her."
    }
  ]
}
```

## Output

The output is printed to stdout and also saved in `outputs/` as a JSON file.

Example schema:
```json
{
  "title": "Title here",
  "duration_seconds_min": 120,
  "scenes": [
    {
      "line": 1,
      "narration": "Single sentence narration.",
      "characters": [
        {
          "name": "Ava",
          "appearance": "late 20s, short hair, calm demeanor",
          "expression": "curious, focused eyes",
          "clothing": "yellow raincoat, black boots"
        }
      ],
      "background": "foggy harbor with a dim lighthouse",
      "context": "Ava arrives at the docks just before dusk.",
      "camera": "medium shot, slow push-in"
    }
  ]
}
```

## Notes
- Each `narration` is a single sentence intended as a voiceover line.
- The model enforces minimum word count to achieve at least 120 seconds.
