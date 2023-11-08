#-------------------------------------------------------------------------------
# Purpose:     2020 Power Python
# Author:      Cho - 메롱메롱 메롱롱
#-------------------------------------------------------------------------------


T1 = ['13', '17', '18', '21', '32']
T3 = list(map(int, T1))
print(T3)


# This does the same thing as:
T3 = [int(x) for x in T1]
print( T3 )


# so what you are doing is
T3 = [[int(letter) for letter in x] for x in T1]
print( T3 )

