#coding:utf-8
'''
循环结构（2种）1.while循环  2.for循环
'''
'''
1.while循环：多次循环，当条件为真（True）是，则会运行循环体语句，直到条件为假（False）时跳出循环
格式：
while 条件语句：
    循环体语句
'''
'''
a=1
while a<10:
    #a+=1 #同a=a+1 为了防止死循环
    print a
    a+=1
    '''
'''
for循环：遍历循环
作用：将一个有序数组中所有数据按顺序依次进行输出的过程（包括不仅限于字符串，列表，元组，字典等）
格式:
for 变量名1 in 变量名2:
for循环相当于依次把变量名2有序数组中的数据赋值给变量名1
'''
# ①遍历字符串
# a = "python"
# for str in a:
#     print str
# ②遍历列表
# list = [1,2,3,'1994',[2,3]]
# for l in list:
#     print l
#③遍历元组 略
#④遍历字典
dict = {"name":"tom","age":18,"sex":"男"}
for d in dict: #遍历字典时，默认是遍历键名，不会输出键值
    print d,dict[d] #dict[d]是输出键值的方法



