#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

# 내용이 동일한가 ? equal
# 그 자체가 같은 내용인가 ?

la=[1,2,3]
lb=[1,2,3]
lc = la


if(la == lb):  print("la equal(==) to lb")
else : print("la not equal to lb")

if(la is lb):  print("la is to lb")
else : print("la is not to lb")

if(la == lc):  print("la equal(==) to lc")
else : print("la not equal to lc")

if(la is lc):  print("la is to lc")
else : print("la is not to lc")


print("id(la)= ", id(la))
print("id(lb)= ", id(lb))
print("id(lc)= ", id(lc))