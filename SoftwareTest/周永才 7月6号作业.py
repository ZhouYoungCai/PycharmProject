1.通过while循环编写1+2+3+....+100的和

#coding:utf-8
a = 1
s = 0
while a<=100:
    s+=a
    print s
    a+=1

2.通过while循环编写100内所有的奇数和

#coding:utf-8
a = 1
s = 0
while a<=100:
    s+=a
    print s
    a+=2

3.通过while循环编写100内所有的偶数和

#coding:utf-8
a = 2
s = 0
while a<=100:
    s+=a
    print s
    a+=2

1.编写程序实现：提示用户输入考试分数，如果分数大于100，输出分数无效，
如果分数大于等于90，输出非常优秀，如果分数大于等于80分，输出优秀，
如果分数大于等于70分，输出良好，如果分数大于等于60分，输出及格，
如果小于60分，输出等着补考吧

#coding:utf-8
score = input("请输入考试分数：")
if score < 60:
    print "等着补考吧"
elif 60 <= score < 70:
    print "及格"
elif 70 <= score < 80:
    print "良好"
elif 80 <=score < 90:
    print "优秀"
elif 90 <= score <= 100:
    print "非常优秀"
else:
    print "分数无效"

2.编写程序实现，提示用户输入三个数，最终输出三个数中最大的值.

#coding:utf-8
a = input("请输入一个数：")
b = input("请输入一个数：")
c = input("请输入一个数：")
if a <= b <= c:
    print c
elif b <= a <= c:
    print c
elif a <= c <= b:
    print b
elif c <= a <= b:
    print b
elif b <= c <= a:
    print a
elif c <= b <= a:
    print a
else:
    print "输入有误"

3.编写程序实现，提示用户输入三位的整数，判断是否是水仙花数字.

例如水仙花数：153  1**3+5**3+3**3=153（百位数、十位数、个位数的立方和与它本身相等为水仙花数）

提示：

取个位数： 153%10
取十位数:  153/10%10
取百位数： 153/100

#coding:utf-8
i = input("请输入一个三位数：")
j = (i/100)**3+(i/10%10)**3+(i%10)**3
if j==i:
    print "是水仙花数字"
else:
    print "不是水仙花数字"


4.编写程序实现，输出100~999的所有水仙花数，用while循环.

#coding:utf-8
i=99
while i<999:
    i+=1
    j = (i/100)**3+(i/10%10)**3+(i%10)**3
    if j==i:
	print i


5.对100以内的两位数，请使用一个while循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）.

#coding:utf-8
i=9
while i<100:
    i+=1
    if i/10<i%10:
	print i

6.输出99乘法表。用while循环打印.

#coding:utf-8
i=0
j=0
while i<9:
    i+=1
    while j<9:
        j+=1
        print j,"x",i,"=",i*j,"\t",
        if i==j:
            j=0
            print("")
            break

7. 日报.

