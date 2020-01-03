# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv

#解決分級警告頁面
payload={'from':'/bbs/Gossiping/index.html','yes':'yes'}
rs=requests.session()
res=rs.post('https://www.ptt.cc/ask/over18',data=payload)

page=int(input('請輸入要找幾頁：'))

#換頁
def next_page():
    soup_next=soup.select('div.btn-group-paging a')
    url_new='https://www.ptt.cc/'+soup_next[1]['href']
    return url_new

find_list=list()
url='https://www.ptt.cc/bbs/Gossiping/index.html'
#爬蟲主程式
for i in range(page):
    res=rs.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    for a in soup.find_all('div','r-ent'):
        list_three=list()
        if a.find('a'):
            href=a.find('a')['href']
            title=a.find('a').string
            date=a.find('div','date').string
            list_three.append(title)
            list_three.append('https://www.ptt.cc/'+href)
            list_three.append(date)
        else:
            for i in range(3):
                list_three.append('None')
        find_list.append(list_three)
    url=next_page()

#確認用
"""
for i in find_list:
    print(i)
"""

#寫成csv
"""        
with open('ptt.csv','w',encoding='utf8',newline='') as f:
    writes=csv.writer(f)
    writes.writerow(('標題','連結','日期'))
    for item in find_list:
        writes.writerow((column for column in item))
"""