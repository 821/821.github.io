---
layout: indexed
title: CLI 工具常用命令
---
凡例
衹記錄自己認爲常用的命令。
以實例和實例一部分爲主。

## aria2
簡介：下載工具。單是 CLI 下載的工具其實很多，但 aria2 的特點是有 RPC ，所以有比如妖妖舞網盤直接添加到 aria2 的瀏覽器插件。

官方文檔： http://aria2.sourceforge.net/manual/en/html/
最普通的下載： `aria2c http://example.com/1.txt`
使用多個來源同時下載： `aria2c -s2 http://example.com/1.txt http://mirror.example.com/1.txt`
指定文件名： `aria2c -o 2.txt http://example.com/1.txt` 或 `aria2c --out=2.txt http://example.com/1.txt`
指定文件夾： `-d D:\` 或 `--dir=D:\`
指定 header ： `aria2c  "User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 115Browser/5.1.3"` 可指定多次
指定要僞裝的瀏覽器： `aria2c -U <USER_AGENT>` 或 `arai2c --user-agent=<USER_AGENT>`
指定下載列表： `aria2c --input-file=D:\1.txt`
列表可以指定多個來源，其他命令則另起 N 行且行頭使用空白符來代替 `--` ，舉例：
```bash
http://example.com/1.txt	http://mirror.example.com/1.txt
	dir=E:\
	out=2.txt
