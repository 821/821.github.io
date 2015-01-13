---
layout: indexed
title: JavaScript 入門
---
##前言
隨便學學一個普通的編程語言，大槪是這樣：先來個 Hello world ，算算 1+1 ，看看字符串、變量、數組等的格式，熟悉書寫規範。然後看看語句，什麼 if else for while return break 。由於有很多模塊，所以讀讀所需模塊的 manuals 。好，現在可以開始邊抄代碼邊熟練了，甚至還沒熟練就滿足需求，不用再學了。
坑爹的 JavaScript 又是怎樣的呢？ JavaScript 的功能是主要做網頁， HTML 和 CSS 要會吧？再學完一般編程的必由之路，是不是以爲可以開始抄代碼了？抄你妹！那堆 $ 是什麼？ document.getElementsByName 又是怎麼回事？許多年以後，你纔知道是 jQuery 和 DOM ……勉強能用的 JavaScript = HTML + CSS + DOM + jQuery + RegExp + JavaScript 基礎。一個看似純情的 Lambda 語言 JavaScript 裏竟然有這麼多花花腸子，無疑會給人造成許多困擾，而且樣樣去學，時間成本擺在那裏。卽使學了這些，抄代碼也常抄出翔，因爲裏面難免有點 XML, JSON, BOM, AJAX, 各種 API... 而且， JavaScript 也存在版本問題， ECMAScript 1 2 3 4 5 6 ……看到如此亂象，能不頭大嗎？還沒說 E4X, CoffeeScript, Node.js 呢。

##學來幹嘛
首先是美化自己的網頁。很多複雜的功能如果通過 JavaScript 來完成會比較輕鬆。比如，本文的右側有個大綱，這玩意就是用 JavaScript 生成的，省卻我每次做索引之苦。嗯，不過其實這個代碼我沒怎麼讀過，是從別的網站「借」來的。
其次是改動別人的網頁。比如，我常用的讀秀及其各種衍生物，這個體系中有大量的隱藏屬性有待發掘，但如果每次手動未免太累了，所以寫點腳本，把需要的東西便捷的挖出來。

##敎材評介
學電腦學得要評介相關敎材，對我來說是第二次——上一次是 TeX ，原因是 TeX 體系龐雜，很多書華而不實。 JavaScript 也是龐雜混亂的，而且有過之而無不及，所以也要來一次——而且這次更嚴重，很多書都是業界「大牛」寫的，但是眞的不是很普適。

JavaScript: The Good Parts (JavaScript 语言精粹) 要有點基礎再看。他畫的圖看起來很累。
JavaScript: The Definitive Guide (JavaScript权威指南) 這本書給人便祕或難產的感覺。由於太過囉嗦，很難堅持下去。
Professional JavaScript for Web Developers (JavaScript 高级程序设计) 有些章節結構淸晰又好讀，有些章節就馬馬虎虎。
DOM Scripting: Web Design with JavaScript and the Document Object Model (JavaScript DOM 编程艺术) 一本常用於推薦給新手的書。一章講完基礎（而且這一章簡而明，讀起來比較順暢），再一章就進 DOM 了。但是從第四章開始又不講人話了。
AdvancED DOM Scripting: Dynamic Web Design Techniques (JavaScript DOM高级程序设计) 書籍強調不要過度依賴庫而不理解其原理——也就是用輪子還要求知道輪子是怎麼造的。
Beginning JavaScript with DOM Scripting and Ajax: From Novice to Professional (深入浅出JavaScript) 絕對不是 "beginning" 用書，或者用譯名吐槽一下，有「深入」而無「淺出」。
Head First JavaScript (深入浅出JavaScript) 是的，和上面那麼撞了譯名。這本花哨、不得要領，浪費時間。
Pro JavaScript Techniques (精通JavaScript) 完全不是人話，看不懂。
ppk on JavaScript (ppk談JavaScript) 人話多一些，但也不能拿來入門呀。
Accelerated DOM Scripting with Ajax, APIs, and Libraries (JavaScript捷径教程) 也屬於提高類，不過寫得還挺系統。

好了，最常見的書都被我噴完了，那要怎麼快速入門？
答案是，結合各種書籍、敎程，取長補短。

##學習計劃
這個「學習計劃」也非常適用於很久不用以後重新撿起。這裏假設讀者的閱讀速度跟本人一樣，如果跟不上，說明還沒達到閱讀的第四境界 XD
準備：打開 Chrome ，按 F12 ，這就是練習環境， console 。下載好書籍。如果不懂 HTML 和 CSS ，滾去學一會。
第一、二小時：基本命令、格式。敎材： DOM Scripting 第二章。不會編程的，時間加一倍。
第三小時： DOM 。敎材： Professional JavaScript 第十章。關鍵是知道有什麼，具體寫的時候可以查。
第四小時： RegExp 。敎材： Professional JavaScript 第五章第四節。如果之前沒學過，換成 Definitive Guide 第十章。 JavaScript 用個正則表達式也很繁瑣，看好返回値的特點，在 console 練一下。
第五小時： jQuery 。敎材： Definitive Guide 第十九章，可跳讀。個人覺得 jQuery 討厭而過時，但別人用得很多。這個部分有個入門書 Beginning JavaScript and CSS Development with jQuery (jQuery JavaScript与CSS开发入门经典) ，差評很多，因爲眞的很入門，而且書名完全不對，應該叫 Beginning jQuery with JavaScript and CSS 。
好了，Level 1 完成，可以開始抄點淺顯的代碼。

##重點備忘
隨便寫點，沒有普遍性。

###基本寫法
句末加個 ;
註釋加 //

###字符串
字符串加 "" 或 '' ，分行要加 \\ 。
雙引號內可以直接用單引號，反之亦然。
雙引號內用雙引號要加 \\ ，單引號同此。
屬性 length 偶爾能用上。

###數組 (Array)
比如 DOM 的 `getElementsByTagName` 和 RegExp 的 `match` ，結果就記在數組裏。
JavaScript 數組很平常，可以混搭着放入任意類型的數據如函數、數組等作爲元素，低端用戶見得最多的當然是純字符串的形式了。
每次寫完一個數組未免太傻，所以用一個變量來代表他：
{% highlight javascript %}
var a = ['abc', '123'];
{% endhighlight %}

抽取元素的方法也很平常，和別的語言一樣都是從 0 開始計數的：
{% highlight javascript %}
a[0] // 這就等於 'abc';
{% endhighlight %}

要添加元素還是很平常：
{% highlight javascript %}
a[2] = 'abc123';
{% endhighlight %}

數組也有其屬性，最常用的就是長度（不大於 2^32-1 ）：
{% highlight javascript %}
a.length // 現在是 3;
a.length = 4 // 這樣就多出個空元素 undefined;
a.length = 2 // 這樣就把後面的元素砍掉了;
//至於會報錯的極端情況，腦洞不太大都不會碰到（比如設成負數、字符串）;
{% endhighlight %}

###循環 (loop)
旣然用了數組，就免不了用到他的好基友循環。
for 循環配合數組就要用到 for/in 循環，我們用上一節的數組犯個賤，連續彈對話框：
{% highlight javascript %}
for (var i in a){
    alert(a[i]);
}
{% endhighlight %}

用 for/in 還是挺方便的。如果改成單純的 for 循環，要這麼寫：
{% highlight javascript %}
for (var i = 0; i < a.length; i++){
    alert(a[i]);
}
{% endhighlight %}

如果改寫成 while 循環：
{% highlight javascript %}
var i = 0;
while (i < a.length){
    alert(a[i]);
    i++;
}
{% endhighlight %}