
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     2017 Computer Introduction - CSED
# Author:      Cho
#-------------------------------------------------------------------------------
# zip 함수는 동일한 갯수의 요소값을 갖는 시퀀스 자료형을 묶어주는 역할을 한다.

la = [ 1,2,3,4,5,6]
lb = [11, 22, 33, 44, 55, 66]
lc = [ 1, 0 , 1, 0, 1, 1]

za = list(zip([1,2,3], [4,5,6]))
zb = list(zip([1,2,3], [4,5,6], [7,8,9]))
zc = list(zip("abc", "def", "COLA"))

print(za)
print(zb)
print(zc)

print("\n How to work zip() ")

for x,y,z in zip(la, lb, lc):
    s = x*y*z
    print(("s= ", s))

