---
layout: indexed
title: C++
date: '2015/04/11'
---
學過 Python ， Python 是高級語言，高度抽象化，自帶垃圾淸理，免編譯，跨平臺。 Python 的這些特點讓人能夠比較專心編寫程序中對象的各種境遇，比如寫一個下載腳本，需要考慮的就衹是下載的事，要不要模擬瀏覽器，下載哪些鏈接，放進哪個文件夾之類，一切行爲都像自己平時下載東西，衹不過工具換了。
C++ 是中級語言（以前 C 是高級，現在都算低級了， C++ 怎麼看都是中或低級），可以做對效率要求更高的事，但同時也比較難。所謂「難」包含很多方面，一是做同樣的事，需要掌握更多知識點；二是抽象化不足，沒有一些方便的寫法；三是和硬件更貼近，需要考慮的問題有時會多些。還是說下載，用 C++ 要自己下載並編譯相關的庫，想着命名空間，考慮參數怎麼傳遞，考慮內存有沒有釋放。弄得自己像電腦的僕人一樣。所以學 C++ 就莫名其妙的要學很多感覺跟自己做的事不那麼相關的事，當然難了。學 Python 要有「三個月滅亡中國」的口氣，而學 C++ 則是「持久戰」了。
旣然 C++ 難學難用，爲什麼還要學？就是因爲和 Python 非常不同，學 C++ 纔更好加深對 Python 的理解。其次， C++ 的應用範圍更廣，如果堅持學下去，能做的事比 Python 多。

## 書籍
C++ 的書籍可謂汗牛充棟，衹能擇其精要稍加介紹。
C++ 之父 Stroustrup 出了 "A Tour of C++", "The C++ Programming Language", "Programming: Principles and Practice Using C++" 這三本。第一本很薄，宜粗學。後兩本看名字就知道側重點不同。最後一本時間較早，是 98 標準，代碼過時但思想不過時。
"C++ Primer" 有聖經之稱，簡直是字典。所以作者又寫了一本 "Essential C++" 。
"C++ Primer Plus" 這本更像敎材，不過有點囉嗦。
"Sams Teach Yourself C++ in One Hour a Day" 一部簡明的入門書，不錯的選擇。
"Effective C++" 提高書，好評後作者又寫了 "More Effective C++" 。

## 基礎

### 基本形態
C++ 第一次讓我覺得他很「中級」，就是因爲基本形態都不一樣，程序寫起來很囉嗦。比如 Hello World ，在 Python 就一行、兩個知識點，而 C++ 有八行、十幾個知識點。

```cpp
// 註釋用雙斜槓
#include <iostream> // 使用 iostream 這個頭文件
using namespace std; // 使用 std 這個 namespace
int main() // 每個 C++ 程序必須有一主函數，程序從 int 開始執行
{
// 如未指定 namespace ，cout 前應加 std:
	cout << "Hello, World!"
	<< endl;
/* cout 就是輸出，與之相反的就是 cin
<< 在 iostream 裏爲「放入」，可以在一個語句內用多次
其實 >> 也是放入，方向不同
C++ 對於字符串也是可用單引號也可用雙引號的
C++ 語句結束使用分號，而不是斷行，可以一行內很多分號
endl 就是斷行，當然寫 "\n" 也行
C++ 對縮進沒有要求，縮進是爲了好看
這是跨行註釋 */
	return 0; // 這一行可以不寫。
}
```

### 變量
C++ 的變量有 bool(眞假), char(一字節，如字母 a), int(整數，四字節), float(單精度浮點値), double(雙精度浮點値，八字節), void(空値), wchar_t(寬字符) 。
沒有字符串？眞沒有，不過標準庫有。

```cpp
extern int i, j; // extern 是聲明變量， int 指出類型
i = 3, j = 5; // 初始化 i 和 j
int a = 1 // 聲明並初始化
```

### 數組

