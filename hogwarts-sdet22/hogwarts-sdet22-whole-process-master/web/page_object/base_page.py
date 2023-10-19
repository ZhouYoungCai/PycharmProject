"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from utils.file_tools import FileTool
from utils.log_utils import logger


class BasePage:
    _BASE_URL = ""

    def __init__(self, base_driver: WebDriver = None):
        # 如果
        # 实例化子类的过程中，没有传递driver的话，那么就会初始化一个driver，同步会打开一个浏览器
        #
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)

        else:
            self.driver = base_driver
        if self._BASE_URL:
            self.driver.get(self._BASE_URL)
            self.__login_by_cookie()


    def __login_by_cookie(self):
        cookies = FileTool.read_yaml("cookie")
        # logger.debug(f"从文件读取的cookie信息为{cookies}")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()


    def find(self, by, locator=None):
        if locator:
            logger.debug(f"定位的元素为{by}-{locator}")
            return self.driver.find_element(by=by, value=locator)
        else:
            logger.debug(f"定位的元素为{by}")
            return self.driver.find_element(*by)

    def switch_to_new_window(self):
        logger.debug("切换窗口")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def quit(self):
        logger.debug("退出浏览器")
        self.driver.quit()

    def goto_address(self, url):
        """
        跳转到某个页面
        :param url:
        :return:
        """
        self.driver.get(url)
