#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #导入显示等待时间的包
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("https://www.baidu.com")
'''
使用显示等待时间之前必须先调用WebDriverWait模块
使用语法：
WebDriverWiat(x,y,z).until(lambda x:x.find_element_by_元素属性)
x:网页窗口对象（bro）  y:等待时间（s）   z:在等待过程中，每隔多久查看一次元素 单位（s）
lambda x:x 可以理解为网页窗口对象，固定格式
'''
a = WebDriverWait(bro,10,2).until(lambda x:x.find_element_by_id("kk"))
a.send_keys("123")
#总结：只针对一个元素进行时间的等待，要是找不到该元素则会一直消耗完所有的等待时间才进行下一步