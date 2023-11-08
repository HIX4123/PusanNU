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

def fcall( F ) :
    print("---- fcall ----- " )
    F()


for w in range(1,5):
    fname= "foo"+str(w)
    print( f' fname={fname}')
    fcall( fname )


