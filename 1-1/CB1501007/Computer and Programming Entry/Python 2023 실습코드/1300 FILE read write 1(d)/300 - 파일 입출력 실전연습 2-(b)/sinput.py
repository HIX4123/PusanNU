#-*- coding: cp949 -*-
#-------------------------------------------------------------------------------
# Purpose:     2018 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


import fileinput

for idx, line in enumerate(fileinput.input()):
    print "i= ", idx, ": ", line