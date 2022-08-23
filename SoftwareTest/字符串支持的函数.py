#coding:utf-8
#1.upper()   2.lower()   3.capitalize()
#格式：变量名.upper()

s = "helLoPyThoN"
print s.upper() #全部字母大写格式
print s.lower() #全部字母小写格式
print s.capitalize() #首字母大写格式 

#1.find()
t = "I love python"
#find查找子字符串，返回子字符串的首字符下标索引
print t.find("love")
print t.find('py')
print t.find("heno") #当不包含子字符串是，返回-1

#1.split() #字符串分割，以列表返回分割后的部分
c = "Hello world"
print c.split(),type(c.split()) #默认以空格作为分隔符
d = "He:llo: wor:ld"
print d.split(":") #指定以：作为分隔符

#1.startswith(),endswith()
#判断字符串以xxx开头/结尾，返回布尔值
print "helloworld".startswith("a")
print "helloworld".startswith("hel")
print "helloworld".endswith("ld")


