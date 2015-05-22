---
layout: post
title: VBScript
---
VBScript ，一個有點過氣的玩意，但偶爾還會秀一下存在感。

## 數據類型

類型|特點
----|----
Empty|未初始化變量。數値變量爲 0 ，字符串變量爲 ""
Null|無任何有效數據
Boolean|True, False。
Byte|整數， 0 - 255
Integer|整数， -32,768 - 32,767
Long|整數， -2,147,483,648 - 2,147,483,647
Currency|小數，範圍很大
Single|單精度浮點數
Double|雙精度浮點數
Date (Time)|日期， AD 100 - AD 9999
String|字符串， 20 億字符以內。
Object|對象
Error|錯誤號

## 變量
命名必須以字母開頭，不可用 . ， 255 字符以內。
定義與賦値：
```vbscript
Dim var
var = "abc"
```