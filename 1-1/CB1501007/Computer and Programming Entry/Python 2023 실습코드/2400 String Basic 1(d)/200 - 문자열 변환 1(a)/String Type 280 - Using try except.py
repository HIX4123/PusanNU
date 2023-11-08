#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-10-16
#-------------------------------------------------------------------------------

L = [ '34', '56.7', 'good', "500", '45summer' ]
Q = [ ]
for w in L :
    try:
        Number = float(w)
        print (Number)
    except:
        print ("Error! Not a float!")
    try:
        Number = int(w)
        print (Number)
    except:
        print ("Error! Not an integer!")
    try:
        Number = alpha(w)
        print (Number)
    except:
        print ("Error! Not a float!")

