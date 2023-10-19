"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium.webdriver.common.by import By

from web.page_object.base_page import BasePage
from web.page_object.calender_page import CalenderPage


class FeishuPage(BasePage):
    _BASE_URL = "https://www.feishu.cn/"

    def goto_calender(self):
        # time.sleep(30)
        self.find(By.CSS_SELECTOR, "[data-elem-id='RgUrMDgfe8']").click()
        self.find(By.CSS_SELECTOR, ".headerExtra_productList").click()
        self.find(By.CSS_SELECTOR, "[title='日历']").click()
        # self.goto_address("ddd")
        self.switch_to_new_window()
        return CalenderPage(self.driver)

    def goto_calender_by_url(self):
        # self.goto_address(url)
        pass

    def goto_cloud_file(self):
        pass