import random

def quick_sort(list,i,j):
    if i >= j:
        return 
    pivot = list[i]  
    low = i
    high = j
    while i < j:
        while i < j and list[j] >= pivot:
            j -= 1
        list[i]=list[j]
        while i < j and list[i] <=pivot:
            i += 1
        list[j]=list[i]
    list[j] = pivot
    
    quick_sort(list,low,i-1)
    quick_sort(list,i+1,high)
    return

a = []

for i in range(100000):
    a.append(random.random() + 10000)
    
#a= [2,5,9,3,7,1,5,45,45,65,3,345,6,67,23,3,423,4,23,423,45,6,7,657,56,78,8,0,9]

quick_sort(a,0,len(a)-1)
print("主人排好了！！")
print("成绩排行:",a)


























            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            






