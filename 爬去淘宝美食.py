import re
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import pymongo

from 爬虫.爬取淘宝美食.config import *

clint=pymongo.MongoClient(MONGO_URL)
db=clint[MONGO_DB]


"""""""""
显性等待(是你在代码中定义等待一定条件发生后再进一步执行你的代码。):
WebDriverWait，配合该类的until()和until_not()方法进行的等待。它主要的意思就是：程序每隔xx秒看一眼，如果条件成立了，则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException。
调用方法如下：
WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)

until()方法参数：
method: 在等待期间，每隔一段时间调用这个传入的方法，直到返回值不是False
message: 如果超时，抛出TimeoutException，将message传入异常

until 中参数method ,用expected_conditions类中的方法：
presence_of_element_located 判断某个元素是否被加到了dom树里
element_to_be_clickable 判断某个元素中是否可见并且是enable的，这样的话才叫clickable
text_to_be_present_in_element 判断某个元素中的text是否包含了预期的字符串
presence_of_all_elements_located: 判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，那么只要有1个元素存在，这个方法就返回True
"""
browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
def search():
    try:
        browser.get('https://www.taobao.com/')
        input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))                    #判断是否加载完成      只要符合条件的q出现就通过
        submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))            #判断是否是可点击
        input.send_keys('美食')
        submit.click
        total=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))                      #返回总的页数
        get_products()
        return total.text
    except TimeoutException:
        return  search()

def next_page(page_number):
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))  # 判断是否加载完成      只要符合条件的q出现就通过
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))  # 判断是否是可点击
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number)))           #在选中的东西里包含某某文字
        get_products()
    except TimeoutException:
        next_page(page_number)

def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html=browser.page_source              #获取源代码
    doc=pq(html)
    items=doc('#mainsrp-pager > div > div > div > ul > li.item.active > span').items()                  #后边调用item方法可以得到所有选择的内容
    for item in items:
        product={
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储到MongoDB成功',result)
    except Exception:
        print('存储到MongoDB失败',result)

def main():
    total=search()
    total=int(re.compile('(\d+)').search(total).group(1))                              #group(0)匹配正则表达式整体的结果         group(1)列出第一个括号的匹配部分       group(2)列出第二个括号匹配部分
    for i in range(2,total+1):
        next_page(i)




if __name__=='__main__':
    main()
