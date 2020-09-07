import requests
from bs4 import BeautifulSoup
import time
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
for i in range(1,11):
    link = 'https://beijing.anjuke.com/sale/p' + str(i)
    r = requests.get(link, headers = headers)
    print ('现在爬取的是第', i, '页')
    soup = BeautifulSoup(r.text, 'lxml')
    house_list = soup.find_all('li', class_="list-item")
    for house in house_list:
        name = house.find('div', class_ ='house-title').a.text.strip()
        price = house.find('span', class_='price-det').strong.text.strip()
        price_area = house.find('span', class_='unit-price').text.strip()
        no_room = house.find('div', class_='details-item').contents[1].text
        area = house.find('div', class_='details-item').contents[3].text
        floor = house.find('div', class_='details-item').contents[5].text
        year = house.find('div', class_='details-item').contents[7].text
        address = house.find('span', class_='comm-address').text.strip()
        address = address.replace('\xa0\xa0\n                    ','  ')
        tag_list = house.find_all('span', class_='item-tags')
        tags = [i.text for i in tag_list]
        print (name, price, price_area, no_room, area, floor, year, address, tags)
    time.sleep(5)
