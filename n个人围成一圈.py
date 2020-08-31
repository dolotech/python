#有n个人围成一圈，顺序排号。
#从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。


j = 10
y = [p for p in range(1,j+1)]    #  列表推导式

k = h = l = 0
while l < j -1:
    if y[k] != 0:
        h += 1

    if h ==3:
        y[k] = h = 0
        l += 1
    k += 1

    if k ==j:
        k = 0
# print(y)

for k in y:
    if k >0:
        print("K:",k)
        break
    print(k)


p = []
i = 1
while i <=10:
    p.append(i)
    i +=1
print(p)

print([p for p in range(1,10+1)] )