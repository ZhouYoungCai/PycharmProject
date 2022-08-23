#coding:utf-8
from selenium import webdriver
from time import *
bro=webdriver.Firefox()
bro.maximize_window()
bro.get('https://www.bilibili.com/')
bro.find_element_by_class_name("search-keyword").send_keys("selenium")
sleep(2)
ah = bro.current_window_handle #获取当前页面句柄
bro.find_element_by_class_name("search-keyword").submit()
sleep(2)
allh = bro.window_handles #获取所有的页面句柄
for bh in allh:
    if ah!=bh:
        bro.switch_to_window(bh)
bro.find_element_by_xpath(".//*[@id='server-search-app']/div[2]/div[2]/div/div[2]/ul[4]/li[1]/a/div/div[1]/img").click()
sleep(2)
all1h = bro.window_handles
for ch in all1h:
    if ch!=ah and ch!=bh:
        bro.switch_to_window(ch)
bro.find_element_by_xpath(".//*[@id='bilibiliPlayer']/div[1]/div[2]/div[7]/video").click()
sleep(2)
bro.quit()