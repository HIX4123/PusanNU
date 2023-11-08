#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


def foo1():
    print(f' foo1() was called')


def foo2():
    print(f' foo2() was called')

def foo3():
    print(f' foo3() was called')

def foo4():
    print(f' foo4() was called')

def fcall( ) :
    print("---- fcall ----- " )



flist=[ foo1, foo2, foo3, foo4, fcall ]

for (i,w) in enumerate(flist) :
    w()

