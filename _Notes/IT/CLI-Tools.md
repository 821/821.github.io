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
解壓： `7z e abc.7z`
完整路徑解壓： `7z x abc.7z`
刪除一些文件： `7z d abc.7z a*`
更新： `7z u abc.7z b*`
測試完整性： `7z t abc.7z`

#### 輔命令
輔命令的特點是前面有 `-` ，然後是命令的字母（一或兩個），緊接着是命令的參數。

格式與壓縮程度： `7z a -tzip jpg.zip *.jpg -m0` 這表示不壓縮，衹打包成 zip 。其中的 `m` 可以選 0-9 。
包括某文件： `7z e abc.7z -i*.txt`
排除某文件： `7z e abc.7z -x*.txt`
密碼： `7z a -pyourpassword abc.7z *.txt`
強制執行： `7z e abc.7z -y` 相當於出現選項時（比如問是否覆蓋）一律選 yes