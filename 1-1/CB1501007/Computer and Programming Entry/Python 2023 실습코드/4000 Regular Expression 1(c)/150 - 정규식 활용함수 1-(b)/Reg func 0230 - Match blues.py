
# match( )는 첫번째 match를 찾아준다.
# 만일 multiple line인 경우에는 첫 라인에 없을 경우
# None을 돌려준다.

import re

st="""summertime blues: lyric
I'm gonna raise a fuss, I'm gonna raise a holler
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

p1= r"홀로[ \w]+싶어"
p1= r"\w{5,}"

out = re.match( p1, st )
if out :
    print("In", out.group() )
else :
    print("None match( )" )


