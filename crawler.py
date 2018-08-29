import urllib.request
import re
from urllib.request import urlretrieve
import os
from bs4 import BeautifulSoup
import configparser

config = configparser.ConfigParser()
config.read('crawler.config')
#下載儲存位置
directoryLocation=os.getcwd()+'\\img'
#設置要爬的頁面
urlList = config['lineStoreUrl']['url'].split(',')


#設置User-Agent
headers=("User_Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0")
#自定義opener
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)



def getTitle(content):
    soup = BeautifulSoup(content, 'html.parser')
    title=soup.find('h3','mdCMN08Ttl').text
    return title

for i in range(0,len(urlList)):

    content = urllib.request.urlopen(urlList[i]).read().decode("utf-8","ignore")
    rule = '(https.*sticker\.png)' #正則匹配
    title = getTitle(content)
    fileLocation = directoryLocation+"\\"+title
    if not os.path.exists(fileLocation):
        os.makedirs(fileLocation)
    print('開始下載 '+title)
    imglist = re.compile(rule).findall(content) #獲取圖片列表
    for j in range(0,len(imglist)):
        imgurl = imglist[j]
        file = fileLocation+"\\"+str(j+1)+".jpg"
        urlretrieve(imgurl, filename=file)
        print('第', j +1, '張下載完成!')
print("已全部下載完成")

