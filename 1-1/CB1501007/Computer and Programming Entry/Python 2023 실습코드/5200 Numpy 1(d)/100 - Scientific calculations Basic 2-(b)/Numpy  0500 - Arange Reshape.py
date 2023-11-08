
from numpy  import *
a = arange(10).reshape(2,5)
print(a)
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
print(a.shape)
print(a.ndim)

b = array( [ (1.5,2,3), (4,5,6) ] )
print("b= ", b)
c = array( [ [1,2], [3,4] ], dtype=complex )
print("c= ",c)
e = zeros( (3,4) )
f = ones( (2,3,4), dtype=int16 )

print("e= ", e)
print("f= ", f)

g = arange( 10, 30, 5 )
h = arange( 0, 2, 0.3 )
i = linspace( 0, 2, 9 )

print("g h i")
print(g, h, i)


b = arange(12).reshape(4,3)
print("b after reshape", b)
c = arange(24).reshape(2,3,4)
print("c after reshape",c)

