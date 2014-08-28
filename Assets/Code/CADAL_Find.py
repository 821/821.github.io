# -*- coding: utf-8 -*-
import httplib,urllib,os
#一堆構造鏈接用的變量
BookNum=raw_input("Tell me your BookNum: ")
BookNum1=BookNum[:2]
BookNum2=str((int(BookNum[2:5])+1)*1000).zfill(6)
BookType=["book","anc","minguo","minguoqikan","qikan","deg","dunhuang","eng","shufa"]
BookLib=["dlib","dlib1","dlib2","dlib3","dlib4","dlib5","dlib6","newebooks7","newebooks8","newebooks9","newebooks10","newebooks11"]
#存儲用的文件夾
Path="F:\\"+BookNum+"\\"
for Type in BookType:
	for Lib in BookLib:
		URIPart="/"+Lib+"/ebooks/"+Type+"/"+BookNum1+"/"+BookNum2+"/"+BookNum+"/ptiff/"
		URI=URIPart+"00000001.djvu"
		#測試鏈接是否正確，正確就進入下載階段，不正確就試下一個
		Test=httplib.HTTPConnection("210.32.137.91")
		Test.request("GET", URI)
		Response=Test.getresponse()
		if Response.status == 200:
			os.mkdir(Path)
			#Catalog.xml 一般都是存在的，不判斷了
			CatURL="http://210.32.137.91"+"/"+Lib+"/ebooks/"+Type+"/"+BookNum1+"/"+BookNum2+"/"+BookNum+"/meta/Catalog.xml"
			DownCat=urllib.urlretrieve(CatURL,Path+"Catalog.xml")
			for Page in range(1,99999999):
				ThePage=str(Page).zfill(8)+".djvu"
				#測試該頁是否存在，如果存在就下載，不存在說明下完了
				PageTest=httplib.HTTPConnection("210.32.137.91")
				PageTest.request("GET", URIPart+ThePage)
				PageResponse=PageTest.getresponse()
				if PageResponse.status == 200:
					PageURL="http://210.32.137.91"+URIPart+ThePage
					DownPage=urllib.urlretrieve(PageURL,Path+ThePage)
				else:
					print "Finish!"
					raw_input()
					#用 break 會直接跳出，看不到回饋，所以來個 dirty hack
		else:
			pass
print "Not found!"
raw_input()