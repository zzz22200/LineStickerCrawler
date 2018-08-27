import requests, os
from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup
from urllib.error import HTTPError

first = 'https://sdl-stickershop.line.naver.jp/stickershop/v1/sticker/'
last = '/android/sticker.png'
links = []
try:
    for i in range(23486912, 23486951):
        links.append(first + str(i) + last)  ##範例、str("%03d" % i) 若為三位數，且不足位數需補0
    x = 1
    for link in links:
        local = os.path.join('C:\\Users\\ximple\\Desktop\\line爬圖\\社畜戰爭\\%s.jpg' % x)  # 檔案儲存位置
        x += 1
        urlretrieve(link, local)
        print('第', x - 1, '張下載完成!')
except HTTPError as e:
    print("已全部下載完成")