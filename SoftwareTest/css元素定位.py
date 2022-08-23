#coding:utf-8
from selenium import webdriver
from time import *
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("https://www.baidu.com/")
# bro.find_element_by_css_selector("#kw").send_keys("123") #通过属性id定位，id用#代替
# bro.find_element_by_css_selector(".s_ipt").send_keys("123") #通过属性class定位，name用点号（.）代替
# bro.find_element_by_css_selector("[name=wd]").send_keys("123") #通过属性name定位，需要加上中括号

# bro.find_element_by_css_selector("input[autocomplete='off']").send_keys("123")#通过标签+属性来定位
bro.find_element_by_css_selector("div#u1>a.mnav").click() #通过组合（父子）标签来定位点击新闻
