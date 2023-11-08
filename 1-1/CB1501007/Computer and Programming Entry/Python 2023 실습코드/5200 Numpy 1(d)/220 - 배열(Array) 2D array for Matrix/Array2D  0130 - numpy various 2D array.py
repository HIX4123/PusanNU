
import numpy

a = numpy.matrix('1 2; 3 4')                 # use Matlab-style syntax
b = numpy.arange(25).reshape((5, 5))         # create a 1-d range and reshape
c = numpy.array(list(range(25))).reshape((5, 5))   # pass a Python range and reshape
d = numpy.array([5] * 25).reshape((5, 5))    # pass a Python list and reshape
e = numpy.empty((5, 5))                      # allocate, but don't initialize
f = numpy.ones((5, 5))                       # initialize with ones
g = numpy.ndarray((5, 5))                    # use the low-level constructor


print("\n a=", a)
print("\n b=", b)
print("\n c=", c)
print("\n d=", d)
print("\n e=", e)
print("\n f=", f)
print("\n g=", g)