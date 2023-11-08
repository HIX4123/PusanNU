

import datetime

now = datetime.datetime.now()
print(now)  # 2020-06-04 09:41:19.792114

nowDate = now.strftime( '%Y-%m-%d')
print('out1 = ', nowDate)      # 2020-05-28

nowTime = now.strftime('%H:%M:%S')
print('out2 = ', nowTime)      # 12:11:32

nowTime = now.strftime('%H시 %M분 %S초')
print('한국식으로  = ', nowTime)      # 12:11:32

# string formatted time

nowTime = now.strftime('%Y년 %m월 %d일')
print('out4 = ', nowTime)      # 12:11:32

nowDatetime = now.strftime( '%Y-%m-%d %H:%M:%S')
print('out3 = ', nowDatetime)  # 2020-05-28 12:11:32