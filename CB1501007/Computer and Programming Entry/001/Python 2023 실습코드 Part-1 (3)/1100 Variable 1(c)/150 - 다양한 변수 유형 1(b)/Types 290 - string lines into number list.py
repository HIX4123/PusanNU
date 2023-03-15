#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-09-02
#-------------------------------------------------------------------------------


strline = "2345  453  89 122 1200 3400\n"
xl = list( map (int, strline.split()))
print(xl)
print(sum(xl))


strline = "GOO 2345  453  89 122 1200 3400\n"
xl = list( map (int, strline.split()))
print(xl)