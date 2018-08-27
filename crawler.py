import urllib.request
import re
from urllib.request import urlretrieve

#設置關鍵字
keywords = "4034526"
#quote函數進行url編碼(屏蔽特殊的字符)
key = urllib.request.quote(keywords)
#設置User-Agent
headers=("User_Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0")
#自定義opener
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
#循環遍歷抓取


for i in range(0,1):
    url = "https://store.line.me/stickershop/product/"+key+"/zh-Hant"
    #print(url)
    content = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    rule = '(https://stickershop.line-scdn.net/stickershop/v1/sticker/[0-9]+/ANDROID/sticker.png)' #正則匹配

    chineseRule = '[\u4e00-\u9fff]+'
    titleRule = '"mdCMN08Ttl">' + chineseRule
    titleString = (re.compile(titleRule).findall(content)).__str__()
    title = re.compile(chineseRule).findall(titleString)

    title = getTitle(content)
    imglist = re.compile(rule).findall(content) #獲取圖片列表
    for j in range(0,len(imglist)):
        imgurl = imglist[j]
        file = "C:\\Users\\ximple\\Documents\\LanceProject\\img\\"+str(j+1)+".jpg"
        urlretrieve(imgurl, filename=file)
        print('第', j +1, '張下載完成!')


