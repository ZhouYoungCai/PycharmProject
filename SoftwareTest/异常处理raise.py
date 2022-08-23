#coding:utf-8
from selenium import webdriver
from time import sleep
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("https://www.baidu.com")
a = bro.title
if a==u"百度一下，你就知":
    print "title ok"
else:
    raise NameError("标题错了") #raise异常处理，报错以后会终止后续代码的运行
bro.find_element_by_id("kw").send_keys("123")
