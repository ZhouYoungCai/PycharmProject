#coding:utf-8
'''
input()  输入函数（会自动识别输入内容的能力，常用于number类型，不建议输入字符串类型）
假设输入的是整型，就会自动识别整型。输入的是小数，就会自动是小数
'''
# a = input("请输入一个值：") #a的值可以输入123 和 12.3 去理解
# print a,type(a)

#while循环：多次循环
# a = 1
# while a<10: #当while条件为真的时候，会执行while下面的循环体
#     a+=1
#     print a

#for循环：遍历循环
# a = [1,2,3,4,5]
# for i in a: #会把a依次赋值给i进行打印
#     print i
# b = "Hello"
# for y in b:
#     print y

#range()函数：范围函数，主要运用在Number
#range(x,y,step) x表示起始值  y表示边界值  step表示步长
# print range(20) #当传入一个参数的时候，它是y表示边界值，打印的值是不包括边界值的，打印类型是列表类型
# print range(1,20) #当传入两个参数的时候，它表示x，y。
# print range(1,20,2)# 当传入三个参数的时候，它表示x,y,step。
# print sum(range(2,101,2)) #打印1-100内的所有偶数和
# print range(1,101,2) #打印1-100内所有的奇数

#绝对值的简单写法
# num = input("请输入一个值:")
# if num<0:
#     print -num
# else:
#     print num
#用构建函数的方法写绝对值
# def my_abs(num): #构建函数时需要传入一个参数
#     if num<0:
#         print -num
#     else:
#         return num
# print my_abs(-9)
# print my_abs(28)

#构建类  关键字：class
# class buxi:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def xuexi(self):
#         print "我%s要去学习" %self.name
# buxi1 = buxi("chenchen",18)
# buxi1.xuexi()
# print buxi1.name
# print buxi1.age
# class xueba(buxi):
#     def kaigua(self):
#         print "开了挂，挂了科"
#     def xuexi(self):
#         print "我就不学习"
#
# class xuezha(buxi,xueba):
#     pass
# xuezha1 = xuezha("caoyunbiao",30)
# xuezha1.xuexi()
# xuezha1.kaigua()

#列表的加法和乘法
# a = [1,2,3,4,"Hi"]
# b = [5,6,7,8,"huangpeng"]
# print a+b
# print a[1]*b[3]
# print a[4]+' '+b[4]
# print (a[4]+' ')*b[0]

#关系运算符  返回布尔值
# print 1>2
# print 1<2

#逻辑运算符
# a = 1>2
# b = 1<2
# print a and b
# print a or b
# print not a

#倒序切片
# a = "yuancheng"
# print a[0:-2]
# print a[1:-2]

#if 分支结构
# a = 1
# if a<10: #当if条件为真的时候，就会打印if下面对应的语句，否则打印else下面对应的语句
#     print 10
# else:
#     print 0

#字典
# dict = {"city":"shenzen","tianqi":"qing","wendu":30}
# print dict
# print dict["city"]
# print sorted(dict)

#构建函数的方法：


