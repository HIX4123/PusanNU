#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-27
#-------------------------------------------------------------------------------

## numpy.polynomial.polynomial.polydiv(c1, c2)[source]
## Divide one polynomial by another.
##
## Returns the quotient-with-remainder of two polynomials c1 / c2. The arguments are sequences of coefficients, from lowest order term to highest, e.g., [1,2,3] represents 1 + 2*x + 3*x**2.
##
##
## Parameters:
## c1, c2 : array_like
## 1-D arrays of polynomial coefficients ordered from low to high.
##
## Returns:
## [quo, rem] : ndarrays
## Of coefficient series representing the quotient and remainder.
##


from numpy.polynomial import polynomial as P
c1 = (1,2,3)
c2 = (3,2,1)

print(P.polydiv(c1,c2) )
#(array([3.]), array([-8., -4.]))


print(P.polydiv(c2,c1))
#(array([ 0.33333333]), array([ 2.66666667,  1.33333333])) # may vary
