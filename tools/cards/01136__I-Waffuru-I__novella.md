---
id: tool-01136
type: tool
area: 库
status: active
tags: [Rust, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: novella
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/i-waffuru-i/novella
created: 2026-07-18
updated: 2026-07-18
no: 1136
category: 二、网文 / 长篇 AI 写作系统 库
repo: I-Waffuru-I/novella
stars: 1
url: https://github.com/i-waffuru-i/novella
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 388841f692680cff
  - methods/最强写作方法论_全球最强综合版.md
---

# I-Waffuru-I/novella

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/i-waffuru-i/novella
- **Stars**：1
- **语言**：Rust
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A simple declarative creative writing formatting tool.
- **本地描述**：A simple declarative creative writing formatting tool.
- **拉取时间**：2026-07-23 23:12:10

---


<div align="center"> 
<h1>Novella</h1>
<i>A simple declarative narrative writing tool.</i>
</div>
<br />

Write your story as a text file with inline tags, run it through *Novella* and receive a *pdf* as output with all decorations applied. This is a convenience tool made to facilitate the writing of narrative stories and exporting them easily. 

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- 
The project started as a way to provide customization options for styling text. I'm a fan of adding colourization to characters, tying in with their personality & vibe. When a story stretches on for hundreds of pages, adding the colour each time is a redundant and error-prone task. Even worse, deciding the colour of one character doesn't match anymore, and needing to update it *everywhere* in the document. Not cool.

This self-made problem is solved by this self-made solution :)

> This project is far from complete, but the core functionality is present. I intend to revamp a lot of tags to Markdown-like notation, as it's more intuitive, plus expanding the features available.

## Installation
Currently, the only way to install *Novella* is to build it from source. This will require the Rust toolchain to be installed on your device, as `cargo` is used.
1. Clone this repository
2. Move into the directory
3. run `cargo build --release`
4. The executable will be located at `./target/release/novella`, which you can move where you want, or add to your PATH. 


## Documentation 

Here is [an example story file](examples/park_walk.txt), the features of which I'll explain as we go.

```
# character definitions
bob;120;40;130
mom;40;10;10
gd;40;10;10

# delimiter
$$STORY$$

# narration
The leaves fell out the tree, a choir of silent deaths. Wind scurries past the branches in chaotic yet arrhythmic fashion.
# dialogue
bob;It sure is cold today!
mom;You're right! Luckily we brought our jackets with us.

$sb

In the distance, a security guard walks into view and makes his way to the duo.
gd;Hello there, I was wondering if you two are sufficiently prepared for the cold weather up ahead. I'm telling ya, there might even be snow soon. $bsSnow$be, in this day and age?!
mom;Oh yes, thank you $isvery$ie much. We brought everything we need.
bob;Yes sir.$asBobby takes something out of their bag.$ae We even have gloves.
```

Every story file starts with character definitions. These are characters in the story that talk and act (and sometimes even think!). 
Each character definition features a shorthand name and the rgb-value for the wanted colour. For example, the line `bob;120;40;130` defines an abbreviation string we can use when Bobby talks. 
> For now, these abbreviated names must be 2-3 chars long, but this may change later. 

`$$STORY$$` is a delimiter that splits the file in two. Everything before it counts as 'setup', while everything after is the 'story'. You can omit this if no characters are defined.

Next comes the story itself. Every line results in a text block in the final output. A line can either be narrated or dialogue. The latter is defined by the character short name appearing at the start. If no character is mentioned at the start, Novella treats it as a narration line. Inline tags are handled in both cases.

The default character to start a tag is `$`. This can be changed by providing the `-o` argument 
Styling tags are delimited by a **s**tart tag and **e**nd tag. Currently supported tags are:
- `as & ae`: Insert narration within a dialogue line 
- `is & ie`: Makes the text italic
- `bs & be`: Makes the text bold
- `ss & se`: Makes the font size smaller
- `fs & fe`: Starts a "flashback" section, in which text colour is more pale.

There are a few 'Spacing' tags to play with empty spaces between paragraphs. When any of these are used, the line should be empty, safe for the tag.
- `lb`: A long horizontal bar, often used to signify a long jump in time or new chapter
- `sb`: A short horizontal bar, used moreso to detail a shorter flash forward 
- `nl`: Leaves a vertical space between the lines
- `ns`: Leaves a smaller vertical space between the lines

Empty lines and lines starting with `#` (comments) are ignored and won't make any difference on the output.



