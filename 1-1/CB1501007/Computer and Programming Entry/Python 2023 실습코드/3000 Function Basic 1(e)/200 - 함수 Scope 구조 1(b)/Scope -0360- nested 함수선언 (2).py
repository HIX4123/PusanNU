#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


def outer(x):
    def fa():
        print("In fa()")
        return
    def fb():
        print("In fb()")
        return

    if x < 0.5 :
        fa()
    else :
        fb()



outer(1.1)