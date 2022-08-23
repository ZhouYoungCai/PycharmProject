#coding:utf-8
'''
定义一个学生类student，该学生有名字name和考试分数score的属性。
定义一个方法，输出print_score()该学生的名字以及考试分数。
并进行构建对象及所有调用的方法。
'''
class student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
        print "构建完成"
    def print_score(self):
        print "我的名字是%s,我考了%d分" %(self.name,self.score)
student1 = student("武大郎",20)
student1.print_score()
print student1.name
print student1.score

class people:
    count=0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        people.count+=1
        print "构建完成"
    def drink(self):
        print "I like coffee"
    def sleep(self):
        print "I want to sleep all day"
people1=people('Jack',16,'male')
people1.drink()
people1.sleep()
print "我是第%d人" %people1.count
print "我是第%d人" %people.count
print "长大两岁了"
people1.age=29
print "我Jack现在%d岁了" %people1.age
people2=people("Tom",20,"male")
print "我%s是第%d个人" %(people2.name,people.count)
