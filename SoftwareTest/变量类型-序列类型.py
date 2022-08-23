#coding:utf-8
'''
序列类型（两种） 1.列表   2.元组
'''
'''
1.列表(list)：有序数组，列表可以添加多个数据，添加字符串，数字，列表等。
列表定义方式： 变量名 = [xxx,'xxx',[xxx,"xxxx"]]  #每个元素使用英文逗号隔开
'''
list = [123,"jack",456,[277,"Tom"]]
print list
print type(list)

list1 = ["你好",'Jan']
#转换中文输出格式： str(变量名).decode('string-escape')
print str(list1).decode('string-escape')

print "================分割线============"

'''
2.元组（tuple）:有序数组，代表多个元素的组合，特点是只读类型变量，意味一旦生成，内容不可修改。例：身份证号码
元组的定义方式：变量名 = (xxx,'xxx',[xxx,"xxxx"])
'''
tuple = (123,"jack",456,[277,"Tom"])
print tuple
print type(tuple)

tuple1 = ("你好",'Jan')
#转换中文输出格式： str(变量名).decode('string-escape')
print str(tuple1).decode('string-escape'),type(tuple1)