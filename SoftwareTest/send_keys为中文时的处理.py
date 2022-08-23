#coding=utf-8
from appium import webdriver #导入appium包
import time
desired_caps = {} #定义一个空字典
desired_caps['platformName'] = 'Android' #平台，安卓，一般不用修改
desired_caps['platformVersion'] = '4.4.2' #版本号，不需要精确匹配
desired_caps['deviceName'] = 'Android Emulator' #设备名字，可修改，也可以不改
desired_caps['appPackage'] = 'cn.itools.avdmarket'#需要改，每个APP有对应自己的app包名
desired_caps['appActivity'] = '.ui.activity.HostActivity'
desired_caps['unicodeKeyboard'] = True #使用unicodeKeyboard的编码方式来发送字符串
desired_caps['resetKeyboard'] = True#将键盘给隐藏起来
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)
driver.find_element_by_name(u"请输入关键字").send_keys(u"王者荣耀")
time.sleep(10)
driver.quit()