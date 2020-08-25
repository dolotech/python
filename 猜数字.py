import random
print("猜一下1——100的数字")
t = int(random.random()*100 + 1)
#print(t)
while True:
    i = int(input())
    
    if t == i:
        print("恭喜猜对了",t)
        break
    elif t > i:
        print('你猜小了')
    else:
        print('你猜大了')






























