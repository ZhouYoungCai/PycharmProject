UI级的界面自动化测试要满足以下条件：

1.项目周期足够长
2.反复执行的功能
3.项目允许
4.需求稳定
#coding:utf-8
from selenium import webdriver
from time import *
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("https://www.baidu.com/")
# bro.find_element_by_link_text("新闻").click() #link_text是对超链接的载体进行精确匹配定位元素
sleep(1)
bro.find_element_by_partial_link_text("闻").click() #partial_link_text是对超链接的载体进行模糊匹配定位元素
