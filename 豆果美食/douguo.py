import  requests
import json
#引入队列
from multiprocessing import Queue
from mitmdumptest.douguomeishi.handel_mongo import  mongo_info
#引入线程池
from concurrent.futures import ThreadPoolExecutor

#创建队列
queue_list=Queue()


#这个header 和data要自己试哪个要哪个不要
def handle_request(url,data):                  #这个header要用sublime ctrl+h替换选择。* 和Aa   (.*?):(.*)   "$1":"$2",
    header={
        "client":"4",
        "version":"6955.4",
        "device":"MI 9",
        "sdk":"22,5.1.1",
        "imei":"863064983458102",               #一定不能去掉             在夜神模拟器中收集于网络设置可以设置手机与网络设置，就可以设置IMEI值，这个值可以在那里面伪造
        "channel":"baidu",
        #"mac":"0A:00:27:00:00:06",
        "resolution":"1600*900",
        "dpi":"2.0",
        #"android-id":"04d3b03a0a259801",
        #"pseudo-id":"03a0a25980104d3b",
        "brand":"Xiaomi",
        "scale":"2.0",
        "timezone":"28800",
        "language":"zh",
        "cns":"3",
        "carrier":"CHINA+MOBILE",
        #"imsi":"460079801581025",
        "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Xiaomi Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36",
        "act-code":"1578127339",
        "act-timestamp":"1578127339",
        "uuid":"cc329a60-abf5-42af-8b44-f8d108a311cc",
        "battery-level":"1.00",
        "battery-state":"3",
        "newbie":"1",
        "reach":"10000",
        "Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
        "Accept-Encoding":"gzip, deflate",
        "Connection":"Keep-Alive",
        #"Cookie":"duid=62413283",                        一定不要有，很容易被发现
        "Host":"api.douguo.net",
        #"Content-Length":"179",
    }
    #设置的代理ip
    proxy = {'http': 'http://用户名：密码@代理服务器地址：端口号'}
    response=requests.post(url=url,headers=header,data=data,proxies=proxy)
    return response

def handle_index():
    url='http://api.douguo.net/recipe/flatcatalogs'
    data={
        "client": "4",
        #"_session": "1578467370035863064983458102",
        #"v": "1578460637",       #时间戳
        "_vs": "2305",                  #一定不能去掉
        #"sign_ran": "774399437178d79877cfdb84059fa408",
        #"code": "43af94f0ede983f1",
    }
    response=handle_request(url=url,data=data)
    #print(response.text)
    # 需要把json数据变为dict
    index_response_dict=json.loads(response.text)
    for index_item in index_response_dict['result']['cs']:
        for index_item_1 in index_item['cs']:
            for item in index_item_1['cs']:
                data_2={
                    "client": "4",
                    #"_session": "1578467370035863064983458102",
                    "keyword": item['name'],
                    "order": "3",
                    "_vs": "11104",
                    #"type": "0",
                    #"auto_play_mode": "2",
                    #"sign_ran": "667b5c145425aed03bc940b43ed65515",
                    #"code": "91398da8f5d42ef1",
                }
                queue_list.put(data_2)                 #往队列里放


#线程的处理函数，把队列里的data get出来
def handle_caipu_list(data):
    print('当前处理的食材： ',data['keyword'])
    caipu_list_url='http://api.douguo.net/recipe/v2/search/0/20'
    caipu_list_response=handle_request(url=caipu_list_url,data=data)
    caipu_list_response_dict=json.loads(caipu_list_response.text)
    for item in caipu_list_response_dict['result']['list']:
        caipu_info={}
        caipu_info['shicai'] =data['keyword']
        if item['type']==13:
            caipu_info['user_name']=item['r']['an']
            caipu_info['shicai_id']=item['r']['id']
            caipu_info['describe']=item['r']['cookstory'].replace('\n','').replace(' ','')
            caipu_info['caipu_name']=item['r']['n']
            caipu_info['zuoliao_list']=item['r']['major']
            detail_url='http://api.douguo.net/recipe/detail/'+str(caipu_info['shicai_id'])
            detail_data={
                "client": "4",
                #"_session": "1578620775053863064983458102",
                "author_id": "0",
                "_vs": "11104",
                "_ext": '{"query":{"kw":'+caipu_info['shicai']+',"src":"11104","idx":"1","type":"13","id":'+str(caipu_info['shicai_id'])+'}}',
                #"is_new_user": "1",
                #"sign_ran": "70fdd5df9582b87b7b5c18c77cf2329c",
                #"code": "ca5caf55eeccfb49",
            }
            detail_response=handle_request(url=detail_url,data=detail_data)
            detail_response_dict=json.loads(detail_response.text)
            caipu_info['tips']=detail_response_dict['result']['recipe']['tips']
            caipu_info['cook_step'] = detail_response_dict['result']['recipe']['cookstep']
            print('当前入库的菜谱是 ',caipu_info['caipu_name'])
            mongo_info.insert_item(caipu_info)

        else:
            continue #跳过去
handle_index()
#多线程抓取，引入线程池
pool=ThreadPoolExecutor(max_workers=2)
while queue_list.qsize() >0:
    pool.submit(handle_caipu_list,queue_list.get())
