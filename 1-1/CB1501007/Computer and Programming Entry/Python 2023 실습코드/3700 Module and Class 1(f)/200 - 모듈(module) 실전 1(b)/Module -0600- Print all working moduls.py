
import math


a= 30
b= 40

def foo():
    global a
    a = a+1
    print(a)

content = dir(math) #math.x 있는 것 모두.,
for w in content :
    print("math( ) = ", w)


foo()

gname = globals()
for w in gname :
    print("globals( ) = ", w)


gname = locals()
for w in gname :
    print("locals( ) = ", w)