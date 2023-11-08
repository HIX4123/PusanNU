#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-05-03
#-------------------------------------------------------------------------------


s = 'I would like 1.5 cookies 456.78 please'

for i in s.split():
    try:
        result = float(i) # i를 float로 바꾸려고 함
        print(f" float을 찾음 = { result } ")
    except:
        print(f" float이 아니구먼")
        continue

