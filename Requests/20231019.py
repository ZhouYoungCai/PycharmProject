#coding:utf-8
import requests
#1.无参请求：
r  = requests.get('http://www.baidu.com')
#2.有参请求：
# 方式一：参数和路径分开
param = {'key1': 'value1', 'key2': 'value2', 'key3': None}
r = requests.get('http://www.baidu.com', params=param)
# 方式二：参数和路径拼接
r = requests.get('http://www.baidu.com?key1=value1&key2=value2&key3=None')
# 如果请求参数为字符串类型，可以通过eval()执行一个字符串表达式，并返回表达式的值
param = eval("{'key1':'value1','key2':'value2','key3':None}")
r = requests.get('http://www.baidu.com', params=param)
#四、post请求
param = {'key1':'value1','key2':'value2'}
r = requests.post("http://www.baidu.com", data=param)

