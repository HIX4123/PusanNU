#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-10-16
#-------------------------------------------------------------------------------

test = ['1.1', '4', "456.7", '5', '6.12']

for number in test:
    try:
        print(int(number))
    except ValueError:
        print( f" We got float= {float(number)}")