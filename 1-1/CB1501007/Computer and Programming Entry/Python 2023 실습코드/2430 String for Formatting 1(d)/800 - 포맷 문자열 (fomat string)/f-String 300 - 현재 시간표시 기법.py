

import datetime

date = datetime.datetime.now()
print("  쌩(raw) date 문자열=", date )

# 반드시 { } 안에 표시해야 함.
mys = f' {date:%Y에서 %m월이고 날짜는 %d일} is on a {date:%A}'
print(mys)


print(f'시간은 {date:%H}')
print(f'분은 {date:%M}')
print(f'초(second)는  {date:%S}')

"""
%Y 해, year
%m 달
%d 날
%H 는 Hour
%M은 분
%S 는 초
"""