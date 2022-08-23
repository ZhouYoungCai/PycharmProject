1. 创建一个模块person，定义一个people类，
有类属性名字name，身高height，体重weight ，
类方法：工作work，休息rest，
子类 women继承people类，
重写方法:工作，加入新的方法购物，
再加入一个子类man，同时继承people类与women类，
新增方法喝水，
创建一个新的模块dyp调用person中的所有类，
并对三种类分别进行对象创建及调用各自类的所有方法。
#coding:utf-8
class people:
    def __init__(self,name,sg,tz):
        self.name = name
        self.sg = sg
        self.tz = tz
    def work(self):
        print "我%s要去工作了" %self.name
    def xiuxi(self):
        print "我%s要去休息了" %self.name

class women(people):
    def work(self):
        print "我%s是个家庭妇女，在家带小孩" %self.name
    def gouwu(self):
        print "我的身高是%2.2f,我的体重是%d,我%s要去超市买东西," %(self.sg,self.tz,self.name)

class man(people,women):
    def drink(self):
        print "我不仅仅只会喝水，我还会工作，还会休息，还会购物"

#coding:utf-8
from person import *
people1 = people("Tom",192.2,70)
people1.work()
people1.xiuxi()
print people1.name
women1 = women("Jan",188.3,100)
women1.work()
women1.xiuxi()
women1.gouwu()
man1 = man("武大郎",160.2,90)
man1.work()
man1.xiuxi()
man1.gouwu()
man1.drink()
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
