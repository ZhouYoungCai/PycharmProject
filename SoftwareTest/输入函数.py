#coding:utf-8
'''
1.input()函数
格式： 变量名 = input('请输入文字说明')
input()函数会自动识别输入内容的能力，常用于Number（数字）类型，若要进行字符串输入不建议使用
'''
'''
age = input("请输入你的年龄：")
print "你的年龄是%d岁" %age
print type(age)
name = input("请输入你的名字：")  #键盘输入字符串时，需要加上引号
print "你的名字是%s" %name
print type(name)
print "==================分割线==================="
'''
'''
2. raw_input()函数输入
格式： raw_input('请输入文字说明')
raw_input函数不论输入的内容为数字还是字符串都将被视为字符串类型
'''
# name1 = raw_input("请输入你的名字:")
# print "你的名字是：%s" %name1
# print type(name1)


# input() 和 raw_input()函数的区别
a = input("请输入一个表达式：") #表达式输入2+2
print a,type(a)
b = raw_input("请输入一个表达式：") #表达式输入2+2
print b,type(b)

