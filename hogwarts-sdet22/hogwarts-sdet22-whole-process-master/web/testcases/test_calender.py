"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from web.page_object.feishu_page import FeishuPage


class TestCalender:
    def setup_class(self):
        self.feishu = FeishuPage()

    def teardown_class(self):
        self.feishu.quit()

    def test_create_calender(self):
        calener_page = self.feishu.\
            goto_calender().\
            goto_new_calender_page().\
            create_calender("ad日历")
        # 获取日历信息进行断言
        calender_name_res = calener_page.get_calender_by_name("ad日历")
        # 清理创建日历产生的脏数据信息
        calener_page.delete_calender("ad日历")
        assert calender_name_res == "ad日历"
