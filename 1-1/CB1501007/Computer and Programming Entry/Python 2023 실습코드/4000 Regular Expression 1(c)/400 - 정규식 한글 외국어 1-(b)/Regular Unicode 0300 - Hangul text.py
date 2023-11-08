
# 파이썬 정규식 한글처리 관련
# 한글 코드 범위
# ㄱ ~ ㅎ: 0x3131 ~ 0x314e
# ㅏ ~ ㅣ: 0x314f ~ 0x3163
# 가 ~ 힣: 0xac00 ~ 0xd79f

import re

text = """
안철수 국민의당 "상임공동대"표가 최근 "지하철" 스크린도어 수리 중 숨진 19세
노동자에 대해 "여유가 있었더라면 덜 위험한 일을 택했을 것"이라고 밝혀
논란을 빚고 있다. ㅎㅎㅎㅎ 안 대표는 발언을 뒤늦게 수정했지만 비판은 이어지고 있다.
안 대표는 지난 30일 밤 자신의 "사회관계망서비스(SNS)에 추모글을" 올려
"20살도 채 되지 않은 젊은이가 사고로 목숨을 잃었다. 수많은 사람의 안전을
지키는 일을 하다가 당한 ㅋㅋㅋㅋ 참담한 일"이라고 위로했다.
그러나 이어 "가방 속에서 나온 컵라면이 마음을 더 아프게 한다"며 "조금만
더 여유가 있었더라면 덜 위험한 일을 택했을지도 모른다"고 했다.
이 대목을 두고 누리꾼들의 비판이 쏟아졌다. 정준영 전 청년유니온
정책국장은 자신의 SNS 글을 통해 "여유라고는 느낄 수 없는 절박함 속에서 누군가가
선택한 ‘가장 나쁜 일자리’여도 일하다 목숨을 잃는 일은 없어야 한다"며
"조금 더 여유를 가지고 찾아보았을" ‘덜 위험한 일’이란 "도대체 무엇이냐"고 지적했다.
"""

hangul = re.compile('[\uac00-\ud79f]+') # [가-힣] 까지 모든 한글
vowel  = re.compile('[\u314f-\u3163]+') # 한글 모음
jung   = re.compile('\uC815[\uac00-\ud79f]+') # '정'으로 시작하는 단어
conso  = re.compile('[\u3131-\u314e]+') #  한글 자음
quote  = re.compile('\"(.+)\"') # 인용문의 내부 문제
inner  = re.compile('\".+?\"') # 인용문 전체, 가장 짧게 matching, 처음 매칭부분
greedy = re.compile('\".+\"') # 인용문 전체, 가장 갈게, 최대한 매칭 시키기

a = hangul.findall(text)
b =  jung.findall(text)
c =  quote.findall(text)
d =  conso.findall(text)
e =  inner.findall(text)



print("\n----정으로 시작하는 단어 ------")
for word in b :
    print(word)

print("\n---- 인용문 내부 ------")
for word in c :
    print(word)

print("\n----자음 문자------")
for word in d :
    print(word)

print("\n----인용문 전체 -----")
for word in e :
    print(word)

# 한글의 unicode를 출력하려면
# Console에서 다음과 같이 하면 된다.
# >> u'똥'
# >> u'대한민국'
