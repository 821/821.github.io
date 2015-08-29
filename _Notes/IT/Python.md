---
layout: indexed
title: Python 半小時上手
date: '2014/08/08'
---
本文代碼如無說明，均爲 Python 3 代碼。

學會編程，就能打開人機交互的新篇章，做很多以前做不到的事。當下流行的程序語言，都有其各自的優越性， Python 也不例外：
1. 易學。實現相同功能， Python 需要的知識點往往是最少之一。
2. 易讀。簡潔、單一最優解、強制縮進，很好的敎學語言。
3. 易配。多數 *nix 發行版內置， Windows 安裝包也很小。運行還不用手動編譯。
4. 易用。標準庫就很強，第三方庫也很豐富，各種移植也全面。
5. 易抄。開源社區活躍，代碼雷同特好抄，反編譯輕鬆（但不提倡）。
總而言之，「人生苦短，我用 Python 」。
Python 當然也有缺點：
1. 慢。速度遠低於 C/C++ ，甚至不如 C#/Java 。（很多人學點 Python 主要是爲了網頁抓取、文檔之類高 IO 低 CPU 的事，甁頸並不在語言。）
2. 版本。 Python 2 和 3 區別較大，很多人還不肯遷移到 3 。（其實現在初學根本不用看 2 。）
3. 高級。和 C 相比， Python 更高級，寫不了操作系統這麼底層的東西。（一般人根本不想做這種事。）
無視某一版本，花點錢升級電腦，然後不要抱着寫操作系統的野心， Python 就沒缺點了。

很多敎程容易陷入學術化的泥沼，忘記實用本質。這就像本來衹想敎一個小學生計算圓的面積，結果變成講圓面積公式的來歷，結果把整個平面幾何、解析幾何、微積分全部講完，小學生在學到三角函數時已吐血身亡。
所以本文的目標是掛一漏萬、避難趨易，讓讀者自己提綱挈領、綱舉目張。多數人應能半小時內讀完並對大部分內容有印象，而且這些內容「剛好」是最重要的——至少我自己用到過，所以覺得重要。系統的學習當然是好的，但如果能用前就喪失興趣就糟了。上手之後再進行系統學習，會覺得很輕鬆，而且更能專注於編程思想、美化代碼、易錯細節等方面。

## 方法論

#### 有問題找模塊
模塊之於編程語言，就像軟件之於操作系統。在操作系統裏，想下載就裝下載軟件，想 P 圖就裝 PS ，編程也是如此。
我的常用模塊（基本是標準庫）：
os, shutil 處理文件與文件夾
re 正則表達式
requests 網頁訪問與抓取
BeautifulSoup 網頁內容整理（或者叫抓取的後期處理）
threading 多線程
pyQt 高級的 GUI （初學可用 tkinter 過渡）
絕大多數敎程都會把這一節放到書末且往往不得要領（比如大篇幅討論如何寫模塊，卻不告訴讀者早就有很多無比好用的模塊），導致學習者讀到之前就失去耐心，卽使讀到也不知道是幹嘛用的，本文特地放到最前。

#### 讀文檔
這在使用開源軟件裏面簡直是憲法第一條。用模塊肯定要看文檔的，不用說。

#### 邊用邊學
把本文迅速瀏覽一遍就可以寫了，寫自己想寫的。比如抓網站，或者按需生成文件，想幹嘛就幹嘛，別太複雜就行。至於那些 tutorial 、習題，對非專業人員就是浪費腦細胞，有空再說。

#### 搜索提問
Google 和 StackOverflow 是學編程最好的朋友。

#### 寫註釋
對於新學到的知識點，可以寫詳細一些的註釋。一方面將來可以複習，另一方面寫註釋的過程也可以加深理解。

## 基本要求與命令

#### 文件名後綴
`.py`: 最常見的後綴
`.pyw`: 執行不帶 console ，在 cmd 下跑也看不見回饋和錯誤，不適合做測試用
`.pyc`: Python 運行需轉換成字節代碼 `.pyc` ，這是自動的，手動可在 Python console 執行：
```python
import py_compile
py_compile.compile('something.py')
```
`.pyo`: 優化的，在 cmd/shell 執行： `python -O -m py_compile something.py`
一般我們不編譯 Python 腳本，會用 `py` 和 `pyw` 就好。

