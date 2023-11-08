#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

# convert string into date time format.
import datetime


str_date = '2016-10-06 15:14:54.322989'
str_date = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
d_date = datetime.datetime.strptime(str_date , '%Y-%m-%d %H:%M:%S.%f')
print(d_date)
print(type(d_date)) # check d_date type.


# convert date time to regular format.

reg_format_date = d_date.strftime("%d %B %Y %I:%M:%S %p")
print(reg_format_date)

# some other date formats.
reg_format_date = d_date.strftime("%Y-%m-%d %I:%M:%S %p")
print(reg_format_date)
reg_format_date = d_date.strftime("%Y-%m-%d %H:%M:%S")
print(reg_format_date)


(dt, micro) = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S.%f').split('.')
dt = "%s%03d" % (dt, int(micro) / 1000)
print ("2. dt ", dt)