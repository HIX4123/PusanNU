
def cmp(a, b):
    return (a > b) - (a < b)

def sign(a):
    return (a > 0) - (a < 0)


L=[ 5, -87, 12.34, 0, 0.0, -0.89, 0.63e3, -5.6e-3 ]

print("\n Using sign(a)")
for w in L :
    print( f'Number= {w:12}, sign={sign(w):3}')



