#列表：[234234,243234,6546], ["dfad","234234"]
#数字：,123123,34,12
#字典：{}
#字符串 str： "adf"  '你的名字'  "123"
#空值：None
#布尔型 bool：True,  False

print(["a","B"])

print(['a','Brere'])

print(['a','412312'])

print(['a',412312])


a = True   

b = 1==1  

print("b:",b)


if a:
    print("真",a)
else:
    print("假",a)

x = 3 - 4 == 9
if x:
    print("是")
else:
    print("假",x)

#==============================================
def fun(p):
    print(p)

fun("abc")

print("#==============================================")

dic = {"a":"许多","b":"许颖娜","c":None}#  键:值    键值对
dic["d"] = "好好玩"
print(dic["d"])
dic = {}
for boy in dic :
    if boy == "b":
        dic[boy] = "捣蛋鬼"
        break
   # print(boy)
       
#print(dic)


c = 0
while True:
    c +=1
   # print("while",c)
    break
    
#=======================================================


d = {"1":"a","2":"b","3":"c"}
f = {}

for e in d :
    f[e] = d[e]    

print(d)
print(f)

j = {}
g = {}

count = 0
while count < 100:
    j[str(count)] = count + 100
    count += 1


for y in j:
    g[y] = j[y]

print("------",g)

z = str(1231)

print( type(z))


p = "123"

h  = int(p)

print(h + 1)

o = "789"
l = int (o)

print(type(o)==type(l))
print(o,l)





















