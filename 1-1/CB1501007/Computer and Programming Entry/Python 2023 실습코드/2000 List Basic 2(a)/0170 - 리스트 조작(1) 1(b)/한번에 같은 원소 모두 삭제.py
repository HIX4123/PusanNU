#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2022-03-03
#-------------------------------------------------------------------------------

# 여러 원소를 한번에 리스트에서 삭제하기

x = [1,2,3,2,2,2,3,4]
결과 = list(filter(lambda a: a != 2, x))

print(결과)