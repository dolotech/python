list = [5435,34,2,243,4,345,45,657,67,676,999]

first = list[0]

l = len(list)

count = 1

while count < l:
    if first < list[count]:
        first = list[count]
    count +=1
     
print("最大分：",first)

print("=========================== \n")




