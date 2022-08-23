#coding:utf-8
'''
类的继承和重写
类的继承：可以理解为孩子（子类）继承父亲（父类）的财产、基因等。
类继承和重写，子类继承父类，若不修改重写内容，则默认父类所有的方法及属性框架
子类继承父类写法：
class 子类名(父类名):
'''
class father: #父类
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sleep(self):
        print "我%s要去睡觉了" %self.name
    def work(self):
        print "我今年%d岁，我%s要去工作了" %(self.age,self.name)
#构建实例化对象
if __name__=="__main__": #其中name和main前后的是两个下划线，这句加在所有执行语句前面，这样可以避免其他包调用时
                         #执行到该方法的语句（注：这个方法加入后，下面的执行语句需要缩进）
    father1 = father('Jack',30)
    father1.sleep()
    father1.work()
    print father1.name
    print father1.age

class son(father):
    def __init__(self,name,age,sex): #添加了一个新的属性
        self.name = name
        self.age = age
        self.sex = sex
    def drink(self): #添加一个新的方法
        print "我%s要喝奶奶" %self.name
    def work(self): #重写的方法
        print "我才%d岁，还不会工作" %self.age
if __name__=="__main__":
    son1 = son("Jackson",2,'male') #构建实例化对象，需要对应属性个数
    son1.sleep() #继承了父类的方法
    son1.drink() #调用了自己定义的新方法
    son1.work() #调用重写的方法