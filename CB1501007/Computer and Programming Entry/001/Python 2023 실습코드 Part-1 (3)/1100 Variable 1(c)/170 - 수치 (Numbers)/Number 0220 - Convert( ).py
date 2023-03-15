

Num = "45 -90  23.45 -90.5  3.14e+6 -90.45e-9".split( )

for w in Num :
    if "." in w : value = float(w)
    else        : value = int(w)
    print( value )