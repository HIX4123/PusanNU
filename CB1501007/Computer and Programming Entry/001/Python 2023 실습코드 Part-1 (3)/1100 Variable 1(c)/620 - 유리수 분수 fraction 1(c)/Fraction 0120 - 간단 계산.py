
import fractions

a = fractions.Fraction(12,23)
b = fractions.Fraction(17,a)
c = fractions.Fraction(-5,b)

print(c)
print(a+b)


x= fractions.Fraction(12,23)
y= fractions.Fraction(9, 17)
print(" x+y= ", x+y )

print( f' 결과= {float(x+y)*391:12.8f}')