```cpp
char v[6] = [1,2,3,4,5,6]; // 六個 char 的數組 v
```

### 指針
這是很多語言沒有的槪念。在 C++ 的世界裏，每個變量都有內存位置，可以使用指針來管理內存。
指針也是變量，也有變量的那幾種形式。

```cpp
char *p; // 類似聲明變量， * 表明了指針的身份
char∗ p = &v[3]; // 這個指針指向數組 v 的第四個元素
```

### 運算
算術： `+` `-` `*` `/` `%` `++` `--`
判斷： `==` `!=` `<` `>` `<=` `>=`
邏輯： `&&` `||` `!`
位： `&` `|` `^` `~` `<<` `>>`
賦値： `=` `+=` `-=` `*=` `/=` `%=` `<<=` `>>=` `&=` `^=` `|=`
其中位的運算是直接作用到二進制的，很不抽象。

### 函數
int 返回類型。其他情況可以類推，比較特殊的是 Elem ，返回指針。
函數的變量也要聲明，很麻煩。
C++ 可以創建多個同名函數，叫重載、多態。

### if else

```cpp
if (condition)
{
	statement;
}
// 沒有 else 當然也行
else
{
	statement;
}
```

### switch
C++ 沒有 elif ，而是用 `switch` 。

```cpp
switch (expression)
{
	case valueOne: statement;
		break;
	case valueTwo: statement;
		break;
	...
	case valueN: statement;
		break;
	default: statement;
}
```
有點像 if... elif... else 。比如 expression 寫 `i` ， case 那邊寫個 `case 1:` ，這就和 `if (i = 1)` 是等效的。

### goto
goto 被認爲容易導致混亂、應該避免，所以很多語言比如 Python 都沒有。存在卽合理，不存在也不一定不合理。我就很喜歡 goto ，寫 goto 就混亂那是因爲自己本來就混亂。

```cpp
lable: // 這就設置了 goto 的標籤
goto lable // 跳到標籤的位置
```
不過寫循環當然沒必要用 goto 這麼囉嗦的方法。

### while

```cpp
while (condition) // 如有多條件，可用運算符 && 或 || 連接
{
	statement;
}
```
condition 也有可能衹是一個 true 。程序會一直跑下去，所以要小心使用。

#### continue 和 break
continue 就是跳到循環的開頭。
break 是跳出循環。
一般跟 if 語句結合使用。

#### do while

```cpp
do
{
	statement;
}
while (condition);
```
跟直接 while 不同， do while 中的 statement 至少會執行一次。

### for

```cpp
for (initialization; condition; action)
{
	statement;
}
```
initialization 可以是任何合法 C++ 語句，不過一般用來創建一個計數的變量，比如 `i = 1` 。
action 也可以是任何合法 C++ 語句，不過一般用來遞增或遞減計數變量，比如 `i++` 。
for 的 initialization, condition, action 三條都可以不寫，這叫空語句。但與其說可以不寫，不如說是在別處寫了。
for 那句如果寫成 `for (; ; )` ，那就永遠停不下來了。
寫 Python 從不用 while ，但看見這麼囉嗦的 for ，頓時覺得 while 也不錯……

## 面向對象
其實我比較習慣函數編程，不過面向對象編程是 C++ 的重點。

### 類
創建一個汪星人對象，交配是隱私，年齡是半隱私（保護），顏色和叫聲可公開：

```cpp
class Dog
{
	private:
		void Mate();
	protected:
		int Age;
	public:
		std::string Color;
		void Bark() const { cout << "Rough rough...\n";}
}
```

### 對象
接上，比如一隻叫 Obama 的狗。

```cpp
Dog Obama;
Obama.Age = 1;
Obama.Color = "Black";
// 想聽聽叫聲嗎？
Obama.Bark();
// 當然，看不見交配。
```

### 繼承
比如哈士奇，繼承「狗」的屬性。

```cpp
class Husky : public Dog
```