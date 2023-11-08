#-------------------------------------------------------------------------------
# Purpose:     Zoh's Work     "過猶不及"
#-------------------------------------------------------------------------------
def foo():
    s = 0
    for w in range(10000):
        s = another(s, w)

def callfoo100():
    for w in range(100):
        foo()


def another(a,b):
    return(a+b**2)

import cProfile
import re
cProfile.run( 'callfoo100()' )

#cProfile.run('re.compile("foo|bar")')