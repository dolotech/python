def s(o):
    l = len(o)
    i  = 0
    while i < l-1:
        j = i+1
        while j < l:
            if o[i] > o[j]:
                o[i] , o[j] = o[j] , o[i]
            j+=1
        i+=1

a = [4,4,6,7,2,3,4,5,9,0]

s(a)
print(a)

def s(d):
    o = len (d)
    i = 0
    while i < o-1:
        j = i+1
        while j < o:
            if d[i] > d[j]:
                d[i],d[j]=d[j],d[i]
            j += 1
        i += 1
t = [1,3,2,6,5,4,7,9,0]
s(t)
print(t)








