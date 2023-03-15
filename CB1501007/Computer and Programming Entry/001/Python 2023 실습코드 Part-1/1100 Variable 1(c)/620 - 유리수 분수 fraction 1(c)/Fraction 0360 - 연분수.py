#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

# ( 1 2 ( 3 4 ( 5 6 7 ) )
import fractions

a = 5 + fractions.Fraction(6, 7)
b = 3 + fractions.Fraction(4 ,a)
c = 1 + fractions.Fraction(2 ,b)
print(c)

a = 3 + fractions.Fraction(7, 5)
b = 1 + fractions.Fraction(11,a)
c = 3 + fractions.Fraction(4, 5)
d = 4 + fractions.Fraction(c, b)
print(d)


a = 1 + fractions.Fraction(2, 3)
print(a)