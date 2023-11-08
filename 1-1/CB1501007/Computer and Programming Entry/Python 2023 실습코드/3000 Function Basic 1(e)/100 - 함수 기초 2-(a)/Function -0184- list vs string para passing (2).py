#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-03-25
#-------------------------------------------------------------------------------


def endmark(L):
    L.append("$")
    L.pop(0)
    return

def endmark2(S):
    S += "$"
    return(S)



a=[1,2,3,4,5]
print(f"Before a = {a}")
endmark(a)
print(f"After a = {a}")