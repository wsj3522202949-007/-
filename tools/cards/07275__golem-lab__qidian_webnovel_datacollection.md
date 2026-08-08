---
id: tool-07275
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 本地写作]
title: qidian_webnovel_datacollection
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/golem-lab/qidian_webnovel_datacollection
created: 2026-07-18
updated: 2026-07-18
no: 7275
category: 画龙补充 / 扩容入库 — 补充源
repo: golem-lab/qidian_webnovel_datacollection
stars: 4
url: https://github.com/golem-lab/qidian_webnovel_datacollection
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: e1f66767146e2603
  - methods/QUICK_START.md
---

# golem-lab/qidian_webnovel_datacollection

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/golem-lab/qidian_webnovel_datacollection
- **Stars**：4
- **语言**：Jupyter Notebook
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：qidian_webnovel_datacollection
- **拉取时间**：2026-07-25 19:16:19

related:
  - methods/QUICK_START.md
---

# Qidian-Webnovel-Corpus

A brief introduction to the **Qidian-Webnovel** Corpus. https://doi.org/10.34894/GQXX3K

The corpus creation process involved a manual search for translated novels available on **Webnovel.com** within the **NOVEL** category, only targeting **completed works**.

Subsequently, each identified translated novel was mapped with its original counterpart on **Qidian.com**. 

As a result, we got 120 novels (from which 10 of these novels' license on Qidian.com had expired, so ther was no data for this 10 novels on Qidian). 

The final corpus consists of **110** novels, and all the reader comments and replies to the novels. (Timestamp 01/09/2024)

Comments and replies are catergorised by **book-level**, **chapter-level** and **paragraph level**, and stored by per novel.

We also collected the user profiles of readers who has left comments or replies on the novels. 
**We only collect personal data that are necessary for the purpose of the scientific research, and strictly abid by the EU GDPR.**

Only metadata are openly available. User comments can be access after signing a Data Trransfer Agreement (see below).

**About the data**

- **bookList**

  - This csv file contain the mapping link for the same story published on both qidian and webnovel. The final corpus consists of 110 stories. According to WebNovel’s categorisation visible on the website interface, these 110 stories consist of 103 Male Lead and 7 Female Lead. 

- **qidianFreeChapterDates**

  - This zip file contains CSV files, each named by its corresponding Qidian bookID. Each CSV file contains the publication dates for all free available chapters of that story in the dataset.

- **qidianFreeChapterIds**

  - This zip file contains text files, each named by its corresponding Qidian bookID. Each text file contains the unique IDs for all free chapters of that story.

- **qidianFreeChapterMeta**

  - This zip file contains CSV files, each named by its corresponding Qidian bookID. Each CSV file contains metadata for all chapters of that book, including the number of reviews received for each paragraph (reviewNum), chapterID, and bookID.

- **webnovelFreeChapterDates**

  - This zip file contains CSV files, each named by its corresponding WebNovel bookID. Each CSV file contains metadata for the free available chapters, including their publish time and update time.

- **webnovelFreeChapterIds**

  - This zip file contains CSV files, each named by its corresponding WebNovel bookID. Each CSV file contains the chapterID and chapter title for all free available chapters.

- **webnovelFreeChapterMeta**

  - This zip file contains CSV files, each named by its corresponding WebNovel bookID. Each CSV file contains metadata for all chapters of that book, including the number of reviews received for each paragraph (reviewAmount), paragraphID, chapterID, and bookID.

- **qidianReviews_depersonalised**

  - This zip file contains CSV files, each named by its corresponding Qidian bookID. Each CSV file contains reviewId, content (of the review), likeCount (number of likes for this review), userID, level (the level of the user account).

- **qidianReplies_depersonalised**

  - This zip file contains CSV files, each named by its corresponding Qidian bookID. Each CSV file contains reviewId, quoteReviewId (the review of this reply to) content (of the reply), likeAmount (number of likes for this review), userID, userlevel (the level of the user account).
  
- **webnovelReviews_Booklevel_depersonalized**

  - This zip file contains csv files, each named by it's corresponding WebNovel bookID. Each CSV file contains metadata for reviews to the book, inclduing reviewId, content (book review), bookId, totalscore (review score), replyAmount (number of replies to this review), likeAmount (number of likes to this review), userID, (the level of the user account).

- **webnovelReviews_Chapterlevel_depersonalized**

  - This zip file contains csv files, each named by it's corresponding WebNovel bookID. Each CSV file contains metadata for chapter reviews of the book, including chapterId, reviewId, content (review), userID, (the level of the user account).

- **webnovelReviews_Paragraphlevel_depersonalized**

  - This zip file contains csv files, each named by it's corresponding WebNovel bookID. Each CSV file contains metadata for paragraph reviews of the book, including chapterId, paragraphId, reviewId, content (review), replyAmount (number of replies to this review), likeAmount (number of likes to this review), userID, userLevel(the level of the user account).

- **webnovelReplies_Booklevel_depersonalized**

  - This zip file contains csv files, each named by it's corresponding WebNovel bookID. Each CSV file contains metadata for replies to book reviews, including bookId, bookName, reviewId, content (reply), likeAmount (number of likes to this review), pReviewId (the book review ID), userID, and userLevel(the level of the user account).

- **webnovelReplies_Chapterlevel_depersonalized**

  - This zip file contains csv files, each named by it's corresponding WebNovel bookID. Each CSV file contains metadata for replies to the chapter reviews of the book, including chapterId, reviewId, sourceReviewId (the chapter review ID) content (replies), level (the level of the user account).

- **webnovelReplies_Paragraphlevel_depersonalized**

  - This zip file contains csv files, each named by it's corresponding WebNovel bookID. Each CSV file contains metadata for replies to the paragraph reviews of the book, including chapterId, paragraphId, reviewId, content (reply), sourceReveiwId (the paragraph review ID), userID, (the level of the user account).


**License**


This dataset is partially (story metadata, chapter metadata, and story mappings) released under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

The depersonalized reader response data included in this dataset is subject to a separate **Data Transfer Agreement**. Users must review and accept the DTA before accessing or using the reader comments data. 

- Terms of Use
  -  Researchers affiliated with universities or not-for-profit research institutes may use the Qidian-Webnovel Corpus 110 dataset for conducting not-for-profit scientific research, in accordance with the Data Transfer Agreement provided by the University of Groningen.

- Restrictions
  -  The files with restricted access are not open in order to be able to comply with third party licenses and to mitigate a risk of re-identification in terms of the GDPR. It is not allowed to disclose the full version of the Qidian-Webnovel Corpus 110 dataset to any third party or otherwise use it for your own benefit or for the benefit of a third party, without first obtaining written consent from the University of Groningen. 

- Terms of Access
  -  Permission for access can be granted by the University of Groningen Digital Competence Centre on behalf of the researcher(s) responsible for this dataset after assessment of credentials of the applicant and the reasons for the request. The signing of a Data Transfer Agreement is part of the procedure before access can be granted.
The procedure starts with a request for access via this dataset at DataverseNL.

For more information about the dataset, you can reach out to z.yu@rug.nl.



