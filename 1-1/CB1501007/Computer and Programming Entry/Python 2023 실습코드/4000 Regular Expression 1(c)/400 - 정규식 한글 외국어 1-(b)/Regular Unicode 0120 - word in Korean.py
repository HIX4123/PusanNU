
# 파이썬 정규식 한글처리 관련
# 한글 코드 범위
# ㄱ ~ ㅎ: 0x3131 ~ 0x314e
# ㅏ ~ ㅣ: 0x314f ~ 0x3163
# 가 ~ 힣: 0xac00 ~ 0xd79f

# 문장을 나누거가, 의문문을 찾을 때

import re

text = """
프로그램 오류를 찾아 고치는 디버깅 debugginh
작업은 소프트웨어 개발에서 아주 중요한 과정이다.
시스템에 문제가 생긴다고     ? 일단 그 문제가 정말 ‘확실’한 것인지 반복해 확인해야 한다.
오류가 나면 보통 디버거(debugger)라는 특별한 (프로그램)을 사용해서 메모리에
저장된 값을 추적해야 한다.  뭐라꼬?
디버거는 내시경, 실시간 CT 같은 것이다.
"""

print( re.findall( r"\b\w+\b", text ) ) # 어절 찾기
print( re.findall( r"\(\w+\b\)", text ) ) # (어절)
print( re.findall( r"\b\w+\.", text ) )
print( re.findall( r"\b\w+[ ]*\?", text ) )
