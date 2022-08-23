#coding:utf-8
from selenium import webdriver #导入selenium的包
from time import *
bro = webdriver.Firefox() #构建网页窗口对象
bro.maximize_window() #最大化窗口  格式：对象名.maximize_window()
sleep(1) #休眠1s
# bro.set_window_size(400,500) #手动设置窗口大小  格式：对象名.set_window_size(宽,高)
bro.get("https://www.baidu.com") #打开指定网址  格式: 对象名.get("url")
sleep(1)
bro.get("https://www.taobao.com/")
bro.back() #模拟浏览器后退功能  #格式：对象名.back()
sleep(1)
bro.forward() #模拟浏览器前进的功能  #格式：对象名.forward()
print bro.title #打印网页的title
sleep(1)
if bro.title==u"淘宝网 - 淘！我喜欢111123": #判断title与预期结果是否一致
    print True
else:
    print False
sleep(2)
bro.quit() #关闭浏览器  格式：对象名.quit()