```
保存進度： `--save-session=D:\2.txt`
開啓續傳： `-c` 或 `--continue=true`
允許覆蓋： `--allow-overwrite=true`
同時進行的任務數量： `-j 20` 或 `--max-concurrent-downloads=10`， 這個命令是 aria2 獨有的，我用來抓取異體字字典的時候遇到過 bug ，比如 a b c 三個文件同時下載着，結果 a 下成了 b 之類的事情不時發生。
跳過已有文件： `--auto-file-renaming=false` 已有文件默認是改名下載
不要寫太多 log ： `--console-log-level=error` 不然一不小心 log 文件有幾 GB

## wget
簡介：老牌下載工具，很多命令其實都被 aria2 吸收了。這裏衹記好用的「組合拳」。

後臺下載整個列表： `wget -b -i url.txt` 。 `-b` 的好處是，在 cmd 中輸入後，立刻轉入後臺，可以馬上執行下一條命令。如果有一串記下鏈接的文件， `1.txt` `2.txt` ... `n.txt` ，可以一次性在一個 cmd 窗口中輸入多條命令，從而實現 n 個進程同時下載。

## 7-zip
簡介：老牌壓縮工具，格式豐富，命令多，速度快，界面醜。

#### 主命令
壓縮、添加： `7z a abc.7z *.txt`
添加某目錄下所有文件、文件夾： `7z a abc.7z D:\abc\`
解壓： `7z e abc.7z`
完整路徑解壓： `7z x abc.7z`
刪除一些文件： `7z d abc.7z a*`
更新： `7z u abc.7z b*`
測試完整性： `7z t abc.7z`

#### 輔命令
輔命令的特點是前面有 `-` ，然後是命令的字母（一或兩個），緊接着是命令的參數。

遞歸： `7z a abc.7z *.txt -r`
格式與壓縮程度： `7z a -tzip jpg.zip *.jpg -m0` 這表示不壓縮，衹打包成 zip 。其中的 `m` 可以選 0-9 。
包括某文件： `7z e abc.7z -i*.txt`
排除某文件： `7z e abc.7z -x*.txt`
密碼： `7z a -pyourpassword abc.7z *.txt`
強制執行： `7z e abc.7z -y` 相當於出現選項時（比如問是否覆蓋）一律選 yes

## Git
簡介：個人用會覺得比較囉嗦的文件管理系統。

#### 關係圖
Git 的命令，基本上就是四個位置的相互操作。記住關係圖， Git 就掌握了一半。
![Git]({{ site.url }}/Assets/Pic/Git.png)

#### init 初始化

#### add 添加
將改動添加到索引中。
git add [filename] 添加特定文件的改動
git add . 添加所有文件的改動並把有文件被刪這個改動添加到索引，有他 rm 和 mv 都可以忘了

#### commit 提交
將改動從索引提交到本地倉庫。
git commit -m \"\[commit message\]\" 提交時附上對提交的描述
git commit -a -m \"\[commit message\]\" 先添加，再提交
git commit –amend -m \"\[commit message\]\" 提交後又做了修改，但不想增加提交數量時使用，挺自欺欺人的

#### reset 撤銷
撤銷對本地倉庫來說是提交的反義，一種磨滅歷史的行爲。
git reset --soft 撤銷最後一次提交，索引和工作文件保持被修改狀態
git reset --mixed 撤銷最後一次提交和此提交中涉及的所有添加，工作文件保持被修改狀態，也作 git reset
git reset --hard 撤銷最後一次提交後的所有修改

#### revert 回滾
回滾相當於從本地倉庫裏找到某次提交，然後用一次新的提交來中和該提交。要求所有本地文件及改動都要添加到倉庫裏。與撤銷的區別在於，比如一個倉庫裏有三次提交，這時做一次撤銷，則集體對第三次提交失憶，一切回到兩次提交時的狀態；而如果使用回滾，則文件回到第二次提交的狀態，但倉庫記錄第三次提交，並記一個第四次提交，說明這次提交是一個回滾動作。
git revert HEAD^ 回滾最後一次提交， HEAD^ 當然可以換成別的參數
git revert \[commit message\] 不記得是哪次提交，記得提交描述時使用

#### diff 差異
git diff 索引和工作文件的差異
git diff –cached 索引和本地倉庫的差異
git diff HEAD 本地倉庫和工作文件的差異
git diff \[source branch\] \[target branch\] 比對分支差異

#### checkout 調出
直接從本地倉庫調出文件，覆蓋到工作文件。是個頗有風險的命令。分支不存在時新建一個。
git checkout -b \[branch name\]

#### branch 分支簡單操作
git branch \[branch\] \[branch name\] 建立分支
git branch \-m \[old\] \[new\] 給分支改名，如有同名分支想覆蓋，用 \-M
git branch \-a 羅列所有分支
git branch \-r 羅列遠程分支
git branch \-d \[branch name\] 刪除分支，強制刪除用 \-D
git branch \-d \-r \[branch name\] 刪除遠程分支

#### merge 合倂
git merge \[branch name\] 將其他分支合倂到當前分支

#### rebase 合流
基本上， merge 保留分支的提交史，而 rebase 則是將一個分支的提交史強加在另一分支頭上，讓人以爲一直是在後者上工作而不知道曾經有前者在幹活。自欺欺人的命令。

#### clone 複製
複製遠程倉庫。下載時 https 最方便安全又普遍，還支持 rsync, ftp, ssh 等。
git clone \[remote address\] \[foldername\] 複製遠程倉庫，當參數 foldername 省略時，就地建立一個跟遠程倉庫同名的子文件夾，並將文件放在裏面。

#### remote 遠程管理
git remote 羅列
git remote \-v 查看主機網址，記住：名字是 orgin 的很重要
git remote \-o \[name\] \[remote address\] 設置並命名
git remote add \[name\] \[remote address\] 添加
git remote rm \[name\] 刪除
git remote rename \[old\] \[new\] 改名

#### fetch 更新
從遠程倉庫下載到本地倉庫，或者說把本地倉庫改成跟遠程倉庫一樣。
git fetch \[remote\] \[branch\] 更新， branch 不寫則是 master
git fetch origin master 取回主分支

#### pull 取回
取回並非簡單取回，可以看作更新並合倂。
git pull \[remote\] \[branch\]\:\[local branch\] 將遠程分支與本地分支合倂， branch 不寫則是 master

#### push 推送
將本地倉庫推送到遠程倉庫。
git push \[remote\] \[local branch\]\:\[branch\] 將本地分支的更新推送到遠程分支上， branch 不寫則新建一個與 local branch 同名的
git push origin master 推送主分支
git push origin 當前分支推送到遠程對應分支
git push 衹有一個分支時的省略句
git push \-u origin master 設置，每次用 git push 都相當於 git push origin master
git push \-\-force origin 暴力推送，會導致合倂， \-\-force 也作 \-f
git push origin\:\[branch\] 刪除遠程分支

#### 常量
HEAD^ 最後一次提交
HEAD^^ HEAD 的上一次提交
HEAD^n HEAD 的上 n 次提交
HEAD~n HEAD 的上 n-1 次提交，或叫倒數第 n 次提交
COMMIT_EDITMSG 最後一次提交的提交信息

#### 資料
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