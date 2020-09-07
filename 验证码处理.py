"""""""""
图形验证码
"""
#一般方法
import tesserocr
from PIL import Image
image=Image.open(r'C:\Users\Mechrevo\Desktop\code.jpg')
result=tesserocr.image_to_text(image)
print(result)

#灰度化
from PIL import Image           #将图片灰度化
im = Image.open('C:\\Users\\Mechrevo\\Desktop\\code.jpg')
#灰度化：
gray = im.convert('L')  #对于彩色图像，不管其图像格式是PNG，还是BMP，或者JPG，在PIL中，使用Image模块的open()函数打开后，返回的图像对象的模式都是“RGB”。而对于灰度图像，不管其图像格式是PNG，还是BMP，或者JPG，打开后，其模式为“L”。
gray.show()
gray.save("C:\\Users\\Mechrevo\\Desktop\\code_gray.jpg")

threshold = 150         #二值化，采用阈值分割法，threshold为分割点
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = gray.point(table, '1')
image.show()
image.save("C:\\Users\\Mechrevo\\Desktop\\code_thresholded.jpg")
#灰度是表明图像明暗的数值，即黑白图像中点的颜色深度，范围一般从0到255，白色为255 ，黑色为0，故黑白图片也称灰度图像。灰度值指的是单个像素点的亮度。灰度值越大表示越亮。
#方法一：
import pytesseract
th = Image.open('C:\\Users\\Mechrevo\\Desktop\\code_thresholded.jpg')
print(pytesseract.image_to_string(th))
#方法二·：
result=tesserocr.image_to_text(image)

"""""""""""
滑动验证码
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from io import BytesIO
from PIL import Image

EMAIL = 'cqc@cuiqingcai.com'
PASSWORD = '66666'
BORDER = 6
INIT_LEFT = 60

#初始化
class CrackGeetest():
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD

    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return:
        """
        button=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return button

    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img=self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
        time.sleep(2)
        location=img.location
        #location属性可以返回该图片对象(既这张图片)在浏览器中的位置，以字典的形式返回      如：{‘x’:30,‘y’:30}           坐标轴是以屏幕左上角为原点，x轴向右递增，y轴像下递增
        size=img.size
        #图片对象的高度，宽度{‘height’:30,‘width’:30}
        top,bottom,left,right=location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        return (top,bottom,left,right)

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))           #BytesIO实现了在内存中读写bytes
        return screenshot

    def get_geetest_image(self,name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top,bottom,left,right=self.get_position()
        print('验证码位置',top,bottom,left,right)
        screenshot=self.get_screenshot()                    #get_screenshot() 获取截图
        captcha=screenshot.crop((left,top,right,bottom))          #crop方法将图片裁剪         crop((x0,y0,x1,y1))方法可以对图片做裁切。左上和右下
        captcha.save(name)
        return captcha

    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#base > div.content-outter > div > div.inner-conntent > div:nth-child(3) > div > form > div:nth-child(1) > div > div.ivu-input-wrapper.ivu-input-type.ivu-input-group.ivu-input-group-with-prepend > input')))
        password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#base > div.content-outter > div > div.inner-conntent > div:nth-child(3) > div > form > div:nth-child(2) > div > div.ivu-input-wrapper.ivu-input-type.ivu-input-group.ivu-input-group-with-prepend > input')))
        email.send_keys(self.email)
        password.send_keys(self.password)




#九宫格
import os
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import listdir

USERNAME = '15874295385'
PASSWORD = 'fpdpvx119'


class CrackWeiboSlide():
    def __init__(self):
        self.url = 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https://m.weibo.cn/'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.username = USERNAME
        self.password = PASSWORD

    def __del__(self):
        self.browser.close()

    def open(self):
        """
        打开网页输入用户名密码并点击
        :return: None
        """
        self.browser.get(self.url)
        username = self.wait.until(EC.presence_of_element_located((By.ID, 'loginName')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'loginPassword')))
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginAction')))
        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()




























