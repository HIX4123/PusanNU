#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문 2020
# Author:      Cho -    조환규 교수님 만쉐이...
# 나의 목표:   학생들을 최대한 괴롭히자.
# Created:     2020-03-26
#-------------------------------------------------------------------------------

a = 100
b = a
print( type(a))
print( " id(a)=", id(a))
print( " id(b)=", id(b))
print( " id(100)=", id(100))

b = 111
print( type(b))
print( " id(a)=", id(a))
print( " id(b)=", id(b))
print( " id(100)=", id(100))

la=[3,4,5]
lb= la
print( " id(la)=", id(la))
print( " id(lb)=", id(lb))

la.append(50)
print("la=", la)
print("lb=", lb)

