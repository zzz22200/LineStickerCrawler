from urllib import request
from urllib import error
from urllib.request import urlretrieve
import os, re
from bs4 import BeautifulSoup
import configparser
from apng2gif import apng2gif

config = configparser.ConfigParser()
config.read('crawler.config')
# 下載儲存位置
directoryLocation = os.getcwd() + '\\img'
# 設置要爬的頁面
urlList = config['lineStoreUrl']['url'].split(',')
downLoadType = '貼圖'

# 設置User-Agent
headers = ("User_Agent",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0")
# 自定義opener
opener = request.build_opener()
opener.addheaders = [headers]
request.install_opener(opener)


def saveImg(imgurl, downLoadType):
    fileLocation = directoryLocation + "\\" + downLoadType + "\\" + title
    if not os.path.exists(fileLocation):
        os.makedirs(fileLocation)
    file = fileLocation + "\\" + str(count + 1) + ".png"
    urlretrieve(imgurl, filename=file)
    return file


def getTitle(content):
    soup = BeautifulSoup(content, 'html.parser')
    title = soup.find('h3', 'mdCMN08Ttl').text
    return title


def hasAnimationPng(imgurl):
    animationUrl = imgurl[:-4] + '_animation@2x.png'
    try:
        animationUrl = re.sub('ANDROID', 'IOS', animationUrl)
        request.urlopen(animationUrl)
        file = saveImg(animationUrl, '動圖')
        apng2gif(file)
    except error.URLError  as err:
        saveImg(imgurl, downLoadType)


for i in range(0, len(urlList)):
    downLoadType = '貼圖'
    content = request.urlopen(urlList[i]).read().decode("utf-8", "ignore")
    rule = '(https.*sticker\.png)'  # 正則匹配
    ruleEmoji = '(https.*/\d{3}\.png)'
    title = getTitle(content)
    title = re.sub('\s', '', title)
    title = re.sub('[\W_]+', '', title)

    print('開始下載 ' + title)
    imglist = re.compile(rule).findall(content)  # 獲取圖片列表
    if len(imglist) == 0:
        imglist = re.compile(ruleEmoji).findall(content)  # 小表情規則
        downLoadType = '小表情'
    for count in range(0, len(imglist)):
        imgurl = hasAnimationPng(imglist[count])

        print('第', count + 1, '張下載完成!')
print("已全部下載完成")
