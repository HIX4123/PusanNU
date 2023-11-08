#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-11-08
#-------------------------------------------------------------------------------

def addmore( S ):
    return S * 1.15


salary = [100, 200, 220, 300, 310 ]
lmap  =  map( addmore, salary )

print( next( lmap ) )  # 필요할때만 하나씩 꺼냄
print( next( lmap ) )
print( next( lmap ) )
print( next( lmap ) )


for w in lmap :
    print("w=", w)

