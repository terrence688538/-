from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import pandas as pd


def yiyueriqi():
    try:
        browser = webdriver.Chrome()
        wait = WebDriverWait(browser, 10)
        browser.get('http://qianxi.baidu.com/')
        quanguo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#content > div > div.app-head > div.app-head-left.app-head-city.right-side > div')))
        quanguo.click()
        wuhan = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#hot_city_ids > a:nth-child(13)')))
        wuhan.click()
        qianchu=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#content > div > div.mgs-handle.antd > ul > li:nth-child(2)')))
        qianchu.click()
        riqi_1=0
        riqi_2=0
        bbb = pd.DataFrame(columns=['城市', '省份'])
        ccc = pd.DataFrame(columns=['城市', '省份'])
        for i in range(22,53):
            riqi_1 +=1
            riqi = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#content > div > div.app-head > div.app-head-left.mgs-date > div')))
            riqi.click()
            #riqi_list = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#content > div > div.app-head > div.app-head-left.mgs-date > div > div > ul.hui-option-list')))
            riqi_nouyi = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#content > div > div.app-head > div.app-head-left.mgs-date > div > div > ul.hui-option-list > li:nth-child('+str(i)+')')))
            riqi_nouyi.click()
            html = browser.page_source
            items = re.findall('<div><span class="mgs-date-city">(.*?)</span><span class=.*?>(.*?)</span></div></td><td>(.*?)</td></tr>',html)
            aaa=pd.DataFrame(items,columns=['省份','城市','1月第'+str(riqi_1)+'天流出'])
            bbb=pd.merge(aaa,bbb,how='outer',on=['省份','城市'])
        for i in range(1,23):
            riqi_2 +=1
            riqi = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#content > div > div.app-head > div.app-head-left.mgs-date > div')))
            riqi.click()
            #riqi_list = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#content > div > div.app-head > div.app-head-left.mgs-date > div > div > ul.hui-option-list')))
            riqi_nouyi = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#content > div > div.app-head > div.app-head-left.mgs-date > div > div > ul.hui-option-list > li:nth-child('+str(i)+')')))
            riqi_nouyi.click()
            html = browser.page_source
            items = re.findall('<div><span class="mgs-date-city">(.*?)</span><span class=.*?>(.*?)</span></div></td><td>(.*?)</td></tr>',html)
            aaa=pd.DataFrame(items,columns=['省份','城市','1月第'+str(riqi_2)+'天流出'])
            ccc=pd.merge(aaa,ccc,how='outer',on=['省份','城市'])
        return bbb,ccc
    except:
        return yiyueriqi()


def main():
    merge1,merge2=yiyueriqi()
    merge1.to_excel(r'C:\Users\Mechrevo\Desktop\一月武汉人口流出.xlsx')
    merge2.to_excel(r'C:\Users\Mechrevo\Desktop\二月武汉人口流出.xlsx')

main()


