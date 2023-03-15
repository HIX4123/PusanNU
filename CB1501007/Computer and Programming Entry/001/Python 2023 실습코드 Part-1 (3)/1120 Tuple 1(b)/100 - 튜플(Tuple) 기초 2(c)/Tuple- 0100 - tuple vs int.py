# 다양한 tuple-related 변수들

t0 = (20)
t1 = (20, )
t2 = {20, 33}  # brace
t3 = ( )        # empty tuple
t4 = 41, 42, 43, 44
t5 = { 32:"삼십2", 99:"구십구 " }
t6 = ( (1,2,3), (10,20,30), -100 )


L=[ t0, t1, t2, t3, t4, t5, t6]

for w in L :
    print( type(w))

"""
immutable(생성, 이후에는 수정이 불가능), mutable(수정가능)
"""