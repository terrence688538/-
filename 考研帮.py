from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
cap={
  "platformName": "Android",
  "platformVersion": "5.1.1",                 #模拟机下看设置
  "deviceName": "192.168.43.182:5555",       #cmd下输入命令adb devices
  "appPackage": "com.tal.kaoyan",        #cmd下进入cd C:\SDK\build-tools\29.0.2  输入aapt.exe dump badging +apk包的名字  获取package name
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",  #一般情况下可以通过上面的方法获取      如果没有  先输入adb shell在输入logcat | grep cmp= 回车 然后打开所要爬取的app
  "noReset": True
}
time.sleep(2)
driver=webdriver.Remote("http://localhost:4723/wd/hub",cap)
def get_size():
  x=driver.get_window_size()['width']
  y=driver.get_window_size()['height']
  return (x,y)


driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tip_commit']").click()
try:
  if WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']")):
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']").click()
except:
  pass
if WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/kylogin_phone_input_phonenum']")):
  driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/login_code_touname']").click()
if WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")):
  driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']").send_keys("18050064062")
  driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_password_edittext']").send_keys("jzy688538")
  driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/login_login_btn']").click()

try:
  if WebDriverWait(driver, 5).until(
          lambda x: x.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/view_wemedia_cacel']")):
    driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/view_wemedia_cacel']").click()
except:
  pass

try:
  if WebDriverWait(driver,5).until(
    lambda x:x.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/kaoyan_home_schtip_close']")):
    driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/kaoyan_home_schtip_close']").click()
except:
  pass

if WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath("//android.view.View[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")):
  driver.find_element_by_xpath("//android.view.View[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()


  l=get_size()
  x1=int(l[0]*0.5)
  y1=int(l[1]*0.75)
  y2=int(l[1]*0.25)
  while True:
    driver.swipe(x1,y1,x1,y2)               #鼠标滑动，从x1,y1到x1,y2
    time.sleep(0.8)