#### 文件頭
在 \*nix 下運行 Python 腳本，第一行應加 `#!/usr/bin/env python3.4` 。
非 unicode 腳本，應加 `# -*- coding: gb18030 -*-` 之類的內容。

#### 註釋
同一行內 `#` 後的都算註釋。
多行註釋在開頭和結尾後用 `'''` 。

### 語句
一行內可以用 `;` 分割多個語句。
多行可以用 `\` 連接一個語句。

#### 幫助
格式是 help(command) ，記住就好，可以經常看看。

#### 輸出 print
```python
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# 這麼寫不好懂，換平常的例子，衹放點 value 相關的：
print('hello, world') # hello, world
print('hello' + 'world') # helloworld
print('hello', 'world') # hello world
```
Python 2 可用 `print value` 格式。

## 變量

#### 保留字
這些詞是 Python 的內置命令，不能用作變量名：
None, False, True, and, or, not, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, pass, raise, return, try, while, with, yield

#### 類型
NoneType: None
bool: True, False
int: 64 位的機子上就是 64 位以內的整數
float: 小數
complex: 複數
str: 字符串，默認 unicode ，實際是一種特殊的列表
byte: 字節——這是 Python 2 的 str 形式
list: 列表
tuple: 元組，可看作衹讀列表
dict: 字典
set: 集合，存儲無序不重複對象，實際上是一種類
frozenset: 衹讀集合
```python
var = 1 # int
var = 1.5 # float
var = "123" # 字符串
var = '\n' # 也是字符串，這是個換行符
var = '\u0020' # Unicode 字符串
var = "It's a string." # 雙引號裏用單引號或反過來都不用在前面加上 \
var = [1,2,'ok'] # 列表
var = (1,2,'ok') # 元組
var = {'name':'Tom','age':15,'race':'Caucasian'} # 字典
var = {1,2} # 集合
```
小補充：字典和列表都是常用類型，字典無序，列表有序。字典耗內存較大，列表則小。字典的複雜度是 O(1) 而列表是 O(n) 。這就是說，比如有兩個字典，他們大小不同，但搜索元素時花的時間是一樣的。而如果有兩個列表，前者的長度是後者的三倍，則搜索前者花的時間也是後者的三倍。所以，當我們處理比較大的數據時，應該使用字典而非列表。

#### 賦値
除了最簡單的形式，還有：
```python
var1 = var2 = var3 = 123 # 賦予相同的値
var1, var2, var3 = 123, 456, 'string' # 簡寫模式
# 不要亂用簡寫，會降低代碼可讀性的
var = input('Prompt') # 用一個變量來代表一串命令
(a, b, c) = var # 一種比較酷的方法
```

#### 置換
```python
a,b = b,a
```
這就把 a 和 b 兩個變量的値對調了。

#### 轉換
```python
int(var) # 轉成整數
float(var) # 轉成浮點數
str(var) # 轉成字符串
str(var).zfill(3) # 控制位數，比如 1 轉成 '001'
```
還有很多，記住這些基本夠用。

#### 切片
```python
# 這裏的 m 和 n 都是自然數
str[n] # str 的第 n+1 個字符
str[m:n] # str 的第 m+1 到第 n 個字符
str[m:] # str 的第 m+1 及以後的字符
str[:n] # str 的第 1 到第 n 個字符
str[-n:] # str 的最後 n 個字符
list[m:n] # 參照字符串，或者說字符串的本質就是 list
a[0:2] = [1, 12] # 可以直接對切片賦値
```

#### 字符串類變量的一些簡單處理
可以先定義字符串，然後用形如 `str1.find("some")` 的命令，也可以直接對字符串作用
```python
"some texts".find("some") # 查找，會返回位置，本例是 0 ，找不到是 -1
"some texts".replase("some","no") # 替換
```
還有其他處理如 join, split, lower, translate, strip 等，這裏不討論。

#### 運算
```python
var=1 + var1 # 與數字
var="string" + var # 與字符串
var=var1 + var2 # 變量之間
```
算術運算符：除了最簡單的 `+` `-` `*` `/` `%` ，還有 `**` 乘方， `//` 整除。
比較運算符：`==` 等於， `!=` 或 `<>` 不等於， `>` `<` `>=` `<=` 。
賦値運算符：算術運算符後面加個等號，比如 `a+=b` 相當於 `a=a+b` 。
運算符兩邊的空格隨意。

