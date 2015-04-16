---
layout: indexed
title: Python 半小時上手
date: '2014/08/08'
---
學習 Python ，如果學時超過五小時還不能寫點實用小腳本，則必是以下幾種可能：
一、跟電腦、編程八字不合或幾乎沒摸過電腦。
二、智力發育不全、受敎育程度低或年過古稀。
三、所讀敎程太專業或重點不淸。
其中第三點的可能性最高，因爲前二者多半不會想學 Python ，或者乾脆不知道這是什麼玩意。問題就是第三點了。
很多敎程容易陷入學術化的泥沼，忘記了實用本質。這就像本來衹想敎人計算圓的面積，結果一不小心把整個平面幾何和微積分全部講完，而讀者在學到三角函數的時候已決定放棄了。
本文的目標是掛一漏萬、避難趨易，讓讀者自己提綱挈領、綱舉目張。多數人應能半小時內讀完並對大部分內容有印象，而且這些內容「剛好」是最重要的——至少我自己用到過，所以覺得重要。

## 優勢
當下流行的程序語言，都有其各自的優越性， Python 也不例外：
1. 易學。編寫同樣一個程序， Python 需要的知識點往往是最少之一。
2. 易讀。 Python 簡潔、單一最優解、強制縮進，不故意噁心都好讀。
3. 易配。多數 Linux 和 Unix 發行版內置， Windows 下也衹需很小的安裝包。
4. 易用。 Python 不必手動編譯，雙擊腳本就能跑。
5. 易抄。 Python 開源社區活躍，提問也很快得到解決。

## 正確學習方法

#### 有問題找模塊
模塊之於編程語言，就像軟件之於操作系統。在操作系統裏，想下載就裝下載軟件，想 P 圖就裝 PS ，編程也是如此。
我的常用模塊（基本是標準庫）：
os, shutil 處理文件與文件夾
requests 網頁訪問與下載
re 正則表達式
threading 多線程
tkinter 簡單易上手的 GUI
由於絕大多數敎程都會把這一節放到書末且往往不得要領（比如大篇幅討論如何寫模塊，卻不告訴讀者早就有很多無比好用的模塊，簡直本末倒置），導致學習者讀到之前就失去耐心，卽使讀到也不知道是幹嘛用的，本文特地放到最前。

#### 讀文檔
這在使用開源軟件裏面簡直是憲法第一條。用模塊肯定要看文檔的，不用說。

#### 邊用邊學
把本文迅速瀏覽一遍就可以寫了，寫自己想寫的。比如抓網站，或者按需生成文件，想幹嘛就幹嘛，別太複雜就行。至於那些 tutorial 、習題，對非專業人員就是浪費腦細胞，有空再說。

#### 搞淸版本
Python 有 2 和 3 ，官方力推 3 ，但推廣遇到了很大的阻力，所以現在二者並存。 3 的命令格式更嚴格、規範， 2 比較鬆散。網上很多討論以及模塊都是基於 2 的，不一定能直接用。
用 3 有個福利，那就是對 unicode 的處理好。所以試了一段時間後，我決定用 3 。

## 基本要求與命令

#### 文件名後綴
`.py`: 最常見的後綴
`.pyw`: 執行時不帶 console
`.pyc`: Python 運行需要轉換成字節代碼 `.pyc` ，不需手動操作，想手動時在 console 執行：
{% highlight python linenos %}
import py_compile
py_compile.compile('something.py')
{% endhighlight %}
`.pyo`: 優化的，在 Terminal 或 CMD 下執行： `python -O -m py_compile something.py`


#### 文件頭
在 *nix 下運行 Python 腳本，第一行應加 `#!/usr/bin/env python3.4` 。
非 unicode 腳本，應加 `# -*- coding: gb18030 -*-` 之類的內容。

#### 註釋
同一行內 `#` 後的都算註釋。
多行註釋在開頭和結尾後用 `'''` 。

#### 字符串
字符串就是一串字符。凡字符串都加引號，數字不加，所以 `"123"` 和 `123` 是不同的。
{% highlight python %}
'word'
'\n' # 這是個換行
'\u0020' # 支持 unicode
"It's a string."
{% endhighlight %}

