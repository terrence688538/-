import pymongo
from pymongo.collection import Collection

#链接mongodb
client=pymongo.MongoClient(host='127.0.0.1',port=27017)
#加入一个叫抖音的数据库
db=client['douyin']

def handle_int_task():
    task_id_collection=Collection(db,'task_id')                #加入一个表叫task_id
    with open(r'D:\test\爬虫\抖音\抖音id.txt','r') as f_share:
        for f_share_task in f_share.readlines():          #变成列表然后用for循环遍历
            init_task={}
            init_task['share_id']=f_share_task.replace('\n','')
            task_id_collection.insert(init_task)

def save_task(task):
    task_id_collection = Collection(db, 'task_id')
    task_id_collection.update({'share_id':task['share_id']},task,True)


#返回表里的一个数据
def handle_get_task():
    task_id_collection=Collection(db,'task_id')
    return task_id_collection.find_one_and_delete({})


#handle_int_task()
print(handle_get_task())