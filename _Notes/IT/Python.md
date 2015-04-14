---
layout: indexed
title: Python 半小時上手
date: '2014/08/08'
---
Python 隨便學學就能解決很多小問題，是最易學習的編程語言之一。同樣一個問題，找 C 可能要寫 100 行代碼，但 Python 寫 20 行就夠了。 C 的那 100 行可能包含了 100 個知識點，而 Python 就是 20 個。
Python 好處極多，對一般用戶來說最明顯的是腳本運行和環境簡單。 Python 腳本可以直接使用，不像 C, VB 等需要編譯。 Python 是跨平臺的，集成在不少系統裏，沒集成的系統也衹需要下載很小的安裝包，模塊也可通過 pip 等手段快速獲得。

學習 Python ，如果學時超過五小時還不能寫點實用小腳本，則必是以下幾種可能：
一、跟電腦、編程八字不合或幾乎沒摸過電腦。
二、智力發育不全、受敎育程度低或年過古稀。
三、所讀敎程太專業或重點不淸。
其中第三點的可能性最高，因爲前二者多半不會想學 Python ，或者乾脆不知道這是什麼玩意。其實五小時就已經是很長很長的時間，因爲正常人一天能高度集中精力的時間也就五小時左右，再多就容易精神渙散，衹能做複習、用舊貨之類相對輕鬆的活動。很多敎程容易陷入學術化的泥沼裏，忘記了其實用本質。這就像本來衹想敎別人如何計算圓的面積，結果一不小心把整個平面幾何和微積分全部講完，而讀者在學到三角函數的時候已經決定放棄了。

本文的目標是掛一漏萬、避難趨易，讓讀者自己提綱挈領、綱舉目張。多數人應能半小時內讀完並對大部分內容有印象，而且這些內容「剛好」是最重要的——至少我自己用到過，所以覺得重要。

## 正確學習方法

### 有問題找模塊
模塊之於編程語言，就像軟件之於操作系統，需要就裝。在操作系統裏，想下載就裝個下載軟件，想 P 圖就裝個 PS ，編程也是如此。記住這點，至少 Python 這門特別容易的語言就入門了一半。很多問題坐在那裏用基本命令想會想死的，但有了模塊就立馬解決。
模塊的用法也很簡單，下載，解壓，放在 Lib 目錄，然後在腳本的開頭寫形如 import xlib 的就行了。有的大型模塊需要專門安裝，這些文檔裏都會有。多個模塊用 , 分隔或寫多行 import xlib 。
我的常用模塊：
os, shutil 處理文件與文件夾
requests 網頁訪問與下載
re 正則表達式
sys 與 bat 對接
threading 多線程
tkinter 簡單易上手的 GUI
pyinstaller 打包 exe 給沒有 Python 的機子用

如果想知道自己引用的模塊有什麼命令，可以使用類似這樣的命令：
{% highlight python %}print(dir(xlib)){% endhighlight %}
由於絕大多數敎程都會把這一節放到書末且往往不得要領（比如大篇幅討論如何寫模塊，卻不告訴讀者早就有很多無比好用的模塊，簡直本末倒置），導致學習者讀到之前就失去耐心，卽使讀到也不知道是幹嘛用的，本文特地放到前面來。

### 讀文檔
這在使用開源軟件裏面簡直是憲法第一條。用模塊肯定要看文檔的，不用說。

### 邊用邊學
把本文迅速瀏覽一遍就可以寫了，寫自己想寫的。比如抓網站，或者按需生成文件，反正想幹嘛就幹嘛，別太複雜就行。至於那些 tutorial 、習題，對非專業人員就是浪費腦細胞，有空再說。

### 搞淸版本
Python 有 2 和 3 ，官方力推 3 ，但是可能改動太大還是怎麼了，反正遇到了很大的阻力，所以現在二者並存。 3 的命令格式更嚴格、規範一點， 2 比較鬆散。網上很多討論以及第三方模塊都是基於 2 的，不一定能直接使用。用 3 有個福利，那就是對 unicode 的處理好。所以試了一段時間後，我決定用 3 。

