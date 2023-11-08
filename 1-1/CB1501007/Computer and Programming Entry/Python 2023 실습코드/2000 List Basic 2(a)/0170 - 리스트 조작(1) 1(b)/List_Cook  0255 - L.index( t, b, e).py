#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-03-26
#-------------------------------------------------------------------------------

A = "Sun Mon Tue Wed Thu Fri Sat Sun Tue Wed Thu Fri Sat".split()
word = "Wed"
index = A.index( word )
print(f"wed의 위치 = {index}")


index = A.index( word, 7)
print(f"wed의 위치2 = {index}")


#index = A.index( word, 12)
print(f"wed의 위치2 = {index}")
