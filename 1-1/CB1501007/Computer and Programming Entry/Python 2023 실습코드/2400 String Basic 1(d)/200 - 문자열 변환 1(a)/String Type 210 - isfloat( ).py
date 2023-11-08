#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-10-16

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


print(isfloat("56.8"))                      #Flase
print(isfloat(""))                      #Flase
print(isfloat("1234567"))               #True
print(isfloat("NaN"))                   #True            nan is also float
print(isfloat("NaNananana BATMAN"))     #False
print(isfloat("123.456"))               #True
print(isfloat("123.E4"))                #True
print(isfloat(".1"))                    #True
print(isfloat("1,234"))                 #False
print(isfloat("NULL"))                  #False           case insensitive
print(isfloat(",1"))                    #False
print(isfloat("123.EE4"))               #False
print(isfloat("6.523537535629999e-07")) #True
print(isfloat("6e777777"))              #True            This is same as Inf
print(isfloat("-iNF"))                  #True
print(isfloat("1.797693e+308"))         #True
print(isfloat("infinity"))
print(isfloat("infinity and BEYOND"))   #False
print(isfloat("12.34.56"))              #False           Two dots not allowed.
print(isfloat("#56"))                   #False
print(isfloat("56%"))                   #False
print(isfloat("0E0"))                   #True
print(isfloat("x86E0"))                 #False
print(isfloat("86-5"))                  #False

print(isfloat("+1e1^5"))
