#coding:utf-8
'''
模块在python中被视为自定义函数或是运算法则等内容，可被其他文件调用的.py文件
调用的方式有两种：
1.import 模块/包名
2.from 模块/包名 import 模块名/*（代表所有模块）
注：被调用的.py文件，调用后项目会生成一个同名.pyc后缀的文件
'''
import iPhone #当只调用模块名时，需要使用模块名下面的函数，使用格式：模块名.函数名()
iPhone.huawei()
iPhone.xiaomi()

from iPhone import huawei #当只调用模块名下一个方法时，那只能使用这个方法下的对应语句
huawei()

from iPhone import * #当调用了模块下所有的方法时，可以直接使用所有的方法
xiaomi()
huawei()
