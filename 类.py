class Studen():  # 类（图纸，模板）
    name = ''       #属性 （变量）
    age = 0
    grade = 0
    sex = ''
    def print(self):       # 方法（函数）
        print(self.name,self.age,self.grade,self.sex)
    def said(self,msg):
        print(self.name,msg)

s = Studen()   #实例化对象，实例
s.age = 10
s.name = '许多'
s.grade = 4
s.sex = '男'
s.print()
s.said("hello")

s1 = Studen()   #实例化对象，实例
s1.age = 7
s1.name = '许颖娜'
s1.grade = 1
s1.sex = '女'
s1.print()
s1.said("hello")

k = Studen()
k.age = 11
k.name = '杨雅善'
k.grade = 4
k.sex = '女'

k.print()
#--------------------------------------------------


class Duck():
    c = ''
    w = 0
    h = 0
    n = ""
    def cal(self):
        return self.w * self.h

    def chi(self):
        print("我在吃东西")

    def jiao(self):
        print("嘎嘎,我是%s的鸭子，我叫:%s" % (self.c,self.n))

d = Duck()
d.n = "小兵"
d.w = 2
d.c = "白色"
d.h = 20
d.jiao()
d.chi()
print(d.cal())
#---------------------------------------


class Car():
    f = ''
    l = 0
    m = 0
    v  = 0

    def __init__(self,f1 ='铁',l1=10, m1 = 4,v1 = 60) :
        self.f = f1
        self.l = l1
        self.m = m1
        self.v = v1

    def make(self):
        print('我是%s做的' % self.f)
    def luntai(self):
        print('我有%s个轮胎' % self.m)
    def suoyou(self):
        print('我可以坐%s个人,我是%s做的,我有%s个轮胎' % (self.l,self.f,self.m))

    def juli(self,hour):
        return self.v * hour

l = Car()
l.l = 4
l.m = 9
l.make()
l.luntai()
l.suoyou()


car = Car('钢',52,16,61)
car.make()
car.luntai()
car.suoyou()

print(car.juli(8))




