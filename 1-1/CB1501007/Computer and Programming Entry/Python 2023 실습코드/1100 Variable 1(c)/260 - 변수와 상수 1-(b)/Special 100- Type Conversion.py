

x = "101101"  # Converts x to an integer. base specifies the base if x is a string.
y = int(x,2)
print("int(x,2)=", x, y)



y = int("12300214" ,5 ) # Converts x to a long integer. base specifies the base if x is a string.
print(y)

y = float("324.56") # Converts x to a floating-point number.
print("y*10=", y*10)

y = complex( 9 , 3) # Creates a complex number.
print(y)

y = str( 3245) # Converts object x to a string representation.
print("stringed y= ", y+"--")


t = eval("45 + 10") # Evaluates a string and returns an object.
print(t)


t = list("Summer는 여름입니다.") # 문자열을 리스트로 바꿈
print('list=', t)
print("t[-4]=", t[-4])

s = [3, 5, 5, 6, 6, 6, 3] # Converts s to a set.
t = set(s)
print("set=", t)

myb = 0b11010111
myc = bin(myb*1024)
print( myb, myc)

print("hex(14)=",  hex(14)) # 16진수로 바꾸기
print("oct(111)=", oct(111)) # 8진수로 바꾸기

