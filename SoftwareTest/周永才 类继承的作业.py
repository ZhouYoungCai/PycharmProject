1. 创建一个模块person，定义一个people，类	
有类属性名字name，身高height，体重weight ，
类方法：工作work，休息rest，
子类 women继承people类，
重写方法:工作，加入新的方法购物，
再加入一个子类man，同时继承people类与women类，
新增方法喝水，
创建一个新的模块dyp调用person中的所有类，
并对三种类分别进行对象创建及调用各自类的所有方法。
#coding:utf-8
class person:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
        print "构建完成"
    def work(self):
        print "我%s的工作是软件测试工程师" %self.name
    def rest(self):
        print "多休息才能长高，我的身高是%d厘米" %self.height

class women(person):
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def work(self):
        print "%s喜欢购物" %self.name
    def shopping(self):
        print "我%s喜欢购物" %self.name    

class man(person,women):
    def drink(self):
        print "我%s还不会喝东西" %self.name

from person import *

person1=person("zhangsan",175,65)
person1.rest()
person1.work()

women1=women("lisi",172,62)
women1.work()
women1.rest()
women1.shopping()

man1=man("wangwu",171,61)
man1.work()
man1.drink()
man1.rest()
man1.shopping()

2.请查看以下代码，求结果
class A:
   def go(self):
      print "go A go!"
   def stop(self):
      print "stop A stop!"

class B(A):
   def go(self):
      print "go B go!"

class C(A,B):
   def stop(self):
      print "stop C stop!"

实例化如下：
a=A();b=B();c=C()

求运行结果：
a.go();a.stop();    #go A go!    stop A stop!

b.go();b.stop();    #go B go!    stop A stop!

c.go();c.stop();    #go A go!    stop C stop!
