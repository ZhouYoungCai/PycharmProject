"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 针对于现有用例做底层封装（日志、格式、其他工具），和具体的业务逻辑无关
from typing import List

import jsonpath
import requests

from utils.file_tools import FileTool
from utils.log_utils import logger


class FeishuApi:
    # 优化点： 1. headers 的token 重复
    # 2. 日志信息重复(封装父类的send方法，子类统一调用)
    def __init__(self):
        # 如何切换环境
        env_config = FileTool.read_yaml("env")
        default_env = env_config["default"]
        self.base_url = env_config[default_env]

    def __set_token(self, requests_info):
        """
        :param requests_info: 接口请求的其他信息 kwargs
        :return: 接口请求的其他信息 kwargs + 塞入的token信息
        """
        # 避免重复获取token
        if not hasattr(self, "token"):
            body_data = {"app_id": "cli_a16851154ab8100d", "app_secret": "gKcy0rkIVl7gV4AY5itwRrcNkVzlURp6"}
            url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
            r = requests.post(url, json=body_data)
            self.token = r.json()["tenant_access_token"]

        if requests_info.get("headers"):
            requests_info["headers"].update({"Authorization": f"Bearer {self.token}"})
        else:
            requests_info["headers"] = {"Authorization": f"Bearer {self.token}"}
        return requests_info

    def send(self, method, url, **kwargs):
        """
        针对requests 做二次封装。 日志信息、响应格式规范
        :return:
        """
        # 在发起请求之前，将token信息塞入到头信息=> 1.头信息在哪里？ 2. 怎么塞
        kwargs = self.__set_token(kwargs)
        r = requests.request(method, self.base_url + url, **kwargs)
        logger.debug(f"响应值信息为{r.json()}")
        return r.json()

