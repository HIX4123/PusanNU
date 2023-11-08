
import numpy
import array

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

t1 =  array.array('l', [5,6,7,8,100])
# t2 =  array.array('c', 'hello world good boy')
# Python 3에서는 c를 지원하지 않는다. 더 이상
t3 =  array.array('u', 'hello \u2641')
t4 =  array.array('l', [1, 2, 3, 4, 5])
t5 =  array.array('d', [1.0, 2.0, 3.14])

x = array.array('b')
x.frombytes('test'.encode())
print(x)
print(x.tobytes())
print( x.tobytes().decode() )

print(t1[0])
print(t3)
print(t4)
print(t5)