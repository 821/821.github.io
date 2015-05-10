---
layout: indexed
title: C 語言新坑
date: '2015/05/09'
---
C 語言是當下最重要的編程語言，沒有之一。有一天我忽然發覺自己與其學 C++ 不如學 C ，因爲我討厭面向對象編程，能不用就不用。
其實我差不多十年前學過，好像是三天內上午上課下午上機，學到吐那種，一點印象都沒了。 C 語言是常用語言裏最難的一門，或者說是抽象度最低的一門，所以衹能挖一個坑慢慢塡了。反正我坑多，摔多就不痛。

## 基礎
```c
/* 多行註釋 */
// 單行註釋
#include <stdio.h> // # 表示預處理器指令
int main (void) // 主函數
{
	printf("Hello, World!\n");
	puts("Hello, World!"); // 效果同上
// puts 和 printf 相差一個換行，而且 printf 輸出 % 號要寫作 %%
	printf(%d, 1+1); // %d 這種寫法在 Python 見過
	int num; // 定義變量 num
	scanf("%d", num) // 請用戶來輸入
	return 0;
}
```

#### 保留字
auto, else, long, switch, break, enum, register, typedef, case, extern, return, union
char, float, short, unsigned, const, for, signed, void, continue, goto, sizeof, volatile, default, if, static, while, do, int, struct, _Packed, double

### 變量、運算、循環、分支
在 C++ 學過了。

#### 數組
```c
// 格式： type arrayName [ arraySize ]; 比如：
int array[5];
// 在 array 的 第 0 位添加元素：
array[0] = 1
// 訪問 array 第 0 位元素的値：
array[0]
// 多維數組：
int a[3][2] = {
 	{0, 1, 2},
 	{3, 4},
 	{5, 6}
};
// 嵌套的大括號也可不寫：
int a[2][3] = {0,1,2,3,4,5,6};
// 訪問多維數組：
int num = a[0][1] // 訪問數組 a 的第一行第 2 元素
```

### 常量
```c
#define TEN 10 // 定義一個常量 TEN ，値爲 10
const int ONE = 1; // 定義一個常量 ONE ，値爲 1
```
常量名一般用大寫。

### 存儲類
```c
auto int a; // 局部變量的默認類
static int c = 5; // 全局變量
extern int count; // 全局到別的文件都能訪問
register int b; // 存在寄存器，而非內存
```