---
id: tool-00768
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: sakkanoheya
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/daegunkor/sakkanoheya
created: 2026-07-18
updated: 2026-07-18
no: 768
category: 二、网文 / 长篇 AI 写作系统 库
repo: daegunkor/sakkanoheya
stars: 0
url: https://github.com/daegunkor/sakkanoheya
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# daegunkor/sakkanoheya

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/daegunkor/sakkanoheya
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A novel sharing site with Helper tools that help writing the novel.
- **本地描述**：A novel sharing site with Helper tools that help writing the novel.
- **拉取时间**：2026-07-23 23:01:26

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---



<p align="center"><img src="./readmeImg/sakkanoheyaHeader.jpg"></p>

<span  style='color:#F73A3A; font-weight:bold; font-size:18px;'>プロジェクト名｜</span>
<span class='content'>作家の部屋 http://sakkanoheya.com/ </span>

<span class='subject'>開発期間 / 開発人員｜</span>
<span class='content'>2017. 5. 16 ~ 2017. 8. 25( ３ヶ月 ) 　/　 6人</span>

<span class='subject'>開発環境｜</span>
<span class='content'>Laravel(PHP MVCFramwork), JavaScript, jQuery, D3.js,
 	       HTML5, CSS3, Bootstrap
</span>

<span class='subject'>概要｜</span>
<span class='content'>アマチュア小説作家の執筆を手伝うヘルパーツールを備えている
小説共有サイト。<br>
小説の内容は多数の事件で構成され、事件は「人物、事物、場所」の影響で作られる。このサービスでは<span class='highlite'>背景設定部分</span>で事件を定義し、事件に基づいて<span class='highlite'>執筆部分</span>で小説の内容を作成。

<span class='subject'>担当</span><br>
<span class='sub-subject'>1. 背景設定部分の人物相関図（ D3.js )</span><br>
<a href='https://github.com/daegunkor/sakkanoheya/blob/master/app/Http/Controllers/RelationController.php'>CONTROLLER : app/Http/Controllers/RelationController.php</a><br>
<a href='https://github.com/daegunkor/sakkanoheya/tree/master/resources/views/background/relationship'>VIEW : resources/views/background/relationship</a>

<span class='sub-subject'>2. 地図作成ツール（ D3.js )</span><br>
<a href='https://github.com/daegunkor/sakkanoheya/blob/master/app/Http/Controllers/MapController.php'>CONTROLLER : app/Http/Controllers/MapController.php</a><br>
<a href='https://github.com/daegunkor/sakkanoheya/tree/master/resources/views/background/map'>VIEW : resources/views/background/map</a>

<span class='sub-subject'>3. 執筆部分のエディター  ( jQuery )</span><br>
<a href='https://github.com/daegunkor/sakkanoheya/blob/master/app/Http/Controllers/writeNovelController.php'>CONTROLLER : app/Http/Controllers/writeNovelController.php</a><br>
<a href='https://github.com/daegunkor/sakkanoheya/tree/master/resources/views/write_novel'>VIEW : resources/views/write_novel</a>


<span class='subject'>サービスの流れ</span>
<p align="center"><img src="./readmeImg/serviceFlow.jpg"></p>

<span class='subject'>主なサービス</span>
<p align="center"><img src="./readmeImg/main_func.jpg"></p>
