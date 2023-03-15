#!/usr/bin/python3
# https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html
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
print(' 한글이 어떻게 될까요 ? strings are now utf-8 \u03BCnico\u0394é!')
print('Python', python_version(), end="")
print(' has', type(b' bytes for storing data'))
print('and Python', python_version(), end="")
print(' also has', type(bytearray(b'bytearrays')))

print('\n timing range()')

N= 100
def test_while():
    i = 0
    while i < N :
        i += 1
        print(i, end=" ")
        if i%10 == 0 : print("\n")
    return

test_while()
