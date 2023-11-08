#!/usr/bin/python3

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


Strings = [ "345", "0.234", "56.7", "Good", "454", "4.5e+10"]


for w in Strings :
    if isfloat(w) :
        print( float(w) )

