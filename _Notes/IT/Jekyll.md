---
layout: indexed
title: Jekyll 常用知識合集
---
## Jekyll
<a href="http://jekyllrb.com/docs/home/" rel="external">官方文檔</a>及其<a href="http://jekyllcn.com/docs/home/" rel="external">中文翻譯</a>其實解決了絕大多數用戶對於 Jekyll 本身的疑問。但有些問題他的索引不是直觀，幫他索引一下。
<a href="http://jekyllrb.com/docs/configuration/#markdown-options" rel="external">Markdown 詳細設置</a>
<a href="http://jekyllrb.com/docs/templates/#code-snippet-highlighting" rel="external">代碼高亮</a>
<a href="http://jekyllrb.com/docs/templates/#post-url" rel="external">文章鏈接</a>
<a href="http://jekyllrb.com/docs/templates/#gist" rel="external">插入 Gist</a>

#### Permalinks
Jekyll 中有三種文件大量涉及 permalinks 的問題。首先是 posts ，這在 _config.yml 裏寫一句形如 permalink: /:title/ 的就行了，在每個文件裏寫也行。對於 collections ，在需要在對應的 collection 裏寫這句話。到了 pages 裏，索性不能總結性的寫了，衹能在每個 page 文件裏寫。

## Markdown
Jekyll 支持使用人性化一些的 <a href="https://help.github.com/articles/github-flavored-markdown/" rel="external">GitHub Flavored Markdown</a> (GFM) 。其餘看官方就好：<a href="http://daringfireball.net/projects/markdown/syntax" rel="external">官方版</a>，<a href="http://markdown.tw/" rel="external">繁體版</a>，<a href="http://wowubuntu.com/markdown/" rel="external">簡化字版</a>。

#### 實用語法
需要加 \\ 的字符： \\ \` \* \_ \{ \} \[ \] \( \) \# \+ \- \. \!
標題：在行首使用 \# ，幾級標題用幾個 \# ，行尾也可以加上等量的 \# 表示關閉標籤
淸單：無序淸單在行首加上 \* \+ \- 三選一，有序淸單是數字加 \. ，數字可亂寫
引用：在需要引用的部分每一行行首加上 \> ，引言中的引言加兩個
程序：行首加上一個 tab 或四個空格，則區塊被 pre code 兩個標籤包圍。如果衹要一小截，用一對 \` 包夾，這樣有 code 沒有 pre
分割線：一行 \* 或 \-
鏈接：形如 \[link\]\(http://example.net/\) \"Optional Title\" ，可以用相對路徑
參考：類似鏈接，寫作 \[example\]\[id\] ，二者之間可加空格
圖片：形如 \!\[Alt text\]\(http://example\.net/img\.jpg \"Optional title\"\)
em: 一對 \* 或 \_ 包夾
strong: 一對 \*\* 或 \_\_ 包夾

#### GFM
GFM 作爲 Markdown 最常用的「方言」，其實挺不錯的。
首先是合理化了一些地方：
行末不用加那兩個破空格
形如 what\_the\_fuck 的一整個詞裏的兩個 _ 包夾部分不會被轉換
標準的 URL 會自動變成鏈接
其次是加了一些功能：
刪節線：一對 ~~ 包夾的詞會轉成刪節線
引用：兩行 \`\`\` 包夾的段落會轉成引用
代碼：引用的前一個如果寫成形如 \`\`\`ruby 這樣就是代碼高亮
表格：用 | 分列，一行 - 表示以上是欄頭， : 在 - 行中的位置表示靠哪邊

## Textile
對於需要 div 或 span 標籤的文章， textile 比較方便。
不喜歡把版面佈置得太複雜，衹記錄一部分就行了。其餘直接看<a href="http://redcloth.org/textile" rel="external">官方文檔</a>。

#### 大樣式
（注意： . 後面都是有空格的，不然易出錯）
標題：形如 h1. ，數字可換
引用： bq.
無序淸單：前面加 \* ， \* 的數量越多，縮進越多
有序淸單：前面加 # ， 也可以同上做子淸單或與之結合
定義式淸單：形如 - coffee := Hot and black ，得到黑體的被定義對象和下一行縮進的定義
腳註：在正文加 \[1\] ，腳註內容前加 fn1. 
表格：第一行形如 |\_. name|\_. age| ，之後形如 |Tom|5|
div ：前面加 div. 

#### 小樣式
加粗：形如 \*strong\*
加重：形如 \_stress\_
斜體：形如 \_\_italicized__
書名：形如 ??citation??
刪除：形如 -delete- 或 [-delete-]
下劃線：形如 +underline+ 或 [+underline+]
上標：形如 ^uper^
下標：形如 ~lower~
鏈接：形如 \"example\":http://example.com
插圖：形如 !http://example.com/example.jpg!
代碼：形如 @code@

#### HTML 屬性
span ：形如 %span%
class ：很多樣式可以加上 class ，如 %(class)span%
ID ：形如 \*(\#special)strong\*

#### 不使用 textile 轉成 HTML
整段：段落前後用 <notextile> 和 </notextile> 框起來
行中：形如 ==no textile==

## GitHub

#### 半公開
總有些東西，可公開又不希望太多人看到，尤其不希望別人用 Google 之類綜合搜索引擎找到。怎麼辦？
首先可以用 Gist 。 Gist 雖然是 Git 管理的，但版本顯示、目錄等方面不如正常 repo 。
其次是 private repo 。不過 GitHub 的 private repo 要錢，但我又想把代碼放在 GitHub ，好統一管理。
於是觀察 <a href="https://github.com/robots.txt" rel="external">GitHub robots</a> ，發現其實每個 repo 衹有 master 會收錄，其餘是禁止蜘蛛的。那麼，對於可公開又不願大面積分享的內容，可以通過建立其他分支的方式上傳。
在 repo 的 setting 可以把 main 指定爲 default branch 。以後每次進 repo 都會默認看到 main ——不過這樣代碼會曝露在 GitHub 本身的搜索引擎下，所以不設也罷。

#### 發行版
在 repo 的鏈接後面加上 `/releases` ，卽可發佈發行版。