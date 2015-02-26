---
layout: indexed
title: Python 半小時上手
date: '2014/08/08'
---
Python 隨便學學就能用來解決很多小問題，比所謂最易學的「易語言」容易多了。很多時候，與其找一堆亂七八糟工具，不如動動手，寫一段十來行的腳本，效果反而更好，還能預防老年癡獃。
Python 的好處極多，對一般用戶來說最明顯的兩點是腳本運行和環境簡單。 Python 寫出來的小玩意不需要編譯就能直接使用，不像 C, VB 等需要編譯。其次是 Python 是跨平臺的，集成在不少系統裏，沒有集成的系統也衹需要下載一個很小的安裝包，很多模塊也可通過 pip 等手段快速獲得。
如果學時超過五小時還不能寫點實用小腳本，則必是以下幾種可能：
一、跟電腦、編程八字不合或幾乎沒摸過電腦。
二、智力發育不全、受敎育程度低或年過古稀。
三、所讀敎程太專業或重點不淸。
其中第三點的可能性最高，因爲前二者多半不會想學 Python ，或者乾脆不知道這是什麼玩意。其實五小時是很長的時間，因爲正常人一天能高度集中精力的時間也就五小時左右，再多就容易精神渙散，衹能做複習、用舊貨之類相對輕鬆的活動。
本文的目標是掛一漏萬、避難趨易，讓讀者自己提綱挈領、綱舉目張。多數人應能半小時內讀完並對大部分內容有印象，而且這些內容「剛好」是最重要的。

## 正確的學習方法

### 有問題找模塊
江靑死了找不到，那就找模塊。模塊就像操作系統上的插件，需要就用。而 Python 正好模塊挺多，所以就像操作系統裏的 Windows 一樣，很容易找到解決方案。
對一般人而言，記住這點， Python 就學會了一半。很多問題坐在那裏用基本命令想會想死的，有問題搜一下看哪個模塊能解決。比如下載，用基本命令搞死人，用模塊 urllib 馬上好。
模塊的用法也很簡單，下載，解壓，放在 Lib 目錄，然後在腳本的開頭寫形如 import xlib 的，就行了。多個模塊用 , 分隔或寫多行 import xlib 。
我的常用模塊：
os, shutil 和 glob 處理文件與文件夾
requests, urllib/urllib.request 和 httplib/http.client, <a href="http://pycurl.sourceforge.net/" rel="external">PycURL</a> 網頁訪問與下載
re 正則表達式
threading 多線程

如果想知道自己引用的模塊有什麼命令，可以使用類似這樣的命令：
{% highlight python %}print(dir(xlib))
"many words"{% endhighlight %}
由於絕大多數敎程都會把這一節放到書末且往往不得要領（比如大篇幅討論如何寫模塊，卻不告訴讀者早就有很多無比好用的模塊，簡直本末倒置），導致學習者讀到之前就失去耐心，卽使讀到也不知道是幹嘛用的，本文特地放到前面來。

### 讀文檔
這在使用開源軟件裏面簡直是憲法第一條。用模塊肯定要看文檔的，不用說。

### 邊用邊學
把本文迅速瀏覽一遍就可以寫了，寫自己想寫的。比如抓網站，或者按需生成文件，反正想幹嘛就幹嘛，別太複雜就行。至於那些 tutorial 、習題，對非專業人員就是浪費腦細胞，有空再說。
使用時記住：反正 Python 是很強大的，無所不能的，遊戲 Civilization IV 和網盤 Dropbox 就是 Python 寫的，做不到說明自己水平不到而已。

### 搞淸版本
Python 有 2 和 3 ，官方力推 3 ，但是可能改動太大還是怎麼了，反正遇到了很大的阻力，所以現在二者並存。 3 的命令格式更嚴格、規範一點， 2 比較鬆散。網上很多討論以及第三方模塊都是基於 2 的，不一定能直接使用。
用 3 有個福利，那就是對 unicode 的處理好。所以我還用 3 。

## 安裝與使用
第一步，下載，安上。
第二步，設置好環境變量。
現在可以雙擊運行 .py 腳本了，但是如果有 bug 會閃退，怎麼辦呢？很簡單，在命令行打形如 python yourscript.py 的一串就行。
也許還有第三步：裝模塊。有的模塊需要到官網下載，更多的常用模塊是 cmd 或 bash 跑一下 pip install blablabla 或 easy_install blablabla 就行了。

## 基本要求與命令

