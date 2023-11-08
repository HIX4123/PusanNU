#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-08-31
#-------------------------------------------------------------------------------



# 리스트와 동일하게 bytearray를 slice 할 수 있고, mutable이기 때문에 slice의 내용을 변경할 수도 있다.
#  Occurence Count

arr = bytearray(b"aabbcccc")
print("Test1 =", arr.count(b"c") )

# bytearray내의 각 element를 돌며 특정 패턴이 매치하는 횟수를 셀 수도 있다. count()의 argument는 byte 오브젝트여야만 한다. 즉 ‘b’로 시작하는 문자열 스트링이거나 0~255 사이의 정수값이어야 한다.
# Find pattern

data = bytearray(b"python")
print("data.find(b'on')=", data.find(b"on"))
print("data.find(b'java')=", data.find(b"java"))



# bytearray 내에서 특정 문자열을 검색할 수도 있다. 이 경우 일치되는 문자열의 가장 왼쪽 인덱스를 리턴한다. 일치되는 문자열이 없으면 -1을 리턴한다.
# In operator

data = bytearray([100,20,10,200,200])
print("data2 = ", data )

print(" 200 in data = ",  200 in data )
print(" 0 in data = ",  0 in data )

# Merge

left = bytearray(b"Hello ")
right = bytearray(b"World")
print("left + right=", left+right  )



#- bytearray를 list로 변환




init = [100,255,255,0]
b = bytearray(init)
print(" b= ", b)

result = list(b)
print("result=", result)

# byte값들의 리스트 (0~255 사이의 숫자)는 bytearray로 변환할 수 있다. 반대로 bytearray를 list로 변환도 가능함




# Append, del, insert

vals = bytearray()
vals.append(0)
vals.append(1)
vals.append(2)

print("vals=", vals )

del vals[0:1]
print("after del -> vals=", vals )

vals.insert(1,3)
print("after insert -> vals=", vals )


