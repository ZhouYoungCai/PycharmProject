#coding:utf-8
'''
元素定位方式一共有8种：
id  name   class_name   link_text   partial_link_text   tag_name    xpath   css
'''
from selenium import webdriver #导入selenium的包
from time import *
bro = webdriver.Firefox() #构建网页窗口对象 格式：对象名 = webdriver.浏览器名()
bro.maximize_window() #最大化窗口  格式：对象名.maximize_window()
bro.get("https://www.baidu.com")
sleep(1)
#send_keys表示模拟输入
# bro.find_element_by_id("kw").send_keys("123") #定位元素使用格式 对象名.find_element_by_元素定位方法("对应元素属性")
# bro.find_element_by_name("wd").send_keys(u"元素定位方式")
bro.find_element_by_class_name("s_ipt").send_keys(u"class_name不能定位有空格的属性值")
sleep(1)
#清空输入框： clear()
bro.find_element_by_id("kw").clear()
sleep(1)
#click()表示对元素模拟点击操作
# bro.find_element_by_id("su").click()
bro.find_element_by_id("kw").submit() #提交输入框里的值
sleep(1)
bro.quit()
