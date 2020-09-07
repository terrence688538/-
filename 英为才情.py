import requests
import xlwings as xw
import pandas as pd
import numpy as np
import re
from WindPy import *

wb=xw.Book(r'C:\Users\Mechrevo\Desktop\日报\日报数据库Wind(1).xlsx')
#https://cn.investing.com/rates-bonds/germany-2-year-bond-yield-historical-data  德国2年
#https://cn.investing.com/rates-bonds/germany-10-year-bond-yield-historical-data   德国10年
#https://cn.investing.com/currencies/us-dollar-index-historical-data                                美元指数
#https://cn.investing.com/commodities/crude-oil-historical-data                        NYMEX原油
#https://cn.investing.com/currencies/eur-usd-historical-data                   欧元兑美
#https://cn.investing.com/currencies/gbp-usd-historical-data                    英镑兑美元
#https://cn.investing.com/commodities/gold-historical-data                黄金
#https://cn.investing.com/currencies/usd-cnh-historical-data             离岸人民比
#https://cn.investing.com/currencies/usd-cny-historical-data                 在岸
#https://cn.investing.com/indices/volatility-s-p-500-historical-data             VIX
#https://cn.investing.com/rates-bonds/germany-2-year-bond-yield-historical-data   美2
#https://cn.investing.com/rates-bonds/germany-10-year-bond-yield-historical-data      美10

def scrapy(date,html):
    date = date
    pattern_1 = re.compile('<td.*?>' + date + '</td>.*?<td.*?Font.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?Font">(.*?)</td>',re.S)
    kai_pan, shou_pan, fudong = re.findall(pattern_1, html)[0]
    return kai_pan,shou_pan,fudong
url=[
    'https://cn.investing.com/indices/volatility-s-p-500-historical-data',
    'https://cn.investing.com/currencies/us-dollar-index-historical-data',
    'https://cn.investing.com/currencies/gbp-usd-historical-data',
    'https://cn.investing.com/currencies/eur-usd-historical-data',
    'https://cn.investing.com/currencies/usd-cny-historical-data',
    'https://cn.investing.com/currencies/usd-cnh-historical-data',
    'https://cn.investing.com/commodities/crude-oil-historical-data',
    'https://cn.investing.com/commodities/gold-historical-data',
    'https://cn.investing.com/rates-bonds/u.s.-10-year-bond-yield-historical-data',
    'https://cn.investing.com/rates-bonds/u.s.-2-year-bond-yield-historical-data',
    'https://cn.investing.com/rates-bonds/germany-10-year-bond-yield-historical-data',
    'https://cn.investing.com/rates-bonds/germany-2-year-bond-yield-historical-data',
]
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
date='2020年9月4日'
data_standard='2020-9-4'
date_before="2020年9月3日"
zhai_yao=[]
for i in range(len(url)):
    a=requests.get(url[i],headers=headers)
    html=a.text
    shou_pan,kai_pan,fudong=scrapy(date,html)
    shou_pan_before, kai_pan_before, fudong_before = scrapy(date_before, html)
    name=['VIX','美元指数','英镑兑美元','欧元兑美元','在岸','离岸','原油','黄金','美债10','美债2','德债10','德债2']
    a=i
    if a==0:
        sht = wb.sheets[0]
        sht.api.Rows(5).Insert()
        sht.range('B5').value =data_standard
        sht.range('C5').value=shou_pan
    elif a==1:
        sht = wb.sheets[2]
        sht.api.Rows(5).Insert()
        sht.range('B5').value = data_standard
        sht.range('C5').value = shou_pan
    elif a==2:
        sht = wb.sheets[2]
        sht.range('H5').value = data_standard
        sht.range('I5').value = shou_pan
    elif a==3:
        sht = wb.sheets[2]
        sht.range('K5').value = data_standard
        sht.range('L5').value = shou_pan
    elif a==4:
        sht = wb.sheets[2]
        sht.range('R6').value = data_standard
        sht.range('S6').value = shou_pan
    elif a==5:
        sht = wb.sheets[2]
        sht.range('T6').value = shou_pan
    elif a==6:
        sht = wb.sheets[3]
        sht.api.Rows(5).Insert()
        sht.range('B5').value = data_standard
        sht.range('C5').value = shou_pan
    elif a==7:
        sht = wb.sheets[3]
        sht.range('E6').value = data_standard
        sht.range('F6').value = shou_pan
    elif a==8:
        sht = wb.sheets[4]
        sht.api.Rows(5).Insert()
        sht.range('B5').value = data_standard
        sht.range('C5').value = shou_pan
    elif a==9:
        sht = wb.sheets[4]
        sht.range('E5').value = data_standard
        sht.range('F5').value = shou_pan
    elif a==10:
        sht = wb.sheets[4]
        sht.range('H5').value = data_standard
        sht.range('I5').value = shou_pan
    elif a==11:
        sht = wb.sheets[4]
        sht.range('K5').value = data_standard
        sht.range('L5').value = shou_pan
    if i<1:
        print(date+name[i] + '收：', shou_pan, name[i] + '开：', kai_pan, name[i] + '变化：',float(shou_pan)-float(shou_pan_before) )
    elif i>7:
        print(date + name[i] + '收：', shou_pan, name[i] + '开：', kai_pan, name[i] + '变化：',((float(shou_pan) - float(shou_pan_before))*100),'个基点')
    else:
        print(date + name[i] + '收：', shou_pan, name[i] + '开：', kai_pan, name[i] + '变化：',fudong)
    #time.sleep(random.uniform(3,5))


w.start()
gu_piao=w.wsq("DJI.GI,IXIC.GI,SPX.GI,GSPTSE.GI,IBOVESPA.GI,FTSE.GI,FCHI.GI,GDAXI.GI,IMOEX.MCX,N225.GI,KS11.GI,AS51.GI,HSI.HI", "rt_date,rt_pre_close,rt_open,rt_pct_chg")
zhi_shu=pd.DataFrame(gu_piao.Data).T
Name=['道琼斯','纳斯达克','标普500','多伦多','巴西','英国','法国','德国','俄罗斯','日经','韩国','澳大利亚','恒生']
zhi_shu['name']=Name
#zhi_shu.set_index(Name)
gujia=wb.sheets[1]
zhi=zhi_shu[3]
zhi=zhi[:,np.newaxis]
gujia.range('R9').value =zhi