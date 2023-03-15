#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

_var = 100

my = Test()
print("my.foo=", my.foo)
print("my._bar=", my._bar)