#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-04
#-------------------------------------------------------------------------------

import datetime

myDatetime = datetime.datetime.strptime('2020-06-03 12:11:32', '%Y-%m-%d %H:%M:%S')
print(myDatetime)

yourDatetime = myDatetime.replace(day=27)
print(myDatetime)   # 2020-06-03 12:11:32
print(yourDatetime) # 2020-06-27 12:11:32