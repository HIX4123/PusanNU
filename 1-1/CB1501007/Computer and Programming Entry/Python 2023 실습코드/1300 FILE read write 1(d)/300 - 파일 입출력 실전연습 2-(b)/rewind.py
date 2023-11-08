#-*- coding: cp949 -*-
# Name:        module1
# Author:      Zoh
# Created:     30-12-2017
#-------------------------------------------------------------------------------

fa = open("test.txt", "r")

print fa.readline()
print fa.readline()
print fa.readline()

x = fa.tell()
print fa.readline()

fa.seek(x)
print fa.readline()


