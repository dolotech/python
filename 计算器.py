while True:
    print("请输入一个数字")
    u = int(input())
    print("请输入一个符号")
    q = input()
    print("请再输入一个数字")
    i = int(input()) 
    s = 0
    if q == "+":  
        s = u + i
    elif q == "-":
        s = u - i
    elif q == "*":
        s = u * i
    elif q == "/":
        s = u / i
    print("结果:",s)

    
    
    