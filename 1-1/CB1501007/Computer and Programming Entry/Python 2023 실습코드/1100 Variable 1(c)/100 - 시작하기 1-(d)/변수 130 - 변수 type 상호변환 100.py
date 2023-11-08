#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-07-06
#-------------------------------------------------------------------------------


abin =  0b10100
lnum=[ '32', '13.45', 100, abin , 0x9abc7, 0o340723, "Summer", ]

for w in lnum :
    print( "Type(", w, ")=", type(w))

a = int('0b101010', 2)
b = int('0o52', 8)
c = int('0x2a', 16)

print("a,b,c=", a, b, c)

a,b,c,d,e=format(42, 'b'), format(42, 'o'), format(42, 'x'), format(42, 'X'), format(42, 'd')
print("a,b,c,d,e=", a,b,c,d,e)

