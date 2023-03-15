
# 튜플 선언
tuple1 = (1,2,3,4,5)
print(type(tuple1) )
print("tuple1=", tuple1)

# 인덱싱이나 슬라이싱을 이용해서 변경
# tuple + tuple + tuple 자료형 일치

tuple2 = tuple1[0:2]+(10,)+tuple1[2:]
print("tuple2=", tuple2)

nullt= tuple() # 빈 튜플 만들기


