#coding:utf-8
from selenium import webdriver
from time import *
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("file:///C:/Users/THINK/Desktop/html/lizi.html")
sleep(2)
#相对路径的写法： 格式: .//表示某层级下 option标签 [@属性名='属性值']
# bro.find_element_by_xpath(".//option[@id='4']").click()
bro.find_element_by_xpath(".//*[@id='3']").click() #*代表某一个标签
