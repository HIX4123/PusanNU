# python2, python3의 문자열 처리 방법이 다름.

"""
python2은 ascii가 기본,
python3은 unicode가 기본

LINUX와 윈도우의 한글 처리 방법이 다름.

윈도우는 CP949가 기본
LINUX는 euc-kr이 기본.
(.profile에 명기하기 나름이지만, 보통 euc-kr)

웹 세상에서는 utf-8이 기본.
"""


S =   "아름다운_우리_한글을_사랑합니다."
uS = u"아름다운_우리_한글을_사랑합니다."
print("문자열 S의 type()=", type(S))
print("문자열 uS의 type()=", type(uS))
# Python3에서 unicode 차별 없음

print(S[2:7]) # 시작은 2, 7을 넘지않음
for i in range( len(S)) :
    print("S[%2d]= %s " %(i,S[i]))





