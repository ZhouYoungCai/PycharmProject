#coding:utf-8
from selenium import webdriver
from time import *
bro = webdriver.Firefox()
bro.get("file:///C:/Users/THINK/Desktop/html/lizi.html")
sleep(1)
bro.find_element_by_link_text("hetao").click()
sleep(1)
ah = bro.current_window_handle #获取当前页面句柄
print ah,type(ah)
allh = bro.window_handles #获取所有页面窗口句柄
for bh in allh:
    if bh!=ah: #若页面句柄不等于第一个句柄，即相当于此时的bh已为新窗口句柄
        bro.switch_to_window(bh) #切换页面句柄时使用格式 ：对象名.switch_to_window(句柄名)
bro.find_element_by_name("bt").click()
sleep(1)
bro.quit()