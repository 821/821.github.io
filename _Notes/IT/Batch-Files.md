---
layout: indexed
title: 批處理命令備查
date: '2014/08/04'
---
簡單使用批處理不難，我邊學邊寫本文，也就花了兩天。本來批處理看看 HELP 就差不多的，可是某些命令的解釋如同火星文，衹好親自整理一番。筆記較簡單，自認爲比較重要的會打上「☯」號，覺得不重要的會降低他的標題檔次，保持右側導航簡練。
微軟標準，在討論 DOS 命令時，一般使用方括號表示可選內容； | 表示若干項選一樣； drive 表示盤符，比如 C ； path 表示路徑； filename 表示文件名； string 表示字符串。儘管 DOS 對大小寫不敏感，用戶可以隨便寫，但書寫命令的時候，一般用大寫來寫命令和命令參數，而小寫寫一些路徑、文件、字符串之類的用戶參數。有時用 source 和 destination 表示來源和目標，來源可不含盤符和路徑，目錄可不含文件名。
話說批處理語法不大科學，學了批處理，你會 get 一個新技能： dirty hack 。

## 習慣
? 表示一個字符和空字符
* 表示若干個字符
^ 表示行首
$ 表示行尾
\x 表示一個字符——以區分命令
命令與參數間，必須使用空格來分割
. 表示當前目錄中的所有文件和文件夾☯
.. 表示上一級目錄
[命令] /? 表示查詢這個命令的用法☯
& 把兩行命令粘起來☯

常見命令參數用法：
有時有點出入，但基本上就這樣。
/F 強制執行
/Q 靜默，不提示用戶
/S 包括所有子文件夾、文件
/Y 表示所有確認項都選 y ，也就是 yes
/-Y 表示所有確認項都要再確認一次

## 非執行類

### 註釋
REM 整行
:: 整行

### 回顯
```bat
ECHO ON|OFF
ECHO [message]
```
`@` 使用後隱藏整行正在執行的命令，所以爲了完全隱身，都是寫成 `@ECHO OFF` 。

### 暫停☯
`PAUSE` 有兩個用法：一是避免窗口自動關閉，二是等待用戶操作

### 標籤與跳轉☯
```bat
:lable ::設置標籤
GOTO lable ::運行到這一行時，跳轉到設置了標籤的地方繼續運行
```

### 調用☯
`CALL` 直接調用另一腳本，並且運行完後還後再運行本腳本後的命令

#### 淸屛cls
淸除之前執行的一堆命令

## 文件夾類

#### 查看
```bat
DIR [drive:][path][filename] [/A[[:]attributes]] [/B] [/C] [/D] [/L] [/N] [/O[[:]sortorder]] [/P] [/Q] [/R] [/S] [/T[[:]timefield]] [/W] [/X] [/4] [drive:][path][filename]
```
查看本目錄下的文件和文件夾

### 切換☯
```bat
CHDIR|CD [/D] [drive:][path]
CD ::顯示當前目錄的路徑
CD .. ::進入上級目錄
CD [drive:path] ::進入特定目錄
CD [path] ::進入當前目錄的子目錄
CD\ ::跳到當前驅動器的根目錄
CD \[name] ::將當前文件夾改名爲 name
Drive: ::進入特定驅動器
```

#### 創建
```bat
MKDIR|MD [drive:]path
MD drive:path ::在特定驅動器下建立文件夾
MD path ::在當前文件夾下建立子文件夾
```

#### 刪除
```bat
RMDIR|RM [drive]:path [/S] [/Q]
```
不帶參數時衹刪空目錄

## 文件類

### 移動
```bat
MOVE [/Y|/-Y] [drive:][path]dirname1 dirname2
MOVE [/Y|/-Y] [source] [destination]
```
前面是官方的，但我認爲後者淸楚一點

#### 重命名
```bat
RENAME|REN [drive:][path]filename1 filename2
```

#### 刪除
```bat
DEL|ERASE [/P] [/F] [/S] [/Q] [/A[[:]attributes]] names
```

### 複製與合倂☯
#### COPY
```bat
COPY [/D] [/V] [/N] [/Y | /-Y] [/Z] [/L] [/A | /B ] source [/A | /B] [+ source [/A | /B] [+ ...]] [destination [/A | /B]]
```
兩種合倂方式： copy *.txt all.txt 以及 copy 1.txt + 2.txt + 3.txt all.txt

