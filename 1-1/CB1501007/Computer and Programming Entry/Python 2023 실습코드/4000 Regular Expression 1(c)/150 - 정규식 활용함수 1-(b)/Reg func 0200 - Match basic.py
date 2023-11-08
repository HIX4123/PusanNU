# match( )는 주어진 문자열의 처음부터 시작하여 비교를 한다.
# 이 첫번째 match가 있는 경우 이것을 확인해서 true로 돌려준다.
# 만일 multiple line인 경우에는 첫 라인에 없을 경우
# None을 돌려준다. 따라서 조심해야 한다.

import re

st = """summertime blues: lyric I'mgonna raise a fuss, I'm gonna raise a holler
About a-workin' all summer just to try to earn a dollar
Every time I call my baby, try to get a date
My boss says, "no dice son, you gotta work late"
Sometimes I wonder what I'm a-gonna do
But there ain't no cure for the summertime blues

Well, my mom and pop told me, "son, you gotta make some money"
If you want to use the car to go ridin' next Sunday
Well, I didn't go to work, told the boss I was sick
"Well, you can't use the car 'cause you didn't work a lick"
Sometimes I wonder what I'm a gonna do
But there ain't no cure for the summertime blues
I'm gonna take two weeks,…
"""

p2 = r"홀로[ \w]+싶어"
p1 = r"\w{5,}"

out = re.match(p1, st)
if out:
    print("In", out.span(), out.group())
else:
    print("None match( )")


out = re.match(p1, st[out.end() + 1 :])  # 다음 match, string의 범위를 점함.
if out:
    print("In", out.span(), out.group())
else:
    print("None match( )")
