#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-14
#-------------------------------------------------------------------------------



# Return double of n
def twist(n):
    return ( (n+323)**7%573 + 123*(n+11)**3 )%1000

# We double all numbers using map()
numbers = [1, 2, 3, 4, 11, 12, 17 ]
result = map( twist, numbers) # map object

print( "result=", result )
print( "list(result)=", list(result))

