---
layout: indexed
title: CLI 工具常用命令
---
## aria2
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
同時進行的任務數量： `-j 20` 或 `--max-concurrent-downloads=10`