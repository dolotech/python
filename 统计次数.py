#统计列表中出现某个数值的次数

def s(b, c):
    r = 0
    i = 0
    while i < len(b):
        if b[i] == c:
            r +=1
        i += 1
    return r


b = [1, 2, 3, 4, 5, 6,6]

c = s(b, 6)
print(c)
