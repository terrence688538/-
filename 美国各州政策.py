import requests
from bs4 import BeautifulSoup
import pymongo

client=pymongo.MongoClient('localhost')
db=client['USA_policy']

def save_to_mongo(result):
    try:
        if db['zheng_ce'].insert(result):
            print('存储到MongoDB成功',result)
    except Exception:
        print('存储到MongoDB失败',result)

url='https://www.washingtonpost.com/graphics/2020/national/states-reopening-coronavirus-map/'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
}
response=requests.get(url=url,headers=headers)
soup=BeautifulSoup(response.text,'html.parser')
country=soup.find_all('div',class_='mt-md pl-sm pr-sm')
for i in country:
    mesg = i.find_all('p')
    timeflow = []
    for j in mesg:
        timeflow.append(j.text)
    try:
        open=i.find_all('li', class_="db font-xs pb-sm")[0].text.replace('Open now: ', ''),
    except:
        pass
    try:
        close=i.find_all('li', class_="db font-xs pb-sm")[1].text.replace('Still closed: ', '')
    except:
        pass
    item={
        'name':i.h3.text,
        'serious':i.find_all('span',class_="bold font-xs mb-sm dib pa-xxs pl-xs pr-xs white brad-4 highlight")[0].text,
        'open': open,
        'close': close,
        'Timeflow':timeflow
    }
    save_to_mongo(item)


list=[]