
import fractions

bunsu=[]

for i in range(3,11) :
    for j in range(3,11):
        bunsu.append( fractions.Fraction(i,j))


bunsu.sort()

for i,w in enumerate(bunsu) :
    print( f'i= {i:2} :  {w.numerator:2}/{w.denominator}')
    #                        분자           분모