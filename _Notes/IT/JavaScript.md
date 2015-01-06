---
layout: indexed
title: 簡單 JavaScript 入門
---
##前言
隨便學學一個普通的編程語言，大槪是這樣：先來個 Hello world ，算算 1+1 ，看看字符串、變量、數組等的格式，熟悉書寫規範。然後看看語句，什麼 if else for while return break 。由於有很多模塊，所以讀讀所需模塊的 manuals 。好，現在可以開始邊抄代碼邊熟練了，甚至還沒熟練就滿足需求，不用再學了。
坑爹的 JavaScript 又是怎樣的呢？ JavaScript 的功能是主要做網頁， HTML 和 CSS 要會吧？再學完一般編程的必由之路，是不是以爲可以開始抄代碼了？抄你妹！那堆 $ 是什麼？ document.getElementsByName 又是怎麼回事？許多年以後，你纔知道是 jQuery 和 DOM ……勉強能用的 JavaScript = HTML + CSS + DOM + jQuery + RegExp + JavaScript 基礎。一個看似純情的 Lambda 語言 JavaScript 裏竟然有這麼多花花腸子，無疑會給人造成許多困擾，而且樣樣去學，時間成本擺在那裏。卽使學了這些，抄代碼也常抄出翔，因爲裏面難免有點 XML, JSON, BOM, AJAX, DHTML, 各種 API... 而且， JavaScript 也存在版本問題， ECMAScript 1 2 3 4 5 6 ……看到如此亂象，能不頭大嗎？還沒說 E4X, CoffeeScript, Node.js 呢。

##學來幹嘛
首先是美化自己的網頁。很多複雜的功能如果通過 JavaScript 來完成會比較輕鬆。比如，本文的右側有個大綱，這玩意就是用 JavaScript 生成的，省卻我每次做索引之苦。嗯，不過其實這個代碼我沒怎麼讀過，是從別的網站「借」來的。
其次是改動別人的網頁。比如，我常用的讀秀及其各種衍生物，這個體系中有大量的隱藏屬性有待發掘，但如果每次手動未免太累了，所以寫點腳本，把需要的東西便捷的挖出來。

##敎材評介
學電腦學得要評介相關敎材，對我來說是第二次——上一次是 TeX ，原因是 TeX 體系龐雜，很多書華而不實。 JavaScript 也是龐雜混亂的，而且有過之而無不及，所以也要來一次。

JavaScript: The Good Parts (JavaScript 语言精粹) 要有點基礎再看。他畫的圖看起來很累。
JavaScript: The Definitive Guide (JavaScript权威指南) 這本書給人便祕或難產的感覺。由於太過囉嗦，很難堅持下去。
Professional JavaScript for Web Developers (JavaScript 高级程序设计) 有些章節結構淸晰又好讀，有些章節就馬馬虎虎。
DOM Scripting: Web Design with JavaScript and the Document Object Model (JavaScript DOM 编程艺术) 一本常用於推薦給新手的書。一章講完基礎（而且這一章簡而明，讀起來比較順暢），再一章就進 DOM 了。但是從第四章開始又不講人話了。
AdvancED DOM scripting: dynamic web design techniques (JavaScript DOM高级程序设计) 書籍強調不要過度依賴庫而不理解其原理——也就是用輪子還要求知道輪子是怎麼造的。

好了，最常見的書都被我噴完了，那要怎麼快速入門？
答案是，結合各種書籍、敎程，取長補短。

##學習計劃
這個「學習計劃」也非常適用於很久不用以後重新撿起。這裏假設讀者的閱讀速度跟本人一樣，如果跟不上，說明還沒達到閱讀的第四境界 XD
準備：打開 Chrome ，按 F12 ，這就是練習環境， console 。下載好書籍。如果不懂 HTML 和 CSS ，滾去學一會。
第一、二小時：基本命令、格式。敎材： DOM Scripting 第二章。不會編程的，時間加一倍。
第三小時： DOM 。敎材： Professional JavaScript 第十章。關鍵是知道有什麼，具體寫的時候可以查。
第四小時： RegExp 。敎材： Professional JavaScript 第五章第四節。如果之前沒學過，換成 Definitive Guide 第十章。 JavaScript 用個正則表達式也很繁瑣，看好返回値的特點，在 console 練一下。
第五小時： jQuery 。敎材： Definitive Guide 第十九章，可跳讀。
好了，Level 1 完成，可以開始抄點淺顯的代碼。