#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import time

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print (time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))

# Time intervals are floating-point numbers in units of seconds. Particular
# instants in time are expressed in seconds since 12:00am, January 1, 1970(epoch).
ticks = time.time()
print( "\n 1. Number of ticks since 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print ("\n 2. Local current time :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print( "\n 3. Local current time :", localtime)

from datetime import datetime

# 1/1000초로 측정하기 위하여.
# [:-3] => Removing the 3 last characters as %f is for microsecs.
print("\n 4.", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])



