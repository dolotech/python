def ppp (oo):
    if oo >= 90:
        return "A"
    elif oo >= 80:
        return "B"
    elif oo >= 70:
        return "C"
    elif oo >= 60:
        return "D"
    else:
        return "F"
        
        
d = ppp(87)

print("等级:",d)


        
        