#### 幫助
格式是 help(command) ，記住就好，可以經常看看，非常有助於提高。

#### 輸出 print
{% highlight python %}print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
{% endhighlight %}
一般就寫個 value 和 file ， value 寫得最多。
Python 2 可以用 `print value` 這個格式，但跟基本格式不同，所以在 3 中被拋棄了。

#### 其他
看<a href="http://www.cnblogs.com/vamei/archive/2012/11/09/2762224.html" rel="external">這裏</a>。

## 變量

#### 保留字
這些詞是 Python 的內置命令，不能用作變量名：
ArithmeticError, AssertionError, AttributeError, DeprecationWarning, EOFError, Ellipsis, EnvironmentError, Exception, False, FloatingPointError, FutureWarning, IOError, ImportError, IndentationError, IndexError, KeyError, KeyboardInterrupt, LookupError, MemoryError, NameError, None, NotImplemented, NotImplementedError, OSError, OverflowError,  PendingDeprecationWarning, ReferenceError, RuntimeError, RuntimeWarning, StandardError, StopIteration, SyntaxError, SyntaxWarning, SystemError, SystemExit, TabError, True, TypeError, UnboundLocalError, UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError, UserWarning, ValueError, Warning, WindowsError, ZeroDivisionError, _, __debug__, __doc__, __import__, __name__, abs, apply, basestring, bool, buffer, callable, chr, classmethod, cmp, coerce, compile, complex, copyright, credits, delattr, dict, dir, divmod, enumerate, eval, execfile, exit, file, filter, float, frozenset, getattr, globals, hasattr, hash, help, hex, id, input, int, intern, isinstance, issubclass, iter, len, license, list, locals, long, map, max, min, object, oct, open, ord, pow, property, quit, range, raw_input, reduce, reload, repr, reversed, round, set, setattr, slice, sorted, staticmethod, str, sum, super, tuple, type, unichr, unicode, vars, xrange, zip

#### 類型
數字、字符串、列表（一串字符串或數字或二者都有）、元組（衹讀的列表）、字典。

#### 賦値
{% highlight python %}var=123 # 數字
var="string" # 字符串
var=[1,2,'ok'] # 列表
var={'name':'Tom','age':15,'race':'Caucasian'} # 字典
var1=var2=var3=123 # 賦予相同的値
var1,var2,var3=123,456,"string" # 簡寫模式
var=print("123") # 用一個變量來代表一串命令
var=input("Prompt") # 請用戶輸入變量，屬性是字符串{% endhighlight %}

#### 置換
{% highlight python %}
a,b =b,a
{% endhighlight %}
這就把 a 和 b 兩個變量的値對調了。

#### 轉換
{% highlight python %}
int(var) # 轉成整數
float(var) # 轉成浮點數
str(var) # 轉成字符串
str(var).zfill(3) # 控制位數，比如 1 轉成 '001'
{% endhighlight %}
還有很多，記住這些基本夠用。

#### 切片
{% highlight python %}
str[n] # str 的第 n+1 個字符
str[m:n] # str 的第 m+1 到第 n 個字符
str[m:] # str 的第 m+1 及以後的字符
str[:n] # str 的第 1 到第 n 個字符
list[m:n] # 參照字符串，或者說字符串的本質就是 list
a[0:2] = [1, 12] # 可以直接對切片賦値
{% endhighlight %}

#### 字符串類變量的一些簡單處理
可以先定義字符串，然後用形如 `str1.find("some")` 的命令，也可以直接對字符串作用
{% highlight python %}
"some texts".find("some") # 查找，會返回位置，本例是 0 ，找不到是 -1
"some texts".replase("some","no") # 替換
{% endhighlight %}
還有其他處理如 join, split, lower, translate, strip 等，這裏不討論。

