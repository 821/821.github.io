---
layout: page
title: 筆記
---
#筆記
筆記顯然絕大多數是重複造輪子，但爲什麼要做筆記？原因在於，別人寫的，不管文字多麼通透，也不是直達內心的。閱讀別人的筆記，難免有些「隔」。記筆記，就是爲了不「隔」。

{% for Notes in site.Notes %}
	<a href="{{ Notes.url }}">{{ Notes.title }}</a><br />
{% endfor %}