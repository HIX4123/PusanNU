##dtype 접두사
##
##설명
##
##사용 예
##
##
## b 불리언 b (참 혹은 거짓)
## i 정수 i8 (64비트)
## u 부호 없는 정수 u8 (64비트)
## f 부동소수점 f8 (64비트)- 디폴트
## c 복소 부동소수점 c16 (128비트)
## O 객체 0 (객체에 대한 포인터)
## S 바이트 문자열 S24 (24 글자)
## U 유니코드 문자열 U24 (24 유니코드 글자)

import numpy as np


a = np.zeros(5)
print("\n 1. a=", a)


b = np.zeros((2, 3))
print("\n 2. b=",b)
print("\n 3. b.dtype", b.dtype)

c = np.zeros((5, 5), dtype="i")
print("\n 4. c=",c)
print("c[3][4]=", c[3][4])


d = np.zeros(5, dtype="U")
print(d)

e = np.ones((2, 3, 4), dtype="i8")
print(e)

print(np.arange(3, 21, 2))  # 시작, 끝(포함하지 않음), 단계
