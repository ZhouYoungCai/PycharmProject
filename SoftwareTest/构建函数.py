#coding:utf-8
'''
构建函数使用def关键字
构建函数有四种形式：
1.不传递任何参数
2.传递固定个参数
3.缺省参数，默认参数，当不传缺省参数的对应参数时按照默认进行输出
4.不定个数参数，就是在对应参数前加*
'''
# 1.不传递任何参数
def info(): #构建函数以def开头，info()为函数名
    print "My name is Tom"  #构建函数的对应语句（方法）
info() #调用函数的方法

# 2.传递固定个参数
def info1(name,age):
    print "My name is %s,My age is %d" %(name,age)
info1("曹运镖",27)

# 3.缺省参数，默认参数，当不传缺省参数的对应参数时按照默认进行输出
def info2(name,age=28,kg=90): #注：默认参数只能放在非默认参数之后
    print "My name is %s,My age is %d,My kg is %d" %(name,age,kg)
info2('Jack',30,80)

# 4.不定个数参数，就是在对应参数前加*
def info3(*num):
    for i in num:
        print "num is %d" %i
info3(1,2,3,4,5)