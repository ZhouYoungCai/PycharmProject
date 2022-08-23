#coding:utf-8
from selenium import webdriver
from time import sleep
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("https://www.baidu.com")
bro.implicitly_wait(10)
bro.find_element_by_id("kw").send_keys("123")
bro.find_element_by_id("s").click()
'''
语法格式：网页对象.implicitly_wait(s)
若10s等待时间内找到了该元素，就不再等待直接获取元素对象。 它是全局的等待时间
'''