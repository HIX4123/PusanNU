#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-04-07
#-------------------------------------------------------------------------------


L = input("Type two numbers:")
myb = int( L.split()[0] )
mye = int( L.split()[1] )
print(myb, mye, myb+mye)

S = 0
for w in range(myb, mye+1):
        S += w


print(f"{myb}부터 {mye}까지 합은 {S}")


# function foo(x,y) : parameter
# A.py에서 command line직접 들어가는 명령 argumewnt