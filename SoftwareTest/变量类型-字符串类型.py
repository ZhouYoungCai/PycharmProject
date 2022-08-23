#coding:utf-8
'''
字符串（string）：当我们的值不是纯数字的时，必须使用字符串定义，字符串可以定义内容包括
数字、汉字、符号、字母等。
'''
#定义方式： ①变量名='xxxx'  ②变量名="xxxx"   ③变量名='''xxxx'''
g = '中文'
print g,type(g)
h = "English"
print h,type(h)
j = '''@'''
print j,type(j)
k = "123"
print k,type(k)
i = "I'm jack"
k = 'I\'m jack' # 用单引号定义时，要是里面内容有单引号，必须使用 \ （转移符）
print i