import json
try:
    from 爬虫.抖音.handle_db import save_task
except:
    from handle_db import save_task
#一定要写成response的形式，否则mitmdump不会运行
def response(flow):
    #下边这个链接要通过fiddler获取
    if "aweme/v1/user/follower/list" in flow.request.url:
        for user in json.loads(flow.response.text)['followers']:
            douyin_info={}
            douyin_info['share_id']=user['uid']
            douyin_info['douyin_id']=user['short_id']
            douyin_info['nick_name']=user['nickname']
            save_task(douyin_info)
