
# yield( )는 iterator를  돌려주는 것으로 일반적인 return과는 다르다.
# 1. for 문이 실행되며, 먼저 generator 함수가 호출된다.
# 2. generator 함수는 일반 함수와 동일한 절차로 실행된다.
# 3. 실행 중 while 문 안에서 yield 를 만나게 된다. 그러면 return 과 비슷하게 함수를 호출했던 구문으로 반환하게 된다. 여기서는 첫번재 i 값인 0 을 반환하게 된다. 하지만 반환 하였다고 generator 함수가 종료되는 것이 아니라 그대로 유지한 상태이다.
# 4. x 값에는 yield 에서 전달 된 0 값이 저장된 후 print 된다. 그 후 for 문에 의해 다시 generator 함수가 호출된다.
# 5. 이때는 generator 함수가 처음부터 시작되는게 아니라 yield 이후 구문부터 시작되게 된다. 따라서 i += 1 구문이 실행되고 i 값은 1로 증가한다.
# 6. 아직 while 문 내부이기 때문에 yield 구문을 만나 i 값인 1이 전달 된다.
# 7. x 값은 1을 전달 받고 print 된다. (이후 반복)


def generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

for x in generator(5):
    print("generating= ", x)


for x in [0,1,2,3,4]:
    print(" List element= ", x)