#### 運算
{% highlight python %}var=1+var1 # 與數字
var="string"+var # 與字符串
var=var1+var2 # 變量之間{% endhighlight %}
算術運算符：除了最簡單的 `+` `-` `*` `/` `%` ，還有 `**` 乘方， `//` 整除。
比較運算符：`==` 等於， `!=` 或 `<>` 不等於， `>` `<` `>=` `<=` 。
賦値運算符：算術運算符後面加個等號，比如 `a+=b` 相當於 `a=a+b` 。

## 語句

### if
{% highlight python linenos %}
# 條件裏用得最多的就是比較運算符
if 條件 : # 不同條件可以用 and 和 or 來連接
	幹活
elif 條件 : # 這句可以不用，也可以用很多個
	幹活
else: # 其實也經常不寫
	幹活
{% endhighlight %}
需要注意的是縮進，縮進不對是不行的。而且有時還能用到嵌套：
{% highlight python linenos %}
if 條件 :
	幹活
	if 條件 :
		幹活
	else:
		幹活
else:
	幹活
{% endhighlight %}
如果搞錯縮進就亂套了。

### while 循環
{% highlight python linenos %}
while 情況 :
	幹活
else: # 這個不必要
	幹活
{% endhighlight %}
while 循環也可以像 if 那樣嵌套起來。

### for 循環
{% highlight python linenos %}
for var in list/string:
	幹活
else: # 這個不必要
	幹活
{% endhighlight %}
僅用於有一個列表或者字符串，不過列表可以用命令造，比如最常見的 `range(a,b)` 的形式。

#### break
用於提前跳出循環，通常是一個循環裏面套了個 if ，滿足條件了就跳出來。
其實我個人更喜歡用 input() 來終止程序，因爲窗口會保留。

#### continue
還是循環裏套了個 if ，比如一個循環內部有幾百行，很煩，走到若干行後一個 if 滿足條件，這輪循環不走了，直接開始走下一輪。

#### pass
就是空語句，爲了保持完整性而使用。比如在 if 裏用 pass ，然後 else 的時候執行。

## 函數
{% highlight python linenos %}
def FunctionName(parameters):
	commands # 有很多行可以用 ; 來分割一下
	return # 可返回邏輯判斷、數字、字符串、變量
# return 還能運算，比如返回 a+b 。返回多個値： return (a,b,c)
# 不寫 return 後的內容或乾脆不寫 return 語句時，返回 None
# 使用函數：
FunctionName(independent parameters)
{% endhighlight %}
回想一下代數，什麼是函數。其實這寫法就相當說定義一個函數如 f(x,y,z)= 什麼什麼。等到要用這函數的時候，再塡一下具體的 x,y,z 就行。沒有 parameter 也可以，形式用 `func()` 。
如果想在函數外使用 return 回來的變量，最簡單的方法就是把變量全局化。比如：
{% highlight python linenos %}
def func():
	global a,b
	return (a,b)
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

## 讀寫文件
{% highlight python linenos %}
f = open('1.txt', 'w') # 打開文件
# 文件可帶路徑，也可不帶
# 模式裏，默認爲 r 衹讀 ， r+ 是讀寫， w 覆蓋， a 追加
# 對於二進制文件，如圖片， Windows 下應加 b ，寫法如 r+b
f.read() # 看內容
f.readline() # 逐行讀
f.readlines() # 返回的是列表
f.write(string) # 寫入
f.close() # 關上之後就不能 read write 之類了
{% endhighlight %}

## 其他常用命令
{% highlight python linenos %}
del i
# 刪掉變量
exec("print('yes')")
# 執行語句。看起來雞肋？用來批量生成變量就很好用。
assert i = 1
# 比如你很確定 i = 1 ，如果不是寧可程序 error ，那就用罷。

{% endhighlight %}

## 模塊
掌握以上知識點卽可運用模塊進行稍微複雜一點的編程。
{% highlight python linenos %}
import modname # 基本引入形式
print(dir(modname)) # 看看 modname 裏都有哪些命令
modname.func(parameters) # 基本使用形式
import modname2 as l # 縮寫引入
l.func2(parameters) # 縮寫後
from modname3 import * # 懶人引入
func3(parameters) # 寫起來簡單了，但可能造成污染
from modname4 import func4 # 小心的懶人
func4(parameters) # 等於衹引入了一個命令，污染的可能性較小
{% endhighlight %}

