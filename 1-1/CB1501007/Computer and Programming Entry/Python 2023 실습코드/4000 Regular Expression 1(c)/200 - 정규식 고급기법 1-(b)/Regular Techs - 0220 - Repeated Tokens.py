

import re

bts="""
모든 게 궁금해 how's your day
Oh tell me (oh yeah yeah, ah yeh ah yeh)
뭐가 널 행복하게 하는지
Oh text me (oh yeah yeah, ah yeh ah yeh)
Your every picture
내 머리맡에 두고 싶어 oh bae
Come be my teacher
네 모든 걸 다 가르쳐줘 네 모든
걸 다 가르쳐줘 with love
with love
Oh my my my, oh my my my
I've waited all my life
네 전부를 함께하고 싶어
Oh my my my, oh my my my
Looking for something right
이제 조금은 나 알겠어
than a moment, than a moment, love
(Ooh ah ooh ah ooh ah ooh ah ah) I have waited longer
(Ooh ah ooh ah ooh ah ooh ah ooh)
"""

#\1은 group(1)을 말한다.


# \1은 앞에서 matching된 단어를 이어받음
print("\n 특정 단어가 연이어 나타나는 경우")
out = re.finditer( r'(\b[\w]+)\s+\1',  bts )
for w in out :
    print(w.span(), w.group() )

print("\n 특정 구절이 연이어 나타나는 경우")
out = re.finditer( r'(\b[\w ]+)\s+\1',  bts, re.DOTALL )
for w in out :
    print(w.span(), w.group() )

print("\n 줄을 건너 특정 구절이 연이어 나타나는 경우")
out = re.finditer( r'(\b[\w \n]+)\s+\1',  bts )
for w in out :
    print(w.span(), w.group() )




