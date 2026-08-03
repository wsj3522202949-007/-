---
id: tool-07462
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: royalroadapi
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/nico6bury/royalroadapi
created: 2026-07-18
updated: 2026-07-18
no: 7462
category: 画龙补充 / 扩容入库 — 补充源
repo: nico6bury/royalroadapi
stars: 0
url: https://github.com/nico6bury/royalroadapi
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# nico6bury/royalroadapi

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/nico6bury/royalroadapi
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A Python API wrapper for RoyalRoad that can asynchronously curate EPUBs
- **本地描述**：royalroadapi
- **拉取时间**：2026-07-25 19:22:39

related:
  - methods/QUICK_START.md
---

This is a fork of the original repository with some changes I made in order to get things working on my machine. So far, I mostly have just added a function called initialise_headers(), which is supposed to be called before doing anything, as otherwise the global headers variable doesn't get initialized before it's used.

The following is just a copy of the original README:

# RoyalRoadLAPI
A Python API to request and send data with the fanfiction website RoyalRoadL

To obtain individual data from a fiction, you must first call the get_fiction_object() function if you have a fiction id, or use search_fiction() to get a fiction id. #(to collect all data, refer to bottom)

get_fiction_object() takes a single argument, the fiction id, and returns a parsed html file of the fiction page.

With this object, you can request data from the page without making a http request for each piece of data.

eg.

	fiction_id = search_fiction(search_term) # to get a fiction id from a given search term
	fiction = get_fiction_object(fiction_id) # to get the fiction page and its information
	title = get_fiction_title(fiction) # to get the fictions title

Data that can be requested includes:

	

	get_fiction_title(fiction)
		returns the title as a string

	get_fiction_cover_image(fiction)
		returns the webaddress of the cover image for the fiction as string, very rarely returns a base64 encoded string of the image,
		image can be saved, refer to obtain_and_save_image() below

	get_fiction_author(fiction)
		returns the author as a string

	get_fiction_description(fiction)
		returns the fiction description as a string

	get_fiction_genres(fiction)
		returns all the genres as a list

	get_fiction_rating(fiction)
		returns all the different ratings as a list,
		eg. [overall_rating,best_rating,rating_count,style_rating,story_rating,character_rating,grammar_rating]

	get_fiction_statistics(fiction)
		returns the fictions statistics as a list,
		eg. [total_views,average_views,followers,favorites,rating_amount,pages]

	get_chapter_links(fiction)
		returns the links to each chapter of the fiction as a list,
		in original chronological order

	get_chapter_amount(fiction) #or simply get the length of the list returned above
		returns the amount of chapters as an integer,
		recommended to get the length of chapter_link instead if both are needed (to be efficient)

	get_fiction_info(fiction)
		Instead of gathering select information,
		all the data is returned as a list in the form,
		eg. [url,title,cover_image,author,description,genres,ratings,stats,chapter_links,chapter_amount]
		ratings and stats are both returned as lists in the forms
		[overall_rating,best_rating,rating_count,style_rating,story_rating,character_rating,grammar_rating]
		[total_views,average_views,followers,favorites,rating_amount,pages]
		Finally, chapter_links returns a list of the chapter URLs in original chronological order, minus the domain
	
	get_fiction(fiction_id or search term, directory (may be relative), start_chapter, end_chapter) #download a fiction by id or search term and save it as an epub
		returns the absolute final location of the epub file,
		start_chapter and end_chapter default to the first chapter and the last chapter released,
		invalid ranges are cleaned up,
		directory is created if it doesn't exist,
		file is overwritten if it already exists and isn't open
	
	get_fictions(fiction_id_start, fiction_id_end, directory)
		returns nothing,
		downloads entire fictions in the given range and saves them as epubs in the given directory,
		the range defaults to the entire fiction list of royalroadl
	
	find_latest_fiction_id()
		returns the lastest fiction id as an integer
	
	get_fiction_location(fiction_id, directory, start_chapter, end_chapter)
		returns the location of where the file would be saved for the given parameters if it saved correctly,
		this is useful due to all the stripping and sanitization that occurs to the epub
	
	check_active_fiction(fiction, fiction_id)
		returns True if the fiction has not been deleted,
		returns None if it has been removed
	
	obtain_and_save_image(directory,cover_image) #decode the base64 image or download the image from the cover_image url and then save it
		takes a directory and saves the cover_image in it as cover.jpg
	
	#considering implementing a function to return chapter content and information from a given fiction_id and chapter_num, or just a chapter_id, or potentially, a chapter_link
		

If using login.py it is possible to login to royalroad and request secure pages, read messages (now implemented) and even send messages.

Eg.

    login_object = login("email","password")
        #logs into an account and returns the security keys and cookies in the login_object

    status = send_message(login_object,"userid","subject","message")
        #returns true if the message successfully sent, and false if not.

    messages = read_messages(login_object)
	#returns all messages as a list in a list of messages that have not been deleted. Messages are as follows, [message_id,author,author_id,title,status,time]
