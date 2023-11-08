#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-04
#-------------------------------------------------------------------------------

# datetime.strptime(date_string, format)
# time.strptime(time_string[, format])

from datetime import datetime

datetime_str = '06/05/20 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

print(type(datetime_object))
print(datetime_object)  # printed in default format



