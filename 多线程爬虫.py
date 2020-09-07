#先来一个单线程
import requests
import time
link_list = []
with open(r'C:\Users\Mechrevo\Desktop\alexa.txt', 'r') as file:
    file_list = file.readlines()              #读取文本所有内容，并且以数列的格式返回结果，一般配合for in使用
    for eachone in file_list:
        link = eachone.split('\t')[1]
        link = link.replace('\n','')
        link_list.append(link)

start = time.time()
for eachone in link_list:
    try:
        r = requests.get(eachone)
        print (r.status_code, eachone)
    except Exception as e:
        print('Error: ', e)
end = time.time()
print ('串行的总时间为：', end-start)


#多线程
import _thread
import time

# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(threadName, time.ctime())

_thread.start_new_thread(print_time, ("Thread-1", 1))
_thread.start_new_thread(print_time, ("Thread-2", 2))
print("Main Finished")

#案例
import threading
import time

class myThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.delay)
        print("Exiting " + self.name)


def print_time(threadName, delay):
    counter = 0
    while counter < 3:
        time.sleep(delay)
        print(threadName, time.ctime())
        counter += 1

threads = []

# 创建新线程
thread1 = myThread("Thread-1", 1)
thread2 = myThread("Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()

print("Exiting Main Thread")






#守护线程
import _thread
import threading
import time

def doSth(arg):
    # 拿到当前线程的名称和线程号id
    threadName = threading.current_thread().getName()
    tid = threading.current_thread().ident
    for i in range(5):
        print("%s *%d @%s,tid=%d" % (arg, i, threadName, tid))
        time.sleep(2)

def simpleThread():
    # 创建子线程，执行doSth
    # 用这种方式创建的线程为【守护线程】
    #主线程死去“护卫”也随“主公”而去
    _thread.start_new_thread(doSth,("开启了子线程",))
    mainThreadName = threading.current_thread().getName()
    print(threading.current_thread())
    for i in range(5):
        print("我是主线程@%s" % (mainThreadName))
        time.sleep(1)

        # 阻塞主线程，以使【守护线程】能够执行完毕
    while True:
        pass

if __name__ == '__main__':
    simpleThread()















