---
layout: indexed
title: Scheme 簡述
date: '2015/05/02'
---
函數編程是命令編程的鏡子，命令編程的缺點就是函數編程的優點，反之亦然。雖然由於歷史因素，函數編程並非主流，但學習一下或許能有一些啓發。
最常見的函數編程語言就是 Lisp, Scheme, Racket, Haskell 。 Scheme 是 MIT 出的 Lisp 方言， Racket 是 Lisp 較實用的方言，而 Haskell 是一門漸漸火起來的新興語言。 Scheme 是很多北美高校第一門語言（現在地位漸漸被 Python 替代），用 Scheme 來闡釋程序設計一般原理的「名著」就有 ["SICP"](http://mitpress.mit.edu/sicp/) 和 ["How to Design Programs"](http://www.ccs.neu.edu/home/matthias/HtDP2e/) 。另外 "The Little Schemer" 和 ["TSPL"](http://www.scheme.com/tspl3/) 則是比較專門的 Scheme 敎材。
本文的願景是，讀完後可直接讀 SICP ，而不必糾結於 Scheme 的語法，看 Emacs 配置文件時也不要那麼驚訝。

## 環境
最常用的是 MIT Scheme ，安裝得到 Edwin ，一個類似 Emacs 的編輯器。
在 Edwin 使用 `C-x z` 進入 Scheme 命令交互狀態。可以用 `(edit)` 再次回到 Edwin 。
Scheme 的標準文件名後綴是 scm 。
{% highlight scheme %}
; Scheme 用分號註釋
; 訪問文件夾
(cd "F:\\") ; 是不是有點像 Shell ？
; 打開文件
(load "F:\\my.scm")
{% endhighlight %}
如果要編譯，可以用 [Racket](http://download.racket-lang.org/) 。

## 函數
爲了學習函數的格式，我們先通過計算來看看 Scheme 的函數格式：
{% highlight scheme %}
(+ 1 2 3) ; 1+2+3
(quotient 3 2) ; 整除
(modulo 3 2) ; 取模
(sqrt 4) ; 開方
(expt a b) ; a 的 b 次方
(exp 1) ; 2.718281828459045
(sin 1) ; 這是三角函數
; 嵌套一下，你就眼花
(- 2 (/ 4 2)) ; 2-(4/2)
{% endhighlight %}
眞是一股邪祟之氣外露……

### 命名與調用
旣然是函數編程，命名變量和命名函數是一樣的格式。
{% highlight scheme %}
; 命名變量，相當於 Python 的 var = 1
(define var 1)
; 命名函數
(define (add i j) (+ i j))
; 調用函數
(add 1 2) ; (+ 1 2)
{% endhighlight %}

### 局部
聲明一個局部變量，我們通常用 `let` 。
{% highlight scheme %}
(let ((i 1) (j 2))
(let* ((i 1) (j (+ i 1)))
; 後者是聲明的同時還調用了第一個聲明了
{% endhighlight %}

## 分支

### if
{% highlight scheme %}
(define (abs x)
	(if (or (> x 0) (= x 0))
		x)
	(if (< x 0)
		(- x)))
{% endhighlight %}

### cond
比較像 switch 。
{% highlight scheme %}
(define (abs x)
	(cond ((> x 0) x)
		((= x 0) 0)
		(else (- x))))
{% endhighlight %}

### 檢驗
{% highlight scheme %}
(equal? "hello" "hello") ; 比較
(list? (list 1 2 3)) ; 檢驗是否列表，空表不算列表
(null? list) ; 檢驗是否空表
(string? str) ; 檢驗是否字符串
; 還有很多這類函數
{% endhighlight %}