#coding=utf-8
from appium import webdriver #导入appium包
import time
desired_caps = {} #定义一个空字典
desired_caps['platformName'] = 'Android' #平台，安卓，一般不用修改
desired_caps['platformVersion'] = '4.4.2' #版本号，不需要精确匹配
desired_caps['deviceName'] = 'Android Emulator' #设备名字，可修改，也可以不改
desired_caps['appPackage'] = 'cn.itools.avdmarket'#需要改，每个APP有对应自己的app包名
desired_caps['appActivity'] = '.ui.activity.HostActivity'#需要改，每个APP对应有直接的活动名
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#构建手机页面对象app
time.sleep(10)
# 格式：对象名.swipe(x1,y1,x2,y2,time)
#  x1,y1表示起始位置    x2,y2表示终止位置   time为延迟时间 ms
driver.swipe(166,890,455,193,5000)
time.sleep(10)
driver.quit()