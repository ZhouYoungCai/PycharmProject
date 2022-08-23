#coding:utf-8
'''
break:中断循环，当条件语句为真时，直接中终止跳出循环
continue:跳出本次循环，执行下一轮循环
pass:占位符
'''
#while举例：
'''
a = 0
while a<10:
    a+=1
    if a==7:
        # break
        # continue
        pass
    print a,
else: #当上述循环非强制情况下完成循环，则执行else下的语句
    print "=====over======"
'''
#for 举例：

str = "python"
for obj in str:
    if obj=='t':
        continue
    print obj
else:
    print "=====over===="
