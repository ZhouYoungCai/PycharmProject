#coding:utf-8

from selenium import webdriver  # 导入webdriver包
from time import *
driver = webdriver.Ie()  # 初始化一个火狐浏览器实例：driver
driver.maximize_window()  # 最大化浏览器
sleep(5)  # 暂停5秒
driver.get("https://www.baidu.com")  # 通过get()方法，打开一个url站点
sleep(5)  # 暂停5秒钟
driver.quit()
