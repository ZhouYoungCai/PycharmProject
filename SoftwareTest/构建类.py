#coding:utf-8
'''
类是面向对象语言中独有的。
类：可以定义框架（类属性）和对应使用的方法，根据类可以构建对象
构建出的对象将满足可以使用该类所有的方法并且拥有所有的属性
类使用关键字  class
'''
'''
格式：
class 类名:
    类变量=0  构建计数 （不是必须）
    def __init__(self,属性1，属性2，属性3....):
        self.属性1 = 属性1
        self.属性2 = 属性2
        self.属性3 = 属性3
        ....
        类名.类变量+=1
    def 方法1(self):
        内置语句1
    def 方法2(self):
        内置语句2
    .....
'''
class people: #people是类名
    count=0  #count是类变量
    def __init__(self,name,age,sex): #注意init前后有两个下划线，self是一个固定格式，后面的name,age,sex都是属性
        self.name = name #封装属性
        self.age = age
        self.sex = sex
        people.count+=1 #构建计数+1
        print "构建完成"
    def drink(self): #定义一个drink方法
        print "I like coffee" #drink方法下的内置语句
    def sleep(self):#定义一个sleep方法
        print "I want to sleep all day" #sleep方法下的内置语句
#根据类构建对象实例  格式：变量名 = 类名(对应属性给予的值)
people1 = people('Jack',27,'male')
#根据该构建的对象使用所有方法 格式：变量名.函数名()
people1.drink()
people1.sleep()
#查看类变量的方法
print "我是第%d人" %people1.count  #通过对象访问类变量
print "我是第%d人" %people.count  # #修改对象实例的属性
print "长大两岁了"
people1.age = 29
print "我Jack现在%d岁了" %people1.age

#构建第二个对象
people2 = people('Tom',20,"male")
print "我%s是第%d个人" %(people2.name,people2.count)