## 語句

### if
```python
# 條件裏用得最多的就是比較運算符
if 條件 : # 不同條件可以用 and 和 or 來連接
	幹活
elif 條件 : # 這句可以不用，也可以用很多個
	幹活
else: # 其實也經常不寫
	幹活
```
需要注意的是縮進，縮進不對是不行的。而且有時還能用到嵌套：
```python
if 條件 :
	幹活
	if 條件 :
		幹活
	else:
		幹活
else:
	幹活
```
如果搞錯縮進就亂套了。

### while 循環
```python
while 情況 :
	幹活
else: # 這個不必要
	幹活
```
while 循環也可以像 if 那樣嵌套起來。
其實寫循環一般不建議用 `else` 。

### for 循環
while 不太好用，因爲計數通常需要在循環內寫類似 `i = i + 1` 的東西。計數出現在不同位置還會影響程序運行，對思路不淸的新人來說有點危險，但更重要的還是太囉嗦。
還是咱們 for 好：
```python
for var in list/string:
	幹活
else: # 這個不必要
	幹活
```
僅用於有一個列表或者字符串，不過列表可以用命令造，比如最常見的 `range(a,b)` 的形式，當 a 爲 1 時，可以衹寫 b 。

#### break
用於提前跳出循環，通常是一個循環裏面套了個 if ，滿足條件了就跳出來。
其實我個人更喜歡用 input() 來終止程序，因爲窗口會保留。

#### continue
還是循環裏套了個 if ，比如一個循環內部有幾百行，很煩，走到若干行後一個 if 滿足條件，這輪循環不走了，直接開始走下一輪。

#### pass
就是空語句，爲了保持完整性而使用。比如在 if 裏用 pass ，然後 else 的時候執行。

## 函數
```python
def FunctionName(parameters):
# 沒有 parameter 也可以，形式用 func()
# 可以有多個 parameters ，用逗號區隔
# 某個 parameter 後面跟上 = True 時，表示他是可選的
	commands # 有很多行可以用 ; 來分割一下
	return # 可返回邏輯判斷、數字、字符串、變量
# return 還能運算，比如 return a+b 
# return 可以返回多個値： return (a,b,c)
# 不寫 return 後的內容或乾脆不寫 return 語句時，返回 None
# 使用函數：
FunctionName(independent parameters)
```
回想一下代數，什麼是函數。其實這寫法就相當說定義一個函數如 f(x,y,z)= 什麼什麼。等到要用這函數的時候，再塡一下具體的 x,y,z 就行。
如果想在函數外使用 return 回來的變量，最簡單的方法就是把變量全局化。比如：
```python
def func():
	global a,b
	return (a,b)
```
執行完後，整個腳本都會獲得變量 a 和 b 。不然 a 和 b 在運行完腳本之後就不見了。
或者用另一種方法來傳遞：
```python
def func():
	return (a, b)
c, d = func()
```
a 和 b 消失了，但他們的値被 c 和 d 繼承。

### 高階函數
來個複雜一點的例子：
```python
def func(a,b):
	return a(b)
```
func 中的變量 a 同時也是一個函數，所以 func 就是個高階函數。實際上，有個叫 `map()` 的內置函數就跟這個 func 很類似。

### 匿名函數
看起來有點雞肋，不過有時卻是必須的。比如有些地方不能寫帶參數的函數，比如 `print(x)` ，這時寫 `lambda: print(x)` 就可以。
```python
lambda [arg1 [,arg2,.....argn]]:expression
# 下面是兩個等價的東西
add = lambda x, y: x + y
def add(x,y):
	return x + y
```

