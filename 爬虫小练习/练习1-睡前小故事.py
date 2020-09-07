# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:09:04 2019

@author: Mechrevo
"""

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def getHTML(url,headers):
    try:
        r=requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "爬取失败"
        
def parsehtml(html,namelist,urllist):
    url='http://www.tom61.com/'
    soup=BeautifulSoup(html,'html.parser')
    t=soup.find('dl',class_="txt_box")
    i=t.find_all('a')
    for link in i:
        urllist.append(url+link.get('href'))
        namelist.append(link.get('title'))

def main():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    namelist=[]
    urllist=[]
    for i in range(1,11):
        if i==1:
            url='http://www.tom61.com/ertongwenxue/shuiqiangushi/index.html'
        else:
            url='http://www.tom61.com/ertongwenxue/shuiqiangushi/index_'+str(i)+'.html'
        print('正在爬取第%s页的故事连接：'%(i))
        print(url+'\n')
        html=getHTML(url,headers)
        parsehtml(html,namelist,urllist)
    print('连接爬取完成')
    print(namelist)
    print(urllist)
    frame=pd.DataFrame({'name':namelist,'url':urllist})
    print(frame)
if __name__=='__main__':
    main()
        

