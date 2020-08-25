

a = [1,23,1,231,23,1,23,1,23,123,1,23,12]
l = len(a)
i = 0
while i < l:
    a[i],a[l-1-i] = a[l-1-i],a[i]
    i += 1
print(a)    