#### XCOPY
複製文件和目錄樹，一般用不上這麼強悍的命令
```bat
XCOPY source [destination] [/A | /M] [/D[:date]] [/P] [/S [/E]] [/V] [/W] [/C] [/I] [/Q] [/F] [/L] [/G] [/H] [/R] [/T] [/U] [/K] [/N] [/O] [/X] [/Y] [/-Y] [/Z] [/B] [/EXCLUDE:file1[+file2][+file3]...]
```

## 變量☯

`%0` 批處理命令本身
`%1`-`%9` 表示以空格分隔的參數，比如有個 a.bat 文件，他的命令是 `MOVE %3 D:\1` ，在 DOS 執行 `a.bat 1.txt 2.txt 3.txt` 時， `%3` 就代表 `3.txt`
`~x,y` 表示字符串的第 x 到 y 個字符，但注意他數數從 0 開始，不是 1 。比如 `%date:~0,10%` ，就是形如 2014/01/01 這樣的東西

### 設定
```bat
SET [variable=[string]]
```
定義好之後，使用 `%variable%` 就表示那串 string ，比如 `SET hw=hello world` ，以後所有 `%hw%` 就代表 hello world

形如 `SET v` 的意思是羅列所有 v 開頭的 variables ，如果沒有，會將 `ERRORLEVEL` 設定爲 1
由於需要使用 `=` 號定義，所以變量名不能包含 = 號
可以一次設定很多個變量，不同變量用空格隔開

### 用戶輸入
```bat
SET /P variable=[promptString]
```
參數 `/P` 允許用戶在運行腳本時輸入變量，而 promptString 會作爲提示顯示，比如可以設置成「請輸入一個數」，用戶輸入一個數後，變量的値從「請輸入一個數」變成用戶輸入的數

### 運算
```bat
SET /A expression
```
這 expression 可以是如 `a=1+2` 的純數字運算，可以是變量間運算，也可以是變量和數字間的運算
這裏的運算不支持對小數的運算，結果如果有小數，一律抹去取整
支持的運算符有：
`,` 表達式之間的分隔符，比如 `a=b+c,b=c+d`
算術運算符： `+` `-` `*` `/` `(` `)` `%`
邏輯移位： `<<` `>>` ，個人理解 `a"<<"b=a*2^b a">>"b` 就是 `a/2^b`
與：雖然我們一般以 `m^n` 表示 m 的 n 次方，但在批處理裏是與 `abc^defg` 是 `abcdefg`
`&` 不懂是什麼意思，寫的時候要加 `""`
特殊寫法 `var*=2` 就是 `var=var*2` ，上面的全都可以這麼寫
一元運算符： `!` 邏輯非， `~` 按位求反（個人理解 `~a` 是 `-a-1` ）， `|` 或

#### 內置變量不經設定，本來就存在的變量：
`%CD%` `%DATE`% `%TIME%` `%RANDOM%` `%ERRORLEVEL%`
以上不用說，剩下不重要，眞省事

#### 臨時設置環境變量
```bat
PATH=[%path%;][drive:]path
SET PATH=%path%;[drive:]path
```
臨時設置環境變量，僅在批處理內有效，多個文件夾用 `;` 分隔，後者是在 DOS 中的用法

## IF 語句☯
```bat
IF [NOT] ERRORLEVEL number command
IF [NOT] string1==string2 command
IF [NOT] EXIST filename command
[ELSE command]
```
有點編程基礎就知道，這是簡單的條件語句。
可以單用 `IF [NOT]` ，也可以多配個 `ELSE` ，或者一個 `IF` 配個 `IF NOT` ，這是靈活的
關於語句的判斷，還支持這些數學上的：
`EQU` 等於
`NEQ` 不等於
`LSS` 小於
`LEQ` 小於等於
`GTR` 大於
`GEQ` 大於等於

### 循環
IF 結合 GOTO 可以變成循環，是個不錯的用法：
```bat
@ECHO OFF
SET var=0
:continue
SET /A var+=1
echo 第 %var% 次循環
IF %var% lss 100 GOTO continue
ECHO 循環結束
PAUSE
```

## FOR 語句☯
這一節複雜度比較高，囉嗦的話寫幾萬字都講不完。
```bat
FOR [[drive:]path]] %variable IN (set) DO command [command-parameters]
```
注意：批處理中， `%variable` 應寫作 `%%variable` ，並且是區分大小寫的