#### 註釋
同一行內 # 後的都算註釋。
多行註釋在開頭和結尾後用 """ 。

#### 字符串
字符串就是一串字符。凡字符串都加引號，數字不加，所以 "123" 和 123 是不同的。
{% highlight python %}'word'
'\n' # 這是個換行
"many words"{% endhighlight %}

#### 命令的格式
基本上，命令遵循這樣的格式：
{% highlight python %}command(values,others){% endhighlight %}
其中， values 是被執行對象，而 others 通常是一些參數之類的，比如要不要緩存之類。
但是，因爲命令經常被用來用去，次次寫很麻煩，所以我們經常會寫成一個變量的樣子：
{% highlight python %}name=command(values,others){% endhighlight %}

#### 幫助
格式是 help(command) ，記住就好，可以經常看看，非常有助於提高。

#### 打開文件 open
{% highlight python %}file1=open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None){% endhighlight %}
記得加上引號。用完後加上個 closed 。
這個命令裏展示了一堆默認模式，不寫就是默認的，當然可以寫別的。
重點介紹幾個 mode ：
r 直讀（默認）
w 純寫入，如果存在就覆蓋，不存在就創建
w+ 讀寫，如果存在就覆蓋，不存在就創建

#### 輸出 print
{% highlight python %}print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
{% endhighlight %}
一般就寫個 value 和 file ， value 寫得最多。
Python 2 可以用 print value 這個格式，但跟基本格式不同，所以在 3 中被拋棄了。
還有一種比較特殊的寫法：
v1="a"
v2="b"
{% highlight python %}print "1 %s 2 %s." % (v1, v2)
{% endhighlight %}
這樣實際出現的是 1 a 2 b 。這種寫法讓句子比較連貫一些，不過要小心數錯……

#### 其他
看<a href="http://www.cnblogs.com/vamei/archive/2012/11/09/2762224.html" rel="external">這裏</a>。

## 變量

#### 賦値
變量的名稱除了那幾十個保留字隨便用。變量的類型有，有數字、字符串、列表（一串字符串或數字或二者都有）、元組（衹讀的列表）、字典。可以這麼定義：
{% highlight python %}var=123 # 數字
var="string" # 字符串
var=[1,2,'ok'] # 列表
var={'name':'Tom','age':15,'race':'Caucasian'} # 字典
var1=var2=var3=123 # 賦予相同的値
var1,var2,var3=123,456,"string" # 簡寫模式
var=raw_input("Prompt") # 請用戶輸入變量，屬性是字符串，這命令僅在 Python 2 可用
var=input("Prompt") # 輸入的是可以運算的，比如輸入 1+1 ，得到不是字符串 "1+1" ，而是 2 ；但在 Python 3 效果等同與 2 中的 raw_input{% endhighlight %}

#### 轉換
{% highlight python %}int(var) # 轉成整數
float(var) # 轉成浮點數
str(var) # 轉成字符串{% endhighlight %}
還有很多，記住這三個基本夠用了。

#### 裁剪
{% highlight python %}str[m:n] # str 的第 m+1 到第 n 個字符
str[m:] # str 的第 m+1 及以後的字符
str[:n] # str 的第 1 到第 n 個字符
list[m:n] # list 的第 m+1 到第 n 個元素，參照字符串的情況{% endhighlight %}

#### 字符串類變量的一些處理
可以先定義字符串，然後用形如 str.find("some") 的命令，也可以直接對字符串作用
{% highlight python %}"some texts".find("some") # 查找，會返回位置，比如這裏會返回 0 ，如果找不到就返回 -1
"some texts".replase("some","no") # 替換{% endhighlight %}
還有其他處理如 join, split, lower, translate, strip，這裏不討論。

#### 運算
{% highlight python %}var=1+var1 # 與數字
var="string"+var # 與字符串
var=var1+var2 # 變量之間{% endhighlight %}
算術運算符：除了最簡單的 + - * / % ，還有 ** 乘方， // 整除。
比較運算符：== 等於， != 或 <> 不等於， > < >= <= 這四個比較簡單。
賦値運算符：算術運算符後面加個等號，比如 a+=b 相當於 a=a+b 。

## 語句

### if 條件
{% highlight python %}
if 條件 : # 不同條件可以用 and 和 or 來連接
	執行
elif 條件 : # 這句可以不用，也可以用很多個
	執行
else: # 其實也經常不寫
	執行{% endhighlight %}
需要注意的是縮進，縮進不對是不行的。而且有時還能用到嵌套：
{% highlight python %}if 條件 :
	執行
	if 條件 :
		執行
	else:
		執行
else:
	執行{% endhighlight %}
如果搞錯縮進就亂套了。

### while 循環
{% highlight python %}
while 情況 :
	執行
else: # 這個不必要
	執行{% endhighlight %}
while 循環也可以像 if 那樣嵌套起來。

### for 循環
{% highlight python %}
for var in list/string:
	執行
else: # 這個不必要
	執行{% endhighlight %}
僅用於有一個列表或者字符串，不過列表可以用命令製造，比如最常見的 range(1,100) 。
這個循環一出，等於定義了一個變量 var ，好好在循環裏用他就是了。
for 循環也可以像 if 那樣嵌套起來。比如這個腳本，是列出所有 1935-1984 年的月份，並且寫成 yyyymm 格式，輸出到 yyyymm.txt：
{% highlight python linenos %}f=file("yyyymm.txt", "w")
for year in range(1935,1985):
	for month in range(1,13):
		i=str(year)+str(month).zfill(2)
		print >>f,i{% endhighlight %}

### break
用於提前跳出循環，通常是一個循環裏面套了個 if ，滿足條件了就跳出來。
其實我個人更喜歡用 input() 來終止程序，因爲窗口會保留。

### continue
還是循環裏套了個 if ，比如一個循環內部有幾百行，很煩，走到若干行後一個 if 滿足條件，這輪循環不走了，直接開始走下一輪。

### pass
就是空語句，爲了保持完整性而使用。比如在 if 裏用 pass ，然後 else 的時候執行。

## 函數
{% highlight python linenos %}def FunctionName(parameters):
	commands # 有很多行可以用 ; 來分割一下
	return # 函數終結，返回一個値，可以返回 True False 這樣的邏輯判斷，或者數字、字符串、變量，還能順便運算一下，比如返回個 a+b 。如果要返回多個値，這麼寫： return (a,b,c)
FunctionName(independent parameters){% endhighlight %}
回想一下初中代數，什麼是函數。其實這個寫法就相當說定義一個函數比如 f(x,y,z)= 什麼什麼。等到要用這個函數的時候，再塡寫一下具體的 x,y,z 就行了，當然塡寫 parameters 的時候可以用變量，可以放進循環裏寫， blablabla ，反正到處用。定義的使用沒有 parameter 也可以，但這樣使用的時候也沒有。
其實所有命令都可以看作是函數。

## Cheat Examples
我不喜歡 cheatsheets ，脫離上下文的代碼經常讓人看不懂。所以我寫 cheat examples 。
### PycURL
一個簡單的下載函數。
{% highlight python linenos %}
import os, pycurl
def dxDown(url, fullpath):
	c=pycurl.Curl() # 縮寫一下
	c.setopt(pycurl.PROXY, "127.0.0.1:1080") # 掛代理
	c.setopt(pycurl.PROXYUSERPWD, "name:pass") # 代理的用戶名密碼
	c.setopt(c.FOLLOWLOCATION, True) # 允許重定向
	c.setopt(pycurl.TIMEOUT, 5000) # 超時設定
	c.setopt(pycurl.USERAGENT, b"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)") # 模擬瀏覽器
	c.setopt(pycurl.URL, url) # 訪問指定網址
	c.setopt(pycurl.COOKIEJAR, 'cookie.txt') # 把 cookie 存到文件
	c.setopt(pycurl.COOKIEFILE, "cookie.txt") # 用文件掛 cookie
	f = open(fullpath, 'wb') # 定義一個文件
	c.setopt(c.WRITEDATA, f) # 指定返回信息的寫入文件，或作 c.setopt(c.WRITEFUNCTION, f.write)
	c.perform() # 獲得服務器返回信息
	hc=c.getinfo(pycurl.HTTP_CODE) # HTTP 信息，如 200 、 404 ，需 perform
	f.close() # 關閉文件，不然會一直佔用
	if hc != 200: # 如果 HTTP_CODE 不是 200
		os.remove(fullpath) # 那就刪掉咯
{% endhighlight %}

## 延伸學習
<a href="http://www.amazon.com/Python-Essential-Reference-4th-Edition/dp/0672329786" rel="external">Python Essential Reference</a>一個較全面且不囉嗦的敎材。
<a href="https://docs.python.org/2.7/tutorial/index.html" rel="external">官方 Tutorial</a>，<a href="http://www.pythondoc.com/pythontutorial27/index.html" rel="external">中文版</a>
<a href="http://woodpecker.org.cn/abyteofpython_cn/chinese/" rel="external">简明 Python 教程</a> 可以作爲簡易快速的備查。
<a href="http://shop.oreilly.com/product/0636920028154.do" rel="external">Learning Python</a> 本文講得不詳細的地方找這本書就對了。
<a href="http://shop.oreilly.com/product/0636920027072.do" rel="external">Python Cookbook</a> 惡俗一點的說，就是 Python 實戰寶典。這本和上一本都有中文版，網上很多，隨便下載。
<a href="http://diveintopython.org/" rel="external">Dive into Python</a> 雖然有點舊，不過確實比較深入，再用比較惡俗的說法，叫 Python 高級敎程。
<a href="www.codecademy.com/glossary/python" rel="external">Codecademy</a> 可以叫 Python 習題集吧，解答在 Google 。