#### 安裝非標準庫
對於非標準庫，主要有四種形式。
一：開 cmd ， `pip install modname` 。
二：開 cmd ， `easy_install modname` 。
三：下載，解壓，開 cmd ，進文件夾， `python setup.py install` 。
四：下載，解壓，放進 Python 的 Lib 目錄。
五：下載一個安裝包，像裝軟件一樣裝起來。

## 異常處理*
異常並不一定發生，本部分作爲選讀。
{% highlight python linenos %}
try:
	down(link)
except BaseException:
	print("die")
	raise # 抛出，這句可不寫
else:
	print("good")
{% endhighlight %}
例中的 down 是個下載函數，函數說好回饋 200 時怎樣、 404 304 302 怎樣，但還是可能有各種問題，所以在 `except` 裏說，如果出現 `BaseException` 狀況，一律顯示 die 。 `BaseException` 指的是所有異常情況，具體見<a href="https://docs.python.org/3/library/exceptions.html#concrete-exceptions" rel="external">文檔</a>，或快速查看<a href="http://www.w3cschool.cc/python/python-exceptions.html" rel="external">中文簡表</a>。

## 面向對象編程 *
零基礎半小時內理解面向對象編程 (OOP) 思想幾乎是不可能的，這裏算選學部分。不過 OOP 在處理較大量非常類似的物件時有很大優勢，還是有必要介紹一下的。
對於外行人來說， OOP 的主要功能其實是創建模板。

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
	pass
{% endhighlight %}

## 出版物
<a href="http://www.amazon.com/Beginning-Python-From-Novice-Professional/dp/159059519X" rel="external">Beginning Python: from Novice to Professional</a> 本文沒有覆蓋的基礎內容。
<a href="http://www.amazon.com/Python-Essential-Reference-4th-Edition/dp/0672329786" rel="external">Python Essential Reference</a> 一個較全面且不囉嗦的敎材，進階用爲主。
<a href="http://shop.oreilly.com/product/0636920028154.do" rel="external">Learning Python</a> 囉嗦的來了。
<a href="http://www.amazon.com/Python-Standard-Library-Example-Developers/dp/0321767349" rel="external">The Python Standard Library by Example</a> 標準庫能讀完，也算民間高手了。
<a href="http://www.amazon.com/Python-Practice-Concurrency-Libraries-Developers/dp/0321905636" rel="external">Python in Practice: Create Better Programs Using Concurrency, Libraries, and Patterns</a> 進階書，用得到的話可以看。
<a href="http://www.diveintopython3.net/" rel="external">Dive into Python 3</a> 確實較深入。
<a href="http://learnpythonthehardway.org/book/" rel="external">Learn Python the Hard Way</a> 用來學未免蠢，用來複習提高倒不錯。

## 網絡資源
<a href="https://docs.python.org/3/" rel="external">官方文檔</a>，<a href="http://www.pythondoc.com/pythontutorial3/index.html" rel="external">中文版</a>
<a href="http://woodpecker.org.cn/abyteofpython_cn/chinese/" rel="external">简明 Python 教程</a> 可以作爲簡易快速的備查。
<a href="http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000" rel="external">Python 教程</a> 在中文 IT 敎程裏，也算佼佼者了。
<a href="http://docs.python-guide.org/en/latest/" rel="external">The Hitchhiker’s Guide to Python</a> 不少深入的話題，値得認眞讀。
<a href="https://github.com/qyuhen/book/" rel="external">Python 学习笔记</a> 講得比較深，但是用的是 Python 2 。
<a href="http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011" rel="external">Introduction to Computer Science and Programming</a> MIT 的編程課，有配套敎材，以前用 Lisp 的方言 Scheme ，現在 Python 2 。涉及一些編程思想，能體會到代數和電腦的關係。
<a href="http://www.jb51.net/list/list_97_1.htm" rel="external">腳本之家</a> 採集了很多腳本的網站。