#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-07-06
#-------------------------------------------------------------------------------

abin =  0b10100
lnum=[ '32', '13.45', 100, abin , 0x9abc7, 0o340723, "Summer", ]

for w in lnum :
    print( "Type(", w, ")=", type(w))

print( "Type(", abin, ")=", type(abin))

x = 12
print( isinstance(x, int) )
y = 12.0
print( isinstance(y, float) )


print( isinstance( 45.001, (int, float)) )

a= int('9034')
print(a*100)
a= float('90.34')
print(a*100)
