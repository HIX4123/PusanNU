
# Python 3에서는 range( )와 xrange()를 하나로 통일하였다.

import sys

a = range(1,11)  # list는 range( )와는 다르다. Python2.0과 Python 3.0과의 차이
print( type(a) )

for w in a :
    print("*", end=" ")

la = list( a )
print("\n la=", la)


print("a[3]=", a[3])

r = range(10000)
listr= list( range(10000) )
print( " sys.getsizeof(r)= ", sys.getsizeof(r) )
print( " sys.getsizeof(listr)= ", sys.getsizeof(listr) )
