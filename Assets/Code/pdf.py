#coding: gbk
#使用 Python 3
import http.client,urllib.request,os,re
#獲取各種參數
def GetAll(ZXLink):
	Domain=re.findall(r'http://([^/]+)/.+',ZXLink)[0] # 域名
	URI=re.findall(r'http://[^/]+(/.+)',ZXLink)[0] # URI
	Response = urllib.request.urlopen(ZXLink)
	Web = str(Response.read())
	Response.close()
	PDFLink = re.findall(r'<a href="([^<]+)" target="_blank" >PDF</a>', Web)[0] # PDF 的實際鏈接
	ssNo = re.findall(r'ssNo = "(\d{8})"', Web)[0] # 超星號
	jpgRange = re.findall(r'jpgRange = "(\d+-\d+)"', Web)[0] # 頁碼
	return (PDFLink, Name, ssNo, jpgRange)
#下載
def DownPDF(Link, Page):
	urllib.request.urlretrieve(Link, Path+Page+".pdf")

for a in range(1,100):
	ZX=input("ZX link: ")
	PDFLink, Name, ssNo, jpgRange = GetAll(ZX)
	Path="F:\\"+ssNo+"\\"
	os.makedirs(Path, exist_ok=True)
	DownPDF(PDFLink,jpgRange)