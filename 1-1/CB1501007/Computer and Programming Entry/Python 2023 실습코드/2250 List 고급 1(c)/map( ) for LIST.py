#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-11-08
#-------------------------------------------------------------------------------

def addmore( S ):
    return S * 1.15


salary = [100, 200, 220, 300]
sal2 = list( map( addmore, salary ))
print( sal2 )


func =map(lambda mylocal: mylocal*1.5, salary)
print( func )

sal3  = list( map(lambda mylocal: mylocal*1.2, salary) )
print( sal3 )