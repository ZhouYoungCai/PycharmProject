#coding:utf-8
'''
1.编写程序实现：提示用户输入考试分数，如果分数大于100，输出分数无效，
如果分数大于等于90，输出非常优秀，如果分数大于等于80分，输出优秀，
如果分数大于等于70分，输出良好，如果分数大于等于60分，输出及格，
如果小于60分，输出等着补考吧
'''
# score = input("请输入考试分数：")
# if 0<= score < 60:
#     print "等着补考吧"
# elif 60 <= score < 70:
#     print "及格"
# elif 70 <= score < 80:
#     print "良好"
# elif 80 <=score < 90:
#     print "优秀"
# elif 90 <= score <= 100:
#     print "非常优秀"
# else:
#     print "分数无效"

#编写程序实现，提示用户输入三个数，最终输出三个数中最大的值.
'''
a = input("请输入一个数：")
b = input("请输入一个数：")
c = input("请输入一个数：")
if a>=b:
    temp=a
else:
    temp=b
if c>=temp:
    print c
else:
    print temp
'''

#编写程序实现，提示用户输入三位的整数，判断是否是水仙花数字.
# 提示：
# 取个位数： 153%10
# 取十位数:  153/10%10
# 取百位数： 153/100
'''
i = input("请输入一个三位数：")
ge = i%10
shi = i/10%10
bai = i/100
if i==ge**3+shi**3+bai**3:
    print "是水仙花数"
else:
    print "不是水仙花数"
'''

#4.编写程序实现，输出100~999的所有水仙花数，用while循环.
'''
a = 100
while a<=999:
    g = a%10
    s = a/10%10
    b = a/100
    if a==g**3+s**3+b**3:
        print a
    a+=1
'''

#对100以内的两位数，请使用一个while循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）.
'''
a = 10
while a<=99:
    g = a%10
    s = a/10%10
    if s<g:
        print a
    a+=1
'''
#输出99乘法表。用while循环打印.
x = 1
y = 1
while x<=9:
    y=1
    while y<=x:
        print "%d*%d=%2d" %(x,y,x*y),
        y+=1
    print
    x+=1

#coding:utf-8
'''1.通过while循环编写1+2+3+....+100的和

2.通过while循环编写100内所有的奇数和

3.通过while循环编写100内所有的偶数和'''
# a = 1
# s = 0
# while a<=100:
#     s+=a  #同s=s+a
#     a+=1
# print s
#100内的奇数，以及奇数和
'''
a = 1
s = 0
while a<=100:
    if a%2==1:
        s+=a #s=s+a
        print a
    a+=1
print s
'''
#100内的偶数，以及偶数和
'''
a = 1
s = 0
while a<=100:
    if a%2<>1:
        s+=a
        print a
    a+=1
print s
'''
