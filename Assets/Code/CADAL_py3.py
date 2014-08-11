# -*- coding: utf-8 -*-
import http.client,urllib.request,os,re
#一堆構造鏈接用的變量
UserInput=input("The link or BookNum: ")
FindNum=re.search(r'\d{8}',UserInput)
BookNum=FindNum.group(0)
BookNum1=BookNum[:2]
BookNum2=str((int(BookNum[2:5])+1)*1000).zfill(6)
BookType=["book","anc","minguo","minguoqikan","qikan","deg","dunhuang","eng","shufa"]
BookLib=["dlib","dlib1","dlib2","dlib3","dlib4","dlib5","dlib6","newebooks7","newebooks8","newebooks9","newebooks10","newebooks11"]
#存儲用的文件夾， \ 號第一個是不生效的，所以寫兩個
Path="F:\\"+BookNum+"\\"
#寫個鏈接測試函數一會用
def Check(Tested):
	Test=http.client.HTTPConnection("210.32.137.91")
	Test.request("GET", Tested)
	Response=Test.getresponse()
	if Response.status == 200:
		return True
	else:
		return False
#開始循環，找正確鏈接了
for Type in BookType:
	for Lib in BookLib:
		URIPart="/"+Lib+"/ebooks/"+Type+"/"+BookNum1+"/"+BookNum2+"/"+BookNum+"/ptiff/"
		URI=URIPart+"00000001.djvu"
		#測試鏈接是否正確，正確就進入下載階段，不正確就試下一個
		if Check(URI):
			os.makedirs(Path, exist_ok=True)#如果文件夾已存在就不用建立了
			#Catalog.xml 一般都是存在的，不判斷了
			print("Downloading Catalog.xml")
			CatURL="http://210.32.137.91"+"/"+Lib+"/ebooks/"+Type+"/"+BookNum1+"/"+BookNum2+"/"+BookNum+"/meta/Catalog.xml"
			DownCat=urllib.request.urlretrieve(CatURL,Path+"Catalog.xml")
			for Page in range(1,99999999):
				ThePage=str(Page).zfill(8)+".djvu"
				#測試該頁是否存在，如果存在就下載，不存在說明下完了
				if Check(URIPart+ThePage):
					#看看是否已經下載，下過了就跳過
					FileExist=os.path.isfile(Path+ThePage)
					if FileExist == False:
						print("Downloading page "+str(Page))
						PageURL="http://210.32.137.91"+URIPart+ThePage
						DownPage=urllib.request.urlretrieve(PageURL,Path+ThePage)
					else:
						pass
				else:
					print("Finish!")#看不見這一句說明沒下載完。
					input()
					#用 break 會直接跳出，看不到回饋，所以來個 dirty hack
		else:
			pass
print("Not found!")#看不見這一句說明沒試完所有鏈接程序就跳出了。
input()