#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

def time2float( s ):
    ftr = [3600,60,1]
    floats = [float(x) for x in s.split(':')]
    print( floats )
    return( floats[0]*3600.0 + floats[1]*60.0 + floats[2])

timestr = '00:04:23.12'

print( time2float( timestr ))

