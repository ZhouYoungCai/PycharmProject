#coding:utf-8
from selenium import webdriver
from time import *
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("https://www.baidu.com/")
#xpath是第一个万能定位方式，在没有其他属性可以使用时就可以使用xpath来定位元素
#不同浏览器xpath的值可能不一样
#绝对路径：从起始html标签至该元素所在位置
# bro.find_element_by_xpath("html/body/div[1]/div[1]/div/div[3]/a[2]").click()

bro.find_element_by_xpath("html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input").send_keys(u"xpath绝对路径的写法")