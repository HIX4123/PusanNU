

a = 100
b = a
print(f"type(a)= {type(a)}")
print( " id(a)=", id(a))
print( " id(b)=", id(b))
print( " id(100)=", id(100))

b += 1
print(f"type(b)= {type(b)}")
print( " id(a)=", id(a))
print( " id(b)=", id(b))
print( " id(101)=", id(101))
