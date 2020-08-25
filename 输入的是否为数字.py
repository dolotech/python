try:
    a = input("输入一个数：")
    #判断用户输入的是否为数字
    if(not a.isdigit()):
        print("a 必须是数字")
        raise ValueError("a 必须是数字")
except ValueError as e:
    print("引发异常：",repr(e))