## 讀寫文件
```python
f = open('1.txt', 'w', encoding='utf-8') # 打開文件
# 文件可帶路徑，也可不帶
# 模式裏，默認爲 r 衹讀 ， r+ 是讀寫， w 覆蓋， a 追加
# 對於二進制文件，如圖片， Windows 下應加 b ，寫法如 r+b
# encoding 是不必寫的
f.read() # 看內容
f.readline() # 逐行讀
f.readlines() # 返回的是列表，除了末行，都帶 '\n'
f.read().splitlines() # 返回逐行讀出的列表，不帶 '\n'
f.write(string) # 寫入
f.close() # 關上之後就不能 read write 之類了
```

## 其他常用命令
```python
del i
# 刪掉變量
assert i = 1
# 確定 i = 1 ，如果不是則程序出錯
exec("print('yes')")
# 執行語句。看起來雞肋？批量生成變量就很好用
type(var)
# 看看 var 是個什麼類型
```
這裏爲 `assert` 閒扯一句。實際上這貨是爲調試而生的。測試 (test) 是通過給出 input 看看程序是否按照自己的意願回饋 output ，而調試 (debug) 按字面意思就是找到並排除 bug 。一般的，我們可以通過 `print` 顯示變量這方法來調試，用完之後需要註釋掉。用 `assert` 的話，不註釋掉也不影響，可以提高調試效率。
內置函數的總表見<a href="https://docs.python.org/3.4/library/functions.html" rel="external">文檔</a>。

## 模塊
掌握以上知識點卽可運用模塊進行稍微複雜一點的編程。
```python
import modname # 基本引入形式
print(dir(modname)) # 看看 modname 裏都有哪些命令
modname.func(parameters) # 基本使用形式
import modname2 as l # 縮寫引入
l.func2(parameters) # 縮寫後
from modname3 import * # 懶人引入
func3(parameters) # 寫起來簡單了，但可能造成污染
from modname4 import func4 # 小心的懶人
func4(parameters) # 等於衹引入了一個命令，污染的可能性較小
```

#### 安裝非標準庫
對於非標準庫，主要有四種形式。
一：開 cmd ， `pip install modname` 。
二：開 cmd ， `easy_install modname` 。
三：下載，解壓，開 cmd ，進文件夾， `python setup.py install` 。
四：下載，解壓，放進 Python 的 Lib 目錄。
五：下載一個安裝包，像裝軟件一樣裝起來。

#### 關於 pip
pip 的升級：在命令行執行 `python -m pip install -U pip` ，如果是 *nix 系統則執行 `pip install -U pip`
pip 的單獨安裝：下載 <a href="https://bootstrap.pypa.io/get-pip.py" rel="external">get pip</a> ，然後 `python get-pip.py`

## 異常處理 \*
異常並不一定發生，本部分作爲選讀。
```python
try:
	down(link)
except BaseException:
	print("die")
	raise MyException('message') # 抛出，這句可不寫
else:
	print("good")
```
例中的 down 是個下載函數，函數說好回饋 200 時怎樣、 404 304 302 怎樣，但還是可能有各種問題，所以在 `except` 裏說，如果出現 `BaseException` 狀況，一律顯示 die 。 `BaseException` 指的是所有異常情況，具體見<a href="https://docs.python.org/3/library/exceptions.html#concrete-exceptions" rel="external">文檔</a>，或快速查看<a href="http://www.w3cschool.cc/python/python-exceptions.html" rel="external">中文簡表</a>。

## 面向對象編程 \*
Python 的 OOP 給我的印象很不好，滿天飛的 `self` 和下劃線，代碼的美感都毀了。而且，零基礎要半小時理解面向對象編程 (OOP) 思想過於困難，這裏算選學部分。
對外行人來說， OOP 的主要意義其實是創建模板。

#### 槪念
類：比如四個東西， Washington, Jefferson, Roosevelt, Lincoln ，屬於什麼類？ Human 。
對象：比如 Washington ，他就是 Human 的一個對象。
繼承： Human 裏有很多類別，比如 Caucasian 。 Caucasian 具有 Human 的全部特性，這叫繼承。其中， Human 是父類， Caucasian 是子類。
類可以有很多項屬性和動作，建立好類，每個對象像套用函數一樣用類來決定行爲就行了，類就像個模板一樣。所以 OOP 對於需要到很多個對象的編程是比較方便的。

