"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from web.page_object.base_page import BasePage


class NewCalenderPage(BasePage):

    def create_calender(self, calender_name):
        from web.page_object.calender_page import CalenderPage
        self.find(By.CSS_SELECTOR, ".calendar-title input").send_keys(calender_name)
        self.find(By.CSS_SELECTOR, ".confirm-wrapper button").click()
        return CalenderPage(self.driver)