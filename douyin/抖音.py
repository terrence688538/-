import requests
from lxml import etree
import re
from 爬虫.抖音.handle_db import handle_get_task
import time

def handle_decode(input_data):

    search_douyin_str=re.compile(r'抖音ID：')
    # 抖音web数字混淆破解列表
    regex_list = [
        {'name': [' &#xe603; ', ' &#xe60d; ', ' &#xe616; '], 'value': 0},
        {'name': [' &#xe602; ', ' &#xe60e; ', ' &#xe618; '], 'value': 1},
        {'name': [' &#xe605; ', ' &#xe610; ', ' &#xe617; '], 'value': 2},
        {'name': [' &#xe604; ', ' &#xe611; ', ' &#xe61a; '], 'value': 3},
        {'name': [' &#xe606; ', ' &#xe60c; ', ' &#xe619; '], 'value': 4},
        {'name': [' &#xe607; ', ' &#xe60f; ', ' &#xe61b; '], 'value': 5},
        {'name': [' &#xe608; ', ' &#xe612; ', ' &#xe61f; '], 'value': 6},
        {'name': [' &#xe60a; ', ' &#xe613; ', ' &#xe61c; '], 'value': 7},
        {'name': [' &#xe60b; ', ' &#xe614; ', ' &#xe61d; '], 'value': 8},
        {'name': [' &#xe609; ', ' &#xe615; ', ' &#xe61e; '], 'value': 9},
    ]
    #正则表达式替换数字
    for i1 in regex_list:
        for i2 in i1['name']:
            input_data=re.sub(i2,str(i1['value']),input_data)
    share_web_html = etree.HTML(input_data)
    user_info = {}
    user_info['nickname'] = share_web_html.xpath('//*[@id="pagelet-user-info"]/div[2]/div[1]/p[1]/text()')[0]
    douyin_id1=share_web_html.xpath("//p[@class='shortid']/text()")[0].replace(' ','')
    douyin_id2=''.join(share_web_html.xpath("//p[@class='shortid']/i/text()"))
    user_info['douyin_id']=re.sub(search_douyin_str,'',douyin_id1+douyin_id2)
    #user_info['job']=share_web_html.xpath("//span[@class='info']/text()")[0].replace(' ','')
    user_info['describe']=share_web_html.xpath("//p[@class='signature']/text()")[0]
    user_info['guanzhu']=''.join(share_web_html.xpath("//p[@class='follow-info']/span[1]//i/text()"))
    fensi= ''.join(share_web_html.xpath("//p[@class='follow-info']/span[2]//i/text()"))
    danwei1=share_web_html.xpath("//p[@class='follow-info']/span[2]/span[@class='num']/text()")[-1]
    if danwei1.strip()=='w':
        user_info['fans']=str(int(fensi)/10)+'w'
    like = ''.join(share_web_html.xpath("//p[@class='follow-info']/span[3]//i/text()"))
    danwei2= share_web_html.xpath("//p[@class='follow-info']/span[3]/span[@class='num']/text()")[-1]
    if danwei2.strip() == 'w':
        user_info['like'] = str(int(like) / 10) + 'w'
    print(user_info)


def handle_douyin_web_share(task):
    share_web_url = 'https://www.douyin.com/share/user/%s'%task['share_id']
    share_web_header={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }
    share_web_response=requests.get(url=share_web_url,headers=share_web_header)
    handle_decode(share_web_response.text)

while True:
    task=handle_get_task()
    handle_douyin_web_share(task)
    time.sleep(2)
