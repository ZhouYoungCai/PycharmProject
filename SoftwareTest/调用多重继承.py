#coding:utf-8
'''
类的调用和多重继承。
类的调用也是遵循模块调用的两种方式。
多重继承：可以理解为还有个孙子，他不单单可以继承父亲，还可以继承爷爷。
多重继承：多个类间的互相继承
多重继承的写法：
class 类名(父类名,子类名):
注：相同方法名的方法以及框架都优先继承父类，若不同方法则可以完全同时继承。
'''
from leijichenghechongxie import *
class sun(father,son):
    def play(self): #添加新方法
        print "我%s还在妈妈的肚子里" %self.name
    def drink(self): #重写了drink的方法
        print "我%s还不会喝东西" %self.name
sun1 = sun('Jacksun',0) #优先继承父类名的框架（属性）
sun1.work() #优先继承父类名的方法
sun1.drink()
sun1.sleep()
sun1.play()