#!/usr/bin/python3
# Zoh Q. 2019

from __future__ import division
from platform import python_version

# print 문장
print('Python', python_version())
print('Hello, World!')
print("some text,", end="")
print(' print more text on the same line')


# 정수 나눗셈
print('Python', python_version())
print('11 / 3 =', 11 / 3)
print('11 // 3 =', 11 // 3)
print('11 / 3.0 =', 11 / 3.0)
print('11 // 3.0 =', 11 // 3.0)

#unicode
print('1. 한글이 어떻게 될까요 ? ')
print('2. Python', python_version())
print('3. has', type(b' bytes for storing data'))
print('4. and Python', python_version())
print('5. also has', type(bytearray(b'bytearrays')))



N= 100
def test_while():
    i = 0
    while i < N :
        i += 1
        print(i, end=" ")
        if i%10 == 0 : print("\n")
    return

test_while()
