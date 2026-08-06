---
id: tool-07186
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 中文友好, 本地写作]
title: chinese-poetry
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/chinese-poetry/chinese-poetry
created: 2026-07-18
updated: 2026-07-18
no: 7186
category: 画龙补充 / 扩容入库 — 补充源
repo: chinese-poetry/chinese-poetry
stars: 52876
url: https://github.com/chinese-poetry/chinese-poetry
tier: "S"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
  - methods/QUICK_START.md
---

# chinese-poetry/chinese-poetry

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/chinese-poetry/chinese-poetry
- **Stars**：52876
- **语言**：JavaScript
- **License**：MIT
- **Topics**：chinese, chinese-poetry, ci, json, poetry, tangshi
- **GitHub 描述**：The most comprehensive database of Chinese poetry 🧶最全中华古诗词数据库,  唐宋两朝近一万四千古诗人,  接近5.5万首唐诗加26万宋诗.  两宋时期1564位词人，21050首词。
- **本地描述**：chinese-poetry
- **拉取时间**：2026-07-25 19:13:27

related:
  - methods/QUICK_START.md
---

<p align="center">
  <a href="https://github.com/chinese-poetry/chinese-poetry">
      <img src="https://avatars3.githubusercontent.com/u/30764933?s=200&v=4" alt="chinese-poetry">
  </a>
</p>

<h2 align="center">chinese-poetry: 最全中文诗歌古典文集数据库</h2>

<p align="center">
  <a href="https://travis-ci.com/chinese-poetry/chinese-poetry" rel="nofollow">
    <img height="28px" alt="Build Status" src="https://img.shields.io/travis/chinese-poetry/chinese-poetry?style=for-the-badge" style="max-width:100%;">
  </a>
  <a href="https://github.com/chinese-poetry/chinese-poetry/blob/master/LICENSE">
    <img height="28px" alt="License" src="http://img.shields.io/badge/license-mit-blue.svg?style=for-the-badge" style="max-width:100%;">
  </a>
  <a href="https://github.com/chinese-poetry/chinese-poetry/graphs/contributors">
    <img height="28px" alt="Contributors" src="https://img.shields.io/github/contributors/chinese-poetry/chinese-poetry.svg?style=for-the-badge" style="max-width:100%;">
  </a>
  <a href="https://www.patreon.com/jackeygao" rel="nofollow">
    <img height="28px" alt="Patreon" src="https://img.shields.io/endpoint.svg?url=https%3A%2F%2Fshieldsio-patreon.vercel.app%2Fapi%3Fusername%3Djackeygao%26type%3Dpledges&style=for-the-badge" style="max-width:100%;">
  </a>
</p>


最全的中华古典文集数据库，包含 5.5 万首唐诗、26 万首宋诗、2.1 万首宋词和其他古典文集。诗人包括唐宋两朝近 1.4 万古诗人，和两宋时期 1.5 千古词人。数据来源于互联网。

**为什么要做这个仓库?** 古诗是中华民族乃至全世界的瑰宝，我们应该传承下去，虽然有古典文集，但大多数人并没有拥有这些书籍。从某种意义上来说，这些庞大的文集离我们是有一定距离的。而电子版方便拷贝，所以此开源数据库诞生了。此数据库通过 JSON 格式分发，可以让你很方便的开始你的项目。

