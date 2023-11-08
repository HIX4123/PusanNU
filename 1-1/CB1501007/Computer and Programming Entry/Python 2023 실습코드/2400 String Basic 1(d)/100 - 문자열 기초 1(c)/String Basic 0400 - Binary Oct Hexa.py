
# Purpose: 이진수(binary) 처리하기


n = 100
binrep = bin(n)[2:] # 스트링에서 2번째 문자부터 끝까지
                    # 앞 부분의 0b를 제거한다.

print("n의 이진표현=", bin(n))
print("n의 이진일부 표현=", binrep)


hexrep = hex(n)
print(hexrep)
print(hexrep[2:])


q = 0b100111010101
r = 0x46abcff1201
w = 0o110275416
print("십진수 표현 = ", q)
print("십진수 표현 = ", r)
print("십진수 표현 = ", w)