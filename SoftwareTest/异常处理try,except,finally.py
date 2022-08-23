#coding:utf-8
from selenium import webdriver
from time import sleep
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("https://www.baidu.com")
'''格式：
try:
    语句1     正确      错误      错误      正确
    语句2     错误      正确      错误      正确
except: #捕捉try有错误，则会运行
    语句3     运行      运行      运行      不运行
finally：
    语句4     运行      运行      运行      运行
'''
try:
    bro.find_element_by_id("kw").send_keys("123")
    bro.find_element_by_id("s").click()
except:
    bro.get_screenshot_as_file("d:\\baidu_error.png") #保存截图到D盘，格式：对象名.get_screenshot_as_file("路径")
finally:
    print "==========over========="