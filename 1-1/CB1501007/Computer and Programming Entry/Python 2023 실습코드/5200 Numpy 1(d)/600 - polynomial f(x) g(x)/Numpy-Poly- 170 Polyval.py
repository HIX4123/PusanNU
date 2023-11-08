#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-09-25
#-------------------------------------------------------------------------------

import numpy as np
from numpy.polynomial.polynomial import polyval

polyval(1, [1,2,3])

a = np.arange(4).reshape(2,2)
print("\n a = ", a )

b = polyval(a, [1,2,3])
print("\n b = ", b )
c = np.arange(4).reshape(2,2) # multidimensional coefficients
print("\n c = ", c )

d = polyval([1,2], c, tensor=True)
print("\n d = ", d )

e = polyval([1,2], c, tensor=False)
print("\n e = ", e )
