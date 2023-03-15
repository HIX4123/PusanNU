
import fractions

a = fractions.Fraction(1,3)
b = fractions.Fraction(2,7)
c = fractions.Fraction(3,5)
d = fractions.Fraction(4,11)
s = a + b + c
print(f"a+b+c = {s}")

s = s - 2*d
print(f"a+b+c-2d = {s}")

print(f"s*s - s = {s*s - s }")