## 安裝與使用
第一步：下載，安上。
第二步：設置好環境變量（可能自動就設好了，免去這一步）。
現在可以雙擊運行 .py 腳本了，但是如果有 bug 會閃退，怎麼辦呢？很簡單，在命令行打形如 python yourscript.py 的一串就行。
也許還有第三步：裝模塊。有的模塊需要到官網下載，更多的常用模塊是 cmd 或 bash 跑一下 pip install blablabla 或 easy_install blablabla 就行了。
第三步 pip 不成功的話，走第四步： http://www.lfd.uci.edu/~gohlke/pythonlibs/

## 基本要求與命令

#### 註釋
同一行內 # 後的都算註釋。
多行註釋在開頭和結尾後用 \"\"\" 。

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

#### 置換
{% highlight python %}
a,b =b,a
{% endhighlight %}
這就把 a 和 b 兩個變量的値對調了。

#### 轉換
{% highlight python %}int(var) # 轉成整數
float(var) # 轉成浮點數
str(var) # 轉成字符串{% endhighlight %}
還有很多，記住這三個基本夠用了。

#### 切片
{% highlight python %}str[m:n] # str 的第 m+1 到第 n 個字符
str[m:] # str 的第 m+1 及以後的字符
str[:n] # str 的第 1 到第 n 個字符
list[m:n] # list 的第 m+1 到第 n 個元素，參照字符串的情況{% endhighlight %}

#### 字符串類變量的一些簡單處理
可以先定義字符串，然後用形如 str1.find("some") 的命令，也可以直接對字符串作用
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
{% highlight python linenos %}
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
{% highlight python linenos %}
while 情況 :
	執行
else: # 這個不必要
	執行{% endhighlight %}
while 循環也可以像 if 那樣嵌套起來。

### for 循環
{% highlight python linenos %}
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
		print >>f,i
{% endhighlight %}

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
回想一下代數，什麼是函數。其實這寫法就相當說定義一個函數比如 f(x,y,z)= 什麼什麼。等到要用這函數的時候，再塡寫一下具體的 x,y,z 就行了。定義沒有 parameter 也可以，但這樣使用的時候也沒有。
其實所有命令都可以看作是函數。
如果想在函數外使用 return 回來的變量，最簡單的方法就是把變量全局化。比如：
{% highlight python linenos %}
def func():
	global a,b
	return (a, b)
{% endhighlight %}
執行完後，整個腳本都會獲得變量 a 和 b 。不然 a 和 b 在運行完腳本之後就不見了。
或者用另一種方法來傳遞：
{% highlight python linenos %}
def func():
	return (a, b)
c, d = func()
{% endhighlight %}
a 和 b 消失了，但他們的値被 c 和 d 繼承。

### 高階函數
來個複雜一點的例子：
{% highlight python linenos %}
def func(a,b):
	return a(b)
{% endhighlight %}
func 中的變量 a 同時也是一個函數，所以 func 就是個高階函數。實際上，有個叫 `map()` 的內置函數就跟這個 func 很類似。

### 匿名函數
看起來有點雞肋，不過有時卻是必須的。
{% highlight python %}
lambda [arg1 [,arg2,.....argn]]:expression
{% endhighlight %}

## 異常處理
有時候，代碼沒寫錯，但運行環境出錯，比如下載東西服務器的回饋出錯，或者用戶手賤之類。於是就有了異常處理。下面提供最簡單的例子：
{% highlight python linenos %}
try:
	down(link)
except BaseException:
	print("die")
else:
	print("good")
{% endhighlight %}
例子中的 down 是個下載函數，函數說好回饋 200 時怎樣、 404 304 302 怎樣，但還是可能有各種問題，所以在 `except` 裏說，如果出現 `BaseException` 狀況，一律顯示 die 。 `BaseException` 指的是所有異常情況，具體見 <a href="https://docs.python.org/3/library/exceptions.html#concrete-exceptions" rel="external">文檔</a>，或快速查看<a href="http://www.w3cschool.cc/python/python-exceptions.html" rel="external">中文簡表</a>。

