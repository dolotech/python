a = [345,2,45,214,51,245,2134,5,2345,23,45,23,45,23,45,2,345,23,45]
r = len(a)
y = 0
while y < r-1:
    c=y+1
    while c < r:
        if a[y] > a[c]:
            a[y],a[c] = a[c],a[y]
        c += 1   
    y += 1
print("成绩排行:",a)   
        
        





























            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            






