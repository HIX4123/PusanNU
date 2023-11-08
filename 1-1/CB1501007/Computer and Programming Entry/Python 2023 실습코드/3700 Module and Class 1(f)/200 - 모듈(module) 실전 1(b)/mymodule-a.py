# FILE : mymath02.py

mypi = 3.14
goodpi = 3.141593
mystring = "이것은 한글이다"

def add(a, b):
    print("calling add( )")
    return a + b

def area(r):
    print("calling area( )")
    return mypi * r * r

print(area(4.0))
