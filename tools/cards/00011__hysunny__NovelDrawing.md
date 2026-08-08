---
id: tool-00011
type: tool
area: 库
status: active
tags: [C#, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: NovelDrawing
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/hysunny/noveldrawing
created: 2026-07-18
updated: 2026-07-18
no: 11
category: 二、网文 / 长篇 AI 写作系统 库
repo: hysunny/NovelDrawing
stars: 9
url: https://github.com/hysunny/noveldrawing
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d929a045ac9217e1
  - methods/最强写作方法论_全球最强综合版.md
---

# hysunny/NovelDrawing

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/hysunny/noveldrawing
- **Stars**：9
- **语言**：C#
- **License**：None
- **Topics**：—
- **GitHub 描述**： Many people like reading novels, at the same time, most of these people have their own impression of the characters in novels. But due to lack of drawing skills, the impression can’t be drawn. Novel Drawing is a mobile application for novel lovers, of which the theme is novel, and of which the main line is drawing characters in the novel, and of which the purpose is to enrich public life. The application has the following features.        First of all, Novel Drawing is designed for drawing users’ favorite characters. Users can create characters according to the description of novels. The application can provide some models so that it will be easier to create wonderful works. Users can change the size of every part of the character to make it be more suitable. Besides, users can share their works with their friends use both this platform and some other platforms. And they can vote for works they like. At the same time, there could be some competitions to choose the most suitable characters. In addition, authors can use this platform to design some characters in their own novels. Authors can recommend works they like. This can help authors be more close to readers and help readers understand the novel. One of the most interesting parts is the DrawBar. It is the exclusive Post Bar for users. Users can communicate with other fans of the same novel. They can discuss with each other about the content, characters and story line of the novel. Users also can make friends whit similar interest through this platform.         Nowadays, there are some applications with single function, but none of these applications can combine entertainment with social contact. There are a few applications which focus on face production, but almost all of them lack social contact. The work for this competition can achieve the goal, and Novel Drawing is innovative and groundbreaking. In addition, the authors of the novels can use this application to communicate with the readers, and can use the application to create appropriate characters for fictions they write. When it comes to user experience, the application constructs a new way of social entertainment on the basis of interests. When it comes to technical design, the project will use some existing technologies for Windows. The Visual Studio 2013 will be the development tool. The system will run Windows Phone. When it comes to user interaction and visual design, we will do our best to seek professional. The project pursues high visibility, humane, simple and clear, natural and understandable interface to give a good impression for users.        In summary, Novel Drawing is a potential and innovative project which is feasible.
- **本地描述**：Many people like reading novels, at the same time, most of these people have their own impression of the characters in novels. But due to lack of drawing skills, the impression can’t be drawn. Novel Drawing is a mobile application for novel lovers, of which the theme is novel, and of which the main line is drawing characters in the novel, and of which the purpose is to enrich public life. The application has the following features.        First of all, Novel Drawing is designed for drawing users’ favorite characters. Users can create characters according to the description of novels. The application can provide some models so that it will be easier to create wonderful works. Users can change the size of every part of the character to make it be more suitable. Besides, users can share their works with their friends use both this platform and some other platforms. And they can vote for works they like. At the same time, there could be some competitions to choose the most suitable characters. In addition, authors can use this platform to design some characters in their own novels. Authors can recommend works they like. This can help authors be more close to readers and help readers understand the novel. One of the most interesting parts is the DrawBar. It is the exclusive Post Bar for users. Users can communicate with other fans of the same novel. They can discuss with each other about the content, characters and story line of the novel. Users also can make friends whit similar interest through this platform.         Nowadays, there are some applications with single function, but none of these applications can combine entertainment with social contact. There are a few applications which focus on face production, but almost all of them lack social contact. The work for this competition can achieve the goal, and Novel Drawing is innovative and groundbreaking. In addition, the authors of the novels can use this application to communicate with the readers, and can use the application to create appropriate characters for fictions they write. When it comes to user experience, the application constructs a new way of social entertainment on the basis of interests. When it comes to technical design, the project will use some existing technologies for Windows. The Visual Studio 2013 will be the development tool. The system will run Windows Phone. When it comes to user interaction and visual design, we will do our best to seek professional. The project pursues high visibility, humane, simple and clear, natural and understandable interface to give a good impression for users.        In summary, Novel Drawing is a potential and innovative project which is feasible.
- **拉取时间**：2026-07-23 22:39:11

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# NovelDrawing —— 画小说

> Imagine Cup 2015 参赛作品

### 1. 背景

现如今，阅读小说是广大中青年不可缺少的爱好之一。而每部小说中最不可缺的就是**人物角色**，每个人对人物角色的理解不一样，那么这个角色在每个人心目中的形象也都不一样。 

每个人都对小说中的人物角色形象有所想象，但目前大家也只是想象而已，有美术功底或是设计功底的可以手绘或用画图软件来将自己的**“想象”现实化**，可是大众们却不能。而且，每当有自己喜爱的小说被改编成影视作品时，广大群众的大多数反应都是“惨不忍睹”， 选角和自己心目中的角色形象相差太远，实为让人心碎。

比如： 很可能你心目中的小龙女可能是这样的（左图），但电视剧中的小龙女却是这样的（右图）

![示例1](https://github.com/hysunny/NovelDrawing/blob/main/materials/images/case1.png)

很可能你心目中的慕言可能是这样的（左图），但电视剧中的慕言却是这样的（右图）

![示例2](https://github.com/hysunny/NovelDrawing/blob/main/materials/images/case2.png)

因此，我们从自身出发，站在大众需求的角度，想做出一款服务于大众的产品，即给大家提供一个能“画”出“它”们的平台，用“傻瓜式“的操作，简单容易的就能”画“出心中所想。经过对以上问题的思考、细化和扩展，我们设计了这款**以绘制角色为主线，功能多样化的“画小说”移动应用软件**。

### 2. 产品的初步功能设计如下图:

![产品功能](https://github.com/hysunny/NovelDrawing/blob/main/materials/images/function.png)

主要功能有:

(1) “画“出心目中的小说角色(用五官、身体等部件拼接，也可拉伸扭转、放大缩小)

(2) 在线分享——晒出用户自己的“作品”、打赏自己喜爱的“ 作品”

(3) 官方定期举办评比会，用户可选出某部小说中最符合你心目中角色的形象

(4) 引进小说作者入驻，拉近与读者的距离

(5) 用户可自助建立“画吧”，讨论小说，分享自己的作品

(6) 结交“画友”，在线聊天

(7) 登录注册等功能

上述功能特点:

(1) `小说 + 拼脸`，创新融合——填补市场空白

(2) `兴趣 + 娱乐 + 社交`，产品功能综合 —— 打造一个小说爱好者的互动”天堂“

### 3. 产品适用场景

(1)小说爱好者阅读小说时，对小说中的人物角色形象有所”想象“，但因无绘画基础，无法 “画“出心中所想。

(2)小说爱好者想要找到与自己志同道合的人。

(3)小说作者想和自己的读者有近距离的交流。
