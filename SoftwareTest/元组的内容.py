#coding:utf-8
'''
元组（tuple）:属于只读变量，所以不支持增加、删除和修改元组内的元素
'''
#1.元组的切片，同列表。（举例：参考列表，把中括号改为小括号即可）
#2.元组的加法和乘法运算，同列表。
# b = (1,2,3,'Hi')
# c = (4,5,6,'Jack')
# d = b+c
# print d
#3. 无法修改和删除单个元素，可删除整组元素
# 格式：del 变量名
a = (1,3,3,4,2,5)
print a
# del a
# print a

#4.元组中支持的函数
#count()函数
print a.count(3)
#sorted()函数
print sorted(a),type(sorted(a))
#max(),min(),len() 参考列表