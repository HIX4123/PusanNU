#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------
#!/opt/local/bin/python3.4

from functools import singledispatch;

class A(object):

    # default method handles dispatch for undefined types
    # note reversed positional args to match single dispatch functools
    @singledispatch
    def _first(self,arg):
        raise TypeError("no match for A._first(%s)" % type(arg));

    # adapter maps instance call to (reversed) static method call
    def first(self, arg = None): return A._first(arg, self);

    # def first()
    @_first.register(type(None))
    def _(self,none):
        print("A.first() called");

    # def first(float f)
    @_first.register(float)
    def _(self,f):
        print("A.first(float %s) called" % f);

a = A();
a.first();              # A.first() called
a.first(None);          # A.first() called
a.first(3.14);          # A.first(float 3.14) called

class B(object): pass;
b = B();
try: a.first(b);        # no match for A._first(<class '__main__.B'>)
except TypeError as ex: print(ex);