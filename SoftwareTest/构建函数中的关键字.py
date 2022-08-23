#coding:utf-8
# return :返回值
'''
def my_abs(num):
    if num<0:
        print -num
    else:
        print num
print my_abs(8)
'''
#其中my_abs(8)已经调用了def里的方法，def里的方法就有print的操作，即print 8，而
#在调用方法前面加入print即是输出def返回的默认值，默认值为None
#注：若在编写函数时未添加返回值，则默认return一个None值

#理解print和return的区别：
def a():
    print 1
def b():
    return 3
d=a() #d是a()函数下的方法，print 1 即打印1
e=b() #e是b()函数下的方法，return 3 返回一个3的值
# print d+1 #打印出来的1是不能存储后期使用，所以不能执行1+1=2的操作
print e+1 #return返回的值可以存储着后续使用，因此可以打印3+1=4

# 注：print打印的值只是作为显示，但return返回的值可以存储继续使用