## 面向對象編程 *
零基礎半小時內理解面向對象編程 (OOP) 思想幾乎是不可能的，而 Python 單用函數編程也行，所以這裏算是選學部分。不過 OOP 在處理較大量非常類似的物件時有很大優勢，還是有必要介紹一下的。

#### 槪念
類：比如四個東西， Washington, Jefferson, Roosevelt, Lincoln ，屬於什麼類？ Human 。
對象：比如 Washington ，他就是 Human 的一個對象。
繼承： Human 裏有很多類別，比如 Caucasian 這個子類。 Caucasian 具有 Human 的全部特性，這叫繼承。其中， Human 是父類， Caucasian 是子類。
類可以有很多項屬性和動作，建立好類，每個對象像套用函數一樣用類來決定行爲就行了，類就像個模板一樣。所以 OOP 對於需要到很多個對象的編程是比較方便的。

#### 例子
{% highlight python linenos %}
class Human (Object): # class 是聲明建立類， Human 是類名 ， Object 是常用的最高父類
	def __init__(self, name, born): # __init__ 是個方法，第一個變量永遠是 self
		self.name = name
		self.born = born
	def age(self): # 際要用到 name 和 born ，但現在衹需要寫 self 了
		print (self.name+' is '+str(2015-self.born)+' years old')
# 定義好類，再把一個對象的參數寫進去：
w = Human('Washington', 1732)
# 想看 w 記的是哪個名字時執行：
w.name
# 想要看 Washington 的年齡時執行：
w.age()
# 再建立個 Caucasian
class Caucasian (Human):
# 有了 Human 打底，不用再 __init__ ：
	def skin(self):
		print('White')
{% endhighlight %}

## 書籍
<a href="http://www.amazon.com/Beginning-Python-From-Novice-Professional/dp/159059519X" rel="external">Beginning Python: from Novice to Professional</a> 本文沒有覆蓋的基礎內容。
<a href="http://www.amazon.com/Python-Essential-Reference-4th-Edition/dp/0672329786" rel="external">Python Essential Reference</a> 一個較全面且不囉嗦的敎材，進階用爲主。
<a href="http://shop.oreilly.com/product/0636920028154.do" rel="external">Learning Python</a> 囉嗦的來了。
<a href="http://www.amazon.com/Python-Standard-Library-Example-Developers/dp/0321767349" rel="external">The Python Standard Library by Example</a> 標準庫能讀完，也算民間高手了。
<a href="http://www.amazon.com/Python-Practice-Concurrency-Libraries-Developers/dp/0321905636" rel="external">Python in Practice: Create Better Programs Using Concurrency, Libraries, and Patterns</a> 進階書，用得到的話可以看。

## 網頁
<a href="https://docs.python.org/3/" rel="external">官方文檔</a>，<a href="http://www.pythondoc.com/pythontutorial3/index.html" rel="external">中文版</a>
<a href="http://woodpecker.org.cn/abyteofpython_cn/chinese/" rel="external">简明 Python 教程</a> 可以作爲簡易快速的備查。
<a href="http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000" rel="external">Python 教程</a> 在中文 IT 敎程裏，也算佼佼者了。
<a href="http://docs.python-guide.org/en/latest/" rel="external">The Hitchhiker’s Guide to Python</a> 不少深入的話題，値得認眞讀。
<a href="https://docs.python.org/3/reference/index.html" rel="external">The Python Language Reference</a> 系統的手冊。
<a href="http://diveintopython.org/" rel="external">Dive into Python</a> 確實較深入。
<a href="https://github.com/qyuhen/book/" rel="external">Python 学习笔记</a> 講得比較深，但是用的是 Python 2 。
<a href="http://learnpythonthehardway.org/book/" rel="external">Learn Python the Hard Way</a> 用來學未免蠢，用來複習提高倒不錯。
<a href="https://www.codecademy.com/glossary/python" rel="external">Codecademy</a> Python 習題，容易得有回到幼兒園的感覺。