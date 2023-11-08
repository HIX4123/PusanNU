#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-21
#-------------------------------------------------------------------------------


def cho( ) :
    yield "조"
    yield "환"
    yield "규"
    yield "랑"
    yield "께"

ycho = cho( ) # ycho가 generator
a = next(ycho)
print(a)
a = next(ycho)
print(a)
a = next(ycho)
print(a)