#### 例子
```python
class Human (Object): # class 是聲明建立類， Human 是類名 ， Object 是常用的最高父類
	def __init__(self, name, born): # __init__ 是個方法，第一個變量永遠是 self
		self.name = name # 寫了這句，外部就能調用這個變量了
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
```
說實話， Python 基礎裏看起來最不優美的就是 OOP 。什麼 `__init__` ，還有一堆 `self.` ，簡直不要太醜。如果 `def` 能嵌套，我幾乎沒機會用 `class` ……

## 補充閱覽
#### 書籍
<a href="http://www.amazon.com/Beginning-Python-From-Novice-Professional/dp/159059519X" rel="external">Beginning Python: from Novice to Professional</a> 本文沒有覆蓋的基礎內容。
<a href="http://www.amazon.com/Python-Essential-Reference-4th-Edition/dp/0672329786" rel="external">Python Essential Reference</a> 一個較全面且不囉嗦的敎材，進階用爲主。
<a href="http://shop.oreilly.com/product/0636920028154.do" rel="external">Learning Python</a> 囉嗦的來了。
Think Python 簡短，知識點梳理比較到位。
<a href="http://www.diveintopython3.net/" rel="external">Dive into Python 3</a> 確實較深入，但編排有問題，不能作爲入門書。
<a href="http://www.amazon.com/Python-Standard-Library-Example-Developers/dp/0321767349" rel="external">The Python Standard Library by Example</a> 標準庫能讀完，也算民間高手了。
<a href="http://www.amazon.com/Python-Practice-Concurrency-Libraries-Developers/dp/0321905636" rel="external">Python in Practice: Create Better Programs Using Concurrency, Libraries, and Patterns</a> 進階書，用得到的話可以看。
<a href="https://www.packtpub.com/application-development/expert-python-programming" rel="external">Expert Python Programming</a> 進階書，涉及很多細節，讓你的代碼更 Pythonic 。

#### 網絡資源
<a href="https://docs.python.org/3/" rel="external">官方文檔</a> 不用解釋其重要性了。
<a href="http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000" rel="external">Python 教程</a> 在中文 IT 敎程裏，也算佼佼者了。原本是 2 的，升級了。
<a href="http://docs.python-guide.org/en/latest/" rel="external">The Hitchhiker’s Guide to Python</a> 不少深入的話題，値得認眞讀。
<a href="https://github.com/qyuhen/book/" rel="external">Python 学习笔记</a> 講得比較深，但用的是 Python 2 。
<a href="http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011" rel="external">Introduction to Computer Science and Programming</a> MIT 的編程課，有配套敎材，以前用 Lisp 的方言 Scheme ，現在 Python 2 ，涉及一些編程思想。
<a href="http://www-inst.eecs.berkeley.edu/~cs61a/fa11/" rel="external">Structure and Interpretation of Computer Programs</a> UCB 的編程課，跟 MIT 那門用相同敎材，但 Python 版本是 3 。相比 MIT 那門，好處是文檔多，壞處是沒視頻。
<a href="http://www.jb51.net/list/list_97_1.htm" rel="external">腳本之家</a> 採集了很多腳本的網站。
<a href="http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html" rel="external">Code Like a Pythonista</a> 個人來講不需要強求，但是看看也好。
<a href="https://leetcode.com/" rel="external">LeetCode</a> 自虐向代碼題庫，支持多門語言。

建議：爲了快速上手，本文把很多「高級玩法」（比如遞歸、動態）都被隱藏了。半小時後，搜一下庫，寫幾個自己的剛需腳本。然後過一遍官方文檔，看完 MIT 那門課，就可以着手寫複雜的東西了。這時再看前面幾本出版物，除了標準庫發現不了幾個新知識點，會覺得都很簡單。當然，做 LeetCode 還是會經常 Time limit exceeded 。