#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-14
#-------------------------------------------------------------------------------



# Double all numbers using map and lambda

numbers = [1, 2, 3, 4, 9, -3, 5, 10 ]
result = map(lambda x: x + x, numbers)
print(list(result))


