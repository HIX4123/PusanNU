
myb = bytes(10)    # 0이 10개 들어있는 바이트 객체 생성
print("myb=", myb)

listb= bytes([10, 20, 30, 40, 50])    # 리스트로 바이트 객체 생성
print("listb=", listb, type(listb))

qb = bytes(b'hello')    # 바이트 객체로 바이트 객체 생성
print("qb= ", qb)

"""
bytearray도 1바이트 단위의 값을 연속적으로 저장하는 시퀀스 자료형인데,
bytes와 차이점은 요소를 변경할 수 있느냐의 차이다.
bytes는 요소를 변경할 수 없고, bytearray는 요소를 변경할 수 있다.

•bytearray(): 빈 바이트 배열 객체를 생성
•bytearray(길이): 정해진 길이만큼 0으로 채워진 바이트 배열 객체를 생성
•bytearray(반복가능한객체): 반복 가능한 객체로 바이트 배열 객체를 생성
•bytearray(바이트객체): 바이트 객체로 바이트 배열 객체를 생성

다음은 바이트 배열 객체의 첫 번째 요소를 변경합니다.

"""

x = bytearray(b'hello')
x[0] = ord('a')    # ord는 문자의 ASCII 코드를 반환
print("x=", x)
qb = bytearray(b'aello')
print("qb= ", qb)

# 파이썬에서 문자열( str)의 기본 인코딩은
# UTF-8인데, b'hello'와 같이 문자열을 바이트 객체로 만들면 각 문자를 ASCII 코드로 저장합니다. 보통 문자열을 UTF-8이 아닌 ASCII 코드로 처리하고 싶을 때 바이트 객체를 사용합니다.
# 문자열(str)을 바이트 객체로 바꾸려면
# encode 메서드를 사용합니다. •문자열.encode()


qa = 'hello'.encode()     # str을 bytes로 변환
print("qa = ", qa)


x = '안녕'.encode('euc-kr')
print("another x = ",  x.decode('euc-kr')    )
y = '안녕'.encode('utf-8')
q = y.decode('utf-8')
print("q=", q)
