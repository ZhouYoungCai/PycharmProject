#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #导入键盘事件的包。注意k的大小写
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("https://www.baidu.com")
time.sleep(1)
bro.find_element_by_id("kw").send_keys("seleniumm")
time.sleep(1)
#模拟删除按钮 BACK_SPACE  格式：元素.send_keys(Keys.键盘操作)
bro.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
#SPACE 模拟空格按钮
time.sleep(1)
bro.find_element_by_id("kw").send_keys(Keys.SPACE)
time.sleep(1)
bro.find_element_by_id("kw").send_keys(u"教程")
time.sleep(1)
#CONTROL,'a'表示全选
bro.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
#CONTROL,'x'表示剪切
time.sleep(1)
bro.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')#剪切
time.sleep(1)
bro.find_element_by_id("kw").send_keys(Keys.CONTROL,'v') #粘贴    c表示复制
time.sleep(1)
bro.find_element_by_id("kw").send_keys(Keys.ENTER)
time.sleep(3)
bro.quit()