"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from api.calendar.calender import CalenderApi
from utils.jsonpath_utils import JsonpathUtils


class TestCalender:

    def setup_class(self):
        self.calender_api = CalenderApi()

    # def test_get_by_main(self):
    #     self.calender_api.get_by_main()
    #     assert False

    # def test_get(self):
    #     self.calender_api.get()
    #     assert False

    def test_get_list(self):
        assert self.calender_api.get_list()

    def test_create(self):
        # 1. 创建一个接口，
        r = self.calender_api.create("ck22期01", "ck22期01", "private", -1, "ck22期01")
        calendar_id = JsonpathUtils.get_field_by_jsonpath(r, "$..calendar_id")[0]
        # 2. 获取对应的接口信息，断言获取到的接口信息是否正确
        r = self.calender_api.get(calendar_id)
        calender_summary = JsonpathUtils.get_field_by_jsonpath(r, "$..summary")[0]
        assert calender_summary == "ck22期01"

    def test_delete(self):
        assert True

    def test_search(self):
        assert True
