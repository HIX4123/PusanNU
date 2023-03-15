
# 튜플 선언
tuple1 = (1,2,3,4,5)
print(type(tuple1) )
print("tuple1=", tuple1)

# 튜플은 직접적으로 요소 변경 불가능
# tuple[2] = 10 #ERROR!!
# 인덱싱이나 슬라이싱을 이용해서 변경



tuple2 = tuple1[0:2]+(10,)+tuple1[2:]
print("tuple2=", tuple2)

nt=()
for w in range(10):
    nt = nt + (w,)
    print(f"nt={nt}")


