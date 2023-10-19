"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from web.page_object.base_page import BasePage
from web.page_object.new_calender_page import NewCalenderPage


class CalenderPage(BasePage):
    def switch_date_mode(self):
        pass
    # 面试问题： UI自动化测试过程中， 如果出现报错 no such element（找不到元素），应该如何解决
    # 1. 查看是否设置了隐式等待或强制等待，保证页面是加载出来的状态
    # 2. 查看是否有iframe 或者 window ，可以去进行切换
    # 3. 在console 使用 js 是否可以正常定位且点击
    # 4. 如果以上都没实现，则需要检查定位是否写错
    def goto_new_calender_page(self):

        self.find(By.CSS_SELECTOR, ".sidebar-more-trigger").click()
        self.find(By.CSS_SELECTOR, ".sidebar-more-popup-item").click()
        # time.sleep(10)
        return NewCalenderPage(self.driver)

    def get_calender_by_name(self, calender_name):
        try:
        # 通过文本查找元素是否存在，如果存在，那么就获取text，如果不存在会报错
            ele = self.find(By.XPATH, f"//*[text()='{calender_name}']")
            return ele.text
        # 解决报错问题： 添加异常捕获
        except:
            return False

    def delete_calender(self, calender_name):
        ele = self.find(By.XPATH, f"//*[text()='{calender_name}']")
        ActionChains(self.driver).move_to_element(ele).perform()
        # 通过文本查找日历，然后查找日历的爷爷元素。通过爷爷元素定位类名中包含unfollow的元素，也就是叉号。
        # 主要考验通过子元素定位父元素的技巧
        # ..代表选取当前节点的父节点
        self.find(By.XPATH, f"//*[text()='{calender_name}']/../..//*[contains(@class, 'unfollow')]").click()
        self.find(By.CSS_SELECTOR, ".uni-btn-theme-primary").click()
        # 返回当前实例本身，因为删除之后依然停留在日历页面
        return self