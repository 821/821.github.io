---
layout: indexed
title: 慢慢學 C#
date: '2015/04/28'
---
C# 設計類似 C/C++ ，但實現通過虛擬機，所以又像 Java 。然而我被平時不小心用到使用 JRE 的軟件更新失敗噁心過多次，有別的選擇，就不想看見 Java ，所以覺得學 C# 比較好。
C# 缺點當然不少。他不像 Python 那麼優美、易學，也不像 C 那樣底層、高效。他就是個中不溜，有點尷尬的感覺，但他畢竟還是個比較高效而嚴謹的語言，用戶體驗較好。因爲不易學，所以慢慢學，學到一點寫一點，本文將是一個持久戰。
這次的環境是 Windows 7 + Mono 。我不想用 IDE ，能編譯就好，用 Mono 還能跨平臺。

## 基礎

### 編譯
VS 下編譯 C# 的命令是 `csc file.cs` 。 Mono 是 `mcs file.cs` 。

### 基本形態
C# 旣然有個 C ，很多基本語法和 C++ 還是比較接近的。
```csharp
using System; // 使用命名空間
class HelloWorld // 類
{
	static void Main () // Main 是方法
	{
		Console.WriteLine ("Hello World\n"); // Main 的行爲
		Console.ReadKey(); // 相當於 cmd 的 pause
	}
}
```
一個 C# 程序的基本結構就這樣，除了 `ReadKey` 那句不能再少了。
可以看到，語句基本上以 `;` 結束。程序從 `Main` 開始執行。

### 類型
C# 類型還分三大類：

#### 值
bool: True, False
byte: 8 位無符號整數，也就是 0-255
short: 16 位無符號整數
uint: 32 位無符號整數
ulong: 64 位無符號整數
sbyte: 8 位有符號整數
short: 16 位有符號整數
int: 32 位有符號整數
long: 64 位有符號整數
float: 32 位單精度浮點
double: 64 位雙精度浮點
decimal: 128 位十進制値
char: 16 位 unicode 字符
賦値和轉換舉例：
```csharp
double d = 1.23;
int i, j;
i = (int)d;
Console.WriteLine(i.ToString());
```
最後上屛的應該是 1 。

#### 引用
對象 object: System.Object 的別名，最高父類
動態 dynamic: 類似 object
字符串 string: System.String 的別名
```csharp
//兩個等價例子
string str = @"C:\Windows";
string str = "C:\\Windows";
```

#### 指針
寫作 `int*` 之類。

### 運算、條件、循環
跟 C++ 一樣。

### 封裝
封裝決定類成員的範圍。封裝使用五種 access specifiers ：
public 到處用
private 類內部函數可訪問
protected 類內部及子類可訪問
internal 當前程序可訪問
protected internal 當前程序中，類內部子類可訪問

### 方法
方法的功能很像 Python 的函數，但更強大。格式：
```csharp
<Access Specifier> <Return Type> <Method Name>(Parameters)
{
   Method Body
}
```
Access Specifier 在「封裝」部分有介紹。
Return Type 在「値』部分有介紹。
Parameters 部分別忘了定義類型。方法外已定義參數稱爲實際參數，而方法去改變了的那些參數也會被內存保留，稱爲形式參數。Parameters 的類型前如果不加關鍵字，雖然也產生形式參數，但方法外再次調用該參數時還是會調用到實際參數，也就是表現爲那個參數沒有變化。如果在每個 parameters 類型前面加上關鍵字 `ref` ，則形式參數覆蓋實際參數。由於 `return` 語句衹能返回一個値，在 parameters 前加上 `out` 可以返回多個値。
C# 裏的方法可以引用自己，這叫作遞歸。比如做個階乘：
```csharp
using System;
namespace CalculatorApplication
{
	class NumberManipulator
	{
		private int factorial(int num)
		{
			int result;
			if (num == 1)
			{
				return 1;
			}
			else
			{
				result = factorial(num - 1) * num;
				return result;
			}
		}
		static void Main(string[] args)
		{
			NumberManipulator n = new NumberManipulator();
			Console.WriteLine("8 的階乘： {0}", n.factorial(8));
			Console.ReadLine();
		}
	}
}
```
總體來講，比 Python 繁瑣多了。