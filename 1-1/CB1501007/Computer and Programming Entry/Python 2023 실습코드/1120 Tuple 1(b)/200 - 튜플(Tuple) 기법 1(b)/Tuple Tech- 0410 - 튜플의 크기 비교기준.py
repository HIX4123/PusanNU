# 리스트는 그 값을 생성, 삭제, 수정이 가능하지만
# 튜플은 그 값을 변화시킬 수 없다. 절대로.... 이것이 강점
# 얼핏 보면 튜플과 리스트는 비슷한 역할을 한다.
#
# 하지만 프로그래밍을 할 때 튜플과 리스트는 구분해서 사용하는것이 유리하다.
# 튜플과 리스트의 가장 큰 차이는 값을 변화시킬 수 있는 지 없는 지의 차이
#
# 리스트의 항목 값은 변화가 가능하고 튜플은 변화가 불가능하다.
# 따라서 프로그램이 진행되는 동안 그 값이 항상 변하지 않기를 바란다면
# 또는 바뀔까 걱정하고 싶지 않다면 주저하지 말고 튜플을 사용해야 할 것이다.
# 이와는 반대로 수시로 그 값을 변화시켜야 할 경우라면 리스트를 사용해야 한다.
# 실제 프로그램에서는 평균적으로 튜플보다는 리스트를 훨씬 많이 쓰게 된다.

t0 = "one", "two", 3, 400, 500  #꼭 괄호를 안쳐도 됩니다.

t1 = ( )
t2 = (1,0)
t3 = (10,20,30)
t4 = 10,20,30, (10,20)
t5 = ('a', 'b', ('ab', 'cd'))


print("t0=", t0, "leng=",len(t0))
print("t1=", t1, "leng=",len(t1))
print("t2=", t2, "leng=",len(t2))
print("t3=", t3, "leng=",len(t3))
print("t4=", t4, "leng=",len(t4))
print("t5=", t5, "leng=",len(t5))


t23 = t2 + t3
print("t2 + t3 = ", t23)

t2x5 = t2 * 5
print("t2*5 = ", t2x5)

if t3 == t4 : print("test1: t3와 t4는 같습니다")
if 20 in t4 : print("test2: 20은 t4 안에 있습니다")
if (10,20) in t4 : print("test3: (10,20)은 t4 안에 있습니다")
else : print("test4: 아니요. (10,20)은 t4에 없습니다")


if (3,4,5) == (3,4,5) : print("test5: 둘은 같은 튜플입니다 ")

if (3,4,5) == (3,5,4) : print("test6: 둘은 같은 튜플입니다 ")
else : print("test7: 아니요. 둘은 다른 튜플입니다")