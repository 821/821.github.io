---
layout: indexed
title: Jekyll 常用知識合集
---
##Jekyll
<a href="http://jekyllrb.com/docs/home/" rel="external">官方文檔</a>及其<a href="http://jekyllcn.com/docs/home/" rel="external">中文翻譯</a>其實解決了絕大多數用戶對於 Jekyll 本身的疑問。但有些問題他的索引不是直觀，幫他索引一下。  
<a href="http://jekyllrb.com/docs/configuration/#markdown-options" rel="external">Markdown 詳細設置</a>  
<a href="http://jekyllrb.com/docs/templates/#code-snippet-highlighting" rel="external">代碼高亮</a>  
<a href="http://jekyllrb.com/docs/templates/#post-url" rel="external">文章鏈接</a>  
<a href="http://jekyllrb.com/docs/templates/#gist" rel="external">插入 Gist</a>  

##Textile
Textile 沒有噁心的兩個空格換行機制，所以一般都用他 (Markdown 功能確實比較若，不過現在支持用 Github Flavored 了，就還好，設置是 GFM) 。不喜歡把版面佈置得太複雜，衹記錄一部分就行了。其餘直接看<a href="http://redcloth.org/textile" rel="external">官方文檔</a>。  
###大樣式
（注意： . 後面都是有空格的，不然易出錯）  
標題：形如 h1. ，數字可換  
引用： bq.  
無序淸單：前面加 \* ， \* 的數量越多，縮進越多  
有序淸單：前面加 # ， 也可以同上做子淸單或與之結合  
定義式淸單：形如 - coffee := Hot and black ，得到黑體的被定義對象和下一行縮進的定義  
腳註：在正文加 \[1\] ，腳註內容前加 fn1.   
表格：第一行形如 |\_. name|\_. age| ，之後形如 |Tom|5|  
div ：前面加 div.   
###小樣式
加粗：形如 \*strong\*  
加重：形如 \_stress\_  
斜體：形如 \_\_italicized__  
書名：形如 ??citation??  
刪除：形如 -delete- 或 [-delete-]  
下劃線：形如 +underline+ 或 [+underline+]  
上標：形如 ^uper^  
下標：形如 ~lower~  
鏈接：形如 "example":http://example.com  
插圖：形如 !http://example.com/example.jpg!  
代碼：形如 @code@  
###HTML 屬性
span ：形如 %span%  
class ：很多樣式可以加上 class ，如 %(class)span%  
ID ：形如 \*(\#special)strong\*  
###不使用 textile 轉成 HTML
整段：段落前後用 <notextile> 和 </notextile> 框起來  
行中：形如 ==no textile==  

##Git
注意： [] 以內的內容，都是用戶自定義的，不用帶上尖括號本身。  
我個人不太喜歡 Git ，覺得索引沒什麼用，分支對單幹的人來說也很少用。很多命令具有自欺欺人的味道，有些地方太繁複，體系也較複雜。但是，現在很多時候並不是你想用他，而是人家衹支持他，所以你衹好用……總之 Git 是必備技能，需要有一定瞭解。  
Git 眞的相當複雜，命令的意義往往不是一兩個詞就能解釋淸楚的，所以就有了本文。本文的重點有兩個：一是對常用命令的列舉，可以看作是一種備查；二是對基本槪念的解釋，爲的是自己幾年後看本文還能快速上手。  
###關係圖
Git 的命令，基本上就是四個位置的相互操作。記住關係圖， Git 就掌握了一半。  
![Git](../Assets/Pic/Git.png)
###init 初始化
###add 添加
將改動添加到索引中。  
git add [filename] 添加特定文件的改動  
git add . 添加所有文件的改動並把有文件被刪這個改動添加到索引，有他 rm 和 mv 都可以忘了  
###commit 提交
將改動從索引提交到本地倉庫。  
git commit -m "[commit message]" 提交時附上對提交的描述  
git commit -a -m "[commit message]" 先添加，再提交  
git commit –amend -m "[commit message]" 提交後又做了修改，但不想增加提交數量時使用，挺自欺欺人的  
###reset 撤銷
撤銷對本地倉庫來說是提交的反義，一種磨滅歷史的行爲。  
git reset --soft 撤銷最後一次提交，索引和工作文件保持被修改狀態  
git reset --mixed 撤銷最後一次提交和此提交中涉及的所有添加，工作文件保持被修改狀態，也作 git reset  
git reset --hard 撤銷最後一次提交後的所有修改  
###revert 回滾
回滾相當於從本地倉庫裏找到某次提交，然後用一次新的提交來中和該提交。要求所有本地文件及改動都要添加到倉庫裏。與撤銷的區別在於，比如一個倉庫裏有三次提交，這時做一次撤銷，則集體對第三次提交失憶，一切回到兩次提交時的狀態；而如果使用回滾，則文件回到第二次提交的狀態，但倉庫記錄第三次提交，並記一個第四次提交，說明這次提交是一個回滾動作。  
git revert HEAD^ 回滾最後一次提交， HEAD^ 當然可以換成別的參數  
git revert [commit message] 不記得是哪次提交，記得提交描述時使用  
###diff 差異
git diff 索引和工作文件的差異  
git diff –cached 索引和本地倉庫的差異  
git diff HEAD 本地倉庫和工作文件的差異  
git diff [source branch] [target branch] 比對分支差異  
###checkout 調出
直接從本地倉庫調出文件，覆蓋到工作文件。是個頗有風險的命令。  
###branch 分支簡單操作
git branch [branch] [branch name] 建立分支  
git branch -m [old] [new] 給分支改名，如有同名分支想覆蓋，用 -M  
git branch -a 羅列所有分支  
git branch -r 羅列遠程分支  
git branch -d [branch name] 刪除分支，強制刪除用 -D  
git branch -d -r [branch name] 刪除遠程分支  
###merge 合倂
git merge [branch name] 將其他分支合倂到當前分支  
###rebase 合流
基本上， merge 保留分支的提交史，而 rebase 則是將一個分支的提交史強加在另一分支頭上，讓人以爲一直是在後者上工作而不知道曾經有前者在幹活。自欺欺人的命令。  
###clone 複製
複製遠程倉庫。下載時 https 最方便安全又普遍，還支持 rsync, ftp, ssh 等。  
git clone [remote address] [foldername] 複製遠程倉庫，當參數 foldername 省略時，就地建立一個跟遠程倉庫同名的子文件夾，並將文件放在裏面。  
###remote 遠程管理
git remote 羅列  
git remote -v 查看主機網址，記住：名字是 orgin 的很重要  
git remote -o [name] [remote address] 設置並命名  
git remote add [name [remote address] 添加  
git remote rm [name] 刪除  
git remote rename [old] [new] 改名  
###fetch 更新
從遠程倉庫下載到本地倉庫，或者說把本地倉庫改成跟遠程倉庫一樣。  
git fetch [remote] [branch] 更新， branch 不寫則是 master  
git fetch origin master 取回主分支  
###pull 取回
取回並非簡單取回，可以看作更新並合倂。  
git pull [remote] [branch]:[local branch] 將遠程分支與本地分支合倂， branch 不寫則是 master  
###push 推送
將本地倉庫推送到遠程倉庫。  
git push [remote] [local branch]:[branch] 將本地分支的更新推送到遠程分支上， branch 不寫則新建一個與 local branch 同名的  
git push origin master 推送主分支  
git push origin 當前分支推送到遠程對應分支  
git push 衹有一個分支時的省略句  
git push -u origin master 設置，每次用 git push 都相當於 git push origin master  
git push --force origin 暴力推送，會導致合倂， --force 也作 -f  
git push origin:[branch] 刪除遠程分支  
###常量
HEAD^ 最後一次提交  
HEAD^^ HEAD 的上一次提交  
HEAD^n HEAD 的上 n 次提交  
HEAD~n HEAD 的上 n-1 次提交，或叫倒數第 n 次提交  
COMMIT_EDITMSG 最後一次提交的提交信息  
###資料
收集一些寫得比較好的，和 Git 有關的文章。  
<a href="http://git-scm.com/book" rel="external">Git Book</a> 官方書，但很多東西都沒寫。  
<a href="http://gitready.com/" rel="external">git ready</a> 一份詳細敎程。  
<a href="https://www.kernel.org/pub/software/scm/git/docs/user-manual.html" rel="external">Git User’s Manual</a> 詳細得讓人不想看，推送失敗怎麼辦之類的細節都有介紹。  
<a href="http://gitref.org/" rel="external">Git Reference</a> 結合實例的敎程。  
<a href="http://marklodato.github.io/visual-git-guide/index-zh-cn.html" rel="external">图解Git</a> 重點解釋一些不太好理解的槪念。  
<a href="http://ihower.tw/git/" rel="external">Git 版本控制系統</a> 一串關於 Git 的「高級」用法。  
<a href="http://blog.yorkxin.org/posts/2011/07/29/git-rebase" rel="external">Git-rebase 小筆記</a>  
<a href="http://www.ruanyifeng.com/blog/2014/06/git_remote.html" rel="external">Git远程操作详解</a>  
<a href="http://www.worldhello.net/gotgithub/index.html" rel="external">GotGitHub</a>