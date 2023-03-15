
def cmp(a, b):
    return (a > b) - (a < b)

def sign(a):
    return (a > 0) - (a < 0)


L=[ 5, -87, 12.34, 0, 0.0, -0.89, 0.63e3, -5.6e-3 ]

print("\n Using sing(a)")
for w in L :
    print( f'Number= {w:12}, sign={sign(w):3}')


sign1 = lambda x: -1 if x < 0 else 1 # is 15% faster. Same with
sign2 = lambda x: x and (-1 if x < 0 else 1)

print("\n Using lambda(x)")
for w in L :
    print( f'Number= {w:12}, sign1={sign1(w):3}')

import numpy as np
print("\n Using numpy(x)")
for w in L :
    print( f'Number= {w:12}, np.sign={np.sign(w):3}')
