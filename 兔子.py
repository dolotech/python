#一对兔子出生一个月后每个月能生一对兔子
#12个月一对兔子能生多少对

def oiu(o):
    i = 0
    k = 0
    l = 1
    while i < o:
        k,l = l ,k + l
        i += 1

    return l

u =  oiu(100)
print(u)   
    

