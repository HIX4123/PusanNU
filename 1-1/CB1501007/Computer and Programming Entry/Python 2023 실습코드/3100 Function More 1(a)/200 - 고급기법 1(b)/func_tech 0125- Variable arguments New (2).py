#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2021-03-06
#-------------------------------------------------------------------------------

def printinfo( arg1, *vartuple ):
    #"This prints a variable passed arguments"
    print( " arg1 = ", arg1 )
    for var in vartuple:
        print( f' vartuple = {var}')
    return;


# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
printinfo( [70, 60, 50], 5, 6, [9,10], "헐" )