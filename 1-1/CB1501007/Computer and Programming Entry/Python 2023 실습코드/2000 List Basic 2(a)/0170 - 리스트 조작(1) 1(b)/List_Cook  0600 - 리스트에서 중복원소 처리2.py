#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-06-03
#-------------------------------------------------------------------------------



Z=list("234583331404")
N=[]
L= len(Z)-1
for i in range( L ) :
    print(f"i={i:2},L={L}, {Z[i], Z[i+1]}")
    if( Z[i] == Z[i+1]) :
       Z.pop(i)
       L -= 1


print(Z)