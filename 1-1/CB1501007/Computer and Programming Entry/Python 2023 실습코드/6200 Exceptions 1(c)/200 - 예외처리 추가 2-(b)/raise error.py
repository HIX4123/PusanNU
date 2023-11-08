#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------
class NameShortError(ValueError):
    pass

def valida(name):
    if len(name) < 5 :
        raise NameShortError(name)
    else :
        print("Good name=", name)


valida("Good boy")

valida("Good")