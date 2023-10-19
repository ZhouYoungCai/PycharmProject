#coding:utf-8
from selenium import webdriver
from selenium.webdriver.by import By

driver = webdriver.chrome()
driver.get("https://www.baidu.com/")
def please1wait(self):
	self.driver.find_element(By.xpath,'//*[id="kw"]').sendkeys("霍格沃兹测试学院")
