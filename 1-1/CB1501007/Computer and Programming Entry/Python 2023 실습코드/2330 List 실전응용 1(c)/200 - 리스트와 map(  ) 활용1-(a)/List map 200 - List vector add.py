#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-14
#-------------------------------------------------------------------------------


def add2(a,b):
    return(a+b)




# Add two lists using map and lambda

numbers1 = [1, 2, 3, 11, -10]
numbers2 = [4, 5, 6, 5 , 100]

result = map( lambda x,y: x-y, numbers1, numbers2)
print(list(result))

result = map( lambda x,y: add2(x,y), numbers1, numbers2)
print(list(result))





