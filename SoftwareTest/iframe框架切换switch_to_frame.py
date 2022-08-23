#coding:utf-8
from selenium import webdriver
from time import *
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("https://mail.qq.com/")
'''使用框架切换只能使用两种属性进行切换，分别为id，name
格式： 网页对象名.switch_to_frame("id")
       网页对象名.switch_to_frame("name")
'''
bro.switch_to_frame('login_frame')
bro.find_element_by_id("u").send_keys("171129658")
sleep(1)
bro.find_element_by_id("p").send_keys("a123456")
sleep(1)
bro.find_element_by_id("login_button").click()
sleep(2)
bro.switch_to_default_content() #切出框架  格式：网页对象名.switch_to_default_content()
bro.find_element_by_link_text("基本版").click()
sleep(2)
bro.quit()