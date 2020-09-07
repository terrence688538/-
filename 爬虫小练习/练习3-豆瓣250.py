# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 09:43:49 2019

@author: Mechrevo
"""

#爬取豆瓣250
import requests
from bs4 import BeautifulSoup
import pandas as pd
def getHTML(url,headers):
    try:
        r=requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '爬取出错'
def parsehtml(html,movielist):
    soup=BeautifulSoup(html,'lxml')
    m=soup.find('ol',class_="grid_view")
    t=m.find_all('li')
    for link in t:
        name=link.find('span',class_='title').text.strip()
        rate=link.find('span',class_="rating_num").text.strip()
        num=link.find('div',class_="star").contents[7].text.strip()
        info = link.find('div', class_='bd').p.text.strip()
        info = info.replace("\n", " ").replace("\xa0", " ")
        movielist.append([name,rate,num,info])
        
        
def main():
    movielist=[]
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    for i in range(11):
            url='https://movie.douban.com/top250?start='+str(i*25)+'&filter='
            print('正在爬取第%s页：'%(i))
            print(url+'\n')
            html=getHTML(url,headers)
            parsehtml(html,movielist)
    frame=pd.DataFrame(movielist)
    print(frame)

if __name__=='__main__':
    main()
