#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import datetime
import time

print ( time.strptime() )

x1 = time.strptime('00:01:00,000'.split(',')[0],'%H:%M:%S')
x2 = time.strptime('00:01:14','%H:%M:%S')
x3 = datetime.timedelta(hours=x1.tm_hour,minutes=x1.tm_min,seconds=x1.tm_sec).total_seconds()

print(x1)
print(x2)
print(x3)


