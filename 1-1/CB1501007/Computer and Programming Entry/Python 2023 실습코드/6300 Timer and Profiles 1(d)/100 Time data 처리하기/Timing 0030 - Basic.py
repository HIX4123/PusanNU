#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

from datetime import datetime

dt = datetime(2023, 2, 20, 13, 35, 42, 123456)
#            Year  Mon Day H   M    S   microsecond

result = dt.strftime("%Y년 %m월 %d일 %H시 %M분 %S.%f초")

print("> 문자열 변환 전 형식 : ", type(dt))
print(f" result = {result}")
print("> 문자열 변환 후 출력 : ", dt      )
print("> 문자열 변환 후 형식 : ", type(result))
print("> 문자열 변환 후 출력 : ", result)
