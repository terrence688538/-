from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import multiprocessing

#获取尺寸
def get_size(driver):
  x=driver.get_window_size()['width']
  y=driver.get_window_size()['height']
  return(x,y)

def handle_douyin(driver):
#定位搜索框
  while True:
    if WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.ss.android.ugc.aweme.lite:id/jz")):
      #driver.tab([(),()])  坐标在bonds里（Monitor里）
      driver.find_element_by_id("com.ss.android.ugc.aweme.lite:id/jz").click()
      driver.find_element_by_id("com.ss.android.ugc.aweme.lite:id/jz").send_keys("1812892006")
      while driver.find_element_by_id("com.ss.android.ugc.aweme.lite:id/jz").text != "1812892006":
        driver.find_element_by_id("com.ss.android.ugc.aweme.lite:id/jz").send_keys("抖音号: 1812892006")
        time.sleep(1.23)

    #搜索
    driver.find_element_by_id("com.ss.android.ugc.aweme.lite:id/k1").click()

    #查看是否有关注
    if WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.ss.android.ugc.aweme.lite:id/ap9")):
      driver.find_element_by_id("com.ss.android.ugc.aweme.lite:id/a5_").click()

    #点击粉丝
    if WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.ss.android.ugc.aweme.lite:id/uy")):
      driver.find_element_by_id("com.ss.android.ugc.aweme.lite:id/uy").click()

    time.sleep(1.223)
    l=get_size(driver)
    x1=int(l[0]*0.5)
    y1=int(l[1]*0.9)
    y2=int(l[1]*0.15)

    while True:
      if '没有更多了' in driver.page_source:
        break
      elif 'TA还没有粉丝' in driver.page_source:
        break
      else:
        driver.swipe(x1,y1,x1,y2)
        time.sleep(0.85)

    driver.find_element_by_id("com.ss.android.ugc.aweme.lite:id/hy").click()
    driver.find_element_by_id("com.ss.android.ugc.aweme.lite:id/hy").click()
    driver.find_element_by_id("com.ss.android.ugc.aweme.lite:id/jz").clear()


def handle_appium(device,port):
  cap = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": device,
    "udid": device,  # 两台设备以上需要udid这个参数            因为Appium其实是通过哦udid来识别设备的
    "appPackage": "com.ss.android.ugc.aweme.lite",
    "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
    "noReset": True,
    "unicodekeyboard": True,  # 可以输入中文
    "resetkeyboard": True,
  }

  driver = webdriver.Remote('http://localhost:'+str(port)+'/wd/hub', cap)

  # 点击搜索
  try:
    if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("com.ss.android.ugc.aweme.lite:id/yp")):
      driver.find_element_by_id("com.ss.android.ugc.aweme.lite:id/yp").click()
  except:
    pass

  handle_douyin(driver)

if __name__ == '__main__':
  m_list=[]
  #定义两台设备
  devices_list=['192.168.0.103:5555','192.168.0.105:5555']
  for device in range(len(devices_list)):
    port =4723+2*device
    m_list.append(multiprocessing.Process(target=handle_appium,args=(devices_list[device],port)))
  for m1 in m_list:
    m1.start()
  for m2 in m_list:
    m2.join()







