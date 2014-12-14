---
layout: horizontal
title: 若干電腦字體表
---
字體本來就是我比較在意的，加上折騰 TeX ，越發覺得需要專帖收集。
爲了一目瞭然，就用表格模式配合各種縮寫和說明好了。

##正表

名稱 | 體 | 字形 | 字符集 | 擴展 | 協議 | 備註
-----|----|------|--------|-----|------|-----
SonyReader Ming | 宋 | 舊 | A | ttf | 私有 | 同套字體還有隸、楷、黑三體
[I.BMing](http://founder.acgvlyric.org/iu/doku.php/) | 宋 | 舊 | D| ttf | IPA1 | 修改自IPAmjMincho，強行舊字形
[Asebi Mincho](https://metasta.github.io/asebi/) | 宋 | 舊 |  | otf | IPA1 | 有[源碼](https://github.com/metasta/asebi)，基於IPAmjMincho等
[IPAmjMincho](http://mojikiban.ipa.go.jp/) | 宋 | 2004 | D | ttf | IPA1 |
[HanaMinB](http://fonts.jp/hanazono/) | 宋 | 2004 | E | ttf | OFL | A 衹到 Ext-A ， B 纔全
[cwtex-q-fonts](https://code.google.com/p/cwtex-q-fonts/) | 多 | 舊 | BIG-5 | ttf | OFL+GPL2 | 有仿宋、宋、黑、楷、圓，cwTeX所附字體之修正
[全字庫正宋體](http://www.cns11643.gov.tw) | 宋 | 臺標 | D | ttf | 待考 | 分成兩個字體文件，另有楷體
[BabelStone Han](http://www.babelstone.co.uk/Fonts/Han.html) | 宋 | 新 | 部分A-C | ttf | APL | 作者興趣不在繁體，在二簡
[思源黑體](https://github.com/adobe-fonts/source-han-sans/) | 黑 | 各國 | A+部分B-E | otf | Apache2 | TeX不能直接用
Hiragino Mincho ProN | 宋 | 2004 | Pro | otf | 私有 | MAC OS字體，磅重有 3 和 6
Iwata Souchou Pro M | 仿宋 | 90 | Pro | otf | 私有 |
方正新秀麗 | 宋 | 舊 | BIG-5 | ttf | 私有 | 強行舊字形
宋体-方正超大字符集 | 宋 | 新 | 方正 | ttf | 私有 | 分成兩個字體文件，另有楷體
FZSongS | 宋 | 新 | 2005 | ttf | 私有 | 分成兩個字體文件，另有楷體， Ubuntu 的字體
AdobeFangsongStd-Regular | 宋 | 新 | A | otf | 私有 | 另有國標宋、臺標明、楷、黑等
[Unifonts 6.0](http://okuc.net/SoftWare/UniFonts6.0.exe) | 宋 | 新 | D | ttf | 盜版 | 實際上主要是中易宋體和華康明體
Kozuka Mincho Pr6N | 宋 | 2004 | Pr6 | otf | 私有 | 有 1-6 磅粗細，另有黑體
新細明體+更新包 | 宋 | 臺標 | B | ttf | 私有 | 微軟默認繁體

##說明

####字形
中國基本上是新字形。
臺灣各種矛盾，自命正統又喜標新立異，結果經常滑天下之大稽。臺灣敎育部標準宋體眞是「奇葩」，走之底不從舊字形「⻍」，不從新字形「⻌」，自己根據楷書做了一波三折的「<font face="MingLiu">辶</font>」，不宋不楷，讓人看得眼睛痛。
日本在 JIS90 的時候是日式新字形，後來 JIS2004 的時候又參考回康煕字典，所以現在的 JIS2004 有較多舊字形成分。表中省略 JIS 。

####字符集
字符集表現的是字體的收字數量。當然越大越好，但也需要一些標準來規範。
Unicode / ISO10646: CJK Basic 部分 20925 個漢字（中臺日韓各要一點的雜燴）， CJK Ext-A 收 6582 個漢字， Ext-B 收 42711 個漢字， Ext-C 收 4149 個漢字， Ext-D 收 222 個漢字， Ext-E 收 5762 個漢字， Ext-E 和 Ext-F 還在實驗室階段， Ext-E 預計在 Unicode 8.0 面世。正表中的 A B C D E 就是 Ext-A 之類的縮寫，由於字體製作人一般不會跳過前面的做後面的，默認寫 B 則包含 CJK, Ext-A, Ext-B 。可以看到， Ext-B 比其他加起來都多，所以多數字體止步於 Ext-A 。整個 Unicode CJK 又叫 Unihan 。
GB-2312: 收漢字 6763 個，符號 715 個。這些字在 Unihan 裏叫 G0 。
GB-12345: 收漢字 6866 個，這些字的非 G0 部分在 Unihan 裏叫 G1 。
BIG-5: 收漢字 13060 個，符號 808 個。
GBK: 收漢字 21003 個，符號 882 個，留有 1894 個造字碼位。 GB-2312 和 BIG-5 之倂集。
GB18030-2000: 收漢字 27533 個。 GBK 和 Ext-A 之倂集。
GB18030-2005: 收漢字 70244 個。 GB18030-2000 和 Ext-B 之倂集。表中簡稱 2005 。
方正超大字符集：收漢字 64395 個， GB18030-2000 加 36862 個 Ext-B 所收字。表中簡稱方正。
漢字構形資料庫：自成體系，收漢字 112533 個，其中楷書 62366 個（其餘是甲骨文、金文、小篆、簡帛等一般人不用的），另收異體字 12208 組。<br>
[Adobe Japan](http://www.adobe.com/content/dam/Adobe/en/devnet/font/pdfs/5078.Adobe-Japan1-6.pdf): 把字分爲六等。 1-3 有 9354 個，稱爲 Std ； 1-4 有 15444 個，稱爲 Pro ； 1-5 有 20317 個，稱爲 Pr5 ； 1-6 有 23058 個，稱爲 Pr6 。

####協議
字體協議複雜而特殊，附各種鏈接： [IPA1](http://opensource.org/licenses/IPA), [OFL](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web), [APL](http://ftp.gnu.org/non-gnu/chinese-fonts-truetype/LICENSE)

####選取原則
爲什麼選了這些字體，又沒選別的字體呢？

單條充分非必要條件：
一、全舊字形宋體或舊字形仿宋。
二、收字包含全 CJK Basic + Ext-A 和絕大多數 Ext-B 。

符合三條以上必收，符合兩條選收：
一、以書法家字跡、古籍爲原型且不經過多干預。
二、收字包含全 CJK Basic + Ext-A 。
三、仿宋。
四、帶 vert 或 vrt2 屬性的原生 otf 。
五、開源免費。
六、完整磅重選擇。

不收：
一、三無（無網站、無說明、找不到負責人）。
二、太醜。
三、同系列已收（同系列收錄優先級：仿宋-宋-楷-其他）。
四、難用的（比如 GT2000 ，收字八萬多，但衹有 01 能用於 Unicode ）。
五、日本字體，有 N 的都是 JIS2004 ，其對應無 N 的是 JIS90 ，就不收了。