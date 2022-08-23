#coding:utf-8
from selenium import webdriver
from time import *
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("file:///C:/Users/THINK/Desktop/html/lizi.html")
# bro.find_element_by_id("5").send_keys("chen")
sleep(1)
#二次定位使用tag_name，若不能直接定位元素时，则需要先定位上一级元素标签，然后再进行定位
# bro.find_element_by_tag_name('select').find_element_by_id("3").click()
#注意后面标签是一个元素组需要用elements
a = bro.find_element_by_tag_name('select').find_elements_by_tag_name("option")
for i in a: #循环点击，每循环一次就对a进行操作
    i.click()
    sleep(1)