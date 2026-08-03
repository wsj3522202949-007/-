---
id: tool-00217
type: tool
area: 库
status: active
tags: [Claude插件, JavaScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: jQA
summary: Claude Code 插件式写作流
source: https://github.com/madebymike/jqa
created: 2026-07-18
updated: 2026-07-18
no: 217
category: 二、网文 / 长篇 AI 写作系统 库
repo: MadeByMike/jQA
stars: 3
url: https://github.com/madebymike/jqa
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# MadeByMike/jQA

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/madebymike/jqa
- **Stars**：3
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A jQuery plugin for writing quality assurance tests
- **本地描述**：A jQuery plugin for writing quality assurance tests
- **拉取时间**：2026-07-23 22:45:24

---

jQA
===

JQA is very tiny jQuery plugin to help run quality assurance tests on web content.

It is not intended for use in a production environment but rather on a test server or as a bookmarklet.

<a href="http://madebymike.github.io/jQA/">View demo</a>

Usage
-------------------

```html
<script src="/path/to/jQuery.js"></script>
<script src="/path/to/jQA.js"></script>
<script src="/path/to/my-test-cases.js"></script>
<script>
  $(document).ready(function(){
    jQA.doQA();
  });
</sctipt>
```

Writing tests cases
-------------------

You can add one or more rules at a time. Each rule must requires a unique name and a selector. This is all that is required although without a message this is fairly useless. 
```javascript
{
  "name of rule":{
		"selector":"body img", // string: jQuery selector
		"filter": function(object){  }, // function: Filter items matched items by returning true
		"each": function(object){  }, // function: Called for item after filtering. Useful for highlighting on the page.
		"message": "Images should have alt text", // string | function: The message to be returned by the rule.
		"severity": 2 // integer: When run jQA can ignore rules above a specified severity score
	}
}
```
Simple rule:

```javascript
jQA.addQA({
  "Inline styles":{
    "selector":"body *[style]",
    "message": "Do not use in-line styles."
  }
});	
```

A more complicated rule:

```javascript
jQA.addQA({
  "invalid emails":{
    "selector":"[href^='mailto:']",
    "filter":function(index,obj){
      //Crude email verification
      if( /(.+)@(.+){2,}\.(.+){2,}/.test($(obj).attr("href")){
        return true;
      }
      return false;
    },
    "each":function(obj){
      //Highlight error on page
      $(obj).css("border-bottom","dashed 1px red");
    },
    "message": "incorrect email format",
    "severity": 5 // Any number you like, 1 = worst 
  }
});
```

Options
-------

Not many settings at the moment. Set a message for the jQA modal header and the default severity if you like.

```javascript
jQA.settings({
	"headerMessage":"jQA has detected the following",
	"defaultSeverity":5
});
```

Initiating QA
----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Rules can be added before the DOM has loaded. Once the page is ready, and you have added rules run `jQA.doQA()`. You can optionally pass 2 parameters when running `doQA`, a callback and a severity score. The callback will be run imediately after QA and can be used to display messages. Alternatively QA can be run on page load without a callback and messages can be accessed without running QA again. Passing a severity will tell jQA to ignore rules with a severity score above this number. The severity scale is reversed.

```javascript
$(document).ready(function(){
	var silent = true; // log errors to console
	var severity = 2; // ignore rules with a severity greater than 2
	jQA.doQA(function(messages){
		console.log(messages);
	},severity);
	// you can also access messages like this:
	console.log(jQA.messages);
});
```
