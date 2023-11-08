#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-30
#-------------------------------------------------------------------------------

def foo():
    print("In foo()")
    goo()
    moo()
    return


def goo():
    print("In goo()")
    roo()
    moo()
    return



def roo():
    print("In roo()")
    return

def moo():
    print("In moo()")
    return



print("스타트:")
foo()