古诗采集没有记录过程，因为古诗数据庞大，目标网站有限制，采集过程经常中断超过了一个星期。2017 年新加入全宋词，[全宋词爬取过程及数据分析](https://jackeygao.github.io/r/words/crawl-ci.html)。

## 高频词分析图

<details open>
  <summary><b>宋词受欢迎的词牌名</b></summary>

<div align="center">
<img src="https://raw.githubusercontent.com/jackeygao/chinese-poetry/master/images/ci_rhythmic_topK.png" alt="两宋喜欢的词牌名">
</div>
</details>

<details>
  <summary><b>宋词高频词</b></summary>
  <img src="https://raw.githubusercontent.com/jackeygao/chinese-poetry/master/images/ci_words_topK.png" alt="宋词高频词" style="max-width:100%;">
</details>

<details>
  <summary><b>宋词作者作品榜</b></summary>
  <img src="https://raw.githubusercontent.com/jackeygao/chinese-poetry/master/images/ci_author_topK.png" alt="宋词作者作品榜" style="max-width:100%;">
</details>

<details>
  <summary><b>唐诗高频词</b></summary>
  <img src="https://raw.githubusercontent.com/jackeygao/chinese-poetry/master/images/tang_text_topK.png" alt="唐诗高频词" style="max-width:100%;">
</details>

<details>
  <summary><b>唐诗作者作品榜</b></summary>
  <img src="https://raw.githubusercontent.com/jackeygao/chinese-poetry/master/images/tang_author_topK.png" alt="唐诗作者作品榜" style="max-width:100%;">
</details>

<details>
  <summary><b>宋诗高频词</b></summary>
  <img src="https://raw.githubusercontent.com/jackeygao/chinese-poetry/master/images/song_text_topK.png" alt="宋诗高频词" style="max-width:100%;">
</details>

<details>
  <summary><b>宋诗作者作品榜</b></summary>
  <img src="https://raw.githubusercontent.com/jackeygao/chinese-poetry/master/images/song_author_topK.png" alt="宋诗作者作品榜" style="max-width:100%;">
</details>

## 数据集

- [唐诗宋诗](https://github.com/chinese-poetry/chinese-poetry/blob/master/%E5%85%A8%E5%94%90%E8%AF%97)
- [全宋词](https://github.com/chinese-poetry/chinese-poetry/blob/master/%E5%AE%8B%E8%AF%8D)
- [五代·花间集](https://github.com/chinese-poetry/chinese-poetry/blob/master/%E4%BA%94%E4%BB%A3%E8%AF%97%E8%AF%8D/huajianji)
- [五代·南唐二主词](https://github.com/chinese-poetry/chinese-poetry/blob/master/%E4%BA%94%E4%BB%A3%E8%AF%97%E8%AF%8D/nantang)
- [论语](https://github.com/chinese-poetry/chinese-poetry/blob/master/%E8%AE%BA%E8%AF%AD)
- [诗经](https://github.com/chinese-poetry/chinese-poetry/blob/master/%E8%AF%97%E7%BB%8F)
- [幽梦影](https://github.com/chinese-poetry/chinese-poetry/blob/master/%E5%B9%BD%E6%A2%A6%E5%BD%B1)
- [四书五经](https://github.com/chinese-poetry/chinese-poetry/blob/master/%E5%9B%9B%E4%B9%A6%E4%BA%94%E7%BB%8F)
- [蒙学](https://github.com/chinese-poetry/chinese-poetry/blob/master/%E8%92%99%E5%AD%A6)
- [纳兰性德诗集](https://github.com/chinese-poetry/chinese-poetry/blob/master/%E7%BA%B3%E5%85%B0%E6%80%A7%E5%BE%B7)
- [御定全唐詩](https://github.com/chinese-poetry/chinese-poetry/blob/master/%E5%BE%A1%E5%AE%9A%E5%85%A8%E5%94%90%E8%A9%A9)


## 贡献

本项目目的是借助技术来生成格式化(JSON)数据，让开发者更方便快速的构建诗词类应用程序。身单力薄，欢迎更多人来维护，你可以通过以下方法来参与贡献：

- 直接提交 PR 或者通过 issue 讨论来优化完善此数据库，理论上古诗歌体非宗教类都欢迎加入，部分有争议性的数据需要社区投票讨论决定是否加入。关于诗句的纠错在创建 PR 时请标明出处。更多规范请[参考贡献规范文档](https://github.com/chinese-poetry/chinese-poetry/wiki/%E5%8F%82%E4%B8%8E%E8%B4%A1%E7%8C%AE%E8%A7%84%E8%8C%83)。

- 如果你没有办法直接参与完善的过程，你也可以通过 「[爱发电赞助](https://afdian.net/a/chinese-poetry)」  「[Patreon 周期性赞助](https://www.patreon.com/jackeygao)」 的形式来持续帮助并激励我去优化完善此数据库。如果您不喜欢周期性赞助，你也可以通过「[支付宝](https://github.com/jackeyGao/JackeyGao.github.io/blob/master/static/images/alipay.png)」或者「[微信赞赏码](https://github.com/jackeyGao/JackeyGao.github.io/blob/master/static/images/wechat.jpg)」进行一次性赞助(备注留下邮箱)。

- 如有建议或吐槽，欢迎联系我的邮箱 gaojunqi@outlook.com。

无论通过哪种形式贡献最终都会使之变得更好！

### 赞助者

无

### 贡献者

<p align="center">
<img src="https://opencollective.com/chinese-poetry/contributors.svg?width=890&button=false" alt="Contributors">
</p>

## 案例展示

<details>
  <summary>案例展示</summary>
  
- [中文诗歌主页](https://chinese-poetry.github.io)是一个基于浏览器的诗词网站，包含唐诗三百首、宋词三百首等文集。
- [animalize](https://github.com/animalize) **/** [QuanTangshi](https://github.com/animalize/QuanTangshi)  *离线全唐诗 Android*
- [justdark](https://github.com/justdark) **/** [pytorch-poetry-gen](https://github.com/justdark/pytorch-poetry-gen)  *a char-RNN based on pytorch*
- [Clover27](https://github.com/Clover27) **/** [ancient-Chinese-poem-generator](https://github.com/Clover27/ancient-Chinese-poem-generator)  *Ancient-Chinese-Poem-Generator*
- [chinese-poetry](https://github.com/chinese-poetry) **/** [poetry-calendar](http://chinese-poetry.github.io/poetry-calendar/)  *诗词周历*
- [chenyuntc](https://github.com/chenyuntc) **/** [pytorch-book](https://github.com/chenyuntc/pytorch-book/blob/master/chapter9-神经网络写诗(CharRNN)/) *简体唐诗生成(char-RNN)，可生成藏头诗，自定义诗歌意境，前缀等。*
- [okcy1016](https://github.com/okcy1016) **/** [poetry-desktop](https://github.com/okcy1016/poetry-desktop/) *诗词桌面*
- [huangjianke](https://github.com/huangjianke) **/** [weapp-poem](https://github.com/huangjianke/weapp-poem/) *诗词墨客 小程序版*
- [汉字之美](https://hz.xusenlin.com/) *汉字之美是一个方便查询的诗词网站，简洁干净，方便使用。*
- [PaddlePaddle](https://github.com/PaddlePaddle) **/** [PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP#%E4%BA%A4%E4%BA%92%E5%BC%8Fnotebook%E6%95%99%E7%A8%8B) *基于ERNIE-GEN(Transformer)的深度学习诗词生成，可自行修改逻辑来生成多种诗词风格。*
- [Harold-y](https://github.com/Harold-y) **/** [chinese-poetry-db-web](https://github.com/Harold-y/chinese-poetry-db-web) *基于本仓库的MySQL DB整合 + 诗词Web端展示与检索*
  
</details>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=chinese-poetry/chinese-poetry&type=Date)](https://star-history.com/#chinese-poetry/chinese-poetry&Date)

## License

[MIT](https://github.com/chinese-poetry/chinese-poetry/blob/master/LICENSE) 许可证。
