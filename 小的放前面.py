


a = [6,23,23,12,12,3,23,12,31,31,31,123,123,231]

l = len(a)
e = 0
h = l-1
k = a[e]

while e < h:
    while e < h and a[h] >= k:
        h -= 1
    a[e] = a[h]
    while e < h and a[e] < k:
        e += 1
    a[h] = a[e]

a[e] = k

print(a)
