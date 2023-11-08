#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-04
#-------------------------------------------------------------------------------

import datetime

now = datetime.datetime.now()
print(now)  # 2020-06-04 09:41:19.792114

nowDate = now.strftime('%Y-%m-%d')
print(nowDate)      # 2020-05-28

nowTime = now.strftime('%H:%M:%S')
print(nowTime)      # 12:11:32

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)  # 2020-05-28 12:11:32