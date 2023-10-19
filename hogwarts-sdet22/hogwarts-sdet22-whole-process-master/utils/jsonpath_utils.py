"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from typing import List

import jsonpath


class JsonpathUtils:

    @classmethod
    def get_field_by_jsonpath(cls, obj, expr) -> List:
        r = jsonpath.jsonpath(obj, expr)
        return r
