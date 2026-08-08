---
id: tool-07606
type: tool
area: 库
status: active
tags: [文风迁移, Ink, 协议宽松, 本地优先, 英文文档, 改稿润色, 本地写作]
title: ink-explorer
summary: 风格微调/文风迁移
source: https://github.com/wildwinter/ink-explorer
created: 2026-07-18
updated: 2026-07-18
no: 7606
category: 画龙补充 / 扩容入库 — 补充源
repo: wildwinter/ink-explorer
stars: 16
url: https://github.com/wildwinter/ink-explorer
tier: "B"
use_case: "风格微调/文风迁移"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: a5406db96a8238b5
  - methods/QUICK_START.md
---

# wildwinter/ink-explorer

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/wildwinter/ink-explorer
- **Stars**：16
- **语言**：Ink
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Allows runtime exploration of Ink and Dink stories
- **本地描述**：ink-explorer
- **拉取时间**：2026-07-25 19:27:04

related:
  - methods/QUICK_START.md
---

# Ink Explorer

**Ink Explorer** is a tool for visualizing and debugging [Ink](https://github.com/inkle/ink) stories. It allows you to explore the structure of your Ink code, play through it interactively, and inspect the state of your variables and visit counts in real-time.

![Ink Explorer Overview](https://github.com/wildwinter/ink-explorer/blob/main/doc/App.png)

## Features

### Graph View

Ink Explorer generates a visual node graph of your Ink story, starting with a Root node (which represents the entrypoint of the Ink) and shows Knots and Stitches and how they connect.

- **Interactive Graph**: Click nodes to navigate the graph. Drag nodes to rearrange them.
- **Minimap**: navigate large graphs easily.
- **Visit Highlights**: The graph automatically highlights the nodes that have been visited. The brighter the red, the more recently it has been visited.

### Live Ink

Play through your story interactively within the tool. You can start your playthrough from any node in the graph, as if you had set a particular knot or stitch path when you started the story.

- **Choice Handling**: Make choices just like in a game.
- **Step Back**: Undo your last step to explore different outcomes.
- **Restart**: Quickly restart the story from the beginning or a specific node.
- **Bonus Dink Support**: Automatic formatting for "Dink" style dialogue tags.

If you have **Follow** ticked, the graph will automatically centre and follow the node your story is currently on.

![Live Ink](https://github.com/wildwinter/ink-explorer/blob/main/doc/App.png)

### Code View

The code view shows the source code for any node in the graph.

You can toggle the code view off and on in the View menu.

- **Context Aware**: Click a node in the graph to see its source ink.
- **Follow Mode**: Automatically show the code for the current active node during playback.

![Code View](https://github.com/wildwinter/ink-explorer/blob/main/doc/CodeView.png)

### Variable Inspection

Inspect and edit global variables in real-time.

- **Search**: Filter variables by name.
- **Edit**: Modify variable values (Numbers, Strings, Booleans, Lists) on the fly to test different states.
- **Lists**: Full support for viewing and editing Ink Lists.

You need to have started a test for the variables to appear.

![Variables](https://github.com/wildwinter/ink-explorer/blob/main/doc/Variables.png)

### Visit Tracking

Track exactly how many times each knot and stitch has been visited.

- **Real-time Updates**: Counts update as you play.

![Visits](https://github.com/wildwinter/ink-explorer/blob/main/doc/Visits.png)

### States Management

Save and load the global variables and visit count of your story.

This is useful to take snapshots of a state to easily restore it, for testing.

- **Snapshots**: Capture the current story state (variables, path, visit counts).
- **Auto-Load**: Configure a state to automatically load when starting a test, effectively setting a "save point" for debugging.

![States](https://github.com/wildwinter/ink-explorer/blob/main/doc/States.png)

## Releases

You can find releases for various platforms [on the releases page](https://github.com/wildwinter/Ink-Explorer/releases).

## Usage

1. **Open an Ink File**: Use `File > Open...` to load your `.ink` file.
2. **Explore**: Use the graph to see the structure.
3. **Play**: Use the **Live Ink** tab to play through the story.
4. **Debug**: Use the **Variables** and **Visits** tabs to monitor state.

## Security Issues

### Note on Windows Security

Because this is a hobbyist project, this app is **currently not digitally signed*** for Windows. When you run the installer, Windows may show a blue "Windows protected your PC" box.

To install anyway:

1. Click "**More info**" on the blue popup.

2. Click "**Run anyway**".

Alternatively, you can right-click the .exe, select Properties, check the Unblock box at the bottom, and click OK.

For more details on why Windows shows this, see the [Official Microsoft SmartScreen Documentation](https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/).

\* *Because it costs a lot and seems to be impossible outside North America right now for individual developers. Thanks Microsoft!*

### Note on Mac Security

The app is signed. Because it's easier on Mac.

## Acknowledgements

Huge thanks to [Inkle](https://www.inklestudios.com/) for creating Ink, and to [Yannick Lohse](https://github.com/y-lohse) for `inkjs`.

This tool is built with Electron, amongst other things.

## License and Attribution

This is licensed under the MIT license - you should find it in the root folder. If you're successfully or unsuccessfully using this tool, I'd love to hear about it!

You can find me [on Medium, here](https://wildwinter.medium.com/).
