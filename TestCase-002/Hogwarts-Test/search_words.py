#coding:utf-8
from selenium import webdriver
from time import *

def test_search():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https:www.baidu.com/")
    sleep(2)
    driver.find_element_by_css_selector("#kw").send_keys("霍格沃兹测试学院")
    sleep(2)
    driver.find_element_by_css_selector("#su").click
    sleep(2)
    result = find_element_by_css_selector(".result:nth-child(2)>h3>a>em").text
    sleep(2)
    assert "霍格沃兹测试学院" in result
