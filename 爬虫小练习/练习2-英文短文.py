# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 21:22:48 2019

@author: Mechrevo
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def getHTML(url,headers):
    try:
        r=requests.get(url,headers,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "爬取出错"
def parsehtml(html,englishnamelist,chinanamelist,urllist):
    url='http://www.en8848.com.cn/'
    soup=BeautifulSoup(html,'html.parser')
    t=soup.find('div',class_="ch_content")
    i=t.find_all('a')
    for link in i[1:59:2]:
        urllist.append(url+link.get('href'))
        englishnamelist.append(link.get('title'))
    o=t.find_all('p')
    for link1 in o:
        chinanamelist.append(link1.text)

def main():
    englishnamelist=[]
    chinanamelist=[]
    urllist=[]
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    for i in range(1,21):
        if i==i:
            url='http://www.en8848.com.cn/article/love/dating/index.html'
        else:
            url='http://www.en8848.com.cn/article/love/dating/index_'+str(i)+'.html'
        print('正在爬取第%s页:'%(i))
        print(url+'\n')
        html=getHTML(url,headers)
        parsehtml(html,englishnamelist,chinanamelist,urllist)
    print('爬取完成')
    frame=pd.DataFrame({'url':urllist,'中文名':chinanamelist,'英文名':englishnamelist})
    print(frame)

if __name__=='__main__':
    main()
            
            
    
    