
import re

preal =  r"^[+-]?[0-9]*\.[0-9]+$"
pint  =  r"^[-+]?[0-9]+$"
pexp  =  r"^[-+]?[0-9]*\.?[0-9]+[eE][-+]?[0-9]+$"

def strnum( s ):
    a=0
    if re.match(pint,  s) : a=1
    if re.match(preal, s) : a+=10
    if re.match(pexp,  s) : a+=100
    return(a)

lnum=[ '-32', '+78.9030', '13.45', '100top', '134.45e10', '100E-23', '.8909' ]

for w in lnum :
    print( w, "= ", strnum(w))



