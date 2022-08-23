#coding=utf-8
from appium import webdriver #导入appium包
import time
desired_caps = {} #定义一个空字典
desired_caps['platformName'] = 'Android' #平台，安卓，一般不用修改
desired_caps['platformVersion'] = '4.4.2' #版本号，不需要精确匹配
desired_caps['deviceName'] = 'Android Emulator' #设备名字，可修改，也可以不改
desired_caps['appPackage'] = 'com.ibox.calculators'#需要改，每个APP有对应自己的app包名
desired_caps['appActivity'] = '.SplashActivity'#需要改，每个APP对应有直接的活动名
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#构建手机页面对象app
driver.find_element_by_name("8").click()
time.sleep(1)
driver.find_element_by_name("+").click()
time.sleep(1)
driver.find_element_by_name("7").click()
time.sleep(1)
driver.find_element_by_name("=").click()
time.sleep(10)
driver.quit()