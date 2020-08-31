'''
class Rect():
    chang = 0
    kuan = 0

    def __init__(self,c,k) :
        self.chang = c
        self.kuan = k

    def zhouchang(self):
        return (self.chang + self.kuan) *2

    def mianji(self):
        return self.chang * self.kuan

    def zhengfang(self):
        a =  self.chang == self.kuan
        return a

r = Rect(100,50)

print("面积:",r.mianji())
print("周长:",r.zhouchang())



r = Rect(300,100)
print("面积:",r.mianji())
print("周长:",r.zhouchang())

print(r.zhengfang())
'''


class Changfang():

    chang = 0
    kuan = 0    
    
    def __init__(self,v,c):
        self.chang = v 
        self.kuan = c  

    def yi(self):
        return (self.chang + self.kuan) *2

    def re(self):
        return self.chang * self.kuan

    def san(self):
        return self.chang != self.kuan

t = Changfang(20,10)               

print(t.yi())
print(t.re())   

print(t.san())

print(t.chang,t.kuan)