`(set)` 是一組文件或字符等，可使用通配符如 `*.txt` ，也可以是用分號、逗號、空格等分隔的一串
`(set)` 會被逐個提取成變量，執行 `DO` ，再提取下一個，而不是一次提取完了再 `DO`
`DO` 後面的語句可以加上 `()` ，然後斷行，這樣看起來倒是挺整齊的
擴展命令：

### 僅匹配文件夾
```bat
FOR /D %variable IN (set) DO command [command-parameters]
```

### 檢查整個目錄樹
```bat
FOR /R [[drive:]path] %variable IN (set) DO command [command-parameters]
```

### 等差數列
```bat
FOR /L %variable IN (start,step,end) DO command [command-parameters]
```
程序會根據 `(start,step,end)` 生成等差數列，再執行任務

### 逐行分析文件
```bat
FOR /F ["options"] %variable IN (file-set|"string"|'command') DO command [command-parameters]
```
之前的命令執行 DO 的時候，是逐個文件的，現在是文件逐行 DO 。 其中 options 豐富了命令的多樣性：

#### 忽略指定字符開頭的行
`eol=.`
`.` 代表任何一個字符，衹能是一個，不然報錯，弱爆了的命令
默認情況下， `FOR /F` 會忽略以 `;` 開頭的行，以便寫註釋什麼的，使用 `"eol="` 時纔會讀取以 `;` 開頭的行

#### 跳過若干行
`skip=n`
跳過前 `n` 行，從第 `n+1` 行開始讀取

#### 按符號截取
`delims=符號表`
假設符號表爲 `.,` ，則僅保留 `(file-set|"string"|'command')` 中每一行的第一個 . 或 , 前面的部分，比如 hello, world 會被截取成 hello

#### 按字符位置截取
`tokens=x,y,m-n`
x, y, m, n 都是數字或者 * 號
單獨使用時，表示截取第 x, y, 還有 m-n 個字符
可與 `delims` 結合變成新的奇葩用法，比如 `"delims=, tokens=3"` ，被截取對象是 hello,world,hi,bat ，則截取 hi 。
與 `delims` 結合時，如果 `tokens` 有多個，則截取後分配到多個變量中。比如
```bat
FOR /F "delims=, tokens=1,3-4" %%i IN (test.txt) DO ECHO %%i %%j
```
假設 test.txt 就是 hello,world,hi,bat 則輸出 hello hi bat
* 號不單獨用，表示剩下的。比如
```bat
FOR /F "delims=, tokens=1-2,*" %i IN (test.txt) DO ECHO %i %j
```
輸出爲 hello world hi,bat 。

#### 允許文件名出現奇怪的字符
`usebackq`
使用後，在 `(file-set)` 加上 " 就行了。比如 hello world.txt ，不寫成 "hello world.txt" 會報錯的……
`("string")` 要改成 `('string')`
`('command')` 也隨之改成 `(\`command\`)`

#### 額外處理 variable今有一個變量 %%I ，當他加上其他參數時：
```bat
%%~I ::刪除引號
%%~fI ::合法的完整路徑 full
%%~dI ::僅驅動器 drive
%%~pI ::僅路徑 path
%%~nI ::僅文件名 name
%%~xI ::僅擴展名 extend
%%~sI ::路徑僅縮略名
%%~aI ::文件屬性 attribute
%%~tI ::文件日期、時間 time
%%~zI ::文件大小
```
可以搭配使用，比如 `%%~nxI` ，就是文件名加擴展名

## 功能增強
VBScript 或 PowerShell 。

## 二逼自娛腳本

#### 打包器
WinRAR 的逐個文件夾打包功能會把文件夾包進去，用這個腳本來剃掉文件夾。
```bat
FOR /D %%I IN (*) DO (
CD %%I
"C:\Program Files\WinRAR\winrar" u -afzip "%%I" *.* -m5
MOVE /Y "%%I".zip F:\s&CD ..
)
```

#### 永久添加環境變量
原理是利用註冊表來添加環境變量。
```bat
@echo off
SET regpath=HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
SET /P newpath=輸入要添加的文件夾
reg add "%regpath%" /v "path" /d "%%path%%;%%thepath%%" /f
```