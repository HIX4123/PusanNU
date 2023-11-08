#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-02-29
#-------------------------------------------------------------------------------

import sys
import numpy
import array

La = [ True , 'a', 100, "summer", 456.3489242, [4,5,6,7], range(500) ]

for w in La :
    print( w, ": ", type(w), ">> ", sys.getsizeof(w))



datatype="""
'c' char character 1
'b' signed char int 1
'B' unsigned char int 1
'u' Py_UNICODE Unicode character 2 (see note)
'h' signed short int 2
'H' unsigned short int 2
'i' signed int int 2
'I' unsigned int long 2
'l' signed long int 4
'L' unsigned long long 4
'f' float float 4
'd' double float 8
"""

t1 =  array.array('i', [5,6,7])
#t2 =  array.array('c', 'hello world good boy')   # Python 3에서는 c를 지원하지 않는다. 더 이상
t2 =  array.array('u', 'hello 한국인 \u2641')
t3 =  array.array('l', [1, 2, 3])
t4 =  array.array('f', [1.0, 2.0, 3.14])
t5 =  array.array('d', [1.0, 2.0, 3.14])
t6 =  array.array('L', [ 3, 4, 5])
t7 =  array.array('i', [1])
for w in range(100):
    t7.append( w )

Lb = [ t1, t2, t3, t4, t5, t6, t7 ]

for (i,w) in enumerate(Lb) :
    print( i+1, " size()",  sys.getsizeof(w), type( w[0]) )