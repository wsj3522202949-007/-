---
id: tool-07659
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 本地写作]
title: goodbooks-10k
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/zygmuntz/goodbooks-10k
created: 2026-07-18
updated: 2026-07-18
no: 7659
category: 画龙补充 / 扩容入库 — 补充源
repo: zygmuntz/goodbooks-10k
stars: 895
url: https://github.com/zygmuntz/goodbooks-10k
tier: "S"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# zygmuntz/goodbooks-10k

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/zygmuntz/goodbooks-10k
- **Stars**：895
- **语言**：Jupyter Notebook
- **License**：NOASSERTION
- **Topics**：books, goodreads, ratings, recommendations, recommender-systems
- **GitHub 描述**：Ten thousand books, six million ratings
- **本地描述**：goodbooks-10k
- **拉取时间**：2026-07-25 19:29:09

related:
  - methods/QUICK_START.md
---

# goodbooks-10k

This dataset contains six million ratings for ten thousand most popular (with most ratings) books. There are also:

* books marked to read by the users
* book metadata (author, year, etc.) 
* tags/shelves/genres

## Access

Some of these files are quite large, so GitHub won't show their contents online. See [samples/](samples/) for smaller CSV snippets.

Open the [notebook](https://github.com/zygmuntz/goodbooks-10k/blob/main/quick_look.ipynb) for a quick look at the data. Download individual zipped files from [releases](https://github.com/zygmuntz/goodbooks-10k/releases).

The dataset is accessible from [Spotlight](https://maciejkula.github.io/spotlight/datasets/goodbooks.html), recommender software based on PyTorch.

## Contents

**ratings.csv** contains ratings sorted by time. It is 69MB and looks like that:

	user_id,book_id,rating
	1,258,5
	2,4081,4
	2,260,5
	2,9296,5
	2,2318,3
	
Ratings go from one to five. Both book IDs and user IDs are contiguous. For books, they are 1-10000, for users, 1-53424. 	

**to_read.csv** provides IDs of the books marked "to read" by each user, as _user_id,book_id_ pairs, sorted by time. There are close to a million pairs.

**books.csv** has metadata for each book (goodreads IDs, authors, title, average rating, etc.). The metadata have been extracted from goodreads XML files, available in `books_xml`.

### Tags

**book_tags.csv** contains tags/shelves/genres assigned by users to books. Tags in this file are represented by their IDs. They are sorted by _goodreads_book_id_ ascending and _count_ descending. 

In raw XML files, tags look like this:

	<popular_shelves>
		<shelf name="science-fiction" count="833"/>
		<shelf name="fantasy" count="543"/>
		<shelf name="sci-fi" count="542"/>
		...
		<shelf name="for-fun" count="8"/>
		<shelf name="all-time-favorites" count="8"/>
		<shelf name="science-fiction-and-fantasy" count="7"/>	
	</popular_shelves>

Here, each tag/shelf is given an ID. **tags.csv** translates tag IDs to names.

### goodreads IDs

Each book may have many editions.  _goodreads_book_id_ and _best_book_id_ generally point to the most popular edition of a given book, while goodreads  _work_id_ refers to the book in the abstract sense. 

You can use the goodreads book and work IDs to create URLs as follows:

https://www.goodreads.com/book/show/2767052   
https://www.goodreads.com/work/editions/2792775  

Note that _book_id_ in **ratings.csv** and **to_read.csv** maps to _work_id_, not to _goodreads_book_id_, meaning that ratings for different editions are aggregated.
