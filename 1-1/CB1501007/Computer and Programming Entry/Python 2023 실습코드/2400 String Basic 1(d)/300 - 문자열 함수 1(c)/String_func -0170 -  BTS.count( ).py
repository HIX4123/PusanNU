BTS="""
모든 게 궁금해 how's your day
Oh tell me (oh yeah yeah, ah yeh ah yeh)
뭐가 널 행복하게 하는지
Oh text me (oh yeah yeah, ah yeh ah yeh)
Your every picture
내 머리맡에 두고 싶어 oh bae
Come be my teacher
네 모든 걸 다 가르쳐줘
Your one, your two
Listen my my baby 나는
저 하늘을 높이 날고 있어
(그때 니가 내게 줬던 두 날개로)
이제 여긴 너무 높아
난 내 눈에 널 맞추고 싶어
Yeah you makin' me a boy with love
Oh my my my, oh my my my
I've waited all my life
네 전부를 함께하고 싶어
Oh my my my, oh my my my
Looking for something right
이제 조금은 나 알겠어
than a moment, than a moment, love
(Ooh ah ooh ah ooh ah ooh ah ah) I have waited longer
(Ooh ah ooh ah ooh ah ooh ah ooh)
For a boy with, for a boy with love
널 알게 된 이후 ya 내 삶은 온통 너 ya
사소한 게 사소하지 않게 만들어버린 너라는 별
(Oh yeah) 하나부터 열까지 ay ay 모든 게 특별하지 ay ay
너의 관심사 걸음걸이 말투와
사소한 작은 습관들까지 (oh ah)
Ay 다 말하지 너무 작던 내가 영웅이 된 거라고 (oh nah)
난 말하지 운명 따윈 처음부터 내 게 아니었다고 (oh nah)
세계의 평화 (no way)
거대한 질서 (no way)
그저 널 지킬 거야 난 (boy with love)
Listen my my baby 나는
저 하늘을 높이 날고 있어
(그때 니가 내게 줬던 두 날개로)
이제 여긴 너무 높아
난 내 눈에 널 맞추고 싶어
Yeah you makin' me a boy with love
Oh my my my, oh my my my
You got me high so fast
네 전부를 함께하고 싶어
Oh my my my, oh my my my
You got me fly so fast
이제 조금은 나 알겠어
than a boy with love
(Ooh ah ooh ah ooh ah ooh ah ah) love is nothing stronger
(Ooh ah ooh ah ooh ah ooh ah ooh) (than a boy with) than a boy with love
툭 까놓고 말할게
나도 모르게 힘이 들어가기도 했어
높아버린 sky, 커져버린 hall
때론 도망치게 해달라며 기도했어
But 너의 상처는 나의 상처
깨달았을 때 나 다짐했던걸
니가 준 이카루스의 날개로
태양이 아닌 너에게로
Let me fly
Oh my my my, oh my my my
I've waited all my life
네 전부를 함께하고 싶어
Oh my my my, oh my my my
Looking for something right
이제 조금은 나 알겠어
than a moment, than a moment, love
(Ooh ah ooh ah ooh ah ooh ah ah) love is nothing stronger
(Ooh ah ooh ah ooh ah ooh ah ooh) (than a boy with) than a boy with love
"""

print(f"BTS 가사 길이= {len(BTS)}")
my_count = BTS.count("my")
print(f" my_count= { my_count}")

my_count = BTS.count("my", 1, len(BTS)//2 )
print(f" my_count 반 = { my_count}")


my_count = BTS.count("my", -700, -1 ) # 뒤에서 700번 문자까지.
print(f" 거꾸로 my_count 반 = { my_count}")