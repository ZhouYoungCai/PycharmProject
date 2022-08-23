#coding:utf-8
'''
python打印必须使用print 打印结果（函数运行结果）
'''
#1.打印纯数字
print 123
#2.打印字符串
print 'jack',;print "tom",;print '''jan'''
#3.打印变量名  print 变量名
a = 1
print a
#4.打印多个内容，格式： print 变量名1,内容1,type(变量名)
print a,123,"chen",type(a)
#5.为打印添加说明
age = 18
print "my age is",age
#6.打印格式字符（格式化输出）
# ①打印整型（%d） decimal 十进制的整数
age = 19
print "my age is %d" %age #注：当变量名为整型的时候，可以使用%d来代替变量，%age是代入变量
#② 打印字符串（%s） string
name = "张三"
print "我的名字是：%s" %name

#同时打印整型和字符串时使用 %（变量名1，变量名2）
print "my age is %d,my name is %s." %(age,name)

#③打印浮点型（%f）
shengao = 172.345
print "my shengao is :%f" %shengao #浮点型打印时默认保留6位小数
print "my shengao is :%2.2f" %shengao
print "my shengao is :%8.2f" %shengao

#第二和第三条格式： %n.nf(第一个n代表打印宽度，总数=整数+小数点+小数位数；第二个n代表小数后保留位数)
#补充： 当第二个n生效保留完小数点后总位数依然大于第一个n时，第一个n不生效
#       当第二个n生效保留完小数点后总位数依然小于第一个n时，第一个n的总数才会生效，并用空格补齐不足位数
