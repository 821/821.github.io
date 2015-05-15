---
layout: indexed
title: 漫遊 Python 庫
date: '2015/04/20'
---
## 多線程
### threading
Python 主要有兩個多線程標準庫， thread 和 threading 。前者低級，後者高級。對於不需要太底層的情況，一般使用後者。
threading 有幾個常用方法： `start`, `run`, `join`, `name` 。
最常見的寫法是以線程爲父類，建立特殊對象。但這麼寫邏輯顯得較混亂。
```python
import threading, time
class Worker(threading.Thread):
	def __init__(self, argument):
		threading.Thread.__init__(self)
		self.argument = argument
	def run(self):
		print(self.argument)
		time.sleep(1)
		print(self.argument)
for i in range(20):
	Worker(i).start()
```
單單是這個模塊，已沒有太多必須用例子來詮釋，看
<a href="https://docs.python.org/3/library/threading.html" rel="external">文檔</a>就行了。

## 正則表達式

```python
import re
text = 'ABabcd1234'
# 匹配，衹從字符串的開頭找起，沒有就返回 None
# 格式： re.match(pattern, string, flags=0)
# flags 爲特殊選項，選項間用 | 隔開
mtext = re.match(r'([a-z])([a-z])', text, re.I)
if mtext:
	# 讀取 mtext 兩個方法： group(n) 和 groups()
	# group 的 n 不寫時表示第一個整體被匹配的字串
	print(mtext.group()) # AB
	# 而 n 表示正則表達式裏的圓括號分組
	print(mtext.group(1)) # A
	# groups 則是用元祖來返回所有的 group
	print(mtext.groups()) # ('A', 'B')
# 搜索，會一直找整個字符串，直到找到第一個
# 格式： re.search(pattern, string, flags=0)
stext = re.search(r'([a-z])(\d)', text, re.I)
if stext:
	print(stext.group()) # d1
# 替換
# 格式： re.sub(pattern, replacement, string, max=0)
newtext = re.sub(r'\d', "a", text)
print(newtext) # ABabcdaaaa
```
常用選項：
`re.I` 大小寫不敏感
`re.M` 多行
`re.S` `.` 也能包含 `\n` 之類很特殊的符號
`re.U` 使用 Unicode

## GUI
### tkinter
這個標準庫的命令非常規範，一個例子就夠了：
```python
from tkinter import *
wd = Tk() # 做出一個窗口
wd.title("My Title") # 標題
def doit(): # 瞎編一個複雜的函數給按鈕
	pass
button = Button(wd, text='Do it', command=dl) # 按鈕及其命令
# Tkinter 裏做命令都是這個格式，很簡單罷？
button.pack() # 簡單封裝
wd.mainloop() # 把窗口放入主循環
```
但是也不要小看他， IDLE 就是用他來寫的。
Tkinter 的部件有 Button, Canvas, Checkbutton, Entry, Frame, Label, Listbox, Menubutton, Menu, Message, Radiobutton, Scale, Scrollbar, Text, Toplevel, Spinbox, PanedWindow, LabelFrame, tkMessageBox 這些，詳細的可以查閱 <a href="http://www.tutorialspoint.com/python/python_gui_programming.htm" rel="external">Tkinter Programming</a>

### PyQt
環境： Python 3.4.3, PyQt 4.11.3 。代碼不保證兼容 Python 2 和 PyQt 5 。
安裝需要到官網下載安裝包。
PyQt 也有 Designer ，一個看起來很 Visual Basic 的東西。反正我沒想過要用。

#### 基礎
```python
import sys
from PyQt4.QtGui import *
# PyQt5 把 widgets 分裂出來，所以要加 from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
# 每個 Qt GUI 都需要一個 QApplication ，用以管理各種事項
widget = QWidget() # 括號裏可以塡寫其父類
# 這裏可以放入關於本 QWidget 的東西，比如大小、文字等
widget.show() # 創建時默認 hidden 狀態，要專門顯現
app.exec_() # 進入事件迴路，無事件則等待
# 所謂事件，就是鼠標點擊、鍵盤按鍵等
```
在例子中，使用了 QWidget 來形成窗口。 QWidget 有很多子類，也可以用他們來形成。
比如 QMainWindow ，功能就豐富些，有菜單欄、工具欄、狀態欄等內置部件，適合製作程序的主窗口。另一個常用的叫 QDialog ，比較適合建立對話框。
QWidget 還有很多子類，在文檔都有介紹。

#### 窗口
接上一代碼，在 `widget.show()` 前加入各種奇怪的東西：
```python
widget.resize(500, 500) # 窗口大小
widget.move(0, 0) # 窗口位置，原點是左上角
widget.setWindowTitle('Example') # 窗口標題
widget.setWindowIcon(QIcon('icons/py.ico')) # 圖標
widget.setToolTip('<b>QMainWindow</b>彈') # 彈窗
```
QWidget 的方法很多，還有 `hide`, `close`, `activateWindow`, `setToolTip` 等，都是比較重要的。

#### 按鈕
把 widget 部分去掉（剩下的，後面都叫骨頭了），替換成：
```python
button = QPushButton('Example') # 按鈕文字
button.resize(50, 50)
button.move(0, 0)
button.setWindowTitle('123')
button.clicked.connect(button.close)
# clicked 是信號，把 connect 到括號裏的命令，這裏是 close
# 類似的信號還有 valueChanged 什麼的，命令當然更多
# 信號是 GUI 裏很重要的槪念，需要認眞理解
button.show()
```

#### 文本框
骨頭加上這些：
```python
le = QLineEdit()
le.show()
```

#### 簡單結合與排版
骨頭加上這些：
```python
le = QLineEdit()
b0 = QPushButton('0')

hl1 = QHBoxLayout() # 橫向佈局容器
hl1.addWidget(le) # 加入佈局容器，成爲其 child
hl1.addWidget(b0)

b1 = QPushButton('1')
b2 = QPushButton('2')

hl2 = QHBoxLayout()
hl2.addWidget(b1)
hl2.addWidget(b2)

vl = QVBoxLayout() # 縱向佈局容器
vl.addLayout(hl1) # vl 成了祖父
vl.addLayout(hl2)

mw = QMainWindow()
mw.setLayout(vl) # mw 成了曾祖父
mw.setGeometry(0, 100, 400, 300)
# 窗口位置、大小的另一方式，順序要記淸
mw.show()
```
排版不限於 `QHBoxLayout` 和 `QVBoxLayout` ，但這兩個無疑是最簡單、直觀的。



```python
```