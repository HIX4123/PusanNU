#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-08-31
#-------------------------------------------------------------------------------

# 파이선 bytearray 오브젝트 (bytearray object in Python)
# 파이선의 bytearray는 바이트 값을 저장하는 버퍼 오브젝트이다. 파이선으로 디바이스를 다루는 코드를 다루다 보면 bytearray를 자주 접하게 되기 때문에 이에 대해 간단하게 정리해 놓았다. bytearray는 원래 파이선3에서 처음 도입되었는데 파이선2.7에 백워드 포팅 되었다.

# - 리스트에서 bytearray 만들기


elements = [0, 200, 50, 25, 10, 255]
values = bytearray(elements)
print("value=",  values )
bytearray(b'\x00\xc82\x19\n\xff')

# bytearray의 element를 변경
values[0] = 5
values[1] = 0

# bytearray는 mutable 오브젝트이므로 element의 값을 변경할 수 있다.
# bytearray의 내용 출력

for v in values:
    print("v in value =", v)


# 일반 리스트와 동일하게 iterate 할 수 있다.
#- 문자열로 bytearray 만들기

data = bytearray(b"abc")
print("data=", data)

for d in data:
    print("d in data",d)


# 문자열로 bytearray를 만들때는 문자열 앞에 ‘b’를 붙여줘야 한다.
# bytearray slice

values = [5,10,15,20]
arr = bytearray(values)
print("arr= ", arr )
print("arr[0:2]= ", arr[0:2])


for v in arr:
    print("v in arr= ", v)


