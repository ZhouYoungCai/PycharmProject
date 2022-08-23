#coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains #调用鼠标事件所在的包
'''
右击  context_click()
左击  click_and_hold()
双击  double_click()
拖动  drag_and_drop()
悬停  move_to_element()
使用perform()提交生效操作
使用语法：ActionChains(网页窗口对象).事件(元素对象).perform()
'''
bro = webdriver.Firefox()
bro.maximize_window()
bro.get("https://baidu.com")
a = bro.find_element_by_id("kw")
# ActionChains(bro).context_click(a).perform()
b = bro.find_element_by_xpath(".//*[@id='u1']/a[2]")
sleep(1)
# ActionChains(bro).click_and_hold(b).perform()
#拖动与上述语法略有不同 格式：ActionChains(网页窗口对象).事件(元素对象1,元素对象2).perform()
# ActionChains(bro).drag_and_drop(b,a).perform()
c = bro.find_element_by_xpath(".//*[@id='u1']/a[8]")
ActionChains(bro).move_to_element(c).perform()