
# 함수와 Scoping Rule : Global and Local



def doggie(a,b):
    print("In doggie()")
    b,a = a,b
    print("after swap=", a,b)
    return (a+b)



a = "W"
b = "Z"
print("main 01=", a,b)
doggie(a,b)
print("main 02=", a,b)