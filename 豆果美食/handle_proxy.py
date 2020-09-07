import requests


#106.122.104.152
url='http://ip.hahado.cn/ip'
proxy={'http':'http://用户名：密码@代理服务器地址：端口号'}                  #格式要用这种            在阿布云上买
response=requests.get(url=url,proxies=proxy)
print(response.text)