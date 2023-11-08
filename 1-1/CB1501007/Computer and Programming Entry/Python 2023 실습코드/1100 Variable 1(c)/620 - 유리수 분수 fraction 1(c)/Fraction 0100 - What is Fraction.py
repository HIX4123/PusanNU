#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-01-19
#-------------------------------------------------------------------------------


from fractions import Fraction
from decimal import Decimal

a = Fraction(16, -10)
b = Fraction(-8, 5)
c = Fraction(123)
d = Fraction()
e = Fraction(0, 1)
f = Fraction('3/7')
print(a,b,c,d,e,f)

a = Fraction(' -3/7 ')
b = Fraction('1.414213')
c = Fraction(1414213, 1000000)
d = Fraction(-1, 8)
e = Fraction('7e-6')
f = Fraction(7, 1000000)
print(a,b,c,d,e,f)

a = Fraction(2.25)
b = Fraction(9, 4)
c = Fraction(1.1)
d = Fraction(Decimal('1.1'))
e = Fraction(11, 10)
#   Fraction(3.4, 5 ) 오류
f = Fraction( 12.3)
print(a,b,c,d,e,f)
