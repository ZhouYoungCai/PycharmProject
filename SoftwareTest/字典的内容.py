#coding:utf-8
'''
字典（dict）:一个字典由多个键构成，每个键又由键名和键值构成（使用：分隔）
键与键之间使用,隔开
'''
#1.字典在生成后会进行默认的键重排序（只要有新的值产生后都会重新排序）
dict = {"name":"Jack",'age':27,"sex":"male","kg":90}
print dict
#2.字典中若出现相同键名，则后者键会替换前者，只保留一个键，所以键名是唯一的。
dict1 = {"name":"Jack","name":'Tom','age':27,"sex":"male","kg":90}
print dict1

#3.字典切片不能使用下标索引，根据键名获取对应键值
#格式 变量名[键名]
print dict["name"]

#4.修改字典内的数据，根据键名修改对应键值
#格式：变量名[键名]=新键值
dict['age']=29
print dict

#5.排序使用sorted()函数，结果是对键名排序，排序后返回列表形式
dict3 = {"name":"Jackson",'age':23,"sex":"female","kg":80}
dict4 = sorted(dict3) #排序后的字典
print dict4,type(dict4)

#6.删除键（根据键名删除整个键）
# 格式：del 变量名[键名]
dict5 = {"name":"Jackson",'age':23,"sex":"female","kg":80}
del dict5["name"]
print dict5

#7.添加键
# 格式：变量名[新键名]=新键值
dict5["height"]=172.2
print dict5