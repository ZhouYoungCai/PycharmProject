"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests

from api.feishu_api import FeishuApi
from utils.log_utils import logger

"""
业务接口的描述
"""


class CalenderApi(FeishuApi):
    def get_by_main(self):
        pass

    def get(self, calendar_id):
        url = f"/calendar/v4/calendars/{calendar_id}"
        r = self.send("get",url)
        return r



    def get_list(self):
        url = "/calendar/v4/calendars"
        r = self.send("get", url, headers={"Content-Type": "application/json; charset=utf-8"})
        return r

    def create(self, summary, description, permissions, color, summary_alias):
        url = "/calendar/v4/calendars"
        data = {
            "summary": summary,
            "description": description,
            "permissions": permissions,
            "color": color,
            "summary_alias": summary_alias}
        r = self.send("post", url, json=data)
        return r

    def delete(self):
        pass

    def search(self):
        pass
