def remove(list,item):
    i = 0
    while i <  len(list):
        if list[i] == item:
            list.pop(i)
        else:
            i += 1  



a = [3,3,3,3,3,3,5,6,7,8,9,3,3,3,3,3,3,3,3,3,3,3,20,43]

#a[2:3] = []
#a.pop(2)
#a.remove(3)
#del a[0]




#  去掉列表中所有值为3的元素
remove(a,3)



a = [1,2,3,4,5]

del a[0]

a.insert(-1,7)

print(a)