#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-07-06
#-------------------------------------------------------------------------------

import re

# 전체 스트링의  matching을 위해서는 matching이 시작되는 지점이
# string의 처음과 끝임을 명시해야 한다. ^는 string의 처음, $은 끝.
# 이것이 없으면 text의 일부분과 matching이 되어도 true가 된다.

preal =  r"^[+-]?[0-9]*\.[0-9]+$"
pint2 =  r"[-+]?[0-9]+"
pint  =  r"^[-+]?[0-9]+$"
pexp  =  r"^[-+]?[0-9]*\.?[0-9]+[eE][-+]?[0-9]+$"

def strnum( s ):
    a=0
    if re.match(pint,  s) : return("int")
    if re.match(preal, s) : return("float")
    if re.match(pexp,  s) : return("expon")
    return("none")

lnum=[ '-32', '+78.9030', '13.45', 'good', '100top', '134.45e10', '100E-23', '.8909' ]

for w in lnum :
    print( w, "= ", strnum(w))

a= re.match( pint2, "-345.6789")
print(a.group())

a= re.match( pint, "-345.6789")
print(a)




