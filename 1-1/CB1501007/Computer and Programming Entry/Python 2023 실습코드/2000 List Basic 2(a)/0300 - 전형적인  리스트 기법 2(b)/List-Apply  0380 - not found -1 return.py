#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-14
#-------------------------------------------------------------------------------

L = list("부산갈매기너는정녕나를버리련가")


def my_index1(L, obj):
     for i, el in enumerate(L):
             if el == obj:
                     return i
     return -1

def my_index2(L, obj):
    try:
           return L.index(obj)
    except ValueError:
           return -1

def my_index3(L, obj):
    if obj in L:
           return L.index(obj)
    return -1


for w in list("정기매가똥부"):
    print(f' w={w},  {my_index1(L,w)}')
